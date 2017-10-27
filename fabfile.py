from fabric.api import env, roles, sudo, execute, put, run, local, lcd, prompt, cd, parallel
import os

env.roledefs = {
    "webserver" : [ "172.31.35.226", "172.31.24.2", "172.31.17.13" ],
    "database" : [ "172.31.117.35", "172.31.112.114" ],
}

env.roledefs["all"] = [h for r in env.roledefs.values() for h in r]

packages_required = {
    "webserver" : [ "httpd", "php", "ntp", "php-myqli" ],
    "database" : [ "mariadb-server" ]
}

download_files = {
    "database" : [ "http://labfiles.linuxacademy.com/python/fabric/sakila.sql",
                   "http://labfiles.linuxacademy.com/python/fabric/sakila-data.sql"],
    "webserver" : [ "http://labfiles.linuxacademy.com/python/fabric/index.php"]
}

@roles("database")
def install_database():
    sudo("yum -y install %s" % " ".join(packages_required["database"]), pty=True)
    sudo("systemctl enable mariadb", pty=True)
    sudo("systemctl start mariadb", pty=True)  
    sudo(r""" mysql -h 127.0.0.1 -u root -e "CREATE USER 'web'@'%' IDENTIFIED BY 'web'; GRANT ALL PRIVILEGES ON *.* TO 'web'@'%'; FLUSH PRIVILEGES;" """)
    run("ps -ef | grep mysql")

@parallel
@roles("database")

def setup_database():
    tmpdir = "/tmp"
    with cd(tmpdir):
        for url in download_files["database"]:
            filename = "%s/%s" %(tmpdir, os.path.basename(url));
            run("wget --no-cache %s -O %s" %(url, filename))
            run("mysql -u root < %s" %filename)

@roles("webserver")
def install_webserver():
    sudo("yum -y install %s" % " ".join(packages_required["webserver"]), pty=True)
    sudo("systemctl enable httpd.service", pty=True)
    sudo("systemctl start httpd.service", pty=True)
    sudo("setsebool -P httpd_can_network_connect=1", pty=True)
    sudo("setsebool -P httpd_read_user_content=1", pty=True)

@roles("webserver")
def setup_webserver():
    tmpdir = "/tmp"
    remote_dir = "/var/www/html"
    with lcd(tmpdir):
         for url in download_files["webserver"]:
             filename = "%s/%s" %(tmpdir, os.path.basename(url));
             local("wget --no-cache %s -O %s" %(url,filename))
             put(filename,"/var/www/html/", mode=0755, use_sudo=True)

    database = pick_server(env.roledefs["database"])
    sudo(r""" echo "<?php \\$db = '%s'; ?> " > /var/www/html/db.php """ % env.roledefs['database'][database])

def pick_server(mylist):
    database = 0
    while not 1<=database<=len(mylist):
         for i, db in enumerate(mylist,1):
             print "[%s] - %s" % (i, db)
         database =  prompt("Enter the number of the database should I connect %s to: " % (env.host), validate=int)
         return int(database)-1

@roles("all")
def upgrade_servers():
    sudo("yum -y upgrade", pty=True)

def deploy():
    execute(upgrade_servers)
    execute(install_database)
    execute(install_webserver)
    execute(setup_database)
    execute(setup_webserver)
    print "t|x > tw"

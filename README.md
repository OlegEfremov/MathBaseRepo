Production

Place nginx.conf.example content to
/etc/nginx/conf.d/default

Run gunicorn with:
/home/leobreslav/venv/bin/gunicorn LBBase_v_0_40.wsgi:application  -c gunicorn.conf

(for detached use -D flag)


=== Setup server from scratch ===

0) Create 2 directories in home: logs, gunicorn.


1) Install all system dependencies (python, mysql, nginx)
2) Install virtual environment
3) Clone project
git clone %path_to_git%

4) install all python requirements dependencies
pip3 install -r requirements.txt

5) Setup .env file - 

5.1) mysql password should be consistent with real  mysql login/password on server

5.2) generate secret key (with any service) and add it to .env

5.3) save .env_prod out of project dir in case you remove it.

5.4) copy .env_prod to .env inside project directory.

6) Setup nginx

6.1) Replace /etc/nginx/conf.d/default.conf content with nginx.conf.example

6.2) Restart nginx (see COMMANDS section) 

7) Setup systemctl

7.1) Create "sudo touch /etc/systemd/system/gunicorn.service"

7.2) "sudo nano /etc/systemd/system/gunicorn.service" and copy-paste
the content from "unix.service.example"

7.3) Reload systemctl itself: "sudo systemctl daemon-reload"

7.4) Enable autoload on reboot: "sudo systemctl enable gunicorn.service" 


=== Deploying project ===

After you successfully finished server setup you may proceed with
deploying you app from local computer.

DEPLOY COMMANDS (FROM LOCAL COMPUTER)

1) Deploy itself: fab deploy
2) Replace server db with local db: fab replace_prod_db_with_local_db


If any problems occur, for example you see 502 error after
starting gunicorn, observe "systemctl status" output.

OTHER COMMANDS

SSH Access: ssh leobreslav@134.0.118.26 -p 2392
Stop NGINX: sudo nginx -s stop
Start NGINX: sudo nginx

Start gunicorn: sudo systemctl start gunicorn  
Stop gunicorn: sudo systemctl stop gunicorn  
Status gunicorn: sudo systemctl status gunicorn  


SSH

OTHER UBUNTU CONSOLE TOOLS:
mc, htop
search your past commands: Ctrl+R, %your text%, then Ctrl+R loop  

"pwd" = print working directory
"cd ~" = goto home directory  

To change the standard ssh port:
1) sudo nano /etc/ssh/sshd_config:
Add/edit "Port 2392"

2) Restart ssh:
"sudo service ssh restart"

How to run ssh with non-standard port:
 "ssh leobreslav@134.0.118.26 -p 2392"

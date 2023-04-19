# Tesseract-Docker-Service
An auto updated docker ocr service. 


[Unit]
Description=My Service Updater

[Service]
Type=simple
ExecStart=/path/to/update-script.sh
Restart=always
RestartSec=10s

[Install]
WantedBy=multi-user.target


sudo systemctl enable myservice-updater
sudo systemctl start myservice-updater

sudo systemctl status myservice-updater


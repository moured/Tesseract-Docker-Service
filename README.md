# Tesseract-Docker-Service
An auto updated docker ocr service. 

nano /etc/systemd/system/ocr_updater.service

sudo systemctl start ocr_updater.service
sudo systemctl enable ocr_updater.service

journalctl -u ocr_updater.service -n 50 -f

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


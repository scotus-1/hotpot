# Server Installation Notes

#### Set up the server yk
- allow tcp/udp 25565 port on website
- allow 3876 tcp and 24454 udp
- sudo apt update && apt upgrade
- sudo apt install nano, htop, iputils-ping


- add aliases
```
export cnt=ubuntu_mc_1
alias rcon="docker exec -it $cnt rcon-cli"
alias logs="docker logs --follow $cnt"
```

- install docker
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker ubuntu

- install docker compose
sudo apt install libffi-dev libssl-dev python3 python3-pip
pip install docker-compose

- mkdir server
- clone itzg/minecraft-server --depth=1 && cd

- docker login container-registry.oracle.com
- docker buildx build --build-arg BASE_IMAGE=container-registry.oracle.com/graalvm/jdk-ee:ol8-java17-22.3.2-b1 --tag tnguyen/minecraft-server:java17-graalvm-ee --load .

- download the docker-compose.yml and EDIT IT

- set up sftp
sudoedit /etc/ssh/sshd_config

```
Match group sftp
ChrootDirectory /home
X11Forwarding No
AllowTcpForwarding no
```

sudo addgroup sftp
sudo usermod -aG sftp ubuntu

go to simplevoicechat config and set bind-address to *

# sites-up-monitor

## Description
Project to monitor web sites and check if they are running

## How to run
- This repository to your local machine:
```
git clone https://github.com/n-freman/sites-up-monitor.git
```

- Without changing directory you should run:
```
pip install -e sites-up-monitor
```

- Change directory to project directory:
```
cd sites_up_monitor
```

- You need to create input.csv file, which contains
hosts/ips and ports which you want to keep checking.<br>
Example of such file:

```
Host;Ports
ya.ru;xzx1
localhost;
;80
yandex.ru;443
last.fm;80,443
172.16.3.1;53
192.168.1.210;53
```

Notice that ```;``` must be a separator

- Now you can run:
```
python -m sites_up_monitor
```

And see the results in ```output.log``` file

### Extra
You can specify input and ouput files locations in ```sites_up_monitor/config.py```
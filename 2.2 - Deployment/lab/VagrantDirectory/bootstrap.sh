sudo apt-get update -y
sudo apt install -y python3-pip
sudo python3 -m pip install pip pandas matplotlib twitter Flask airflow -U
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install mailutils
export AIRFLOW_HOME=/vagrant/airflow
sudo python3 -m pip install airflow

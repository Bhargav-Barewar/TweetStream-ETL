
# 🐦 Twitter ETL Pipeline with Airflow & AWS
![screenshot](https://drive.google.com/file/d/1rJk_hhDOqyQQ4CEZd_iQ0MvzD8qZeVtH/view?usp=sharing)

This project is a simple ETL (Extract, Transform, Load) pipeline that extracts tweets from Twitter using the Tweepy API, transforms the data using Pandas, and loads it into an Amazon S3 bucket. Apache Airflow is used for workflow orchestration, and the whole pipeline runs on an AWS EC2 instance.

---

## 🚀 Features

- Extracts tweets from Twitter using the Tweepy API
- Transforms tweets into a structured Pandas DataFrame
- Loads the data to an Amazon S3 bucket
- Orchestrates the workflow using Apache Airflow

---

## 🛠 Technologies Used

- **Language:** Python 3.x  
- **API:** [Tweepy](https://docs.tweepy.org/en/stable/) for Twitter data  
- **Data Processing:** Pandas
- **Cloud Storage:** Amazon S3  
- **Workflow Orchestration:** Apache Airflow  
- **Deployment:** Ubuntu on AWS EC2  
- **Additional Libraries:** `s3fs`, `tweepy`, `pandas`, `apache-airflow`

---

## 📦 Requirements

Install these on your EC2 instance:
```bash
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow pandas s3fs tweepy
```

---

## 🧰 Setup Guide

### ✅ 1. Launch EC2 Instance

1. Go to AWS EC2 Dashboard → Launch Instance
2. Select Ubuntu as OS
3. Choose instance type (e.g., t2.micro)
4. Create/download a key pair (e.g., `airflow_ec2_key`)
5. Ensure HTTP and HTTPS are allowed
6. Launch the instance

---

### 🔑 2. Assign IAM Role with S3 Access

1. Create an IAM Role (EC2 type)
2. Attach the `AmazonS3FullAccess` policy
3. Attach the role to your EC2 instance via **Actions → Security → Modify IAM Role**

---

### 🪣 3. Create S3 Bucket

1. Go to S3 Dashboard
2. Click "Create Bucket"
3. Provide a unique name (e.g., `twitter-etl-bucket`)
4. Leave defaults and create the bucket

---

### 📁 4. Upload ETL Project Files

1. SSH into EC2 using the downloaded key
2. Setup Airflow directory:
```bash
cd airflow
sudo nano airflow.cfg
# Set dag_folder to: /home/ubuntu/airflow/twitter_dags
mkdir twitter_dags
cd twitter_dags
```

3. Add your Python files:
   - `dag.py`
   - `etl_function.py`

Paste code using `nano`, or upload using SCP.

---

### 🌐 5. Access Airflow Web UI

1. Run:
```bash
airflow standalone
```

2. Copy the credentials shown in the terminal

3. In AWS Console:
   - Go to EC2 → Instance → Security → Edit Inbound Rules
   - Add a rule:
     - Type: Custom TCP
     - Port: `8080`
     - Source: `Your IP/32`

4. Visit:
```text
http://<Your-EC2-Public-DNS>:8080
```
Login using the credentials from terminal.

---

### 🔐 6. Set Airflow Variable for Twitter API (GUI)

Open Airflow in your browser:
```text
http://<Your-EC2-Public-DNS>:8080
```
Then:

1. Click **Admin → Variables**
2. Click the "**+**" button to add the following key–value pairs:
3. Get bearer token from [link](https://developer.x.com/en/docs/x-api)

| Variable Name     | Purpose                          | Example Value               |
|------------------|----------------------------------|-----------------------------|
| `bearer_token`   | API authentication key           | `your_bearer_token`         |


---

### 📊 Running the Pipeline

1. Enable the DAG `twitter_dag` from the Airflow UI
2. Trigger it manually or wait for scheduled execution
3. Data will be saved to:
```text
s3://your-bucket-name/elonmusk_tweets.csv
```

---

## What I Did Well

- Successfully set up an EC2 instance on AWS and installed the required libraries
- Configured Apache Airflow and created a DAG to run the ETL pipeline
- Implemented the ETL pipeline using Python and the Tweepy API
- Loaded the data into an S3 bucket and made it accessible through the Airflow web UI
- Documented the project and provided instructions for others to follow

---

## 📘 What I Learned

- Provisioning and configuring EC2 on AWS
- Setting up Apache Airflow and DAGs
- Working with Twitter API via Tweepy
- Using S3 buckets for cloud storage
- Automating ETL workflows on the cloud

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


from PyPDF2 import PdfReader



def extract_text_from_pdf(pdf_path):
    
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    return text


skills = [
    # Original skills
    "ROS", "C++", "Python", "TensorFlow", "PyTorch", "Keras", "Matlab", "Simulink",
    "Linux", "Git", "Bash", "Docker", "OpenCV", "SLAM", "VHDL", "Verilog", "FPGA",
    "CUDA", "Caffe", "Scikit-learn", "Pandas", "NumPy", "SciPy", "R", "Java", "C",
    "SQL", "NoSQL", "Hadoop", "Spark", "Tableau", "Matplotlib", "Seaborn", "NLTK",
    "Spacy", "Selenium", "Jupyter", "Arduino", "RaspberryPi", "TensorRT", "ONNX",
    "GCP", "AWS", "Azure", "Kubernetes", "Ansible", "Terraform", "Jenkins", "Flask",
    "Django", "FastAPI", "REST", "GraphQL", "HDFS", "Hive", "Pig", "Mahout",
    "SparkML", "MLlib", "Kafka", "RabbitMQ", "Celery", "Elasticsearch", "Logstash",
    "Kibana", "Prometheus", "Grafana", "Airflow", "ETL", "Redux", "React", "Vue",
    "Angular", "Bootstrap", "HTML", "CSS", "JavaScript", "TypeScript", "Perl", "Go",
    "Ruby", "Scala", "Lua", "Shell", "PowerShell", "ObjectiveC", "Swift", "Android",
    "iOS", "Xcode", "Unity", "Blender", "Gazebo", "Autonomous", "LIDAR", "RADAR",
    "Sonar", "ZMQ", "Protobuf", "Thrift", "Hadoop", "MapReduce", "ROS-MoveIt!", "PHP",

    # Additional robotics skills
    "ROS2", "Gazebo", "V-REP", "Webots", "CoppeliaSim", "LabVIEW", "PLC",
    "Robotics Operating System", "Inverse Kinematics", "Forward Kinematics",
    "Path Planning", "Motion Planning", "Computer Vision", "Image Processing",
    "Sensor Fusion", "Control Systems", "Robotic Arm Programming", "PCB Design",

    # Additional AI/ML skills
    "GANs", "Reinforcement Learning", "Natural Language Processing", "Deep Learning",
    "Machine Learning", "Neural Networks", "Computer Vision", "Transformers",
    "BERT", "GPT", "XGBoost", "LightGBM", "CatBoost", "PySpark", "Dask",
    "Ray", "MLflow", "DVC", "Weights & Biases", "Optuna", "AutoML",
    "Feature Engineering", "Data Preprocessing", "Model Deployment",

    # Additional frontend skills
    "WebGL", "Three.js", "D3.js", "SVG", "WebAssembly", "PWA",
    "Responsive Design", "SASS", "LESS", "Webpack", "Babel", "ESLint",
    "Jest", "Cypress", "Storybook", "Next.js", "Nuxt.js", "Svelte",
    "Electron", "Progressive Enhancement", "Accessibility", "SEO",

    # Additional backend skills
    "Node.js", "Express.js", "NestJS", "Spring Boot", "ASP.NET Core",
    "Laravel", "Ruby on Rails", "Phoenix", "FastAPI", "gRPC", "WebSocket",
    "Microservices", "RESTful API Design", "OAuth", "JWT", "SOAP",
    "Message Queues", "Caching (Redis, Memcached)", "Load Balancing",
    "Database Design", "ORM (SQLAlchemy, Hibernate)", "GraphQL",

    # DevOps and Cloud
    "CI/CD", "GitLab", "Bitbucket", "Travis CI", "CircleCI", "SonarQube",
    "Artifactory", "Puppet", "Chef", "Salt", "Vagrant", "Packer",
    "ELK Stack", "Serverless", "Containers", "Microservices",
    "Infrastructure as Code", "Site Reliability Engineering",

    # Database skills
    "MongoDB", "PostgreSQL", "MySQL", "Oracle", "SQLite", "Cassandra",
    "Redis", "Neo4j", "InfluxDB", "TimescaleDB", "Couchbase",
]
def get_skills(resume_text):
    skills_found = []
    for skill in skills:
        if skill in resume_text:
            skills_found.append(skill)
    return skills_found

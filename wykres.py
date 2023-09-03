#wykres
import matplotlib.pyplot as plt



def pokaz_na_wykresie(dane, nazwa_tech):

    # Twój słownik
    data = dane


    # Sortowanie słownika według wartości
    sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

    top_20_data = dict(list(sorted_data.items())[:25])

    # Nazwy technologii i ich liczby
    tech_names = list(top_20_data.keys())
    tech_values = list(top_20_data.values())


    # Tworzenie wykresu
    plt.figure(figsize=(10, 6), facecolor='black')
    plt.barh(tech_names, tech_values, color='springgreen')

    # Ustawienie czerwonego tła
    plt.gca().set_facecolor('dimgray')

    # Ustawienie koloru obwódki na czarny
    for spine in plt.gca().spines.values():
        spine.set_edgecolor('gray')

    plt.xlabel('Liczba wystąpień')
    plt.ylabel('Technologie')
    plt.title(f'Popularność technologii w {nazwa_tech}')

    # Ustawienie koloru etykiet osi i tytułu na biały
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')
    plt.xlabel('Liczba wystąpień', color='white')
    plt.ylabel('Technologie', color='white')
    plt.title(f'Popularność technologii w {nazwa_tech}', color='white')

    plt.gca().invert_yaxis()  # Odwrócenie osi Y, aby największe wartości były na górze
    plt.show()


if __name__ == "__main__":
    dane = {'SQL': 105, 'Python': 71, 'Java': 22, 'Oracle': 21, 'Scala': 19, 'PL/SQL': 17, 'Git': 14, 'Microsoft Power BI': 14, 'T-SQL': 12, 'Kafka': 11, 'Spark': 10, 'Power BI': 9, 'Tableau': 9, 'AWS': 9, 'R': 9, 'C#': 8, 'JavaScript': 8, 'Docker': 7, 'MySQL': 7, 'PostgreSQL': 7, 'Jira': 7, 'Bash': 7, 'Microsoft SQL Server': 7, 'Snowflake Data Cloud': 6, 'Azure': 6, 'SAP': 6, 'Microsoft Azure': 6, 'Kubernetes': 5, 'SAS': 5, 'Hadoop': 5, 'Azure DevOps': 5, 'Google Cloud Platform': 5, 'MSSQL': 5, 'Apache Spark': 5, 'Microsoft Excel': 5, 'Confluence': 4, 'ERP': 4, 'Jenkins': 4, 'Airflow': 4, 'Data Lake': 4, 'Quantexa': 4, 'Azure Databricks 5': 4, 'PySpark 4': 4, 'Azure Data Factory 3': 4, 'SQL 3': 4, 'Azure DevOps 3': 4, 'Excel': 3, 'Google Analytics': 3, 'REST': 3, 'MS SQL': 3, 'Hive': 3, 'Databricks': 3, 'C++': 3, 'Windows Server': 3, 'TSQL': 3, 'SSIS': 3, 'Grafana': 3, 'Pandas': 3, 'Apache Airflow': 3, 'BigQuery': 3, 'VBA': 3, 'HTML': 3, 'GitLab': 2, 'Terraform': 2, 'Qlik': 2, 'Snowflake': 2, 'Big Data': 2, 'Data modeling': 2, 'ETL': 2, 'Linux': 2, 'DAX': 2, 'VMware': 2, 'Looker': 2, 'GitHub': 2, 'Zabbix': 2, 'Sybase': 2, 'PowerShell': 2, 'Perl': 2, 'Node.js': 2, 'NoSQL': 2, 'DBT': 2, 'Druid': 2, 'CI/CD': 2, 'DWH': 2, 'ETL/ELT': 2, 'Azure Data Factory': 2, 'Azure Synapse': 2, 'Azure Cosmos DB': 2, 'PySpark': 2, 'NiFi': 2, 'HBase': 2, 'Gitlab': 2, 'Spring Framework': 2, 'LakeHouse': 2, 'Qlik Sense': 1, 'SPPS': 1, 'BI software': 1, 'API': 1, 'GraphQL': 1, 'AsyncAPI': 1, 'SAP/Oracle': 1, 'Cognos': 1, 'MongoDB': 1, 'Reporting Services': 1, 'RandSQL': 1, 'JIRA': 1, 'bash': 1, 'Informatica (Data Governance/Data Quality)': 1, 'SAP ERP': 1, 'Data Integration': 1, 'Data Warehousin': 1, 'Software Architecture': 1, 'SQL Server Integration Services': 1, 'Pentaho Data Integration': 1, 'data warehouse': 1, 'SQL-Server': 1, 'AWS S3': 1, 'and MongoDB': 1, 'Lynx': 1, 'Power Shell': 1, 'dbt': 1, 'TensorFlow': 1, 'PyTorch': 1, 'SSAS': 1, 'COBOL': 1, 'GIT': 1, 'Microsoft Hyper-V/AzureStack HCI OS': 1, 'SAN': 1, 'iSCSI': 1, 'FC': 1, 'Kanban': 1, 'Scrum': 1, 'Splunk Core': 1, 'Nagios': 1, 'SCOM': 1, 'Prometheus': 1, 'Telegraf': 1, 'AppDynamics': 1, 'Dynatrace': 1, 'Apache': 1, 'Web-logic': 1, 'Tomcat': 1, 'JBoss': 1, 'EVM': 1, 'Substrate': 1, 'Google Data Studio': 1, 'NumPy': 1, 'SciPy': 1, 'AzURE': 1, 'BI': 1, 'MS Office': 1, 'LAN': 1, 'Supervised Learning': 1, 'Non- supervised Learning': 1, 'Cloud programming': 1, 'Agile': 1, 'RESTful API': 1, 'Unix shell scripting': 1, 'Autosys': 1, 'Core Java': 1, 'Java EE': 1, 'Team City': 1, 'Udeploy': 1, 'Spring': 1, 'Springboot': 1, 'Hibernate': 1, 'SSRS': 1, 'Data Pipelines': 1, 'Data Engineering': 1, 'Data Warehousing': 1, 'Informatica PowerCenter': 1, 'Informatica Intelligent Cloud Services': 1, 'Netezza': 1, 'Azure SQL': 1, 'Microsoft SSIS': 1, 'Microsoft Dynamics': 1, 'Active Directory': 1, 'gpo': 1, 'Cisco': 1, 'fortigate': 1, 'Unix': 1, 'Databases': 1, 'Design Patterns': 1, 'CSS': 1, 'Google Tag Manager': 1, 'Dataslayer': 1, 'Supermetrics': 1, 'Google Calendar': 1, 'Looker Studio': 1, 'Google Spreedsheet': 1, 'Universal Analytics': 1, 'Alteryx': 1, 'Dataiku': 1, 'Talend': 1, 'Informatica Power Center': 1, 'Oracle Forms': 1, 'C': 1, 'Kinesis': 1, 'Zeppelin': 1, 'Pythom': 1, 'Ansible': 1, 'Salt': 1, 'Puppet': 1, 'Azure Databricks': 1, 'MS SQL Server': 1, 'Maven': 1, 'Gradle': 1, 'PL-SQL': 1, 'Presto SQL': 1, 'PHP': 1, 'Hadoop ecosystem (HDFS': 1, 'YARN)': 1, 'Sqoop': 1, 'Casandra': 1, 'Scylla': 1, 'SQL Oracle': 1, '4GL': 1, 'Elasticsearch': 1, 'Cassandra': 1, 'HPALM': 1, 'PLSQL': 1, 'SQL/T-SQL': 1, 'BPMN': 1, 'UML': 1, 'Shell': 1, 'Power Automate': 1, 'RPA': 1, 'Enterprise Architect': 1, 'SoapUI': 1}

    pokaz_na_wykresie(dane, "")
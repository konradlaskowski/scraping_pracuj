from collections import Counter

def count_technologies(tech_list):
    tech_count = Counter(tech_list)
    return tech_count

# Przykładowa lista technologii
tech_list = ['Python', 'AWS', 'SQL', 'Docker', 'Java', 'C', 'C++', 'Fortran', 'Python', 'Bash', 'Python', 'SQL', 'Git', 'Bash', 'Python', 'Go', 'Git', 'Ansible', 'Terraform', 'AWS', 'Docker', 'Groovy', 'Java', 'JavaScript', 'Python', 'Spring Framework', 'Hibernate', 'Jenkins', 'Git', 'REST API', 'Elasticsearch', 'Logstash', 'Kibana', 'MongoDB', 'Oracle', 'Postgre', 'Python', 'PowerShell', 'Python', 'Java', 'AWS', 'Git', 'Nexus', 'Artifactory', 'Gradle', 'Teamscale', 'CI/CD', 'Python', 'Bash', 'Ansible', 'Terraform', 'Go', 'Node.js', 'Git', 'GitHub', 'Jenkins', 'Python', 'SQL', 'MSSQL', 'Python', 'Bash', 'Ansible', 'Terraform', 'Jenkins', 'Git', 'Linux', 'Python', 'Linux', 'Google Cloud Platform', 'Bash', 'AWS', 'Kubernetes', 'Bash', 'Python', 'Terraform', 'Networking', 'Linux', 'IaC', 'Red Hat', 'Linux', 'Python', 'Ansible', 'Python', 'Java', 'C#', 'Tensorflow', 'scikit-learn', 'pyTorch', 'h2o', 'Kedro', 'Kubeflow', 'Katib', 'MLFlow', 'AWS', 'Microsoft Azure', 'Google Cloud Platform', 'Python', 'Git', 'AWS', 'Ansible', 'Linux', 'CI/CD tools', 'Python', 'Kubernetes', 'MySQL', 'MariaDB', 'PostgreSQL', 'MongoDB', 'Elasticsearch', 'Redis', 'Memcached', 'Cassandra', 'Python', 'Bash', 'Python', 'Pandas', 'Python', 'SQL', 'C++', 'Python', 'PostgreSQL', 'Qt', 'Git', 'GitHub', 'Visual Studio Code', 'Agile', 'Scrum', 'SQL', 'R', 'Python', 'Spark', 'Kafka', 'Jenkins', 'Kubernetes', 'Scala', 'Java', 'Python', 'Python', 'Java', 'SQL', 'Jenkins', 'Python', 'SQL', 'Python', 'SQL', 'Python', 'SQL', 'Docker', 'Ansible', 'Python', 'SQL', 'Unix Shell', 'Azure DevOps', 'Apache Spark', 'Python', '.NET', 'C++', 'Python', 'AWS', 'Django', 'React.js', 'Python', 'AWS', 'Django', 'NoSQL', 'React.js', 'Python', 'Java', 'C++', 'MongoDB', 'Snowflake Data Cloud', 'SQL', 'AWS', 'Python', 
'Python', 'SQL', 'Oracle', 'Python', 'Django', 'DRF', 'FastAPI', 'Pytest', 'Celery', 'JavaScript', 'TypeScript', 'React.js', 'Hooks', 'Python', 'SQL', 'Bash', 'Python', 'Shell', 'Linux', 'Python', 'Java', 'SQL', 'GitLab', 'Python', 'SQL', 'Google Cloud Platform', 'Microsoft Power BI', 'React.js', 'Python', 'Flask', 'jQuery', 'HTML', 'CSS', 'Python', 'Google Cloud Platform', 'Windows Server']


# # Użycie funkcji
# result = count_technologies(tech_list)
# sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

# lista_technologi = []
# # Wyświetlenie wyników
# # for tech, count in sorted_result.items():
# #     lista_technologi.append(f"{{tech}: {count}}")
# final_dict = {}
# for tech, count in sorted_result.items():
#     final_dict[tech] = count




def policz_posegreguj_technologie(lista_tech:list):
        # Użycie funkcji
    result = count_technologies(tech_list)
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

    lista_technologi = []
    # Wyświetlenie wyników
    # for tech, count in sorted_result.items():
    #     lista_technologi.append(f"{{tech}: {count}}")
    final_dict = {}
    for tech, count in sorted_result.items():
        final_dict[tech] = count
    return final_dict

# for x in final_dict:
#     print(f'{x} : {final_dict[x]}')

# print(final_dict)


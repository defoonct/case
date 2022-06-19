from diagrams import Cluster, Diagram
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage
from diagrams.onprem.network import Haproxy
from diagrams.onprem.network import Internet
from diagrams.onprem.network import Nginx
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka

with Diagram(show=False):
    users = Users("Users")
    web_app = Server("Web application")
    application = Server("Loan application")

    with Cluster("Entrypoint"):
        entrypoint = [Haproxy(), Nginx()]

    with Cluster("Third party integrations"):
        integrations = [Internet(), PostgreSQL()]

    with Cluster("Queue"):
        queue = [Kafka(), Kafka(), Kafka()]

    with Cluster("Datastore"):
        datastore = Storage() - Storage()

    users >> entrypoint >> web_app >> queue >> application >> integrations
    application >> datastore

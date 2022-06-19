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

    with Cluster("Entrypoint"):
        entrypoint = [Haproxy(), Nginx()]

    with Cluster("Loan application"):
        application = Server()

    with Cluster("Third party integrations"):
        integrations = [Internet(), PostgreSQL()]

    with Cluster("Customer requests"):

        with Cluster("Web application"):
            web_app = Server()

        with Cluster("Queue"):
            with Cluster("Queue"):
                queue = Kafka()

            with Cluster("App"):
                app = Server()

    with Cluster("Datastore"):
        datastore = Storage() - Storage()

    users >> entrypoint >> web_app >> queue >> application >> integrations
    web_app >> app >> datastore
    app >> application
    queue >> datastore

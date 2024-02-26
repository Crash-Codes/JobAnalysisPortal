import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_listings"]

# Insert the extracted data into the jobs collection
collection = db["jobs"]
collection.insert_many(job_listings)

# Print the number of documents inserted
print(f"{len(job_listings)} documents inserted into the jobs collection")

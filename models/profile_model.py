from pymongo import MongoClient
from pymongo.errors import PyMongoError
from helpers.logger import logger

# Set up MongoDB client using URI
client = MongoClient("mongodb+srv://skuhandran:H8tpfKQ5ir4HRKqT@data-services.itent.mongodb.net/?retryWrites=true&w=majority&appName=data-services")

# Use the 'data-services' database
db = client["data-services"]
# Use the 'profiles' collection (it will be created automatically if it doesn't exist)
profiles_collection = db["profiles"]

def save_profile_to_db(client_id, profile):
    """
    Create a new profile or update an existing one based on client_id.
    """
    try:
        existing_profile = profiles_collection.find_one({"client_id": client_id})
        if existing_profile:
            profiles_collection.update_one({"client_id": client_id}, {"$set": profile})
        else:
            profiles_collection.insert_one(profile)
        return True  # Indicate success
    except PyMongoError as e:
        logger.error(f"Error saving profile to database: {e}")
        return False  # Indicate failure

def get_profile_from_db(client_id):
    """
    Retrieves a profile from the MongoDB collection based on client_id.
    """
    try:
        return profiles_collection.find_one({"client_id": client_id})
    except PyMongoError as e:
        logger.error(f"Error retrieving profile from database: {e}")
        return None  # Indicate failure

def delete_all_profiles():
    """
    Deletes all documents from the profiles collection.
    """
    try:
        result = profiles_collection.delete_many({})
        return result.deleted_count  # Return the number of deleted documents
    except PyMongoError as e:
        logger.error(f"Error deleting profiles from database: {e}")
        return 0  # Indicate failure

def get_profile_by_mobile(mobile_number):
    """
    Find a profile by mobile number.
    """
    try:
        return profiles_collection.find_one({"contact.phone": mobile_number})
    except PyMongoError as e:
        logger.error(f"Error finding profile by mobile number: {e}")
        return None  # Indicate failure
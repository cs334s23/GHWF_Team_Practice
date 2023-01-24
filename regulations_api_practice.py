import requests

REGULATIONS_API_KEY = "gLYbI3nQyGOe3aBPdKKWeEB9bkfoDAOyfC6uCtUl"

def make_request():
    """
    Use the request library to verify if we can make a successful API call using our own API Key (constant)
    Url used is from the Regulations.gov API documentation
    """
    try:
        response = requests.get("https://api.regulations.gov/v4/dockets?filter[searchTerm]=water&api_key=" + REGULATIONS_API_KEY)
        response.raise_for_status()
        print("Request Successful")
    except requests.exceptions.HTTPError as e:
        print("Request Failed with error %s" % (e))

def total_elements_of_query(url):
    """
    return total (totalElements in content of request) of query based on URL search provided. 
    NOTE: The solution from this code could be wrong. 
    EDIT: It was, edit code to check multiple pages
    """
    response = requests.get(url + REGULATIONS_API_KEY)
    response = response.json()

    return response["meta"]["totalElements"]

def main():
    make_request()
    dockets = total_elements_of_query("https://api.regulations.gov/v4/dockets?sort=title&api_key=")
    documents = total_elements_of_query("https://api.regulations.gov/v4/documents?sort=title&api_key=")
    comments = total_elements_of_query("https://api.regulations.gov/v4/comments?filter[postedDate][ge]=1900-09-01&filter[postedDate][le]=2020-09-01&api_key=")

    print("dockets = %s\ndocuments = %s" % (dockets, documents))
    print("Comments = " + str(comments))
    print("Edwin has made a change within regulations")

if __name__ == "__main__":
    main()

# Sirius News Highlights

## Built By [Mary Ng'ang'a](https://github.com/marynganga/)

## Description
Sirius News Highlights is a web application that displays a list of various news sources like BBC and CNN. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the [News API](https://newsapi.org/).

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/marynganga/Sirius-News-Highlights/
        $ cd Sirius-News-Highlights

## Running the Application
* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.6 tests/test_news_article.py
        $ python3.6 tests/test_news_source.py
        
## Technologies Used
* Python3.6
* Flask

## License
MIT &copy;2017 [Mary Ng'ang'a](https://github.com/marynganga/)

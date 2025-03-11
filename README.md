![Cinema](cinema.jpg)
# Movie Data Analysis Project

## Overview
This project delivers a data-driven application that enables users to analyze movies, actors, directors, and genres based on ratings and popularity metrics. The tool is designed to support both casual users interested in film analytics and film production/distribution companies making data-driven decisions.

## Business Case
- **For Users**: Explore and analyze actors, directors, movie genres, ratings, and popularity
- **For Film Industry**: Support data-driven decision making in production and distribution

## Key Features
- Analysis of movie ratings and popularity trends
- Genre performance analysis
- Director and actor performance metrics
- Insights for film production companies

## Data Sources
The project utilizes several datasets from IMDb Non-Commercial Datasets:
- `Title.basics.tsv.gz`: Basic movie and series information (11M+ rows)
- `name.basics.tsv.gz`: Information about actors, writers, directors (14M+ rows)
- `title.ratings.tsv.gz`: Average ratings and vote counts (1.5M+ rows)
- `title.crew.tsv.gz`: Directors and writers per movie (11M+ rows)
- `title.principals.tsv.gz`: Actors and characters per movie (91M+ rows)

Additional data from Kaggle:
- Full TMDB Movies Dataset: Includes ratings, votes, budget, revenue data (1.2M rows)

## Database Design
The project implements a relational database with multiple interconnected tables following a carefully designed entity-relationship model. The implementation focused on movies from 2020 onwards, containing:
- 47,000+ movies
- 7,000+ persons
- 860,000+ character entries

## Analysis Dataframes
Two primary dataframes drive the analysis:
1. **actors_df** (860k+ characters):
   - Actor/actress personal information
   - Movie and character details
   - Ratings and popularity metrics

2. **movies_df** (98k+ movies):
   - Release year, genre and duration
   - Director information
   - Ratings and popularity metrics

## Key Findings
- Genre popularity ranking: 1) Action, 2) Drama, 3) Comedy
- Top directors by performance: Denis Villeneuve, John Krasinski, Adam McKay
- Notable high-performing cast members: Scarlett Johansson, Leonardo DiCaprio, James Remar

## Technical Challenges and Solutions
| Challenge | Solution |
|-----------|----------|
| Loading huge datasets into MySQL database | Filtered data to include only 2010 onwards |
| Inconsistent budget and revenue data | Abandoned budget-revenue analysis approach |
| Movies with few votes skewing ratings | Implemented vote count threshold for analysis |
| Managing massive character dataset (91M+ rows) | Added filtering based on series/movie information |

## Implementation Details
- **Frontend**: Streamlit application
- **Database**: MySQL
- **Visualization**: Tableau for exploratory data analysis
- **Python Libraries**: Data processing and analysis

## Future Improvements
- Expand dataset to include more historical data
- Implement additional analysis metrics
- Enhance visualization capabilities
- Add personalized recommendation features

## Tools and Technologies
- Python (data processing, analysis, and application backend)
- SQL (data storage and retrieval)
- Streamlit (web application interface)
- Tableau (data visualization and EDA)
- Environment management for reproducibility

## Project Context
Developed as a final project for the Ironhack Data Analytics Bootcamp (January 2025).

## Getting Started
Go to streamlit folder and execute the code:
Streamlit run Movie.py

## Contributors
Víctor Ramírez Rubio

## License
This project uses IMDb non-commercial datasets and follows their terms of use.

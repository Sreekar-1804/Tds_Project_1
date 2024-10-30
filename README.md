# TDS_Project_1

This project uses the GitHub API to scrape data about users and repositories based on specific criteria, such as location and follower count.

## Overview

This project performs the following:
- Fetches all GitHub users in Sydney with over 100 followers.
- Retrieves up to 500 of their most recent repositories.
- Saves user and repository data in `users.csv` and `repositories.csv`.
- Analyzes the data and provides insights based on specified questions.

## Files

- **main.py**: Main Python script for data collection and processing.
- **users.csv**: Contains data about GitHub users in Sydney with over 100 followers, including fields like `login`, `name`, `company`, `location`, `email`, `bio`, and more.
- **repositories.csv**: Contains data about the users' repositories, with fields such as `login`, `full_name`, `created_at`, `stargazers_count`, `language`, and more.
- **README.md**: Project documentation.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sreekar-1804/Tds_Project_1.git
   cd TDS_Project_1

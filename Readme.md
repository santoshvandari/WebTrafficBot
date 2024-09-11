# Website Traffic Simulation Script

This script simulates user interaction with a given website by visiting the URL, scrolling, hovering over random elements, and staying on the page for a random amount of time. It uses Playwright and runs asynchronously to simulate more realistic user behavior.

## Features

- Simulates a real user visit by using different user agents.
- Scrolls and hovers over elements randomly.
- Visits the specified URL in headless mode.
- Randomly stays on the website for a specific period to imitate real user traffic.

## Requirements

- Python 3.7+
- Playwright

## Usages

Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
   git clone https://github.com/santoshvandari/WebTrafficBot.git
   cd WebTrafficBot
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and MAC User
     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Run the Script
 ```bash
   python3 main.py -u <URL> # python3 main.py -u https://facebook.com
   or 
   python4 main.py --url <URL> # python3 main.py --url https://facebook.com
   
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this Mero Share IPO Filler Script, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this Script.

## License
This project is licensed under the MIT [License](LICENSE).
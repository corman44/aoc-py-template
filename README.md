## Python Project Template for Advent of Code

https://adventofcode.com/

### Features
- [x] automated day solutions setup
- [x] automated input gathering from AoC

### Setup
- Create Repo from this template
- Generate venv with ```python3 venv```
- Activate venv with ```source venv```
- Install base packages with ```pip3 install -r requirements.txt```
- Get Cookie
  - signin to AoC using your method of choice
  - copy the session cookie to a .env file in your project root folder with the following format ```SESSION_COOKIE=<cookie>```
    - cookie can be found by pressing f12 -> Application -> Cookies -> session
- Test the template script by running _create-day.py_ and entering 1 (ensure that year & day combo is already available on AoC)

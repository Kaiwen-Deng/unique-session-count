# unique-session-count

## Purpose

A simple script for counting number of unique sessions in each ` browser`, `operational system` or `device`.


## Dependencies
- pip install pandas
- pip install numpy
- put data sets in `json` format in [data](data/) folder (you can put multiple json files)

## Usage
- clone the repo:
```
git clone https://github.com/Kaiwen-Deng/unique-session-count.git
```
- go to the repo;
- in the repo, put the data sets you want to calculate in [data](data/) folder;
- use the player.sh in command terminal: 
```bash
Usage: ./player.sh <field>
```
Options: specify the field to count session. The field could be one of followings:
- `browser_family`
- `os_family`
- `device_family`

## Example

```bash
./player.sh os_family
```
Then it will return result (example):
```json
{'Android': 47172, 'Chrome OS': 86, 'Fedora': 10, 'Linux': 785, 'Mac OS X': 1809, 'Other': 7625, 'Ubuntu': 172, 'Windows 10': 18686, 'Windows 7': 15317, 'Windows 8': 462, 'Windows 8.1': 2366, 'Windows Phone': 97, 'Windows RT': 3, 'Windows RT 8.1': 1, 'Windows Vista': 83, 'Windows XP': 342, 'iOS': 13340}
```

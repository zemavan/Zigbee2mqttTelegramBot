###                      Zigbee2mqtt with telegram bot automatition

### Before Start:
   - Zigbee is a lighweight communications protocol.
   - MQTT is a machine to machine network protocol for messages.

### Precausions:
   - Zigbee is not designed for realtime communication, so the range of it depends on sensor that you are using.
   - Zigbee`s goal is to be lightweight and energy-efficient. When there are no changes, the sensor wont post data.
   - The goal of this project is to understand the fundamentals of IoT development.

### Requisites
- Docker 
- Python 3.9+  
- Zigbee-dongle
- Sensor  
- Telegram Bot


### 1. Clone repository
```bash
git clone https://github.com/zemavan/Zigbee2mqttTelegramBot.git
```


## 2. Setup the virtul environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## 3. ENV (optional)
touch .env in main directory of the project
```bash
touch .env 
> TOKEN=YourTelegramBotToken
> logFilePath=PathToLogTxtFile
```
## 4. GetStarted
    1. cd zigbee2mqtt
    2. *Connect the Dongle
    3. docker compose up
    4. Pass the Onboarding for zigbee2mqtt on port 8082
       https://www.zigbee2mqtt.io/guide/getting-started/#installation
    5. Connect zigbee sensors

By default the topic is zigbee2mqtt, if devices name is fridge the topic will be zigbee2mqtt/fridge
You should indicate it in the mqtt/mqtt.py

Zigbee2mqtt pushes the messages on topic in json file format, so we parse and save it on our log.txt file that we declareted before in .env file, to make it possible for our telegram bot get data from.

## 5. Telegram bot
https://core.telegram.org/bots/tutorial#getting-ready

   1. Provide telegram token into .env file
   2. The code for the bot in TelegramBot/bot.py has some functions to test api.

## 6. Start
When the project is set:
   ### 1. Check if the environment is activated.
   ### 2. Procede to zegibee2mqtt folder and start up docker compose
   ### 3. Procede to mqtt folder and start up mqtt by 
   ```bash python mqtt.py
   ``` 
   The output should be "Connected" 

   ### 4. Procede to TelegramBot and start up bot by 
   ```bash python bot.py
   ```
   The output should be this:
        INFO:aiogram.dispatcher:Start polling
        INFO:aiogram.dispatcher:Run polling for bot @

## 7. Test
When you send to your bot command 'temperature', the bot should answer with the current temperature.















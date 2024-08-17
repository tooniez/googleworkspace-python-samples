# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-apps-chat

# [START chat_create_message_app_cred_with_cards]
from authentication_utils import create_client_with_app_credentials
from google.apps import chat_v1 as google_chat

# This sample shows how to create message with a card attached with app
# credential
def create_message_with_app_cred_with_cards():
    # Create a client
    client = create_client_with_app_credentials()

    # Initialize request argument(s)
    request = google_chat.CreateMessageRequest(
      # Replace SPACE_NAME here
      parent = "spaces/SPACE_NAME",
      message = {
        "text": "Hello with app credential!",
        "cards_v2" : [{
          "card_id": "card-id",
          "card": {
            "sections": [{
              "widgets": [{
                "button_list": {
                  "buttons": [
                    {
                      "text": "Edit",
                      "disabled": True,
                    },
                    {
                      "icon": {
                        "known_icon": "INVITE",
                        "alt_text": "check calendar"
                      },
                      "on_click": {
                        "open_link": {
                          "url": "https://www.google.com"
                        }
                      }
                    }
                  ]
                }
              }]
            }]
          }
        }]
      }
    )

    # Make the request
    response = client.create_message(request)

    # Handle the response
    print(response)

create_message_with_app_cred_with_cards()

# [END chat_create_message_app_cred_with_cards]
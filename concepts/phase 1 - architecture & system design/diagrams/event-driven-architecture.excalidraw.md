---
excalidraw-plugin: parsed
tags: [eda, events, async, broker]
---
# Excalidraw Data
## Text Elements
Producer
(Front-end) ^producer1-text
Producer
(Account) ^producer2-text
Event Channel
(Message Broker) ^channel-text
Consumer
(Notifications) ^consumer1-text
Consumer
(Fraud Detection) ^consumer2-text
emit events ^l-emit
subscribe ^l-sub
subscribe ^l-sub2
Events = immutable facts; consumers subscribe without coupling ^caption
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "obsidian-excalidraw-plugin",
  "elements": [
    {
      "type": "rectangle",
      "version": 1,
      "id": "producer1-box",
      "x": 20,
      "y": 40,
      "width": 140,
      "height": 70,
      "strokeColor": "#1971c2",
      "backgroundColor": "#e7f5ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800032,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "producer1-text",
      "x": 38.25,
      "y": 55.0,
      "width": 103.5,
      "height": 40,
      "text": "Producer\n(Front-end)",
      "fontSize": 15,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#1971c2",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800033,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "producer2-box",
      "x": 20,
      "y": 140,
      "width": 140,
      "height": 70,
      "strokeColor": "#1971c2",
      "backgroundColor": "#e7f5ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800034,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "producer2-text",
      "x": 46.75,
      "y": 155.0,
      "width": 86.5,
      "height": 40,
      "text": "Producer\n(Account)",
      "fontSize": 15,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#1971c2",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800035,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "channel-box",
      "x": 240,
      "y": 85,
      "width": 150,
      "height": 80,
      "strokeColor": "#e03131",
      "backgroundColor": "#fff5f5",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800036,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "channel-text",
      "x": 242.0,
      "y": 105.0,
      "width": 146.0,
      "height": 40,
      "text": "Event Channel\n(Message Broker)",
      "fontSize": 15,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#e03131",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800037,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "consumer1-box",
      "x": 470,
      "y": 30,
      "width": 140,
      "height": 70,
      "strokeColor": "#2f9e44",
      "backgroundColor": "#ebfbee",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800038,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "consumer1-text",
      "x": 471.25,
      "y": 45.0,
      "width": 137.5,
      "height": 40,
      "text": "Consumer\n(Notifications)",
      "fontSize": 15,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#2f9e44",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800039,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "consumer2-box",
      "x": 470,
      "y": 130,
      "width": 140,
      "height": 70,
      "strokeColor": "#2f9e44",
      "backgroundColor": "#ebfbee",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800040,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "consumer2-text",
      "x": 462.75,
      "y": 145.0,
      "width": 154.5,
      "height": 40,
      "text": "Consumer\n(Fraud Detection)",
      "fontSize": 15,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#2f9e44",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800041,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "p1-ch",
      "x": 160,
      "y": 70,
      "width": 80,
      "height": 20,
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800042,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          80,
          20
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "p2-ch",
      "x": 160,
      "y": 160,
      "width": 80,
      "height": -20,
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800043,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          80,
          -20
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "ch-c1",
      "x": 390,
      "y": 105,
      "width": 80,
      "height": -40,
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800044,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          80,
          -40
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "ch-c2",
      "x": 390,
      "y": 145,
      "width": 80,
      "height": 20,
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800045,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          80,
          20
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-emit",
      "x": 160,
      "y": 40,
      "width": 103.5,
      "height": 17,
      "text": "emit events",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800046,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-sub",
      "x": 420,
      "y": 15,
      "width": 86.5,
      "height": 17,
      "text": "subscribe",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800047,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-sub2",
      "x": 420,
      "y": 165,
      "width": 86.5,
      "height": 17,
      "text": "subscribe",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800048,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "caption",
      "x": 140,
      "y": 230,
      "width": 537.0,
      "height": 17,
      "text": "Events = immutable facts; consumers subscribe without coupling",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#868e96",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800049,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    }
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  }
}
```
%%
## Element Links
## Embedded Files

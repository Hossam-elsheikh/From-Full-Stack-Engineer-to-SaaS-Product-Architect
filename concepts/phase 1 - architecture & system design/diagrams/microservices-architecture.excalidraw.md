---
excalidraw-plugin: parsed
tags: [microservices, architecture, gateway]
---
# Excalidraw Data
## Text Elements
API Gateway ^gateway-text
User
Service ^users-text
Order
Service ^orders-text
Payment
Service ^payments-text
User DB ^users-db-text
Order DB ^orders-db-text
Payment DB ^payments-db-text
Loosely coupled services, each owning its own database ^caption
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
      "id": "gateway-box",
      "x": 150,
      "y": 20,
      "width": 240,
      "height": 60,
      "strokeColor": "#7048e8",
      "backgroundColor": "#f3f0ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800011,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "gateway-text",
      "x": 218.25,
      "y": 38.5,
      "width": 103.5,
      "height": 23,
      "text": "API Gateway",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "strokeColor": "#7048e8",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": null,
      "seed": 800012,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "gw-users",
      "x": 190,
      "y": 80,
      "width": 0,
      "height": 40,
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
      "seed": 800013,
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
          0,
          40
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "gw-orders",
      "x": 270,
      "y": 80,
      "width": 0,
      "height": 40,
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
      "seed": 800014,
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
          0,
          40
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "gw-payments",
      "x": 350,
      "y": 80,
      "width": 0,
      "height": 40,
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
      "seed": 800015,
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
          0,
          40
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "users-box",
      "x": 130,
      "y": 120,
      "width": 120,
      "height": 55,
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
      "seed": 800016,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "users-text",
      "x": 155.25,
      "y": 127.5,
      "width": 69.5,
      "height": 40,
      "text": "User\nService",
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
      "seed": 800017,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "orders-box",
      "x": 210,
      "y": 120,
      "width": 120,
      "height": 55,
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
      "seed": 800018,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "orders-text",
      "x": 235.25,
      "y": 127.5,
      "width": 69.5,
      "height": 40,
      "text": "Order\nService",
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
      "seed": 800019,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "payments-box",
      "x": 290,
      "y": 120,
      "width": 120,
      "height": 55,
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
      "seed": 800020,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "payments-text",
      "x": 315.25,
      "y": 127.5,
      "width": 69.5,
      "height": 40,
      "text": "Payment\nService",
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
      "seed": 800021,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "u-db",
      "x": 150,
      "y": 175,
      "width": 0,
      "height": 30,
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
      "seed": 800022,
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
          0,
          30
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "o-db",
      "x": 230,
      "y": 175,
      "width": 0,
      "height": 30,
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
      "seed": 800023,
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
          0,
          30
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "p-db",
      "x": 310,
      "y": 175,
      "width": 0,
      "height": 30,
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
      "seed": 800024,
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
          0,
          30
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "users-db-box",
      "x": 130,
      "y": 205,
      "width": 120,
      "height": 45,
      "strokeColor": "#1971c2",
      "backgroundColor": "#d0ebff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800025,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "users-db-text",
      "x": 155.25,
      "y": 216.0,
      "width": 69.5,
      "height": 23,
      "text": "User DB",
      "fontSize": 14,
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
      "seed": 800026,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "orders-db-box",
      "x": 210,
      "y": 205,
      "width": 120,
      "height": 45,
      "strokeColor": "#e03131",
      "backgroundColor": "#ffc9c9",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800027,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "orders-db-text",
      "x": 231.0,
      "y": 216.0,
      "width": 78.0,
      "height": 23,
      "text": "Order DB",
      "fontSize": 14,
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
      "seed": 800028,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "payments-db-box",
      "x": 290,
      "y": 205,
      "width": 120,
      "height": 45,
      "strokeColor": "#2f9e44",
      "backgroundColor": "#b2f2bb",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "seed": 800029,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "payments-db-text",
      "x": 302.5,
      "y": 216.0,
      "width": 95.0,
      "height": 23,
      "text": "Payment DB",
      "fontSize": 14,
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
      "seed": 800030,
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
      "x": 120,
      "y": 275,
      "width": 469.0,
      "height": 17,
      "text": "Loosely coupled services, each owning its own database",
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
      "seed": 800031,
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

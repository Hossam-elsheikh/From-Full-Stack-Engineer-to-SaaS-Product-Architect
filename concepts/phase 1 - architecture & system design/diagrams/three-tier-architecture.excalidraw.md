---
excalidraw-plugin: parsed
tags: [architecture, tiers, scaling]
---
# Excalidraw Data
## Text Elements
Presentation Tier
UI / HTTP ^presentation-text
request ^l-req
Application Tier
Business Logic ^application-text
Data Tier
Database / Storage ^data-text
read/write ^l-db
Multi-Tier: each tier runs on separate infrastructure ^caption
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
      "id": "presentation-box",
      "x": 100,
      "y": 20,
      "width": 260,
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
      "seed": 800000,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "presentation-text",
      "x": 152.75,
      "y": 35.0,
      "width": 154.5,
      "height": 40,
      "text": "Presentation Tier\nUI / HTTP",
      "fontSize": 16,
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
      "seed": 800001,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "a-pa",
      "x": 230,
      "y": 90,
      "width": 0,
      "height": 40,
      "strokeColor": "#1971c2",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800002,
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
      "type": "text",
      "version": 1,
      "id": "l-req",
      "x": 245,
      "y": 95,
      "width": 69.5,
      "height": 17,
      "text": "request",
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
      "seed": 800003,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "application-box",
      "x": 100,
      "y": 130,
      "width": 260,
      "height": 70,
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
      "seed": 800004,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "application-text",
      "x": 157.0,
      "y": 145.0,
      "width": 146.0,
      "height": 40,
      "text": "Application Tier\nBusiness Logic",
      "fontSize": 16,
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
      "seed": 800005,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "a-ad",
      "x": 230,
      "y": 200,
      "width": 0,
      "height": 40,
      "strokeColor": "#e03131",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800006,
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
      "id": "data-box",
      "x": 100,
      "y": 240,
      "width": 260,
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
      "seed": 800007,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "data-text",
      "x": 148.5,
      "y": 255.0,
      "width": 163.0,
      "height": 40,
      "text": "Data Tier\nDatabase / Storage",
      "fontSize": 16,
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
      "seed": 800008,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-db",
      "x": 90,
      "y": 260,
      "width": 95.0,
      "height": 17,
      "text": "read/write",
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
      "seed": 800009,
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
      "x": 80,
      "y": 350,
      "width": 460.5,
      "height": 17,
      "text": "Multi-Tier: each tier runs on separate infrastructure",
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
      "seed": 800010,
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

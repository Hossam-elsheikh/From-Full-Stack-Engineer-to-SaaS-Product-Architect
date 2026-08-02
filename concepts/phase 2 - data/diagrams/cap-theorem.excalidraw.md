---
excalidraw-plugin: parsed
tags: [cap, consistency, availability, distributed]
---
# Excalidraw Data
## Text Elements
Consistency
(CP) ^c-text
Availability
(AP) ^a-text
Partition Tolerance
(CA impossible) ^p-text
choose 2 of 3 ^l-ca
During a partition pick Consistency or Availability ^l-pick
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
      "id": "c-box",
      "x": 185,
      "y": 20,
      "width": 140,
      "height": 60,
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
      "seed": 800050,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "c-text",
      "x": 203.25,
      "y": 30.0,
      "width": 103.5,
      "height": 40,
      "text": "Consistency\n(CP)",
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
      "seed": 800051,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "a-box",
      "x": 20,
      "y": 170,
      "width": 140,
      "height": 60,
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
      "seed": 800052,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "a-text",
      "x": 34.0,
      "y": 180.0,
      "width": 112.0,
      "height": 40,
      "text": "Availability\n(AP)",
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
      "seed": 800053,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "p-box",
      "x": 350,
      "y": 170,
      "width": 150,
      "height": 60,
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
      "seed": 800054,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "p-text",
      "x": 339.25,
      "y": 180.0,
      "width": 171.5,
      "height": 40,
      "text": "Partition Tolerance\n(CA impossible)",
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
      "seed": 800055,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "c-a",
      "x": 185,
      "y": 90,
      "width": -40,
      "height": 90,
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
      "seed": 800056,
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
          -40,
          90
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "c-p",
      "x": 325,
      "y": 90,
      "width": 55,
      "height": 90,
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
      "seed": 800057,
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
          55,
          90
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "a-p",
      "x": 160,
      "y": 230,
      "width": 230,
      "height": 0,
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
      "seed": 800058,
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
          230,
          0
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-ca",
      "x": 95,
      "y": 130,
      "width": 120.5,
      "height": 17,
      "text": "choose 2 of 3",
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
      "seed": 800059,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-pick",
      "x": 90,
      "y": 260,
      "width": 443.5,
      "height": 17,
      "text": "During a partition pick Consistency or Availability",
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
      "seed": 800060,
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

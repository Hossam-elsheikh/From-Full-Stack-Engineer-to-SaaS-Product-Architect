---
excalidraw-plugin: parsed
tags: [databases, replication, availability]
---
# Excalidraw Data
## Text Elements
Primary
(writes) ^primary-text
Replica 1
(reads) ^replica1-text
Replica 2
(reads) ^replica2-text
writes ^l-write
sync ^l-sync
Replicas serve reads + survive failures; primary owns writes ^caption
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
      "id": "primary-box",
      "x": 20,
      "y": 80,
      "width": 150,
      "height": 80,
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
      "seed": 800061,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "primary-text",
      "x": 56.0,
      "y": 100.0,
      "width": 78.0,
      "height": 40,
      "text": "Primary\n(writes)",
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
      "seed": 800062,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "replica1-box",
      "x": 290,
      "y": 30,
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
      "seed": 800063,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "replica1-text",
      "x": 321.75,
      "y": 40.0,
      "width": 86.5,
      "height": 40,
      "text": "Replica 1\n(reads)",
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
      "seed": 800064,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "replica2-box",
      "x": 290,
      "y": 110,
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
      "seed": 800065,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "replica2-text",
      "x": 321.75,
      "y": 120.0,
      "width": 86.5,
      "height": 40,
      "text": "Replica 2\n(reads)",
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
      "seed": 800066,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "p-r1",
      "x": 170,
      "y": 100,
      "width": 120,
      "height": -40,
      "strokeColor": "#2f9e44",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800067,
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
          120,
          -40
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "p-r2",
      "x": 170,
      "y": 130,
      "width": 120,
      "height": 10,
      "strokeColor": "#2f9e44",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "seed": 800068,
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
          120,
          10
        ]
      ],
      "startBinding": null,
      "endBinding": null
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-write",
      "x": 40,
      "y": 60,
      "width": 61.0,
      "height": 17,
      "text": "writes",
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
      "seed": 800069,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "l-sync",
      "x": 215,
      "y": 55,
      "width": 44.0,
      "height": 17,
      "text": "sync",
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
      "seed": 800070,
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
      "y": 210,
      "width": 520.0,
      "height": 17,
      "text": "Replicas serve reads + survive failures; primary owns writes",
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
      "seed": 800071,
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

# Home

[[Journal/Chronicles|Chronicles]] | [[Journal/Characters|Characters]] | [[Journal/Loot|Loot]] | [[Journal/Quests|Quests]]

![[assets/logo/Brightflameslogo.svg]]

## Players

%% DATAVIEW_PUBLISHER: start

```dataview
TABLE WITHOUT ID
  link(file.name) AS "Character", status as "Status", age + " " + race + " " + gender AS "Description", descriptors AS "Traits"
FROM "Characters/Players"
SORT file.name
```

%%

| Character                                    | Status | Description        | Traits |
| -------------------------------------------- | ------ | ------------------ | ------ |
| [[Characters/Players/Dain.md\|Dain]]         | \-     | Adult Half-orc Man | \-     |
| [[Characters/Players/Jacob.md\|Jacob]]       | \-     | Adult Half-orc Man | \-     |
| [[Characters/Players/Malik.md\|Malik]]       | \-     | \- \- \-           | \-     |
| [[Characters/Players/Mesmer.md\|Mesmer]]     | \-     | \- \- \-           | \-     |
| [[Characters/Players/Ragnar.md\|Ragnar]]     | \-     | \- \- \-           | \-     |
| [[Characters/Players/Svengali.md\|Svengali]] | \-     | \- \- \-           | \-     |
| [[Characters/Players/Tazendal.md\|Tazendal]] | \-     | \- \- \-           | \-     |

%% DATAVIEW_PUBLISHER: end %%

## Sessions

%% DATAVIEW_PUBLISHER: start

```dataview
TABLE WITHOUT ID 
	default(file.link,"") + " " + summary AS "Session",
	saga AS "Saga" 
FROM "Journal" WHERE file.name != "Quests" AND file.name != "Battles" AND file.name != "Loot" AND file.name != "Characters" AND file.name != "Chronicles"
SORT file.name DESC
```

%%

| Session                                | Saga   |
| -------------------------------------- | ------ |
| [[Journal/Sessions/01.md\|01]] Title 1 | Saga 1 |

%% DATAVIEW_PUBLISHER: end %%

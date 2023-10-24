# edi_energy_ahb_conditions_and_packages

Bedingungen und Paket-Definitionen, die aus Anwendungshandbüchern (AHBs) extrahiert wurden.

## Sinn & Zweck

EDI@Energy ([edi-energy.de](https://www.edi-energy.de/)) veröffentlicht Anwendungshandbücher (AHB) in einem unstrukturierten, schlecht maschinenlesbaren Format (PDF oder Word).
Die Anwendungshandbücher enthalten Bedingungen, aus denen hervorgeht, in welchen Fällen welche Informationen in einzelnen EDIFACT-Nachrichten anzugeben sind (vgl. dazu "[Allgemeine Festlegungen](https://www.edi-energy.de/index.php?id=38&tx_bdew_bdew%5Buid%5D=1429&tx_bdew_bdew%5Baction%5D=download&tx_bdew_bdew%5Bcontroller%5D=Dokument&cHash=8e36c79772212df9c240433664b6ffef)" Kapitel 6.4).

Dieses Repository enthält die Definition der Bedingungen (als Text) in einem maschinenlesbaren Format.

### Beispiel

Die Bedingung `[110]` aus dem UTILMD-Anwendungshandbuch:

```json
{
  "condition_key": "110",
  "condition_text": "Wenn SG10 CAV+LGS/ EGS/ BIL/ GEL/ GAL/ SOL/ WNL/ WFL / WAL vorhanden",
  "edifact_format": "UTILMD"
}
```

Diese Struktur heißt [`ConditionKeyConditionTextMapping`](https://ahbicht.readthedocs.io/en/latest/api/ahbicht.html#ahbicht.mapping_results.ConditionKeyConditionTextMapping).
Offensichtlich besteht auch mit der Datengrundlage aus diesem Repository nach wie vor das Problem, dass der fachliche _Inhalt_ der Bedingung (`condition_text`) selbst nicht maschinell interpretierbar ist.

Analog sind hier auch Paket-Definitionen abgelegt; hier exemplarisch das ORDERS-Paket `[5P]`:

```json
{
  "package_key": "5P",
  "package_expression": "[84] ∧ [81] ∧ [82]",
  "edifact_format": "ORDERS"
}
```

Diese Struktur heißt [`PackageKeyPackageExpressionMapping`](https://ahbicht.readthedocs.io/en/latest/api/ahbicht.html#ahbicht.mapping_results.PackageKeyConditionExpressionMapping) und ist mit [ahbicht](https://github.com/Hochfrequenz/ahbicht/) interpretierbar.

## Struktur

Zur Strukturierung nutzen wir nicht die Format- oder AHB-Versionen (z.B. UTILMD `5.2e` oder GPKE AHB `6.1e`), sondern lediglich den Zeitraum zu dem die Daten gültig sind.
Beispielsweise bezeichnet `FV2110` die Datenformate, die seit 2021-10-01 gültig sind oder `FV2304` die Datenformate, die seit 2023-04-01 gültig sind.

Alle Dateien sind mit [prettier](https://www.prettier.io/) formatiert.

## Motivation

Wir freuen uns über jede durch dieses Repository ersparte Stunde Arbeit, in der wichtige Probleme gelöst werden können, anstatt AHBs zu scrapen.
Wir freuen uns auch über jeden Pull Request, der die Datengrundlage verbessert.

## Urheberrecht

Das Urheberrecht der hier versionierten Daten liegt bei EDI@energy bzw. den Autor\*innen der Anwendungshandbücher selbst.
Dieses Repository macht die Daten aus den AHBs lediglich leichter zugänglich.
Hochfrequenz garantiert weder für die Korrektheit noch die Vollständigkeit der hier bereitgestellten Daten, stellt aber auch keine Bedingungen an deren Nutzung.

## Weiterführendes Tooling

Dieses Repository ist Teil der [Hochfrequenz Libraries und Tool für eine echte Digitalisierung der Marktkommunikation](https://github.com/Hochfrequenz/digital_market_communication/).

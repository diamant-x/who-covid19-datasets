ECHO "Downloading WHO data"
python "source\data\raw\who_PfdDownloader.py"
python "source\data\interim\who_PfdParserToCsvInterim.py"
python "source\data\processed\who_CleanupAndHomogenization.py"
python "source\data\processed\who_ConsolidationByStructure.py"
ECHO "Downloading ITA data"
python "source\data\raw\ita_CsvDownloaderRegional.py"
python "source\data\processed\ita_ConsolidateRegional.py"
ECHO "Downloading ESP data"
python "source\data\raw\esp_PfdDownloader.py"
python "source\data\interim\esp_PfdParserToCsvInterim.py"
python "source\data\processed\esp_CleanupAndHomogenization.py"
python "source\data\processed\esp_ConsolidationByStructure.py"
ECHO "Downloading DEU data"
python "source\data\raw\deu_PfdDownloader.py"
python "source\data\interim\deu_PfdParserToCsvInterim.py"
python "source\data\processed\deu_CleanupAndHomogenization.py"
python "source\data\processed\deu_ConsolidationByStructure.py"
ECHO "Consolidating Country Region data"
python "source\data\processed\cross_CountryRegionConsolidation.py"

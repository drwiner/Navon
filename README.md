# Navon

The Navon Project is an application made with Processing (https://processing.org/) to display words in the format of a Navon figure (https://en.wikipedia.org/wiki/Navon_figure). Each letter in the word is at a different level in the navon figure. The Navon Word is thus a Navon figure in which each letter in the figure is composed of the subsequent letter, and so on, except for the last letter which is completely formed. 

Development mode: Enable custom letter formation. In this mode, the user fills in the cells of a grid and submits the design with an associated letter or symbol. This letter is added to the application's database of available letters.

Production mode: The user enters text; if any letter in the text does not correspond to a letter in the database, then a default letter is used. The user enters a direction (the navon word can be compsed from global -> narrow, or vice versa) {footnote: research shows that human attention adopts global precedence and thus should likely more easily read navon words from global -> narrow}. In this mode, the user can use arrow keys to zoom in and out of the figure, or optional parameters for auto zooming can be configured.

The purpose of the Navon project is to investigate how people are able to shift attention across "levels of abstraction". How does zooming through a navon word compare with flashing each letter individually: are people able to read the navon word more easily? The Navon Project could be used to easily generate experimental stimuli to test hypotheses about the nature of attention shifts; to decipher the attention properties associated with narrowing and defocusing attention. 

drwiner@ncsu.edu
David Winer

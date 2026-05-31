#!/usr/bin/env python3
"""Standalone import script for GA153 — GA153 - Inneres Wesen des Menschen und Leben zwischen Tod und neuer Geburt"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA153 - Inneres Wesen des Menschen und Leben zwischen Tod und neuer Geburt"""
GA_NUMBER = "GA153"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "AUFGABE UND ZIEL DER GEISTESWISSENSCHAFT UND DAS GEISTIGE SUCHEN IN DER GEGENWART Öffentlicher Vortrag am 6. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Wer derjenigen Form geisteswissenschaftlicher Weltanschauung, von der ich mir gestatten werde, heute abend und übermorgen zu spre­chen, einen gewissen Wert beimessen will, wird sich schon einmal bekannt machen müssen mit dem eigentümlichen, in der Mensch­heitsentwickelung gelegenen Widerspruche, daß eine geistige Strö­mung, ein geistiger Impuls von einem gewissen, höheren Gesichts­punkte aus in eminentestem Sinne zeitgemäß sein kann und daß dieses also Zeitgemäße dennoch zunächst von der Zeitgenossenschaft scharf zurückgewiesen wird, zurückgewiesen in einer, man möchte sagen, durchaus begreiflichen Weise.",
      "Zeitgemäß war der Impuls zu einer neuen Anschauung vom Weltenall des Raumes, den Kopernikus in der Morgenröte der neuen Zeit gegeben hat, zeitgemäß zweifellos von dem Gesichtspunkte aus, daß die Entwickelung der Menschheit gerade zur Zeit des Kopernikus notwendig machte, daß dieser Impuls kam, und zeitgemäß erwies sich dieser Impuls durchaus noch für lange Zeiten, insoferne als gegen ihn Front gemacht wurde von all denjenigen, die an den alten Denkgewohnheiten, an jahrhundert- und jahrtausendalten Vorurteilen fest­halten wollten. Zeitgemäß in einem solchen Sinne erscheint den Bekennern der hier gemeinten Geisteswissenschaft diese geisteswissen­schaftliche Weltanschauung, und unzeitgemäß ist sie von dem Ge­sichtspunkte aus, von dem sie noch von vielen unserer Zeitgenossen beurteilt werden muß. Dennoch glaube ich im Laufe des heutigen und übermorgigen Vortrages zeigen zu können, daß in unterbewußten Seelentiefen der gegenwärtigen Menschheit etwas wie eine Sehnsucht nach dieser geisteswissenschaftlichen Weltanschauung besteht und etwas wie eine Hoffnung nach ihr lebt.",
      "So wie sie sich zunächst darstellt, will sie sein, diese Geisteswissen­schaft, eine echte Fortsetzerin der naturwissenschaftlichen Geistesarbeit, wie sie in den letzten Jahrhunderten geleistet worden ist, und",
      "ganz unrichtig wäre es, wenn man glauben wollte, daß diese Geistes­wissenschaft von sich selbst aus eine Gegnerschaft enifaltete gegen die großen Triumphe, gegen die unermeßlichen Errungenschaften und die weitblickenden Wahrheiten, welche das naturwissenschaftliche Denken gebracht hat; im Gegenteile, dasjenige, was Naturwissenschaft war und ist für die Erkenntnis der Außenwelt, das will die Geistes­wissenschaft sein für die Erkenntnis der geistigen Welt. So könnte sie geradezu ein Kind der naturwissenschaftlichen Denkweise genannt werden, obwohl dies noch in weitesten Kreisen bezweifelt wird.",
      "Um eine Vorstellung, nicht einen Beweis, zunächst eine Vorstellung, die eine Verständigung hervorrufen soll, anzuführen, sei über das Verhältnis der hier gemeinten Geisteswissenschaft zur naturwissen­schaftlichen Weltanschauung das Folgende gesagt.",
      "Blicken wir auf die große, gewaltige Entwickelung naturwissen­schaftlicher Erkenntnis in den letzten drei bis vier Jahrhunderten, so sagen wir uns, daß sie auf der einen Seite unermeßliche Wahrheiten über den weiten Horizont der naturwissenschaftlichen Denkweise gebracht hat, daß andrerseits dieses Denken eingeflossen ist in das praktische Leben. Überall sehen wir uns entgegenieuchten auf dem Gebiete des kommerziellen Lebens das, was die in die Lebenspraxis hineingeflossene Erkenntnis und die Errungenschaften der Natur­wissenschaft uns gebracht haben. Will man sich eine Vorstellung machen, wie die hier gemeinte Geisteswissenschaft zu diesen Fort-schritten steht, so kann man folgenden Vergleich machen. Man kann hinblicken auf den Bauern, der sein Feld bestellt, der einerntet die Früchte des Feldes: der größte Teil dieser Früchte des Feldes, der eingeerntet wird, wird hereingenommen in das menschliche Leben, zur Nahrung der Menschen verwendet, ein kleiner Teil bleibt übrig, er wird verwendet zur neuen Fruchtaussaat. Nur von diesem letzteren Teile kann man sagen, daß er folgen darf den Triebkräften, den inneren Lebens- und Bildung skräften, die im aufsprossenden Korn und in der Frucht selber liegen. Dasjenige, was in die Scheune geführt wird, wird zumeist abgebracht von seinem in den eigenen Bildungsgesetzen liegenden Fortschritt, wird gleichsam in eine Seitenströmung geführt, zur Menschennahrung verwendet, setzt nicht fort in untnittelbarer",
      "Weise dasjenige, was in dem Keirne liegt, was die eigentlichen Triebkräfte sind. So erscheint der Geisteswissenschaft, die hier gemeint ist, ungefähr dasjenige, was die Naturwissenschaft in den letzten Jahrhunderten an Erkenntnissen gebracht hat. Der weitaus größte Teil ist dazu verwendet worden, Einsicht zu gewähren in die äußeren sinnlichen Tatsachen, ist dazu verwendet worden, in den menschlichen Nutzen einzugehen. Aber zurückbleiben kann gerade von den Ge­danken der letzten Jahrhunderte in der menschlichen Seele etwas, was nicht verwendet wird, um das oder jenes zu begreifen in der sinnlichen Außenwelt, nicht verwendet wird, um Maschinen zu bauen oder Industrie zu pflegen, sondern das lebendig gemacht wird, das erhalten wird in seiner Richtung wie das Korn, das zur Aussaat benützt wird und seinen Bildungsgesetzen folgen darf Wenn der Mensch dies leben läßt in seiner Seele, wenn er ein Gefühl dafür hat, zu fragen: Wie läßt sich das seelische Leben durchleuchten und erkennen an den Begriffen und Ideen, welche die Naturwissenschaft geliefert hat, wie läßt sich tnit diesen Ideen leben, wie läßt es sich von diesen Ideen aus begreifen, wo die Haupttriebkräfte des Seeleniebens liegen? - Wenn die Seele ein Gefühl dafür hat, diese Frage aufzuwerfen tnit der ganzen Fülle des seelischen Lebens, dann erscheint erst dasjenige, was in unserer Zeit in die menschliche Kultur übergeht.",
      "Und auch in ganz anderer Beziehung ist diese Geisteswissenschaft vielfach ein Kind der naturwissenschaftlichen Denkungsweise zu nennen. Nur muß der Geist in einer anderen Art erforscht werden als die Natur. Gerade wenn man auf ebenso sicherer methodischer Basis dem Geiste gegenüberstehen will, wie die Naturwissenschaft der Natur gegenübersteht, muß man das naturwissenschaftliche Denken um­formen, so prägen, daß es ein taugliches Werkzeug für die Erkenntnis des Geistes werden kann. Wie das werden kann, davon soll einiges tnitgeteilt werden.",
      "Gerade wenn man so recht fest steht auf dem Boden der Natur­wissenschaft, da sieht man ein, daß mit den Mitteln, mit denen die Naturwissenschaft arbeitet, eine geistige Erkenntniswissenschaft sich nicht gewinnen läßt. Immer mehr und mehr ist von erleuchteten Geistern gesprochen worden, daß vom sicheren Boden der Naturwissenschaft",
      "ausgehend der Mensch einsehen muß, daß seine Er­kenntnis begrenzt sei. Naturwissenschaft und KanJ haben dazu beigetragen, den Glauben heraufzubringen, daß die Erkenntniskräfte des menschlichen Geistes begrenzte seien, daß der Mensch nicht eindrin­gen könne mit seinem Wissen in den Quell, mit dem sich die Seele verbinden muß.",
      "In dieser Richtung gibt Geisteswissenschaft der Naturwissenschaft völlig recht. Gerade für diejenigen Geisteskräfte und für jene Erkenntnisfähigkeit, welche die Naturwissenschaft groß gemacht haben und auf denen die Naturwissenschaft auch stehen, bleiben muß, für sie gibt es keine Möglichkeit einzudringen in das geistige Gebiet.",
      "Aber in der menschlichen Seele schlummern andere Erkenntnisfähigkeiten, Erkenntnisfähigkeiten, welche im Alltag und im Getriebe der gewöhnlichen Wissenschaft nicht verwendet werden können, die hervorgeholt werden können aus der menschlichen Seele, und wenn sie hervorgeholt werden aus den unergründlichen Tiefen der menschlichen Seele, dann machen sie aus dem Menschen etwas anderes, dann durchleben und durchkraften sie ihn mit einer neuen Erkenntnisart, mit einer solchen Erkenntnisart, welche eindringen kann in Gebiete, welche der bloßen Naturwissenschaft verschlossen sind. Es ist - ich lege einen Wert auf den Ausdruck -, es ist eine Art geistiger Chemie, durch welche man in die geistigen Gebiete des Daseins eindringen kann, aber eine Chemie, welche nur in bezug auf sichere Logik und in bezug auf methodisches Denken Ähnlichkeit hat mit der äußeren naturwissenschaftlichen Chemie.",
      "Es ist die Chemie der Seele selber.",
      "Um uns zu verständigen, sei von diesem Gesichtspunkte aus ver­gleichsweise das folgende gesagt: Wenn wir Wasser vor uns haben -es hat gewisse Eigenschaften, der Chemiker kommt und zeigt, daß Wasserstoff und Sauerstoff darinnen sind. Der erstere brennt, ist gasförmig, ist etwas ganz anderes als das Wasser. Würde jemand, der von Chemie nichts weiß, dem Wasser ansehen können, daß in ihm Wasserstoff ist? Das Wasser brennt nicht, es löscht das Feuer sogar! Dennoch kommt der Chemiker, trennt ab vom Wasser den Wasser­stoff. Mit dem Wasser läßt sich vergleichen der Mensch, wie er im Alltag vor uns steht, wie er ferner vor der gewöhnlichen Wissenschaft",
      "steht: in ihm ist vereinigt Physisch-Leibliches und Geistig-Seelisches. Die äußere Wissenschaft und diejenige Weltanschauung, die sich auf dieser Wissenschaft aufbaut, hat völlig recht, wenn sie sagt: Diesem Menschen, der uns gegenübersteht, kann man nicht ansehen, daß in ihm Seelisch-Geistiges ist. - Und begreiflich ist es, daß diese Weltan­schauung es ableugnet.",
      "Aber diese Ableugnung ist geradeso, als wollte man die Natur des Wasserstoffes ableugnen, weil man das Wasser vor sich sieht. Allerdings, die Notwendigkeit eines Beweises liegt vor, daß das Seelische abgetrennt dargestellt werden kann.",
      "Daß es eine solche geistige Chemie gibt, das ist dasjenige, was Geistes­wissenschaft der Menschheit zu sagen hat, wie der Kopernikanismus der überraschten Menschheit zu sagen hatte, daß die Erde nicht stille steht, sondern in rasendem Tempo um die Sonne sich dreht. Und wie noch bis in das 19.",
      "Jahrhundert hinein Kopernikus' Schriften auf dem Index eines Religionsbekenntnisses standen, werden in gewisser Be­ziehung lange die Erkenntnisse der Geisteswissenschaft auf dem Index anderer Weltanschauungen stehen, die sich nicht losmachen können von dem, was jahrhundertealte Vorurteile und Autoritäten sind. Und daß diese Geisteswissenschaft dennoch bis zu einem gewissen Grade Herz und Seele ergreifen kann, daß sie gerade nicht außerhalb des Suchens unserer Zeit liegt, dafür haben wir ja einen kleinen Beweis, dessen ich mich nicht rühmen will, der aber erwähnt werden darf als ein Zeugnis für das in den Seelen verborgene Zeitgemäße der Geistes­wissenschaft.",
      "Sind wir doch in der Lage, bereits in unserer Zeit dieser Geisteswissenschaft eine freie Hochschule auf freiem schweizerischen Boden in der Nähe von Basel zu bauen und können wir erblicken durch das Verständnis der Freunde dieser Geistesströmung das Wahr­zeichen in dem im Baustile neuen Doppelkuppel-Rundbau, welcher von den Höhen Dornachs heruntergrüßt. Daß dieser Bau schon im Auf­richten ist, daß die Formen dieser Kuppeln schon über den Rundbau sich erheben, das läßt uns heute mit Hoffnung und Befriedigung von Geisteswissenschaft sprechen, trotz all der Gegnerschaft und trotz all des Unverständrisses, das ihr heute noch begegnen muß in weiten Kreisen.",
      "Das, was ich als geistige Chemie bezeichnet habe, ist etwas, was nicht erarbeitet werden kann durch äußere Methoden, dasjenige, was",
      "geistige Chemie genannt werden kann, vollzieht sich lediglich in der menschlichen Seele selber, und Verrichtungen sind es intirn seelisch-geistiger Art, welche die Seele nicht so lassen, wie sie im alltäglichen Leben und in der Wissenschaft ist, sondern die wirken auf die Seele so, daß sie sich umarbeitet, daß sie ein ganz anderes Werkzeug wird, als sie im Alltagsleben ist. Und nicht sind es irgendwelche wunder­bare Verrichtungen aus irgendeinem Aberglauben, die also in geisti­ger Chemie angewendet werden, sondern es sind durchaus innere geistig seelische Verrichtungen, welche sich aufbauen aus dem, was auch im Alltagsleben vorhanden ist, Kräfte der Seele, die immer da sind, die wir im Alltagsleben brauchen, die aber in diesem Ailtags­leben, ich möchte sagen, nebenher verwendet werden, aber die un­ermeßlich gesteigert werden müssen, ins Unbegrenzte sich erkraften müssen, wenn der Mensch wirklich zum geistigen Erkennen kommen soll.",
      "Die eine Kraft, welche sich so nebenher im alltäglichen Leben betätigt, aber unermeßlich gesteigert werden muß, das ist die Auf­merksamkeit.",
      "Was ist Aufmerksamkeit? Nun, wir lassen das Leben, das an der Seele vorüberflutet, nicht so, wie es sonst sich gestaltet, vorüberfluten. Wir raffen uns im Inneren auf, um den geistigen Blick auf dies oder jenes hinzurichten. Einzelne Dinge greifen wir heraus aus dem seeli­schen Leben, stellen sie in das Blickfeld des Bewußtseins, konzen­trieren die Kräfte der Seele auf dieses Einzige. Wir enifachen ein Interesse, das heraushebt einzelne Tatsachen und Wesenheiten aus dem vorüberflutenden Strome des Daseins. Diese Aufmerksamkeit ist im täglichen Leben durchaus notwendig. Man wird immer mehr ein­sehen, wenn Geisteswissenschaft ein wenig in die Seelen eindringt, daß das, was für die Menschen die Gedächtnisfrage ist, im Grunde genommen nur eine Aufmerksamkeitsfrage ist, und daß dies wichtige Gesichtspunkte für die Erziehungsfrage geben wird. Je mehr man sich bemüht beim aufwachsenden Menschen und auch später, die Seele immer mehr in die Tätigkeit der Aufmerksamkeit zu versetzen, desto mehr wird das Gedächtnis gestärkt, desto mehr wächst unser Gedächtnis heran, desto intensiver gestaltet es sich. Und ein anderes",
      "noch! Wer hätte heute nicht gehört von der traurigen Seelenerschei­nung, die man die Diskontinuität des Bewußtseins nennt? Es gibt Menschen, die Lebenslagen haben, in denen sie sich selbst vergessen, die nicht wissen: Du warst mit deinem Ich bei diesem oder jenem Erlebnisse - nicht wissen, was sie durchgemacht haben. Sie können ihr Heim verlassen ohne Sinn und Verstand, erst nach Tagen oder nach Jahren sich wiederfinden und anknüpfen an das, was sie vor vielen Tagen, Wochen, Monaten, Jahren erlebt haben. Niemals würden solche Erscheinungen zu jener Tragik führen können, wenn man wüßte, daß auch diese Integrität, dieses Gesundhalten des Menschen abhängt von einer regelrechten Entwickelung der Aufmerksamkeits­betätigung. So ist Aufmerksamkeitsbetätigung etwas, was wir im gewöhnlichen Leben durchaus bräuchen, sie ist aber auch etwas, was der Geistesforscher entwickeln muß zu einer besonderen inneren Seelenerkraftung. Er muß sie vertiefen zu dem, was man nennen könnte Meditation, Konzentration.",
      "Das sind technische Ausdrücke. So wie wir im gewöhnlichen Leben veranlaßt sind, diesem oder jenem Gegenstande die Aufmerksamkeit zuzuwenden, so verwendet der Geistesforscher aus seiner inneren Willkür alle Seelenkräfte auf ein Bild, eine Gemütsstimmung, auf Willensimpulse, die er überschauen kann, die ganz klar vor seiner Seele sind. Aber so konzentriert er auf sie alle seine Kräfte, daß er wie im tiefen Schlafe alles Denken und Trachten, alle Sorgen, alle Affekte des Lebens so zum Stillstande gebracht hat, wie sie im Still-stande sind im tiefen Schlafe, nur daß er sein Bewußtsein nicht ver­liert, daß er es völlig wach erhält. Aber alle Kräfte der Seele, welche sonst zerstreut sind ins Äußere, sind konzentriert auf eine durch Willkür in den Mittelpunkt des menschlichen Seelenerlebens gestellte Vorstellung, Empfindung oder einen Impuls. Dadurch drängen sich die Seelenkräfte zusammen, und dasjenige, was sonst nur schlummert zwischen den Zeilen des Lebens, das kraftet sich heraus, prägt sich heraus aus der menschlichen Seele. Das tritt tatsächlich ein, daß durch diese innere Erkraftung der menschlichen Seele, innere Konzentra­tionstätigkeit, innere unermeßlich gesteigerte Aufmerksamkeit die See]e sich so in sich erfühlen, erleben lernt, daß sie fähig wird, sich",
      "bewußt herauszureißen aus dem physisch-sinnlichen Leibe, wie der Wasserstoff durch die chemische Methode herausgesondert wird aus dem Wasser. Allerdings, es ist eine innere seelische Erarbeitung, die durch Jahre geht, wenn der Geistesforscher durch seine Konzentra­tionsbetätigung sich dazu befähigen will, sich herauszureißen aus dem physischen Leibe. Dann aber kommt die Zeit, wo der Geistesforscher einen Sinn zu verbinden weiß mit dem Worte: Ich erlebe mich als geistig-seelisches Wesen außerhalb meines Leibes, und ich weiß, daß dieser Leib außerhalb meiner Seele sich befindet. Ich weiß, wenn die Seele sich erkraftet, kann sie sich erleben, auch wenn sie den Leib vor sich hat mit allen seinen Schicksalen! - Der Mensch wird sich in dem, was er selbst ist, vollständig äußerliche Persönlichkeit, erlebt sich als geistig-seelisches Wesen in Absonderung von seinem Leibe. Dieses geistig-seelische Wesen zeigt dann ganz andere Eigenschaften als sonst, wenn es sich mit dem physischen Leibe bedeckt.",
      "Zunächst läßt sich die Denkkraft erleben. Und da ich nicht von Abstraktionen sprechen will, so stoßen Sie sich nicht daran, daß ich ungescheut und vorurteilsfrei dasjenige schildern möchte, was heute noch so paradox klingt. Wenn der Geistesforscher anfängt einen Sinn zu verbinden mit dem Worte: Du erlebst jetzt in deiner Seele auch außerhalb deiner Sinne und des Gehirns -, dann erfühlt er sich in seinem Denken nicht in seinem Kopfe, sondern wie seinen Kopf um-wandelnd und umwebend, ja, er weiß - da man, solange man im Leben zwischen Geburt und Tod steht, immer wiederum in den Leib zurückkehren muß - genau den Moment zu beobachten, wo er wie­derum zurückkehrt mit seinem Denken in sein Nervensystem und Gehirn, wie dieses Gehirn ihm einen Widerstand bietet, wie er unter-tauchen muß, ja er fühlt es, wie er untertaucht und - gestat ten Sie den Ausdruck - einschnappt in sein physisches Gehirn, das jetzt wieder folgt dem, was das Geistig-Seelische vollbringt. Dieses Sich-Erleben außerhalb des Leibes und Wieder-Untertauchen gehört zu den erschütterndsten Erlebnissen des Geistesforschers. Aber dieses rein in sich selber sich erlebende Denken, das außer-halb des Gehirns verläuft, stellt sich anders dar als das physische Denken.",
      "Die physischen Gedanken sind schattenhaft gegen die, welche wie eine neue Welt dastehen vor dem Geistesforscher; es durchdringen sich die Gedanken mit innerer Bildhaftigkeit. Deshalb nennen wir das Imagination, aber nicht aus dem Grunde, weil wir glauben, daß sie etwas Phantastisches, Erdachtes enthält, sondern dasjenige, was wahrgenommen wird, das wird erlebt, imaginiert, aber dieses Imagi-nieren ist ein Untertauchen in die Dinge selbst, man lebt die Dinge, und es stellen sich so die Dinge und Vorgänge der geistigen Welt vor die Seele hin. So kann das Denken abgesondert werden vom physisch-leiblichen Leben, und der Geistesforscher kann sich wissen in der Welt geistiger Vorgänge und Kräfte. Auch andere Kräfte können abgelöst werden aus dem rein Leiblich-Physischen. Dann erlebt der Geistesforscher zunächst sich selber in seiner rein geistig-seelischen Wesenheit.",
      "Aber es ist dasjenige, was er in der geistigen Welt erlebt, eine ganz andere Art des Wahrnehmens als das Wahrnehmen der äußeren sinn­lichen Welt. Da sind die Dinge, ich selbst bin draußen: so ist es nicht vom Augenblicke an, wo man im geistig-seelischen Erleben eine geistige Welt um sich hat, die wirklich mit derselben Notwendigkeit aufsteigt wie um einen Blindgeborenen Farbe und Licht im Augen­blicke, wo er operiert worden ist. Dieses Erleben ist ein solches, daß man mit seinem ganzen Wesen untertaucht in diese Dinge. Dann weiß man: Du nimmst sie wahr, indem du gleichsam ausgeflossen bist in sie. - Man weiß, daß man diese Dinge in der Imagination nachbildet. Man fühlt, daß die Wahrnehmung zugleich Nachbildung ist: man fühlt sich in einer fortwährenden Tätigkeit, nicht in einem passiven Wahrnehmen wie in der äußeren Welt. Deshalb könnte man das Auf­]eben der imaginativen Gedankenwelt eine geistige Mimik, ein geisti­ges Mienenspiel nennen. Dieses Geistig-Seelische ist in fortwährender Tätigkeit. Man reißt sich aus dem Leiblichen heraus, das Seelische ist in fortwährender Tätigkeit. Man fühlt sich etwa so damit verbun­den, wie ein Mensch in der physischen Welt das Seelenieben eines anderen erleben könnte. So erlebt man das, was die Wesen und Vor­gänge der geistigen Welt enthalten: man wird selbst der Ausdruck davon. In der geistigen Miene, die man annimmt, drückt man selbst",
      "das Wesen der Dinge aus. Eine Tätigkeit, ein aktives Wahrnehmen ist es, zu dem man getrieben wird. Und man kann sagen: Geistes­forschung stellt ganz andere Anforderungen an die menschliche Seele als die äußere Wissenschaft, die mehr passiv hinnimmt.",
      "So wie nun das Denken, die Denkkraft als Geistig-Seelisches heraus-gesondert werden kann aus dem Leiblich-Physischen, so kann auch eine andere Kraft, die der Mensch sonst nur im Leibe verwendet, aus diesem Leibe herausgesondert werden. So sonderbar das klingt, diese andere Kraft ist die Sprachkraft, die Kraft, die wir im gewöhnlichen Leben im Sprechen anwenden.",
      "Wie ist es denn, wenn wir sprechen? Unser Gedankenleben läßt mitvibrieren unser Gehirn. Dieses hat seine Verbindung mit dem Sprachapparat, Muskeln werden in Bewegung gesetzt, was wir denken, fließt aus im Wort und lebt im Wort.",
      "Können wir nicht sagen: Indem wir sprechen, ergießen wir, was in unserer Seele ist, in leiblich physi­sche Organe hinaus? - Dadurch, daß der Mensch die Aufmerksamkeit so steigert und noch etwas hinzufügt, was auch ins Unbegrenzte ge­steigert werden muß, entsteht die Loslösung der Sprachkraft vom physisch sinnlichen Leibe. Diese Kraft ist die Hingabe.",
      "Wir kennen sie, diese Kraft, in den Momenten, wenn wir religiös fühlen, wenn wir in Liebe diesem oder jenem Wesen hingegeben sind, wenn wir in treuer Forschung den Dingen folgen, wenn wir unser vergessen; wir kennen sie, diese Hingabe, sie verfließt nur sozusagen zwischen den Zeilen des gewöhnlichen Lebens und der gewöhnlichen Forschung. Der Geistesforscher muß diese Kraft unbegrenzt erkraften, er muß den Strömen des Daseins so hingegeben sein, wie er selbst nur hin­gegeben ist diesen Strömen des Daseins im Schlafe, im tiefen Schlafe, wenn alle Regsamkeit seiner Glieder ruht, wenn alle seine Sinne schweigen und der Mensch ganz hingegeben ist und nichts tut.",
      "Dann ist er im Schlafe in Bewußtlosigkeit verfallen. Wenn sich aber der Mensch durch innere Willkür dazu aufraffen kann, daß er alle seine Tätigkeit unterdrückt, alle Regsamkeit der Glieder unterdrückt, daß er aber wach bleibt und das Gefühl, die Empfindung entwickelt, ein­gegossen dem Strome des Daseins zu sein, nichts zu wollen, als was die Welt für einen will, wenn er dieses Gefühl immer wieder hervorruft",
      "abgesondert von der Steigerung der Aufmerksamkeit, dann er­kraftet sich die Seele immer mehr und mehr durch diese unbegrenzte Hingabe.",
      "Nur müssen diese beiden Übungen abgetrennt gemacht werden, denn sie widersprechen ja einander. Die Aufmerksamkeit fordert Anspannung und Hinlenken zu einem Objekte, die andere Übung tiefe Hingabe, passive Hingabe, wie im religiösen Empfinden etwa oder wie in der Hingabe an ein geliebtes Wesen. Die Früchte, die der Mensch aus der unermeßlichen Steigerung der unbegrenzten Hin-gabe schöpft, sind eben, daß sein geistiges Wesen sich heraussondert aus der physisch4eiblichen Betätigung. Und so kann diejenige Kraft, die sonst in das Wort sich ausgießt, abgetrennt werden von der äußeren Sprachbetätigung, kann im Seelisch-Geistigen bleiben. Dann wird wieder wie durch eine geistige Chemie die Sprachkraft aus ihrer physisch-sinnlichen Verbindung herausgerissen und der Mensch erlebt dasjenige, was man das geistige Gehör, das geistige Hören nennen kann.",
      "Wiederum ist es so, daß der Mensch sich erlebt außerhalb seines Leibes, daß er sich aber erlebt, indem er untertaucht in die Dinge, das innere Wesen dieser Dinge wahrnimmt und es in sich nachlebt wie mit einer inneren Gebärde, mit einer inneren Geste. Wie wenn wir versucht sind, durch ein besonderes Nachahmungstalent, durch be­sondere Gesten dasjenige auszudrücken, was uns beschäftigt. Das macht die Seele, wenn sie sich herausgerissen hat: sie spielt aktiv nach, es ist ein aktives Betätigen. Weil man den Dingen folgt, weil man nachbildet das innere Weben und Wesen der Dinge, nimmt man diese Dinge wahr. In der äußeren sinnlichen Welt sind wir passiv beim Hören, als Geistesforscher tauchen wir unter in das Wesen der Dinge, wir hören ihr inneres Weben. Dasjenige, was Pythagoras die Sphärenmusik genannt hat, ist keine bloße Phantasie: er hört, indem er ausspricht. Ein sprechendes Hören, ein hörendes Sprechen ist es im Untertauchen in das Wesen der Dinge. Die wahre echte Inspiration ist es, die sich also ergibt.",
      "Eine dritte Art inneren Erlebens kann über den Geistesforscher kommen, wenn er die gesteigerte Aufmerksamkeit und Hingabe",
      "weiterentwickelt. Betrachten wir das Kind, das heranwächst. Es ist eine Eigentümlichkeit des heranwachsenden Menschen, daß er sich seine Richtung im Raume, daß er sich die Art und Weise, in den Raum hineingestellt zu sein, selber geben muß im Laufe des Lebens.",
      "Der Mensch wird geboren, indem er nicht gehen, nicht stehen kann, indem er sich, wie man hier in Österreich zu sagen pflegt, aller Viere bedienen muß, um vorwärtszukommen. Dann entwickelt er die Kräfte, die ihn aufrichten, Aufrichtekräfte.",
      "Dadurch tritt dann hervor, was soviele große Geister gefühlt haben, indem sie sagen konnten, daß, wenn der Mensch sich aufrichtet von der horizontalen Richtung zur aufrechten Richtung, sein Blick nicht mehr haftet am Irdischen, sondern er nach oben blickt. Das Wesentliche ist, daß der Mensch durch ein inneres Erleben sich herausentwickelt aus einem hilflosen, horizontalen Leben in das aufrechte vertikale Leben hinein.",
      "Die Naturwissenschafter werden schon sehen, daß das etwas ganz anderes ist als alle die Vererbungskräfte, die dem Tiere seine Richtungskräfte geben. Ganz andere Kräfte wirken im Tiere, die das Tier in diese oder jene Richtung zum Vertikalen bringen, als im Menschen.",
      "Im Menschen wirkt eine Summe von Kräften und reißt ihn heraus aus seiner hilflosen Lage. Diejenigen Raumrichtungskräfte, durch die er eigentlich im wahren Sinne des Wortes Erdenmensch ist, durch die er das erst wird, was er als Mensch auf Erden ist, diese Kräfte wirken sehr im Verborgenen.",
      "Man kommt ihnen nur bei, wenn man sich ein wenig in die Geisteswissenschaft vertieft hat; es ist ein großes System, eine große Summe von Kräften. Nicht alle werden verbraucht im Kindheitsalter, es schlummern noch Kräfte dieser Art im Menschen drinnen, aber sie bleiben unbenützt im äußeren Leben und im wissen­schaftlichen Leben.",
      "Indem der Mensch die Seelenübungen verrichtet, wird er durch die gesteigerte Aufmerksamkeit und Hingabe gewahr, wie in ihm die Kräfte sitzen, die er gehabt hat als Kind: er wird geistiger Richtkräfte sich bewußt. Und die Folge davon ist, daß er zum inneren Mienenspiel, zur inneren Geste auch innere Physiognomie seinem Geistig-Seelischen hinzuzufügen vermag.",
      "Wenn der Mensch anfängt, einen Sinn verbinden zu können mit dem Worte: Dein Leib ist außer dir - dann kommt nach und nach die Zeit heran, wo er sich",
      "der Kräfte bewußt wird, die ihn als physisch-sinnliches Wesen vertikal auf die Erde gestellt haben. Dadurch kommt er in die Lage, diesen Kräften andere Richtungen zu geben, aus sich selber eine andere Gestalt zu machen, als er gemacht hat im Leben seiner Kindheit: er gibt sich nicht nur eine wirkliche Gestalt, er weiß innere Bewegung zu entwickeln, er weiß seinem Geistig-Seelischen eine andere Physio­gnomie zu geben, als er sich als Erdenwesen gegeben hat. Dadurch kommt er dazu, hinunterzutauchen in andere geistige Vorgänge und Wesen, daß er die Kräfte, die ihn vom kriechenden Kinde zum auf­rechten Menschen wandeln, wandelt, daß er innen ähnlich wird den geistigen Dingen und Wesen und dadurch wahrnimmt. Das ist die wahre, reale Intuition. Das wirkliche Wahrnehmen geistiger Dinge und Vorgänge ist ein Untertauchen, ein Einswerden mit den geistigen Dingen. Während man das, was in den Wesen vorgeht, erlebt durch die innere Imagination, so daß man ihre Gesten nachzubilden vermag, vermag man sich selber in die Dinge und Vorgänge zu verwandeln, vermag man die innere geistige Gestalt der Dinge anzunehmen. Man nimmt sie durch geistige Aktivität wahr.",
      "Ich habe Ihnen nicht durch philosophische Ausdrücke schildern wollen, wie sich der Geistesforscher hineinlebt in geistige Vorgänge und Wesenheiten, ich habe möglichst konkret schildern wollen, wie sich die Seele losreißt und untertaucht in die geistige Welt, indem sie aktiv wahrnehmend wird. Es ist klar ersichtlich geworden, daß jeder Schritt in voller Aktivität unternommen werden muß, daß jeder Schritt so sein muß, daß wir nur dadurch das Wesen kennen von den Dingen und Vorgängen der geistigen Welt, wenn wir nachbilden, aktiv nachschaffen können. Das ist der große Unterschied der geistigen Erkenntnis von der äußeren Erkenntnis, daß letztere sich passiv hingibt den Dingen und daß geistige Erkenntnis in fortwährender Aktivität leben muß, daß der Mensch zu dem werden muß, was er wahrnimmt.",
      "Nun, es wird einem heute schon verziehen, wenn man im Allge­meinen von einer geistigen Welt spricht. Das lassen sich die Leute noch gefallen. Das aber wirkt heute noch paradox, daß jemand sagen kann: Der Mensch kann sich loslösen von allem Denken, Fühlen und",
      "Wahrnehmen, das an das Irdische gebunden ist, und sich dann, indem vor ihm alle Welt der Sinne verschwindet, umgeben fühlen von einer neuen, ganz konkreten neuen Welt, in welcher Vorgänge und Wesen rein geistiger Art sind, wie hier in der physischen Welt Vorgänge und Wesenheiten sind. Nicht ein allgemein verschwommener Pantheismus, nicht eine allgemeine Sauce ist es.",
      "Wenn man vom allgemeinen Pantheismus spricht, ist es der Geisteswissenschaft gegenüber, wie wenn man jemand auf eine Wiese führt und sagt, das alles, alle Blüm­chen, alle Käferchen, ist Natur, alles ist Pan-Natur. Die Leute werden wenig zufrieden sein, denn sie wissen: man kommt nur dann zurecht, wenn man die einzelnen Blumen, Käfer und chemischen Vorgänge verfolgen kann.",
      "Ebenso spricht die Geisteswissenschaft von Wahr­nehmungen konkreter geistiger Vorgänge und Wesenheiten. Sie darf sich nicht scheuen, die Zeit herauszufordern, indem sie sich sagt: Wie wir in der Außenwelt die Menschen sehen, unter ihnen die Hierarchie der Tiere, die Hierarchie der Pflanzen, der Mineralien, so schwindet das um uns herum aus dem geistigen Honrizonte, indem wir uns hinein-leben in die geistige Welt, aber es tauchen geistige Reiche auf, geistige Hierarchien, Wesen, die zunächst dem Menschen gleich sind, Wesen, die über dem Menschen stehen, Wesen und Geschöpfe, die höhere Reiche des Daseins füllen, einzelne individuelle geistige Wesen und Geschöpfe. - Wie die Menschenseele sich selbst hineinstellt und zu leben hat in der geistigen Welt, wenn sie den Leib im Tode ablegt und durch die Pforte des Todes gegangen ist, wie sie hindurchgeht durch die geistigen Reiche, davon soll übermorgen die Rede sein.",
      "Was Geisteswissenschaft als ihre Methode ausbildet: man merkt es sofort, es unterscheidet sich sehr wesentlich von dem, was unsere Zeitgenossen zugeben können, was sich herausgebildet hat aus den Denkgewohnheiten der Jahrhunderte und was so festsitzt wie die früheren Vorurteile gegenüber dem Kopernikanischen Weltsysteme. Aber wie muß Geisteswissenschaft sich gegenüber dem Suchen der Zeit verhalten, wenn sie sich recht verstehen will, wenn sie sich recht verhalten will gegenüber diesem Suchen der Zeit?",
      "Der erste Einwand, der uns aus unserer Zeit so leicht gemacht wer­den kann, ist der, daß man sagt: Ja, der Geistesforscher spricht davon,",
      "daß die Seele erst besondere Kräfte entwickeln soll, dann kann sie hineinschauen in die geistige Welt. Wer diese Kräfte noch nicht ent­wickelt hat, wer es noch nicht dazu gebracht hat, zum Abtrennen des Denkens, der Sprachkraft, der Aufrichtekraft, den ginge also die geistige Welt gar nichts an! - Solcher Einwand ist geradeso wie der, der da sagen würde: Denjenigen, der nicht malen kann, den gehen die Bilder nichts an. - Malen kann nur der, der malen gelernt hat, aber es wäre traurig, wenn nur der die Bilder verstehen könnte, der malen kann. Die Seele versteht die Bilder, auch wenn der Mensch nicht selber malen kann, sie hat eine Sprache in sich, welche sich mit der menschlichen Kunst verbindet. Auffinden die Tatsachen und Vor-gänge der geistigen Welt und sie schildern, das kann nur derjenige, der selbst zum Geistesforscher geworden ist. Wenn aber der Geistes-forscher sich bemüht, dasjenige, was er erforscht, in Worte der ge­wöhnlichen Gedanken und Ideen zu kleiden, dann ist das, was er so gibt, begreiffich jeder Seele, auch derjenigen, die kein Forscher ge­worden ist, wenn sie nur hinwegzunehmen vermag, was aus der zeit­genössischen Bildung kommt, die sich gibt, als ob sie auf dem festen Boden der Naturwissenschaft stünde, aber in Wahrheit dies nur glaubt. Wenn sich die Seele nur aller Vorurteile begibt, wenn sie sich nur unbefangen wie dem Betrachten eines Bildes hingibt, dann ist jeder imstande, das Ergebnis der Geistesforschung zu verstehen.",
      "Die Menschenseele ist zur Empfindung der Wahrheit veranlagt, und tief ist in den Menschenseelen, wenn sie sich nur selber verstehen wollen, eine geheime, intime Sprache, eine Sprache, durch die jeder, auf welcher Bildungs- und Entwickelungsstufe er stehe, den Geistes-forscher verstehen kann, wenn er ihn nur verstehen will. Das ist es aber gerade, was der Geistesforscher in dem Suchen unserer Zeit findet. In verflossenen Jahrhunderten hat der Mensch allein nur durch Glaubensvorstellungen etwas wissen wollen über die geistige Welt, in späterer Zeit haben die Menschen geglaubt, daß ein sicheres Wissen sich nur auf die äußeren Tatsachen aufbaue. In unserer Zeit wissen es die Seelen zwar noch nicht, im Oberbewußtsein sitzt es noch nicht, aber für den Geistesforscher ist es klar: wir leben in einer Zeit, in der sich in den Tiefen der Menschenseele, von denen die Seele nichts",
      "weiß, vorbereitet Sehnsucht nach der Geisteswissenschaft, Hofinung auf diese Geisteswissenschaft. Immer mehr und mehr wird man er-kennen, daß alte Vorurteile schwinden müssen. Namentlich in bezug auf das Denken wird man da so manches erkennen.",
      "So wird es heute noch viele Menschen geben, gerade diejenigen, welche glauben, auf dem festen philosophischen Boden zu stehen, welche sagen: Haben es nicht Kant und die Philosophie bewiesen, daß der Mensch nicht hinuntertauchen kann mit seinem Wissen? Kommt nun da eine solche Geisteswissenschaft, will Kant bekämpfen und will zeigen, daß das nicht richtig ist, was die moderne Philosophie zeigen will! - Ja, Geisteswissenschaft will gar nicht zeigen, daß das unrichtig ist, was Kant von seinem und die moderne Wissenschaft von ihrem Stand­punkte aus sagt, aber die Zeit wird lehren, daß es noch andere Ge­sichtspunkte gegenüber richtig und unrichtig gibt als diejenigen, an die man sich gewöhnt hat.",
      "Nehmen wir an, wie sich zum Beispiel die wirkliche Lebenspraxis verhält. Da könnte jemand kommen und klar beweisen, daß der Mensch mit seinen Augen unfähig ist, jemals Zellen zu sehen, die als kleinste Organismen den großen Organismus aufbauen.",
      "Dieser Beweis könnte ganz richtig sein, so richtig sein, als der Kant'sche oder philosophische Beweis richtig ist. Nehmen wir an, wir lebten in einer Zeit, in der das Mikroskop noch nicht erflinden sei, und jemand käme und würde scharfsinnig beweisen, der Mensch könne mit seinen Augen die kleinsten Teile nicht sehen.",
      "Der Beweis könnte klappen und nichts könnte einzuwenden sein. Aber darauf kam es nicht an im wirklichen Fortgang der Forschung, vielmehr darauf kam es an, trotz alledem zu zeigen, daß physische Werkzeuge unmittelbar gefunden werden können, um dasjenige zu erreichen, was ganz zu beweisen nicht möglich sein würde, wenn die Fähigkeiten unbewaffnet blieben.",
      "Recht haben diejenigen, die da sagen, die mensch­lichen Fähigkeiten sind begrenzt. Die Geisteswissenschaft widerspricht dem ja nicht, sie zeigt nur, daß es eine geistige Erkraftung und Ver­stärkung menschlicher Erkenntniskräfte gibt, wie etwa das Mikro­skop und Teleskop im äußeren Leben, und daß trotz der Richtigkeit des entgegengestellten Gedankenganges die fruchtbare Geistesfor­schung sich gerade jenseits eines solchen Richtigen und Unrichtigen",
      "stellen muß. Die Menschen werden lernen, nicht mehr so zu pochen auf das, was sich mit den beschränkten Mitteln beweisen läßt, sie wer­den einsehen, daß das Leben andere Anforderungen an die Menschheits-entwickelung stellt als dasjenige,was man oft nur so logisch sicher nennt.",
      "Und ein anderes muß gesagt werden, wenn das wirkliche Suchen der Zeit, nicht das eingebildete Suchen der Zeit, in Beziehung gebracht wird mit dem, was der Geistesforscher als Aufgabe und Ziel hat. Noch einmal muß hingewiesen werden auf die gewaltigen, großen Fortschritte der Naturwissenschaft.",
      "Es ist ihnen gegenüber nicht zu verwundern, daß es heute Geister gibt, die glauben auf dem festen Boden der Naturwissenschaft ein Weltgebäude aufzurichten. Es gibt heute schon eine solche Geistesrichtung; sie nennt sich nobler die monistische Geistesströmung.",
      "Diese Geistesströmung, deren Ober­haupt der ganz gewiß auf seinem naturwissenschaftlichen Gebiete große Haecke/, deren Feldmarschall Ostwa/d ist, sie versucht durch einen Ausbau dessen, was nur aus Naturerkenntnis gewonnen werden kann, eine Weltanschauung aufzubauen. Das Suchen der Zeit wird gegenüber einem solchen Versuche zu folgendem Ergebnis kommen.",
      "Solange die Naturwissenschaft dabei stehen bleibt, die Gesetze des äußerlich sinnlichen Daseins zu erforschen und Zusammenhänge des äußeren sinnlichen Daseins vor der Seele zu vergegenwärtigen und darzustellen, steht sie auf richtigem Boden, auf festem Boden. Sie hat wahrhaftig Großes geleistet, daß sie alten Vorurteilen das Lebens-licht gründlich ausgeblasen hat.",
      "So wie noch Faust selbst vor der Natur gestanden und zu einer äußeren, materiellen Magie gegriffen hat, so kann derjenige, der heute die Naturwissenschaft versteht, nicht mehr zu einer äußeren, materiellen Magie greifen. Aber ein anderes ist es, daß das geistige Leben selber auf dem Wege, der charakterisiert worden ist, eine innere Magie der Seele zeigt.",
      "Gegen alle theoretische Naturerklärung, gegen allen Aberglauben, gegen alle Geistesströmung, die die äußere Natur so erklären will, daß sie dieses oder jenes Wesen findet hinter den Naturerscheinungen so, wie man einen Dämon hinter den Rädchen einer Uhr sucht, hat die Naturwissenschaft ihr Großes geleistet in der Negation dieser Weltanschauung. Solange die Geister sich damit befassen, das alte Ungesunde zu bekämpfen, solange",
      "Front gemacht werden kann gegen solche Geistesströmung, solange lebt eine solche Naturwissenschaft von dem, was bekämpft werden mußte. Aber dieser Kampf hat den Höhepunkt schon überschritten, er hat sein Gutes schon geleistet. Nun gilt es nicht mehr den Kampf zu führen, sondern zu fragen: Mit welchen Mitteln können wir eine Weltanschauung bilden, in welcher die Seele lebend Platz hat? Da versagt der Haeckelsche Monismus. Immer klarer und klarer wird es werden, daß die Naturwissenschafter groß waren als Soldaten, als Krieger im Bekämpfen des alten Aberglaubens, daß sie aber sind wie Krieger, die den Krieg vollendet haben und heimkommen und nicht die Kräfte haben, um Industrien zu entwickeln, Ackerbau zu treiben. Der Naturwissenschaft soll nicht ihre Größe genommen werden, wenn sie hingestellt wird als Bekämpfer abergläubischer Vorstellun­gen. Solange die Denker stehen bleiben im Kampfe, haben sie etwas, was sie aufrecht hält; wenn aber der Mensch eine Weltanschauung sich aufbauen will, in welcher in den Vorstellungen die Seele einen Platz hat, da stehen sie als Krieger da, die keinen Platz haben in Friedenszeiten, und es baut sich eben keine Weltanschauung auf.",
      "Diese Stimmung kann der Geistesforscher schauen in den Unter­gründen der Seele. Das ist das Geheimnis der heutigen Zeit. Aber wenn sie so von einem höheren Gesichtspunkte aus durchaus zeit­gemäß ist, diese geistesforscherische Weltanschauung, sie ist unzeit­gemäß vor vielen Zeitgenossen, die nicht tief genug hineinschauen in das, was sie eigentlich selber wollen. Daher bringt diese Geistes­wissenschaft zunächst ein Weltenbild, das sich so ansieht, als ob es nicht auf einem festen wissenschaftlichen Boden stünde. Das Welten-bild des Monismus will nur auf der Grundlage der äußeren Welt und Wissenschaft aufgebaut sein. In innerer Aktivität der Geistesforschung ergibt sich für die Seele, was die Seele erhebt zur Geistesgemeinschaft, ergibt sich die Geisteswelt in wahrnehmbarer Aktivität. Durch die Geisteswissenschaft kann der Mensch wieder wissen von der wahren Geisteswelt. Davon weiß das sogenannte monistische Weltenbild nichts zu sagen.",
      "Dieses Suchen der menschlichen Seele läßt sich nicht unterdrücken, und so hat sich ein Teil unserer Zeitgenossen schon daran gewöhnt,",
      "die Gedanken gleichsam in sich selber so zu stellen, daß sie laufen wie die Gedanken der äußeren Naturwissenschaft. Was ist geworden? Das ist geworden, daß ein Teil unserer Zeitgenossen - die sich damit be­schäftigen, die wissen es - darauf verfallen ist, das Geistige so ansehen zu wollen, wie man das Sinnliche anschaut.",
      "Ich sage nicht, daß nicht auf diesem Wege etwas durchaus Wahres zustande kommen kann, aber die Methode ist eine andere. Dasjenige, was man Spiritismus nennt mit allen seinen Auswüchsen, das will äußerlich ohne Aktivität in der Wahrnehmung geistige Wesenheiten und Vorgänge äußerlich passiv anschauen, so wie man physisch-sinnliche Vorgänge anschaut.",
      "Wessen Kind ist dieser rein äußerliche Spiritismus? Das Kind jener Geistesströmung, die auf dem Standpunkte der monistischen Strö­mung steht und dem Aberglauben des Materialismus sich hingibt. Was, wird ein Zeitgenosse sagen, der Spiritismus ein Kind des echten Haeckelschen Monismus? - Die Welt wird sich überzeugen, daß es mit diesem Kinde so geht wie im Leben.",
      "Mancher Vater, manche Mutter hat die schönsten Gedanken über all das, was im Kinde sich entwickeln soli, und es kann doch ein rechter Balg entstehen. Was der Monismus sich als wirkliche Kulturerrungenschaft erträumt, was er der Menschheit geben will, auf das kommt es nicht an: der bloße Glaube an das Materielle wird den Glauben erzeugen, daß die Geister materiell sich betätigen.",
      "Je mehr der rein monistische Materiallsmus wachsen würde, umsomehr würden spiritistische Gesellschaften auf-blühen als das notwendige Gegenbild. Je mehr es den Bekennern der Haeckel- und Ostwald'schen Richtung gelingen wird, wahre Geisteswissenschaft zurückzudrängen, destomehr werden sie sehen, daß sie züchten werden den Spiritismus, die Kehrseite der wahren Geisteswissenschaft.",
      "So sicher der Geistesforscher steht auf dem Boden des erkennenden, des wißbaren Geisteswissens, so wenig kann er der Methode folgen, die den Geist materialisieren will, so wenig kann er sich hingeben dem passiven Forschen des materialistischen geistigen Lebens.",
      "Ein Mann, der als Philosoph eine gewisse Schätzung verdient, hat einen sonderbaren Aufsatz in einer viel gelesenen Zeitschrift geschrie­ben. Er schrieb zum Beispiel, daß Spinoza und Kant für manche",
      "Menschen schwer zu lesen sind, man liest sich hinein, aber da wandeln und wirbeln die Begriffe nur so dahin. Es soll nicht geleugnet werden, daß es für die meisten Menschen so ist, daß die Begriffe durchein­anderwirbeln. Jener Philosoph gibt einen Ratschlag, wie man das gemäß dem Suchen unserer Zeit anders gestalten könnte. Er sagt :",
      "Wir haben ja heute eine Einrichtung, einen technischen Fortschritt, durch den das, was bloß in abstrakten Gedanken die Seele verwirrt, recht anschaulich vor die Seele gebracht werden kann. - Der Philosoph will in einer Art von Kino zeigen, wie Spinoza zunächst dasitzt und Glas schleift, wie der Gedanke der Ausdehnung über ihn kommt, der sich verwandelt in das Bild des Denkens und so weiter. So könnte die ganze Spinoza'sche Ethik und Weltanschauung aufgebaut werden auf kinematographische Weise. Dem Suchen der Zeit wäre Rechnung getragen. Merkwürdig, daß der Herausgeber dieser vielgelesenen kine­matographischen Schrift die Anmerkung gemacht hat, so könnte dem uralten metaphysischen Bedürfnisse des Menschen durch eine Er­findung, die manchen als Spielerei erscheint, abgeholfen werden.",
      "Nun könnte es ja von einer gewissen Seite her dem äußeren Suchen der Zeit angemessen sein, wenn man Spinozas Ethik im Kino oder im Film Kants Kritik der reinen Vernunft ablesen könnte. Warum denn nicht? Das liebt unsere Zeit. Wir können uns überzeugen, daß man diese passive Hingabe liebt. Sehen wir uns einmal an, sagen wir, die Anschlagsäulen, versuchen wir die Gedanken der Menschen zu erraten, die davorstehen. Zu einem Vortrage, wo keine Lichtbilder gegeben werden, wo darauf reflektiert wird, daß die Seele aktiv mit-arbeitet, sind die Menschen schwer zu haben. Sie werden s ich lieber dorthin begeben, wo man sich nur passiv hinzugeben braucht. Wenn man aber in die Tiefen der Zeit hineinschaut, weiß man, daß in der Seele doch ruht der Trieb nach Aktivität, der Trieb, sich wiederzu­finden als Seele in voller Aktivität. Frei, mit sicherem innerem Halt bedacht, kann die Seele nur sein, wenn sie innere Aktivität hat. Im Leben sich zurechtfinden, sich orientieren kann die Seele nur, wenn die Seele sich bewußt wird und wenn sie weiß, daß sie dabei ist bei dem, was sie in Tätigkeit zu erleben vermag. Und von der Geisteswelt vermag sie nur das einzusehen, was sie tätig zu erleben weiß, was sie",
      "sich in Tätigkeit zu erringen weiß. In der Geistesforschung wird Wahrnehmen zugleich eine Art Mitarbeit : dadurch wird Geistes­wissenschaft zu einer Erweckung der tief unterbewußten Triebe der Seele. Im geisteswissenschaftlichen Denken wird Mitdenken zu einer Tätigkeit, zu einer Aktivität.",
      "Dadurch kommt sie entgegen dem in­timsten Suchen unserer Zeit. Denn in bezug auf die hier berührten Dinge ist unsere Zeit eine Zeit des Überganges. Es ist leicht und trivial zu sagen, wir leben in einer Übergangszeit, denn jede Zeit ist eine Übergangszeit.",
      "Daher ist ein solcher Ausspruch richtig, aber banal. Es kommt darauf an, zu wissen, worin in einer solchen Zeit der Übergang besteht. Will man unsere Zeit in ihren Übergängen schildern, muß man sagen : Es ist notwendig - denn dadurch konnten die Naturwissenschaften und was durch sie groß geworden ist, zu ihren Errungenschaften kommen -, daß einmal die Menschheit durch Jahrhunderte durch die Erziehung zur Passivität gegangen ist.",
      "Denn nur so, durch die Hingebung an die materialistischen Wahrheiten, konnte erreicht werden, was erreicht werden mußte. Aber es ist im Leben so, daß alles sich rhythmisch abspielt, wie ein freies Pendel.",
      "So muß die Menschenseele, wenn sie erzogen worden ist durch Jahr­hunderte in treuer, passiver Hingabe, sich aufraffen zur Aktivität, um sich zu finden. Denn was ist sie durch die Passivität geworden? Das­jenige, was sie geworden ist durch die Passivität, werde ich ungescheut aussprechen mit dem radikal klingenden Satze, der für viele zwar viel zu paradox klingt.",
      "Aber auf der anderen Seite zeigt gerade das Einleben in die Geisteswissenschaft, daß, wenn man dieses radikale Ergebnis nicht betont, man sich nicht zur Konsequenz aufrafft. Man hat nicht den Mut, die wirkliche Konsequenz zu ziehen, auch bei den­jenigen nicht, welche vorgehen, einzig und allein auf dem Boden der Naturwissenschaft zu stehen.",
      "Denn hätte man den Mut, dann würde man merkwürdige Worte äußern hören im Suchen der Zeit.",
      "Am Ausgangspunkte der alttestamentlichen Urkunden stehen die Worte - jeder mag sie nehmen, wofür er sie nehmen kann, er mag sie für ein Bild oder eine oberflächliche oder tiefere Tatsache halten; in dem, was ich darüber zu sagen habe, können alle übereinstimmen - : «Ihr werdet sein wie Gott, und unterscheiden das Gute und Böse!»",
      "Es klingt uns das Wort herüber aus dem Anfang des Alten Testarnen­tes. Wie man es auch nehmen will, das wird man zugeben müssen, daß es ein Bedeutungsvolles ausdrückt für die Menschennatur. Dem Versuchet wird es zugeschrieben, der herannaht an den Menschen und ihm ins Ohr sagt : «Wenn du mir folgst, so witst du sein wie ein Gott und unterscheiden das Gute und Böse.» Das wird man einsehen können; alle menschliche Freiheit und Selbständigkeit hängt mit dem zusammen, was diese Worte ausdrücken.",
      "Aber sie drücken aus, daß der Mensch gewissermaßen aufgefordert wurde durch den Ver­sucher, über sich hinaus sich anzuschauen wie ein anderes Wesen als er ist, wie ein Gott sich zu verhalten zu dem Guten und Bösen. Mag man über dieses Wort und den Versucher denken, wie man will.",
      "Dieser Versucher - ich fordere nicht, daß man ihn hinnimmt wie ein wirkliches Wesen, obschon : «Den Teufel spürt das Völkchen nie, und wenn er sie beim Kragen hätte» - wie man ihn auch nehmen mag, derjenige, der das Suchen der Zeit ein wenig zu belauschen vermag, der hört denn doch sein Raunen wieder, er nahet sich : da ist er - ohne allen Aberglauben mag es gesagt werden, da ist er, und für diejenigen, welche den Mut haben, die letzte Konsequenz der reinen naturwissenschaftlichen Weltanschauung zu ziehen, bringt er Worte einer großen Eigentümlichkeit, einer sonderbaren Weisheit hervor. Sie haben nur nicht den Mut zur letzten Konsequenz, denn sie nehmen doch den Glauben auf an eine Unterscheidung des Guten und Bösen.",
      "Sie müßten diesen Glauben ableugnen, wenn sie rein auf dem Boden der bloßen naturwissenschaftlichen Notwendigkeit sich stellten. Sie müßten sagen : Es scheint die Sonne gleichmäßig über Gute und Böse - sie müßten sagen, daß das Böse geradeso verrichtet wird wie das Gute.",
      "Es raunt der Versucher die Konsequenz der bloßen naturwissenschaftlichen Weltanschauung : Ihr seid ja nur höher entwickelte Tiere, ihr seid ja Tiere - und das ist, was der Ver­sucher spricht : Ihr seid ja nur entwickelte Tiere und dürft, wenn Ihr Euch selbst versteht, keinen Unterschied machen zwischen dem Guten und Bösen. - Das ist es, was unsere Zeit zu einer Übergangszeit macht, daß der Versucher mit der das Entgegengesetzte zuraunenden Stimme in unserer Zeit wieder spricht.",
      "Hätte man den Mut, so wäre das die Konsequenz der bloß passiven Hingabe an die naturwissenschaftliche Erkenntnis. Daß die Zeit be­wahrt bleibe vor dieser Stimme, daß in das Suchen der Zeit hinein­gebracht werde Wissen vom geistigen Leben, das ist die Aufgabe, das Ziel der Geisteswissenschaft.",
      "Diejenigen, die diese Geisteswissen­schaft noch bekämpfen vom Standpunkte einer Wissenschaft, sie werden sich überzeugen müssen, daß es sich mit diesem Kampfe so verhält, wie es sich mit dem Kampfe gegen den Kopernikanismus verhielt. Jetzt, wo wir durch unseren Bau in Dornach hervorgetreten sind und mehr beachtet werden, mehren sich auch die Stimmen der Gegner.",
      "Als ich auf solche Stimmen einwendete, daß die Gegner auf jenem Standpunkte stehen, da sagte einer, der sich betroffen fühlte mit Recht, der Unterschied wäre nur der, daß das, was Kopernikus sagte, Tatsachen seien und daß das, was die Geisteswissenschaft bringe, nur Behauptungen seien - er merkt nur nicht, der Arme, daß für die Leute damals die Lehren des Kopernikus auch nichts anderes waren als leere Behauptungen. Er merkt nicht, daß es sich hier um Tatsachen geistigen Lebens handelt, daß er heute leere Behauptungen nennt, was vor einer wirklichen Forschung Tatsachen des geistigen Lebens sind.",
      "Und so kann man Einwand über Einwand aus dem Suchen unserer Zeit heraus erhoben finden von der Wissenschaft und von seiten des religiösen Lebens. Aber so wie diejenigen Menschen mit sich zurechtgekommen sind, welche zur Zeit des Kopernikus gesagt haben : An die Umdrehung der Erde können wir nicht glauben, sie steht nicht in der Bibel, - so sagen die Leute heute : An das, was die Geisteswissenschaft zu sagen hat, glauben wir nicht, es steht nicht in der Bibel. - Doch, so werden die Menschen mit dem, was die Geisteswissenschaft zu sagen hat, zurechtkommen, wie die Bibel-gläubigen mit der Sache des Kopernikus zurechtgekommen sind.",
      "Immer wieder muß erinnert werden an einen zugleich gelehrten, tief gelehrten Mann und Priester, der an der hiesigen Universität ge­wirkt hat, Rektor dort war. Als er seine Rektorrede gehalten hat über Galilei, sagte er : Damals standen die Leute, die da an Religiöses glaubten, auf dem Standpunkte des Glaubens; heute weiß der wahr­haft religiöse Mensch, daß durch jede neue Wahrheit, die erforscht",
      "wird, ein Stück zu der Herrlichkeit der göttlichen Weltordnung hinzu­gefügt wird. - So könnte man annehmen, vor Kolumbus wäre jemand hingetreten und hätte gesagt : Das neue Land dürfen wir nicht ent­decken, wir leben in einem schönen Lande, in dem die Sonne scheint; wissen wir denn, daß die Sonne auch die Kraft hat, das neue Land zu bescheinen? So kommen dem Religösen, der an seinem Glaubens-dogma hängt, die Entdeckungen der Geisteswissenschaft vor, und so kommen dem Geistesforscher diejenigen vor, die die religiösen Empfindungen gestört glauben durch die Entdeckungen der Geistes­wissenschaft. Der muß eine wankende religiöse Vorstellung, einen schwachen Glauben haben, der da glauben kann, diese göttliche Sonne werde nicht auch das neue geistige Land bescheinen. Die Zeit aber in ihrem Suchen, wenn sie immer mehr und mehr sich durchdringen wird mit Geisteswissenschaft, sie wird davon so berührt werden, wie manche heute es noch nicht sich träumen lassen. Geisteswissenschaft hat begreiflicherweise noch viele Gegner, aber im Einklang fühlt man sich doch in dieser Geisteswissenschaft mit all denjenigen Geistern der Menschheit, die, wenn sie auch noch nicht Geisteswissenschaft gehabt haben, doch geahnt haben jenen Zusammenhang der Men­schenseele mit den geistigen Welten, der eben durch die Geistes­wissenschaft aufgeschlossen wird.",
      "So fühlt man sich gerade in bezug auf das, was über das neue Wort des Versuchers gesagt worden ist, im Einklange mit fchilkr und seinem Ahnen der geistigen Welt. Er hat durchaus den Impuls bekommen, den Menschen mit seiner Seele herauszuheben aus der bloßen Tierheit, hat gewußt, daß der Mensch seinen Anteil hat an der geistigen Welt. Man fühlt sich im tiefen Einklang mit diesem führenden Geiste der neuen geistigen Weltanschauung, man empfindet, daß man dasjenige, was heute mit breiteren Sätzen ausgeführt werden sollte, wie in ein Gefühl zusammenfassen kann mit den Schillerschen Worten : Die Tierheit wich! Bekräftigend dies steht die Geisteswissenschaft gegen­über dem Versucher der heutigen Zeit.",
      "Es darf erinnert werden an einen Geist, der hier in Österreich gewirkt hat, der gefühlt hat in seiner tiefen Seele den dunklen Drang dessen, was die Geisteswissenschaft zur Gewißheit erhebt. Gefühlt",
      "hat er es, mit seinem Denken einsam dastehend, an geistigen Aus­blicken festhaltend, trotzdem er als Arzt auf dem Boden der Natur­wissenschaft stand : Ernst Freiherr von Feuchtersleben, der tief gemütvolle Mensch. Und zusammengefaßt sei dasjenige, was heute gesagt worden ist, in den Worten Feuchterslebens, in denen lebt, was in der Seele erfühlt werden kann als geistige Kraft, wenn sie sich mit Geistes­wissenschaft erfüllt hat, wenn sie sich gewiß ist ihres Zusammen­hanges mit der geistigen Welt : « Die menschliche Seele kann es sich nicht verhehlen, daß ihr wahres, berechtigtes Glück doch nur liegt in der Erweiterung ihres inneren Wesens und Besitzes.» Die Erweiterung, die Befestigung, die Sicherung dieses inneren Wesens, dieses geistigen Innenwesens der Seele, soll dem Sucher der Zeit durch die Geistes­wissenschaft dargeboten werden!"
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Wer derjenigen Form geisteswissenschaftlicher Weltanschauung, von der ich mir gestatten werde, heute abend und übermorgen zu spre­chen, einen gewissen Wert beimessen will, wird sich schon einmal bekannt machen müssen mit dem eigentümlichen, in der Mensch­heitsentwickelung gelegenen Widerspruche, daß eine geistige Strö­mung, ein geistiger Impuls von einem gewissen, höheren Gesichts­punkte aus in eminentestem Sinne zeitgemäß sein kann und daß dieses also Zeitgemäße dennoch zunächst von der Zeitgenossenschaft scharf zurückgewiesen wird, zurückgewiesen in einer, man möchte sagen, durchaus begreiflichen Weise."
      ],
      [
        "Zeitgemäß war der Impuls zu einer neuen Anschauung vom Weltenall des Raumes, den Kopernikus in der Morgenröte der neuen Zeit gegeben hat, zeitgemäß zweifellos von dem Gesichtspunkte aus, daß die Entwickelung der Menschheit gerade zur Zeit des Kopernikus notwendig machte, daß dieser Impuls kam, und zeitgemäß erwies sich dieser Impuls durchaus noch für lange Zeiten, insoferne als gegen ihn Front gemacht wurde von all denjenigen, die an den alten Denkgewohnheiten, an jahrhundert- und jahrtausendalten Vorurteilen fest­halten wollten.",
        "Zeitgemäß in einem solchen Sinne erscheint den Bekennern der hier gemeinten Geisteswissenschaft diese geisteswissen­schaftliche Weltanschauung, und unzeitgemäß ist sie von dem Ge­sichtspunkte aus, von dem sie noch von vielen unserer Zeitgenossen beurteilt werden muß.",
        "Dennoch glaube ich im Laufe des heutigen und übermorgigen Vortrages zeigen zu können, daß in unterbewußten Seelentiefen der gegenwärtigen Menschheit etwas wie eine Sehnsucht nach dieser geisteswissenschaftlichen Weltanschauung besteht und etwas wie eine Hoffnung nach ihr lebt."
      ],
      [
        "So wie sie sich zunächst darstellt, will sie sein, diese Geisteswissen­schaft, eine echte Fortsetzerin der naturwissenschaftlichen Geistesarbeit, wie sie in den letzten Jahrhunderten geleistet worden ist, und"
      ],
      [
        "ganz unrichtig wäre es, wenn man glauben wollte, daß diese Geistes­wissenschaft von sich selbst aus eine Gegnerschaft enifaltete gegen die großen Triumphe, gegen die unermeßlichen Errungenschaften und die weitblickenden Wahrheiten, welche das naturwissenschaftliche Denken gebracht hat; im Gegenteile, dasjenige, was Naturwissenschaft war und ist für die Erkenntnis der Außenwelt, das will die Geistes­wissenschaft sein für die Erkenntnis der geistigen Welt.",
        "So könnte sie geradezu ein Kind der naturwissenschaftlichen Denkweise genannt werden, obwohl dies noch in weitesten Kreisen bezweifelt wird."
      ],
      [
        "Um eine Vorstellung, nicht einen Beweis, zunächst eine Vorstellung, die eine Verständigung hervorrufen soll, anzuführen, sei über das Verhältnis der hier gemeinten Geisteswissenschaft zur naturwissen­schaftlichen Weltanschauung das Folgende gesagt."
      ],
      [
        "Blicken wir auf die große, gewaltige Entwickelung naturwissen­schaftlicher Erkenntnis in den letzten drei bis vier Jahrhunderten, so sagen wir uns, daß sie auf der einen Seite unermeßliche Wahrheiten über den weiten Horizont der naturwissenschaftlichen Denkweise gebracht hat, daß andrerseits dieses Denken eingeflossen ist in das praktische Leben.",
        "Überall sehen wir uns entgegenieuchten auf dem Gebiete des kommerziellen Lebens das, was die in die Lebenspraxis hineingeflossene Erkenntnis und die Errungenschaften der Natur­wissenschaft uns gebracht haben.",
        "Will man sich eine Vorstellung machen, wie die hier gemeinte Geisteswissenschaft zu diesen Fort-schritten steht, so kann man folgenden Vergleich machen.",
        "Man kann hinblicken auf den Bauern, der sein Feld bestellt, der einerntet die Früchte des Feldes: der größte Teil dieser Früchte des Feldes, der eingeerntet wird, wird hereingenommen in das menschliche Leben, zur Nahrung der Menschen verwendet, ein kleiner Teil bleibt übrig, er wird verwendet zur neuen Fruchtaussaat.",
        "Nur von diesem letzteren Teile kann man sagen, daß er folgen darf den Triebkräften, den inneren Lebens- und Bildung skräften, die im aufsprossenden Korn und in der Frucht selber liegen.",
        "Dasjenige, was in die Scheune geführt wird, wird zumeist abgebracht von seinem in den eigenen Bildungsgesetzen liegenden Fortschritt, wird gleichsam in eine Seitenströmung geführt, zur Menschennahrung verwendet, setzt nicht fort in untnittelbarer"
      ],
      [
        "Weise dasjenige, was in dem Keirne liegt, was die eigentlichen Triebkräfte sind.",
        "So erscheint der Geisteswissenschaft, die hier gemeint ist, ungefähr dasjenige, was die Naturwissenschaft in den letzten Jahrhunderten an Erkenntnissen gebracht hat.",
        "Der weitaus größte Teil ist dazu verwendet worden, Einsicht zu gewähren in die äußeren sinnlichen Tatsachen, ist dazu verwendet worden, in den menschlichen Nutzen einzugehen.",
        "Aber zurückbleiben kann gerade von den Ge­danken der letzten Jahrhunderte in der menschlichen Seele etwas, was nicht verwendet wird, um das oder jenes zu begreifen in der sinnlichen Außenwelt, nicht verwendet wird, um Maschinen zu bauen oder Industrie zu pflegen, sondern das lebendig gemacht wird, das erhalten wird in seiner Richtung wie das Korn, das zur Aussaat benützt wird und seinen Bildungsgesetzen folgen darf Wenn der Mensch dies leben läßt in seiner Seele, wenn er ein Gefühl dafür hat, zu fragen: Wie läßt sich das seelische Leben durchleuchten und erkennen an den Begriffen und Ideen, welche die Naturwissenschaft geliefert hat, wie läßt sich tnit diesen Ideen leben, wie läßt es sich von diesen Ideen aus begreifen, wo die Haupttriebkräfte des Seeleniebens liegen? - Wenn die Seele ein Gefühl dafür hat, diese Frage aufzuwerfen tnit der ganzen Fülle des seelischen Lebens, dann erscheint erst dasjenige, was in unserer Zeit in die menschliche Kultur übergeht."
      ],
      [
        "Und auch in ganz anderer Beziehung ist diese Geisteswissenschaft vielfach ein Kind der naturwissenschaftlichen Denkungsweise zu nennen.",
        "Nur muß der Geist in einer anderen Art erforscht werden als die Natur.",
        "Gerade wenn man auf ebenso sicherer methodischer Basis dem Geiste gegenüberstehen will, wie die Naturwissenschaft der Natur gegenübersteht, muß man das naturwissenschaftliche Denken um­formen, so prägen, daß es ein taugliches Werkzeug für die Erkenntnis des Geistes werden kann.",
        "Wie das werden kann, davon soll einiges tnitgeteilt werden."
      ],
      [
        "Gerade wenn man so recht fest steht auf dem Boden der Natur­wissenschaft, da sieht man ein, daß mit den Mitteln, mit denen die Naturwissenschaft arbeitet, eine geistige Erkenntniswissenschaft sich nicht gewinnen läßt.",
        "Immer mehr und mehr ist von erleuchteten Geistern gesprochen worden, daß vom sicheren Boden der Naturwissenschaft"
      ],
      [
        "ausgehend der Mensch einsehen muß, daß seine Er­kenntnis begrenzt sei.",
        "Naturwissenschaft und KanJ haben dazu beigetragen, den Glauben heraufzubringen, daß die Erkenntniskräfte des menschlichen Geistes begrenzte seien, daß der Mensch nicht eindrin­gen könne mit seinem Wissen in den Quell, mit dem sich die Seele verbinden muß."
      ],
      [
        "In dieser Richtung gibt Geisteswissenschaft der Naturwissenschaft völlig recht.",
        "Gerade für diejenigen Geisteskräfte und für jene Erkenntnisfähigkeit, welche die Naturwissenschaft groß gemacht haben und auf denen die Naturwissenschaft auch stehen, bleiben muß, für sie gibt es keine Möglichkeit einzudringen in das geistige Gebiet."
      ],
      [
        "Aber in der menschlichen Seele schlummern andere Erkenntnisfähigkeiten, Erkenntnisfähigkeiten, welche im Alltag und im Getriebe der gewöhnlichen Wissenschaft nicht verwendet werden können, die hervorgeholt werden können aus der menschlichen Seele, und wenn sie hervorgeholt werden aus den unergründlichen Tiefen der menschlichen Seele, dann machen sie aus dem Menschen etwas anderes, dann durchleben und durchkraften sie ihn mit einer neuen Erkenntnisart, mit einer solchen Erkenntnisart, welche eindringen kann in Gebiete, welche der bloßen Naturwissenschaft verschlossen sind.",
        "Es ist - ich lege einen Wert auf den Ausdruck -, es ist eine Art geistiger Chemie, durch welche man in die geistigen Gebiete des Daseins eindringen kann, aber eine Chemie, welche nur in bezug auf sichere Logik und in bezug auf methodisches Denken Ähnlichkeit hat mit der äußeren naturwissenschaftlichen Chemie."
      ],
      [
        "Es ist die Chemie der Seele selber."
      ],
      [
        "Um uns zu verständigen, sei von diesem Gesichtspunkte aus ver­gleichsweise das folgende gesagt: Wenn wir Wasser vor uns haben -es hat gewisse Eigenschaften, der Chemiker kommt und zeigt, daß Wasserstoff und Sauerstoff darinnen sind.",
        "Der erstere brennt, ist gasförmig, ist etwas ganz anderes als das Wasser.",
        "Würde jemand, der von Chemie nichts weiß, dem Wasser ansehen können, daß in ihm Wasserstoff ist?",
        "Das Wasser brennt nicht, es löscht das Feuer sogar!",
        "Dennoch kommt der Chemiker, trennt ab vom Wasser den Wasser­stoff.",
        "Mit dem Wasser läßt sich vergleichen der Mensch, wie er im Alltag vor uns steht, wie er ferner vor der gewöhnlichen Wissenschaft"
      ],
      [
        "steht: in ihm ist vereinigt Physisch-Leibliches und Geistig-Seelisches.",
        "Die äußere Wissenschaft und diejenige Weltanschauung, die sich auf dieser Wissenschaft aufbaut, hat völlig recht, wenn sie sagt: Diesem Menschen, der uns gegenübersteht, kann man nicht ansehen, daß in ihm Seelisch-Geistiges ist. - Und begreiflich ist es, daß diese Weltan­schauung es ableugnet."
      ],
      [
        "Aber diese Ableugnung ist geradeso, als wollte man die Natur des Wasserstoffes ableugnen, weil man das Wasser vor sich sieht.",
        "Allerdings, die Notwendigkeit eines Beweises liegt vor, daß das Seelische abgetrennt dargestellt werden kann."
      ],
      [
        "Daß es eine solche geistige Chemie gibt, das ist dasjenige, was Geistes­wissenschaft der Menschheit zu sagen hat, wie der Kopernikanismus der überraschten Menschheit zu sagen hatte, daß die Erde nicht stille steht, sondern in rasendem Tempo um die Sonne sich dreht.",
        "Und wie noch bis in das 19."
      ],
      [
        "Jahrhundert hinein Kopernikus' Schriften auf dem Index eines Religionsbekenntnisses standen, werden in gewisser Be­ziehung lange die Erkenntnisse der Geisteswissenschaft auf dem Index anderer Weltanschauungen stehen, die sich nicht losmachen können von dem, was jahrhundertealte Vorurteile und Autoritäten sind.",
        "Und daß diese Geisteswissenschaft dennoch bis zu einem gewissen Grade Herz und Seele ergreifen kann, daß sie gerade nicht außerhalb des Suchens unserer Zeit liegt, dafür haben wir ja einen kleinen Beweis, dessen ich mich nicht rühmen will, der aber erwähnt werden darf als ein Zeugnis für das in den Seelen verborgene Zeitgemäße der Geistes­wissenschaft."
      ],
      [
        "Sind wir doch in der Lage, bereits in unserer Zeit dieser Geisteswissenschaft eine freie Hochschule auf freiem schweizerischen Boden in der Nähe von Basel zu bauen und können wir erblicken durch das Verständnis der Freunde dieser Geistesströmung das Wahr­zeichen in dem im Baustile neuen Doppelkuppel-Rundbau, welcher von den Höhen Dornachs heruntergrüßt.",
        "Daß dieser Bau schon im Auf­richten ist, daß die Formen dieser Kuppeln schon über den Rundbau sich erheben, das läßt uns heute mit Hoffnung und Befriedigung von Geisteswissenschaft sprechen, trotz all der Gegnerschaft und trotz all des Unverständrisses, das ihr heute noch begegnen muß in weiten Kreisen."
      ],
      [
        "Das, was ich als geistige Chemie bezeichnet habe, ist etwas, was nicht erarbeitet werden kann durch äußere Methoden, dasjenige, was"
      ],
      [
        "geistige Chemie genannt werden kann, vollzieht sich lediglich in der menschlichen Seele selber, und Verrichtungen sind es intirn seelisch-geistiger Art, welche die Seele nicht so lassen, wie sie im alltäglichen Leben und in der Wissenschaft ist, sondern die wirken auf die Seele so, daß sie sich umarbeitet, daß sie ein ganz anderes Werkzeug wird, als sie im Alltagsleben ist.",
        "Und nicht sind es irgendwelche wunder­bare Verrichtungen aus irgendeinem Aberglauben, die also in geisti­ger Chemie angewendet werden, sondern es sind durchaus innere geistig seelische Verrichtungen, welche sich aufbauen aus dem, was auch im Alltagsleben vorhanden ist, Kräfte der Seele, die immer da sind, die wir im Alltagsleben brauchen, die aber in diesem Ailtags­leben, ich möchte sagen, nebenher verwendet werden, aber die un­ermeßlich gesteigert werden müssen, ins Unbegrenzte sich erkraften müssen, wenn der Mensch wirklich zum geistigen Erkennen kommen soll."
      ],
      [
        "Die eine Kraft, welche sich so nebenher im alltäglichen Leben betätigt, aber unermeßlich gesteigert werden muß, das ist die Auf­merksamkeit."
      ],
      [
        "Was ist Aufmerksamkeit?",
        "Nun, wir lassen das Leben, das an der Seele vorüberflutet, nicht so, wie es sonst sich gestaltet, vorüberfluten.",
        "Wir raffen uns im Inneren auf, um den geistigen Blick auf dies oder jenes hinzurichten.",
        "Einzelne Dinge greifen wir heraus aus dem seeli­schen Leben, stellen sie in das Blickfeld des Bewußtseins, konzen­trieren die Kräfte der Seele auf dieses Einzige.",
        "Wir enifachen ein Interesse, das heraushebt einzelne Tatsachen und Wesenheiten aus dem vorüberflutenden Strome des Daseins.",
        "Diese Aufmerksamkeit ist im täglichen Leben durchaus notwendig.",
        "Man wird immer mehr ein­sehen, wenn Geisteswissenschaft ein wenig in die Seelen eindringt, daß das, was für die Menschen die Gedächtnisfrage ist, im Grunde genommen nur eine Aufmerksamkeitsfrage ist, und daß dies wichtige Gesichtspunkte für die Erziehungsfrage geben wird.",
        "Je mehr man sich bemüht beim aufwachsenden Menschen und auch später, die Seele immer mehr in die Tätigkeit der Aufmerksamkeit zu versetzen, desto mehr wird das Gedächtnis gestärkt, desto mehr wächst unser Gedächtnis heran, desto intensiver gestaltet es sich.",
        "Und ein anderes"
      ],
      [
        "noch!",
        "Wer hätte heute nicht gehört von der traurigen Seelenerschei­nung, die man die Diskontinuität des Bewußtseins nennt?",
        "Es gibt Menschen, die Lebenslagen haben, in denen sie sich selbst vergessen, die nicht wissen: Du warst mit deinem Ich bei diesem oder jenem Erlebnisse - nicht wissen, was sie durchgemacht haben.",
        "Sie können ihr Heim verlassen ohne Sinn und Verstand, erst nach Tagen oder nach Jahren sich wiederfinden und anknüpfen an das, was sie vor vielen Tagen, Wochen, Monaten, Jahren erlebt haben.",
        "Niemals würden solche Erscheinungen zu jener Tragik führen können, wenn man wüßte, daß auch diese Integrität, dieses Gesundhalten des Menschen abhängt von einer regelrechten Entwickelung der Aufmerksamkeits­betätigung.",
        "So ist Aufmerksamkeitsbetätigung etwas, was wir im gewöhnlichen Leben durchaus bräuchen, sie ist aber auch etwas, was der Geistesforscher entwickeln muß zu einer besonderen inneren Seelenerkraftung.",
        "Er muß sie vertiefen zu dem, was man nennen könnte Meditation, Konzentration."
      ],
      [
        "Das sind technische Ausdrücke.",
        "So wie wir im gewöhnlichen Leben veranlaßt sind, diesem oder jenem Gegenstande die Aufmerksamkeit zuzuwenden, so verwendet der Geistesforscher aus seiner inneren Willkür alle Seelenkräfte auf ein Bild, eine Gemütsstimmung, auf Willensimpulse, die er überschauen kann, die ganz klar vor seiner Seele sind.",
        "Aber so konzentriert er auf sie alle seine Kräfte, daß er wie im tiefen Schlafe alles Denken und Trachten, alle Sorgen, alle Affekte des Lebens so zum Stillstande gebracht hat, wie sie im Still-stande sind im tiefen Schlafe, nur daß er sein Bewußtsein nicht ver­liert, daß er es völlig wach erhält.",
        "Aber alle Kräfte der Seele, welche sonst zerstreut sind ins Äußere, sind konzentriert auf eine durch Willkür in den Mittelpunkt des menschlichen Seelenerlebens gestellte Vorstellung, Empfindung oder einen Impuls.",
        "Dadurch drängen sich die Seelenkräfte zusammen, und dasjenige, was sonst nur schlummert zwischen den Zeilen des Lebens, das kraftet sich heraus, prägt sich heraus aus der menschlichen Seele.",
        "Das tritt tatsächlich ein, daß durch diese innere Erkraftung der menschlichen Seele, innere Konzentra­tionstätigkeit, innere unermeßlich gesteigerte Aufmerksamkeit die See]e sich so in sich erfühlen, erleben lernt, daß sie fähig wird, sich"
      ],
      [
        "bewußt herauszureißen aus dem physisch-sinnlichen Leibe, wie der Wasserstoff durch die chemische Methode herausgesondert wird aus dem Wasser.",
        "Allerdings, es ist eine innere seelische Erarbeitung, die durch Jahre geht, wenn der Geistesforscher durch seine Konzentra­tionsbetätigung sich dazu befähigen will, sich herauszureißen aus dem physischen Leibe.",
        "Dann aber kommt die Zeit, wo der Geistesforscher einen Sinn zu verbinden weiß mit dem Worte: Ich erlebe mich als geistig-seelisches Wesen außerhalb meines Leibes, und ich weiß, daß dieser Leib außerhalb meiner Seele sich befindet.",
        "Ich weiß, wenn die Seele sich erkraftet, kann sie sich erleben, auch wenn sie den Leib vor sich hat mit allen seinen Schicksalen! - Der Mensch wird sich in dem, was er selbst ist, vollständig äußerliche Persönlichkeit, erlebt sich als geistig-seelisches Wesen in Absonderung von seinem Leibe.",
        "Dieses geistig-seelische Wesen zeigt dann ganz andere Eigenschaften als sonst, wenn es sich mit dem physischen Leibe bedeckt."
      ],
      [
        "Zunächst läßt sich die Denkkraft erleben.",
        "Und da ich nicht von Abstraktionen sprechen will, so stoßen Sie sich nicht daran, daß ich ungescheut und vorurteilsfrei dasjenige schildern möchte, was heute noch so paradox klingt.",
        "Wenn der Geistesforscher anfängt einen Sinn zu verbinden mit dem Worte: Du erlebst jetzt in deiner Seele auch außerhalb deiner Sinne und des Gehirns -, dann erfühlt er sich in seinem Denken nicht in seinem Kopfe, sondern wie seinen Kopf um-wandelnd und umwebend, ja, er weiß - da man, solange man im Leben zwischen Geburt und Tod steht, immer wiederum in den Leib zurückkehren muß - genau den Moment zu beobachten, wo er wie­derum zurückkehrt mit seinem Denken in sein Nervensystem und Gehirn, wie dieses Gehirn ihm einen Widerstand bietet, wie er unter-tauchen muß, ja er fühlt es, wie er untertaucht und - gestat ten Sie den Ausdruck - einschnappt in sein physisches Gehirn, das jetzt wieder folgt dem, was das Geistig-Seelische vollbringt.",
        "Dieses Sich-Erleben außerhalb des Leibes und Wieder-Untertauchen gehört zu den erschütterndsten Erlebnissen des Geistesforschers.",
        "Aber dieses rein in sich selber sich erlebende Denken, das außer-halb des Gehirns verläuft, stellt sich anders dar als das physische Denken."
      ],
      [
        "Die physischen Gedanken sind schattenhaft gegen die, welche wie eine neue Welt dastehen vor dem Geistesforscher; es durchdringen sich die Gedanken mit innerer Bildhaftigkeit.",
        "Deshalb nennen wir das Imagination, aber nicht aus dem Grunde, weil wir glauben, daß sie etwas Phantastisches, Erdachtes enthält, sondern dasjenige, was wahrgenommen wird, das wird erlebt, imaginiert, aber dieses Imagi-nieren ist ein Untertauchen in die Dinge selbst, man lebt die Dinge, und es stellen sich so die Dinge und Vorgänge der geistigen Welt vor die Seele hin.",
        "So kann das Denken abgesondert werden vom physisch-leiblichen Leben, und der Geistesforscher kann sich wissen in der Welt geistiger Vorgänge und Kräfte.",
        "Auch andere Kräfte können abgelöst werden aus dem rein Leiblich-Physischen.",
        "Dann erlebt der Geistesforscher zunächst sich selber in seiner rein geistig-seelischen Wesenheit."
      ],
      [
        "Aber es ist dasjenige, was er in der geistigen Welt erlebt, eine ganz andere Art des Wahrnehmens als das Wahrnehmen der äußeren sinn­lichen Welt.",
        "Da sind die Dinge, ich selbst bin draußen: so ist es nicht vom Augenblicke an, wo man im geistig-seelischen Erleben eine geistige Welt um sich hat, die wirklich mit derselben Notwendigkeit aufsteigt wie um einen Blindgeborenen Farbe und Licht im Augen­blicke, wo er operiert worden ist.",
        "Dieses Erleben ist ein solches, daß man mit seinem ganzen Wesen untertaucht in diese Dinge.",
        "Dann weiß man: Du nimmst sie wahr, indem du gleichsam ausgeflossen bist in sie. - Man weiß, daß man diese Dinge in der Imagination nachbildet.",
        "Man fühlt, daß die Wahrnehmung zugleich Nachbildung ist: man fühlt sich in einer fortwährenden Tätigkeit, nicht in einem passiven Wahrnehmen wie in der äußeren Welt.",
        "Deshalb könnte man das Auf­]eben der imaginativen Gedankenwelt eine geistige Mimik, ein geisti­ges Mienenspiel nennen.",
        "Dieses Geistig-Seelische ist in fortwährender Tätigkeit.",
        "Man reißt sich aus dem Leiblichen heraus, das Seelische ist in fortwährender Tätigkeit.",
        "Man fühlt sich etwa so damit verbun­den, wie ein Mensch in der physischen Welt das Seelenieben eines anderen erleben könnte.",
        "So erlebt man das, was die Wesen und Vor­gänge der geistigen Welt enthalten: man wird selbst der Ausdruck davon.",
        "In der geistigen Miene, die man annimmt, drückt man selbst"
      ],
      [
        "das Wesen der Dinge aus.",
        "Eine Tätigkeit, ein aktives Wahrnehmen ist es, zu dem man getrieben wird.",
        "Und man kann sagen: Geistes­forschung stellt ganz andere Anforderungen an die menschliche Seele als die äußere Wissenschaft, die mehr passiv hinnimmt."
      ],
      [
        "So wie nun das Denken, die Denkkraft als Geistig-Seelisches heraus-gesondert werden kann aus dem Leiblich-Physischen, so kann auch eine andere Kraft, die der Mensch sonst nur im Leibe verwendet, aus diesem Leibe herausgesondert werden.",
        "So sonderbar das klingt, diese andere Kraft ist die Sprachkraft, die Kraft, die wir im gewöhnlichen Leben im Sprechen anwenden."
      ],
      [
        "Wie ist es denn, wenn wir sprechen?",
        "Unser Gedankenleben läßt mitvibrieren unser Gehirn.",
        "Dieses hat seine Verbindung mit dem Sprachapparat, Muskeln werden in Bewegung gesetzt, was wir denken, fließt aus im Wort und lebt im Wort."
      ],
      [
        "Können wir nicht sagen: Indem wir sprechen, ergießen wir, was in unserer Seele ist, in leiblich physi­sche Organe hinaus? - Dadurch, daß der Mensch die Aufmerksamkeit so steigert und noch etwas hinzufügt, was auch ins Unbegrenzte ge­steigert werden muß, entsteht die Loslösung der Sprachkraft vom physisch sinnlichen Leibe.",
        "Diese Kraft ist die Hingabe."
      ],
      [
        "Wir kennen sie, diese Kraft, in den Momenten, wenn wir religiös fühlen, wenn wir in Liebe diesem oder jenem Wesen hingegeben sind, wenn wir in treuer Forschung den Dingen folgen, wenn wir unser vergessen; wir kennen sie, diese Hingabe, sie verfließt nur sozusagen zwischen den Zeilen des gewöhnlichen Lebens und der gewöhnlichen Forschung.",
        "Der Geistesforscher muß diese Kraft unbegrenzt erkraften, er muß den Strömen des Daseins so hingegeben sein, wie er selbst nur hin­gegeben ist diesen Strömen des Daseins im Schlafe, im tiefen Schlafe, wenn alle Regsamkeit seiner Glieder ruht, wenn alle seine Sinne schweigen und der Mensch ganz hingegeben ist und nichts tut."
      ],
      [
        "Dann ist er im Schlafe in Bewußtlosigkeit verfallen.",
        "Wenn sich aber der Mensch durch innere Willkür dazu aufraffen kann, daß er alle seine Tätigkeit unterdrückt, alle Regsamkeit der Glieder unterdrückt, daß er aber wach bleibt und das Gefühl, die Empfindung entwickelt, ein­gegossen dem Strome des Daseins zu sein, nichts zu wollen, als was die Welt für einen will, wenn er dieses Gefühl immer wieder hervorruft"
      ],
      [
        "abgesondert von der Steigerung der Aufmerksamkeit, dann er­kraftet sich die Seele immer mehr und mehr durch diese unbegrenzte Hingabe."
      ],
      [
        "Nur müssen diese beiden Übungen abgetrennt gemacht werden, denn sie widersprechen ja einander.",
        "Die Aufmerksamkeit fordert Anspannung und Hinlenken zu einem Objekte, die andere Übung tiefe Hingabe, passive Hingabe, wie im religiösen Empfinden etwa oder wie in der Hingabe an ein geliebtes Wesen.",
        "Die Früchte, die der Mensch aus der unermeßlichen Steigerung der unbegrenzten Hin-gabe schöpft, sind eben, daß sein geistiges Wesen sich heraussondert aus der physisch4eiblichen Betätigung.",
        "Und so kann diejenige Kraft, die sonst in das Wort sich ausgießt, abgetrennt werden von der äußeren Sprachbetätigung, kann im Seelisch-Geistigen bleiben.",
        "Dann wird wieder wie durch eine geistige Chemie die Sprachkraft aus ihrer physisch-sinnlichen Verbindung herausgerissen und der Mensch erlebt dasjenige, was man das geistige Gehör, das geistige Hören nennen kann."
      ],
      [
        "Wiederum ist es so, daß der Mensch sich erlebt außerhalb seines Leibes, daß er sich aber erlebt, indem er untertaucht in die Dinge, das innere Wesen dieser Dinge wahrnimmt und es in sich nachlebt wie mit einer inneren Gebärde, mit einer inneren Geste.",
        "Wie wenn wir versucht sind, durch ein besonderes Nachahmungstalent, durch be­sondere Gesten dasjenige auszudrücken, was uns beschäftigt.",
        "Das macht die Seele, wenn sie sich herausgerissen hat: sie spielt aktiv nach, es ist ein aktives Betätigen.",
        "Weil man den Dingen folgt, weil man nachbildet das innere Weben und Wesen der Dinge, nimmt man diese Dinge wahr.",
        "In der äußeren sinnlichen Welt sind wir passiv beim Hören, als Geistesforscher tauchen wir unter in das Wesen der Dinge, wir hören ihr inneres Weben.",
        "Dasjenige, was Pythagoras die Sphärenmusik genannt hat, ist keine bloße Phantasie: er hört, indem er ausspricht.",
        "Ein sprechendes Hören, ein hörendes Sprechen ist es im Untertauchen in das Wesen der Dinge.",
        "Die wahre echte Inspiration ist es, die sich also ergibt."
      ],
      [
        "Eine dritte Art inneren Erlebens kann über den Geistesforscher kommen, wenn er die gesteigerte Aufmerksamkeit und Hingabe"
      ],
      [
        "weiterentwickelt.",
        "Betrachten wir das Kind, das heranwächst.",
        "Es ist eine Eigentümlichkeit des heranwachsenden Menschen, daß er sich seine Richtung im Raume, daß er sich die Art und Weise, in den Raum hineingestellt zu sein, selber geben muß im Laufe des Lebens."
      ],
      [
        "Der Mensch wird geboren, indem er nicht gehen, nicht stehen kann, indem er sich, wie man hier in Österreich zu sagen pflegt, aller Viere bedienen muß, um vorwärtszukommen.",
        "Dann entwickelt er die Kräfte, die ihn aufrichten, Aufrichtekräfte."
      ],
      [
        "Dadurch tritt dann hervor, was soviele große Geister gefühlt haben, indem sie sagen konnten, daß, wenn der Mensch sich aufrichtet von der horizontalen Richtung zur aufrechten Richtung, sein Blick nicht mehr haftet am Irdischen, sondern er nach oben blickt.",
        "Das Wesentliche ist, daß der Mensch durch ein inneres Erleben sich herausentwickelt aus einem hilflosen, horizontalen Leben in das aufrechte vertikale Leben hinein."
      ],
      [
        "Die Naturwissenschafter werden schon sehen, daß das etwas ganz anderes ist als alle die Vererbungskräfte, die dem Tiere seine Richtungskräfte geben.",
        "Ganz andere Kräfte wirken im Tiere, die das Tier in diese oder jene Richtung zum Vertikalen bringen, als im Menschen."
      ],
      [
        "Im Menschen wirkt eine Summe von Kräften und reißt ihn heraus aus seiner hilflosen Lage.",
        "Diejenigen Raumrichtungskräfte, durch die er eigentlich im wahren Sinne des Wortes Erdenmensch ist, durch die er das erst wird, was er als Mensch auf Erden ist, diese Kräfte wirken sehr im Verborgenen."
      ],
      [
        "Man kommt ihnen nur bei, wenn man sich ein wenig in die Geisteswissenschaft vertieft hat; es ist ein großes System, eine große Summe von Kräften.",
        "Nicht alle werden verbraucht im Kindheitsalter, es schlummern noch Kräfte dieser Art im Menschen drinnen, aber sie bleiben unbenützt im äußeren Leben und im wissen­schaftlichen Leben."
      ],
      [
        "Indem der Mensch die Seelenübungen verrichtet, wird er durch die gesteigerte Aufmerksamkeit und Hingabe gewahr, wie in ihm die Kräfte sitzen, die er gehabt hat als Kind: er wird geistiger Richtkräfte sich bewußt.",
        "Und die Folge davon ist, daß er zum inneren Mienenspiel, zur inneren Geste auch innere Physiognomie seinem Geistig-Seelischen hinzuzufügen vermag."
      ],
      [
        "Wenn der Mensch anfängt, einen Sinn verbinden zu können mit dem Worte: Dein Leib ist außer dir - dann kommt nach und nach die Zeit heran, wo er sich"
      ],
      [
        "der Kräfte bewußt wird, die ihn als physisch-sinnliches Wesen vertikal auf die Erde gestellt haben.",
        "Dadurch kommt er in die Lage, diesen Kräften andere Richtungen zu geben, aus sich selber eine andere Gestalt zu machen, als er gemacht hat im Leben seiner Kindheit: er gibt sich nicht nur eine wirkliche Gestalt, er weiß innere Bewegung zu entwickeln, er weiß seinem Geistig-Seelischen eine andere Physio­gnomie zu geben, als er sich als Erdenwesen gegeben hat.",
        "Dadurch kommt er dazu, hinunterzutauchen in andere geistige Vorgänge und Wesen, daß er die Kräfte, die ihn vom kriechenden Kinde zum auf­rechten Menschen wandeln, wandelt, daß er innen ähnlich wird den geistigen Dingen und Wesen und dadurch wahrnimmt.",
        "Das ist die wahre, reale Intuition.",
        "Das wirkliche Wahrnehmen geistiger Dinge und Vorgänge ist ein Untertauchen, ein Einswerden mit den geistigen Dingen.",
        "Während man das, was in den Wesen vorgeht, erlebt durch die innere Imagination, so daß man ihre Gesten nachzubilden vermag, vermag man sich selber in die Dinge und Vorgänge zu verwandeln, vermag man die innere geistige Gestalt der Dinge anzunehmen.",
        "Man nimmt sie durch geistige Aktivität wahr."
      ],
      [
        "Ich habe Ihnen nicht durch philosophische Ausdrücke schildern wollen, wie sich der Geistesforscher hineinlebt in geistige Vorgänge und Wesenheiten, ich habe möglichst konkret schildern wollen, wie sich die Seele losreißt und untertaucht in die geistige Welt, indem sie aktiv wahrnehmend wird.",
        "Es ist klar ersichtlich geworden, daß jeder Schritt in voller Aktivität unternommen werden muß, daß jeder Schritt so sein muß, daß wir nur dadurch das Wesen kennen von den Dingen und Vorgängen der geistigen Welt, wenn wir nachbilden, aktiv nachschaffen können.",
        "Das ist der große Unterschied der geistigen Erkenntnis von der äußeren Erkenntnis, daß letztere sich passiv hingibt den Dingen und daß geistige Erkenntnis in fortwährender Aktivität leben muß, daß der Mensch zu dem werden muß, was er wahrnimmt."
      ],
      [
        "Nun, es wird einem heute schon verziehen, wenn man im Allge­meinen von einer geistigen Welt spricht.",
        "Das lassen sich die Leute noch gefallen.",
        "Das aber wirkt heute noch paradox, daß jemand sagen kann: Der Mensch kann sich loslösen von allem Denken, Fühlen und"
      ],
      [
        "Wahrnehmen, das an das Irdische gebunden ist, und sich dann, indem vor ihm alle Welt der Sinne verschwindet, umgeben fühlen von einer neuen, ganz konkreten neuen Welt, in welcher Vorgänge und Wesen rein geistiger Art sind, wie hier in der physischen Welt Vorgänge und Wesenheiten sind.",
        "Nicht ein allgemein verschwommener Pantheismus, nicht eine allgemeine Sauce ist es."
      ],
      [
        "Wenn man vom allgemeinen Pantheismus spricht, ist es der Geisteswissenschaft gegenüber, wie wenn man jemand auf eine Wiese führt und sagt, das alles, alle Blüm­chen, alle Käferchen, ist Natur, alles ist Pan-Natur.",
        "Die Leute werden wenig zufrieden sein, denn sie wissen: man kommt nur dann zurecht, wenn man die einzelnen Blumen, Käfer und chemischen Vorgänge verfolgen kann."
      ],
      [
        "Ebenso spricht die Geisteswissenschaft von Wahr­nehmungen konkreter geistiger Vorgänge und Wesenheiten.",
        "Sie darf sich nicht scheuen, die Zeit herauszufordern, indem sie sich sagt: Wie wir in der Außenwelt die Menschen sehen, unter ihnen die Hierarchie der Tiere, die Hierarchie der Pflanzen, der Mineralien, so schwindet das um uns herum aus dem geistigen Honrizonte, indem wir uns hinein-leben in die geistige Welt, aber es tauchen geistige Reiche auf, geistige Hierarchien, Wesen, die zunächst dem Menschen gleich sind, Wesen, die über dem Menschen stehen, Wesen und Geschöpfe, die höhere Reiche des Daseins füllen, einzelne individuelle geistige Wesen und Geschöpfe. - Wie die Menschenseele sich selbst hineinstellt und zu leben hat in der geistigen Welt, wenn sie den Leib im Tode ablegt und durch die Pforte des Todes gegangen ist, wie sie hindurchgeht durch die geistigen Reiche, davon soll übermorgen die Rede sein."
      ],
      [
        "Was Geisteswissenschaft als ihre Methode ausbildet: man merkt es sofort, es unterscheidet sich sehr wesentlich von dem, was unsere Zeitgenossen zugeben können, was sich herausgebildet hat aus den Denkgewohnheiten der Jahrhunderte und was so festsitzt wie die früheren Vorurteile gegenüber dem Kopernikanischen Weltsysteme.",
        "Aber wie muß Geisteswissenschaft sich gegenüber dem Suchen der Zeit verhalten, wenn sie sich recht verstehen will, wenn sie sich recht verhalten will gegenüber diesem Suchen der Zeit?"
      ],
      [
        "Der erste Einwand, der uns aus unserer Zeit so leicht gemacht wer­den kann, ist der, daß man sagt: Ja, der Geistesforscher spricht davon,"
      ],
      [
        "daß die Seele erst besondere Kräfte entwickeln soll, dann kann sie hineinschauen in die geistige Welt.",
        "Wer diese Kräfte noch nicht ent­wickelt hat, wer es noch nicht dazu gebracht hat, zum Abtrennen des Denkens, der Sprachkraft, der Aufrichtekraft, den ginge also die geistige Welt gar nichts an! - Solcher Einwand ist geradeso wie der, der da sagen würde: Denjenigen, der nicht malen kann, den gehen die Bilder nichts an. - Malen kann nur der, der malen gelernt hat, aber es wäre traurig, wenn nur der die Bilder verstehen könnte, der malen kann.",
        "Die Seele versteht die Bilder, auch wenn der Mensch nicht selber malen kann, sie hat eine Sprache in sich, welche sich mit der menschlichen Kunst verbindet.",
        "Auffinden die Tatsachen und Vor-gänge der geistigen Welt und sie schildern, das kann nur derjenige, der selbst zum Geistesforscher geworden ist.",
        "Wenn aber der Geistes-forscher sich bemüht, dasjenige, was er erforscht, in Worte der ge­wöhnlichen Gedanken und Ideen zu kleiden, dann ist das, was er so gibt, begreiffich jeder Seele, auch derjenigen, die kein Forscher ge­worden ist, wenn sie nur hinwegzunehmen vermag, was aus der zeit­genössischen Bildung kommt, die sich gibt, als ob sie auf dem festen Boden der Naturwissenschaft stünde, aber in Wahrheit dies nur glaubt.",
        "Wenn sich die Seele nur aller Vorurteile begibt, wenn sie sich nur unbefangen wie dem Betrachten eines Bildes hingibt, dann ist jeder imstande, das Ergebnis der Geistesforschung zu verstehen."
      ],
      [
        "Die Menschenseele ist zur Empfindung der Wahrheit veranlagt, und tief ist in den Menschenseelen, wenn sie sich nur selber verstehen wollen, eine geheime, intime Sprache, eine Sprache, durch die jeder, auf welcher Bildungs- und Entwickelungsstufe er stehe, den Geistes-forscher verstehen kann, wenn er ihn nur verstehen will.",
        "Das ist es aber gerade, was der Geistesforscher in dem Suchen unserer Zeit findet.",
        "In verflossenen Jahrhunderten hat der Mensch allein nur durch Glaubensvorstellungen etwas wissen wollen über die geistige Welt, in späterer Zeit haben die Menschen geglaubt, daß ein sicheres Wissen sich nur auf die äußeren Tatsachen aufbaue.",
        "In unserer Zeit wissen es die Seelen zwar noch nicht, im Oberbewußtsein sitzt es noch nicht, aber für den Geistesforscher ist es klar: wir leben in einer Zeit, in der sich in den Tiefen der Menschenseele, von denen die Seele nichts"
      ],
      [
        "weiß, vorbereitet Sehnsucht nach der Geisteswissenschaft, Hofinung auf diese Geisteswissenschaft.",
        "Immer mehr und mehr wird man er-kennen, daß alte Vorurteile schwinden müssen.",
        "Namentlich in bezug auf das Denken wird man da so manches erkennen."
      ],
      [
        "So wird es heute noch viele Menschen geben, gerade diejenigen, welche glauben, auf dem festen philosophischen Boden zu stehen, welche sagen: Haben es nicht Kant und die Philosophie bewiesen, daß der Mensch nicht hinuntertauchen kann mit seinem Wissen?",
        "Kommt nun da eine solche Geisteswissenschaft, will Kant bekämpfen und will zeigen, daß das nicht richtig ist, was die moderne Philosophie zeigen will! - Ja, Geisteswissenschaft will gar nicht zeigen, daß das unrichtig ist, was Kant von seinem und die moderne Wissenschaft von ihrem Stand­punkte aus sagt, aber die Zeit wird lehren, daß es noch andere Ge­sichtspunkte gegenüber richtig und unrichtig gibt als diejenigen, an die man sich gewöhnt hat."
      ],
      [
        "Nehmen wir an, wie sich zum Beispiel die wirkliche Lebenspraxis verhält.",
        "Da könnte jemand kommen und klar beweisen, daß der Mensch mit seinen Augen unfähig ist, jemals Zellen zu sehen, die als kleinste Organismen den großen Organismus aufbauen."
      ],
      [
        "Dieser Beweis könnte ganz richtig sein, so richtig sein, als der Kant'sche oder philosophische Beweis richtig ist.",
        "Nehmen wir an, wir lebten in einer Zeit, in der das Mikroskop noch nicht erflinden sei, und jemand käme und würde scharfsinnig beweisen, der Mensch könne mit seinen Augen die kleinsten Teile nicht sehen."
      ],
      [
        "Der Beweis könnte klappen und nichts könnte einzuwenden sein.",
        "Aber darauf kam es nicht an im wirklichen Fortgang der Forschung, vielmehr darauf kam es an, trotz alledem zu zeigen, daß physische Werkzeuge unmittelbar gefunden werden können, um dasjenige zu erreichen, was ganz zu beweisen nicht möglich sein würde, wenn die Fähigkeiten unbewaffnet blieben."
      ],
      [
        "Recht haben diejenigen, die da sagen, die mensch­lichen Fähigkeiten sind begrenzt.",
        "Die Geisteswissenschaft widerspricht dem ja nicht, sie zeigt nur, daß es eine geistige Erkraftung und Ver­stärkung menschlicher Erkenntniskräfte gibt, wie etwa das Mikro­skop und Teleskop im äußeren Leben, und daß trotz der Richtigkeit des entgegengestellten Gedankenganges die fruchtbare Geistesfor­schung sich gerade jenseits eines solchen Richtigen und Unrichtigen"
      ],
      [
        "stellen muß.",
        "Die Menschen werden lernen, nicht mehr so zu pochen auf das, was sich mit den beschränkten Mitteln beweisen läßt, sie wer­den einsehen, daß das Leben andere Anforderungen an die Menschheits-entwickelung stellt als dasjenige,was man oft nur so logisch sicher nennt."
      ],
      [
        "Und ein anderes muß gesagt werden, wenn das wirkliche Suchen der Zeit, nicht das eingebildete Suchen der Zeit, in Beziehung gebracht wird mit dem, was der Geistesforscher als Aufgabe und Ziel hat.",
        "Noch einmal muß hingewiesen werden auf die gewaltigen, großen Fortschritte der Naturwissenschaft."
      ],
      [
        "Es ist ihnen gegenüber nicht zu verwundern, daß es heute Geister gibt, die glauben auf dem festen Boden der Naturwissenschaft ein Weltgebäude aufzurichten.",
        "Es gibt heute schon eine solche Geistesrichtung; sie nennt sich nobler die monistische Geistesströmung."
      ],
      [
        "Diese Geistesströmung, deren Ober­haupt der ganz gewiß auf seinem naturwissenschaftlichen Gebiete große Haecke/, deren Feldmarschall Ostwa/d ist, sie versucht durch einen Ausbau dessen, was nur aus Naturerkenntnis gewonnen werden kann, eine Weltanschauung aufzubauen.",
        "Das Suchen der Zeit wird gegenüber einem solchen Versuche zu folgendem Ergebnis kommen."
      ],
      [
        "Solange die Naturwissenschaft dabei stehen bleibt, die Gesetze des äußerlich sinnlichen Daseins zu erforschen und Zusammenhänge des äußeren sinnlichen Daseins vor der Seele zu vergegenwärtigen und darzustellen, steht sie auf richtigem Boden, auf festem Boden.",
        "Sie hat wahrhaftig Großes geleistet, daß sie alten Vorurteilen das Lebens-licht gründlich ausgeblasen hat."
      ],
      [
        "So wie noch Faust selbst vor der Natur gestanden und zu einer äußeren, materiellen Magie gegriffen hat, so kann derjenige, der heute die Naturwissenschaft versteht, nicht mehr zu einer äußeren, materiellen Magie greifen.",
        "Aber ein anderes ist es, daß das geistige Leben selber auf dem Wege, der charakterisiert worden ist, eine innere Magie der Seele zeigt."
      ],
      [
        "Gegen alle theoretische Naturerklärung, gegen allen Aberglauben, gegen alle Geistesströmung, die die äußere Natur so erklären will, daß sie dieses oder jenes Wesen findet hinter den Naturerscheinungen so, wie man einen Dämon hinter den Rädchen einer Uhr sucht, hat die Naturwissenschaft ihr Großes geleistet in der Negation dieser Weltanschauung.",
        "Solange die Geister sich damit befassen, das alte Ungesunde zu bekämpfen, solange"
      ],
      [
        "Front gemacht werden kann gegen solche Geistesströmung, solange lebt eine solche Naturwissenschaft von dem, was bekämpft werden mußte.",
        "Aber dieser Kampf hat den Höhepunkt schon überschritten, er hat sein Gutes schon geleistet.",
        "Nun gilt es nicht mehr den Kampf zu führen, sondern zu fragen: Mit welchen Mitteln können wir eine Weltanschauung bilden, in welcher die Seele lebend Platz hat?",
        "Da versagt der Haeckelsche Monismus.",
        "Immer klarer und klarer wird es werden, daß die Naturwissenschafter groß waren als Soldaten, als Krieger im Bekämpfen des alten Aberglaubens, daß sie aber sind wie Krieger, die den Krieg vollendet haben und heimkommen und nicht die Kräfte haben, um Industrien zu entwickeln, Ackerbau zu treiben.",
        "Der Naturwissenschaft soll nicht ihre Größe genommen werden, wenn sie hingestellt wird als Bekämpfer abergläubischer Vorstellun­gen.",
        "Solange die Denker stehen bleiben im Kampfe, haben sie etwas, was sie aufrecht hält; wenn aber der Mensch eine Weltanschauung sich aufbauen will, in welcher in den Vorstellungen die Seele einen Platz hat, da stehen sie als Krieger da, die keinen Platz haben in Friedenszeiten, und es baut sich eben keine Weltanschauung auf."
      ],
      [
        "Diese Stimmung kann der Geistesforscher schauen in den Unter­gründen der Seele.",
        "Das ist das Geheimnis der heutigen Zeit.",
        "Aber wenn sie so von einem höheren Gesichtspunkte aus durchaus zeit­gemäß ist, diese geistesforscherische Weltanschauung, sie ist unzeit­gemäß vor vielen Zeitgenossen, die nicht tief genug hineinschauen in das, was sie eigentlich selber wollen.",
        "Daher bringt diese Geistes­wissenschaft zunächst ein Weltenbild, das sich so ansieht, als ob es nicht auf einem festen wissenschaftlichen Boden stünde.",
        "Das Welten-bild des Monismus will nur auf der Grundlage der äußeren Welt und Wissenschaft aufgebaut sein.",
        "In innerer Aktivität der Geistesforschung ergibt sich für die Seele, was die Seele erhebt zur Geistesgemeinschaft, ergibt sich die Geisteswelt in wahrnehmbarer Aktivität.",
        "Durch die Geisteswissenschaft kann der Mensch wieder wissen von der wahren Geisteswelt.",
        "Davon weiß das sogenannte monistische Weltenbild nichts zu sagen."
      ],
      [
        "Dieses Suchen der menschlichen Seele läßt sich nicht unterdrücken, und so hat sich ein Teil unserer Zeitgenossen schon daran gewöhnt,"
      ],
      [
        "die Gedanken gleichsam in sich selber so zu stellen, daß sie laufen wie die Gedanken der äußeren Naturwissenschaft.",
        "Was ist geworden?",
        "Das ist geworden, daß ein Teil unserer Zeitgenossen - die sich damit be­schäftigen, die wissen es - darauf verfallen ist, das Geistige so ansehen zu wollen, wie man das Sinnliche anschaut."
      ],
      [
        "Ich sage nicht, daß nicht auf diesem Wege etwas durchaus Wahres zustande kommen kann, aber die Methode ist eine andere.",
        "Dasjenige, was man Spiritismus nennt mit allen seinen Auswüchsen, das will äußerlich ohne Aktivität in der Wahrnehmung geistige Wesenheiten und Vorgänge äußerlich passiv anschauen, so wie man physisch-sinnliche Vorgänge anschaut."
      ],
      [
        "Wessen Kind ist dieser rein äußerliche Spiritismus?",
        "Das Kind jener Geistesströmung, die auf dem Standpunkte der monistischen Strö­mung steht und dem Aberglauben des Materialismus sich hingibt.",
        "Was, wird ein Zeitgenosse sagen, der Spiritismus ein Kind des echten Haeckelschen Monismus? - Die Welt wird sich überzeugen, daß es mit diesem Kinde so geht wie im Leben."
      ],
      [
        "Mancher Vater, manche Mutter hat die schönsten Gedanken über all das, was im Kinde sich entwickeln soli, und es kann doch ein rechter Balg entstehen.",
        "Was der Monismus sich als wirkliche Kulturerrungenschaft erträumt, was er der Menschheit geben will, auf das kommt es nicht an: der bloße Glaube an das Materielle wird den Glauben erzeugen, daß die Geister materiell sich betätigen."
      ],
      [
        "Je mehr der rein monistische Materiallsmus wachsen würde, umsomehr würden spiritistische Gesellschaften auf-blühen als das notwendige Gegenbild.",
        "Je mehr es den Bekennern der Haeckel- und Ostwald'schen Richtung gelingen wird, wahre Geisteswissenschaft zurückzudrängen, destomehr werden sie sehen, daß sie züchten werden den Spiritismus, die Kehrseite der wahren Geisteswissenschaft."
      ],
      [
        "So sicher der Geistesforscher steht auf dem Boden des erkennenden, des wißbaren Geisteswissens, so wenig kann er der Methode folgen, die den Geist materialisieren will, so wenig kann er sich hingeben dem passiven Forschen des materialistischen geistigen Lebens."
      ],
      [
        "Ein Mann, der als Philosoph eine gewisse Schätzung verdient, hat einen sonderbaren Aufsatz in einer viel gelesenen Zeitschrift geschrie­ben.",
        "Er schrieb zum Beispiel, daß Spinoza und Kant für manche"
      ],
      [
        "Menschen schwer zu lesen sind, man liest sich hinein, aber da wandeln und wirbeln die Begriffe nur so dahin.",
        "Es soll nicht geleugnet werden, daß es für die meisten Menschen so ist, daß die Begriffe durchein­anderwirbeln.",
        "Jener Philosoph gibt einen Ratschlag, wie man das gemäß dem Suchen unserer Zeit anders gestalten könnte.",
        "Er sagt :"
      ],
      [
        "Wir haben ja heute eine Einrichtung, einen technischen Fortschritt, durch den das, was bloß in abstrakten Gedanken die Seele verwirrt, recht anschaulich vor die Seele gebracht werden kann. - Der Philosoph will in einer Art von Kino zeigen, wie Spinoza zunächst dasitzt und Glas schleift, wie der Gedanke der Ausdehnung über ihn kommt, der sich verwandelt in das Bild des Denkens und so weiter.",
        "So könnte die ganze Spinoza'sche Ethik und Weltanschauung aufgebaut werden auf kinematographische Weise.",
        "Dem Suchen der Zeit wäre Rechnung getragen.",
        "Merkwürdig, daß der Herausgeber dieser vielgelesenen kine­matographischen Schrift die Anmerkung gemacht hat, so könnte dem uralten metaphysischen Bedürfnisse des Menschen durch eine Er­findung, die manchen als Spielerei erscheint, abgeholfen werden."
      ],
      [
        "Nun könnte es ja von einer gewissen Seite her dem äußeren Suchen der Zeit angemessen sein, wenn man Spinozas Ethik im Kino oder im Film Kants Kritik der reinen Vernunft ablesen könnte.",
        "Warum denn nicht?",
        "Das liebt unsere Zeit.",
        "Wir können uns überzeugen, daß man diese passive Hingabe liebt.",
        "Sehen wir uns einmal an, sagen wir, die Anschlagsäulen, versuchen wir die Gedanken der Menschen zu erraten, die davorstehen.",
        "Zu einem Vortrage, wo keine Lichtbilder gegeben werden, wo darauf reflektiert wird, daß die Seele aktiv mit-arbeitet, sind die Menschen schwer zu haben.",
        "Sie werden s ich lieber dorthin begeben, wo man sich nur passiv hinzugeben braucht.",
        "Wenn man aber in die Tiefen der Zeit hineinschaut, weiß man, daß in der Seele doch ruht der Trieb nach Aktivität, der Trieb, sich wiederzu­finden als Seele in voller Aktivität.",
        "Frei, mit sicherem innerem Halt bedacht, kann die Seele nur sein, wenn sie innere Aktivität hat.",
        "Im Leben sich zurechtfinden, sich orientieren kann die Seele nur, wenn die Seele sich bewußt wird und wenn sie weiß, daß sie dabei ist bei dem, was sie in Tätigkeit zu erleben vermag.",
        "Und von der Geisteswelt vermag sie nur das einzusehen, was sie tätig zu erleben weiß, was sie"
      ],
      [
        "sich in Tätigkeit zu erringen weiß.",
        "In der Geistesforschung wird Wahrnehmen zugleich eine Art Mitarbeit : dadurch wird Geistes­wissenschaft zu einer Erweckung der tief unterbewußten Triebe der Seele.",
        "Im geisteswissenschaftlichen Denken wird Mitdenken zu einer Tätigkeit, zu einer Aktivität."
      ],
      [
        "Dadurch kommt sie entgegen dem in­timsten Suchen unserer Zeit.",
        "Denn in bezug auf die hier berührten Dinge ist unsere Zeit eine Zeit des Überganges.",
        "Es ist leicht und trivial zu sagen, wir leben in einer Übergangszeit, denn jede Zeit ist eine Übergangszeit."
      ],
      [
        "Daher ist ein solcher Ausspruch richtig, aber banal.",
        "Es kommt darauf an, zu wissen, worin in einer solchen Zeit der Übergang besteht.",
        "Will man unsere Zeit in ihren Übergängen schildern, muß man sagen : Es ist notwendig - denn dadurch konnten die Naturwissenschaften und was durch sie groß geworden ist, zu ihren Errungenschaften kommen -, daß einmal die Menschheit durch Jahrhunderte durch die Erziehung zur Passivität gegangen ist."
      ],
      [
        "Denn nur so, durch die Hingebung an die materialistischen Wahrheiten, konnte erreicht werden, was erreicht werden mußte.",
        "Aber es ist im Leben so, daß alles sich rhythmisch abspielt, wie ein freies Pendel."
      ],
      [
        "So muß die Menschenseele, wenn sie erzogen worden ist durch Jahr­hunderte in treuer, passiver Hingabe, sich aufraffen zur Aktivität, um sich zu finden.",
        "Denn was ist sie durch die Passivität geworden?",
        "Das­jenige, was sie geworden ist durch die Passivität, werde ich ungescheut aussprechen mit dem radikal klingenden Satze, der für viele zwar viel zu paradox klingt."
      ],
      [
        "Aber auf der anderen Seite zeigt gerade das Einleben in die Geisteswissenschaft, daß, wenn man dieses radikale Ergebnis nicht betont, man sich nicht zur Konsequenz aufrafft.",
        "Man hat nicht den Mut, die wirkliche Konsequenz zu ziehen, auch bei den­jenigen nicht, welche vorgehen, einzig und allein auf dem Boden der Naturwissenschaft zu stehen."
      ],
      [
        "Denn hätte man den Mut, dann würde man merkwürdige Worte äußern hören im Suchen der Zeit."
      ],
      [
        "Am Ausgangspunkte der alttestamentlichen Urkunden stehen die Worte - jeder mag sie nehmen, wofür er sie nehmen kann, er mag sie für ein Bild oder eine oberflächliche oder tiefere Tatsache halten; in dem, was ich darüber zu sagen habe, können alle übereinstimmen - : «Ihr werdet sein wie Gott, und unterscheiden das Gute und Böse!»"
      ],
      [
        "Es klingt uns das Wort herüber aus dem Anfang des Alten Testarnen­tes.",
        "Wie man es auch nehmen will, das wird man zugeben müssen, daß es ein Bedeutungsvolles ausdrückt für die Menschennatur.",
        "Dem Versuchet wird es zugeschrieben, der herannaht an den Menschen und ihm ins Ohr sagt : «Wenn du mir folgst, so witst du sein wie ein Gott und unterscheiden das Gute und Böse.» Das wird man einsehen können; alle menschliche Freiheit und Selbständigkeit hängt mit dem zusammen, was diese Worte ausdrücken."
      ],
      [
        "Aber sie drücken aus, daß der Mensch gewissermaßen aufgefordert wurde durch den Ver­sucher, über sich hinaus sich anzuschauen wie ein anderes Wesen als er ist, wie ein Gott sich zu verhalten zu dem Guten und Bösen.",
        "Mag man über dieses Wort und den Versucher denken, wie man will."
      ],
      [
        "Dieser Versucher - ich fordere nicht, daß man ihn hinnimmt wie ein wirkliches Wesen, obschon : «Den Teufel spürt das Völkchen nie, und wenn er sie beim Kragen hätte» - wie man ihn auch nehmen mag, derjenige, der das Suchen der Zeit ein wenig zu belauschen vermag, der hört denn doch sein Raunen wieder, er nahet sich : da ist er - ohne allen Aberglauben mag es gesagt werden, da ist er, und für diejenigen, welche den Mut haben, die letzte Konsequenz der reinen naturwissenschaftlichen Weltanschauung zu ziehen, bringt er Worte einer großen Eigentümlichkeit, einer sonderbaren Weisheit hervor.",
        "Sie haben nur nicht den Mut zur letzten Konsequenz, denn sie nehmen doch den Glauben auf an eine Unterscheidung des Guten und Bösen."
      ],
      [
        "Sie müßten diesen Glauben ableugnen, wenn sie rein auf dem Boden der bloßen naturwissenschaftlichen Notwendigkeit sich stellten.",
        "Sie müßten sagen : Es scheint die Sonne gleichmäßig über Gute und Böse - sie müßten sagen, daß das Böse geradeso verrichtet wird wie das Gute."
      ],
      [
        "Es raunt der Versucher die Konsequenz der bloßen naturwissenschaftlichen Weltanschauung : Ihr seid ja nur höher entwickelte Tiere, ihr seid ja Tiere - und das ist, was der Ver­sucher spricht : Ihr seid ja nur entwickelte Tiere und dürft, wenn Ihr Euch selbst versteht, keinen Unterschied machen zwischen dem Guten und Bösen. - Das ist es, was unsere Zeit zu einer Übergangszeit macht, daß der Versucher mit der das Entgegengesetzte zuraunenden Stimme in unserer Zeit wieder spricht."
      ],
      [
        "Hätte man den Mut, so wäre das die Konsequenz der bloß passiven Hingabe an die naturwissenschaftliche Erkenntnis.",
        "Daß die Zeit be­wahrt bleibe vor dieser Stimme, daß in das Suchen der Zeit hinein­gebracht werde Wissen vom geistigen Leben, das ist die Aufgabe, das Ziel der Geisteswissenschaft."
      ],
      [
        "Diejenigen, die diese Geisteswissen­schaft noch bekämpfen vom Standpunkte einer Wissenschaft, sie werden sich überzeugen müssen, daß es sich mit diesem Kampfe so verhält, wie es sich mit dem Kampfe gegen den Kopernikanismus verhielt.",
        "Jetzt, wo wir durch unseren Bau in Dornach hervorgetreten sind und mehr beachtet werden, mehren sich auch die Stimmen der Gegner."
      ],
      [
        "Als ich auf solche Stimmen einwendete, daß die Gegner auf jenem Standpunkte stehen, da sagte einer, der sich betroffen fühlte mit Recht, der Unterschied wäre nur der, daß das, was Kopernikus sagte, Tatsachen seien und daß das, was die Geisteswissenschaft bringe, nur Behauptungen seien - er merkt nur nicht, der Arme, daß für die Leute damals die Lehren des Kopernikus auch nichts anderes waren als leere Behauptungen.",
        "Er merkt nicht, daß es sich hier um Tatsachen geistigen Lebens handelt, daß er heute leere Behauptungen nennt, was vor einer wirklichen Forschung Tatsachen des geistigen Lebens sind."
      ],
      [
        "Und so kann man Einwand über Einwand aus dem Suchen unserer Zeit heraus erhoben finden von der Wissenschaft und von seiten des religiösen Lebens.",
        "Aber so wie diejenigen Menschen mit sich zurechtgekommen sind, welche zur Zeit des Kopernikus gesagt haben : An die Umdrehung der Erde können wir nicht glauben, sie steht nicht in der Bibel, - so sagen die Leute heute : An das, was die Geisteswissenschaft zu sagen hat, glauben wir nicht, es steht nicht in der Bibel. - Doch, so werden die Menschen mit dem, was die Geisteswissenschaft zu sagen hat, zurechtkommen, wie die Bibel-gläubigen mit der Sache des Kopernikus zurechtgekommen sind."
      ],
      [
        "Immer wieder muß erinnert werden an einen zugleich gelehrten, tief gelehrten Mann und Priester, der an der hiesigen Universität ge­wirkt hat, Rektor dort war.",
        "Als er seine Rektorrede gehalten hat über Galilei, sagte er : Damals standen die Leute, die da an Religiöses glaubten, auf dem Standpunkte des Glaubens; heute weiß der wahr­haft religiöse Mensch, daß durch jede neue Wahrheit, die erforscht"
      ],
      [
        "wird, ein Stück zu der Herrlichkeit der göttlichen Weltordnung hinzu­gefügt wird. - So könnte man annehmen, vor Kolumbus wäre jemand hingetreten und hätte gesagt : Das neue Land dürfen wir nicht ent­decken, wir leben in einem schönen Lande, in dem die Sonne scheint; wissen wir denn, daß die Sonne auch die Kraft hat, das neue Land zu bescheinen?",
        "So kommen dem Religösen, der an seinem Glaubens-dogma hängt, die Entdeckungen der Geisteswissenschaft vor, und so kommen dem Geistesforscher diejenigen vor, die die religiösen Empfindungen gestört glauben durch die Entdeckungen der Geistes­wissenschaft.",
        "Der muß eine wankende religiöse Vorstellung, einen schwachen Glauben haben, der da glauben kann, diese göttliche Sonne werde nicht auch das neue geistige Land bescheinen.",
        "Die Zeit aber in ihrem Suchen, wenn sie immer mehr und mehr sich durchdringen wird mit Geisteswissenschaft, sie wird davon so berührt werden, wie manche heute es noch nicht sich träumen lassen.",
        "Geisteswissenschaft hat begreiflicherweise noch viele Gegner, aber im Einklang fühlt man sich doch in dieser Geisteswissenschaft mit all denjenigen Geistern der Menschheit, die, wenn sie auch noch nicht Geisteswissenschaft gehabt haben, doch geahnt haben jenen Zusammenhang der Men­schenseele mit den geistigen Welten, der eben durch die Geistes­wissenschaft aufgeschlossen wird."
      ],
      [
        "So fühlt man sich gerade in bezug auf das, was über das neue Wort des Versuchers gesagt worden ist, im Einklange mit fchilkr und seinem Ahnen der geistigen Welt.",
        "Er hat durchaus den Impuls bekommen, den Menschen mit seiner Seele herauszuheben aus der bloßen Tierheit, hat gewußt, daß der Mensch seinen Anteil hat an der geistigen Welt.",
        "Man fühlt sich im tiefen Einklang mit diesem führenden Geiste der neuen geistigen Weltanschauung, man empfindet, daß man dasjenige, was heute mit breiteren Sätzen ausgeführt werden sollte, wie in ein Gefühl zusammenfassen kann mit den Schillerschen Worten : Die Tierheit wich!",
        "Bekräftigend dies steht die Geisteswissenschaft gegen­über dem Versucher der heutigen Zeit."
      ],
      [
        "Es darf erinnert werden an einen Geist, der hier in Österreich gewirkt hat, der gefühlt hat in seiner tiefen Seele den dunklen Drang dessen, was die Geisteswissenschaft zur Gewißheit erhebt.",
        "Gefühlt"
      ],
      [
        "hat er es, mit seinem Denken einsam dastehend, an geistigen Aus­blicken festhaltend, trotzdem er als Arzt auf dem Boden der Natur­wissenschaft stand : Ernst Freiherr von Feuchtersleben, der tief gemütvolle Mensch.",
        "Und zusammengefaßt sei dasjenige, was heute gesagt worden ist, in den Worten Feuchterslebens, in denen lebt, was in der Seele erfühlt werden kann als geistige Kraft, wenn sie sich mit Geistes­wissenschaft erfüllt hat, wenn sie sich gewiß ist ihres Zusammen­hanges mit der geistigen Welt : « Die menschliche Seele kann es sich nicht verhehlen, daß ihr wahres, berechtigtes Glück doch nur liegt in der Erweiterung ihres inneren Wesens und Besitzes.» Die Erweiterung, die Befestigung, die Sicherung dieses inneren Wesens, dieses geistigen Innenwesens der Seele, soll dem Sucher der Zeit durch die Geistes­wissenschaft dargeboten werden!"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "WAS HAT DIE GEISTESWISSENSCHAFT ÜBER LEBEN, TOD UND UNSTERBLICHKEIT DER MENSCHENSEELE ZU SAGEN? Öffentlicher Vortrag am 8. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Wenn es schon in einer gewissen Beziehung schwierig ist, sich über die Grundlage der Geisteswissenschaft, wie sie hier gemeint ist, so auseinanderzusetzen, wie es im Vortrag von vorgestern geschehen ist, so darf wohl gesagt werden, daß die Mitteilungen in bezug auf die­jenigen Forschungsergebnisse, die den Gegenstand des heutigen Vor­trages bilden sollen, in gewisser Beziehung eigentlich ein Wagnis sind gegenüber den Vorstellungsarten und Denkgewohnheiten der Ge­genwart. Denn wird man in dem, was der Vortrag von vorgestern ausdrückte, schon manches paradox finden müssen von diesen Vor­stellungsarten und Denkgewohnheiten aus, so wird man von einem solchen Gesichtspunkte aus ganz gewiß und begreiflicherweise es nicht leicht haben, in dem, was heute zu sagen ist, ernstes Forschen zu sehen.",
      "Man wird viel eher in weiten Kreisen der Gegenwart geneigt sein, darinnen nur die Schwärmereien eines sonderbaren Phantasten zu sehen. Dessen muß man sich wohl bewußt sein, wenn man über diese Dinge redet, bewußt sein dessen, daß alles dasjenige, was in einer späteren Zeit in das allgemeine Bewußtsein übergeht, vieles sogar von dem, was dann später ein Selbstverständliches wird, in der Zeit, in der es zuerst auftritt, etwas Paradoxes, etwas Phantastisches ist.",
      "Dieses möchte ich nur vorausschicken, um zu charakterisieren, wie sehr der Geistesforscher sich dessen bewußt ist, was alles begreif­licherweise empfunden werden kann, wenn er seine für die heutige Zeit durchaus noch paradox erscheinenden Forschungsresultate mit­zuteilen sich gestattet.",
      "Bevor ich auf diese Forschungsergebnisse zu sprechen komme, möchte ich in ein paar einleitenden Worten die Grundstimmung der Seele des Geistesforschers charakterisieren. Diese Grundstimmung ist ja eine ganz andere als die Stimmung gegenüber einem andern Forschungsfelde. Während man dem äußeren Leben und seinen Erkenntnissen",
      "gegenüber und auch der gewöhnlichen Wissenschaft gegenüber heute mit einem gewissen Recht das Gefühl hat, man habe die Erkenntniskräfte in sich, man brauche sie nur sozusagen in Wirk­samkeit überzuführen, dann könne man urteilen über all dasjenige, was die Natur selbst und der Forscher aus der Natur darbietet, während man bei dieser Forschung alle Mühe darauf verwendet, um eben zu forschen, um eben die Dinge zu beobachten und durch den Verstand ihre Gesetze zu erkennen, ist die Stimmung des Geistes­forschers gegenüber der Wahrheit, gegenüber allem Erkenntnis­streben doch eine ganze andere. Da bekommt man, indem man sich in diese Geistesforschung hineinarbeitet, immer mehr das Bedürfnis, alle Arbeit der Seele, all ihr Streben zunächst auf die Vorbereitung zu verwenden und man bekommt immer mehr und mehr das Gefühl : wenn man sich irgendeiner Wahrheit aus diesem oder jenem Gebiet nähern will, so möchte man eigentlich immer noch warten, immer weiter und weiter sich vorbereiten, weil man das Bewußtsein hat : je mehr Mühe und Arbeit auf jenen Weg verwendet wird, bevor man forscht, desto mehr macht man sich reif, die Wahrheit zu empfangen.",
      "Denn ein Empfangen der Wahrheit, das ist es, um was es sich bei der eigentlichen Geisteswissenschaft handelt. Und so stark kommt diese Stimmung über die Seele, daß man eine heilige Scheu empfindet, die Dinge an sich herankommen zu lassen, und immer wiederum gegen­über wichtigen, wesentlichen Ergebnissen der Geistesforschung lieber wartet, als die Dinge zu früh in das Bewußtsein hineinkommen zu lassen.",
      "Das bedingt eine ganz besondere Stimmung in dem Geistesforscher selbst, jene Stimmung, die all die Arbeit, von der vorgestern als einer inneren Seelenarbeit in Übungen gesprochen worden ist, allmählich durchdringt : eben die Stimmung von heillget Scheu gegenüber der Wahrheit. Nachdem ich dies vorausgeschickt habe, möchte ich nun unbefangen auf dasjenige eingehen, was über das wichtige, bedeutungsvolle, jeder Seele so naheliegende Thema des heutigen Abends zu sagen sein wird.",
      "Gewiß, es sind nicht die schlechtesten Gemüter unserer Gegenwart, die noch immer festhalten an der Meinung, daß die Wahrheiten des Glaubens besondere seien, und die Wahrheiten des Wissens auch besondere",
      "seien, und die da glauben, daß all dasjenige, was der Mensch sich vorstellen kann als über Geburt und Tod hinausgehend, nur ein Gegenstand des Glaubens und nicht streng beweisbare Wissenschaft sei. Gerade diese strenge Trennung zwischen Glauben und Wissen, sie wird durch die Geisteswissenschaft aufgehoben werden.",
      "Und man fühlt sich doch im Einklang mit dem, was längst hinein wollte in das moderne Geistesstreben, wenn man die Wahrheiten, die jenseits des Todes liegen, in dem Sinne entwickelt, wie es hier geschehen soll, wenn man sich immer wieder so etwas vor Augen hält, wie zum Bei­spiel der große Lessing mit einer der Hauptwahrheiten dieser Geistes-forschung sich doch auseinandersetzte in jener Schrift, die er wie sein geistiges Testament kurz vor dem Tode als reife Frucht seines Denkens und Sinnens verfaßt hat : «Die Erziehung des Menschen­geschlechts». Und es scheut Lessing nicht zurück zu sagen, daß die Anschauung von den wiederholten Erdenleben nicht deshalb ein Irrtum zu sein braucht, weil sie auftrat gleichsam als etwas Erstes, worauf das Menschengeschlecht kam, bevor noch die Vorurteile der Schule und Philosophie etwas wie einen trüben Schleier gebreitet haben über das, was die Menschheit im Beginne der Kulturentwicke­lung vom Jenseits des Todes wußte.",
      "So fühlt man sich gerade auf dem Boden der Geisteswissenschaft in Einklang - es könnten noch viele Geister angeführt werden - mit den besten Persönlichkeiten, die ihr Streben einfügten in die Kulturentwickelung der Menschheit.",
      "Gesagt worden ist vorgestern, daß die Dinge des geistigen Lebens, die Vorgänge des geistigen Lebens nur erforscht werden können dann, wenn wirklich der Mensch durch das vorgestern Geschilderte dazu kommt, in seiner Seele die in ihr schlummernden Fähigkeiten so zu erkraften, daß diese Seele die Möglichkeit findet, durch die geisti­gen Übungen sich herauszuziehen aus dem Physisch-Leiblichen und sich abgesondert von dem Physisch-Leiblichen zu erleben, so daß der Mensch dann einen Sinn verbinden kann mit den Worten : Ich erlebe mich als seelisch-geistiges Wesen außerhalb meines Leibes, und mein Leib mit alledem, was zu ihm gehört in der Sinneswelt, steht vor mir, wie em außerer Gegenstand vor uns steht in der Sinneswelt. - Und schon als ich das letzte Mal hier einige öffentliche Vorträge halten",
      "durfte, konnte ich aufmerksam machen auf den bedeutungsvollen Augenblick, der im Leben des Geistesforschers dann eintritt, wenn wirklich dieser Geistesforscher durch die vorgestern erwähnten Übungen, die Sie näher beschrieben finden in «Wie erlangt man Er­kenntnisse der höheren Welten?» und «Geheimwissenschaft» - hier soll nur hingewiesen werden auf diese Momente - reif geworden ist. Dann kommt eines Tages - man könnte auch sagen eines Nachts -dieses Ereignis.",
      "Es kann eintreten mitten in den gewöhnlichen Vor­gängen des Tages, mitten in der Nacht, und wird, wenn in der richtigen Weise vorbereitet, weder das eine noch das andere stören. In hundert­facher Weise kann es auftreten, ich möchte nur den typischen Charak­ter schildern, der immer ähnlich sein wird dem, was ich jetzt anführen werde.",
      "Da kommt es so, daß der Mensch, wenn er aufwacht aus dem Schlafe, weiß : es geht etwas vor, was kein Traum ist. Er ist entrückt allem, was ihn mit dem Tag verbindet. Oder mitten in den Tagesereignissen tritt ein Moment ein, wo etwas ganz anderes in das Vor­stellen, das Bewußtsein hereintritt.",
      "Das kann dann so sein - es wird immer ähnlich sein dem, was ich jetzt möglichst konkret schildern will -, dies erschütternde Ereignis, daß man das Gefühl hat : Du bist jetzt wie in einem Haus, in das der Blitz eingeschlagen hat. Deine Umgebung löst sich auf wie ein Haus, in das der Blitz geschlagen, und der Blitz geht durch dich durch.",
      "Man fühlt alles, womit man verbunden ist, wie durch die Elemente aus einem herausgelöst. Es ist der denkbar tieferschütterndste Eindruck. Von diesem Momente an oder einem ähnlichen weiß man, was es heißt : außer seinem Leibe in der Seele sich selbst zu erleben.",
      "Und die Geistesforscher aller Zeiten, sie haben einen Ausdruck gebraucht für dieses Erlebnis, der volitreffend er­scheint demjenigen, der das Erlebnis kennt. Denn es hat zu allen Zeiten, wie es die verschiedenen Kulturen bedingten, eine Art von Geistesforschung gegeben.",
      "Die heutige ist angemessen den Fort­schritten der modernen Naturwissenschaft. Aber das, was durch sie erreicht wird, wurde auch erreicht durch die Methoden, die durch die verschiedenen Kulturen möglich waren.",
      "So haben die Geistesforscher der verschiedenen Zeiten die Worte geprägt : Man sei als Mensch angekommen an der Pforte des Todes. - Und tatsächlich, was",
      "man sich zunächst vorstellen kann als erlebbar durch den Tod, es tritt ein nicht unmittelbar als eine Wirklichkeit, denn der Geistes­forscher tritt ja wieder in seinen Leib zurück; alles das aber, was er erlebt, das ist das Bild von demjenigen, was sich wirklich zuträgt, wenn der Mensch durch die Pforte des Todes schreitet, wenn das äußere physische Leben aufhört und das Leben nach dem Tode beginnt. Will man nun verstehen, wie der Geistesforscher zu den Dingen kommt, von denen hier die Rede ist, so muß man sich eben vergegenwärtigen, daß er durch sorgfältige Vorbereitung seiner Seele dazu kommt, ganz anders wahrzunehmen als mit den äußeren Sinnen, daß er wirklich hineinschauen kann in diejenigen Sphären des Daseins, von denen gesprochen werden soll.",
      "Das erste, wozu der Geistesforscher kommt, wenn er einen solchen Moment überwunden hat, bei dem man an der Pforte des Todes steht, könnte man nennen : man gelangt jenseits des menschlichen Gedächtnisses. Die menschliche Gedächtnis- und Erinnerungskraft ist etwas, was gewissermaßen in unserer Seele lebt als der Anfang, möchte man sagen, von einem Geistigen. Das sehen heute selbst schon äußere philosophische Forscher ein. Der zu so glänzendem Erfolg gekommene französische Forscher Bergson sieht schon in dem Gedächtnis des Menschen, in dem Behalten der Erinnerungen etwas rein Geistiges. Und wenn erst die Vorurteile der Naturwissenschaft, die heute noch fast an jedem haften, vorüber sein werden, dann wird man einsehen, wie in dem Schatz unseres Gedächtnisses für die Men­schenseele schon etwas vorliegt, was der Anfang ist zu einem Über­gang zum rein Geistig-Seelischen. Indem wir unsere Vorstellungen zurückschieben in das Gedächntis, bewahren wir sie rein in der Seele auf, nicht durch äußere Vorstellungen. Die naturwissenschaftliche Rechtfertigung dessen, was eben gesagt wurde, würde im Augenblick zuviel Zeit in Anspruch nehmen.",
      "So nun, wie man im gewöhnlichen Leben Erinnerungsbilder wahr­nimmt, die aus dem Schatze unserer Seele heraufkommen, die so, wie sie auftreten, nichts haben, was uns verleiten könnte, sie etwa zu einer Halluzination zu machen, so treten - aber jetzt nicht aus den Seelen-schätzen herauf, sondern aus geistigen Welten heraus - vor die Seele",
      "des Geistesforschers die geistigen Vorgänge und Tatsachen. Und man merkt dann, daß hinter dem, was wir den Gedächtnisschatz nennen, die menschliche Seele noch etwas anderes erleben kann. Der Geistes­forscher sieht da gleichsam das Folgende : nun bist du aus dem Leibe mit der Seele herausgezogen.",
      "Nun kannst du erst recht überblicken dasjenige, was du dir durch die Sinnenwelt erworben hast, den Schatz des Gedächtnisses, der aber durch einen Schleier zudeckt dasjenige, was immer in der Seele ist, was aber zugedeckt wird durch das Ge­dächtnis. - Ja, in diesen menschlichen Seelentiefen ist etwas unten, das immer in ihnen lebt, aber indem der Mensch seine Erinnerungen ausbreitet in seiner Seele, deckt er das unterbewußte Geistig-Seelische zu. Indem der Geistesforscher sich ins Geistig-Seelische erhebt, hat er allerdings, man möchte sagen, wie einen Kometenschweif seines geistig-seelischen Wesens seine Erinnerungen anhängen, aber er kann durch sie hindurchschauen auf etwas, was man nennen könnte : Kräfte höherer Art, als die Kräfte sind, die unsere Erinnerungen aufbewahren.",
      "Wenn der Ausdruck nicht so verpönt wäre - aber es ist ja schwierig, die richtigen Ausdrücke zu finden -, so würde ich sagen : Man steigt von dem Gedächtnis zu einem Übergedächtnis auf. Man kommt in das allmählich hinein, was vorgestern imaginatives Vorstellen genannt worden ist.",
      "Während man bei dem Gedächtnis immer das Gefühl hat : die Bilder steigen herauf, sie stellen sich vor dich hin, indem du passiv bist, - taucht man nun unter in die Dinge und muß aktiv darinnen sein. Man muß dasjenige mit hervorbringen, was als Inhalt eines Übergedächmisses heraufstrebt.",
      "Aber man weiß auch, daß dasjenige, was sich da etitdeckt, was sich da offenbart als hinter dem Gedächtnis Liegendes, immer da war, daß es nur zugedeckt war durch das Ge­dächtnis. Und man weiß, daß dies, was sich da hinunterschiebt, selbst etwas ist, was nun an unserem physischen Organismus arbeitet, was tätig ist an demselben.",
      "Noch eine andere Entdeckung macht man. Sie ist außerordentlich bedeutungsvoll für das Verhältnis der Geistesforschung zur Natur­forschung. Die Naturforschung tritt uns entgegen, indem sie sagt :",
      "All dasjenige, was Menschen sagen, denken und wollen, ist gebunden an die Vorgänge des Nervensystems. Recht hat sie damit, aber sie",
      "kann mit ihren Mitteln nicht die Art, wie das Seelenleben an das Nervensystem gebunden ist, herausbekommen. Man muß zu viel tieferen Grundiagen des Seeleniebens gehen, wenn man mit Geistes­forschung kommt.",
      "Da merkt man : Ja, es ist für das gewöhnliche Vor­stellen des Alltags durchaus richtig, daß alle Gedanken, die wir uns bilden, zum Beispiel an das Gehirn gebunden sind. - Aber wie? Das tiefere Seelische, von dem das gewöhnliche Bewußtsein gar nichts weiß, das bearbeitet erst, sagen wir, eine gewisse Gehirnpartie, das sendet erst seine Arbeitskraft hinein in Sinne und Gehirn.",
      "Dadurch, daß dieses unterbewußte Seelische das Nervensystem bearbeitet, wird es zum Spiegel, und das, was im gewöhnlichen Leben auftritt, ist das Spiegelbild des Seelisch-Geistigen. Gerade wie, wenn Sie sich einem Spiegel nähern, Sie nicht sich sehen oder sich erfühlen, sondern nur das Spiegelbild sehen würden, geradeso verhalten Sie sich, indem Sie Ihr alltägliches Vorstellen, Fühlen und Wollen entwickeln.",
      "Das tiefere Seelische arbeitet erst, und was es da erarbeitet, das macht, daß etwas wahrgenommen werden kann. So ist es das Seelisch-Geistige, was das Auge bearbeitet und was im Auge gewisse Vorgänge hervorruft.",
      "Das Auge spiegelt dann in das Seelisch-Geistige das zurück, was wir zum Beispiel Farben nennen. So ist es das tiefere Seelisch-Geistige, was in dem Leiblichen arbeitet. Und die Geistesforschung wird die Menschen dazu führen, zu erkennen, daß wir es selbst sind, die im Innern unserer Vorstellungen leben und mit dem tieferen Wesen selbst den Leib zu­bereiten, so daß er zum Spiegelungsapparat wird.",
      "In dem Augenblick, wo unsere Vorstellungen zu Erinnerungs­bildern werden, muß aber noch etwas anderes vorgehen. Wir müssen, wenn nicht die Vorstellungen wie Träume an uns vorüberhuschen, sondern zur Erinnerung werden sollen, Aufmerksamkeit verwenden. Alles, was zur Erinnerung werden soll, was bleiben soll in der Seele, auf das müssen wir uns länger konzentrieren als zu einem bloßen Vorstellungsbild. Ein Farbeneindruck würde uns nicht in der Erinne­rung bleiben, wenn wir ihn nur kurz anschauten. Schauen wir ihn etwas länger an, so appellieren wir an die Kraft, die in unserer Seele alles das als Erinnerung behält. Wir schieben unsere Seelentätigkeit in ein tieferes seelisches Wesen zurück. Dieses tiefere seelische Wesen",
      "stellt sich der Geistesforschung dar als ein feiner ätherischer Leib, den man in der Geistesforschung mit dem allerdings verpönten Aus­druck «ätherisch» bezeichnen kann - doch hat das Wort nicht den Sinn, den man in der Chemie gewöhnlich damit verbindet -, es stellt sich dar als ein ätherischer Leib, der schon geistiger Art ist.",
      "Aber nicht nur so wirkt unsere Seele, daß sie diese Erinnerungs­bilder schafit, sondern im Leben zwischen Geburt und Tod schafft sie noch viel mehr in sich hinein. Und da entdeckt die Geistesforschung das Merkwürdige, daß unsere Erinnerungen nur deshalb Vorstellun­gen bleiben, weil sie vom Ätherleibe aufgehalten werden, weil sie nicht in den physischen Leib hineingelassen werden.",
      "Würden sie hineingelassen und zur Tätigkeit darinnen werden, so würden sie übergehen in die Lebenskräfte des physischen Leibes, würden ihn durchorganisieren. Dadurch, daß wir unsere Vorstellungen Vorstellun­gen sein lassen, erhalten wir sie in ihrem Vorstellungscharakter.",
      "Sie können Erinnerungen bleiben, aber die Seele entwickelt auch im Leben viel stärkere Kräfte als die sind, welche die Erinnerungen ent­wickeln, und sie werden nun ebenfalls zunächst in der Seele bewahrt. Doch liegen sie wie ein Übergedächmis hinter dem gewöhnlichen Gedächtnisschatz.",
      "Sie sind in uns. Das erlebt der Geistesforscher, wenn er durch das Gedächtnis hindurchschaut auf den übergedächt­nismäßigen Schatz, daß er weiß : Da lebt in deiner Seele etwas, was nicht hineinwirken kann in den physischen Leib, was jetzt nicht zur Wirksamkeit kommt in deinem physischen Leibe, wenn er zwischen Geburt und Tod ist.",
      "Da ist etwas, was nicht Vorstellung bleibt, was aber doch nicht zur organisch wirksamen Kraft wird. - Der Geistes-forscher erlebt dieses, indem er außerhalb seines Leibes ist. Aber zugleich erlebt er das andere, das er ausdrücken kann damit, daß er sagt : Ja, da erlebe ich etwas in meiner Seele, was in ihr ist, was gewissermaßen keine Anwendung findet, weil es nicht hinein kann in den Leib, der gebildet ist seit der Geburt oder, sagen wir, der Empfängnis.",
      "Indem sich nun der Geistesforscher hineinvertieft in dieses, was ich hier angedeutet habe, erlebt er es so, daß er es crkennen kann, wie man erkennt den Keim, der in einer Pflanze ist. Die Pflanze entwickelt sich zur Frucht hinauf, in welcher der Keim ist.",
      "Keim ist, hat für diese Pflanze keinen Sinn : es kann seine Kräfte nicht in diese Pflanze hineinsenken, es ist aber darinnen, es ist die Aniage zur folgenden Pflanze des nächsten Jahres. Indem der Geistes­forscher hinuntertaucht also, taucht er ein in etwas, was in ihm ein Seelenkeim ist, der gebildet wird zwischen Geburt und Tod, der aber seine Kräfte nicht entwickelt in diesem Leben. Er taucht unter und liegt bereit in dieser Seele für ein folgendes Leben, wie in der Pflanzen-frucht der Keim bereit liegt für die folgende Pflanze, die sich nicht ohne die vorhergehende entwickeln könnte.",
      "So kommt man zur Ansicht der wiederholten Erdenleben, wenn man auf diese Weise unterzutauchen versteht in das Geistig-Seelische. Dasjenige, was wichtig ist, ist nur, daß der Geistesforscher nicht aus dem Auge verliert : Dasjenige, was du da erleben mußt, kann nur ein solches sein, bei dem du immer wieder deiner eigenen Tätigkeit dir bewußt bist. - Denn ist man das nicht, dann wird es zur bloßen Halluzination oder zur bloßen Phantasie.",
      "Es ist ein Irrtum, wenn eingewendet wird : Ja, wie kann der Geistesforscher wissen, daß das nicht Halluzination, nicht Illusion, nicht Phantasie ist? Wenn der Geistesforscher sich so stellen würde zu dem, was er auf die geschil­derte Weise erlebt, wie sich das krankhafte Gemüt zu seinen Halluzi­nationen stellt, dann würde dieser Einwand voll berechtigt sein.",
      "Man ist aber bei einer Halluzination nicht bewußt beteiligt, man durch­schaut sie nicht. Das aber lernt gerade der Geistesforscher genau kennen durch seine Vorbereitungen, daß er unterscheiden kann das­jenige, was nur Reminiszenz der Außenwelt ist, zu dem er sich passiv verhalten muß, von demjenigen, was sich so hinstellt, daß er es erkennt, wie man von einem Buchstaben oder einem Worte weiß : Das, was auf dem Papier steht, bedeutet nicht den Buchstaben nur, sondern etwas anderes.",
      "Denn so verwendet der Geistesforscher nicht dasjenige, was er schaut in der Geistesforschung, wie es bei der Halluzination verwendet wird, sondern er verwendet es so, daß man es vergleichen kann mit einem geistigen Lesen in einer Schrift von Imaginationen, die sich hinstellen. Erst wenn man lernt in seinem Gemüt, dasjenige, was man da in Aktivität hinstellt, so zu verwenden, daß man darinnen lebt wie in den Schriftzügen, die man auch nicht als sich-selbst-bedeutend",
      "hinnimmt, erst indem man sich in freier Weise zu dem erhebt, was da in die Seelenschau hineintritt, kann man dahin gelangen, wirk­lich zu erschauen dasjenige, was Vorgänge und Wesenheiten der geistigen Welt sind. Dann aber kommt man, weil man ja dann sich einlebt in das Element der Seele, das nicht mit dem Leibe einerlei ist, in das Wesen, von dem man sagen kann, daß die Eigenschaft der Unsterblichkeit ihm zukommt.",
      "Geisteswissenschaft ist keine spekulative Phantasie, in der man nachdenkt über die Gründe der Unsterblichkeit, sondern sie zeigt, wie man zur Seele selber kommt, und von dieser wahrhaftigen Seele zeigt sie, was sie ist. Sie legt gleichsam die Seele bloß.",
      "Und dann stellt sich heraus, daß dasjenige, was so als Seele bloßgelegt wird, kein Ergebnis der äußeren Leiblichkeit ist, daß vielmehr die äußere Leib­lichkeit selber das Produkt der Seele ist. Denn wenn man auf der einen Seite in sich entdeckt den Seelenkeim, dem man es anfühlt, aus dem man herauserlebt, daß er der Keim zu einem nächsten Erden-leben ist, so erlebt man in diesem Bewußtseinsinhalt auch dasjenige, was in das menschliche Leiblich-Physische hereingezogen ist, bevor der Mensch als physisches Wesen sein Dasein begonnen hat bei der Geburt oder Empfängnis.",
      "Da erlebt man, daß geradeso, wie die Seele selbst es ist, die räumlich, wie wir es wahrnehmen, ihr Gehirn zubereitet, so das Geistig-Seelische, zu dem man vorgedrungen ist, vor der Geburt oder der Empfängnis in einer geistigen Welt vorhin-den war und darin sich die Kräfte erworben hat, um sich zu verbinden mit dem, was an physischer Materialität gegeben wird von Vater und Mutter, sie zu durchdringen, sie sich anzuorganisieren. Man erlebt, daß der Mensch, wie er in die Welt einzieht, nicht das Ergebnis ist von Vater und Mutter, sondern daß sich verbindet das Geistige mit dem Materiellen, das Geistige, das aus geistigen Welten herunter­kommt, wo es gelebt hat zwischen dem letzten Tod und einer neuen Geburt.",
      "Und der Geistesforscher kann, wenn er so kenneniernt das, was jenseits des Gedächtnisses lebt, auch erkennen lernen, wie die Seele sich verhält, wenn nicht mehr das Leibliche die Tätigkeit des Geistig-Seelischen zurückhält, wenn der Tod über den Menschen ge­kommen ist. Wenn der Tod über den Menschen gekommen ist, dann",
      "lebt die Seele zunächst - das ist die Tatsache, die sich der Geistes­forschung darbietet - in demjenigen, was während des Lebens nicht physisch-leiblich geworden ist, im Gedächtnisschatz.",
      "In der ersten Zeit nach dem Tode breitet sich vor der Seele ein weites Erinnerungsbild von alledem aus, was der Mensch erlebt hat zwischen Geburt und Tod. Alle die Ereignisse kommen auch herauf, die im Leben vergessen worden sind. Dieses Erleben dauert nur wenige Tage. Der Geistesforscher kann dasjenige durchschauen, was da als das erste Erlebnis nach dem Tode auftritt, weil er ja die Natur des Gedächtnisses kennenlernt. Dann wird wirklich für den Geistes-forscher so etwas zum Bewußtseinsinhalt wie für den Toten, wenn er durch die Pforte des Todes geschritten ist. Vor dem Geistesforscher tritt auch auf, wenn er außer dem Leibe ist, dieser Gedankeninhalt; aber das tritt vor ihm auf wie eine Welt : Wie man sonst Sonne, Mond und Sterne, wie man Berge und Wälder um sich hat, so hat man zunächst ein Tableau vor sich; man kann es durchschauen, man kann seine Wirkungskraft ersehen. Indem man sich hineingewöhnt, wirk­lich außerleibllch diese Dinge zu durchschauen, gelangt man auch allmählich dazu, wirklich bewußt den Blick hinzuwerfen auf dasjenige, was die Seele nach dem Tode durchlebt. Erst ist es ein Erinnerungs­bild: gleichsam breiten sich alle die Gedanken aus, die sich gesammelt haben im Gedächtnis. Aber dahinter tritt eine andere Seelenkraft auf. Jetzt ist diese Seelenkraft nicht mehr durch den Leib gehemmt. Nach einigen Tagen verschwindet das Erinnerungsbild aus der Umgebung des Menschen.",
      "Man kommt ja, wie schon eingangs gesagt, auf gewagte Dinge, wenn man über das Thema des heutigen Vortrages sprechen will, aber man kann nicht umhin, wenn man auf das Konkrete eingehen will, diese Dinge zu berühren.",
      "Ich habe darzustellen versucht, was zuerst nach dem Tode erlebt wird. Da hat sich dann ergeben, daß diese Rückschau auf die Gedan­kenbilder ganz individuell für die verschiedenen Menschen verschie­den lange dauert. Aber ungefähr kann man doch sagen, daß sie so lange dauert, als die Kraft dauern kann während des Lebens, durch die der Mensch sich frei wach erhalten kann, wenn er durch irgend etwas",
      "verhindert ist, einzuschlafen. Das ist ja bei den Menschen verschieden. Diese innere Kraft, die ein Mensch hat, um den Schlaf zu bekämpfen, die ist der Maßstab für die Zahl der Tage, nach denen diese Rück­erinnerung dauert. Dann tritt etwas anderes au£ Was jetzt auftritt, in das kann man sich nur vertiefen, wenn man es auch schon durch die außerleiblichen Erlebnisse kennt. Aber es ist schwierig, Worte zu finden für die so ganz anders gearteten Erlebnisse der Seele, als es die Sinneserlebnisse sind. Unsere Sprache ist ja für die sinnliche Welt geprägt. Was außerhalb der Sinneswelt erlebt wird, erlebt die Seele ganz anders. Wenn jemand sich anschickt, mit ganz gewöhnlichen Worten der Sprache dasjenige zu schildern, wofür die Sprache nicht geprägt ist, so wird er nicht unmittelbar aus den Erlebnissen der Seele heraus schildern können dasjenige, was nach der Rückschau erlebt wird, was der Geistesforscher außerhalb des Leibes erlebt. Und das ist, was ich eben mit den ungeschickten Ausdrücken belegen möchte : es ist nämlich kein Fühlen und Wollen, sondern etwas zwi­schen Fühlen und Wollen. Ich möchte es daher nennen : ein fühlendes Wollen - ein wollendes Fühlen.",
      "Man hat diese Seelenkraft gar nicht im gewöhnlichen Leben. Man kennt sie als Geistesforscher. Es ist, wie wenn der Wille mit uns sich dahinbewegte in der Welt, und dieser Wille auf seinen Flügeln oder seinen Fluten dasjenige trüge, was uns nun als Gefühl so entgegen­tritt, daß es wie außer uns west, heranspielt auf den Wogen des Willens. Während wir sonst gewohnt sind, unser Gefühl zu empfangen in der Seele wie etwas, was mit uns verwachsen ist, wird das, was wir jetzt als Gefühl haben, wie wogend und wellend auf den Wellen des Willens empfunden, und wir wissen dennoch, daß wir uns damit ausbreiten in die Welt, daß das, was da draußen ist als wollendes Fühlen, was da ist wie eine Tonwahrnehmung der äußeren Sinnes-welt, von unserem Wesen durchdrungen ist.",
      "Aber in der ersten Zeit nach der Rückschau erlebt dies der Mensch so, daß seine einzige Welt, die er jetzt zunächst wahrnimmt, im Grunde diejenige ist, aus der er mit dem Tode herausgegangen ist. Nachdem das Erinnerungstableau abgedämmert ist, erkraftet sich in der Seele dieses wollende Fühlen. Aber es drückt nur Dinge aus, die mit dem",
      "letzten Erdenleben noch zusammenhängen, so daß wir diese Dinge etwa wie folgt charakterisieren können : Das Erdenieben gibt dem Menschen niemals alles das in seine Erfahrungen herein, was es ihm geben könnte. Wir haben nicht alles genossen, was hätte genossen werden können zwischen Geburt und Tod. Es ist sozusagen zwischen den Zeilen des Lebens etwas von Begierden und Wünschen und Liebe zu anderen Menschen zurückgeblieben. Unbefriedigtes des letzten Lebens, das ist es, auf das wir begehrend geistig zurückblicken, und zwar dauert das jetzt durch Jahre. In diesen Jahren ist es so, daß wir unsere Welt hauptsächlich in dem haben, was wir gewesen sind. Wir schauen in unser letztes Erdensein. Wir schauen in ihm das, was un­erledigt geblieben ist. Und erst dadurch, daß wir in einer Sphäre leben, jahrelang, in der nichts befriedigt werden kann, was auf Erden befriedigt wird, weil wir keine Organe haben zu seiner Befriedigung, arbeiten wir uns heraus aus dem Zusammenhang mit dem letzten Erdenleben.",
      "Über die Länge dieser Zeit kann gesagt werden : Die Zeit, die der Mensch durchlebt in der ersten Kindheit bis zu dem Zeitpunkte, an den er sich zurückerinnern kann, die hat keinen Einfluß auf die Dauer der jetzt geschilderten Erlebnisse. Ebenso hat die Zeit, die nach dem 25., 26. Jahr weiter durchlebt wird, keinen Einfluß mehr. Die Zeit vom 4., 5. Jahre bis in die zwanziger Jahre hinein deutet die Länge an, in der man - so zusammenhängend mit seinem letzten Erdenleben -sich aus ihm herauszuziehen hat. Es stellt sich heraus für die geistige Beobachtung : So lange, als man brauchte, um seinen Leib gleichsam mit den aufwärtsstrebenden Kräften aufzubauen, also so lange, als man brauchte, um das Leben mit den körperlichen, organisch frucht­baren Kräften zu durchsetzen, ungefähr so lange dauert die Zeit, durch die man sich herausfinden muß aus dem letzten Erdenleben. So daß also, wenn ein Mensch zwölf Jahre alt stirbt, er etwa sieben Jahre braucht, um aus dem letzten Erdenleben herauszukommen. Stirbt er aber mit fünfzig Jahren, so tragen die Jahre nach der Mitte der zwanziger Jahre nichts mehr bei zur Verlängerung dieser jetzt genannten Periode.",
      "Von dieser Periode muß gesagt werden, daß dann schon in einer",
      "gewissen Weise folgendes eintritt : Der Mensch nimmt geistige Vor­gänge und Wesenheiten in seiner Umgebung wahr. Wenn der Geistesforscher in seinem Geistig-Seelischen sich erlebt, ist er in einer wirklich geistigen Welt darinnen. In diese Welt zieht der Tote ein, aber er ist so beschäftigt in der Weise, wie wir es vorher besprochen haben, daß er nur auf dem Umweg durch sein früheres Leben einen Zusammenhang gewinnen kann mit dem, was in seiner geistigen Um­gebung ist. Ich möchte ein Beispiel angeben: Jemand geht durch die Pforte des Todes. Er lebt in der Zeit des Sichherausfindens aus dem letzten Erdenleben. Ein Mensch, den er geliebt hat, ist noch im physi­schen Leibe. Derjenige nun, der noch in dem Stadium des jetzt be­sprochenen Erlebens nach dem Tode ist, kann nicht unmittelbar auf die im physischen Leibe lebende Seele schauen, aber es findet gleich­sam eine Art von Umschaltung statt: im letzten Erdenleben haben wir den Menschen geliebt. Auf diese Liebe nun blicken wir hin. Auf dem Umweg durch die Liebe können wir den Weg finden zu einer Seele, die noch auf der Erde ist. Ebenso müssen wir auch den Weg finden zu einer Seele, die in der geistigen Welt mit uns schon lebt.",
      "So kann man sagen : Der Mensch lebt mit der anderen Menschen­seele als Seele nach dem Tode, aber zunächst auf dem Umweg durch sein eigenes Leben. Doch immer mehr entwickelt sich im Menschen eine seelische Kraft, die wiederum nur der Geistesforscher kennt, wenn er sein Geistig-Seelisches erlebt. Für diese seelische Kraft ist nun schon gar kein Ausdruck mehr da. Für die vorher besprochene Kraft kann man wenigstens noch sagen «Wollendes Fühlen» : sie hat etwas Ähnlichkeit mit den Dingen, die da draußen in Wollungen und Fühlungen herumwogen. Das aber, was nun die Seele erlebt, was als eine Kraft in ihr erwacht, je mehr sie sich entfernt in der geschilderten Weise vom letzten Erdenleben, ich kann es nur bezeichnen mit einem wiederum ungeschickten Wort «Kreative seelische Kraft, Schöpfer­kraft». Es ist etwas, was die Seele jetzt unmittelbar erlebt : man muß in eine Aktivität übergehen. Das erlebt die Seele nach dem Tode völlig, aber sie erlebt zugleich, daß die Schöpferkraft wirklich aus-strahlt in die Umgebung. Wiederum - es ist ein ungeschickter Aus­druck, aber ich muß ihn anwenden - ist diese kreative Schöpferkraft",
      "wie etwas, was wie ein geistiges Licht ausstrahlt in die Umgebung, was die geistigen Vorgänge und Wesen beleuchtet, so daß wir sie sehen. Wie wir, wenn morgens die Sonne aufgeht, durch die Sonne die Gegenstände sehen, so sehen wir durch diese innere Leuchtekraft diese geistigen Vorgänge und geistigen Wesen.",
      "Jetzt tritt die Zeit ein, wo die Seele wirklich in einer geistigen Um­gebung ist, in dem Maße, in dem ihr die kreative Kraft erwacht, diese geistige Umgebung zu beleuchten. Und hier haben die Religio­nen keinen unbedeutsamen Ausdruck gebraucht : dieses Sichfühlen in der schöpferischen Kraft, dieses Sicheinleben in eine Welt, die dadurch sichtbar wird, daß man sein eigenes Licht hineinsendet, das ist ein Gefühl von Seligkeit. Selbst die Schmerzen werden so als Seligkeiten erlebt in dieser Welt. - So erlebt die Seele nun ihr weiteres Leben.",
      "Nun handelt es sich darum, daß die Seele in abwechselnden Zu­ständen dieses Erleben durchmachen kann, das eben beschrieben worden ist. Ich komme allerdings in Gebiete, die für ein gewöhnliches Denken ganz im Phantastischen schwimmen. Aber ich darf wohl diese Dinge sagen, denn klar wird es ja werden durch die weiteren Ausfüh­rungen. Die Seele erlebt Wechselzustände. Nicht immer ist sie in dem Zustand, daß sie gleichsam ihre geistige Leuchtekraft, ihre kreative Kraft seelisch ausstrahlt über die Umgebung, so daß geistige Wesenheiten, die um sie herum sind, von ihr erlebt werden, daß die Seele so in der äußeren geistigen Welt lebt, sondern dieser Zustand muß abwechseln mit einem anderen : mit dem, , daß die Seele gleichsam sich herabdämpfen fühlt dieses Ausstrahlen der Leuchtekraft. Die Seele wird innerlich stumpf, sie kann nicht mehr hinstrahlen ihr Licht, sie muß zusammennehmen in sich ihr ganzes Sein. Jetzt kommt dieser Moment heran, wo zwischen Tod und neuer Geburt die Seele ein völlig einsames Leben lebt. Wenn man es vergleichen will mit dem gewöhnlichen Leben, so kann man sagen : Wie im gewöhnlichen Leben wechseln Schlafen und Wachen, so muß abwechseln nach dem Tode ein Leben, das sich ausgießt in die äußere Welt, und ein Leben der innerlichen Einsamkeit, wo hereingenommen wird all das, was man früher im Zustand der Verbreiterung erlebt hat, aber wo die",
      "Seele weiß : Jetzt bist du einsam. - Die Seele wird nicht bewußtlos. Sie erlebt gerade dann ein gesteigertes Bewußtsein, aber sie erlebt : Da draußen ist die geistige Welt, du aber bist allein; alles, was du erlebst, erlebst du in dir. Und das sind nur die Nachklänge des außen Erlebten; nur dadurch kann die innere Leuchtekraft wieder erstarken. Dann wacht man wiederum auf und erlebt wiederum den anderen Zustand.",
      "Es gehört zu den merkwürdigsten Erlebnissen, wirklich einmal zu lernen, einen Sinn zu verbinden damit, daß für die Zeit zwischen dem Tode und einer neuen Geburt das Leben der Seele abwechseln muß in den Zuständen zwischen geselligem Erleben und Einsamkeit, und daß das für die Seele etwas Ähnliches bedeutet wie Schlafen und Wachen in der physischen Welt. Ich habe das eingehend geschildert in meiner Schrift «Die Schwelle der geistigen Welt».",
      "Aber die Seele erlebt so, indem sie weiterlebt zwischen dem Tod und einer neuen Geburt, allmählich ein Herabdämpfen, ein Verglimmen ihrer Leuchte­kraft. Man möchte sagen : Die Erlebnisse der inneren Einsamkeit werden immer stärker.",
      "Sie werden so, daß der Mensch innerlich einen ganzen Kosmos erlebt. Es überkommt ilul etwas wie das Gefühl der Furcht, wenn er entdeckt, was alles da drinnen in der Seele ist und was jetzt herauskommt in der Zeit zwischen dem Tod und einer neuen Geburt.",
      "Dann kommt die Zeit herauf, die ich versuchte darzu­stellen in meinem vierten Mysteriendrama «Der Seelen Erwachen», wo der Mensch nur noch vermag innerliche Erlebnisse zu haben, wo die Nächte der Einsamkeit immer länger und länger werden und der Mensch nicht mehr aufwachen kann zu den Zeiten, wo er seine Leuchtekraft ausstrahlen kann, die Zeit, die ich rnir zu nennen er­laubte : Die Mitternacht des geistigen Daseins zwischen Tod und neuer Geburt. Es ist die Zeit, wo der Mensch alles das, was in den Tiefen der Seele ist, als seine Welt erlebt, wo er nur weiß : Jenseits der Ufer deiner Seele sind die geistigen Welten, in denen alles das lebt, was an geistigen Wesen da ist, in der alle entkörperten und verkörperten Seelen sind. - Aber man weiß es nur, wenn man eben die Nachklänge in sich hat.",
      "Und jetzt entsteht etwas, was wieder nicht mit gewöhnlichen Worten",
      "ausgedrückt werden kann. Nicht wahr, die gewöhnliche Sprache hat das Wort «Sehnsucht» für das Passivstein der Seele. Wir wünschen etwas, wir begehren etwas, was wir nicht haben, aber die Sehnsucht kann es nicht hervorbringen.",
      "Wir können uns nur passiv verhalten. Doch diese Seelenkraft gewinnt einen anderen Charakter. Es bildet sich jetzt die Sehnsucht, wiederum in diese Welt hinein sich zu leben, aus der man in der Einsamkeit herausgerissen ist.",
      "Diese Sehnsucht ist aktiv, ist organisierend in ihren Kräften. Sie wird eine neue Wahr­nehmungskraft der Seele, etwas Reales. Sie gebiert wiederum eine neue Kraft, eine Seelenkraft, die eine äußere Welt wahrnehmen kann, eine Welt, die eine äußere Welt und eine innere zugleich ist.",
      "Wir nehmen sie außerhalb unseres Wesens wahr, und nehmen sie zugleich wahr als die Welt unserer früheren Erdenverkörperung. Das wird jetzt unsere Außenwelt. Wir schauen hin auf all das, was unerledigt geblieben ist in uns, und in uns schimmert die Sehnsucht, Ausgleich zu schaffen im folgenden Erdenieben für das, was man im früheren Erdenieben Böses getan hat, Ausgleich zu schaffen dafür in einem neuen Leben.",
      "Das ist die Zeit, in der jeder Mensch zurückblicken kann auf frühere Erdenleben. Das ist die Zeit, wo dem Menschen vor dem geistigen Auge stehen alle die Taten seiner früheren Leben. Und in ihm erwacht die Tendenz, in einem neuen Erdenieben solchen Ausgleich zu schaffen, daß die Erlebnisse im neuen Erdenleben aus­gleichen und gutmachen dasjenige, was in früheren Erdenleben ver­säumt worden ist.",
      "Ich habe schon Menschen kennengelernt, die sich nicht zur Geistes­wissenschaft bekennen konnten, weil sie, wie sie sagten, mit einem Erdenleben genug hatten. Ich habe auch einen Menschen kennen­gelernt, der etwas Vernünftiges darin fand, von der nächsten Eisen-bahnstation nichts zu wissen. Darauf kommt es nicht an, daß wir nur zurückblicken auf frühere Erdenleben, sondern vielinehr darauf kommt es an, daß jede Seele zurückblickt und zugleich die Tendenz in sich aufnimmt, ein neues Erdenleben zum Ausgleich zu erleben. Und man erlebt weiter, daß es Menschen gibt, denen man etwas schuldig wurde oder die einem etwas schuldig wurden : das tritt vor die Seele hin als Ergänzung, und es tritt die Tendenz auf, wieder zu",
      "leben mit diesem Menschen im Erdenleben. Dadurch werden Kräfte erzeugt, welche zur Erde tendieren. Gleiche Kräfte werden in den verschiedenen Menschen erweckt, und so kommt es zur Wiederbe­gegnung von Menschen, um das wieder auszugleichen, was sie ein­ander schuldig geworden sind in früheren Erdenleben.",
      "Dann erlebt man immer weiter und weiter dieses geistige Leben zwischen dem Tod und einer neuen Geburt. Immer mehr und mehr prägt sich ein die Tendenz zu einem neuemn Erdenleben. Es werden lebendige Tendenzen, und der Mensch schafit sich aus dem, was er so erfahren hat, das Urbild, das geistige Urbild des neuen Erdenlebens. Da schafit er nun selbst, indem die Zeit weiterrückt, was sich verbin­det mit der materiellen Substanz von Vater und Mutter, um in ein neues Erdenleben einzutreten. Und je nachdem diese Substanzen sein können, wird man hingezogen zu dem Verwandten. So daß man sagen kann : Die Wahlverwandtschaft zwischen den ererbten Eigenschaften und dem Urbilde - das entscheidet, zu welchem Elternpaar man sich hingezogen fühlt, in welches Leben man sich hineinfindet. Dadurch kommt der Mensch wiederum zur Erde zurück und vereinigt sich wiederum mit einem physischen, mit einem irdischen Leibe.",
      "Und die Geistesforschung kann nun sehen, was im Kinde auf so mysteriöse Weise sich herausbildet, indem von innen heraus die ausdrucksvolle Miene allmählich tritt, indem aus ungeschickten Be­wegungen geschickte Bewegungen werden, der Körper modernert wird. Es schaut der Geistesforscher dasjenige, was durch das Leben zwischen Tod und neuer Geburt hindurchgegangen ist und wie es sich da immer mehr und mehr mit dem Leibe verbindet. Das schaut der Geistesforscher. Nun sieht er auch ein, warum zunächst keine Erinnerungen an diese Erlebnisse vorhanden sein können : die Kräfte, welche Erinnerungskräfte werden könnten, die werden aufgebraucht, um den Leib zu organisieren. Das Kind hat die Kräfte, sich zu erinnern an alles Frühere, aber die Kräfte werden umgewan­delt. Ebenso wie die Druckkräfte, die ich entwickele, wenn ich über den Tisch fahre mit dem Finger, sich in Wärme verwandeln, so ver­wandelt sich die Erinnerungskraft in organische Kraft. Was das Ge­hirn plastisch macht, das ist umgewandelte rückschauende Kraft, das",
      "verschwindet in dieser Gestalt, in der es die Rückschau entwickeln kann, und organisiert den Leib durch. Es ist das umgewandelte Seelische. Es ist hereingeflossen in den Leib, es wirkt im Leibe darinnen.",
      "So begreifen wir das Leben, in dem wir gerade stehen, wenn wir das Leben verstehen, das vorher, das vor der letzten Geburt liegt. Dieses jetzige Leben, es hat sich seine Kräfte angeeignet zwischen dem letzten Tode und der Geburt. Die Kräfte, die da geistig zutage treten, sind die Erinnerungskräfte, die sich umgewandelt haben, die den Leib durchorganisiert haben. Gewisse niedere Tiere sterben zu­gleich, indem sie reif werden zur Hervorbringung eines anderen Lebens. Das, was der Mensch an Kräften entwickeln muß, um phy­sische Nachkommen zu haben, das muß mit seiner Geschlechtsreife abgeschlossen sein; das kann ich nur andeuten. Die Naturforschung wird einmal darauf kommen , wie die Kräfte, die in der Vererbung liegen, etwas wie eine Erschöpfung erfahren. Darüber wird die Natur­wissenschaft und die Geisteswissenschaft zusammen wichtige Auf­schlüsse geben können.",
      "Aber darinnen wirken geistige Kräfte, und diese geistigen Kräfte sind es, die sich so betätigen, daß sie diesen physischen Leib durch­dringen. Der physische Leib ist gleichsam die Spiegelung des Geisti­gen, und im Grunde genommen sind es eigentlich Zerstörungspro­zesse, die die Spiegelung herbeiführen. Wenn wir Erinnerungsvor­stellungen bilden, wenn wir im Auge Farben sehen, so ist das ein Zerstörungsprozeß. Im Schlafe wird wieder aufgebaut.",
      "So leben wir, indem wir unseren Leib durchdringen und durch­kraften mit den Kräften, die wir außerhalb des Leibes erwerben. Und das Leben läßt sich nur begreifen, wenn wir dieses im Leben tätige Geistig-Seelische ins Auge fassen. Geisteswissenschaft hat es ja nicht so gut, daß sie vom Tod der Pflanzen und Tiere spricht wie vom Tode des Menschen, und das, was ich sagte, das gilt nur für den Menschen.",
      "Auf diese Weise erweitert die Geistesforschung den Blick über das hinaus, was zwischen Geburt und Tod liegt. Ja, auch Einzelheiten werden durch die Geistesforschung erklärbar. Ich kann mir sehr gut denken, daß diejenigen der verehrten Zuhörer, welche etwas übrig haben für diese Geistesforschung, gerne etwas einzelnes hören wollen.",
      "Aber ich kann ja nur einzelne Beispiele anführen. Ein Beispiel, das wie ein rechtes Mysterium des Lebens erscheint, sei hier angeführt : das Dasein der Verbrechernaturen. Der Geistesforscher steht durch­aus nicht etwa auf dem Standpunkte der Utopisten, als wenn die Ver­brecher nicht bestraft werden sollten und so weiter, aber verstehen dasjenige, was im Menschenleben uns entgegentritt, das will der Geistesforscher. Da fragen wir uns : wie liegt es denn mit einem Leben, das sich verbrecherisch offenbart? Nun, leicht sind die Dinge gesagt, aber die Antworten auf solche Fragen muß sich der Geistesforscher erst abringen. Und abringen muß er sich, darüber zu sprechen, weil dasjenige, was er zu sagen hat, gar so paradox erscheint.",
      "Wenn der Verbrecher hellseherisch angeschaut wird, so stellt sich heraus, daß verbrecherische Naturen eine Art geistiger Frühgeburten sind. Es gibt für jede Seele eine Möglichkeit, herunterzukommen in die physische Welt, die gewissermaßen die normale ist.",
      "Aber die Tendenz, die dazu hinführt, die kreuzt sich mit anderen Tendenzen, so daß die meisten Menschen - aber die Verbrecher besonders stark -viel früher ins Erdenleben heruntergehen, als es normalerweise ge­schehen sollte. Und das hat etwas anderes im Gefolge.",
      "So richtig sich durchdringen mit der ganzen Leiblichkeit, so daß man als Vollmensch dasteht, das kann man nur, wenn man sich annähernd zu dem nor­malen Zeitpunkte wieder verkörpert. Aber wenn Gründe vorhanden sind, durch die besonderen Umstände früherer Erdenieben früher herunterzukommen, so nimmt man etwas auf im Unterbewußtsein, wovon man nichts weiß, was in den Tiefen der Seele lebt, etwas, was wie ein Leichtnehmen des Erdenlebens ist, weil man nicht zu dem Zeitpunkte herunterkommt, wo man sich völbg mit dem Erdenieben hätte verbinden können.",
      "Das wird eine innere Seelenstimmung, dieses das Leben-nicht-voll-Nehmen. So kann es sein, daß man im gewöhn­lichen Oberbewußtsein einen starken Selbsterhaltungstrieb hat, den stärksten Egoismus entfaltet im Verbrechertum, und dennoch in seiner inneren Natur, die man nicht kennt, ein gewisses Oberflächlich-nehmen, ein Leichtnehmen des Lebens hat, keinen Wert legen will auf dieses Leben, in das man hineingekommen ist durch eine geistige Frühgeburt.",
      "Wenn das so ist, dann tritt dieses Leben auch so ins",
      "Dasein, daß der Mensch den überhandtiehmenden Selbsterhaltungs­trieb anfeuern kann durch dasjenige, was er nicht kennt. Das Leicht-nehmen des Lebens : das ist es bei den Verbrecherseelen. Erst als ich dies wußte, wurde mir ein anderes klar : Es gibt Lexika der Verbre­chersprache. Man versteht die eigentümliche Art der Verbrechersprache - dieses in den Worten Leichtnehmen des Lebens -, man ver­steht sie erst, wenn man das kennt, was jetzt angedeutet worden ist. In der Gesamtheit der menschlichen Erdenleben gleicht sich dies aber wieder aus, so daß der Verbrecher dasjenige, was er als die Folge des Zu-früh-geboren-Werdens in einem Erdenleben tut, in anderen Erdenleben wieder ausgleicht.",
      "Aber auch anderes wird verständlich durch die Geistesforschung. Da sehen wir Menschen, welche durch ein Unglück hinweggerafft werden, die Erde verlassen durch ein Unglück in einer Zeit, in welcher sie die Erde noch nicht verlassen sollten. Wenn zum Beispiel ein Mensch in seinem 35. Jahre von einer Lokomotive überfahren wird, stecken in seinem Leibe Kräfte, die lange noch wirken könnten. Indem er nun hinausgeht aus der physischen Welt, gehen diese Kräfte nicht in ein Nichts über; die intellektuellen Kräfte verstärken sich merk­würdigerweise gerade durch solche Dinge. Ein Mensch, der so durch ein Unglück umkommt, kann mit starkem Intellekt wieder geboren werden. Geistesforschung, indem sie das Leben von einem großen Horizont aus anblickt, muß über manches anders reden, als man im gewöhnlichen Leben redet. Jemand, der durch eine Krankheit stirbt, der vieles durchinacht durch diese Krankheit, der bereitet seine Seele so, daß seine Willenskräfte verstärkt werden können. Frühzeitiges Sterben durch Krankheit verstärkt die Willens kräfte.",
      "Manches von dem Gesagten mag schon wie reine Phantastereien er­scheinen, aber ich bin mir auch bewußt, daß ich eine gewisse Verantwor­tung habe, wenn ich diese Dinge bespreche, und ich weiß, daß ich dies nicht tun würde, wenn ich nicht wüßte, daß diese Dinge genau gewußt werden müssen, ebenso genau wie die Dinge der äußeren Wissenschaft. Ich würde es als größte Frivolität empfinden, wenn solche Dinge be­sprochen werden, ohne daß in der Seele ein Wissen lebt, das von einer solchen Stimmung durchdrungen ist, wie ich es eben angedeutet habe.",
      "So wird das Leben des Menschen gerade verständlich durch das­jenige, was außerhalb des physischen Lebens liegt. So wie sich das Leben hier zwischen Geburt und Tod entwickelt, so ist es ein Ergeb-nis des Lebens jenseits von Geburt und Tod.",
      "Für manchen mag das wie eine Entwertung des Lebens erscheinen. Damit es nicht so er­scheine, möchte ich hier schon Ausgesprochenes kurz wiederholen. Wenn jemand sagt : Ja, da werden wir darauf aufmerksam gemacht, daß wir das , was wir in einem Erdenieben erleben, uns selbst zubereitet haben! - Wahr ist es.",
      "Wir erleben ein Unglück, weil wir vor der Geburt die Tendenz in unsere Seele eingepflanzt haben, in dieses Unglück einzumünden. So wie die eine Pflanze nur im Hochgebirge leben kann, so sucht die Menschenseele sich ihre Umgebung auf, sie wächst hinein in das Schicksal.",
      "Wie das Schicksal selbstverständlich ist, in den Alpen zu leben für jene Pflanze, so ist es selbstverständlich für die Menschen-seele, sich ins Unglück zu stürzen, weil sie weiß : dadurch kann sie ausgleichen etwas Unvollkommenes aus den früheren Erdenleben. Wenn jemand sagt : So werden wir also zu Schmieden unseres eigenen Unglückes gemacht, und wir sollen nicht nur unser Unglück ertragen und erdulden, sondern wir haben es überirdisch verdient; das kann uns kein Trost sein, - so muß demgegenüber gesagt werden, was ich durch einen Vergleich klarmachen möchte : Nehmen wir an, ein Mensch, dessen Vater sehr reich ist, der im Überfluß lebt ohne etwas gelernt zu haben, erlebt, als junger Mensch von 18 Jahren, den Bankerott des Vaters.",
      "Dann kann es ein großes Unglück für ihn sein, wenn das Leben ihn hart anläßt. Er hat recht, sich im Leben jetzt unglücklich zu fühlen. Aber im 50. Jahr seines Lebens sieht er von einem anderen Gesichtspunkte sein Unglück vom i 8.",
      "Jahr an. Er sagt sich : wenn das Unglück dazumal nicht gekommen wäre, wäre ich vielleicht längst untergegangen, denn ohne dieses Unglück wäre ich niemals ein tüchtiger Mensch im Leben geworden; es war für mich ein Entwickelungsferment meines Lebens. - So sind wir nicht immer in der Lage, in dem Zeitpunkt des Erlebens den richtigen Gesichtspunkt zu finden gegenüber dem, was wir erleben.",
      "Wir stehen in der geistigen Welt auf einem ganz anderen Gesichtspunkt. Wir wissen da, daß das erlebt werden muß im neuen Leben, was Ausgleich",
      "schaffen kann für ein früheres Leben. Da bereiten wir uns selber das Leben, über das wir mit einem gewissen Recht dann klagen, wenn wir es nachher nur vom physischen Standpunkte aus betrachten können.",
      "Ein Weniges möchte ich noch sagen über die Zeit, die verfließt zwischen dem Tode und einer neuen Geburt. Der Geistesforscher muß sich zunächst fragen : Was ist es denn in deiner Seele, was dir, wenn du außer dem Leibe dich seelisch-geistig erlebst, so erscheint, daß es in der Seele ist wie etwas, was von ihr durch den Tod getragen werden kann? - Da erlebt man, daß man aus dem Leibe heraus in das Leben, das außer dem Leibe erlebt wird, seine Überwindungen mit­nimmt. Dasjenige nimmt man mit, was man sich eigentlich erst an­eignen kann nach den zwanziger Jahren. Man wird das heute nicht gerne hören, weil die Leute heute vor den zwanziger Jahren schon für reif gehalten werden wollen. Das kann man ja sehen in den Zeitungen : über und unter dem Strich schreiben oft junge Leute, die noch nicht das 20. Jahr erreicht haben. Aber in Wahrheit ist es doch so: Was wir so recht durch uns selbst in unserer Seele erleben, so daß es wirkliche aufgespeicherte Lebensweisheit wird - das erleben wir dadurch, daß man schon etwas erfahren haben muß, gleichsam eine innerliche Sporenarbeit beim Aufwärtssteigen. Dieses innerliche Auf­wärtssteigen ist dasjenige, was schon ein Vorkeim ist zu dem, was die Seele durchlebt zwischen dem Tod und einer neuen Geburt. Und so muß im fortwährenden Überwinden, im Umwandeln von Kräften die Seele leben. Normalerweise bleibt die Seele so lange in der Zeit zwischen dem Tod und einer neuen Geburt, als sie etwas umzuwandeln hat.",
      "Von anderer Seite betrachtet wäre folgendes zu sagen. Indem wir durch den Tod gegangen sind, haben wir den Seelenschatz gebildet, der mit durch den Tod geht. Aber die Erde verändert sich. Denken Sie zurück, wie die Gegend, wo jetzt Wien steht, sich verändert hat. Das Kulturantlitz der Erde verändert sich, es verändert sich der geistige Inhalt unserer Umgebung, aus dem wir unsere Erinnerungen, unseren Erinnerungsschatz nehmen. Die Seele kommt nun normaler­weise nicht früher zurück, bis sie in eine vollständig neue Umgebung treten kann. Nicht ohne Sinn ist es, daß die Seele wieder geboren",
      "wird, so daß sie in einem neuen Erdenleben Neues erleben kann. Dazu muß sie aber alles andere, was sie aus früheren Erdenleben hereingebracht hat, umwandeln. Zum Beispiel muß sie eine andere Sprache lernen und so weiter. Das unifaßt eine Zeit von Jahrtausenden, von ein bis andertlialb Jahrtausend. Aber es können, wie gesagt, geistige Frühgeburten entstehen. Ich kann mich bei der Kürze der Zeit mit der Ausmalung der Verhältnisse, die mit dem Thema zusam­menhängen, nicht weiter befassen, ich kann nur noch sagen, wer da meint : Ja, das ist ja alles wirklich nicht zu glauben. Wie soll denn der Mensch darüber etwas wissen können? - der sei darauf aufmerk­sam gemacht, daß in der Tat spätere Selbstverständlichkeiten, Er­kenntnisse, die in alle Seelen eingedrungen sind, zuerst der Erden-kultur als paradox erschienen sind, wenn sie mitgeteilt wurden. Und derjenige, der heute Geisteswissenschaft pflegen will, der muß sich schon bekannt machen damit, wie begreiflich es ist, daß vielfach noch als Phantastereien aufgenommen wird dasjenige, was er zu sagen hat. Wie einstmals die Kopernikanische Weltanschauung sich eingebürgert hat, nachdem sie zuerst als etwas Schädliches angesehen wurde, so wird auch aufgenommen werden dasjenige, was Geisteswissenschaft der Welt zu geben hat.",
      "Noch einmal sei auf das Bild aufmerksam gemacht, das sich vor den Geistesforscher hinstellt, ihm das starke Bewußtsein zu geben von der Wahrheit, die sich allmählich durchringen wird, auch durch die engsten Felsenspalten der Kultur. Sie wird sich durchdrücken. Er-starken wird man in dem Bewußtsein daran, wenn man auf solche Individualitäten wie Giordano Bruno hinblickt. Er trat vor die Mensch­heit so, daß er jahrhundertealte Vorurteile zerstörte, indem er sagte :",
      "Wenn ihr hinaufschaut in den weiten Raum, erscheint es euch so, als ob die Sonne um die Erde kreise, die Planeten um die Erde kreisten, als ob das blaue Himmelsgewölbe eine Wand sei, eine blaue Wand! -Damals konnte Giordano Bruno auftreten und sagen : Diese blaue Wand erscheint euch nur deshalb, weil euer eigenes Erkenntnisver­mögen, euer Wahrnehmungsvermögen nur bis dahin reicht. Aber die Unendlichkeit des Raumes breitet sich aus da, wo eure beschränkten Sinne eine Wand sehen, und sie ist erfüllt von unendlichen Welten.",
      "Heute muß der Geistesforscher dieser Erweiterung des mensch­lichen Blickes in die Unendlichkeiten des Raumes gedenken, daran denken, wie Giordano Bruno zuerst aufmerksam machte darauf, daß die Grenze des Firmamentes nur von der Beschränktheit des mensch­lichen Wahrnehmungsvermögens selbst gemacht ist. Denn er muß hinweisen darauf, daß das auch für die Zeit des Menschenlebens gilt, die zwischen Geburt und Tod liegt. Indem man mit den physischen Wahrnehmungsorganen sie ansieht, sieht man auch diese Grenze von Geburt und Tod. Wie man einst die Grenze sah da oben am blauen Himmeisgewölbe, die Grenze des Raumes, so ist auch die Zeitgrenze nur hingesetzt, und jenseits breitet sich auch aus die zeitliche Un­endlichkeit, und in diese zeitliche Unendlichkeit sind eingebettet die nach rückwärts und vorwärts verlaufenden Erdenleben. Das kann noch gesagt werden - ich kann das allerdings jetzt nicht näher aus­führen -, daß die ganzen Wiederholungen einmal einen Anfang nahmen dazumal, als die Erde selbst entstand. Und einmal wird der Mensch wieder in ein anderes, in ein vergeistigteres Erdenleben ein­treten.",
      "Wenn man sich auch in der Gegenwart in der angedeuteten Weise mit diesen Erkenntnissen auseinanderzusetzen hat, so muß man dennoch sagen : In den Ahnungen derjenigen, die die Führer der Menschheit waren, lebten diese Erkenntnisse. Man findet in den Ahnungen der führenden Geister der Menschheit vielfach dasjenige, was in der Geisteswissenschaft heute wiederum auflebt. Geistes­wissenschaft, wie sie hier gemeint ist, haben die Menschen nicht ge­habt, denn sie ist ein Kind unserer Zeit und wird aus der Bildung unserer Zeit entstehen. Aber denen, die sich in ihrer Seele verbunden wußten mit dem Geiste des Alls, denen drückt sich in die Worte hinein dasjenige, wozu die Geisteswissenschaft im vollen Sinne Ja sagen kann. Geisteswissenschaft zeigt uns, wie wir das Leben zwischen Geburt und Tod verstehen, indem wir in diesem physischen Leibe , in dem ganzen physischen Leben wirkend und webend dasjenige sehen, was unsterblich ist und in einer geistigen Welt leben kann. Geisteswissenschaft zeigt uns, daß wir das Leben im Leibe haben durch das Leben außer dem Leibe, so daß niemand das Leben im",
      "Leibe verstehen kann, der nicht das Leben außerhalb dieses geistigen Firmamentes versteht. Das drückte Goethe mit Worten aus, ahnend die späteren Erkenntnisse der Geisteswissenschaft, mit Worten, die nicht nur Goethes Bekenntnis zu einem unsterblichen Leben dar­stellen, sondern die auch ausdrücken, daß er wußte, daß der wirkliche Wert des Erkennens des gegenwärtigen Lebens im Erleben des Da­seins davon abhängt, daß man dieses irdische Dasein durchleuchtet weiß von dem, was überirdisch ist, was unsterblich ist. Deshalb sei gerade diese Erkenntnis der Geisteswissenschaft, daß die wahre innere Wesenheit des Sterblichen in einem Unsterblichen begründet ist, kurz zusammengefaßt in die Worte, in denen Goethe seine Anschau­ung ausdrückte. Denen gegenüber, die sich gar nicht wollen aus der eigentümlichen Wesenheit des gegenwärtigen Lebens eine Anschau­ung bilden über ein anderes Leben, denen gegenüber : «möchte ich sagen» - das sind die Worte Goethes - «mit Lorenzo von Medici, daß alle diejenigen auch für dieses Leben tot sind, die kein anderes er­hoffen.»"
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Wenn es schon in einer gewissen Beziehung schwierig ist, sich über die Grundlage der Geisteswissenschaft, wie sie hier gemeint ist, so auseinanderzusetzen, wie es im Vortrag von vorgestern geschehen ist, so darf wohl gesagt werden, daß die Mitteilungen in bezug auf die­jenigen Forschungsergebnisse, die den Gegenstand des heutigen Vor­trages bilden sollen, in gewisser Beziehung eigentlich ein Wagnis sind gegenüber den Vorstellungsarten und Denkgewohnheiten der Ge­genwart.",
        "Denn wird man in dem, was der Vortrag von vorgestern ausdrückte, schon manches paradox finden müssen von diesen Vor­stellungsarten und Denkgewohnheiten aus, so wird man von einem solchen Gesichtspunkte aus ganz gewiß und begreiflicherweise es nicht leicht haben, in dem, was heute zu sagen ist, ernstes Forschen zu sehen."
      ],
      [
        "Man wird viel eher in weiten Kreisen der Gegenwart geneigt sein, darinnen nur die Schwärmereien eines sonderbaren Phantasten zu sehen.",
        "Dessen muß man sich wohl bewußt sein, wenn man über diese Dinge redet, bewußt sein dessen, daß alles dasjenige, was in einer späteren Zeit in das allgemeine Bewußtsein übergeht, vieles sogar von dem, was dann später ein Selbstverständliches wird, in der Zeit, in der es zuerst auftritt, etwas Paradoxes, etwas Phantastisches ist."
      ],
      [
        "Dieses möchte ich nur vorausschicken, um zu charakterisieren, wie sehr der Geistesforscher sich dessen bewußt ist, was alles begreif­licherweise empfunden werden kann, wenn er seine für die heutige Zeit durchaus noch paradox erscheinenden Forschungsresultate mit­zuteilen sich gestattet."
      ],
      [
        "Bevor ich auf diese Forschungsergebnisse zu sprechen komme, möchte ich in ein paar einleitenden Worten die Grundstimmung der Seele des Geistesforschers charakterisieren.",
        "Diese Grundstimmung ist ja eine ganz andere als die Stimmung gegenüber einem andern Forschungsfelde.",
        "Während man dem äußeren Leben und seinen Erkenntnissen"
      ],
      [
        "gegenüber und auch der gewöhnlichen Wissenschaft gegenüber heute mit einem gewissen Recht das Gefühl hat, man habe die Erkenntniskräfte in sich, man brauche sie nur sozusagen in Wirk­samkeit überzuführen, dann könne man urteilen über all dasjenige, was die Natur selbst und der Forscher aus der Natur darbietet, während man bei dieser Forschung alle Mühe darauf verwendet, um eben zu forschen, um eben die Dinge zu beobachten und durch den Verstand ihre Gesetze zu erkennen, ist die Stimmung des Geistes­forschers gegenüber der Wahrheit, gegenüber allem Erkenntnis­streben doch eine ganze andere.",
        "Da bekommt man, indem man sich in diese Geistesforschung hineinarbeitet, immer mehr das Bedürfnis, alle Arbeit der Seele, all ihr Streben zunächst auf die Vorbereitung zu verwenden und man bekommt immer mehr und mehr das Gefühl : wenn man sich irgendeiner Wahrheit aus diesem oder jenem Gebiet nähern will, so möchte man eigentlich immer noch warten, immer weiter und weiter sich vorbereiten, weil man das Bewußtsein hat : je mehr Mühe und Arbeit auf jenen Weg verwendet wird, bevor man forscht, desto mehr macht man sich reif, die Wahrheit zu empfangen."
      ],
      [
        "Denn ein Empfangen der Wahrheit, das ist es, um was es sich bei der eigentlichen Geisteswissenschaft handelt.",
        "Und so stark kommt diese Stimmung über die Seele, daß man eine heilige Scheu empfindet, die Dinge an sich herankommen zu lassen, und immer wiederum gegen­über wichtigen, wesentlichen Ergebnissen der Geistesforschung lieber wartet, als die Dinge zu früh in das Bewußtsein hineinkommen zu lassen."
      ],
      [
        "Das bedingt eine ganz besondere Stimmung in dem Geistesforscher selbst, jene Stimmung, die all die Arbeit, von der vorgestern als einer inneren Seelenarbeit in Übungen gesprochen worden ist, allmählich durchdringt : eben die Stimmung von heillget Scheu gegenüber der Wahrheit.",
        "Nachdem ich dies vorausgeschickt habe, möchte ich nun unbefangen auf dasjenige eingehen, was über das wichtige, bedeutungsvolle, jeder Seele so naheliegende Thema des heutigen Abends zu sagen sein wird."
      ],
      [
        "Gewiß, es sind nicht die schlechtesten Gemüter unserer Gegenwart, die noch immer festhalten an der Meinung, daß die Wahrheiten des Glaubens besondere seien, und die Wahrheiten des Wissens auch besondere"
      ],
      [
        "seien, und die da glauben, daß all dasjenige, was der Mensch sich vorstellen kann als über Geburt und Tod hinausgehend, nur ein Gegenstand des Glaubens und nicht streng beweisbare Wissenschaft sei.",
        "Gerade diese strenge Trennung zwischen Glauben und Wissen, sie wird durch die Geisteswissenschaft aufgehoben werden."
      ],
      [
        "Und man fühlt sich doch im Einklang mit dem, was längst hinein wollte in das moderne Geistesstreben, wenn man die Wahrheiten, die jenseits des Todes liegen, in dem Sinne entwickelt, wie es hier geschehen soll, wenn man sich immer wieder so etwas vor Augen hält, wie zum Bei­spiel der große Lessing mit einer der Hauptwahrheiten dieser Geistes-forschung sich doch auseinandersetzte in jener Schrift, die er wie sein geistiges Testament kurz vor dem Tode als reife Frucht seines Denkens und Sinnens verfaßt hat : «Die Erziehung des Menschen­geschlechts».",
        "Und es scheut Lessing nicht zurück zu sagen, daß die Anschauung von den wiederholten Erdenleben nicht deshalb ein Irrtum zu sein braucht, weil sie auftrat gleichsam als etwas Erstes, worauf das Menschengeschlecht kam, bevor noch die Vorurteile der Schule und Philosophie etwas wie einen trüben Schleier gebreitet haben über das, was die Menschheit im Beginne der Kulturentwicke­lung vom Jenseits des Todes wußte."
      ],
      [
        "So fühlt man sich gerade auf dem Boden der Geisteswissenschaft in Einklang - es könnten noch viele Geister angeführt werden - mit den besten Persönlichkeiten, die ihr Streben einfügten in die Kulturentwickelung der Menschheit."
      ],
      [
        "Gesagt worden ist vorgestern, daß die Dinge des geistigen Lebens, die Vorgänge des geistigen Lebens nur erforscht werden können dann, wenn wirklich der Mensch durch das vorgestern Geschilderte dazu kommt, in seiner Seele die in ihr schlummernden Fähigkeiten so zu erkraften, daß diese Seele die Möglichkeit findet, durch die geisti­gen Übungen sich herauszuziehen aus dem Physisch-Leiblichen und sich abgesondert von dem Physisch-Leiblichen zu erleben, so daß der Mensch dann einen Sinn verbinden kann mit den Worten : Ich erlebe mich als seelisch-geistiges Wesen außerhalb meines Leibes, und mein Leib mit alledem, was zu ihm gehört in der Sinneswelt, steht vor mir, wie em außerer Gegenstand vor uns steht in der Sinneswelt. - Und schon als ich das letzte Mal hier einige öffentliche Vorträge halten"
      ],
      [
        "durfte, konnte ich aufmerksam machen auf den bedeutungsvollen Augenblick, der im Leben des Geistesforschers dann eintritt, wenn wirklich dieser Geistesforscher durch die vorgestern erwähnten Übungen, die Sie näher beschrieben finden in «Wie erlangt man Er­kenntnisse der höheren Welten?» und «Geheimwissenschaft» - hier soll nur hingewiesen werden auf diese Momente - reif geworden ist.",
        "Dann kommt eines Tages - man könnte auch sagen eines Nachts -dieses Ereignis."
      ],
      [
        "Es kann eintreten mitten in den gewöhnlichen Vor­gängen des Tages, mitten in der Nacht, und wird, wenn in der richtigen Weise vorbereitet, weder das eine noch das andere stören.",
        "In hundert­facher Weise kann es auftreten, ich möchte nur den typischen Charak­ter schildern, der immer ähnlich sein wird dem, was ich jetzt anführen werde."
      ],
      [
        "Da kommt es so, daß der Mensch, wenn er aufwacht aus dem Schlafe, weiß : es geht etwas vor, was kein Traum ist.",
        "Er ist entrückt allem, was ihn mit dem Tag verbindet.",
        "Oder mitten in den Tagesereignissen tritt ein Moment ein, wo etwas ganz anderes in das Vor­stellen, das Bewußtsein hereintritt."
      ],
      [
        "Das kann dann so sein - es wird immer ähnlich sein dem, was ich jetzt möglichst konkret schildern will -, dies erschütternde Ereignis, daß man das Gefühl hat : Du bist jetzt wie in einem Haus, in das der Blitz eingeschlagen hat.",
        "Deine Umgebung löst sich auf wie ein Haus, in das der Blitz geschlagen, und der Blitz geht durch dich durch."
      ],
      [
        "Man fühlt alles, womit man verbunden ist, wie durch die Elemente aus einem herausgelöst.",
        "Es ist der denkbar tieferschütterndste Eindruck.",
        "Von diesem Momente an oder einem ähnlichen weiß man, was es heißt : außer seinem Leibe in der Seele sich selbst zu erleben."
      ],
      [
        "Und die Geistesforscher aller Zeiten, sie haben einen Ausdruck gebraucht für dieses Erlebnis, der volitreffend er­scheint demjenigen, der das Erlebnis kennt.",
        "Denn es hat zu allen Zeiten, wie es die verschiedenen Kulturen bedingten, eine Art von Geistesforschung gegeben."
      ],
      [
        "Die heutige ist angemessen den Fort­schritten der modernen Naturwissenschaft.",
        "Aber das, was durch sie erreicht wird, wurde auch erreicht durch die Methoden, die durch die verschiedenen Kulturen möglich waren."
      ],
      [
        "So haben die Geistesforscher der verschiedenen Zeiten die Worte geprägt : Man sei als Mensch angekommen an der Pforte des Todes. - Und tatsächlich, was"
      ],
      [
        "man sich zunächst vorstellen kann als erlebbar durch den Tod, es tritt ein nicht unmittelbar als eine Wirklichkeit, denn der Geistes­forscher tritt ja wieder in seinen Leib zurück; alles das aber, was er erlebt, das ist das Bild von demjenigen, was sich wirklich zuträgt, wenn der Mensch durch die Pforte des Todes schreitet, wenn das äußere physische Leben aufhört und das Leben nach dem Tode beginnt.",
        "Will man nun verstehen, wie der Geistesforscher zu den Dingen kommt, von denen hier die Rede ist, so muß man sich eben vergegenwärtigen, daß er durch sorgfältige Vorbereitung seiner Seele dazu kommt, ganz anders wahrzunehmen als mit den äußeren Sinnen, daß er wirklich hineinschauen kann in diejenigen Sphären des Daseins, von denen gesprochen werden soll."
      ],
      [
        "Das erste, wozu der Geistesforscher kommt, wenn er einen solchen Moment überwunden hat, bei dem man an der Pforte des Todes steht, könnte man nennen : man gelangt jenseits des menschlichen Gedächtnisses.",
        "Die menschliche Gedächtnis- und Erinnerungskraft ist etwas, was gewissermaßen in unserer Seele lebt als der Anfang, möchte man sagen, von einem Geistigen.",
        "Das sehen heute selbst schon äußere philosophische Forscher ein.",
        "Der zu so glänzendem Erfolg gekommene französische Forscher Bergson sieht schon in dem Gedächtnis des Menschen, in dem Behalten der Erinnerungen etwas rein Geistiges.",
        "Und wenn erst die Vorurteile der Naturwissenschaft, die heute noch fast an jedem haften, vorüber sein werden, dann wird man einsehen, wie in dem Schatz unseres Gedächtnisses für die Men­schenseele schon etwas vorliegt, was der Anfang ist zu einem Über­gang zum rein Geistig-Seelischen.",
        "Indem wir unsere Vorstellungen zurückschieben in das Gedächntis, bewahren wir sie rein in der Seele auf, nicht durch äußere Vorstellungen.",
        "Die naturwissenschaftliche Rechtfertigung dessen, was eben gesagt wurde, würde im Augenblick zuviel Zeit in Anspruch nehmen."
      ],
      [
        "So nun, wie man im gewöhnlichen Leben Erinnerungsbilder wahr­nimmt, die aus dem Schatze unserer Seele heraufkommen, die so, wie sie auftreten, nichts haben, was uns verleiten könnte, sie etwa zu einer Halluzination zu machen, so treten - aber jetzt nicht aus den Seelen-schätzen herauf, sondern aus geistigen Welten heraus - vor die Seele"
      ],
      [
        "des Geistesforschers die geistigen Vorgänge und Tatsachen.",
        "Und man merkt dann, daß hinter dem, was wir den Gedächtnisschatz nennen, die menschliche Seele noch etwas anderes erleben kann.",
        "Der Geistes­forscher sieht da gleichsam das Folgende : nun bist du aus dem Leibe mit der Seele herausgezogen."
      ],
      [
        "Nun kannst du erst recht überblicken dasjenige, was du dir durch die Sinnenwelt erworben hast, den Schatz des Gedächtnisses, der aber durch einen Schleier zudeckt dasjenige, was immer in der Seele ist, was aber zugedeckt wird durch das Ge­dächtnis. - Ja, in diesen menschlichen Seelentiefen ist etwas unten, das immer in ihnen lebt, aber indem der Mensch seine Erinnerungen ausbreitet in seiner Seele, deckt er das unterbewußte Geistig-Seelische zu.",
        "Indem der Geistesforscher sich ins Geistig-Seelische erhebt, hat er allerdings, man möchte sagen, wie einen Kometenschweif seines geistig-seelischen Wesens seine Erinnerungen anhängen, aber er kann durch sie hindurchschauen auf etwas, was man nennen könnte : Kräfte höherer Art, als die Kräfte sind, die unsere Erinnerungen aufbewahren."
      ],
      [
        "Wenn der Ausdruck nicht so verpönt wäre - aber es ist ja schwierig, die richtigen Ausdrücke zu finden -, so würde ich sagen : Man steigt von dem Gedächtnis zu einem Übergedächtnis auf.",
        "Man kommt in das allmählich hinein, was vorgestern imaginatives Vorstellen genannt worden ist."
      ],
      [
        "Während man bei dem Gedächtnis immer das Gefühl hat : die Bilder steigen herauf, sie stellen sich vor dich hin, indem du passiv bist, - taucht man nun unter in die Dinge und muß aktiv darinnen sein.",
        "Man muß dasjenige mit hervorbringen, was als Inhalt eines Übergedächmisses heraufstrebt."
      ],
      [
        "Aber man weiß auch, daß dasjenige, was sich da etitdeckt, was sich da offenbart als hinter dem Gedächtnis Liegendes, immer da war, daß es nur zugedeckt war durch das Ge­dächtnis.",
        "Und man weiß, daß dies, was sich da hinunterschiebt, selbst etwas ist, was nun an unserem physischen Organismus arbeitet, was tätig ist an demselben."
      ],
      [
        "Noch eine andere Entdeckung macht man.",
        "Sie ist außerordentlich bedeutungsvoll für das Verhältnis der Geistesforschung zur Natur­forschung.",
        "Die Naturforschung tritt uns entgegen, indem sie sagt :"
      ],
      [
        "All dasjenige, was Menschen sagen, denken und wollen, ist gebunden an die Vorgänge des Nervensystems.",
        "Recht hat sie damit, aber sie"
      ],
      [
        "kann mit ihren Mitteln nicht die Art, wie das Seelenleben an das Nervensystem gebunden ist, herausbekommen.",
        "Man muß zu viel tieferen Grundiagen des Seeleniebens gehen, wenn man mit Geistes­forschung kommt."
      ],
      [
        "Da merkt man : Ja, es ist für das gewöhnliche Vor­stellen des Alltags durchaus richtig, daß alle Gedanken, die wir uns bilden, zum Beispiel an das Gehirn gebunden sind. - Aber wie?",
        "Das tiefere Seelische, von dem das gewöhnliche Bewußtsein gar nichts weiß, das bearbeitet erst, sagen wir, eine gewisse Gehirnpartie, das sendet erst seine Arbeitskraft hinein in Sinne und Gehirn."
      ],
      [
        "Dadurch, daß dieses unterbewußte Seelische das Nervensystem bearbeitet, wird es zum Spiegel, und das, was im gewöhnlichen Leben auftritt, ist das Spiegelbild des Seelisch-Geistigen.",
        "Gerade wie, wenn Sie sich einem Spiegel nähern, Sie nicht sich sehen oder sich erfühlen, sondern nur das Spiegelbild sehen würden, geradeso verhalten Sie sich, indem Sie Ihr alltägliches Vorstellen, Fühlen und Wollen entwickeln."
      ],
      [
        "Das tiefere Seelische arbeitet erst, und was es da erarbeitet, das macht, daß etwas wahrgenommen werden kann.",
        "So ist es das Seelisch-Geistige, was das Auge bearbeitet und was im Auge gewisse Vorgänge hervorruft."
      ],
      [
        "Das Auge spiegelt dann in das Seelisch-Geistige das zurück, was wir zum Beispiel Farben nennen.",
        "So ist es das tiefere Seelisch-Geistige, was in dem Leiblichen arbeitet.",
        "Und die Geistesforschung wird die Menschen dazu führen, zu erkennen, daß wir es selbst sind, die im Innern unserer Vorstellungen leben und mit dem tieferen Wesen selbst den Leib zu­bereiten, so daß er zum Spiegelungsapparat wird."
      ],
      [
        "In dem Augenblick, wo unsere Vorstellungen zu Erinnerungs­bildern werden, muß aber noch etwas anderes vorgehen.",
        "Wir müssen, wenn nicht die Vorstellungen wie Träume an uns vorüberhuschen, sondern zur Erinnerung werden sollen, Aufmerksamkeit verwenden.",
        "Alles, was zur Erinnerung werden soll, was bleiben soll in der Seele, auf das müssen wir uns länger konzentrieren als zu einem bloßen Vorstellungsbild.",
        "Ein Farbeneindruck würde uns nicht in der Erinne­rung bleiben, wenn wir ihn nur kurz anschauten.",
        "Schauen wir ihn etwas länger an, so appellieren wir an die Kraft, die in unserer Seele alles das als Erinnerung behält.",
        "Wir schieben unsere Seelentätigkeit in ein tieferes seelisches Wesen zurück.",
        "Dieses tiefere seelische Wesen"
      ],
      [
        "stellt sich der Geistesforschung dar als ein feiner ätherischer Leib, den man in der Geistesforschung mit dem allerdings verpönten Aus­druck «ätherisch» bezeichnen kann - doch hat das Wort nicht den Sinn, den man in der Chemie gewöhnlich damit verbindet -, es stellt sich dar als ein ätherischer Leib, der schon geistiger Art ist."
      ],
      [
        "Aber nicht nur so wirkt unsere Seele, daß sie diese Erinnerungs­bilder schafit, sondern im Leben zwischen Geburt und Tod schafft sie noch viel mehr in sich hinein.",
        "Und da entdeckt die Geistesforschung das Merkwürdige, daß unsere Erinnerungen nur deshalb Vorstellun­gen bleiben, weil sie vom Ätherleibe aufgehalten werden, weil sie nicht in den physischen Leib hineingelassen werden."
      ],
      [
        "Würden sie hineingelassen und zur Tätigkeit darinnen werden, so würden sie übergehen in die Lebenskräfte des physischen Leibes, würden ihn durchorganisieren.",
        "Dadurch, daß wir unsere Vorstellungen Vorstellun­gen sein lassen, erhalten wir sie in ihrem Vorstellungscharakter."
      ],
      [
        "Sie können Erinnerungen bleiben, aber die Seele entwickelt auch im Leben viel stärkere Kräfte als die sind, welche die Erinnerungen ent­wickeln, und sie werden nun ebenfalls zunächst in der Seele bewahrt.",
        "Doch liegen sie wie ein Übergedächmis hinter dem gewöhnlichen Gedächtnisschatz."
      ],
      [
        "Sie sind in uns.",
        "Das erlebt der Geistesforscher, wenn er durch das Gedächtnis hindurchschaut auf den übergedächt­nismäßigen Schatz, daß er weiß : Da lebt in deiner Seele etwas, was nicht hineinwirken kann in den physischen Leib, was jetzt nicht zur Wirksamkeit kommt in deinem physischen Leibe, wenn er zwischen Geburt und Tod ist."
      ],
      [
        "Da ist etwas, was nicht Vorstellung bleibt, was aber doch nicht zur organisch wirksamen Kraft wird. - Der Geistes-forscher erlebt dieses, indem er außerhalb seines Leibes ist.",
        "Aber zugleich erlebt er das andere, das er ausdrücken kann damit, daß er sagt : Ja, da erlebe ich etwas in meiner Seele, was in ihr ist, was gewissermaßen keine Anwendung findet, weil es nicht hinein kann in den Leib, der gebildet ist seit der Geburt oder, sagen wir, der Empfängnis."
      ],
      [
        "Indem sich nun der Geistesforscher hineinvertieft in dieses, was ich hier angedeutet habe, erlebt er es so, daß er es crkennen kann, wie man erkennt den Keim, der in einer Pflanze ist.",
        "Die Pflanze entwickelt sich zur Frucht hinauf, in welcher der Keim ist."
      ],
      [
        "Keim ist, hat für diese Pflanze keinen Sinn : es kann seine Kräfte nicht in diese Pflanze hineinsenken, es ist aber darinnen, es ist die Aniage zur folgenden Pflanze des nächsten Jahres.",
        "Indem der Geistes­forscher hinuntertaucht also, taucht er ein in etwas, was in ihm ein Seelenkeim ist, der gebildet wird zwischen Geburt und Tod, der aber seine Kräfte nicht entwickelt in diesem Leben.",
        "Er taucht unter und liegt bereit in dieser Seele für ein folgendes Leben, wie in der Pflanzen-frucht der Keim bereit liegt für die folgende Pflanze, die sich nicht ohne die vorhergehende entwickeln könnte."
      ],
      [
        "So kommt man zur Ansicht der wiederholten Erdenleben, wenn man auf diese Weise unterzutauchen versteht in das Geistig-Seelische.",
        "Dasjenige, was wichtig ist, ist nur, daß der Geistesforscher nicht aus dem Auge verliert : Dasjenige, was du da erleben mußt, kann nur ein solches sein, bei dem du immer wieder deiner eigenen Tätigkeit dir bewußt bist. - Denn ist man das nicht, dann wird es zur bloßen Halluzination oder zur bloßen Phantasie."
      ],
      [
        "Es ist ein Irrtum, wenn eingewendet wird : Ja, wie kann der Geistesforscher wissen, daß das nicht Halluzination, nicht Illusion, nicht Phantasie ist?",
        "Wenn der Geistesforscher sich so stellen würde zu dem, was er auf die geschil­derte Weise erlebt, wie sich das krankhafte Gemüt zu seinen Halluzi­nationen stellt, dann würde dieser Einwand voll berechtigt sein."
      ],
      [
        "Man ist aber bei einer Halluzination nicht bewußt beteiligt, man durch­schaut sie nicht.",
        "Das aber lernt gerade der Geistesforscher genau kennen durch seine Vorbereitungen, daß er unterscheiden kann das­jenige, was nur Reminiszenz der Außenwelt ist, zu dem er sich passiv verhalten muß, von demjenigen, was sich so hinstellt, daß er es erkennt, wie man von einem Buchstaben oder einem Worte weiß : Das, was auf dem Papier steht, bedeutet nicht den Buchstaben nur, sondern etwas anderes."
      ],
      [
        "Denn so verwendet der Geistesforscher nicht dasjenige, was er schaut in der Geistesforschung, wie es bei der Halluzination verwendet wird, sondern er verwendet es so, daß man es vergleichen kann mit einem geistigen Lesen in einer Schrift von Imaginationen, die sich hinstellen.",
        "Erst wenn man lernt in seinem Gemüt, dasjenige, was man da in Aktivität hinstellt, so zu verwenden, daß man darinnen lebt wie in den Schriftzügen, die man auch nicht als sich-selbst-bedeutend"
      ],
      [
        "hinnimmt, erst indem man sich in freier Weise zu dem erhebt, was da in die Seelenschau hineintritt, kann man dahin gelangen, wirk­lich zu erschauen dasjenige, was Vorgänge und Wesenheiten der geistigen Welt sind.",
        "Dann aber kommt man, weil man ja dann sich einlebt in das Element der Seele, das nicht mit dem Leibe einerlei ist, in das Wesen, von dem man sagen kann, daß die Eigenschaft der Unsterblichkeit ihm zukommt."
      ],
      [
        "Geisteswissenschaft ist keine spekulative Phantasie, in der man nachdenkt über die Gründe der Unsterblichkeit, sondern sie zeigt, wie man zur Seele selber kommt, und von dieser wahrhaftigen Seele zeigt sie, was sie ist.",
        "Sie legt gleichsam die Seele bloß."
      ],
      [
        "Und dann stellt sich heraus, daß dasjenige, was so als Seele bloßgelegt wird, kein Ergebnis der äußeren Leiblichkeit ist, daß vielmehr die äußere Leib­lichkeit selber das Produkt der Seele ist.",
        "Denn wenn man auf der einen Seite in sich entdeckt den Seelenkeim, dem man es anfühlt, aus dem man herauserlebt, daß er der Keim zu einem nächsten Erden-leben ist, so erlebt man in diesem Bewußtseinsinhalt auch dasjenige, was in das menschliche Leiblich-Physische hereingezogen ist, bevor der Mensch als physisches Wesen sein Dasein begonnen hat bei der Geburt oder Empfängnis."
      ],
      [
        "Da erlebt man, daß geradeso, wie die Seele selbst es ist, die räumlich, wie wir es wahrnehmen, ihr Gehirn zubereitet, so das Geistig-Seelische, zu dem man vorgedrungen ist, vor der Geburt oder der Empfängnis in einer geistigen Welt vorhin-den war und darin sich die Kräfte erworben hat, um sich zu verbinden mit dem, was an physischer Materialität gegeben wird von Vater und Mutter, sie zu durchdringen, sie sich anzuorganisieren.",
        "Man erlebt, daß der Mensch, wie er in die Welt einzieht, nicht das Ergebnis ist von Vater und Mutter, sondern daß sich verbindet das Geistige mit dem Materiellen, das Geistige, das aus geistigen Welten herunter­kommt, wo es gelebt hat zwischen dem letzten Tod und einer neuen Geburt."
      ],
      [
        "Und der Geistesforscher kann, wenn er so kenneniernt das, was jenseits des Gedächtnisses lebt, auch erkennen lernen, wie die Seele sich verhält, wenn nicht mehr das Leibliche die Tätigkeit des Geistig-Seelischen zurückhält, wenn der Tod über den Menschen ge­kommen ist.",
        "Wenn der Tod über den Menschen gekommen ist, dann"
      ],
      [
        "lebt die Seele zunächst - das ist die Tatsache, die sich der Geistes­forschung darbietet - in demjenigen, was während des Lebens nicht physisch-leiblich geworden ist, im Gedächtnisschatz."
      ],
      [
        "In der ersten Zeit nach dem Tode breitet sich vor der Seele ein weites Erinnerungsbild von alledem aus, was der Mensch erlebt hat zwischen Geburt und Tod.",
        "Alle die Ereignisse kommen auch herauf, die im Leben vergessen worden sind.",
        "Dieses Erleben dauert nur wenige Tage.",
        "Der Geistesforscher kann dasjenige durchschauen, was da als das erste Erlebnis nach dem Tode auftritt, weil er ja die Natur des Gedächtnisses kennenlernt.",
        "Dann wird wirklich für den Geistes-forscher so etwas zum Bewußtseinsinhalt wie für den Toten, wenn er durch die Pforte des Todes geschritten ist.",
        "Vor dem Geistesforscher tritt auch auf, wenn er außer dem Leibe ist, dieser Gedankeninhalt; aber das tritt vor ihm auf wie eine Welt : Wie man sonst Sonne, Mond und Sterne, wie man Berge und Wälder um sich hat, so hat man zunächst ein Tableau vor sich; man kann es durchschauen, man kann seine Wirkungskraft ersehen.",
        "Indem man sich hineingewöhnt, wirk­lich außerleibllch diese Dinge zu durchschauen, gelangt man auch allmählich dazu, wirklich bewußt den Blick hinzuwerfen auf dasjenige, was die Seele nach dem Tode durchlebt.",
        "Erst ist es ein Erinnerungs­bild: gleichsam breiten sich alle die Gedanken aus, die sich gesammelt haben im Gedächtnis.",
        "Aber dahinter tritt eine andere Seelenkraft auf.",
        "Jetzt ist diese Seelenkraft nicht mehr durch den Leib gehemmt.",
        "Nach einigen Tagen verschwindet das Erinnerungsbild aus der Umgebung des Menschen."
      ],
      [
        "Man kommt ja, wie schon eingangs gesagt, auf gewagte Dinge, wenn man über das Thema des heutigen Vortrages sprechen will, aber man kann nicht umhin, wenn man auf das Konkrete eingehen will, diese Dinge zu berühren."
      ],
      [
        "Ich habe darzustellen versucht, was zuerst nach dem Tode erlebt wird.",
        "Da hat sich dann ergeben, daß diese Rückschau auf die Gedan­kenbilder ganz individuell für die verschiedenen Menschen verschie­den lange dauert.",
        "Aber ungefähr kann man doch sagen, daß sie so lange dauert, als die Kraft dauern kann während des Lebens, durch die der Mensch sich frei wach erhalten kann, wenn er durch irgend etwas"
      ],
      [
        "verhindert ist, einzuschlafen.",
        "Das ist ja bei den Menschen verschieden.",
        "Diese innere Kraft, die ein Mensch hat, um den Schlaf zu bekämpfen, die ist der Maßstab für die Zahl der Tage, nach denen diese Rück­erinnerung dauert.",
        "Dann tritt etwas anderes au£ Was jetzt auftritt, in das kann man sich nur vertiefen, wenn man es auch schon durch die außerleiblichen Erlebnisse kennt.",
        "Aber es ist schwierig, Worte zu finden für die so ganz anders gearteten Erlebnisse der Seele, als es die Sinneserlebnisse sind.",
        "Unsere Sprache ist ja für die sinnliche Welt geprägt.",
        "Was außerhalb der Sinneswelt erlebt wird, erlebt die Seele ganz anders.",
        "Wenn jemand sich anschickt, mit ganz gewöhnlichen Worten der Sprache dasjenige zu schildern, wofür die Sprache nicht geprägt ist, so wird er nicht unmittelbar aus den Erlebnissen der Seele heraus schildern können dasjenige, was nach der Rückschau erlebt wird, was der Geistesforscher außerhalb des Leibes erlebt.",
        "Und das ist, was ich eben mit den ungeschickten Ausdrücken belegen möchte : es ist nämlich kein Fühlen und Wollen, sondern etwas zwi­schen Fühlen und Wollen.",
        "Ich möchte es daher nennen : ein fühlendes Wollen - ein wollendes Fühlen."
      ],
      [
        "Man hat diese Seelenkraft gar nicht im gewöhnlichen Leben.",
        "Man kennt sie als Geistesforscher.",
        "Es ist, wie wenn der Wille mit uns sich dahinbewegte in der Welt, und dieser Wille auf seinen Flügeln oder seinen Fluten dasjenige trüge, was uns nun als Gefühl so entgegen­tritt, daß es wie außer uns west, heranspielt auf den Wogen des Willens.",
        "Während wir sonst gewohnt sind, unser Gefühl zu empfangen in der Seele wie etwas, was mit uns verwachsen ist, wird das, was wir jetzt als Gefühl haben, wie wogend und wellend auf den Wellen des Willens empfunden, und wir wissen dennoch, daß wir uns damit ausbreiten in die Welt, daß das, was da draußen ist als wollendes Fühlen, was da ist wie eine Tonwahrnehmung der äußeren Sinnes-welt, von unserem Wesen durchdrungen ist."
      ],
      [
        "Aber in der ersten Zeit nach der Rückschau erlebt dies der Mensch so, daß seine einzige Welt, die er jetzt zunächst wahrnimmt, im Grunde diejenige ist, aus der er mit dem Tode herausgegangen ist.",
        "Nachdem das Erinnerungstableau abgedämmert ist, erkraftet sich in der Seele dieses wollende Fühlen.",
        "Aber es drückt nur Dinge aus, die mit dem"
      ],
      [
        "letzten Erdenleben noch zusammenhängen, so daß wir diese Dinge etwa wie folgt charakterisieren können : Das Erdenieben gibt dem Menschen niemals alles das in seine Erfahrungen herein, was es ihm geben könnte.",
        "Wir haben nicht alles genossen, was hätte genossen werden können zwischen Geburt und Tod.",
        "Es ist sozusagen zwischen den Zeilen des Lebens etwas von Begierden und Wünschen und Liebe zu anderen Menschen zurückgeblieben.",
        "Unbefriedigtes des letzten Lebens, das ist es, auf das wir begehrend geistig zurückblicken, und zwar dauert das jetzt durch Jahre.",
        "In diesen Jahren ist es so, daß wir unsere Welt hauptsächlich in dem haben, was wir gewesen sind.",
        "Wir schauen in unser letztes Erdensein.",
        "Wir schauen in ihm das, was un­erledigt geblieben ist.",
        "Und erst dadurch, daß wir in einer Sphäre leben, jahrelang, in der nichts befriedigt werden kann, was auf Erden befriedigt wird, weil wir keine Organe haben zu seiner Befriedigung, arbeiten wir uns heraus aus dem Zusammenhang mit dem letzten Erdenleben."
      ],
      [
        "Über die Länge dieser Zeit kann gesagt werden : Die Zeit, die der Mensch durchlebt in der ersten Kindheit bis zu dem Zeitpunkte, an den er sich zurückerinnern kann, die hat keinen Einfluß auf die Dauer der jetzt geschilderten Erlebnisse.",
        "Ebenso hat die Zeit, die nach dem 25., 26.",
        "Jahr weiter durchlebt wird, keinen Einfluß mehr.",
        "Die Zeit vom 4., 5.",
        "Jahre bis in die zwanziger Jahre hinein deutet die Länge an, in der man - so zusammenhängend mit seinem letzten Erdenleben -sich aus ihm herauszuziehen hat.",
        "Es stellt sich heraus für die geistige Beobachtung : So lange, als man brauchte, um seinen Leib gleichsam mit den aufwärtsstrebenden Kräften aufzubauen, also so lange, als man brauchte, um das Leben mit den körperlichen, organisch frucht­baren Kräften zu durchsetzen, ungefähr so lange dauert die Zeit, durch die man sich herausfinden muß aus dem letzten Erdenleben.",
        "So daß also, wenn ein Mensch zwölf Jahre alt stirbt, er etwa sieben Jahre braucht, um aus dem letzten Erdenleben herauszukommen.",
        "Stirbt er aber mit fünfzig Jahren, so tragen die Jahre nach der Mitte der zwanziger Jahre nichts mehr bei zur Verlängerung dieser jetzt genannten Periode."
      ],
      [
        "Von dieser Periode muß gesagt werden, daß dann schon in einer"
      ],
      [
        "gewissen Weise folgendes eintritt : Der Mensch nimmt geistige Vor­gänge und Wesenheiten in seiner Umgebung wahr.",
        "Wenn der Geistesforscher in seinem Geistig-Seelischen sich erlebt, ist er in einer wirklich geistigen Welt darinnen.",
        "In diese Welt zieht der Tote ein, aber er ist so beschäftigt in der Weise, wie wir es vorher besprochen haben, daß er nur auf dem Umweg durch sein früheres Leben einen Zusammenhang gewinnen kann mit dem, was in seiner geistigen Um­gebung ist.",
        "Ich möchte ein Beispiel angeben: Jemand geht durch die Pforte des Todes.",
        "Er lebt in der Zeit des Sichherausfindens aus dem letzten Erdenleben.",
        "Ein Mensch, den er geliebt hat, ist noch im physi­schen Leibe.",
        "Derjenige nun, der noch in dem Stadium des jetzt be­sprochenen Erlebens nach dem Tode ist, kann nicht unmittelbar auf die im physischen Leibe lebende Seele schauen, aber es findet gleich­sam eine Art von Umschaltung statt: im letzten Erdenleben haben wir den Menschen geliebt.",
        "Auf diese Liebe nun blicken wir hin.",
        "Auf dem Umweg durch die Liebe können wir den Weg finden zu einer Seele, die noch auf der Erde ist.",
        "Ebenso müssen wir auch den Weg finden zu einer Seele, die in der geistigen Welt mit uns schon lebt."
      ],
      [
        "So kann man sagen : Der Mensch lebt mit der anderen Menschen­seele als Seele nach dem Tode, aber zunächst auf dem Umweg durch sein eigenes Leben.",
        "Doch immer mehr entwickelt sich im Menschen eine seelische Kraft, die wiederum nur der Geistesforscher kennt, wenn er sein Geistig-Seelisches erlebt.",
        "Für diese seelische Kraft ist nun schon gar kein Ausdruck mehr da.",
        "Für die vorher besprochene Kraft kann man wenigstens noch sagen «Wollendes Fühlen» : sie hat etwas Ähnlichkeit mit den Dingen, die da draußen in Wollungen und Fühlungen herumwogen.",
        "Das aber, was nun die Seele erlebt, was als eine Kraft in ihr erwacht, je mehr sie sich entfernt in der geschilderten Weise vom letzten Erdenleben, ich kann es nur bezeichnen mit einem wiederum ungeschickten Wort «Kreative seelische Kraft, Schöpfer­kraft».",
        "Es ist etwas, was die Seele jetzt unmittelbar erlebt : man muß in eine Aktivität übergehen.",
        "Das erlebt die Seele nach dem Tode völlig, aber sie erlebt zugleich, daß die Schöpferkraft wirklich aus-strahlt in die Umgebung.",
        "Wiederum - es ist ein ungeschickter Aus­druck, aber ich muß ihn anwenden - ist diese kreative Schöpferkraft"
      ],
      [
        "wie etwas, was wie ein geistiges Licht ausstrahlt in die Umgebung, was die geistigen Vorgänge und Wesen beleuchtet, so daß wir sie sehen.",
        "Wie wir, wenn morgens die Sonne aufgeht, durch die Sonne die Gegenstände sehen, so sehen wir durch diese innere Leuchtekraft diese geistigen Vorgänge und geistigen Wesen."
      ],
      [
        "Jetzt tritt die Zeit ein, wo die Seele wirklich in einer geistigen Um­gebung ist, in dem Maße, in dem ihr die kreative Kraft erwacht, diese geistige Umgebung zu beleuchten.",
        "Und hier haben die Religio­nen keinen unbedeutsamen Ausdruck gebraucht : dieses Sichfühlen in der schöpferischen Kraft, dieses Sicheinleben in eine Welt, die dadurch sichtbar wird, daß man sein eigenes Licht hineinsendet, das ist ein Gefühl von Seligkeit.",
        "Selbst die Schmerzen werden so als Seligkeiten erlebt in dieser Welt. - So erlebt die Seele nun ihr weiteres Leben."
      ],
      [
        "Nun handelt es sich darum, daß die Seele in abwechselnden Zu­ständen dieses Erleben durchmachen kann, das eben beschrieben worden ist.",
        "Ich komme allerdings in Gebiete, die für ein gewöhnliches Denken ganz im Phantastischen schwimmen.",
        "Aber ich darf wohl diese Dinge sagen, denn klar wird es ja werden durch die weiteren Ausfüh­rungen.",
        "Die Seele erlebt Wechselzustände.",
        "Nicht immer ist sie in dem Zustand, daß sie gleichsam ihre geistige Leuchtekraft, ihre kreative Kraft seelisch ausstrahlt über die Umgebung, so daß geistige Wesenheiten, die um sie herum sind, von ihr erlebt werden, daß die Seele so in der äußeren geistigen Welt lebt, sondern dieser Zustand muß abwechseln mit einem anderen : mit dem, , daß die Seele gleichsam sich herabdämpfen fühlt dieses Ausstrahlen der Leuchtekraft.",
        "Die Seele wird innerlich stumpf, sie kann nicht mehr hinstrahlen ihr Licht, sie muß zusammennehmen in sich ihr ganzes Sein.",
        "Jetzt kommt dieser Moment heran, wo zwischen Tod und neuer Geburt die Seele ein völlig einsames Leben lebt.",
        "Wenn man es vergleichen will mit dem gewöhnlichen Leben, so kann man sagen : Wie im gewöhnlichen Leben wechseln Schlafen und Wachen, so muß abwechseln nach dem Tode ein Leben, das sich ausgießt in die äußere Welt, und ein Leben der innerlichen Einsamkeit, wo hereingenommen wird all das, was man früher im Zustand der Verbreiterung erlebt hat, aber wo die"
      ],
      [
        "Seele weiß : Jetzt bist du einsam. - Die Seele wird nicht bewußtlos.",
        "Sie erlebt gerade dann ein gesteigertes Bewußtsein, aber sie erlebt : Da draußen ist die geistige Welt, du aber bist allein; alles, was du erlebst, erlebst du in dir.",
        "Und das sind nur die Nachklänge des außen Erlebten; nur dadurch kann die innere Leuchtekraft wieder erstarken.",
        "Dann wacht man wiederum auf und erlebt wiederum den anderen Zustand."
      ],
      [
        "Es gehört zu den merkwürdigsten Erlebnissen, wirklich einmal zu lernen, einen Sinn zu verbinden damit, daß für die Zeit zwischen dem Tode und einer neuen Geburt das Leben der Seele abwechseln muß in den Zuständen zwischen geselligem Erleben und Einsamkeit, und daß das für die Seele etwas Ähnliches bedeutet wie Schlafen und Wachen in der physischen Welt.",
        "Ich habe das eingehend geschildert in meiner Schrift «Die Schwelle der geistigen Welt»."
      ],
      [
        "Aber die Seele erlebt so, indem sie weiterlebt zwischen dem Tod und einer neuen Geburt, allmählich ein Herabdämpfen, ein Verglimmen ihrer Leuchte­kraft.",
        "Man möchte sagen : Die Erlebnisse der inneren Einsamkeit werden immer stärker."
      ],
      [
        "Sie werden so, daß der Mensch innerlich einen ganzen Kosmos erlebt.",
        "Es überkommt ilul etwas wie das Gefühl der Furcht, wenn er entdeckt, was alles da drinnen in der Seele ist und was jetzt herauskommt in der Zeit zwischen dem Tod und einer neuen Geburt."
      ],
      [
        "Dann kommt die Zeit herauf, die ich versuchte darzu­stellen in meinem vierten Mysteriendrama «Der Seelen Erwachen», wo der Mensch nur noch vermag innerliche Erlebnisse zu haben, wo die Nächte der Einsamkeit immer länger und länger werden und der Mensch nicht mehr aufwachen kann zu den Zeiten, wo er seine Leuchtekraft ausstrahlen kann, die Zeit, die ich rnir zu nennen er­laubte : Die Mitternacht des geistigen Daseins zwischen Tod und neuer Geburt.",
        "Es ist die Zeit, wo der Mensch alles das, was in den Tiefen der Seele ist, als seine Welt erlebt, wo er nur weiß : Jenseits der Ufer deiner Seele sind die geistigen Welten, in denen alles das lebt, was an geistigen Wesen da ist, in der alle entkörperten und verkörperten Seelen sind. - Aber man weiß es nur, wenn man eben die Nachklänge in sich hat."
      ],
      [
        "Und jetzt entsteht etwas, was wieder nicht mit gewöhnlichen Worten"
      ],
      [
        "ausgedrückt werden kann.",
        "Nicht wahr, die gewöhnliche Sprache hat das Wort «Sehnsucht» für das Passivstein der Seele.",
        "Wir wünschen etwas, wir begehren etwas, was wir nicht haben, aber die Sehnsucht kann es nicht hervorbringen."
      ],
      [
        "Wir können uns nur passiv verhalten.",
        "Doch diese Seelenkraft gewinnt einen anderen Charakter.",
        "Es bildet sich jetzt die Sehnsucht, wiederum in diese Welt hinein sich zu leben, aus der man in der Einsamkeit herausgerissen ist."
      ],
      [
        "Diese Sehnsucht ist aktiv, ist organisierend in ihren Kräften.",
        "Sie wird eine neue Wahr­nehmungskraft der Seele, etwas Reales.",
        "Sie gebiert wiederum eine neue Kraft, eine Seelenkraft, die eine äußere Welt wahrnehmen kann, eine Welt, die eine äußere Welt und eine innere zugleich ist."
      ],
      [
        "Wir nehmen sie außerhalb unseres Wesens wahr, und nehmen sie zugleich wahr als die Welt unserer früheren Erdenverkörperung.",
        "Das wird jetzt unsere Außenwelt.",
        "Wir schauen hin auf all das, was unerledigt geblieben ist in uns, und in uns schimmert die Sehnsucht, Ausgleich zu schaffen im folgenden Erdenieben für das, was man im früheren Erdenieben Böses getan hat, Ausgleich zu schaffen dafür in einem neuen Leben."
      ],
      [
        "Das ist die Zeit, in der jeder Mensch zurückblicken kann auf frühere Erdenleben.",
        "Das ist die Zeit, wo dem Menschen vor dem geistigen Auge stehen alle die Taten seiner früheren Leben.",
        "Und in ihm erwacht die Tendenz, in einem neuen Erdenieben solchen Ausgleich zu schaffen, daß die Erlebnisse im neuen Erdenleben aus­gleichen und gutmachen dasjenige, was in früheren Erdenleben ver­säumt worden ist."
      ],
      [
        "Ich habe schon Menschen kennengelernt, die sich nicht zur Geistes­wissenschaft bekennen konnten, weil sie, wie sie sagten, mit einem Erdenleben genug hatten.",
        "Ich habe auch einen Menschen kennen­gelernt, der etwas Vernünftiges darin fand, von der nächsten Eisen-bahnstation nichts zu wissen.",
        "Darauf kommt es nicht an, daß wir nur zurückblicken auf frühere Erdenleben, sondern vielinehr darauf kommt es an, daß jede Seele zurückblickt und zugleich die Tendenz in sich aufnimmt, ein neues Erdenleben zum Ausgleich zu erleben.",
        "Und man erlebt weiter, daß es Menschen gibt, denen man etwas schuldig wurde oder die einem etwas schuldig wurden : das tritt vor die Seele hin als Ergänzung, und es tritt die Tendenz auf, wieder zu"
      ],
      [
        "leben mit diesem Menschen im Erdenleben.",
        "Dadurch werden Kräfte erzeugt, welche zur Erde tendieren.",
        "Gleiche Kräfte werden in den verschiedenen Menschen erweckt, und so kommt es zur Wiederbe­gegnung von Menschen, um das wieder auszugleichen, was sie ein­ander schuldig geworden sind in früheren Erdenleben."
      ],
      [
        "Dann erlebt man immer weiter und weiter dieses geistige Leben zwischen dem Tod und einer neuen Geburt.",
        "Immer mehr und mehr prägt sich ein die Tendenz zu einem neuemn Erdenleben.",
        "Es werden lebendige Tendenzen, und der Mensch schafit sich aus dem, was er so erfahren hat, das Urbild, das geistige Urbild des neuen Erdenlebens.",
        "Da schafit er nun selbst, indem die Zeit weiterrückt, was sich verbin­det mit der materiellen Substanz von Vater und Mutter, um in ein neues Erdenleben einzutreten.",
        "Und je nachdem diese Substanzen sein können, wird man hingezogen zu dem Verwandten.",
        "So daß man sagen kann : Die Wahlverwandtschaft zwischen den ererbten Eigenschaften und dem Urbilde - das entscheidet, zu welchem Elternpaar man sich hingezogen fühlt, in welches Leben man sich hineinfindet.",
        "Dadurch kommt der Mensch wiederum zur Erde zurück und vereinigt sich wiederum mit einem physischen, mit einem irdischen Leibe."
      ],
      [
        "Und die Geistesforschung kann nun sehen, was im Kinde auf so mysteriöse Weise sich herausbildet, indem von innen heraus die ausdrucksvolle Miene allmählich tritt, indem aus ungeschickten Be­wegungen geschickte Bewegungen werden, der Körper modernert wird.",
        "Es schaut der Geistesforscher dasjenige, was durch das Leben zwischen Tod und neuer Geburt hindurchgegangen ist und wie es sich da immer mehr und mehr mit dem Leibe verbindet.",
        "Das schaut der Geistesforscher.",
        "Nun sieht er auch ein, warum zunächst keine Erinnerungen an diese Erlebnisse vorhanden sein können : die Kräfte, welche Erinnerungskräfte werden könnten, die werden aufgebraucht, um den Leib zu organisieren.",
        "Das Kind hat die Kräfte, sich zu erinnern an alles Frühere, aber die Kräfte werden umgewan­delt.",
        "Ebenso wie die Druckkräfte, die ich entwickele, wenn ich über den Tisch fahre mit dem Finger, sich in Wärme verwandeln, so ver­wandelt sich die Erinnerungskraft in organische Kraft.",
        "Was das Ge­hirn plastisch macht, das ist umgewandelte rückschauende Kraft, das"
      ],
      [
        "verschwindet in dieser Gestalt, in der es die Rückschau entwickeln kann, und organisiert den Leib durch.",
        "Es ist das umgewandelte Seelische.",
        "Es ist hereingeflossen in den Leib, es wirkt im Leibe darinnen."
      ],
      [
        "So begreifen wir das Leben, in dem wir gerade stehen, wenn wir das Leben verstehen, das vorher, das vor der letzten Geburt liegt.",
        "Dieses jetzige Leben, es hat sich seine Kräfte angeeignet zwischen dem letzten Tode und der Geburt.",
        "Die Kräfte, die da geistig zutage treten, sind die Erinnerungskräfte, die sich umgewandelt haben, die den Leib durchorganisiert haben.",
        "Gewisse niedere Tiere sterben zu­gleich, indem sie reif werden zur Hervorbringung eines anderen Lebens.",
        "Das, was der Mensch an Kräften entwickeln muß, um phy­sische Nachkommen zu haben, das muß mit seiner Geschlechtsreife abgeschlossen sein; das kann ich nur andeuten.",
        "Die Naturforschung wird einmal darauf kommen , wie die Kräfte, die in der Vererbung liegen, etwas wie eine Erschöpfung erfahren.",
        "Darüber wird die Natur­wissenschaft und die Geisteswissenschaft zusammen wichtige Auf­schlüsse geben können."
      ],
      [
        "Aber darinnen wirken geistige Kräfte, und diese geistigen Kräfte sind es, die sich so betätigen, daß sie diesen physischen Leib durch­dringen.",
        "Der physische Leib ist gleichsam die Spiegelung des Geisti­gen, und im Grunde genommen sind es eigentlich Zerstörungspro­zesse, die die Spiegelung herbeiführen.",
        "Wenn wir Erinnerungsvor­stellungen bilden, wenn wir im Auge Farben sehen, so ist das ein Zerstörungsprozeß.",
        "Im Schlafe wird wieder aufgebaut."
      ],
      [
        "So leben wir, indem wir unseren Leib durchdringen und durch­kraften mit den Kräften, die wir außerhalb des Leibes erwerben.",
        "Und das Leben läßt sich nur begreifen, wenn wir dieses im Leben tätige Geistig-Seelische ins Auge fassen.",
        "Geisteswissenschaft hat es ja nicht so gut, daß sie vom Tod der Pflanzen und Tiere spricht wie vom Tode des Menschen, und das, was ich sagte, das gilt nur für den Menschen."
      ],
      [
        "Auf diese Weise erweitert die Geistesforschung den Blick über das hinaus, was zwischen Geburt und Tod liegt.",
        "Ja, auch Einzelheiten werden durch die Geistesforschung erklärbar.",
        "Ich kann mir sehr gut denken, daß diejenigen der verehrten Zuhörer, welche etwas übrig haben für diese Geistesforschung, gerne etwas einzelnes hören wollen."
      ],
      [
        "Aber ich kann ja nur einzelne Beispiele anführen.",
        "Ein Beispiel, das wie ein rechtes Mysterium des Lebens erscheint, sei hier angeführt : das Dasein der Verbrechernaturen.",
        "Der Geistesforscher steht durch­aus nicht etwa auf dem Standpunkte der Utopisten, als wenn die Ver­brecher nicht bestraft werden sollten und so weiter, aber verstehen dasjenige, was im Menschenleben uns entgegentritt, das will der Geistesforscher.",
        "Da fragen wir uns : wie liegt es denn mit einem Leben, das sich verbrecherisch offenbart?",
        "Nun, leicht sind die Dinge gesagt, aber die Antworten auf solche Fragen muß sich der Geistesforscher erst abringen.",
        "Und abringen muß er sich, darüber zu sprechen, weil dasjenige, was er zu sagen hat, gar so paradox erscheint."
      ],
      [
        "Wenn der Verbrecher hellseherisch angeschaut wird, so stellt sich heraus, daß verbrecherische Naturen eine Art geistiger Frühgeburten sind.",
        "Es gibt für jede Seele eine Möglichkeit, herunterzukommen in die physische Welt, die gewissermaßen die normale ist."
      ],
      [
        "Aber die Tendenz, die dazu hinführt, die kreuzt sich mit anderen Tendenzen, so daß die meisten Menschen - aber die Verbrecher besonders stark -viel früher ins Erdenleben heruntergehen, als es normalerweise ge­schehen sollte.",
        "Und das hat etwas anderes im Gefolge."
      ],
      [
        "So richtig sich durchdringen mit der ganzen Leiblichkeit, so daß man als Vollmensch dasteht, das kann man nur, wenn man sich annähernd zu dem nor­malen Zeitpunkte wieder verkörpert.",
        "Aber wenn Gründe vorhanden sind, durch die besonderen Umstände früherer Erdenieben früher herunterzukommen, so nimmt man etwas auf im Unterbewußtsein, wovon man nichts weiß, was in den Tiefen der Seele lebt, etwas, was wie ein Leichtnehmen des Erdenlebens ist, weil man nicht zu dem Zeitpunkte herunterkommt, wo man sich völbg mit dem Erdenieben hätte verbinden können."
      ],
      [
        "Das wird eine innere Seelenstimmung, dieses das Leben-nicht-voll-Nehmen.",
        "So kann es sein, daß man im gewöhn­lichen Oberbewußtsein einen starken Selbsterhaltungstrieb hat, den stärksten Egoismus entfaltet im Verbrechertum, und dennoch in seiner inneren Natur, die man nicht kennt, ein gewisses Oberflächlich-nehmen, ein Leichtnehmen des Lebens hat, keinen Wert legen will auf dieses Leben, in das man hineingekommen ist durch eine geistige Frühgeburt."
      ],
      [
        "Wenn das so ist, dann tritt dieses Leben auch so ins"
      ],
      [
        "Dasein, daß der Mensch den überhandtiehmenden Selbsterhaltungs­trieb anfeuern kann durch dasjenige, was er nicht kennt.",
        "Das Leicht-nehmen des Lebens : das ist es bei den Verbrecherseelen.",
        "Erst als ich dies wußte, wurde mir ein anderes klar : Es gibt Lexika der Verbre­chersprache.",
        "Man versteht die eigentümliche Art der Verbrechersprache - dieses in den Worten Leichtnehmen des Lebens -, man ver­steht sie erst, wenn man das kennt, was jetzt angedeutet worden ist.",
        "In der Gesamtheit der menschlichen Erdenleben gleicht sich dies aber wieder aus, so daß der Verbrecher dasjenige, was er als die Folge des Zu-früh-geboren-Werdens in einem Erdenleben tut, in anderen Erdenleben wieder ausgleicht."
      ],
      [
        "Aber auch anderes wird verständlich durch die Geistesforschung.",
        "Da sehen wir Menschen, welche durch ein Unglück hinweggerafft werden, die Erde verlassen durch ein Unglück in einer Zeit, in welcher sie die Erde noch nicht verlassen sollten.",
        "Wenn zum Beispiel ein Mensch in seinem 35.",
        "Jahre von einer Lokomotive überfahren wird, stecken in seinem Leibe Kräfte, die lange noch wirken könnten.",
        "Indem er nun hinausgeht aus der physischen Welt, gehen diese Kräfte nicht in ein Nichts über; die intellektuellen Kräfte verstärken sich merk­würdigerweise gerade durch solche Dinge.",
        "Ein Mensch, der so durch ein Unglück umkommt, kann mit starkem Intellekt wieder geboren werden.",
        "Geistesforschung, indem sie das Leben von einem großen Horizont aus anblickt, muß über manches anders reden, als man im gewöhnlichen Leben redet.",
        "Jemand, der durch eine Krankheit stirbt, der vieles durchinacht durch diese Krankheit, der bereitet seine Seele so, daß seine Willenskräfte verstärkt werden können.",
        "Frühzeitiges Sterben durch Krankheit verstärkt die Willens kräfte."
      ],
      [
        "Manches von dem Gesagten mag schon wie reine Phantastereien er­scheinen, aber ich bin mir auch bewußt, daß ich eine gewisse Verantwor­tung habe, wenn ich diese Dinge bespreche, und ich weiß, daß ich dies nicht tun würde, wenn ich nicht wüßte, daß diese Dinge genau gewußt werden müssen, ebenso genau wie die Dinge der äußeren Wissenschaft.",
        "Ich würde es als größte Frivolität empfinden, wenn solche Dinge be­sprochen werden, ohne daß in der Seele ein Wissen lebt, das von einer solchen Stimmung durchdrungen ist, wie ich es eben angedeutet habe."
      ],
      [
        "So wird das Leben des Menschen gerade verständlich durch das­jenige, was außerhalb des physischen Lebens liegt.",
        "So wie sich das Leben hier zwischen Geburt und Tod entwickelt, so ist es ein Ergeb-nis des Lebens jenseits von Geburt und Tod."
      ],
      [
        "Für manchen mag das wie eine Entwertung des Lebens erscheinen.",
        "Damit es nicht so er­scheine, möchte ich hier schon Ausgesprochenes kurz wiederholen.",
        "Wenn jemand sagt : Ja, da werden wir darauf aufmerksam gemacht, daß wir das , was wir in einem Erdenieben erleben, uns selbst zubereitet haben! - Wahr ist es."
      ],
      [
        "Wir erleben ein Unglück, weil wir vor der Geburt die Tendenz in unsere Seele eingepflanzt haben, in dieses Unglück einzumünden.",
        "So wie die eine Pflanze nur im Hochgebirge leben kann, so sucht die Menschenseele sich ihre Umgebung auf, sie wächst hinein in das Schicksal."
      ],
      [
        "Wie das Schicksal selbstverständlich ist, in den Alpen zu leben für jene Pflanze, so ist es selbstverständlich für die Menschen-seele, sich ins Unglück zu stürzen, weil sie weiß : dadurch kann sie ausgleichen etwas Unvollkommenes aus den früheren Erdenleben.",
        "Wenn jemand sagt : So werden wir also zu Schmieden unseres eigenen Unglückes gemacht, und wir sollen nicht nur unser Unglück ertragen und erdulden, sondern wir haben es überirdisch verdient; das kann uns kein Trost sein, - so muß demgegenüber gesagt werden, was ich durch einen Vergleich klarmachen möchte : Nehmen wir an, ein Mensch, dessen Vater sehr reich ist, der im Überfluß lebt ohne etwas gelernt zu haben, erlebt, als junger Mensch von 18 Jahren, den Bankerott des Vaters."
      ],
      [
        "Dann kann es ein großes Unglück für ihn sein, wenn das Leben ihn hart anläßt.",
        "Er hat recht, sich im Leben jetzt unglücklich zu fühlen.",
        "Aber im 50.",
        "Jahr seines Lebens sieht er von einem anderen Gesichtspunkte sein Unglück vom i 8."
      ],
      [
        "Jahr an.",
        "Er sagt sich : wenn das Unglück dazumal nicht gekommen wäre, wäre ich vielleicht längst untergegangen, denn ohne dieses Unglück wäre ich niemals ein tüchtiger Mensch im Leben geworden; es war für mich ein Entwickelungsferment meines Lebens. - So sind wir nicht immer in der Lage, in dem Zeitpunkt des Erlebens den richtigen Gesichtspunkt zu finden gegenüber dem, was wir erleben."
      ],
      [
        "Wir stehen in der geistigen Welt auf einem ganz anderen Gesichtspunkt.",
        "Wir wissen da, daß das erlebt werden muß im neuen Leben, was Ausgleich"
      ],
      [
        "schaffen kann für ein früheres Leben.",
        "Da bereiten wir uns selber das Leben, über das wir mit einem gewissen Recht dann klagen, wenn wir es nachher nur vom physischen Standpunkte aus betrachten können."
      ],
      [
        "Ein Weniges möchte ich noch sagen über die Zeit, die verfließt zwischen dem Tode und einer neuen Geburt.",
        "Der Geistesforscher muß sich zunächst fragen : Was ist es denn in deiner Seele, was dir, wenn du außer dem Leibe dich seelisch-geistig erlebst, so erscheint, daß es in der Seele ist wie etwas, was von ihr durch den Tod getragen werden kann? - Da erlebt man, daß man aus dem Leibe heraus in das Leben, das außer dem Leibe erlebt wird, seine Überwindungen mit­nimmt.",
        "Dasjenige nimmt man mit, was man sich eigentlich erst an­eignen kann nach den zwanziger Jahren.",
        "Man wird das heute nicht gerne hören, weil die Leute heute vor den zwanziger Jahren schon für reif gehalten werden wollen.",
        "Das kann man ja sehen in den Zeitungen : über und unter dem Strich schreiben oft junge Leute, die noch nicht das 20.",
        "Jahr erreicht haben.",
        "Aber in Wahrheit ist es doch so: Was wir so recht durch uns selbst in unserer Seele erleben, so daß es wirkliche aufgespeicherte Lebensweisheit wird - das erleben wir dadurch, daß man schon etwas erfahren haben muß, gleichsam eine innerliche Sporenarbeit beim Aufwärtssteigen.",
        "Dieses innerliche Auf­wärtssteigen ist dasjenige, was schon ein Vorkeim ist zu dem, was die Seele durchlebt zwischen dem Tod und einer neuen Geburt.",
        "Und so muß im fortwährenden Überwinden, im Umwandeln von Kräften die Seele leben.",
        "Normalerweise bleibt die Seele so lange in der Zeit zwischen dem Tod und einer neuen Geburt, als sie etwas umzuwandeln hat."
      ],
      [
        "Von anderer Seite betrachtet wäre folgendes zu sagen.",
        "Indem wir durch den Tod gegangen sind, haben wir den Seelenschatz gebildet, der mit durch den Tod geht.",
        "Aber die Erde verändert sich.",
        "Denken Sie zurück, wie die Gegend, wo jetzt Wien steht, sich verändert hat.",
        "Das Kulturantlitz der Erde verändert sich, es verändert sich der geistige Inhalt unserer Umgebung, aus dem wir unsere Erinnerungen, unseren Erinnerungsschatz nehmen.",
        "Die Seele kommt nun normaler­weise nicht früher zurück, bis sie in eine vollständig neue Umgebung treten kann.",
        "Nicht ohne Sinn ist es, daß die Seele wieder geboren"
      ],
      [
        "wird, so daß sie in einem neuen Erdenleben Neues erleben kann.",
        "Dazu muß sie aber alles andere, was sie aus früheren Erdenleben hereingebracht hat, umwandeln.",
        "Zum Beispiel muß sie eine andere Sprache lernen und so weiter.",
        "Das unifaßt eine Zeit von Jahrtausenden, von ein bis andertlialb Jahrtausend.",
        "Aber es können, wie gesagt, geistige Frühgeburten entstehen.",
        "Ich kann mich bei der Kürze der Zeit mit der Ausmalung der Verhältnisse, die mit dem Thema zusam­menhängen, nicht weiter befassen, ich kann nur noch sagen, wer da meint : Ja, das ist ja alles wirklich nicht zu glauben.",
        "Wie soll denn der Mensch darüber etwas wissen können? - der sei darauf aufmerk­sam gemacht, daß in der Tat spätere Selbstverständlichkeiten, Er­kenntnisse, die in alle Seelen eingedrungen sind, zuerst der Erden-kultur als paradox erschienen sind, wenn sie mitgeteilt wurden.",
        "Und derjenige, der heute Geisteswissenschaft pflegen will, der muß sich schon bekannt machen damit, wie begreiflich es ist, daß vielfach noch als Phantastereien aufgenommen wird dasjenige, was er zu sagen hat.",
        "Wie einstmals die Kopernikanische Weltanschauung sich eingebürgert hat, nachdem sie zuerst als etwas Schädliches angesehen wurde, so wird auch aufgenommen werden dasjenige, was Geisteswissenschaft der Welt zu geben hat."
      ],
      [
        "Noch einmal sei auf das Bild aufmerksam gemacht, das sich vor den Geistesforscher hinstellt, ihm das starke Bewußtsein zu geben von der Wahrheit, die sich allmählich durchringen wird, auch durch die engsten Felsenspalten der Kultur.",
        "Sie wird sich durchdrücken.",
        "Er-starken wird man in dem Bewußtsein daran, wenn man auf solche Individualitäten wie Giordano Bruno hinblickt.",
        "Er trat vor die Mensch­heit so, daß er jahrhundertealte Vorurteile zerstörte, indem er sagte :"
      ],
      [
        "Wenn ihr hinaufschaut in den weiten Raum, erscheint es euch so, als ob die Sonne um die Erde kreise, die Planeten um die Erde kreisten, als ob das blaue Himmelsgewölbe eine Wand sei, eine blaue Wand! -Damals konnte Giordano Bruno auftreten und sagen : Diese blaue Wand erscheint euch nur deshalb, weil euer eigenes Erkenntnisver­mögen, euer Wahrnehmungsvermögen nur bis dahin reicht.",
        "Aber die Unendlichkeit des Raumes breitet sich aus da, wo eure beschränkten Sinne eine Wand sehen, und sie ist erfüllt von unendlichen Welten."
      ],
      [
        "Heute muß der Geistesforscher dieser Erweiterung des mensch­lichen Blickes in die Unendlichkeiten des Raumes gedenken, daran denken, wie Giordano Bruno zuerst aufmerksam machte darauf, daß die Grenze des Firmamentes nur von der Beschränktheit des mensch­lichen Wahrnehmungsvermögens selbst gemacht ist.",
        "Denn er muß hinweisen darauf, daß das auch für die Zeit des Menschenlebens gilt, die zwischen Geburt und Tod liegt.",
        "Indem man mit den physischen Wahrnehmungsorganen sie ansieht, sieht man auch diese Grenze von Geburt und Tod.",
        "Wie man einst die Grenze sah da oben am blauen Himmeisgewölbe, die Grenze des Raumes, so ist auch die Zeitgrenze nur hingesetzt, und jenseits breitet sich auch aus die zeitliche Un­endlichkeit, und in diese zeitliche Unendlichkeit sind eingebettet die nach rückwärts und vorwärts verlaufenden Erdenleben.",
        "Das kann noch gesagt werden - ich kann das allerdings jetzt nicht näher aus­führen -, daß die ganzen Wiederholungen einmal einen Anfang nahmen dazumal, als die Erde selbst entstand.",
        "Und einmal wird der Mensch wieder in ein anderes, in ein vergeistigteres Erdenleben ein­treten."
      ],
      [
        "Wenn man sich auch in der Gegenwart in der angedeuteten Weise mit diesen Erkenntnissen auseinanderzusetzen hat, so muß man dennoch sagen : In den Ahnungen derjenigen, die die Führer der Menschheit waren, lebten diese Erkenntnisse.",
        "Man findet in den Ahnungen der führenden Geister der Menschheit vielfach dasjenige, was in der Geisteswissenschaft heute wiederum auflebt.",
        "Geistes­wissenschaft, wie sie hier gemeint ist, haben die Menschen nicht ge­habt, denn sie ist ein Kind unserer Zeit und wird aus der Bildung unserer Zeit entstehen.",
        "Aber denen, die sich in ihrer Seele verbunden wußten mit dem Geiste des Alls, denen drückt sich in die Worte hinein dasjenige, wozu die Geisteswissenschaft im vollen Sinne Ja sagen kann.",
        "Geisteswissenschaft zeigt uns, wie wir das Leben zwischen Geburt und Tod verstehen, indem wir in diesem physischen Leibe , in dem ganzen physischen Leben wirkend und webend dasjenige sehen, was unsterblich ist und in einer geistigen Welt leben kann.",
        "Geisteswissenschaft zeigt uns, daß wir das Leben im Leibe haben durch das Leben außer dem Leibe, so daß niemand das Leben im"
      ],
      [
        "Leibe verstehen kann, der nicht das Leben außerhalb dieses geistigen Firmamentes versteht.",
        "Das drückte Goethe mit Worten aus, ahnend die späteren Erkenntnisse der Geisteswissenschaft, mit Worten, die nicht nur Goethes Bekenntnis zu einem unsterblichen Leben dar­stellen, sondern die auch ausdrücken, daß er wußte, daß der wirkliche Wert des Erkennens des gegenwärtigen Lebens im Erleben des Da­seins davon abhängt, daß man dieses irdische Dasein durchleuchtet weiß von dem, was überirdisch ist, was unsterblich ist.",
        "Deshalb sei gerade diese Erkenntnis der Geisteswissenschaft, daß die wahre innere Wesenheit des Sterblichen in einem Unsterblichen begründet ist, kurz zusammengefaßt in die Worte, in denen Goethe seine Anschau­ung ausdrückte.",
        "Denen gegenüber, die sich gar nicht wollen aus der eigentümlichen Wesenheit des gegenwärtigen Lebens eine Anschau­ung bilden über ein anderes Leben, denen gegenüber : «möchte ich sagen» - das sind die Worte Goethes - «mit Lorenzo von Medici, daß alle diejenigen auch für dieses Leben tot sind, die kein anderes er­hoffen.»"
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "INNERES WESEN DES MENSCHEN UND LEBEN ZWISCHEN TOD UND NEUER GEBURT ERSTER VORTRAG Wien, 9. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Dieser Vortragszyklus wird das Ziel haben, das menschliche Innenleben zu schildern im Zusammenhang mit dem Leben zwischen dem Tod und einer neuen Geburt, um zu zeigen, wie inrüg diese beiden Gebiete des Daseins zusammenhängen. Und er wird daneben das Ziel haben, Richtlinien zu entwickeln aus der Erkenntnis des Angedeuteten heraus, die den Menschen wirklich orientieren können in manchen schwierigen Lebensiagen, die geeignet sind, in mancher Beziehung einen sicheren Halt des Seelenlebens durch ein gewissermaßen gründ­liches Verständnis dieses Seelenlebens zu geben. Dazu wird notwendig sein, daß Sie sich, meine lieben anthroposophischen Freunde, durch die ersten Vorträge, die ein Fundament, eine Grundiage aufrichten sollen, hindurcharbeiten; sie werden in esoterisch wissenschaftliche Gebiete führen, die vielleicht manchem zunächst abgelegen scheinen könnten, weit weg von dem, was das menschliche Gemüt gerne un­mittelbar ergreifen möchte. Aber wenn wir zu dem gelangen werden, worin diese Vorträge eigentlich ihr Ziel erblicken, dann werden Sie sehen, daß dieses Ziel in einer sicheren Form doch nur zu erreichen ist, wenn man sich zuerst durch die scheinbar entlegenen esoterischen Erkenntnisse, die geboten werden sollen, hindurcharbeitet.",
      "Wenn man das menschliche Innenleben zunächst abstrakt betrachtet, so tritt es einem in drei Formen entgegen, auf die wir oftmals auf­merksam gemacht haben: in den Formen des Denkens, des Fühlens und des Wollens; aber um dieses Innenleben vollständig zu betrachten, muß man noch ein Viertes dazurechnen. Eigentlich gehören nicht nur diese drei genannten Gebiete zum Innenleben des Menschen, sondern es gehört auch schon das dazu, was er aus der bloßen Sinnesempfin-dung macht. Wir lassen ja Farben und Töne, Wärmeeindrücke und dergleichen nicht nur vor unserem Bewußtsein vorüberhuschen, sondern wir fassen diese Eindrücke auf, wir machen sie zu unseren Wahrnehmungen. Und die Tatsache, daß wir uns an diese Eindrücke",
      "erinnern können, daß wir sie behalten können, daß wir nicht nur dann wissen: eine Rose ist rot, wenn wir der Rose unmittelbar gegen­überstehen, sondern daß wir sozusagen die Röte der Rose mit uns herumtragen können, die Farben als eine Erinnerungsvorstellung be­wahren können, das bezeugt uns, daß das Empfindungsleben, das Wahrnehmungsleben, durch das wir uns mit der Außenwelt in Be­rührung bringen, auch schon zu unserem Innenleben gehört. So daß wir sagen können: Zu unserem Innenleben müssen wir zählen die Wahrnehmung der Außenwelt, insofern wir sie eben im Wahrnehmen selber verinnerlichen. Ferner müssen wir die Gedankenwelt dazuzählen, durch die wir uns zunächst Erkenntnisse verschaffen von dem Nächstliegenden und in der Wissenschaft von dem Fernerliegenden, durch die wir in einem viel weiteren Sinn noch als durch die Wahr­nehmung der Außenwelt zu unserer Innenwelt machen. Wir leben ja nicht nur in unseren Wahrnehmungen, wir denken über sie nach und haben das Bewußtsein, daß wir durch unser Nachdenken etwas über die Geheimnisse des Wahrgenommenen erfahren können.",
      "Wir müssen dann zu unserem Innenleben rechnen unsere Gefühle, und wir sind mit den Gefühlen sogleich in demjenigen Gebiete des menschlichen Innenlebens, das sozusagen in sich alles einschließt, was uns als Menschen selbst mit der Welt in eine der Menschenwürde entsprechende Berührung bringt. Daß wir über die Dinge fühlen können, daß wir uns freuen können an der Umgebung, das ist ja erst die Grundiage unseres wahren Menschendaseins, in gewisser Bezie­hung auch alles das, was unser Glück und unser Leid ausmacht. Es spielt sich ja das alles ab in auf- und abwogenden Gefühlen: Gefühle, die unser Leben erhöhen, drängen sich herauf oder heran an uns, erstarken, in denen wir uns glücklich und zufrieden finden. Andere Gefühle drängen sich heran durch die Ereignisse des Lebens, durch unser Schicksal, auch durch unser Innenleben, die unser Leid, unseren Schmerz bedeuten. Und indem man das Wort «Gefühl» ausspricht, deutet man auf das Gebiet hin, das in der Tat eben Glück und Leid des Menschenlebens einschließt.",
      "Wenn man auf das Vierte hinweist, auf den Willen, so handelt es sich um etwas, was uns wiederum wertvoll für die Welt macht, was",
      "uns soin die Welt hineinstellt, daß wir nicht nur erkennend, nicht nur in uns fühlend für uns leben, sondern daß wir auf die Welt zurück-wirken können. Was ein Mensch will, wollen kann, und was vom Willen in die Handlungen ausfließt, das bildet seinen Wert für die Welt. Wir können uns also sagen: Indem wir auf das Gebiet des Willens hinweisen, haben wir es mit jenem Elemente zu tun, das uns den Menschen als ein Glied der Welt zeigt, und es ist unser Innenleben, das da als ein Glied in die Welt einfließt. Ob es die egoistischen, die sozial feindlichen Affekte und Leidenschaften der verbrecherischen Naturen sind, die in den Willen einfließen und von da aus Glied der Welt werden zum Verderben der Welt, oder ob es die hohen reinen Ideale sind, die der Idealist herunterholt aus seiner Berührung mit einer geistigen Weltenordnung und einffießen läßt in sein Handeln, einfließen läßt vielleicht nur in Worte, welche, anfeuernd oder auch Menschenwürde zeigend, auf die Menschen wirken; immer haben wir es auf dem Gebiete des Willens mit dem zu tun, was dem Menschen seinen Wert gibt. So daß der ganze Reichtum, den der Mensch eigent­lich als Seelenwesen haben kann, sich ausdrückt, wenn man diese vier Gebiete nennt: Wahrnehmung, Denken, Fühlen, Wollen.",
      "Für denjenigen, der nun etwas tiefer eingeht auf eine Betrachtung dieser vier, man möchte sagen inneren Sphären der menschlichen Seelennatur, zeigt sich ein bedeutungsvoller Unterschied zwischen zwei und zwei Gliedern dieser viergliedrigen menschlichen Wesenheit. Aber im gewöhnlichen Leben kommt dieser Unterschied eigentlich den Menschen nicht so sehr zum Bewußtsein, er kommt höchstens zum Bewußtsein, wenn wir in der folgenden Weise über diese vier Sphären der Menschennatur nachdenken.",
      "Wenn wir von der Wahrnehmung sprechen und über sie nachden­ken, so können wir die Empfindung haben: mit der Wahrnehmung stehen wir unmittelbar in einer gewissen Beziehung zur Außenwelt. Wir verinnerlichen durch die Wahrnehmung die Außenwelt, sie liefert etwas, was dann zu unserem Innern gehört, wenn wir die Empfindung verarbeiten. Aber wir haben das Gefühl: wir müssen unsere Empfin­dung so eingerichtet haben, daß sie uns in gewisser Beziehung treue Abbilder der Außenwelt gibt. Und jede Erkrankung des Wahrnehmungs-, des Empfindungslebens,",
      "jede Erkrankung der Sinne weist uns ja darauf hin, daß durch eine solche Erkrankung unser Innenleben verarmt, dadurch verarmt, daß wir eben ärrner werden an dem, was wir von der Außenwelt in uns hereinbekommen können.",
      "Gehen wir von dem Wahrnehmen zum Denken über, dann können wir gewahr werden, daß wir auch gegenüber dem Denken die Empfindung haben: es kann uns nicht genügen, wenn dieses Denken bloß in sich selber wühlt und sich in sich ergeht. Die Gedanken haben letzten Endes doch nur einen Wert, wenn sie uns etwas Objektives, außer uns Befindliches in uns vergegenwärtigen, wenn sie Aufschluß zu bringen vermögen von etwas, was außer uns ist. Unser Nach­denken könnte uns nicht befriedigen, wenn wir durch dieses Nach­denken nicht etwas erfahren könnten über die Außenwelt.",
      "Wenn wir aber zu unserem Gefühle vorschreiten und ein wenig über dieses Gefühl nachdenken, dann werden wir finden, daß dieses Gefühl, oder besser gesagt das Gefühlsleben, viel inniger zusammen­hängt mit unserem unmittelbaren Innensein als Denken und Wahr­nehmen. Wir haben die Vorstellung, daß wir uns selber, zunächst rein äusserlich, auf dem physischen Plan entwickeln müssen, wenn wir gewisse Feinheiten der Außenwelt in richtiger Weise empfinden wollen, fühlen wollen. Haben wir einen Gedanken und nennen wir den Gedanken wahr, so sagen wir von einem solchen wahren Ge­danken: er muß eigentlich für alle unsere Mitmenschen gelten, und es muß, wenn wir nur die richtigen Worte finden den Gedanken auszu­drücken, die Möglichkeit geben, von diesem Gedanken auch andere zu überzeugen. Wenn wir einer Naturerscheinung oder aber, sagen wir, einer menschlichen Kunstschöpfung gegenüberstehen und unser Gefühl daran entwickeln, so wissen wir, daß im Grunde genommen zunächst unsere Menschennatur, so wie sie ist, uns nichts hilft, um gleichsam völlig auszuschöpfen, was uns da entgegentreten kann. Es könnte sein, daß wir völlig stumpf bei einer musikalischen oder bei einer malerischen Schöpfung bleiben, einfach weil wir unser Gefühl nicht so erzogen haben, daß wir die Feinheiten wahrnehmen können. Und wenn wir diesen Gedankengang verfolgen, dann finden wir, daß dieses Gefühlsleben etwas sehr Innerliches ist, daß wir es auch so,",
      "wie wir es innerlich erleben, nicht gleich in Gedanken übertragen können auf andere Menschen. Wir sind in unserem Gefühlsleben unter allen Umständen in gewissem Sinne allein, aber wir wissen gleichzeitig, daß dieses Gefühlsleben die Quelle eines ganz besonderen inneren Reichtums, einer inneren Entwickelungs-Tatsache gerade dadurch ist, daß es etwas so Subjektives ist, daß es nicht unmittelbar so ins Objekt hinausfließen kann, wie es innerlich lebt.",
      "Ein Gleiches müssen wir sagen in bezug auf den Willen. Wie sind wir Menschen doch verschieden in bezug auf das, was wir wollen können, auf das, was durch den Willen in unsere Handlungen hinaus­fließen kann!",
      "Nur dadurch kommt ja eigentlich die Mannigfaltigkeit des menschlichen Handelns zustande, daß der eine dies, der andere jenes wollen kann. Wenn wir beim Gefühl uns freuen können, daß wir etwa einen Genossen im Leben finden, der rein innerlich, subjektiv, zu einem ebensolchen Gesichtspunkt des Fühlens gekommen ist wie wir selbst, der gewisse Feinheiten der Außenwelt durch sein Gefühl so verinnerlichen kann, daß ein von uns unabhängiges und doch mit uns zusammenhängendes Verstänlinis vorhanden ist, dann fühlen wir unser Leben gehoben in solcher Genossenschaft.",
      "Wir müssen unser Fühlen jeder allein in uns entwickeln, aber wir können Menschen finden, mit denen dieses Fühlen zusammenklingen kann. Denn obzwar das fühlende Leben innerlich ist, so ist es doch möglich, daß die Menschen in ihrem Fühlen zusammenklingen.",
      "Zwei Willen, die sich auf ein und dasselbe Objekt richten würden, zwei Menschen also, die in demselben Zeitpunkt ein und dasselbe tun wollen, kann es nicht geben. Die Willen können nicht in ein einziges Objekt zusammen-fließen.",
      "Die Kurbel selbst, die wir angreifen, durch die wir eine Maschine drehen, sie können wir nur allein angreifen. Und selbst wenn der andere uns hilft dabei, so ist der Teil der Mbeit, den wir durch unseren Willen vollbringen, eben die Hälfte der ganzen Arbeit, wir machen unsere Hälfte, der andere die andere Hälfte.",
      "Zwei Willens­impulse können nicht in einem Objekt zusammen sein. Obzwar wir uns in gemeinsame Welten hineinstellen durch unseren Willen, sind wir gerade durch diesen Willen so in die Welt hineingestellt, daß wir jeder eine einzelne Individualität für uns sind durch den Willen.",
      "werden wir gerade dadurch hingewiesen darauf, wie der Wille den ganzen individuellen Wert des Menschen ausmacht, wie der Wille sozusagen von diesem Gesichtspunkt aus das Innerste ist. Wir können daraus entnehmen, daß Wahrnehmung und Gedanke mehr äußerlich sind im Innenleben des Menschen, daß Gefühl und Wille das Tiefste, das eigentlich Innere ausmachen. Aber noch ein anderer Unterschied ergibt sich durch eine ganz äußerliche, exoterische Betrachtungsweise für diese vier Kreise des menschlichen Seelenlebens.",
      "Wenn wir mit unserem Wahrnehmen der Welt gegenüberstehen, dann sagen wir uns doch ganz gewiß: Dieses Wahrnehmen vermittelt uns zwar die Welt, aber nur immer von einem einzelnen Gesichtspunkt aus. Wie klein ist der Ausschnitt der Welt, den wir durch unser Wahr­nehmen zu unserem Innenleben machen können! Wir sind abhängig von Ort und Zeit in diesem Wahrnehmen; wir müssen sagen, das wenigste von dem, was wir erahnen in der Welt, kommt durch unsere Wahrnehmung in unser Innenleben herein. - Und gegenüber unseren Gedanken haben wir das Gefühl: wenn wir uns auch noch so sehr bemühen, es kann immer noch weitere Schritte geben, wir können immer noch weiter dringen durch unsere Gedanken. - Kurz, wir haben die Empfindung: die Welt liegt da draußen und du bemächtigst dich nur eines kleinen Stückes dieser Welt durch dein Wahrnehmen, durch dein Denken.",
      "Anders ist es schon mit dem Fühlen. Mit dem Fühlen ist es so, daß man sich sagt: Oh, was alles wäre eigentlich an Möglichkeiten des Fühlens, an Glücks- und Leidensmöglichkeiten in mir selber! Was könnte ich aus den Tiefen meiner Seele alles heraufholen! Und wenn ich es heraufholte, wie viel feiner, wie viel höher würde ich fühlen über die Dinge der Welt! Während man gegenüber dem Wahrnehmen und Denken die Empfindung hat: da draußen ist viel in der Welt und nur einen kleinen Teil kann man erleben in dem Wahrnehmen und Denken, muß man dem Fühlen gegenüber die Empfindung haben:",
      "da unten sind unendliche Tiefen; würde ich sie heraufbringen, so würde mein Fühlen reicher und immer reicher werden. Ich kann nur den kleinsten Teil heraufbekommen und in mein wirkliches Fühlen verwandeln. Während ich also durch mein Wahrnehmen und Denken",
      "nur einen kleinen Teil der Welt zu meiner Innenwelt machen kann, kann ich durch das Fühlen in die Sphären des wirklichen Erlebens nur einen Teil dessen wirklich zum Dasein bringen, was als Möglich­keiten in mir ruht.",
      "Und in viel höherem Maße ist das beim Willen der Fall. Ich will nur das eine andeuten. Wie sehr müssen wir empfinden, daß wir zurückbleiben mit dem, was wir vollbringen, gegenüber dem was wir tun könnten, was in uns veranlagt ist.",
      "So empfinden wir, daß wir durch unser Wahrnehmen und Denken nur einen Teil der Außenwelt hereinbringen in unser Innenleben, und wir empfinden, daß wir von dem, was da im tiefen Schacht der Seele liegt, nur einen Teil heraufholen können durch unser Fühlen und unser Wollen. Dadurch gliedern sich sozusagen in zwei Partien die vier Kreise unseres Seelenlebens: das Wahrnehmen und Denken auf der einen Seite, das Fühlen und Wollen auf der andern Seite.",
      "Ein noch ganz anderes Licht wird auf diese vier Kreise unseres Innenlebens geworfen, wenn wir das, was sich so der Mensch durch Nachdenken exoterisch klarlegen kann, nun esoterisch zu beleuchten versuchen.",
      "Sie wissen, meine lieben Freunde, in der Nacht, wenn der Mensch schläft, ist in einer gewissen Weise der Züsammenhang zwischen seinem Ich, seinem astralischen Leibe auf der einen Seite und seinem physischen Leibe, seinem Ätherleibe auf der anderen Seite, ein anderer als beim Tagwachen. Beim Tagwachen sind, man möchte sagen in normaler Weise zusammengekoppelt physischer Leib, Ätherleib, astralischer Leib und Ich. Dieser Zusammenhang ist beim Schlafe gelockert, so gelockert, daß aus der Sphäre der Sinne und aus der Sphäre des Denkens, also aus der ganzen Sphäre der Bewußtseins-werkzeuge, der astralische Leib und das Ich heraus sind, und daher die Dunkelheit der Nacht sich zunächst über das normale Bewußtsein ausbreitet: die Bewußtlosigkeit. Wenn nun der Mensch durch seine esoterischen Übungen seine Seele so erstarkt, daß er in der geistig-seelischen Wesenheit, die in der Nacht bewußtlos außerhalb des Leibes ist, erkennend, wahrnehmend, also geistig erkennend und wahrnehmend wird, wenn er das Geistig-Seelische wirklich erlebt als",
      "sein Menschliches außerhalb des Leibes, dann tritt für ihn eine neue Welt auf, eine geistige Umwelt, so wie für den Menschen eine physi­sche Umwelt vorhanden ist, wenn er sich der Sinne und seines Gehirns bedient, das ja dem Denken dient. Diese geistige Umwelt, die man dann betrachten kann, ist durchaus nicht immer dieselbe.",
      "Der Mensch kann sich sozusagen in die Lage des Geistesforschers versetzen zu verschiedenen Zeiten, in verschiedener Weise. Und es wirkt eigentlich immer auf das, was der Mensch geistig sieht, die Absicht mit - aber die nicht eigentlich verstandesmäßige Absicht, sondern die in seinem ganzen Seelenleben mehr unbewußt instinktiv liegende Absicht -: was er eigentlich erkennen will.",
      "Wenn der Mensch zum Beispiel aus seinem Leibe herausgeht, um eine Beziehung zu finden zu einem verstorbenen Menschen, dann wirkt diese Absicht auf sein ganzes geistiges Bewußt-seinsfeld. Er übersieht gleichsam alles, was nicht zu dieser Absicht gehört.",
      "Er steuert, wenn ihm die Sache überhaupt gelingt, auf den Toten los und dessen Geschick, um das zu erkennen, was er an dem Toten eben erschauen will. Die übrige geistige Welt bleibt gleichsam -nun, der Ausdruck ist ungeschickt - unbeachtet, bleibt unaufgehellt, und der Mensch erlebt eben dann nur den Zusammenhang mit dem Toten.",
      "So hängt es von seinen Absichten ab, was der Mensch gerade in der geistigen Welt sieht. Daher ist es begreiflich, daß das, was das heUsichtige Bewußtsein beschreibt von dem, was es in der geistigen Welt gesehen hat, in unendlicher Weise verschieden sein kann bei den verschiedenen heliseherischen Individuen.",
      "Jeder kann ganz richtig gesehen haben, was er eben sehen mußte nach der Tendenz, die in ihm lag, als er sich mit seinem Seelisch-Geistigen aus dem Physisch-Leib­lichen herausgebracht hatte.",
      "Ich will nun heute, und in diesen Vorträgen überhaupt, dasjenige schildern, was das hellseherische Bewußtsein sieht, wenn es sich in die geistige Welt begibt mit der Absicht das menschliche Innenleben zu erkennen, diese vier Seelenkreise des Wahrnehmens, des Denkens, des Fühlens, des Wollens, um dahinter zu kommen, was eigentlich in dieser Menschenseele auf- und abwogt und Glück und Leid dieser Menschenseele bewirkt.",
      "Nehmen wir also an, ein heliseherisches Bewußtsein hätte es dahin",
      "gebracht, mit dem Geistig-Seelischen wirklich aus dem Physisch-Leib­lichen so herauszukommen, wie das der Mensch sonst nur im bewußt­losen Zustande im Schlafe tut, und er vollzieht dieses Herausbewegen mit der entschiedenen Tendenz, mit dem Impuls, des Menschen Innenleben erkennen zu lernen, sich entgegentreten zu fühlen das menschliche Innenleben, dann wird sich ihm das ergeben, was ich zu schildern versuchen werde.",
      "Das Nächste, was da dem hellseherischen Bewußtsein entgegentritt, ist eigentlich eine vollständige Umkehrung alles Weltanschauens. So-lange wir im Leibe sind, schauen wir mit den Sinnen um uns herum, denken mit unserem Verstande. Wir schauen eine Welt von Bergen, Flüssen, Wolken, Sternen und so weiter um uns herum, und an einem Punkte dieser Welt erblicken wir uns dann selber, man möchte sagen als etwas Kleinstes gegenüber dieser großen Welt. Indem das hell­seherische Bewußtsein außer dem Leibe zu wirken beginnt, kehrt sich dieses Verhältnis geradezu um. Die Welt, die sich sonst ausbreitet vor unseren Sinnen, über die wir nachdenken mit unserem an das Gehirn gebundenen Verstand, diese Welt, sie entschwindet der Anschauung, der Wahrnehmung. Sie gibt auch keine Gedanken her, wenn man so sagen will. Aber man fühlt sich wie in diese Welt ausgegossen, man fühlt wirklich, wenn man aus seinem Leibe herausgekommen ist, so, daß dieses Erfühlen in der richtigen Weise ausgesprochen ist, wenn man sagt: Die Welt, die du früher angeschaut hast, in die bist du nun ausgegossen, in der bist du darinnen. Du erfüllst bis zu einer gewissen Grenze den ganzen Raum und du webst selber in der Zeit.",
      "Es ist das eine Empfindung, an die man sich erst gewöhnen muß. Es ist eine Empfindung, die man auch so ausdrücken kann, daß man sagt: Was früher Außenwelt war, ist jetzt Innenwelt geworden. Nicht als ob man diese frühere Außenwelt jetzt im Innern trüge, aber das Gefühl, die Empfindung ist da: Innenwelt ist es geworden. Du lebst in dem Raum, in dem früher deine Sinneswahrnehmungen ausgebreitet waren, über dessen Dinge und Vorgänge du dachtest, da lebst du darinnen. - Und das kleine Wesen, das gleichsam im Mittelpunkt des Sinneshorizontes gestanden hat, der Mensch, das wird, wenn man in einer gewissen Weise das hellseherische Bewußtsein entwickelt,",
      "eigentlich jetzt die Welt. Auf die schauen wir so hin, wie wir früher hingeschaut haben auf die ganze im Raum ausgebreitete und in der Zeit verlaufende Außenwelt. Wir sind uns gewissermaßen Welt ge­worden.",
      "Denken Sie nur, meine lieben Freunde, was das für ein Umkehren des menschlichen Welt-Erschauens ist, wenn das, was früher so gar nicht Welt war, wozu man Ich gesagt hat, wenn das da draußen eigent­lich jetzt die Welt ist, auf die alles hin tendiert. Es ist, wie wenn man von allen Punkten des Raumes nach einem einzigen Mittelpunkte schauen würde - und da sieht man sich selber. Es ist, wie wenn man in der Zeit vor- und rückwärts schwimrnen würde - und an einem Punkte in einer Woge dieses Zeitstromes findet man sich selber. Man ist sich selbst die Welt geworden.",
      "Das ist der erste Eindruck, wenn man, ich sage es ausdrücklich noch einmal, mit dieser Tendenz, das menschliche Innenleben kennen­zulernen, das hellseherische Bewußtsein entfaltet. Dann ist dieses der erste Eindruck. Merkwürdig: Man geht aus dem Leibe heraus mit der Tendenz, das menschliche Innenleben kennen zu lernen, und das erste, was einem entgegentritt, ist die menschliche Gestalt selber. Aber wie verändert ist diese menschliche Gestalt! Man kann das nicht oft genug sagen: Man muß mit der Absicht, das menschliche Innenleben kennen zu lernen, herausgehen aus dem Leibe. Dann tritt das alles ein, was ich jetzt sagen werde. Es braucht deshalb beim Hellsehend-werden natürlich nicht immer einzutreten.",
      "Diese Menschengestalt, wie anders stellt sie sich dar! Man weiß:",
      "das, worauf man hinschaut, das, was man da schaut, das bist du. Ja, du bist es, du, der du dich früher von innen erfühlt hast in deiner Haut, in deinem Blut, du stehst draußen. - Aber man sieht eigentlich von dem, was da steht, zunächst nur, man möchte sagen, die äußere Gestalt, jedoch verwandelt. Die Augen, das, was Auge war, leuchtet gewissermaßen wie zwei Sonnen, aber innerliche, in Lichtglanz vibrierende Sonnen, funkelnde, auffunkelnde und im Funkeln ab­dämmernde Sonnen, die strahliges Licht verbreiten. So erscheinen an der verwandelten Menschengestalt die Augen. Die Ohren beginnen in einer gewissen Weise zu tönen; das, was man in der physischen",
      "Welt von den Ohren sieht, sieht man ja nicht, aber man fühlt ein gewisses Tönen. Die ganze Haut erstrahlt in einer Art von Strahlen, die man mehr erfühlt, als daß rnan sie erschauen könnte. Kurz, die menschliche Gestalt erscheint einem wie ein Leuchtendes, Tönendes, Magnetisch-Elektrisches, Strahlungen Aussendendes. Aber die Aus­drücke sind natürlich ungeschickt, weil sie eben der physischen Welt entnommen sind.",
      "So steht die Welt vor uns. Und das ist nun unsere Welt in dem geschilderten Anfang des heilseherischen Erlebens: der lichterglän­zende Mensch, die ganze Haut in einem fühlbaren Erglänzen, schaubar die Augen, hörbar die Ohren! Und jetzt weiß man, wenn man diesen Eindruck hat: Du hast von außerhalb des Leibes deinen Leib, deinen physischen Leib geschaut. Man weiß: vom Gesichtspunkt des Geistes aus gesehen ist der physische Leib so.",
      "Wenn man dann versucht eine innere Tätigkeit auszuüben da draußen, aber außer dem Leibe, die sich vergleichen läßt mit dem Nachdenken - aber es ist eben etwas anderes als das gewöhnliche Denken, es ist ein Entfalten einer inneren schöpferischen Seelenkraft -, wenn man die entwickelt, so sieht man in diesem Leuchtewesen da drinnen mehr: man sieht da drinnen bewegende Kräfte, die, man möchte sagen wie eine Art von Kraftzirkulation diese Leuchtegestalt durchsetzen. Und jetzt weiß man: Das, was du da drinnen wie eine Art Einschluß in deinem Leuchteleib erschaust, das ist dein Gedanken-leben von außen gesehen. Man kann es nun erkennen als einen Teil des Ätherleibes, den man eben sieht. Man sieht den Ätherleib als das webende Gedankenleben. Es ist wie ein Zirkulieren von dunklen Wellen, eine geistige Blutzirkulation, könnte man sagen: dunkle Wellen in dem Leuchteleib, die dem Ganzen ein eigentümliches An-sehen geben und die einem eben die Erkenntnis aufdrängen: Da welit und wallt in deinem physischen Leib der Ätherleib drinnen, den du jetzt von außen anschaust, der dir jetzt sichtbar wird.",
      "Sehen Sie, so erlangt man außerhalb seines Leibes stehend die Erkenntnis, daß es wirklich den physischen Leib und den Ätherleib gibt, und wie sie aussehen, von außen gesehen.",
      "Nun kann aber das innerliche Erkraften noch weitergehen. Würde",
      "man nämlich nur das erschauen, was ich jetzt angeflihrt habe, dann würde man sich eigentümlich vorkommen in der geistigen Welt. Man würde sich dann so vorkommen wie ein Wesen, das auf dem physi­schen Plane zwar die Eindrücke der Außenwelt empfangen kann, aber innerlich ganz gefühisleer wäre, das gar nichts fühlen könnte.",
      "Aber auch das, was diesem Gefühle des physischen Planes entspricht, das kann innerlich sich nun auferwecken da draußen außer dem Leibe. Es ist dies nicht das Fühlen selbst, denn dieses Fühlen hat nur eine Berechtigung, ist nur vorhanden innerhalb des physischen Leibes; aber es ist das, was innerhalb der geistigen Welt dem Fühlen ent­spricht.",
      "Vorher hat man nämlich bloß empfunden: Du bist in dem Raume darinnen und wogst hin in der Zeit. Du bist in dem Raum, in dem du früher die Vorgänge, die Wesenheiten gesehen hast, und in der Zeit, in der du wahrgenommen hast: da bist du darinnen.",
      "Wenn aber das dem Fühlen entsprechende innere Seelentum nun da draußen außer dem Leibe auferweckt wird, dann beginnt dieses Seelische ein Wissen zu entfalten, wodurch allerlei aufleuchtet da draußen, wodurch man nicht nur sich fühlt wie über den Raum verbreitet, sondern wodurch man etwas wahrnimmt, was in diesem Raume darinnen ist, was in diesem Zeitenstrom als Wesen wogt. Und man findet jetzt nicht das, was man früher durch den Leib und seine Organe schauend in der Außenwelt gesehen hat, sondern man findet sich erlebend in dem Innern dieser Außenwelt, in dem Geistigen, das diese Außenwelt durchwallt und durchwogt.",
      "Es ist, wie wenn der Raum, in dem man sich früher nur gefühlt hätte, nun von unzähligen Sternen angefüllt würde, die sich alle bewegen und zu denen man selber gehört. Und jetzt weiß man: Du erlebst dich in deinem astralischen Leib.",
      "Man er­lebt sich so in seinem astralischen Leib außerhalb des physischen Leibes, daß auflebt inhaltlich das, worin man sich früher nur fühlte.",
      "Wenn man jetzt zurückschaut auf das, was man früher von sich selbst gesehen hat, was vorhin sozusagen als die Außenwelt geschildert worden ist, auf diesen Leuchteleib mit der dunklen Gedankenzirkula­tion des Ätherleibes darinnen, dann erscheint einem in dem Augen­blick, wo man sich außer dem Leibe eben auf das Astrale, auf das Sternenleben des astralischen Leibes konzentriert, das was man verlassen",
      "hat, der verlassene Leib, anders. Und man kann nun genau den Unterschied merken, der durch Folgendes ausgedrückt werden kann: Du kannst dich konzentrieren auf dich zurück, dann siehst du deinen Leuchteleib und deinen Gedankenätherleib. Kannst du dich aber so auf dich selbst konzentrieren, daß eine innere Sternenwelt, von der du weißt: du füllst sie aus, sich in dir auslebt, und du schaust nun zurück auf deinen physischen Leib, den du verlassen hast, dann kann das Leuchten aufhören, dann hört die Gedankenzirkulation au£ Es ist das in gewisser Weise willkürlich zu machen, aber es tritt an die Stelle dessen ein Bild unserer eigenen Wesenheit, das uns erscheint -ja es kann nicht anders gesagt werden - als unser personifiziertes Karma. Dasjenige in uns, was wir als Menschen in uns tragen, wes­wegen wir uns dieses oder jenes Schicksal bereiten, das ist wie zu­sammengerollt. Unser Karma, unser Schicksal, personifiziert, steht vor uns. Und wir wissen, wenn wir dieses nun anschauen: Das bist du, aber so, wie du eigentlich in deiner moralischen inneren Wesenheit bist. Das bist du so wie du darinnen stehst in der Welt als eine Indi­vidualität; das bist du ganz selbst.",
      "Noch ein anderes Bewußtsein tritt auf. Dieses Bewußtsein, das da noch hinzukommt, hat etwas sehr Bedrückendes. Man erblickt nämlich dieses ganz personifizierte Schicksal so, daß man es im innersten Zusammenhang mit seiner Leiblichkeit, mit seinem Erdenmenschen erfühlt. Und zwar so, daß man die unmittelbare Erkenntnis hat: Wie in deinem Erdenleibe deine Muskeln aufgebaut sind, wie dein ganzes Muskelsystem ist, ist es eine Schöpfung dieses deines Schicksals, deines Karmas. Jetzt kommt dann die Zeit, wo man sich sagt: Wie verschie­den ist manchmal die Maja von der Wahrheit. Da glauben wir, solange wir auf dem physischen Plane stehen, dieser Muskelmensch bestehe eben aus den fleischigen Muskeln: in Wahrheit sind diese Fleisches-muskeln das kristallisierte Karma. Und sie sind so gestaltet im Men­schen, so kristallisiert, daß der Mensch bis auf die feinste chemische Zusammensetzung hinein in seinem Muskelsystem sein kristallisiertes Karma trägt. So sehr trägt er es, daß sich nun der geistige Erschauer ganz klar wird darüber: Wenn ein Mensch zum Beispiel seine Muskeln so bewegt hat, daß er sich auf eine Stätte begeben hat, auf der ihm ein",
      "Unglück geschehen ist, so ist das aus dem Grunde geschehen, weil in den Muskeln die geistige Kraft darinnen lag, die ihn aus sich selbst heraus an die Stätte getrieben hat, an der ihm das Unglück passierte. Die Weltenordnung hat unser Schicksal kristallisiert in unserem Muskelsystem. Und in unserem Muskelsystem lebt der Geist, für den äußeren physischen Plan kristallisiert, der ohne unser offenbares Wissen uns überall dahin führt, wohin wir eben in Gemäßheit unseres Karmas gehen müssen, kommen müssen.",
      "Wenn diese innere Erkraftung noch weiter geht, wenn der Mensch außer seinem Leibe sozusagen sein Inneres weiter erlebt, dann tritt in ihm dasjenige auf, was sonst im physischen Leben, auf dem physi­schen Plane dem Willensimpuis entspricht. Sobald dieses Willens-leben innerlich auftaucht - aber außer dem Leibe - da fühlt sich der Mensch nicht nur wie in einem Sternensystem darinnen, sondern er fühlt sich wie in der Sonne dieses Sternensystems darinnen, er weiß sich eins mit der Sonne seines Plantensystems. Man möchte sagen:",
      "Wenn man seinen astralischen Leib innerlich erlebt, weiß man sich eins mit den Planeten seines Plantensystems; wenn man sich mit seinem Ich außer dem Leibe erlebt, weiß man sich eins mit der Sonne seines Sternensystems, auf die alles hingerichtet ist, auf die alles hin-tendiert.",
      "Wenn man jetzt zurückschaut auf das, was nun nicht innen, sondern außen ist - denn das, was außen ist, solange man im physischen Leibe ist, das ist, wenn man außer dem Leibe ist, innen. Und das, was innen ist, wenn man im physischen Leibe ist, das ist, wenn man außer dem Leibe ist, außen -, wenn man also jetzt auf sich selber zurückschaut, dann tritt einem ein anderes entgegen, dann tritt einem die Notwendig­keit entgegen im Hinblicken auf sich selbst, daß das, was da draußen in der physischen Welt als die eigene Leiblichkeit sich befindet, ent­stehen mußte und vergehen muß: Entstehen und Vergehen des physischen Leibes tritt einem entgegen. Man wird gleichsam gewahr, wie geistige Mächte und Wesenheiten vorhanden sind, die da die Entstehung dieses physischen Leibes lenken und leiten, und wie andere wieder da sind, die ihn abbauen, diesen physischen Leib. Und man wird sich bewußt, worin sich dieses eigentliche Entstehen und Vergehen",
      "in der physischen Welt wiederum kristallisiert. Denn man weiß: dieses Entstehen und Vergehen ist im Grunde genommen an das Knochensystem des Menschen gebunden. Mit dem Einbauen des Knochensystems in den menschlichen physischen Leib ist sozusagen über die Form, in der der Mensch Geburt und Tod in der physischen Welt erlebt, das Urteil gesprochen. Wie das Knochensystem einkristallisiert ist in den Menschen, so ist durch diese Formung be­stimmt, wie der Mensch als Wesen entsteht und vergeht. Man weiß: Du könntest im physischen Dasein nicht das Wesen sein, das du bist, wenn nicht die ganze Welt zusammengewirkt hätte, um innerhalb deines physischen Daseins deine physische Natur so zu verhärten, daß es als Knochensystem dir entgegentritt. Und man lernt verehren im Knochensystem, so sonderbar das auch klingt, die waltenden Universalweltenmächte, die ihren geistigen Ausdruck in all jenen Wesen finden, die im Sonnenleben konzentriert sind. Man lernt gleichsam erkennen, wie hineingezeichnet worden ist in die Welten-ordnung der Grundplan des Menschen, dieses sein Knochensystem, und wie das andere, was seine physischen Organe sind, gleichsam daran aufgehängt worden ist.",
      "So endet das hellseherische Anschauen dessen, was jetzt Außenwelt wird, mit der Anschauung des Symbols des Todes, man möchte sagen, mit der Anschauung des Knochenmenschen von außen. Denn man gelangt durch diese hellseherischen Vorgänge zuletzt zu der Erkennt­nis, wie die geistigen Welten sich gleichsam ein physisches äußeres Symbol erbildet haben, diese geistige Welten, denen man mit seinem Innern in Wahrheit angehört, und in die man sich gestellt hat, indem man außerhalb seines Leibes gegangen ist. Man lernt sich mit seinem Wesen außer seinem Leibe kennen. Und jetzt lernt man auch erkennen, gerade bei diesem vierten Stadium: Wenn wir in der Welt unsere Handlungen vollziehen, wenn wir unseren Willen entfalten, dann ist das die Kraft in uns, die unbewußt auf dem physischen Plan wirkt, die wir eigentlich erst jetzt kennen: Wenn wir nur einfach vorwärts gehen und uns zu dieser Vorwärtsbewegung der Mechanik unseres Knochensystems bedienen, so wirken in diesem Vorgang des Gehens universelle, kosmische Kräfte mit, Kräfte, in denen wir erst dann",
      "wirklich darinnen sind, wenn wir uns also auf der vierten Stufe außer­halb unseres Leibes erleben.",
      "Denken Sie einmal, meine lieben Freunde: der Mensch macht einen Spaziergang und er bewegt mit Hilfe der Knochennechanik seine Glieder vorwärts; er denkt, daß er das zu seinem Vergnügen mache. Daß das geschehen kann, daß es Kräfte gibt, durch die wir uns vor­wärts bewegen können mit unserer Knochenmechanik, dazu mußte die ganze Welt da sein, und die ganze Welt von göttlich-geistigen Kräften durchwellt sein, von göttlich-geistigen Kräften, von denen wir erst ein Wissen bekommen, wenn wir uns auf dieser vierten Stufe befinden. In jedem unserer Schritte lebt der göttlich-geistige Kosmos mit, und während wir glauben, daß wir es sind, die unsere Füße vorwärtssetzen, könnten wir das nicht, wenn wir nicht lebten in dem geistigen Kosmos, in der göttlichen Welt.",
      "Wir richten, solange wir im physischen Leibe sind, unsere Blicke rings um uns herum. Da sehen wir die Wesen des mineralischen, des pflanzlichen, des tierischen Reiches, sehen Berge, Flüsse, Meere, Seen, Wolken, sehen Sterne, Sonne, Mond; was wir da äußerlich sehen, hat ein Inneres, und in dieses Innere treten wir selber ein, wenn wir in der geschilderten Weise außerhalb unseres Leibes leben. Wenn wir da drinnen leben, wissen wir: Was in ihnen geistig ist, was sich ver­birgt hinter der strahlenden Sonne, hinter den glänzenden Sternen, hinter den Bergen, Flüssen, Meeren, Seen, Wolken, das lebt in unserer Knochenmechanik, wenn wir sie bewegen, und das muß alles da sein. Dann fassen wir auch mehr Verständnis für das, was vorangegangen ist. So wie unser Wille mit unserer Knochermechanik im innigen Zusammenhange steht, stehen unsere Gefühle im innigen Zusammen­hang mit unserem Muskelsystem; dieses Muskelsystem ist ein sym­bolischer Ausdruck für unser Gefühlssystem. So wie unsere Muskeln gebaut sind, so wie unsere Muskeln uns gestatten, sich zu verkürzen und zu verlängern, um dadurch wiederum die Knochenmechanik hervorzurufen, so ist dazu das Planetensystem notwendig, das wir erkunden, wenn wir uns in unserem astralischen Leib befinden. In unserem Muskelsystem lebt das ganze Planetensystem, wie der ganze Kosmos in unserer Knochenmechanik. Was in entsprechender Weise",
      "über die Gedanken und Sinnesempfindungen zu sagen ist, wird noch in den folgenden Vorträgen kommen.",
      "Solche Dinge liefert die geistige Erkenntnis. Wir sehen daraus, daß diese geistige Erkenntnis wahrhaftig nicht bloß etwas ist, was uns Gedanken und Ideen gibt, sondern was uns in unserer ganzen Seele durchdringen kann, so daß wir uns dadurch wirklich selbst erkennen lernen, daß wir ein anderer Mensch werden in unserem ganzen Er­fühlen und Denken. Denn - wenn man das, was jetzt auseinander­gesetzt worden ist als die Erfahrung des heliseherischen Bewußtseins, auf sein Gemüt wirken läßt und zusammendrängt in eine Grund­lebensempfindung der Seele - wie läßt sich dann diese Grundlebens­empfindung der Seele ausdrücken? Wie muß man sagen, wenn man mit einem kurzen Worte das bezeichnen will, was als ein inneres Lebensgefühl in uns angefacht ist durch ein solches Wissen der hell­seherischen Forschung?",
      "Man schaut hin auf das, was scheinbar das Alltäglichste ist, was der Ausdruck unserer alltäglichsten Launen ist, und man bekommt etwas wie einen Eindruck von dem, was Sie in den ersten Sätzen der «Prüfung der Seele» durch den Mund des Capesius und des Benedik­tus geschildert finden: wie im Menschen gleichsam zusammenrinnen die Ziele, die sich die göttlich-geistigen Wesen gesetzt haben, wie hinein­fließt in das, was Menschennatur ist, dasjenige, was göttlich-geistige Wesen durch die Welten hindurch gedacht haben. Und nun will man das zusammenfassen in einer Lebensempfindung: man schaut anders auf die ganze Menschennatur hin als vorher, man weiß jetzt diese menschliche Natur ganz anders von dem göttlichen Kosmos durch­drungen als vorher. Und das Bewußtsein davon entflammt sich, er­starkt sich, erkraftet sich und sagt mit innerem Gemüts- und Gefühls­verständnis: Will man den Menschen verstehen, so kann man es nicht anders als dadurch, daß man wissen lernt: Aus dem Göttlich-Geistigen heraus ist dieser ganze Mensch!",
      "Wenn wir ihn anschauen, wie sein Fühlen hineinfließt in seine Muskeltätigkeit, wie Göttlich-Geistiges, Kosmisches hineinfließt in seine Knochen, wie die ganze Welt lebt in der Bewegung seiner Knochen, wie das ganze Planetensystem lebt in dem Zusammenziehen",
      "und Ausdehnen und Erschlaffen der Muskeln, wenn man das durch­denkt und durchfühlt, dann sagt man mit vollem Verständnis: Ja, aus dem Göttlichen ist dieser Mensch geboren.",
      "Ex deo nascimur."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Dieser Vortragszyklus wird das Ziel haben, das menschliche Innenleben zu schildern im Zusammenhang mit dem Leben zwischen dem Tod und einer neuen Geburt, um zu zeigen, wie inrüg diese beiden Gebiete des Daseins zusammenhängen.",
        "Und er wird daneben das Ziel haben, Richtlinien zu entwickeln aus der Erkenntnis des Angedeuteten heraus, die den Menschen wirklich orientieren können in manchen schwierigen Lebensiagen, die geeignet sind, in mancher Beziehung einen sicheren Halt des Seelenlebens durch ein gewissermaßen gründ­liches Verständnis dieses Seelenlebens zu geben.",
        "Dazu wird notwendig sein, daß Sie sich, meine lieben anthroposophischen Freunde, durch die ersten Vorträge, die ein Fundament, eine Grundiage aufrichten sollen, hindurcharbeiten; sie werden in esoterisch wissenschaftliche Gebiete führen, die vielleicht manchem zunächst abgelegen scheinen könnten, weit weg von dem, was das menschliche Gemüt gerne un­mittelbar ergreifen möchte.",
        "Aber wenn wir zu dem gelangen werden, worin diese Vorträge eigentlich ihr Ziel erblicken, dann werden Sie sehen, daß dieses Ziel in einer sicheren Form doch nur zu erreichen ist, wenn man sich zuerst durch die scheinbar entlegenen esoterischen Erkenntnisse, die geboten werden sollen, hindurcharbeitet."
      ],
      [
        "Wenn man das menschliche Innenleben zunächst abstrakt betrachtet, so tritt es einem in drei Formen entgegen, auf die wir oftmals auf­merksam gemacht haben: in den Formen des Denkens, des Fühlens und des Wollens; aber um dieses Innenleben vollständig zu betrachten, muß man noch ein Viertes dazurechnen.",
        "Eigentlich gehören nicht nur diese drei genannten Gebiete zum Innenleben des Menschen, sondern es gehört auch schon das dazu, was er aus der bloßen Sinnesempfin-dung macht.",
        "Wir lassen ja Farben und Töne, Wärmeeindrücke und dergleichen nicht nur vor unserem Bewußtsein vorüberhuschen, sondern wir fassen diese Eindrücke auf, wir machen sie zu unseren Wahrnehmungen.",
        "Und die Tatsache, daß wir uns an diese Eindrücke"
      ],
      [
        "erinnern können, daß wir sie behalten können, daß wir nicht nur dann wissen: eine Rose ist rot, wenn wir der Rose unmittelbar gegen­überstehen, sondern daß wir sozusagen die Röte der Rose mit uns herumtragen können, die Farben als eine Erinnerungsvorstellung be­wahren können, das bezeugt uns, daß das Empfindungsleben, das Wahrnehmungsleben, durch das wir uns mit der Außenwelt in Be­rührung bringen, auch schon zu unserem Innenleben gehört.",
        "So daß wir sagen können: Zu unserem Innenleben müssen wir zählen die Wahrnehmung der Außenwelt, insofern wir sie eben im Wahrnehmen selber verinnerlichen.",
        "Ferner müssen wir die Gedankenwelt dazuzählen, durch die wir uns zunächst Erkenntnisse verschaffen von dem Nächstliegenden und in der Wissenschaft von dem Fernerliegenden, durch die wir in einem viel weiteren Sinn noch als durch die Wahr­nehmung der Außenwelt zu unserer Innenwelt machen.",
        "Wir leben ja nicht nur in unseren Wahrnehmungen, wir denken über sie nach und haben das Bewußtsein, daß wir durch unser Nachdenken etwas über die Geheimnisse des Wahrgenommenen erfahren können."
      ],
      [
        "Wir müssen dann zu unserem Innenleben rechnen unsere Gefühle, und wir sind mit den Gefühlen sogleich in demjenigen Gebiete des menschlichen Innenlebens, das sozusagen in sich alles einschließt, was uns als Menschen selbst mit der Welt in eine der Menschenwürde entsprechende Berührung bringt.",
        "Daß wir über die Dinge fühlen können, daß wir uns freuen können an der Umgebung, das ist ja erst die Grundiage unseres wahren Menschendaseins, in gewisser Bezie­hung auch alles das, was unser Glück und unser Leid ausmacht.",
        "Es spielt sich ja das alles ab in auf- und abwogenden Gefühlen: Gefühle, die unser Leben erhöhen, drängen sich herauf oder heran an uns, erstarken, in denen wir uns glücklich und zufrieden finden.",
        "Andere Gefühle drängen sich heran durch die Ereignisse des Lebens, durch unser Schicksal, auch durch unser Innenleben, die unser Leid, unseren Schmerz bedeuten.",
        "Und indem man das Wort «Gefühl» ausspricht, deutet man auf das Gebiet hin, das in der Tat eben Glück und Leid des Menschenlebens einschließt."
      ],
      [
        "Wenn man auf das Vierte hinweist, auf den Willen, so handelt es sich um etwas, was uns wiederum wertvoll für die Welt macht, was"
      ],
      [
        "uns soin die Welt hineinstellt, daß wir nicht nur erkennend, nicht nur in uns fühlend für uns leben, sondern daß wir auf die Welt zurück-wirken können.",
        "Was ein Mensch will, wollen kann, und was vom Willen in die Handlungen ausfließt, das bildet seinen Wert für die Welt.",
        "Wir können uns also sagen: Indem wir auf das Gebiet des Willens hinweisen, haben wir es mit jenem Elemente zu tun, das uns den Menschen als ein Glied der Welt zeigt, und es ist unser Innenleben, das da als ein Glied in die Welt einfließt.",
        "Ob es die egoistischen, die sozial feindlichen Affekte und Leidenschaften der verbrecherischen Naturen sind, die in den Willen einfließen und von da aus Glied der Welt werden zum Verderben der Welt, oder ob es die hohen reinen Ideale sind, die der Idealist herunterholt aus seiner Berührung mit einer geistigen Weltenordnung und einffießen läßt in sein Handeln, einfließen läßt vielleicht nur in Worte, welche, anfeuernd oder auch Menschenwürde zeigend, auf die Menschen wirken; immer haben wir es auf dem Gebiete des Willens mit dem zu tun, was dem Menschen seinen Wert gibt.",
        "So daß der ganze Reichtum, den der Mensch eigent­lich als Seelenwesen haben kann, sich ausdrückt, wenn man diese vier Gebiete nennt: Wahrnehmung, Denken, Fühlen, Wollen."
      ],
      [
        "Für denjenigen, der nun etwas tiefer eingeht auf eine Betrachtung dieser vier, man möchte sagen inneren Sphären der menschlichen Seelennatur, zeigt sich ein bedeutungsvoller Unterschied zwischen zwei und zwei Gliedern dieser viergliedrigen menschlichen Wesenheit.",
        "Aber im gewöhnlichen Leben kommt dieser Unterschied eigentlich den Menschen nicht so sehr zum Bewußtsein, er kommt höchstens zum Bewußtsein, wenn wir in der folgenden Weise über diese vier Sphären der Menschennatur nachdenken."
      ],
      [
        "Wenn wir von der Wahrnehmung sprechen und über sie nachden­ken, so können wir die Empfindung haben: mit der Wahrnehmung stehen wir unmittelbar in einer gewissen Beziehung zur Außenwelt.",
        "Wir verinnerlichen durch die Wahrnehmung die Außenwelt, sie liefert etwas, was dann zu unserem Innern gehört, wenn wir die Empfindung verarbeiten.",
        "Aber wir haben das Gefühl: wir müssen unsere Empfin­dung so eingerichtet haben, daß sie uns in gewisser Beziehung treue Abbilder der Außenwelt gibt.",
        "Und jede Erkrankung des Wahrnehmungs-, des Empfindungslebens,"
      ],
      [
        "jede Erkrankung der Sinne weist uns ja darauf hin, daß durch eine solche Erkrankung unser Innenleben verarmt, dadurch verarmt, daß wir eben ärrner werden an dem, was wir von der Außenwelt in uns hereinbekommen können."
      ],
      [
        "Gehen wir von dem Wahrnehmen zum Denken über, dann können wir gewahr werden, daß wir auch gegenüber dem Denken die Empfindung haben: es kann uns nicht genügen, wenn dieses Denken bloß in sich selber wühlt und sich in sich ergeht.",
        "Die Gedanken haben letzten Endes doch nur einen Wert, wenn sie uns etwas Objektives, außer uns Befindliches in uns vergegenwärtigen, wenn sie Aufschluß zu bringen vermögen von etwas, was außer uns ist.",
        "Unser Nach­denken könnte uns nicht befriedigen, wenn wir durch dieses Nach­denken nicht etwas erfahren könnten über die Außenwelt."
      ],
      [
        "Wenn wir aber zu unserem Gefühle vorschreiten und ein wenig über dieses Gefühl nachdenken, dann werden wir finden, daß dieses Gefühl, oder besser gesagt das Gefühlsleben, viel inniger zusammen­hängt mit unserem unmittelbaren Innensein als Denken und Wahr­nehmen.",
        "Wir haben die Vorstellung, daß wir uns selber, zunächst rein äusserlich, auf dem physischen Plan entwickeln müssen, wenn wir gewisse Feinheiten der Außenwelt in richtiger Weise empfinden wollen, fühlen wollen.",
        "Haben wir einen Gedanken und nennen wir den Gedanken wahr, so sagen wir von einem solchen wahren Ge­danken: er muß eigentlich für alle unsere Mitmenschen gelten, und es muß, wenn wir nur die richtigen Worte finden den Gedanken auszu­drücken, die Möglichkeit geben, von diesem Gedanken auch andere zu überzeugen.",
        "Wenn wir einer Naturerscheinung oder aber, sagen wir, einer menschlichen Kunstschöpfung gegenüberstehen und unser Gefühl daran entwickeln, so wissen wir, daß im Grunde genommen zunächst unsere Menschennatur, so wie sie ist, uns nichts hilft, um gleichsam völlig auszuschöpfen, was uns da entgegentreten kann.",
        "Es könnte sein, daß wir völlig stumpf bei einer musikalischen oder bei einer malerischen Schöpfung bleiben, einfach weil wir unser Gefühl nicht so erzogen haben, daß wir die Feinheiten wahrnehmen können.",
        "Und wenn wir diesen Gedankengang verfolgen, dann finden wir, daß dieses Gefühlsleben etwas sehr Innerliches ist, daß wir es auch so,"
      ],
      [
        "wie wir es innerlich erleben, nicht gleich in Gedanken übertragen können auf andere Menschen.",
        "Wir sind in unserem Gefühlsleben unter allen Umständen in gewissem Sinne allein, aber wir wissen gleichzeitig, daß dieses Gefühlsleben die Quelle eines ganz besonderen inneren Reichtums, einer inneren Entwickelungs-Tatsache gerade dadurch ist, daß es etwas so Subjektives ist, daß es nicht unmittelbar so ins Objekt hinausfließen kann, wie es innerlich lebt."
      ],
      [
        "Ein Gleiches müssen wir sagen in bezug auf den Willen.",
        "Wie sind wir Menschen doch verschieden in bezug auf das, was wir wollen können, auf das, was durch den Willen in unsere Handlungen hinaus­fließen kann!"
      ],
      [
        "Nur dadurch kommt ja eigentlich die Mannigfaltigkeit des menschlichen Handelns zustande, daß der eine dies, der andere jenes wollen kann.",
        "Wenn wir beim Gefühl uns freuen können, daß wir etwa einen Genossen im Leben finden, der rein innerlich, subjektiv, zu einem ebensolchen Gesichtspunkt des Fühlens gekommen ist wie wir selbst, der gewisse Feinheiten der Außenwelt durch sein Gefühl so verinnerlichen kann, daß ein von uns unabhängiges und doch mit uns zusammenhängendes Verstänlinis vorhanden ist, dann fühlen wir unser Leben gehoben in solcher Genossenschaft."
      ],
      [
        "Wir müssen unser Fühlen jeder allein in uns entwickeln, aber wir können Menschen finden, mit denen dieses Fühlen zusammenklingen kann.",
        "Denn obzwar das fühlende Leben innerlich ist, so ist es doch möglich, daß die Menschen in ihrem Fühlen zusammenklingen."
      ],
      [
        "Zwei Willen, die sich auf ein und dasselbe Objekt richten würden, zwei Menschen also, die in demselben Zeitpunkt ein und dasselbe tun wollen, kann es nicht geben.",
        "Die Willen können nicht in ein einziges Objekt zusammen-fließen."
      ],
      [
        "Die Kurbel selbst, die wir angreifen, durch die wir eine Maschine drehen, sie können wir nur allein angreifen.",
        "Und selbst wenn der andere uns hilft dabei, so ist der Teil der Mbeit, den wir durch unseren Willen vollbringen, eben die Hälfte der ganzen Arbeit, wir machen unsere Hälfte, der andere die andere Hälfte."
      ],
      [
        "Zwei Willens­impulse können nicht in einem Objekt zusammen sein.",
        "Obzwar wir uns in gemeinsame Welten hineinstellen durch unseren Willen, sind wir gerade durch diesen Willen so in die Welt hineingestellt, daß wir jeder eine einzelne Individualität für uns sind durch den Willen."
      ],
      [
        "werden wir gerade dadurch hingewiesen darauf, wie der Wille den ganzen individuellen Wert des Menschen ausmacht, wie der Wille sozusagen von diesem Gesichtspunkt aus das Innerste ist.",
        "Wir können daraus entnehmen, daß Wahrnehmung und Gedanke mehr äußerlich sind im Innenleben des Menschen, daß Gefühl und Wille das Tiefste, das eigentlich Innere ausmachen.",
        "Aber noch ein anderer Unterschied ergibt sich durch eine ganz äußerliche, exoterische Betrachtungsweise für diese vier Kreise des menschlichen Seelenlebens."
      ],
      [
        "Wenn wir mit unserem Wahrnehmen der Welt gegenüberstehen, dann sagen wir uns doch ganz gewiß: Dieses Wahrnehmen vermittelt uns zwar die Welt, aber nur immer von einem einzelnen Gesichtspunkt aus.",
        "Wie klein ist der Ausschnitt der Welt, den wir durch unser Wahr­nehmen zu unserem Innenleben machen können!",
        "Wir sind abhängig von Ort und Zeit in diesem Wahrnehmen; wir müssen sagen, das wenigste von dem, was wir erahnen in der Welt, kommt durch unsere Wahrnehmung in unser Innenleben herein. - Und gegenüber unseren Gedanken haben wir das Gefühl: wenn wir uns auch noch so sehr bemühen, es kann immer noch weitere Schritte geben, wir können immer noch weiter dringen durch unsere Gedanken. - Kurz, wir haben die Empfindung: die Welt liegt da draußen und du bemächtigst dich nur eines kleinen Stückes dieser Welt durch dein Wahrnehmen, durch dein Denken."
      ],
      [
        "Anders ist es schon mit dem Fühlen.",
        "Mit dem Fühlen ist es so, daß man sich sagt: Oh, was alles wäre eigentlich an Möglichkeiten des Fühlens, an Glücks- und Leidensmöglichkeiten in mir selber!",
        "Was könnte ich aus den Tiefen meiner Seele alles heraufholen!",
        "Und wenn ich es heraufholte, wie viel feiner, wie viel höher würde ich fühlen über die Dinge der Welt!",
        "Während man gegenüber dem Wahrnehmen und Denken die Empfindung hat: da draußen ist viel in der Welt und nur einen kleinen Teil kann man erleben in dem Wahrnehmen und Denken, muß man dem Fühlen gegenüber die Empfindung haben:"
      ],
      [
        "da unten sind unendliche Tiefen; würde ich sie heraufbringen, so würde mein Fühlen reicher und immer reicher werden.",
        "Ich kann nur den kleinsten Teil heraufbekommen und in mein wirkliches Fühlen verwandeln.",
        "Während ich also durch mein Wahrnehmen und Denken"
      ],
      [
        "nur einen kleinen Teil der Welt zu meiner Innenwelt machen kann, kann ich durch das Fühlen in die Sphären des wirklichen Erlebens nur einen Teil dessen wirklich zum Dasein bringen, was als Möglich­keiten in mir ruht."
      ],
      [
        "Und in viel höherem Maße ist das beim Willen der Fall.",
        "Ich will nur das eine andeuten.",
        "Wie sehr müssen wir empfinden, daß wir zurückbleiben mit dem, was wir vollbringen, gegenüber dem was wir tun könnten, was in uns veranlagt ist."
      ],
      [
        "So empfinden wir, daß wir durch unser Wahrnehmen und Denken nur einen Teil der Außenwelt hereinbringen in unser Innenleben, und wir empfinden, daß wir von dem, was da im tiefen Schacht der Seele liegt, nur einen Teil heraufholen können durch unser Fühlen und unser Wollen.",
        "Dadurch gliedern sich sozusagen in zwei Partien die vier Kreise unseres Seelenlebens: das Wahrnehmen und Denken auf der einen Seite, das Fühlen und Wollen auf der andern Seite."
      ],
      [
        "Ein noch ganz anderes Licht wird auf diese vier Kreise unseres Innenlebens geworfen, wenn wir das, was sich so der Mensch durch Nachdenken exoterisch klarlegen kann, nun esoterisch zu beleuchten versuchen."
      ],
      [
        "Sie wissen, meine lieben Freunde, in der Nacht, wenn der Mensch schläft, ist in einer gewissen Weise der Züsammenhang zwischen seinem Ich, seinem astralischen Leibe auf der einen Seite und seinem physischen Leibe, seinem Ätherleibe auf der anderen Seite, ein anderer als beim Tagwachen.",
        "Beim Tagwachen sind, man möchte sagen in normaler Weise zusammengekoppelt physischer Leib, Ätherleib, astralischer Leib und Ich.",
        "Dieser Zusammenhang ist beim Schlafe gelockert, so gelockert, daß aus der Sphäre der Sinne und aus der Sphäre des Denkens, also aus der ganzen Sphäre der Bewußtseins-werkzeuge, der astralische Leib und das Ich heraus sind, und daher die Dunkelheit der Nacht sich zunächst über das normale Bewußtsein ausbreitet: die Bewußtlosigkeit.",
        "Wenn nun der Mensch durch seine esoterischen Übungen seine Seele so erstarkt, daß er in der geistig-seelischen Wesenheit, die in der Nacht bewußtlos außerhalb des Leibes ist, erkennend, wahrnehmend, also geistig erkennend und wahrnehmend wird, wenn er das Geistig-Seelische wirklich erlebt als"
      ],
      [
        "sein Menschliches außerhalb des Leibes, dann tritt für ihn eine neue Welt auf, eine geistige Umwelt, so wie für den Menschen eine physi­sche Umwelt vorhanden ist, wenn er sich der Sinne und seines Gehirns bedient, das ja dem Denken dient.",
        "Diese geistige Umwelt, die man dann betrachten kann, ist durchaus nicht immer dieselbe."
      ],
      [
        "Der Mensch kann sich sozusagen in die Lage des Geistesforschers versetzen zu verschiedenen Zeiten, in verschiedener Weise.",
        "Und es wirkt eigentlich immer auf das, was der Mensch geistig sieht, die Absicht mit - aber die nicht eigentlich verstandesmäßige Absicht, sondern die in seinem ganzen Seelenleben mehr unbewußt instinktiv liegende Absicht -: was er eigentlich erkennen will."
      ],
      [
        "Wenn der Mensch zum Beispiel aus seinem Leibe herausgeht, um eine Beziehung zu finden zu einem verstorbenen Menschen, dann wirkt diese Absicht auf sein ganzes geistiges Bewußt-seinsfeld.",
        "Er übersieht gleichsam alles, was nicht zu dieser Absicht gehört."
      ],
      [
        "Er steuert, wenn ihm die Sache überhaupt gelingt, auf den Toten los und dessen Geschick, um das zu erkennen, was er an dem Toten eben erschauen will.",
        "Die übrige geistige Welt bleibt gleichsam -nun, der Ausdruck ist ungeschickt - unbeachtet, bleibt unaufgehellt, und der Mensch erlebt eben dann nur den Zusammenhang mit dem Toten."
      ],
      [
        "So hängt es von seinen Absichten ab, was der Mensch gerade in der geistigen Welt sieht.",
        "Daher ist es begreiflich, daß das, was das heUsichtige Bewußtsein beschreibt von dem, was es in der geistigen Welt gesehen hat, in unendlicher Weise verschieden sein kann bei den verschiedenen heliseherischen Individuen."
      ],
      [
        "Jeder kann ganz richtig gesehen haben, was er eben sehen mußte nach der Tendenz, die in ihm lag, als er sich mit seinem Seelisch-Geistigen aus dem Physisch-Leib­lichen herausgebracht hatte."
      ],
      [
        "Ich will nun heute, und in diesen Vorträgen überhaupt, dasjenige schildern, was das hellseherische Bewußtsein sieht, wenn es sich in die geistige Welt begibt mit der Absicht das menschliche Innenleben zu erkennen, diese vier Seelenkreise des Wahrnehmens, des Denkens, des Fühlens, des Wollens, um dahinter zu kommen, was eigentlich in dieser Menschenseele auf- und abwogt und Glück und Leid dieser Menschenseele bewirkt."
      ],
      [
        "Nehmen wir also an, ein heliseherisches Bewußtsein hätte es dahin"
      ],
      [
        "gebracht, mit dem Geistig-Seelischen wirklich aus dem Physisch-Leib­lichen so herauszukommen, wie das der Mensch sonst nur im bewußt­losen Zustande im Schlafe tut, und er vollzieht dieses Herausbewegen mit der entschiedenen Tendenz, mit dem Impuls, des Menschen Innenleben erkennen zu lernen, sich entgegentreten zu fühlen das menschliche Innenleben, dann wird sich ihm das ergeben, was ich zu schildern versuchen werde."
      ],
      [
        "Das Nächste, was da dem hellseherischen Bewußtsein entgegentritt, ist eigentlich eine vollständige Umkehrung alles Weltanschauens.",
        "So-lange wir im Leibe sind, schauen wir mit den Sinnen um uns herum, denken mit unserem Verstande.",
        "Wir schauen eine Welt von Bergen, Flüssen, Wolken, Sternen und so weiter um uns herum, und an einem Punkte dieser Welt erblicken wir uns dann selber, man möchte sagen als etwas Kleinstes gegenüber dieser großen Welt.",
        "Indem das hell­seherische Bewußtsein außer dem Leibe zu wirken beginnt, kehrt sich dieses Verhältnis geradezu um.",
        "Die Welt, die sich sonst ausbreitet vor unseren Sinnen, über die wir nachdenken mit unserem an das Gehirn gebundenen Verstand, diese Welt, sie entschwindet der Anschauung, der Wahrnehmung.",
        "Sie gibt auch keine Gedanken her, wenn man so sagen will.",
        "Aber man fühlt sich wie in diese Welt ausgegossen, man fühlt wirklich, wenn man aus seinem Leibe herausgekommen ist, so, daß dieses Erfühlen in der richtigen Weise ausgesprochen ist, wenn man sagt: Die Welt, die du früher angeschaut hast, in die bist du nun ausgegossen, in der bist du darinnen.",
        "Du erfüllst bis zu einer gewissen Grenze den ganzen Raum und du webst selber in der Zeit."
      ],
      [
        "Es ist das eine Empfindung, an die man sich erst gewöhnen muß.",
        "Es ist eine Empfindung, die man auch so ausdrücken kann, daß man sagt: Was früher Außenwelt war, ist jetzt Innenwelt geworden.",
        "Nicht als ob man diese frühere Außenwelt jetzt im Innern trüge, aber das Gefühl, die Empfindung ist da: Innenwelt ist es geworden.",
        "Du lebst in dem Raum, in dem früher deine Sinneswahrnehmungen ausgebreitet waren, über dessen Dinge und Vorgänge du dachtest, da lebst du darinnen. - Und das kleine Wesen, das gleichsam im Mittelpunkt des Sinneshorizontes gestanden hat, der Mensch, das wird, wenn man in einer gewissen Weise das hellseherische Bewußtsein entwickelt,"
      ],
      [
        "eigentlich jetzt die Welt.",
        "Auf die schauen wir so hin, wie wir früher hingeschaut haben auf die ganze im Raum ausgebreitete und in der Zeit verlaufende Außenwelt.",
        "Wir sind uns gewissermaßen Welt ge­worden."
      ],
      [
        "Denken Sie nur, meine lieben Freunde, was das für ein Umkehren des menschlichen Welt-Erschauens ist, wenn das, was früher so gar nicht Welt war, wozu man Ich gesagt hat, wenn das da draußen eigent­lich jetzt die Welt ist, auf die alles hin tendiert.",
        "Es ist, wie wenn man von allen Punkten des Raumes nach einem einzigen Mittelpunkte schauen würde - und da sieht man sich selber.",
        "Es ist, wie wenn man in der Zeit vor- und rückwärts schwimrnen würde - und an einem Punkte in einer Woge dieses Zeitstromes findet man sich selber.",
        "Man ist sich selbst die Welt geworden."
      ],
      [
        "Das ist der erste Eindruck, wenn man, ich sage es ausdrücklich noch einmal, mit dieser Tendenz, das menschliche Innenleben kennen­zulernen, das hellseherische Bewußtsein entfaltet.",
        "Dann ist dieses der erste Eindruck.",
        "Merkwürdig: Man geht aus dem Leibe heraus mit der Tendenz, das menschliche Innenleben kennen zu lernen, und das erste, was einem entgegentritt, ist die menschliche Gestalt selber.",
        "Aber wie verändert ist diese menschliche Gestalt!",
        "Man kann das nicht oft genug sagen: Man muß mit der Absicht, das menschliche Innenleben kennen zu lernen, herausgehen aus dem Leibe.",
        "Dann tritt das alles ein, was ich jetzt sagen werde.",
        "Es braucht deshalb beim Hellsehend-werden natürlich nicht immer einzutreten."
      ],
      [
        "Diese Menschengestalt, wie anders stellt sie sich dar!",
        "Man weiß:"
      ],
      [
        "das, worauf man hinschaut, das, was man da schaut, das bist du.",
        "Ja, du bist es, du, der du dich früher von innen erfühlt hast in deiner Haut, in deinem Blut, du stehst draußen. - Aber man sieht eigentlich von dem, was da steht, zunächst nur, man möchte sagen, die äußere Gestalt, jedoch verwandelt.",
        "Die Augen, das, was Auge war, leuchtet gewissermaßen wie zwei Sonnen, aber innerliche, in Lichtglanz vibrierende Sonnen, funkelnde, auffunkelnde und im Funkeln ab­dämmernde Sonnen, die strahliges Licht verbreiten.",
        "So erscheinen an der verwandelten Menschengestalt die Augen.",
        "Die Ohren beginnen in einer gewissen Weise zu tönen; das, was man in der physischen"
      ],
      [
        "Welt von den Ohren sieht, sieht man ja nicht, aber man fühlt ein gewisses Tönen.",
        "Die ganze Haut erstrahlt in einer Art von Strahlen, die man mehr erfühlt, als daß rnan sie erschauen könnte.",
        "Kurz, die menschliche Gestalt erscheint einem wie ein Leuchtendes, Tönendes, Magnetisch-Elektrisches, Strahlungen Aussendendes.",
        "Aber die Aus­drücke sind natürlich ungeschickt, weil sie eben der physischen Welt entnommen sind."
      ],
      [
        "So steht die Welt vor uns.",
        "Und das ist nun unsere Welt in dem geschilderten Anfang des heilseherischen Erlebens: der lichterglän­zende Mensch, die ganze Haut in einem fühlbaren Erglänzen, schaubar die Augen, hörbar die Ohren!",
        "Und jetzt weiß man, wenn man diesen Eindruck hat: Du hast von außerhalb des Leibes deinen Leib, deinen physischen Leib geschaut.",
        "Man weiß: vom Gesichtspunkt des Geistes aus gesehen ist der physische Leib so."
      ],
      [
        "Wenn man dann versucht eine innere Tätigkeit auszuüben da draußen, aber außer dem Leibe, die sich vergleichen läßt mit dem Nachdenken - aber es ist eben etwas anderes als das gewöhnliche Denken, es ist ein Entfalten einer inneren schöpferischen Seelenkraft -, wenn man die entwickelt, so sieht man in diesem Leuchtewesen da drinnen mehr: man sieht da drinnen bewegende Kräfte, die, man möchte sagen wie eine Art von Kraftzirkulation diese Leuchtegestalt durchsetzen.",
        "Und jetzt weiß man: Das, was du da drinnen wie eine Art Einschluß in deinem Leuchteleib erschaust, das ist dein Gedanken-leben von außen gesehen.",
        "Man kann es nun erkennen als einen Teil des Ätherleibes, den man eben sieht.",
        "Man sieht den Ätherleib als das webende Gedankenleben.",
        "Es ist wie ein Zirkulieren von dunklen Wellen, eine geistige Blutzirkulation, könnte man sagen: dunkle Wellen in dem Leuchteleib, die dem Ganzen ein eigentümliches An-sehen geben und die einem eben die Erkenntnis aufdrängen: Da welit und wallt in deinem physischen Leib der Ätherleib drinnen, den du jetzt von außen anschaust, der dir jetzt sichtbar wird."
      ],
      [
        "Sehen Sie, so erlangt man außerhalb seines Leibes stehend die Erkenntnis, daß es wirklich den physischen Leib und den Ätherleib gibt, und wie sie aussehen, von außen gesehen."
      ],
      [
        "Nun kann aber das innerliche Erkraften noch weitergehen.",
        "Würde"
      ],
      [
        "man nämlich nur das erschauen, was ich jetzt angeflihrt habe, dann würde man sich eigentümlich vorkommen in der geistigen Welt.",
        "Man würde sich dann so vorkommen wie ein Wesen, das auf dem physi­schen Plane zwar die Eindrücke der Außenwelt empfangen kann, aber innerlich ganz gefühisleer wäre, das gar nichts fühlen könnte."
      ],
      [
        "Aber auch das, was diesem Gefühle des physischen Planes entspricht, das kann innerlich sich nun auferwecken da draußen außer dem Leibe.",
        "Es ist dies nicht das Fühlen selbst, denn dieses Fühlen hat nur eine Berechtigung, ist nur vorhanden innerhalb des physischen Leibes; aber es ist das, was innerhalb der geistigen Welt dem Fühlen ent­spricht."
      ],
      [
        "Vorher hat man nämlich bloß empfunden: Du bist in dem Raume darinnen und wogst hin in der Zeit.",
        "Du bist in dem Raum, in dem du früher die Vorgänge, die Wesenheiten gesehen hast, und in der Zeit, in der du wahrgenommen hast: da bist du darinnen."
      ],
      [
        "Wenn aber das dem Fühlen entsprechende innere Seelentum nun da draußen außer dem Leibe auferweckt wird, dann beginnt dieses Seelische ein Wissen zu entfalten, wodurch allerlei aufleuchtet da draußen, wodurch man nicht nur sich fühlt wie über den Raum verbreitet, sondern wodurch man etwas wahrnimmt, was in diesem Raume darinnen ist, was in diesem Zeitenstrom als Wesen wogt.",
        "Und man findet jetzt nicht das, was man früher durch den Leib und seine Organe schauend in der Außenwelt gesehen hat, sondern man findet sich erlebend in dem Innern dieser Außenwelt, in dem Geistigen, das diese Außenwelt durchwallt und durchwogt."
      ],
      [
        "Es ist, wie wenn der Raum, in dem man sich früher nur gefühlt hätte, nun von unzähligen Sternen angefüllt würde, die sich alle bewegen und zu denen man selber gehört.",
        "Und jetzt weiß man: Du erlebst dich in deinem astralischen Leib."
      ],
      [
        "Man er­lebt sich so in seinem astralischen Leib außerhalb des physischen Leibes, daß auflebt inhaltlich das, worin man sich früher nur fühlte."
      ],
      [
        "Wenn man jetzt zurückschaut auf das, was man früher von sich selbst gesehen hat, was vorhin sozusagen als die Außenwelt geschildert worden ist, auf diesen Leuchteleib mit der dunklen Gedankenzirkula­tion des Ätherleibes darinnen, dann erscheint einem in dem Augen­blick, wo man sich außer dem Leibe eben auf das Astrale, auf das Sternenleben des astralischen Leibes konzentriert, das was man verlassen"
      ],
      [
        "hat, der verlassene Leib, anders.",
        "Und man kann nun genau den Unterschied merken, der durch Folgendes ausgedrückt werden kann: Du kannst dich konzentrieren auf dich zurück, dann siehst du deinen Leuchteleib und deinen Gedankenätherleib.",
        "Kannst du dich aber so auf dich selbst konzentrieren, daß eine innere Sternenwelt, von der du weißt: du füllst sie aus, sich in dir auslebt, und du schaust nun zurück auf deinen physischen Leib, den du verlassen hast, dann kann das Leuchten aufhören, dann hört die Gedankenzirkulation au£ Es ist das in gewisser Weise willkürlich zu machen, aber es tritt an die Stelle dessen ein Bild unserer eigenen Wesenheit, das uns erscheint -ja es kann nicht anders gesagt werden - als unser personifiziertes Karma.",
        "Dasjenige in uns, was wir als Menschen in uns tragen, wes­wegen wir uns dieses oder jenes Schicksal bereiten, das ist wie zu­sammengerollt.",
        "Unser Karma, unser Schicksal, personifiziert, steht vor uns.",
        "Und wir wissen, wenn wir dieses nun anschauen: Das bist du, aber so, wie du eigentlich in deiner moralischen inneren Wesenheit bist.",
        "Das bist du so wie du darinnen stehst in der Welt als eine Indi­vidualität; das bist du ganz selbst."
      ],
      [
        "Noch ein anderes Bewußtsein tritt auf.",
        "Dieses Bewußtsein, das da noch hinzukommt, hat etwas sehr Bedrückendes.",
        "Man erblickt nämlich dieses ganz personifizierte Schicksal so, daß man es im innersten Zusammenhang mit seiner Leiblichkeit, mit seinem Erdenmenschen erfühlt.",
        "Und zwar so, daß man die unmittelbare Erkenntnis hat: Wie in deinem Erdenleibe deine Muskeln aufgebaut sind, wie dein ganzes Muskelsystem ist, ist es eine Schöpfung dieses deines Schicksals, deines Karmas.",
        "Jetzt kommt dann die Zeit, wo man sich sagt: Wie verschie­den ist manchmal die Maja von der Wahrheit.",
        "Da glauben wir, solange wir auf dem physischen Plane stehen, dieser Muskelmensch bestehe eben aus den fleischigen Muskeln: in Wahrheit sind diese Fleisches-muskeln das kristallisierte Karma.",
        "Und sie sind so gestaltet im Men­schen, so kristallisiert, daß der Mensch bis auf die feinste chemische Zusammensetzung hinein in seinem Muskelsystem sein kristallisiertes Karma trägt.",
        "So sehr trägt er es, daß sich nun der geistige Erschauer ganz klar wird darüber: Wenn ein Mensch zum Beispiel seine Muskeln so bewegt hat, daß er sich auf eine Stätte begeben hat, auf der ihm ein"
      ],
      [
        "Unglück geschehen ist, so ist das aus dem Grunde geschehen, weil in den Muskeln die geistige Kraft darinnen lag, die ihn aus sich selbst heraus an die Stätte getrieben hat, an der ihm das Unglück passierte.",
        "Die Weltenordnung hat unser Schicksal kristallisiert in unserem Muskelsystem.",
        "Und in unserem Muskelsystem lebt der Geist, für den äußeren physischen Plan kristallisiert, der ohne unser offenbares Wissen uns überall dahin führt, wohin wir eben in Gemäßheit unseres Karmas gehen müssen, kommen müssen."
      ],
      [
        "Wenn diese innere Erkraftung noch weiter geht, wenn der Mensch außer seinem Leibe sozusagen sein Inneres weiter erlebt, dann tritt in ihm dasjenige auf, was sonst im physischen Leben, auf dem physi­schen Plane dem Willensimpuis entspricht.",
        "Sobald dieses Willens-leben innerlich auftaucht - aber außer dem Leibe - da fühlt sich der Mensch nicht nur wie in einem Sternensystem darinnen, sondern er fühlt sich wie in der Sonne dieses Sternensystems darinnen, er weiß sich eins mit der Sonne seines Plantensystems.",
        "Man möchte sagen:"
      ],
      [
        "Wenn man seinen astralischen Leib innerlich erlebt, weiß man sich eins mit den Planeten seines Plantensystems; wenn man sich mit seinem Ich außer dem Leibe erlebt, weiß man sich eins mit der Sonne seines Sternensystems, auf die alles hingerichtet ist, auf die alles hin-tendiert."
      ],
      [
        "Wenn man jetzt zurückschaut auf das, was nun nicht innen, sondern außen ist - denn das, was außen ist, solange man im physischen Leibe ist, das ist, wenn man außer dem Leibe ist, innen.",
        "Und das, was innen ist, wenn man im physischen Leibe ist, das ist, wenn man außer dem Leibe ist, außen -, wenn man also jetzt auf sich selber zurückschaut, dann tritt einem ein anderes entgegen, dann tritt einem die Notwendig­keit entgegen im Hinblicken auf sich selbst, daß das, was da draußen in der physischen Welt als die eigene Leiblichkeit sich befindet, ent­stehen mußte und vergehen muß: Entstehen und Vergehen des physischen Leibes tritt einem entgegen.",
        "Man wird gleichsam gewahr, wie geistige Mächte und Wesenheiten vorhanden sind, die da die Entstehung dieses physischen Leibes lenken und leiten, und wie andere wieder da sind, die ihn abbauen, diesen physischen Leib.",
        "Und man wird sich bewußt, worin sich dieses eigentliche Entstehen und Vergehen"
      ],
      [
        "in der physischen Welt wiederum kristallisiert.",
        "Denn man weiß: dieses Entstehen und Vergehen ist im Grunde genommen an das Knochensystem des Menschen gebunden.",
        "Mit dem Einbauen des Knochensystems in den menschlichen physischen Leib ist sozusagen über die Form, in der der Mensch Geburt und Tod in der physischen Welt erlebt, das Urteil gesprochen.",
        "Wie das Knochensystem einkristallisiert ist in den Menschen, so ist durch diese Formung be­stimmt, wie der Mensch als Wesen entsteht und vergeht.",
        "Man weiß: Du könntest im physischen Dasein nicht das Wesen sein, das du bist, wenn nicht die ganze Welt zusammengewirkt hätte, um innerhalb deines physischen Daseins deine physische Natur so zu verhärten, daß es als Knochensystem dir entgegentritt.",
        "Und man lernt verehren im Knochensystem, so sonderbar das auch klingt, die waltenden Universalweltenmächte, die ihren geistigen Ausdruck in all jenen Wesen finden, die im Sonnenleben konzentriert sind.",
        "Man lernt gleichsam erkennen, wie hineingezeichnet worden ist in die Welten-ordnung der Grundplan des Menschen, dieses sein Knochensystem, und wie das andere, was seine physischen Organe sind, gleichsam daran aufgehängt worden ist."
      ],
      [
        "So endet das hellseherische Anschauen dessen, was jetzt Außenwelt wird, mit der Anschauung des Symbols des Todes, man möchte sagen, mit der Anschauung des Knochenmenschen von außen.",
        "Denn man gelangt durch diese hellseherischen Vorgänge zuletzt zu der Erkennt­nis, wie die geistigen Welten sich gleichsam ein physisches äußeres Symbol erbildet haben, diese geistige Welten, denen man mit seinem Innern in Wahrheit angehört, und in die man sich gestellt hat, indem man außerhalb seines Leibes gegangen ist.",
        "Man lernt sich mit seinem Wesen außer seinem Leibe kennen.",
        "Und jetzt lernt man auch erkennen, gerade bei diesem vierten Stadium: Wenn wir in der Welt unsere Handlungen vollziehen, wenn wir unseren Willen entfalten, dann ist das die Kraft in uns, die unbewußt auf dem physischen Plan wirkt, die wir eigentlich erst jetzt kennen: Wenn wir nur einfach vorwärts gehen und uns zu dieser Vorwärtsbewegung der Mechanik unseres Knochensystems bedienen, so wirken in diesem Vorgang des Gehens universelle, kosmische Kräfte mit, Kräfte, in denen wir erst dann"
      ],
      [
        "wirklich darinnen sind, wenn wir uns also auf der vierten Stufe außer­halb unseres Leibes erleben."
      ],
      [
        "Denken Sie einmal, meine lieben Freunde: der Mensch macht einen Spaziergang und er bewegt mit Hilfe der Knochennechanik seine Glieder vorwärts; er denkt, daß er das zu seinem Vergnügen mache.",
        "Daß das geschehen kann, daß es Kräfte gibt, durch die wir uns vor­wärts bewegen können mit unserer Knochenmechanik, dazu mußte die ganze Welt da sein, und die ganze Welt von göttlich-geistigen Kräften durchwellt sein, von göttlich-geistigen Kräften, von denen wir erst ein Wissen bekommen, wenn wir uns auf dieser vierten Stufe befinden.",
        "In jedem unserer Schritte lebt der göttlich-geistige Kosmos mit, und während wir glauben, daß wir es sind, die unsere Füße vorwärtssetzen, könnten wir das nicht, wenn wir nicht lebten in dem geistigen Kosmos, in der göttlichen Welt."
      ],
      [
        "Wir richten, solange wir im physischen Leibe sind, unsere Blicke rings um uns herum.",
        "Da sehen wir die Wesen des mineralischen, des pflanzlichen, des tierischen Reiches, sehen Berge, Flüsse, Meere, Seen, Wolken, sehen Sterne, Sonne, Mond; was wir da äußerlich sehen, hat ein Inneres, und in dieses Innere treten wir selber ein, wenn wir in der geschilderten Weise außerhalb unseres Leibes leben.",
        "Wenn wir da drinnen leben, wissen wir: Was in ihnen geistig ist, was sich ver­birgt hinter der strahlenden Sonne, hinter den glänzenden Sternen, hinter den Bergen, Flüssen, Meeren, Seen, Wolken, das lebt in unserer Knochenmechanik, wenn wir sie bewegen, und das muß alles da sein.",
        "Dann fassen wir auch mehr Verständnis für das, was vorangegangen ist.",
        "So wie unser Wille mit unserer Knochermechanik im innigen Zusammenhange steht, stehen unsere Gefühle im innigen Zusammen­hang mit unserem Muskelsystem; dieses Muskelsystem ist ein sym­bolischer Ausdruck für unser Gefühlssystem.",
        "So wie unsere Muskeln gebaut sind, so wie unsere Muskeln uns gestatten, sich zu verkürzen und zu verlängern, um dadurch wiederum die Knochenmechanik hervorzurufen, so ist dazu das Planetensystem notwendig, das wir erkunden, wenn wir uns in unserem astralischen Leib befinden.",
        "In unserem Muskelsystem lebt das ganze Planetensystem, wie der ganze Kosmos in unserer Knochenmechanik.",
        "Was in entsprechender Weise"
      ],
      [
        "über die Gedanken und Sinnesempfindungen zu sagen ist, wird noch in den folgenden Vorträgen kommen."
      ],
      [
        "Solche Dinge liefert die geistige Erkenntnis.",
        "Wir sehen daraus, daß diese geistige Erkenntnis wahrhaftig nicht bloß etwas ist, was uns Gedanken und Ideen gibt, sondern was uns in unserer ganzen Seele durchdringen kann, so daß wir uns dadurch wirklich selbst erkennen lernen, daß wir ein anderer Mensch werden in unserem ganzen Er­fühlen und Denken.",
        "Denn - wenn man das, was jetzt auseinander­gesetzt worden ist als die Erfahrung des heliseherischen Bewußtseins, auf sein Gemüt wirken läßt und zusammendrängt in eine Grund­lebensempfindung der Seele - wie läßt sich dann diese Grundlebens­empfindung der Seele ausdrücken?",
        "Wie muß man sagen, wenn man mit einem kurzen Worte das bezeichnen will, was als ein inneres Lebensgefühl in uns angefacht ist durch ein solches Wissen der hell­seherischen Forschung?"
      ],
      [
        "Man schaut hin auf das, was scheinbar das Alltäglichste ist, was der Ausdruck unserer alltäglichsten Launen ist, und man bekommt etwas wie einen Eindruck von dem, was Sie in den ersten Sätzen der «Prüfung der Seele» durch den Mund des Capesius und des Benedik­tus geschildert finden: wie im Menschen gleichsam zusammenrinnen die Ziele, die sich die göttlich-geistigen Wesen gesetzt haben, wie hinein­fließt in das, was Menschennatur ist, dasjenige, was göttlich-geistige Wesen durch die Welten hindurch gedacht haben.",
        "Und nun will man das zusammenfassen in einer Lebensempfindung: man schaut anders auf die ganze Menschennatur hin als vorher, man weiß jetzt diese menschliche Natur ganz anders von dem göttlichen Kosmos durch­drungen als vorher.",
        "Und das Bewußtsein davon entflammt sich, er­starkt sich, erkraftet sich und sagt mit innerem Gemüts- und Gefühls­verständnis: Will man den Menschen verstehen, so kann man es nicht anders als dadurch, daß man wissen lernt: Aus dem Göttlich-Geistigen heraus ist dieser ganze Mensch!"
      ],
      [
        "Wenn wir ihn anschauen, wie sein Fühlen hineinfließt in seine Muskeltätigkeit, wie Göttlich-Geistiges, Kosmisches hineinfließt in seine Knochen, wie die ganze Welt lebt in der Bewegung seiner Knochen, wie das ganze Planetensystem lebt in dem Zusammenziehen"
      ],
      [
        "und Ausdehnen und Erschlaffen der Muskeln, wenn man das durch­denkt und durchfühlt, dann sagt man mit vollem Verständnis: Ja, aus dem Göttlichen ist dieser Mensch geboren."
      ],
      [
        "Ex deo nascimur."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "ZWEITER VORTRAG Wien, 10. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Es war gestern meine Aufgabe, im Zusammenhang mit einer Be­trachtung über Denken, Fühlen, Wollen und Wahrnehmen elnige esoterische Erfahrungen mitzuteilen, welche sich der Menschenseele ergeben, wenn sie geistesforscherisch außer dem Leibe mit der Ab­sicht lebt, etwas über das seelische Innere und seine Wesenheit zu erfahren. Heute wird es meine Aufgabe sein, von einer anderen Seite her solche Erlebnisse anzuführen, weil wir nur dann, wenn wir von den verschiedensten geistigen Gesichtspunkten aus das Leben be­trachten, wirklich Aufschluß über dieses Leben gewinnen können.",
      "Stellen Sie sich einmal richtig vor, wie gestern versucht worden ist zu zeigen, was die Menschenseele sieht, wenn sie zunächst auf die eigene Leiblichkeit und das, was physisch damit zusammenhängt, von außerhalb des Leibes zurückblickt, und was sie dann nachher erlebt; also was des Menschen astralischer Leib und Ich erleben, wenn sie sich immer mehr und mehr erkraften in dem Raum, den sie gleichsam außerhalb des Leibes betreten haben. Es gibt nun noch einen anderen Weg, gewissermaßen dasselbe zu betrachten. Das ist ja gerade das Bedeutsame wirklicher geistiger Betrachtungsweise, daß man im Grunde genommen auf die Rätsel des Daseins durch geistige Be­trachtung erst dadurch kommt, daß man eine Sache von den verschie­densten Seiten aus betrachtet. Es gibt nämlich noch eine andere Art, aus dem Leib herauszukommen. Ich möchte sagen, die gestern ge­schilderte Art zeigte uns: es verläßt dabei die Seele den Leib so, daß sie sich aus dem Leibe einfach in den Raum hinaus begibt und da außer dem Leibe zu leben beginnt. Dieses Aus-dem-Leibe-treten kann noch auf folgende Weise geschehen: Man kann, urn den Weg aus sich heraus zu finden, gerade zunächst tiefer in sich hineinzu­kommen versuchen. Man kann versuchen, an die Erfahrungen anzu­knüpfen mit dem, was in der Seele, man möchte sagen, der geistigen Erfahrung am ähnlichsten ist. Man kann versuchen, mit unserem Gedächtnis an die Erlebnisse anzuknüpfen. Es wurde ja öfter gesagt:",
      "Dadurch, daß wir als Menschenseelen imstande sind, nicht nur etwas wahrzunehmen, zu denken, zu fühlen und zu wollen, sondern die Gedanken und Wahrnehmungen aufzubewahren als Gedächtnisschatz, dadurch verwandeln wir unser Innenleben eigentlich schon in etwas Geistiges. Und ich habe in meinem öffentlichen Vortrage darauf hingewiesen, daß der französische Philosoph Bergson sogar schon darauf gekommen ist, daß man das, was als Gedächtnisschatz in der Seele des Menschen vorhanden ist, nicht als irgendwie mit dem Leiblichen unmittelbar zusammenhängend betrachten kann; daß man es vielmehr als eine seelische Innerlichkeit betrachten muß, als etwas, was die Seele entwickelt, was rein geistig-seelisch vorhanden ist.",
      "Und in der Tat, wenn in dem hellseherischen Bewußtsein die Imagination beginnt, wenn aus dem Dunkel des geistigen Daseins die ersten Eindrücke herauftauchen, so sind diese Eindrücke in ihrer Qualität, in ihrer ganzen Wesenheit sehr ähnlich jenem Seeleninhalt, der als Gedächtnisschatz in uns ist. Wie Erinnerungsbilder, aber jetzt doch wiederum wie etwas unendlich viel Geistigeres, treten die Offen­barungen aus der geistigen Welt bei uns auf, wenn wir mit dem hell­seherischen Bewußtsein wahrzunehmen beginnen. Wir merken dann gleichsam, daß unser Gedächtnlsschatz das erste wirklich Geistige ist, das erste, wodurch wir uns gewissermaßen schon aus unserem Leibe herausheben, daß wir dann aber weiter gehen müssen, daß wir solche im Geistigen schwebende Bilder, wie das Gedächtnis sie uns bietet -allerdings von viel größerer Lebendigkeit - aus Geistestiefen herauf-heben müssen, die nicht unserem Erleben angehören wie die Erinne-rungsvorstellungen, daß gleichsam hinter dem Gedächtnis etwas heraufzieht. Das muß festgehalten werden: es zieht etwas herauf aus fremden geistigen Gebieten, während der Gedächtnisschatz herauf-zieht aus dem, was wir im Physischen miterlebt haben.",
      "Wenn wir nun versuchen, den geistigen Blick zurückzulenken auf die Erlebnisse unseres Ich während der Jahre, die wir Seit dem Zeit­punkte unserer Kindheit erlebt haben, zu dem unsere Erinnerung zurückreicht, wenn wir versuchen, von allem Äußeren abzusehen und ganz in uns hineinzuleben, so daß wir uns immer mehr in unsere Erinnerungen hineinfin den, aus unserem Erinnerungsschatz auch das",
      "heraufholen, was uns gewöhnlich nicht gegenwärtig ist, dann nähern wir uns immer mehr und mehr dem Zeitpunkt, bis zu dem wir uns zurückerinnern können. Und wenn wir solches oft vornehmen, wenn wir uns sogar eine gewisse Praxis darin aneignen - und wir können das - sonst längst vergessene Erinnerungen heraufzuholen, so daß wir eine stärkere Kraft des Sich-Erinnerns entwickeln, wenn wir immer mehr und mehr Vergessenes heraufholen und dadurch unsere Kraft, die die Erinnerungen heraufschafft, stärker machen, dann werden wir sehen, daß, ich möchte sagen, wie auf einer Wiese zwischen den einzelnen grünen Grashalinen und Graspflanzen Blumen auftauchen, dann zwischen den Erinnerungen Bilder, Imaginationen auftauchen von etwas, was wir vorher nicht gekannt haben. Es ist etwas, was wirklich so auftaucht wie die Blumen auf der Wiese zwischen den Graspflanzen, was aber aus ganz anderen geistigen Tiefen herauf-kommt als die Erinnerungen, die eben nur aus unserer eigenen Seele herauftauchen. Und wir lernen dann unterscheiden das, was irgendwie mit unseren Erinnerungen zusammenhängen könnte, von dem, was also herauftaucht aus geistigen Untergründen und geistigen Tiefen. Und so leben wir uns nach und nach in die Möglichkeit ein, eine Kraft zu entfalten, das Geistige herauszuholen aus seinen Untergründen.",
      "Dadurch aber gelangen wir auf eine andere Weise aus unserem Leibe heraus als auf die gestern beschriebene Art. Bei der gestern beschriebenen Art verlassen wir den Leib gewissermaßen unmittelbar. Bei der heute gemeinten Art gehen wir zuerst unser Leben zurück, durchlaufen unser Leben. Wir versenken uns in unser Innenleben, gewöhnen uns, durch die Erstarkung der Erinnerungskraft in unse­rem Innenleben zwischen unseren Erinnerungen Geistiges hervorzu­holen aus der geistigen Welt, und so gelangen wir endlich dazu, hin-auszudringen durch unsere Geburt, durch die Zeitenfolgen über un­sere Empfängnis hinaus, in die geistige Welt, in der wir gelebt haben, bevor wir uns zu unserer jetzigen Inkarnation mit einer physischen Vererbungssubstanz verbunden haben. Wir gelangen, unser Leben durcheilend, hinaus in die geistige Welt, zurück in die Zeit, bevor wir eben hereingetreten sind in diese Inkarnation. Das ist die andere Art, den Leib zu verlassen, hineinzukommen in das Geistige. Und diese",
      "Art weist einen großen Unterschied auf gegenüber der gestern be­schriebenen. Merken Sie wohl auf diese Unterschiede, denn gerade in diesem Vortragszyklus habe ich so manche Feinheiten und Intimi­täten des geistigen Lebens vor Ihnen mitzuteilen. Aber es ist schwie­rig, auf diese Feinheiten und Intimitäten in geeigneten Worten hinzu­weisen. Und nur, wenn man versucht, gerade solche Unterscheidungen zu fassen, kommt man richtig in die Dinge hinein und gewinnt ein sicheres Denken über dieselben.",
      "Wenn man so, wie ich es jetzt beschrieben habe, den Leib verläßt, so kommt man nämlich ganz anders aus seinem Leibe heraus. Wenn man auf die gestern beschriebene Weise herauskommt aus seinem Leibe, so fühlt man sich wie außerhalb seines Leibes in dem Außen-raum. Ich konnte beschreiben, wie man sich verbreitet über den Außenraum, wie man zurückschaut auf seinen physischen Leib. Man tritt aus sich heraus und füllt gleichsam den Raum aus, man tritt in den Raum hinaus. Wenn man aber durchinacht, was jetzt hier gemeint ist, dann tritt man aus dem Raum selber hinaus, dann hört der Raum auf, für einen eine Bedeutung zu haben; man verläßt den Raum und man ist dann nur noch in der Zeit. So daß bei einem solchen Verlassen des Leibes das Wort aufhört, einen Sinn zu haben: Ich bin außerhalb meines Leibes - denn das Außerhalb bedeutet ein räumliches Ver­hältnis. Man fühlt sich dann eben nicht gleichzeitig mit seinem Leibe, man erlebt sich in der Zeit. In der Zeit, in der man war vor der In­karnation, in einem Vorher. Und den Leib erschaut man als nachher existierend. Man ist wirklich nur in der fortströmenden, laufenden Zeit darinnen. Und anstelle des Außen und Innen ist ein Vorher und Nachher getreten.",
      "Dadurch ist man imstande, durch ein solches Herausgehen aus seiner Leiblichkeit, wirklich einzudringen in die Gebiete, die wir durchleben zwischen dem Tod und einer neuen Geburt. Denn man geht in der Zeit zurück, man lebt sich ein in ein Leben, das man vor diesem Erdenleben gelebt hat. Und dieses Erdenleben erscheint so, daß wir sagen: Was ist denn dort in der Zukunft, was erscheint uns denn da als Nachher? Sie sehen da eine genauere Angabe über man­ches, was ich in meinem öffentlichen Vortrage nicht so genau habe",
      "ausführen können: wie man nämlich im Konkreten hineinkommt in die Gebiete, die man durchlebt zwischen dem Tod und einer neuen Geburt.",
      "Nun ist man auf diesem Wege hinausgezogen aus seinem Leibe, indem man in das vorher im Geiste vollbrachte Leben zurückgekehrt ist, man ist damit aber auch aus dem Raum herausgezogen. Dadurch hat dieses Verlassen des Leibes - aus dem Jetzt zu dem Früheren -einen viel höheren Grad von Innerlichkeit als das andere Verlassen, und für den Geistesforscher ist in der Tat dieses jetzt geschilderte Verlassen des Leibes von unendlich größerer Bedeutung als das gestern geschilderte, das nicht aus dem Raume herauskommt. Denn eigentlich begreift man dasjenige, was so recht tiefe Innerlichkeiten der Seele angeht, im Grunde erst auf dem heute beschriebenen Wege. Und da möchte ich Ihnen zunächst eines anführen, aus dem Sie er­sehen werden, wie man versuchen muß, hinter die Intimitäten und Feinheiten des menschlichen Lebens zu kommen.",
      "Im physischen Leibe hier leben wir unser physisches Leben. Wir bedienen uns unserer Sinne, nehmen die Welt wahr, wir stellen die Welt vor, fühlen in ihr, versuchen uns durch unsere Handiungen in dieser Welt einen Wert zu geben, wir handeln bewußt durch unseren Leib. So geht das alltägliche Leben vor sich, so geht das Leben vor sich, insofern wir dem physischen Plan angehören. Nun muß es aber für jeden Menschen, der seine Menschenwürde wahrhaft in sich er­fühlen will, ein höheres Leben geben; und es hat immer ein höheres Seelenleben gegeben. Die Religionen, die den Menschen mit höherem Leben erfüllten, waren immer da. Geisteswissenschaft wird den Men­schen in der Zukunft mit einem solchen höheren Leben erfüllen. Was will dieses höhere Leben? Was will dieses Leben, das in Gedanken, in Gefühlen, in Empfindungen hinausgeht über das, was der physische Plan bieten kann, das bei dem einen nur in dunklen Ahnungen auf religiösem Gebiet, bei dem andern in klar umrissenen Linien der Geisteswissenschaft hinausgeht über das, was die Sinne schauen können, was man mit seinem an das Gehirn gebundenen Verstande denken kann, was man mit seinem Leibe in der Welt verrichten kann?",
      "Nach einem geistigen Leben hin tendiert die menschliche Seele.",
      "Ein geistiges Leben in sich zu erfühlen, von einem solchen geistigen Leben etwas zu wissen, das über das physische Leben hinausgeht, das gibt dem Menschen eigentlich erst seine Würde. Man könnte sagen: Solange der Mensch im physischen Leibe weilt, sucht er seine Würde zu erhöhen, sucht er seine eigentliche Bestimmung zu erahnen durch ein Leben, das er sich vorstellt als über die physische Welt hinaus­gehend, durch ein Erahnen, Empfinden, Erkennen einer geistigen Welt. Blicke auf zum Geiste, fühle, daß geistige Kräfte durch die physischen Welten weben: das sind im Grunde genommen die Töne, die das religiöse und das damit verwandte Leben dem Menschen geben sollen. Und die Sorge des Erziehers, der es mit einem heran­wachsenden Menschenkinde ernst meint, wird sein, dieses Menschen-kind nicht so aufwachsen zu lassen, daß es nur in den äußeren mate­riellen Vorstellungen lebt, sondern ihm Vorstellungen von einer übersinnlichen Welt beizubringen.",
      "Nennen wir jetzt, ohne damit hinweisen zu wollen auf das Eng­umschränkte oder dogmatisch Eingeengte der Religionssysteme, nennen wir das, was so den Menschen hinauszieht aus dieser physi­schen Welt, Religion, und fragen wir gegenüber dem, was wir gerade geschildert haben als ein Hinausgehen der menschlichen Seele über Geburt und Empfängnis in eine dem Erdenleben vorhergehende geistige Welt hinein, wo die Seele auch aus dem Raume heraus ist, fragen wir demgegenüber: Gibt es nun zwischen dem Tod und einer neuen Geburt in der Welt, die wir so betreten, wie wir es auseinander­gesetzt haben, etwas, was man eine Religion jenes Geisterlandes nennen könnte? Gibt es da drüben etwas, was sich mit dem religiösen Leben auf der Erde vergleichen ließe? Wir haben schon in manchen Einzelheiten geschildert und werden noch weiter die Vorgänge zu schildern haben, die der Mensch zwischen dem Tod und einer neuen Geburt durchlebt. Aber jetzt fragen wir uns: Gibt es so etwas wie eine Religion in diesem geistigen Leben? Etwas, von dem man sagen kann: es steht den Erlebnissen, die wir für das Geisterland schildern, so gegenüber, wie die Hinweise auf die übersinnliche Welt dem All­tagsleben des physischen Planes gegenüberstehen?",
      "Derjenige, der auf die geschilderte Weise aus seinem Leibe herauskommt,",
      "der kommt zu der Erkenntnis, daß es so etwas wie eine Art religiösen Lebens da drüben in diesem Geisterlande auch gibt. Und merkwürdigerweise, während man alles das, was man im Geisterlande um sich herum hat, geistige Wesenheiten und geistige Vorgänge, so erlebt wie man hier physische Wesen und physische Vorgänge erlebt, hat man dort fortdauernd während dieses Lebens, oder wenigstens während eines großen Teiles dieses Lebens zwischen dem Tod und einer neuen Geburt, wie ein mächtiges geistiges Gebilde, das Bild des Menschen-Ideals vor sich. Alles, was über den Menschen hinaus-geht, hat man hier auf der Erde als Religion; das Menschenideal, man hat es drüben in der geistigen Welt als Religion. Man lernt verstehen, daß die verschiedenen Wesenheiten der verschiedenen geistigen Hierarchien ihre Absichten, ihre Kräfte zusammenwirken ließen, um im Weltenstrome auf die Art, wie es in meiner «Geheimwissenschaft» beschrieben ist, allmählich den Menschen hervorgehen zu lassen. Den Göttern schwebte als das Ziel ihrer Schöpfung das Menschenideal vor, und zwar jenes Menschenideal, welches wirklich sich nicht so auslebt, wie jetzt der physische Mensch ist, sondern so, wie höchstes mensch­liches Seelengeistesleben in den vollkommen ausgebildeten Anlagen dieses physischen Menschen sich ausleben könnte.",
      "So schwebt als Ziel, als höchstes Ideal, als die Götterreligion den Göttern ein Bild der Menschheit vor. Und wie am fernen Ufer des Götterseins schwebt für die Götter der Tempel, der als höchste künstlerische Götterleistung das Abbild des göttlichen Seins im Menschenbilde hinstellt. Und das ist das Eigentümliche, daß der Mensch, während er sich in dem Geisterlande zwischen dem Tod und einer neuen Geburt heranbildet, sich nach und nach dort immer reifer und reifer macht zum Schauen dieses Menschheitstempels, dieses hohen Menschheitsideals. Und während wir hier auf Erden das religiöse Leben so empfinden, daß es unsere freie Tat sein muß, daß wir es aus uns herausholen müssen, daß es dem materialistischen Sinn auch möglich ist, das Religiöse zu verleugnen, ist das Umgekehrte im Geisterland zwischen dem Tod und einer neuen Geburt der Fall. Je mehr wir in die zweite Hälfte der Zeit zwischen dem Tod und einer neuen Geburt hineinleben, desto deutlicher steht vor uns, so daß wir",
      "es nicht übersehen können, so daß es immer vor unserem geistigen Blicke ist, das hehrste Menschenideal, das Götterziel der Welten. Hier auf Erden kann der Mensch irreligiös sein, weil seine Seele gegenüber dem Physischen den Geist übersehen kann Drüben ist es unmöglich, daß der Mensch nicht das Götterziel schaut; denn das stellt sich ihm mit Sicherheit vor Augen. So steht, namentlich in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt, wie am Ufer des Seins, das heißt am Ufer der dahinströmenden Zeit -nehmen Sie jetzt alle Ausdrücke so, daß wir es zu tun haben außerhalb des Raumes mit der Zeit - so steht es da, das Menschheitsideal. Eine Erkeunmisreligion kann es drüben nicht geben; denn erkennen muß man das, was religiöser Inhalt ist. Das, was ich jetzt geschildert habe, ist drüben religiöser Inhalt. In diesem Sinne irreligiös kann kein Mensch sein, daß er das religiöse Ideal des Geisterlandes nicht vor sich hätte. Denn das steht durch sich selbst da, es ist Götterziel und wird hingestellt als die mächtigste, glorioseste Imagination, wenn wir die zweite Hälfte unseres Lebens zwischen dem Tod und einer neuen Geburt antreten. Aber wenn wir so auch nicht eine Erkenntnis-religion drüben entwickeln können, so entwickeln wir doch unter der Anleitung höherer geistiger Wesenheiten, die da drüben für den Menschen tätig sind, eine Art Religion.",
      "Während uns aber Erkennen, Schauen nicht gelehrt werden kann, weil es ja selbstverständlich ist, muß unser Wollen, unser wollendes Fühlen, unser fühlendes Wollen angeeifert werden in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt, um zu dem, was wir da sehen, wirklich hinzustreben. In unser wollendes Fühlen, in unser fühlendes Wollen fließen Götterwille, Götterfühlen ein, damit wir den Weg in dieser Richtung wählen in der zweiten Hälfte unseres Lebens zwischen dem Tod und einer neuen Geburt. Es sind ja alle Ausdrücke ungeschickt für dieses ganz andersartige Leben, dennoch darf der Ausdruck gebraucht werden: hier werden wir in bezug auf unseren Verstand unterrichtet, nur wenn ein Lehrer durch die Vorstellung geht, wirkt er hier auf Erden weiter auf unser Gefühl. Drüben ist es so, daß, wenn man den weiter noch zu schildern­den Zeitpunkt der Mitte zwischen dem Tod und einer neuen Geburt,",
      "wenn man das, was ich in meinem letzten Mysteriendrama «Der Seelen Erwachen» die Mitternachtstunde genannt habe, überschritten hat, daß dann zunächst eine gewisse Dumpfheit da ist in bezug auch auf das Wollen und Fühlen gegenüber dem, was wie ein herrlicher Tempel in den Fernen der Zeiten steht. Da durchglühen und durch­wärmen göttliche Kräfte unsere inneren Seelenvermögen: ein Unter­richt ist es, der unmittelbar zu unserem Innern spricht und der sich so äußert, daß wir immer mehr und mehr die Fähigkeit gewinnen, wirk­lich den Weg gehen zu wollen zu dem, was wir so als ein Ideal schauen.",
      "Während wir im physischen Leben einem Lehrer gegenüber-stehen können oder einem Erzieher, und er uns gegenüberstehen kann, und wir uns doch im Grunde genommen so fühlen, daß er von außen herein in unser Herz spricht, fühlen wir, daß unsere geistigen Erzieher der höheren Hierarchien, indem sie uns so erziehen, wie ich es jetzt geschildert habe, unmittelbar in unser Inneres herein ihre eigenen Kräfte strömen lassen. Irdische Erzieher sprechen zu uns, geistige Erzieher im Leben zwischen dem Tod und einer neuen Geburt geben uns ihr Leben in unsere Seelen herein, indem sie uns geistig religiös erziehen.",
      "Und so fühlen wir sie immer mehr und mehr in uns, diese Erzieher aus den höheren Hierarchien, so fühlen wir uns immer inniger mit ihnen verbunden. Dadurch aber erkraftet und erstarkt sich unser Innenleben.",
      "Du bist immer mehr und mehr von den Göttern ange­nommen, in dir leben immer mehr und mehr die Götter und sie helfen dir, daß du immer innerlich stärker und stärker wirst! Das ist es, was als ein Grundgefühl durchgeht durch dieses Leben zwischen dem Tod und einer neuen Geburt, namentlich in seiner zweiten Hälfte.",
      "So sehen wir, wie alles in diesem Leben daraufhin angelegt ist, daß unsere Erlebnisse unmittelbar in den Tiefen unserer Seele selbst ab­laufen. Nun kommen wir aber, indem wir also von den Göttern unter­richtet werden, an einen bestimmten Punkt des Erlebens zwischen dem Tod und einer neuen Geburt. An einen wichtigen Punkt kommen wir. Es ist, ich möchte sagen, in der Zeiten fernster Ferne, wo wir das Menschheitsideal erblicken; die Kräfte aber, die in uns durch diese unsere göttlich-geistigen Erzieher gelegt werden können, die sind abhängig von dem, was wir im Laufe unserer Inkarnationen, im Laufe",
      "unseres vorhergehenden Menschenlebens aus uns gemacht haben. Und so stehen wir, indem wir heranleben von der Weltenmitternacht, gerade in der Mitte zwischen dem Tod und einer neuen Geburt, und immer weiterleben in die Zeiten hinein und in fernsten Zeiten das Menschheitsideal sehen, dann endlich an einem Punkt, an der letzten Perspektive des Menschheitsideals. Aber so stehen wir an diesem Punkt, daß wir uns nun sagen müssen - wir sagen es uns natürlich nicht, wir erleben es ganz innerlich, aber man muß sich mit den Worten des gewöhnlichen Lebens aussprechen -: Göttlich-geistige Kräfte haben an dir gewirkt, sind immer innerlicher in deiner Seele geworden, leben jetzt in dir; aber jetzt bist du an dem Punkte, wo du dich nicht mehr weiter mit diesen Kräften durchdringen kannst, denn du müßtest viel vollkommener sein, wenn du weitergehen wolltest als bis hierher.",
      "Und jetzt kommt ein wichtiger Entscheidungspunkt. In diesem Augenblick tritt an uns eine harte Versuchung heran! Die Götter haben es gut mit uns gemeint, sie haben uns alles das gegeben, was sie uns zunächst geben können, sie haben uns so stark gemacht, als es nach Maßgabe der Kraft möglich war, die wir im bisherigen Leben uns erworben haben. So ist diese uns von den Göttern gegebene Stärke in uns, und die Versuchung tritt an uns heran, die uns sagt:",
      "Ja, du kannst jetzt diesen Göttern folgen, du kannst jetzt alles das, was du bist, gleichsam einfließen lassen in das, was die Götter dir gegeben haben an Kräften, du kannst in die geistigen Welten hinein­gehen. Denn viel, viel haben dir die Götter gegeben.",
      "Man kann sich ganz vergeistigen: diese Aussicht steht vor einem. Aber man kann das nur, indem man seinen Weg von der Bahn nach dem großen Menschheitsideale hin ablenkt, indem man herausgeht aus der Bahn. Das heißt mit anderen Worten: man schlägt den Weg em in die geistigen Welten, indem man all seine Unvollkommenheiten in die geistigen Welten mit hineinnimmt. Sie wurden sich dort schon in Vollkommenheiten verwandeln. Sie täten es wirklich. Man könnte mit den Unvol kommenheiten hinein, man wurde mit ihnen, weil man von göttlichen Kräften durchdrungen wäre, ein Wesen sein. Aber dieses Wesen müßte verzichten auf Anlagen, die es doch in sich hat,",
      "die es noch nicht auf seinem bisherigen Wege ausgebildet hat und die nach der Richtung des großen Menschheitsideales liegen; auf die müßte es verzichten. Jedesmal, bevor wir zu einer Erderinkarnation gehen, tritt an uns die Versuchung heran, in der geistigen Welt zu bleiben, in den Geist einzutreten und sich vorwärts zu entwickeln mit demjenigen, was man schon ist, was jetzt ganz durchgöttlicht ist, und zu verzichten auf das, was man als Mensch noch immer mehr werden könnte auf der Bahn nach dem fernen religiösen Ideal der göttlich-geistigen Welt hin. Es tritt die Versuchung heran, irreligiös für das Geisterland zu werden.",
      "Diese Versuchung tritt um so mehr heran, als in keinem Moment der Menschheitsentwicklung Luzifer eine größere Gewalt hat über den Menschen als in diesem Augenblick, wo er ihm einbläst: Ergreife jetzt die Gelegenheit, du kannst im Geiste bleiben, du kannst alles das, was du entwickelt hast, in das geistige Licht überführen! Und vergessen zu machen der Seele, soweit es irgend möglich ist, sucht Luzifer das, was noch als Anlagen vorhanden ist, was da steht in dem fernen Tempel am fernen Ufer des Zeitenseins.",
      "So wie die Menschheit jetzt ist, würde der Mensch nicht in der Lage sein, in diesem Punkt der Versuchung Luzifers zu widerstehen, wenn nicht die Geister, deren Gegner Luzifer ist, jetzt die Angelegenheiten des Menschen übernehmen würden. Und es tritt der Kampf der den Menschen zu seinem Ideale vorwärtsleitenden Götter ein, der die Götterreligion bekennenden Götter mit Luzifer um eine Menschen-seele. Und das Ergebnis dieses Kampfes ist, daß das Urbild, das sich der Mensch von seinem irdischen Dasein gebildet hat, herausgeworfen wird aus der Zeit in den Raum, angezogen wird magnetisch vom Raumesdasein. Dies ist auch der Moment, wo jene magnetische An-ziehung durch das Elternpaar auftritt, wo der Mensch hineinversetzt wird in die Raumes sphären, Verwandtschaft gewinnt mit der Raumes-sphäre. Dadurch aber wird alles dasjenige um den Menschen herum verhüllt, was ihm die Versuchung einflößen könnte, nur in der geisti­gen Welt zu bleiben. Und diese Verhüllung drückt sich aus eben in seiner Umhüllung mit der Leiblichkeit. Er wird in die Leiblichkeit eingefügt, damit er nicht schaut, was Luzifer vor ihn hinstellen will.",
      "Und wenn er in die leibliche Hülle eingehüllt ist und durch seine leib­lichen Sinne und seinen leiblichen Verstand nunmehr die Welt an-sieht, so sieht er nicht das, was er sonst in der geistigen Welt, durch den Versucher verführt, anstreben möchte, er sieht es nicht, er schaut diese Welt geistiger Wesenheiten und Vorgänge von außen, wie sie sich für die Sinne und den an das Gehirn gebundenen Verstand offen­baren. Und indem er im Sinnesleibe ist, übernehmen die ihn vorwärts bringenden Geister seine Entwickelung.",
      "Und fragen wir uns jetzt: Wie viel geht mit uns vor zwischen der Geburt und dem Tode in den unterbewußten Seelentiefen, wie viel geht mit uns vor, ohne daß wir davon wissen ? - Wenn wir uns so leiten müßten, daß wir alles bewußt vollbringen, so könnten wir das Erden-dasein durchaus nicht vollenden. Ich habe schon darauf hingewiesen in meinem Buche über «Die geistige Führung des Menschen und der Menschheit»: der Mensch muß, indem er in die physische Inkarnation tritt, selber erst plastisch an seinem Gehirn- und Nervensystem arbei­ten.",
      "Er arbeitet, aber er arbeitet unbewußt daran. Das alles ist der Ausdruck einer viel größeren Weisheit als diejenige ist, die der Mensch begreifen kann mit seinem sinnlichen Verstand. In uns waltet zwischen der Geburt und dem Tode eine Weisheit, die hinter der Welt vor­handen ist, die wir mit unseren Sinnen anschauen und über welche wir mit unserem an das Gehirn gebundenen Verstand denken.",
      "Da­hinter ist sie vorhanden, diese Weisheit; sie ist verhüllt vor uns zwischen der Geburt und dem Tode. Aber sie waltet, webt, wirkt in uns in den unterbewußten Seelentiefen, und sie muß sozusagen m diesen unterbewußten Seelentiefen des Menschen Angelegenheiten in die Hand nehmen, weil der Mensch auf einige Zeit hinweggerückt werden muß von einem Anblick, der für ihn versucherisch wäre.",
      "Die ganze Zeit, während welcher wir in unserem physischen Leibe leben, würden wir unter sonst normalen Verhältnissen, ohne daß wir eben durch eine sorgfältige Schulung in die geistige Welt eingeführt wer­den, wenn der Hüter der Schwelle uns das Hineinschauen in die geistigen Welten nicht vorenthielte, unser ganzes Leben Schritt für Schritt versucht sein, unsere noch unvollkommenen, unsere noch nicht herausgekommenen Menschenanlagen fallen zu lassen und dem Hinaufschwung",
      "in die geistigen Welten zu folgen, aber mit unseren Unvoll­kommenheiten. Wir brauchen die Zeit unseres Erdenlebens, um in dieser Zeit der Versuchung Luzifers entrückt zu sein.",
      "Bis zu dem angegebenen Zeitpunkt, wo wir in den Raum heraus­geführt werden, hat Luzifer noch nicht die Gewalt, denn da gibt es noch immer eine Möglichkeit, vorwärts zu schreiten, aber er kommt eben in dem Moment heran, wo wir an dem Entscheidungspunkte angelangt sind. Durch unser vorhergehendes Leben können wir nicht vorwärts schreiten, so wollen wir mit den Unvollkommenheiten ab-irren und in der geistigen Welt verbleiben. Davor schützen uns die fortschreitenden Götter, deren Gegner Luzifer ist, indem sie uns dieser geistigen Welt entrücken, indem sie sie vor uns verhüllen, und das, was aus dieser geistigen Welt heraus geschehen muß an uns, hinter unserem Bewußtsein vollziehen.",
      "So stehen wir da als Menschen in der Welt, mit unserem Bewußtsein in unserem physischen Leibe, und sagen uns: Habt Dank, ihr Götter! So viel habt ihr uns gelassen von der Möglichkeit, etwas zu wissen von der Welt, als gerade gut ist für uns. - Denn blickten wir hinter die Schwelle desjenigen, was unser Bewußtseinshorizont ist, so stünden wir in jedem Augenblick vor der Gefahr, unser Menschheits­ziel nicht erreichen zu wollen. Aus jenem helleren, höheren Bewußt­seinszustand, in dem wir zwischen dem Tod und einer neuen Geburt sind, wo wir geistige Welten und geistige Wesenheiten um uns herum haben, wo wir im Geiste sind, mußten wir in die Welt des Raumes versetzt werden, damit uns in der Welt des Raumes verhüllt werde die Welt, die wir nicht ertragen könnten, bis wir die Zeit durchge­macht haben zwischen der Geburt und dem Tode, die Zeit, in der wir, dadurch, daß wir der geistigen Welt entrückt waren, dadurch daß diese geistige Welt in dieser Zeit nicht auf uns gewirkt hat, daß nur materielle Dinge uns umgeben haben, wiederum einen neuen Antrieb empfangen haben nach den fernen Zielen des Menschheits­ideales hin. Denn in der ganzen Zeit, während welcher wir auf Erden leben, während welcher wir mit unserem Bewußtsein nicht in die geistige Welt hineinsehen, wirken nun wiederum, indem sie jetzt nicht durch unser Bewußtsein gestört sind, indem sie nicht gestört",
      "sind dadurch, daß wir versucht sind, Luzifer zu folgen, in uns die uns vorwärtstreibenden göttlichen Geister. Und sie flößen uns wiederum so viel Kraft ein, daß, wenn wir durch die Pforte des Todes gehen, wir wiederum ein Stück vorwärtsdringen können nach dem Mensch­heitsideale hin.",
      "Das ist auch noch ein Geheimnis, das hinter dem Menschendasein steht, das ich mit diesen Worten angedeutet habe. Und ich denke, es ist eine gute Osterempfindung, hinzuschauen auf jene Verhältnisse des Lebens, die mehr durch innerliches Herausgehen aus dem Leibe erreicht werden, hinzuschauen auf die Verhältnisse zwischen dem Tod und einer neuen Geburt, und dem Leben, das wir nachher im physi­schen Leibe gewinnen.",
      "Da blicken wir hin auf dieses Leben zwischen dem Tod und einer neuen Geburt und werden gewahr der Führung der guten göttlich-geistigen Wesen, die uns vorwärts helfen. Wie zu unserer Vergangenheit im Geiste sehen wir zu diesen göttlich-geistigen Wesen auf, und wir verstehen jetzt von diesem unserem Sein im Leibe zwischen der Geburt und dem Tode, daß es uns verliehen wor­den ist von den Göttern, damit die Götter eine Weile, ohne daß wir etwas dazu zu tun brauchen, für uns sorgen können zu unserer Weiterentwickelung.",
      "Während wir die Welt wahrnehmen, während wir in der Welt denken, in ihr fühlen, in ihr wollen, während wir unseren Erinnerungsschatz aufspeichern, um im physischen Dasein ein zu­sammenhängendes Sein zu haben, arbeiten hinter alle dem, hinter diesem unserem bewußten Leben die göttlich-geistigen Wesenheiten. Sie lenken fort den Strom der Zeit.",
      "Sie haben uns entlassen in den Raum, damit wir in diesem Raume gerade so viel Bewußtsein haben, als es diese Götter für gut finden uns zu lassen, wenn sie hinter diesem Bewußtsein unsere Geschicke nach dem großen Menschheitsideale, nach dem Ideale der Götterreligion weiter lenken wollen.",
      "Blicken wir so auf unser Inneres - jetzt auf dasjenige Innere, das wir mit unserem Bewußtsein gar nicht einmal in normalen Verhältnissen des Lebens schauen und erforschen können -, versuchen wir uns zu durchdringen mit der Empfindung: Da in dir lebt etwas, was du allerdings mit den normalen Kräften des Menschenlebens nicht durchschaust, was aber dein tiefstes inneres Seelisches ist, suchen wir es",
      "gewahr zu werden in uns, dieses tiefere in uns verborgene Seelische, und versuchen wir dann gewahr zu werden, wie in diesem Seelischen, das wir selber nicht lenken, die Götter walten, der Gott in uns waltet:",
      "da bekommen wir das rechte Gefühl von dem in uns waltenden Gott. Und daß ein solches Gefühl entstehe, ein solches rechtes Ostergefühl, dafür möchte ich eigentlich die heutigen Worte gesprochen haben, nicht so sehr wegen ihres theoretischen Inhaltes.",
      "Wenn - hinblickend auf das, was sich der Seele darstellt, wenn sie im Raume gleichsam aus sich herausgeht, den Raum erfüllend - diese Seele wissen, lernen kann: Aus dem Göttlichen bin ich geboren, so kann sie durch das heute Gesagte dieses Wissen noch vertiefen, indem sie gewahr werden kann: Mit all dem, was ich weiß, mit all dem, was im Wahrnehmen, Denken, Fühlen und Wollen meiner Seele zugäng­lich ist, bin ich herausgeboren aus einem tieferen Seelischen, aus jenem Seelischen in mir, das noch bei dem Göttlichen ist, das im Zeitenstrom dahinfließt, aber mit dem Göttlichen dahinfließt. Ein Wissen können wir gewahren, das sich ausdrücken kann in einem noch viel tieferen Sinne als derjenige, der gestern gemeint sein konnte am Ende unserer Betrachtung. In einem noch viel tieferen Sinn können wir heute das Wort als Ergebnis unserer Betrachtung hinstellen: Aus dem Gott sind wir geboren. Denn wir gewahren, daß diese Seele mit dem, was sie von sich selber wissen kann, in jedem Zeitpunkt aus dem Göttlichen heraus geboren wird, so daß wir in jedem Zeitpunkt unser tiefstes Inneres erfüllen dürfen mit diesem: Aus dem Gott sind wir geboren.",
      "Ex deo nascimur."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Es war gestern meine Aufgabe, im Zusammenhang mit einer Be­trachtung über Denken, Fühlen, Wollen und Wahrnehmen elnige esoterische Erfahrungen mitzuteilen, welche sich der Menschenseele ergeben, wenn sie geistesforscherisch außer dem Leibe mit der Ab­sicht lebt, etwas über das seelische Innere und seine Wesenheit zu erfahren.",
        "Heute wird es meine Aufgabe sein, von einer anderen Seite her solche Erlebnisse anzuführen, weil wir nur dann, wenn wir von den verschiedensten geistigen Gesichtspunkten aus das Leben be­trachten, wirklich Aufschluß über dieses Leben gewinnen können."
      ],
      [
        "Stellen Sie sich einmal richtig vor, wie gestern versucht worden ist zu zeigen, was die Menschenseele sieht, wenn sie zunächst auf die eigene Leiblichkeit und das, was physisch damit zusammenhängt, von außerhalb des Leibes zurückblickt, und was sie dann nachher erlebt; also was des Menschen astralischer Leib und Ich erleben, wenn sie sich immer mehr und mehr erkraften in dem Raum, den sie gleichsam außerhalb des Leibes betreten haben.",
        "Es gibt nun noch einen anderen Weg, gewissermaßen dasselbe zu betrachten.",
        "Das ist ja gerade das Bedeutsame wirklicher geistiger Betrachtungsweise, daß man im Grunde genommen auf die Rätsel des Daseins durch geistige Be­trachtung erst dadurch kommt, daß man eine Sache von den verschie­densten Seiten aus betrachtet.",
        "Es gibt nämlich noch eine andere Art, aus dem Leib herauszukommen.",
        "Ich möchte sagen, die gestern ge­schilderte Art zeigte uns: es verläßt dabei die Seele den Leib so, daß sie sich aus dem Leibe einfach in den Raum hinaus begibt und da außer dem Leibe zu leben beginnt.",
        "Dieses Aus-dem-Leibe-treten kann noch auf folgende Weise geschehen: Man kann, urn den Weg aus sich heraus zu finden, gerade zunächst tiefer in sich hineinzu­kommen versuchen.",
        "Man kann versuchen, an die Erfahrungen anzu­knüpfen mit dem, was in der Seele, man möchte sagen, der geistigen Erfahrung am ähnlichsten ist.",
        "Man kann versuchen, mit unserem Gedächtnis an die Erlebnisse anzuknüpfen.",
        "Es wurde ja öfter gesagt:"
      ],
      [
        "Dadurch, daß wir als Menschenseelen imstande sind, nicht nur etwas wahrzunehmen, zu denken, zu fühlen und zu wollen, sondern die Gedanken und Wahrnehmungen aufzubewahren als Gedächtnisschatz, dadurch verwandeln wir unser Innenleben eigentlich schon in etwas Geistiges.",
        "Und ich habe in meinem öffentlichen Vortrage darauf hingewiesen, daß der französische Philosoph Bergson sogar schon darauf gekommen ist, daß man das, was als Gedächtnisschatz in der Seele des Menschen vorhanden ist, nicht als irgendwie mit dem Leiblichen unmittelbar zusammenhängend betrachten kann; daß man es vielmehr als eine seelische Innerlichkeit betrachten muß, als etwas, was die Seele entwickelt, was rein geistig-seelisch vorhanden ist."
      ],
      [
        "Und in der Tat, wenn in dem hellseherischen Bewußtsein die Imagination beginnt, wenn aus dem Dunkel des geistigen Daseins die ersten Eindrücke herauftauchen, so sind diese Eindrücke in ihrer Qualität, in ihrer ganzen Wesenheit sehr ähnlich jenem Seeleninhalt, der als Gedächtnisschatz in uns ist.",
        "Wie Erinnerungsbilder, aber jetzt doch wiederum wie etwas unendlich viel Geistigeres, treten die Offen­barungen aus der geistigen Welt bei uns auf, wenn wir mit dem hell­seherischen Bewußtsein wahrzunehmen beginnen.",
        "Wir merken dann gleichsam, daß unser Gedächtnlsschatz das erste wirklich Geistige ist, das erste, wodurch wir uns gewissermaßen schon aus unserem Leibe herausheben, daß wir dann aber weiter gehen müssen, daß wir solche im Geistigen schwebende Bilder, wie das Gedächtnis sie uns bietet -allerdings von viel größerer Lebendigkeit - aus Geistestiefen herauf-heben müssen, die nicht unserem Erleben angehören wie die Erinne-rungsvorstellungen, daß gleichsam hinter dem Gedächtnis etwas heraufzieht.",
        "Das muß festgehalten werden: es zieht etwas herauf aus fremden geistigen Gebieten, während der Gedächtnisschatz herauf-zieht aus dem, was wir im Physischen miterlebt haben."
      ],
      [
        "Wenn wir nun versuchen, den geistigen Blick zurückzulenken auf die Erlebnisse unseres Ich während der Jahre, die wir Seit dem Zeit­punkte unserer Kindheit erlebt haben, zu dem unsere Erinnerung zurückreicht, wenn wir versuchen, von allem Äußeren abzusehen und ganz in uns hineinzuleben, so daß wir uns immer mehr in unsere Erinnerungen hineinfin den, aus unserem Erinnerungsschatz auch das"
      ],
      [
        "heraufholen, was uns gewöhnlich nicht gegenwärtig ist, dann nähern wir uns immer mehr und mehr dem Zeitpunkt, bis zu dem wir uns zurückerinnern können.",
        "Und wenn wir solches oft vornehmen, wenn wir uns sogar eine gewisse Praxis darin aneignen - und wir können das - sonst längst vergessene Erinnerungen heraufzuholen, so daß wir eine stärkere Kraft des Sich-Erinnerns entwickeln, wenn wir immer mehr und mehr Vergessenes heraufholen und dadurch unsere Kraft, die die Erinnerungen heraufschafft, stärker machen, dann werden wir sehen, daß, ich möchte sagen, wie auf einer Wiese zwischen den einzelnen grünen Grashalinen und Graspflanzen Blumen auftauchen, dann zwischen den Erinnerungen Bilder, Imaginationen auftauchen von etwas, was wir vorher nicht gekannt haben.",
        "Es ist etwas, was wirklich so auftaucht wie die Blumen auf der Wiese zwischen den Graspflanzen, was aber aus ganz anderen geistigen Tiefen herauf-kommt als die Erinnerungen, die eben nur aus unserer eigenen Seele herauftauchen.",
        "Und wir lernen dann unterscheiden das, was irgendwie mit unseren Erinnerungen zusammenhängen könnte, von dem, was also herauftaucht aus geistigen Untergründen und geistigen Tiefen.",
        "Und so leben wir uns nach und nach in die Möglichkeit ein, eine Kraft zu entfalten, das Geistige herauszuholen aus seinen Untergründen."
      ],
      [
        "Dadurch aber gelangen wir auf eine andere Weise aus unserem Leibe heraus als auf die gestern beschriebene Art.",
        "Bei der gestern beschriebenen Art verlassen wir den Leib gewissermaßen unmittelbar.",
        "Bei der heute gemeinten Art gehen wir zuerst unser Leben zurück, durchlaufen unser Leben.",
        "Wir versenken uns in unser Innenleben, gewöhnen uns, durch die Erstarkung der Erinnerungskraft in unse­rem Innenleben zwischen unseren Erinnerungen Geistiges hervorzu­holen aus der geistigen Welt, und so gelangen wir endlich dazu, hin-auszudringen durch unsere Geburt, durch die Zeitenfolgen über un­sere Empfängnis hinaus, in die geistige Welt, in der wir gelebt haben, bevor wir uns zu unserer jetzigen Inkarnation mit einer physischen Vererbungssubstanz verbunden haben.",
        "Wir gelangen, unser Leben durcheilend, hinaus in die geistige Welt, zurück in die Zeit, bevor wir eben hereingetreten sind in diese Inkarnation.",
        "Das ist die andere Art, den Leib zu verlassen, hineinzukommen in das Geistige.",
        "Und diese"
      ],
      [
        "Art weist einen großen Unterschied auf gegenüber der gestern be­schriebenen.",
        "Merken Sie wohl auf diese Unterschiede, denn gerade in diesem Vortragszyklus habe ich so manche Feinheiten und Intimi­täten des geistigen Lebens vor Ihnen mitzuteilen.",
        "Aber es ist schwie­rig, auf diese Feinheiten und Intimitäten in geeigneten Worten hinzu­weisen.",
        "Und nur, wenn man versucht, gerade solche Unterscheidungen zu fassen, kommt man richtig in die Dinge hinein und gewinnt ein sicheres Denken über dieselben."
      ],
      [
        "Wenn man so, wie ich es jetzt beschrieben habe, den Leib verläßt, so kommt man nämlich ganz anders aus seinem Leibe heraus.",
        "Wenn man auf die gestern beschriebene Weise herauskommt aus seinem Leibe, so fühlt man sich wie außerhalb seines Leibes in dem Außen-raum.",
        "Ich konnte beschreiben, wie man sich verbreitet über den Außenraum, wie man zurückschaut auf seinen physischen Leib.",
        "Man tritt aus sich heraus und füllt gleichsam den Raum aus, man tritt in den Raum hinaus.",
        "Wenn man aber durchinacht, was jetzt hier gemeint ist, dann tritt man aus dem Raum selber hinaus, dann hört der Raum auf, für einen eine Bedeutung zu haben; man verläßt den Raum und man ist dann nur noch in der Zeit.",
        "So daß bei einem solchen Verlassen des Leibes das Wort aufhört, einen Sinn zu haben: Ich bin außerhalb meines Leibes - denn das Außerhalb bedeutet ein räumliches Ver­hältnis.",
        "Man fühlt sich dann eben nicht gleichzeitig mit seinem Leibe, man erlebt sich in der Zeit.",
        "In der Zeit, in der man war vor der In­karnation, in einem Vorher.",
        "Und den Leib erschaut man als nachher existierend.",
        "Man ist wirklich nur in der fortströmenden, laufenden Zeit darinnen.",
        "Und anstelle des Außen und Innen ist ein Vorher und Nachher getreten."
      ],
      [
        "Dadurch ist man imstande, durch ein solches Herausgehen aus seiner Leiblichkeit, wirklich einzudringen in die Gebiete, die wir durchleben zwischen dem Tod und einer neuen Geburt.",
        "Denn man geht in der Zeit zurück, man lebt sich ein in ein Leben, das man vor diesem Erdenleben gelebt hat.",
        "Und dieses Erdenleben erscheint so, daß wir sagen: Was ist denn dort in der Zukunft, was erscheint uns denn da als Nachher?",
        "Sie sehen da eine genauere Angabe über man­ches, was ich in meinem öffentlichen Vortrage nicht so genau habe"
      ],
      [
        "ausführen können: wie man nämlich im Konkreten hineinkommt in die Gebiete, die man durchlebt zwischen dem Tod und einer neuen Geburt."
      ],
      [
        "Nun ist man auf diesem Wege hinausgezogen aus seinem Leibe, indem man in das vorher im Geiste vollbrachte Leben zurückgekehrt ist, man ist damit aber auch aus dem Raum herausgezogen.",
        "Dadurch hat dieses Verlassen des Leibes - aus dem Jetzt zu dem Früheren -einen viel höheren Grad von Innerlichkeit als das andere Verlassen, und für den Geistesforscher ist in der Tat dieses jetzt geschilderte Verlassen des Leibes von unendlich größerer Bedeutung als das gestern geschilderte, das nicht aus dem Raume herauskommt.",
        "Denn eigentlich begreift man dasjenige, was so recht tiefe Innerlichkeiten der Seele angeht, im Grunde erst auf dem heute beschriebenen Wege.",
        "Und da möchte ich Ihnen zunächst eines anführen, aus dem Sie er­sehen werden, wie man versuchen muß, hinter die Intimitäten und Feinheiten des menschlichen Lebens zu kommen."
      ],
      [
        "Im physischen Leibe hier leben wir unser physisches Leben.",
        "Wir bedienen uns unserer Sinne, nehmen die Welt wahr, wir stellen die Welt vor, fühlen in ihr, versuchen uns durch unsere Handiungen in dieser Welt einen Wert zu geben, wir handeln bewußt durch unseren Leib.",
        "So geht das alltägliche Leben vor sich, so geht das Leben vor sich, insofern wir dem physischen Plan angehören.",
        "Nun muß es aber für jeden Menschen, der seine Menschenwürde wahrhaft in sich er­fühlen will, ein höheres Leben geben; und es hat immer ein höheres Seelenleben gegeben.",
        "Die Religionen, die den Menschen mit höherem Leben erfüllten, waren immer da.",
        "Geisteswissenschaft wird den Men­schen in der Zukunft mit einem solchen höheren Leben erfüllen.",
        "Was will dieses höhere Leben?",
        "Was will dieses Leben, das in Gedanken, in Gefühlen, in Empfindungen hinausgeht über das, was der physische Plan bieten kann, das bei dem einen nur in dunklen Ahnungen auf religiösem Gebiet, bei dem andern in klar umrissenen Linien der Geisteswissenschaft hinausgeht über das, was die Sinne schauen können, was man mit seinem an das Gehirn gebundenen Verstande denken kann, was man mit seinem Leibe in der Welt verrichten kann?"
      ],
      [
        "Nach einem geistigen Leben hin tendiert die menschliche Seele."
      ],
      [
        "Ein geistiges Leben in sich zu erfühlen, von einem solchen geistigen Leben etwas zu wissen, das über das physische Leben hinausgeht, das gibt dem Menschen eigentlich erst seine Würde.",
        "Man könnte sagen: Solange der Mensch im physischen Leibe weilt, sucht er seine Würde zu erhöhen, sucht er seine eigentliche Bestimmung zu erahnen durch ein Leben, das er sich vorstellt als über die physische Welt hinaus­gehend, durch ein Erahnen, Empfinden, Erkennen einer geistigen Welt.",
        "Blicke auf zum Geiste, fühle, daß geistige Kräfte durch die physischen Welten weben: das sind im Grunde genommen die Töne, die das religiöse und das damit verwandte Leben dem Menschen geben sollen.",
        "Und die Sorge des Erziehers, der es mit einem heran­wachsenden Menschenkinde ernst meint, wird sein, dieses Menschen-kind nicht so aufwachsen zu lassen, daß es nur in den äußeren mate­riellen Vorstellungen lebt, sondern ihm Vorstellungen von einer übersinnlichen Welt beizubringen."
      ],
      [
        "Nennen wir jetzt, ohne damit hinweisen zu wollen auf das Eng­umschränkte oder dogmatisch Eingeengte der Religionssysteme, nennen wir das, was so den Menschen hinauszieht aus dieser physi­schen Welt, Religion, und fragen wir gegenüber dem, was wir gerade geschildert haben als ein Hinausgehen der menschlichen Seele über Geburt und Empfängnis in eine dem Erdenleben vorhergehende geistige Welt hinein, wo die Seele auch aus dem Raume heraus ist, fragen wir demgegenüber: Gibt es nun zwischen dem Tod und einer neuen Geburt in der Welt, die wir so betreten, wie wir es auseinander­gesetzt haben, etwas, was man eine Religion jenes Geisterlandes nennen könnte?",
        "Gibt es da drüben etwas, was sich mit dem religiösen Leben auf der Erde vergleichen ließe?",
        "Wir haben schon in manchen Einzelheiten geschildert und werden noch weiter die Vorgänge zu schildern haben, die der Mensch zwischen dem Tod und einer neuen Geburt durchlebt.",
        "Aber jetzt fragen wir uns: Gibt es so etwas wie eine Religion in diesem geistigen Leben?",
        "Etwas, von dem man sagen kann: es steht den Erlebnissen, die wir für das Geisterland schildern, so gegenüber, wie die Hinweise auf die übersinnliche Welt dem All­tagsleben des physischen Planes gegenüberstehen?"
      ],
      [
        "Derjenige, der auf die geschilderte Weise aus seinem Leibe herauskommt,"
      ],
      [
        "der kommt zu der Erkenntnis, daß es so etwas wie eine Art religiösen Lebens da drüben in diesem Geisterlande auch gibt.",
        "Und merkwürdigerweise, während man alles das, was man im Geisterlande um sich herum hat, geistige Wesenheiten und geistige Vorgänge, so erlebt wie man hier physische Wesen und physische Vorgänge erlebt, hat man dort fortdauernd während dieses Lebens, oder wenigstens während eines großen Teiles dieses Lebens zwischen dem Tod und einer neuen Geburt, wie ein mächtiges geistiges Gebilde, das Bild des Menschen-Ideals vor sich.",
        "Alles, was über den Menschen hinaus-geht, hat man hier auf der Erde als Religion; das Menschenideal, man hat es drüben in der geistigen Welt als Religion.",
        "Man lernt verstehen, daß die verschiedenen Wesenheiten der verschiedenen geistigen Hierarchien ihre Absichten, ihre Kräfte zusammenwirken ließen, um im Weltenstrome auf die Art, wie es in meiner «Geheimwissenschaft» beschrieben ist, allmählich den Menschen hervorgehen zu lassen.",
        "Den Göttern schwebte als das Ziel ihrer Schöpfung das Menschenideal vor, und zwar jenes Menschenideal, welches wirklich sich nicht so auslebt, wie jetzt der physische Mensch ist, sondern so, wie höchstes mensch­liches Seelengeistesleben in den vollkommen ausgebildeten Anlagen dieses physischen Menschen sich ausleben könnte."
      ],
      [
        "So schwebt als Ziel, als höchstes Ideal, als die Götterreligion den Göttern ein Bild der Menschheit vor.",
        "Und wie am fernen Ufer des Götterseins schwebt für die Götter der Tempel, der als höchste künstlerische Götterleistung das Abbild des göttlichen Seins im Menschenbilde hinstellt.",
        "Und das ist das Eigentümliche, daß der Mensch, während er sich in dem Geisterlande zwischen dem Tod und einer neuen Geburt heranbildet, sich nach und nach dort immer reifer und reifer macht zum Schauen dieses Menschheitstempels, dieses hohen Menschheitsideals.",
        "Und während wir hier auf Erden das religiöse Leben so empfinden, daß es unsere freie Tat sein muß, daß wir es aus uns herausholen müssen, daß es dem materialistischen Sinn auch möglich ist, das Religiöse zu verleugnen, ist das Umgekehrte im Geisterland zwischen dem Tod und einer neuen Geburt der Fall.",
        "Je mehr wir in die zweite Hälfte der Zeit zwischen dem Tod und einer neuen Geburt hineinleben, desto deutlicher steht vor uns, so daß wir"
      ],
      [
        "es nicht übersehen können, so daß es immer vor unserem geistigen Blicke ist, das hehrste Menschenideal, das Götterziel der Welten.",
        "Hier auf Erden kann der Mensch irreligiös sein, weil seine Seele gegenüber dem Physischen den Geist übersehen kann Drüben ist es unmöglich, daß der Mensch nicht das Götterziel schaut; denn das stellt sich ihm mit Sicherheit vor Augen.",
        "So steht, namentlich in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt, wie am Ufer des Seins, das heißt am Ufer der dahinströmenden Zeit -nehmen Sie jetzt alle Ausdrücke so, daß wir es zu tun haben außerhalb des Raumes mit der Zeit - so steht es da, das Menschheitsideal.",
        "Eine Erkeunmisreligion kann es drüben nicht geben; denn erkennen muß man das, was religiöser Inhalt ist.",
        "Das, was ich jetzt geschildert habe, ist drüben religiöser Inhalt.",
        "In diesem Sinne irreligiös kann kein Mensch sein, daß er das religiöse Ideal des Geisterlandes nicht vor sich hätte.",
        "Denn das steht durch sich selbst da, es ist Götterziel und wird hingestellt als die mächtigste, glorioseste Imagination, wenn wir die zweite Hälfte unseres Lebens zwischen dem Tod und einer neuen Geburt antreten.",
        "Aber wenn wir so auch nicht eine Erkenntnis-religion drüben entwickeln können, so entwickeln wir doch unter der Anleitung höherer geistiger Wesenheiten, die da drüben für den Menschen tätig sind, eine Art Religion."
      ],
      [
        "Während uns aber Erkennen, Schauen nicht gelehrt werden kann, weil es ja selbstverständlich ist, muß unser Wollen, unser wollendes Fühlen, unser fühlendes Wollen angeeifert werden in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt, um zu dem, was wir da sehen, wirklich hinzustreben.",
        "In unser wollendes Fühlen, in unser fühlendes Wollen fließen Götterwille, Götterfühlen ein, damit wir den Weg in dieser Richtung wählen in der zweiten Hälfte unseres Lebens zwischen dem Tod und einer neuen Geburt.",
        "Es sind ja alle Ausdrücke ungeschickt für dieses ganz andersartige Leben, dennoch darf der Ausdruck gebraucht werden: hier werden wir in bezug auf unseren Verstand unterrichtet, nur wenn ein Lehrer durch die Vorstellung geht, wirkt er hier auf Erden weiter auf unser Gefühl.",
        "Drüben ist es so, daß, wenn man den weiter noch zu schildern­den Zeitpunkt der Mitte zwischen dem Tod und einer neuen Geburt,"
      ],
      [
        "wenn man das, was ich in meinem letzten Mysteriendrama «Der Seelen Erwachen» die Mitternachtstunde genannt habe, überschritten hat, daß dann zunächst eine gewisse Dumpfheit da ist in bezug auch auf das Wollen und Fühlen gegenüber dem, was wie ein herrlicher Tempel in den Fernen der Zeiten steht.",
        "Da durchglühen und durch­wärmen göttliche Kräfte unsere inneren Seelenvermögen: ein Unter­richt ist es, der unmittelbar zu unserem Innern spricht und der sich so äußert, daß wir immer mehr und mehr die Fähigkeit gewinnen, wirk­lich den Weg gehen zu wollen zu dem, was wir so als ein Ideal schauen."
      ],
      [
        "Während wir im physischen Leben einem Lehrer gegenüber-stehen können oder einem Erzieher, und er uns gegenüberstehen kann, und wir uns doch im Grunde genommen so fühlen, daß er von außen herein in unser Herz spricht, fühlen wir, daß unsere geistigen Erzieher der höheren Hierarchien, indem sie uns so erziehen, wie ich es jetzt geschildert habe, unmittelbar in unser Inneres herein ihre eigenen Kräfte strömen lassen.",
        "Irdische Erzieher sprechen zu uns, geistige Erzieher im Leben zwischen dem Tod und einer neuen Geburt geben uns ihr Leben in unsere Seelen herein, indem sie uns geistig religiös erziehen."
      ],
      [
        "Und so fühlen wir sie immer mehr und mehr in uns, diese Erzieher aus den höheren Hierarchien, so fühlen wir uns immer inniger mit ihnen verbunden.",
        "Dadurch aber erkraftet und erstarkt sich unser Innenleben."
      ],
      [
        "Du bist immer mehr und mehr von den Göttern ange­nommen, in dir leben immer mehr und mehr die Götter und sie helfen dir, daß du immer innerlich stärker und stärker wirst!",
        "Das ist es, was als ein Grundgefühl durchgeht durch dieses Leben zwischen dem Tod und einer neuen Geburt, namentlich in seiner zweiten Hälfte."
      ],
      [
        "So sehen wir, wie alles in diesem Leben daraufhin angelegt ist, daß unsere Erlebnisse unmittelbar in den Tiefen unserer Seele selbst ab­laufen.",
        "Nun kommen wir aber, indem wir also von den Göttern unter­richtet werden, an einen bestimmten Punkt des Erlebens zwischen dem Tod und einer neuen Geburt.",
        "An einen wichtigen Punkt kommen wir.",
        "Es ist, ich möchte sagen, in der Zeiten fernster Ferne, wo wir das Menschheitsideal erblicken; die Kräfte aber, die in uns durch diese unsere göttlich-geistigen Erzieher gelegt werden können, die sind abhängig von dem, was wir im Laufe unserer Inkarnationen, im Laufe"
      ],
      [
        "unseres vorhergehenden Menschenlebens aus uns gemacht haben.",
        "Und so stehen wir, indem wir heranleben von der Weltenmitternacht, gerade in der Mitte zwischen dem Tod und einer neuen Geburt, und immer weiterleben in die Zeiten hinein und in fernsten Zeiten das Menschheitsideal sehen, dann endlich an einem Punkt, an der letzten Perspektive des Menschheitsideals.",
        "Aber so stehen wir an diesem Punkt, daß wir uns nun sagen müssen - wir sagen es uns natürlich nicht, wir erleben es ganz innerlich, aber man muß sich mit den Worten des gewöhnlichen Lebens aussprechen -: Göttlich-geistige Kräfte haben an dir gewirkt, sind immer innerlicher in deiner Seele geworden, leben jetzt in dir; aber jetzt bist du an dem Punkte, wo du dich nicht mehr weiter mit diesen Kräften durchdringen kannst, denn du müßtest viel vollkommener sein, wenn du weitergehen wolltest als bis hierher."
      ],
      [
        "Und jetzt kommt ein wichtiger Entscheidungspunkt.",
        "In diesem Augenblick tritt an uns eine harte Versuchung heran!",
        "Die Götter haben es gut mit uns gemeint, sie haben uns alles das gegeben, was sie uns zunächst geben können, sie haben uns so stark gemacht, als es nach Maßgabe der Kraft möglich war, die wir im bisherigen Leben uns erworben haben.",
        "So ist diese uns von den Göttern gegebene Stärke in uns, und die Versuchung tritt an uns heran, die uns sagt:"
      ],
      [
        "Ja, du kannst jetzt diesen Göttern folgen, du kannst jetzt alles das, was du bist, gleichsam einfließen lassen in das, was die Götter dir gegeben haben an Kräften, du kannst in die geistigen Welten hinein­gehen.",
        "Denn viel, viel haben dir die Götter gegeben."
      ],
      [
        "Man kann sich ganz vergeistigen: diese Aussicht steht vor einem.",
        "Aber man kann das nur, indem man seinen Weg von der Bahn nach dem großen Menschheitsideale hin ablenkt, indem man herausgeht aus der Bahn.",
        "Das heißt mit anderen Worten: man schlägt den Weg em in die geistigen Welten, indem man all seine Unvollkommenheiten in die geistigen Welten mit hineinnimmt.",
        "Sie wurden sich dort schon in Vollkommenheiten verwandeln.",
        "Sie täten es wirklich.",
        "Man könnte mit den Unvol kommenheiten hinein, man wurde mit ihnen, weil man von göttlichen Kräften durchdrungen wäre, ein Wesen sein.",
        "Aber dieses Wesen müßte verzichten auf Anlagen, die es doch in sich hat,"
      ],
      [
        "die es noch nicht auf seinem bisherigen Wege ausgebildet hat und die nach der Richtung des großen Menschheitsideales liegen; auf die müßte es verzichten.",
        "Jedesmal, bevor wir zu einer Erderinkarnation gehen, tritt an uns die Versuchung heran, in der geistigen Welt zu bleiben, in den Geist einzutreten und sich vorwärts zu entwickeln mit demjenigen, was man schon ist, was jetzt ganz durchgöttlicht ist, und zu verzichten auf das, was man als Mensch noch immer mehr werden könnte auf der Bahn nach dem fernen religiösen Ideal der göttlich-geistigen Welt hin.",
        "Es tritt die Versuchung heran, irreligiös für das Geisterland zu werden."
      ],
      [
        "Diese Versuchung tritt um so mehr heran, als in keinem Moment der Menschheitsentwicklung Luzifer eine größere Gewalt hat über den Menschen als in diesem Augenblick, wo er ihm einbläst: Ergreife jetzt die Gelegenheit, du kannst im Geiste bleiben, du kannst alles das, was du entwickelt hast, in das geistige Licht überführen!",
        "Und vergessen zu machen der Seele, soweit es irgend möglich ist, sucht Luzifer das, was noch als Anlagen vorhanden ist, was da steht in dem fernen Tempel am fernen Ufer des Zeitenseins."
      ],
      [
        "So wie die Menschheit jetzt ist, würde der Mensch nicht in der Lage sein, in diesem Punkt der Versuchung Luzifers zu widerstehen, wenn nicht die Geister, deren Gegner Luzifer ist, jetzt die Angelegenheiten des Menschen übernehmen würden.",
        "Und es tritt der Kampf der den Menschen zu seinem Ideale vorwärtsleitenden Götter ein, der die Götterreligion bekennenden Götter mit Luzifer um eine Menschen-seele.",
        "Und das Ergebnis dieses Kampfes ist, daß das Urbild, das sich der Mensch von seinem irdischen Dasein gebildet hat, herausgeworfen wird aus der Zeit in den Raum, angezogen wird magnetisch vom Raumesdasein.",
        "Dies ist auch der Moment, wo jene magnetische An-ziehung durch das Elternpaar auftritt, wo der Mensch hineinversetzt wird in die Raumes sphären, Verwandtschaft gewinnt mit der Raumes-sphäre.",
        "Dadurch aber wird alles dasjenige um den Menschen herum verhüllt, was ihm die Versuchung einflößen könnte, nur in der geisti­gen Welt zu bleiben.",
        "Und diese Verhüllung drückt sich aus eben in seiner Umhüllung mit der Leiblichkeit.",
        "Er wird in die Leiblichkeit eingefügt, damit er nicht schaut, was Luzifer vor ihn hinstellen will."
      ],
      [
        "Und wenn er in die leibliche Hülle eingehüllt ist und durch seine leib­lichen Sinne und seinen leiblichen Verstand nunmehr die Welt an-sieht, so sieht er nicht das, was er sonst in der geistigen Welt, durch den Versucher verführt, anstreben möchte, er sieht es nicht, er schaut diese Welt geistiger Wesenheiten und Vorgänge von außen, wie sie sich für die Sinne und den an das Gehirn gebundenen Verstand offen­baren.",
        "Und indem er im Sinnesleibe ist, übernehmen die ihn vorwärts bringenden Geister seine Entwickelung."
      ],
      [
        "Und fragen wir uns jetzt: Wie viel geht mit uns vor zwischen der Geburt und dem Tode in den unterbewußten Seelentiefen, wie viel geht mit uns vor, ohne daß wir davon wissen ? - Wenn wir uns so leiten müßten, daß wir alles bewußt vollbringen, so könnten wir das Erden-dasein durchaus nicht vollenden.",
        "Ich habe schon darauf hingewiesen in meinem Buche über «Die geistige Führung des Menschen und der Menschheit»: der Mensch muß, indem er in die physische Inkarnation tritt, selber erst plastisch an seinem Gehirn- und Nervensystem arbei­ten."
      ],
      [
        "Er arbeitet, aber er arbeitet unbewußt daran.",
        "Das alles ist der Ausdruck einer viel größeren Weisheit als diejenige ist, die der Mensch begreifen kann mit seinem sinnlichen Verstand.",
        "In uns waltet zwischen der Geburt und dem Tode eine Weisheit, die hinter der Welt vor­handen ist, die wir mit unseren Sinnen anschauen und über welche wir mit unserem an das Gehirn gebundenen Verstand denken."
      ],
      [
        "Da­hinter ist sie vorhanden, diese Weisheit; sie ist verhüllt vor uns zwischen der Geburt und dem Tode.",
        "Aber sie waltet, webt, wirkt in uns in den unterbewußten Seelentiefen, und sie muß sozusagen m diesen unterbewußten Seelentiefen des Menschen Angelegenheiten in die Hand nehmen, weil der Mensch auf einige Zeit hinweggerückt werden muß von einem Anblick, der für ihn versucherisch wäre."
      ],
      [
        "Die ganze Zeit, während welcher wir in unserem physischen Leibe leben, würden wir unter sonst normalen Verhältnissen, ohne daß wir eben durch eine sorgfältige Schulung in die geistige Welt eingeführt wer­den, wenn der Hüter der Schwelle uns das Hineinschauen in die geistigen Welten nicht vorenthielte, unser ganzes Leben Schritt für Schritt versucht sein, unsere noch unvollkommenen, unsere noch nicht herausgekommenen Menschenanlagen fallen zu lassen und dem Hinaufschwung"
      ],
      [
        "in die geistigen Welten zu folgen, aber mit unseren Unvoll­kommenheiten.",
        "Wir brauchen die Zeit unseres Erdenlebens, um in dieser Zeit der Versuchung Luzifers entrückt zu sein."
      ],
      [
        "Bis zu dem angegebenen Zeitpunkt, wo wir in den Raum heraus­geführt werden, hat Luzifer noch nicht die Gewalt, denn da gibt es noch immer eine Möglichkeit, vorwärts zu schreiten, aber er kommt eben in dem Moment heran, wo wir an dem Entscheidungspunkte angelangt sind.",
        "Durch unser vorhergehendes Leben können wir nicht vorwärts schreiten, so wollen wir mit den Unvollkommenheiten ab-irren und in der geistigen Welt verbleiben.",
        "Davor schützen uns die fortschreitenden Götter, deren Gegner Luzifer ist, indem sie uns dieser geistigen Welt entrücken, indem sie sie vor uns verhüllen, und das, was aus dieser geistigen Welt heraus geschehen muß an uns, hinter unserem Bewußtsein vollziehen."
      ],
      [
        "So stehen wir da als Menschen in der Welt, mit unserem Bewußtsein in unserem physischen Leibe, und sagen uns: Habt Dank, ihr Götter!",
        "So viel habt ihr uns gelassen von der Möglichkeit, etwas zu wissen von der Welt, als gerade gut ist für uns. - Denn blickten wir hinter die Schwelle desjenigen, was unser Bewußtseinshorizont ist, so stünden wir in jedem Augenblick vor der Gefahr, unser Menschheits­ziel nicht erreichen zu wollen.",
        "Aus jenem helleren, höheren Bewußt­seinszustand, in dem wir zwischen dem Tod und einer neuen Geburt sind, wo wir geistige Welten und geistige Wesenheiten um uns herum haben, wo wir im Geiste sind, mußten wir in die Welt des Raumes versetzt werden, damit uns in der Welt des Raumes verhüllt werde die Welt, die wir nicht ertragen könnten, bis wir die Zeit durchge­macht haben zwischen der Geburt und dem Tode, die Zeit, in der wir, dadurch, daß wir der geistigen Welt entrückt waren, dadurch daß diese geistige Welt in dieser Zeit nicht auf uns gewirkt hat, daß nur materielle Dinge uns umgeben haben, wiederum einen neuen Antrieb empfangen haben nach den fernen Zielen des Menschheits­ideales hin.",
        "Denn in der ganzen Zeit, während welcher wir auf Erden leben, während welcher wir mit unserem Bewußtsein nicht in die geistige Welt hineinsehen, wirken nun wiederum, indem sie jetzt nicht durch unser Bewußtsein gestört sind, indem sie nicht gestört"
      ],
      [
        "sind dadurch, daß wir versucht sind, Luzifer zu folgen, in uns die uns vorwärtstreibenden göttlichen Geister.",
        "Und sie flößen uns wiederum so viel Kraft ein, daß, wenn wir durch die Pforte des Todes gehen, wir wiederum ein Stück vorwärtsdringen können nach dem Mensch­heitsideale hin."
      ],
      [
        "Das ist auch noch ein Geheimnis, das hinter dem Menschendasein steht, das ich mit diesen Worten angedeutet habe.",
        "Und ich denke, es ist eine gute Osterempfindung, hinzuschauen auf jene Verhältnisse des Lebens, die mehr durch innerliches Herausgehen aus dem Leibe erreicht werden, hinzuschauen auf die Verhältnisse zwischen dem Tod und einer neuen Geburt, und dem Leben, das wir nachher im physi­schen Leibe gewinnen."
      ],
      [
        "Da blicken wir hin auf dieses Leben zwischen dem Tod und einer neuen Geburt und werden gewahr der Führung der guten göttlich-geistigen Wesen, die uns vorwärts helfen.",
        "Wie zu unserer Vergangenheit im Geiste sehen wir zu diesen göttlich-geistigen Wesen auf, und wir verstehen jetzt von diesem unserem Sein im Leibe zwischen der Geburt und dem Tode, daß es uns verliehen wor­den ist von den Göttern, damit die Götter eine Weile, ohne daß wir etwas dazu zu tun brauchen, für uns sorgen können zu unserer Weiterentwickelung."
      ],
      [
        "Während wir die Welt wahrnehmen, während wir in der Welt denken, in ihr fühlen, in ihr wollen, während wir unseren Erinnerungsschatz aufspeichern, um im physischen Dasein ein zu­sammenhängendes Sein zu haben, arbeiten hinter alle dem, hinter diesem unserem bewußten Leben die göttlich-geistigen Wesenheiten.",
        "Sie lenken fort den Strom der Zeit."
      ],
      [
        "Sie haben uns entlassen in den Raum, damit wir in diesem Raume gerade so viel Bewußtsein haben, als es diese Götter für gut finden uns zu lassen, wenn sie hinter diesem Bewußtsein unsere Geschicke nach dem großen Menschheitsideale, nach dem Ideale der Götterreligion weiter lenken wollen."
      ],
      [
        "Blicken wir so auf unser Inneres - jetzt auf dasjenige Innere, das wir mit unserem Bewußtsein gar nicht einmal in normalen Verhältnissen des Lebens schauen und erforschen können -, versuchen wir uns zu durchdringen mit der Empfindung: Da in dir lebt etwas, was du allerdings mit den normalen Kräften des Menschenlebens nicht durchschaust, was aber dein tiefstes inneres Seelisches ist, suchen wir es"
      ],
      [
        "gewahr zu werden in uns, dieses tiefere in uns verborgene Seelische, und versuchen wir dann gewahr zu werden, wie in diesem Seelischen, das wir selber nicht lenken, die Götter walten, der Gott in uns waltet:"
      ],
      [
        "da bekommen wir das rechte Gefühl von dem in uns waltenden Gott.",
        "Und daß ein solches Gefühl entstehe, ein solches rechtes Ostergefühl, dafür möchte ich eigentlich die heutigen Worte gesprochen haben, nicht so sehr wegen ihres theoretischen Inhaltes."
      ],
      [
        "Wenn - hinblickend auf das, was sich der Seele darstellt, wenn sie im Raume gleichsam aus sich herausgeht, den Raum erfüllend - diese Seele wissen, lernen kann: Aus dem Göttlichen bin ich geboren, so kann sie durch das heute Gesagte dieses Wissen noch vertiefen, indem sie gewahr werden kann: Mit all dem, was ich weiß, mit all dem, was im Wahrnehmen, Denken, Fühlen und Wollen meiner Seele zugäng­lich ist, bin ich herausgeboren aus einem tieferen Seelischen, aus jenem Seelischen in mir, das noch bei dem Göttlichen ist, das im Zeitenstrom dahinfließt, aber mit dem Göttlichen dahinfließt.",
        "Ein Wissen können wir gewahren, das sich ausdrücken kann in einem noch viel tieferen Sinne als derjenige, der gestern gemeint sein konnte am Ende unserer Betrachtung.",
        "In einem noch viel tieferen Sinn können wir heute das Wort als Ergebnis unserer Betrachtung hinstellen: Aus dem Gott sind wir geboren.",
        "Denn wir gewahren, daß diese Seele mit dem, was sie von sich selber wissen kann, in jedem Zeitpunkt aus dem Göttlichen heraus geboren wird, so daß wir in jedem Zeitpunkt unser tiefstes Inneres erfüllen dürfen mit diesem: Aus dem Gott sind wir geboren."
      ],
      [
        "Ex deo nascimur."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "DRITTER VORTRAG Wien, 11. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Zunächst werden wir heute aufmerksam zu machen haben auf einzelne positive okkulte Forschungsresultate, welche auf der einen Seite seht geeignet sind, uns in das Wesen des Menschen hineinzufühten, die aber auf der anderen Seite uns zeigen, als welch kompliziertes Wesen eigentlich dieser Mensch in der Welt darinnensteht. Aber können wir denn anders denken, als daß dieser Mensch als ein recht kompliziertes Wesen in der Welt darinnensteht, wenn wir erwägen, daß das eigent­liche Idealbild des Menschen, das, was der Mensch sein kann, wenn er alle in ihm liegenden Anlagen wirklich zur Entfaltung bringt, im Grunde der Inhalt der Götter-Religion ist, und daß im Grunde ge­nommen all die geistigen Wesenheiten der verschiedenen Hierarchien, die man im Zusammenhang mit der menschlichen Natur kennen­lernen kann, ihre Ziele zusammenwirken lassen, um aus dem gesamten Kosmos heraus den Menschen wie den Sinn dieses Kosmos aufzu­bauen!",
      "Das erste, was zu sagen sein wird, ist, daß der Mensch mit den Wahrnehmungen, die er von der äußeren Welt empfängt, so wie sie ihm in seinem Bewußtsein erscheinen, eigentlich nur einen kleinen Teil dessen wirklich aufnimmt, was da auf ihn einstürmt. Indem der Mensch in der physischen Welt darinnensteht, seine Sinnesorgane geöffnet hat, mit seinem Verstand, der an sein Gehirn, an sein Nerven-system gebunden ist, die Welt betrachtet und sich zu erklären versucht, was da auf diese Weise an den Menschen herankommt, gelangt eigent­lich nur ein kleiner Teil dessen, was da heranstürmt, wirklich zur menschlichen Vorstellung, tritt nur ein kleiner Teil wirklich in das Bewußtsein des Menschen ein. Im Licht und in den Farben, im Ton und so weiter ist viel mehr enthalten, als dem Menschen zum Bewußt-sein kommt. Die äußerliche materialistische Physik spricht in ihrer kindlichen Weltauffassung davon, daß hinter den Farben, hinter dem Licht und so weiter materielle Vorgänge seien, Atomschwingungen und dergleichen. Das ist eben wirklich nur, man kann schon sagen,",
      "eine kindliche Weltauffassung. Denn in Wahrheit stellt sich das Fol­gende ein.",
      "Wir müssen mit dem heliseherischen Blick das menschliche Wahr­nehmen erforschen, denn von diesem Beobachten des wirklichen Wahrnehmungsvorganges kann erst ein Verständnis über das Ver­hältnis des Menschen zu der Umwelt, die ihm vorliegt, ausgehen, wenn wir auch nur auf dem physischen Plane bleiben. Etwas höchst Eigentümliches zeigt sich, wenn man den Wahrnehmungsvorgang hellseherisch beobachtet.",
      "Sagen wir, irgend etwas wirke auf unser Auge, wir nehmen Licht oder Farbe wahr, wir haben also in unserem Bewußtsein die Empfindung des Lichtes oder der Farbe: das Merk­würdige, was man nun entdeckt durch die Geistesforschung, ist, daß im Menschenwesen nicht nur dieses Licht und diese Farbe auftreten, sondern daß da wie im Gefolge von Licht und Farbe gleichzeitig mit unserer Empfindung von Licht- und Farbenbildem, rlaan möchte sagen, eine Art von Licht- oder Farbenleichnam in uns auftritt. Unser Auge veranlaßt uns, daß wir die Licht- und Farbenempfindung haben.",
      "Man könnte also sagen: das Licht strömt zu und bereitet uns die Lichtempfindung, aber tiefer in unser Wesen hineinschauend, ent­decken wir, daß während in unserem Bewußtsein das Licht sitzt, unser Menschenwesen durchzogen wird von etwas, was in diesem Menschenwesen sterben maß, damit wir die Lichtempfindung haben können. Keine Wahrnehmung, keine Empfindung von außen können wir haben, ohne daß sich gleichsam durchdrückt durch diese Empfin­dung eine Art Leichenbildung, die wie im Gefolge dieser Empfindung auftritt.",
      "Geistesforschung muß eben sagen: Da schaue ich mir den Menschen an, ich weiß, jetzt empfindet er rot. Ich sehe aber, daß dieses Rot, das in seinem Bewußtsein lebt, von sich gleichsam etwas aus­gießt, sein ganzes Wesen, insofern es in seine Haut und in die Grenzen seines Ätherleibes eingeflossen ist, durchdringt mit etwas, was wie der Leichnam der Farbe ist, was etwas ertötet in dem Menschen.",
      "Denken Sie nur einmal, daß wir eigentlich immer, indem wir der physischen Welt gegenüberstehen und unsere Sinnesorgane offen haben, die Leichname aller unserer Wahrnehmungen wie Phantome, aber wirksame Phantome, in uns aufnehmen. Immer stirbt etwas in",
      "uns, indem wir die Außenwelt wahrnehmen. Es ist das ein höchst eigentümliches Phänomen. Und der Geistesforscher muß sich fragen: Ja, was geschieht denn da? Was ist denn die Ursache von diesem höchst eigenartigen Phänomen?",
      "Da muß man betrachten, wie es sich eigentlich mit dem verhält, was da wie Licht an uns heranstürmt. Dieses Licht hat eben vieles hinter sich. Es ist gleichsam das, was das Licht offenbart, nur der Vorposten desjenigen, was an uns heranstürmt. Hinter dem Licht steht allerdings nicht jene Wellenbewegung, von der die äußere Physik phantasiert, sondern hinter dem Licht, hinter allen Wahrnehmungen, hinter allen Eindrücken steht zunächst das, was wir nur erfassen, wenn wir geisteswissenschaftlich die Welt anschauen durch Imagina­tionen, durch schöpferische Bilder. In dem Augenblick, wo wir alles sehen würden, alles wahrnehmen würden, was in dem Licht oder in dem Tone oder in der Wärme lebt, würden wir hinter dem, was uns zum Bewußtsein kommt, die schöpferische Imagination wahrnehmen und in dieser sich wieder offenbarend die Inspiration, und in dieser die Intuition. Es ist dasjenige, was uns zum Bewußtsein kommt als Licht-und Tonempfindung, gleichsam die oberste Schicht, gleichsam nur der Schaum dessen, was an uns heranschwingt, aber es lebt darin, was, wenn es uns zum Bewußtsein käme, zur Imagination, Inspiration, Intuition in uns werden könnte.",
      "Also eigentlich haben wir nur ein Viertel von dem, was an uns heranstürmt, wirklich in der Wahrnehmung gegeben, die anderen drei Viertel dringen in uns ein, ohne daß es uns zum Bewußtsein kommt. Während wir also dastehen und eine Farbenempfindung haben, dringen, gleichsam durch die Fläche der Farbenempfindung, die schöpferische Imagination, die Inspiration, die Intuition in uns ein, versenken sich in uns. Wenn wir sie näher untersuchen, diese drei letzteren Eindringlinge, so finden wir, daß wenn diese Imagination, Inspiration, Intuition, so, wie sie sich durch die Sinnes-empfindungen in unseren Organismus hereindrängen wollen, wirklich in diesen hereinkämen, sie so wirken würden, daß sie auch noch während der Zeit unseres physischen Erdendaseins zwischen Geburt und Tod eine solche Vergeistigung in uns hervorrufen würden, wie",
      "ich sie gestern angedeutet habe als ein mögliches Ergebnis der Ver­führung Luzifers. Es würden diese Imagination, Inspiration, Intuition so auf uns wirken, daß wir den Drang bekämen, alles, alles liegen zu lassen, was noch an Anlagen für unser Streben nach fernen Zukünften, zum Menschenideal, in uns vorhanden ist, und wir uns würden ver­geistigen wollen mit all dem, wie wir sind. Wir würden geistige Wesenheiten werden wollen auf dem Vollkommenheitsgrade, den wir bis dahin erlangt haben durch unser Vorleben. Wir würden uns gewissermaßen sagen: Mensch zu werden, das ist uns eine zu große Anstrengung, da müßten wir noch einen schwierigen Weg in die Zukunft gehen. Wir lassen das, was noch an Möglichkeiten zum Menschen hin in uns liegt. Wir werden lieber ein Engel mit all den Unvollkommenheiten, die wir an uns tragen, denn da kommen wir in die geistige Welt unmittelbar hinauf, da vergeistigen wir unser Wesen. Wir werden dann allerdings unvollkommener, als wir nach unseren Anlagen werden könnten im Kosmos, aber wir werden eben geistige, engelartige Wesen.",
      "Da ersehen Sie wiederum an einem Beispiel, wie wichtig das ist, was man nennt: die Schwelle der geistigen Welt, und wie wichtig die Wesenheit ist, die man den Hüter der Schwelle nennt. Denn da steht er schon an dem Punkt, von dem ich eben jetzt gesprochen habe. Er läßt in unser Bewußtsein nur die Empfindung selber herein und läßt nicht dasjenige hereinkommen, was als Imagination, als Inspiration, als Intuition, wenn es in unser Bewußtsein eintreten wurde, einen unmittelbaren Drang nach Vergeistigung, so wie wir sind, mit Ver­zicht auf alles folgende Menschheitsleben in uns erzeugen würde. Das muß uns verhüllt werden, davor wird die Türe unseres Bewußtseins zugeschlossen, aber in unsere Wesenheit dringt es ein. Und indem es in unsere Wesenheit eindringt, ohne daß wir es mit dem Lichte unseres Bewußtseins durchleuchten können, indem wir es hinuntersteigen lassen müssen in die finsteren Untergründe unseres Unterbewußtseins, kommen die geistigen Wesenheiten, deren Gegner Luzifer ist, von der anderen Seite in unser Wesen herein, und es entsteht jetzt in uns der Kampf zwischen Luzifer, der seine Imagination, Inspiration, Intuition hereinsendet, und denjenigen geistigen Wesenheiten, deren",
      "Gegner Luzifer ist. Diesen Kampf würden wir immer schauen bei jeder Empfindung, bei jeder Wahrnehmung, wenn nicht für das äußere Wahrnehmen die Schwelle der geistigen Welt gesetzt wäre, der gegenüber sich nur der hellseherische Blick nicht verschließt.",
      "Daraus ersehen Sie was sich eigentlich alles abspielt in dem Innern der Menschennatur. Das Ergebnis dieses Kampfes, der sich da abspielt, ist das, was ich als eine Art von Leichnam, von partiellem Leichnam in uns charakterisiert habe.",
      "Dieser Leichnam ist der Ausdruck für das, was in uns ganz materiell werden muß, wie ein mineralischer Einschiuß, damit wir nicht in die Lage kommen, es zu vergeistigen. Würde sich dieser Leichnam durch den Kampf von Luzifer und seinen Gegnern nicht ausbilden, so würden wir statt dieses Leichnams das Ergebnis der Imagination, Inspiration und Intuition in uns haben, und wir würden unmittelbar in die geistige Welt aufsteigen.",
      "Dieser Leichnam bildet das Schwergewicht, durch das uns die guten geistigen Wesenheiten, deren Gegner Luzifer ist, in der physischen Welt zu-nächst erhalten, so erhalten, daß wir darin gleichsam verhüllt haben, was als Drang in uns entstehen müßte nach Vergeistigung, damit wir anstreben nach dieser Verhüllung das wirkliche Ideal der mensch­lichen Natur, all die Entfaltung der Anlagen, die in uns sein können. Dadurch daß also dieser Einschiuß, gleichsam dieses Leichnam-Phan­tom sich in uns bildet, daß wir, indem wir wahrnehmen, uns immer sozusagen durchdringen mit etwas, was zu gleicher Zeit Leichnam ist, dadurch ertöten wir in uns während des Wahrnehmens dieses immer aufsteigende Drängen nach Vergeistigung.",
      "Und während sich dieser Einschluß bildet, entsteht das, was ich öfter angedeutet habe und was wichtig ist, daß man es einsieht in seiner ganzen Bedeutung.",
      "Sehen Sie, wenn Sie in einen Spiegel hineinschauen, so haben Sie eine Glasscheibe vor sich, aber durch diese Scheibe würden Sie hindurchschauen, wenn sie nicht mit einem Spiegelbelage belegt wäre. Dadurch, daß die Glasscheibe einen Spiegelbelag hat, spiegelt sich, was vor dem Spiegel ist. Wenn Sie vor Ihrem physischen Körper so stehen würden, daß Sie erleben würden, wie außer den Wahrnehmun­gen auch die Imaginationen, Inspirationen, Intuitionen hineingehen, dann würden Sie durch den physischen Leib hindurchschauen, und",
      "Sie würden ein solches Gefühi erleben, daß Sie sich etwa sagen wür­den: Ich will mit diesem physischen Leibe nichts zu tun haben, ich beachte ihn gar nicht, sondern ich erhebe mich, so wie ich bin, in die geistige Welt. Wirklich, es stünde der physische Leib vor Ihnen wie der Glasspiegel, der keinen Belag hat. Aber nun ist der physische Leib durchdrungen mit diesem Leichnam. Das ist wie der Belag des Spiegels. Und jetzt spiegelt sich alles das, was darauf fällt, aber eben nur so, wie wir es in den Sinneswahrnehmungen haben. Dadurch entstehen die Sinneswahrnehmungen. Unser ständiger Leichnam, den wir in uns tragen, der ist der Spiegelbelag unseres ganzen Leibes, und wir sehen uns dadurch selber in der physischen Welt. Dadurch sind wir als dieses einzelne physische Wesen in der physischen Welt da. So kompliziert schaut sich das menschliche Wesen an.",
      "Nehmen wir den andern Fall, daß wir nicht bloß wahrnehmen, sondern daß wir denken. Wenn wir denken, dann sind es ja nicht Sinneswahrnehmungen. Die Sinneswahrnehmungen können die Ver­anlassung dazu sein, aber das eigentliche Denken verläuft nicht in Sinneswahrnehmungen, sondern verläuft innerlicher. Wenn wir den­ken, machen wir mit dem wirklichen Denken keine Eindrücke auf unseren physischen Leib, wohi aber auf unseren Ätherleib. Aber indem wir denken, kommt wiederum nicht alles das, was in den Gedanken liegt, in uns herein. Würde alles das, was in den Gedanken liegt, in uns hereinkommen, dann würden wir jedesmal, wenn wir denken, zunächst lauter lebende Elementarwesen in uns pulsieren fühlen, wir würden uns ganz innerlich belebt fühien. In München habe ich einnal gesagt: Wenn jemand die Gedanken erlebte, wie sie sind, so würde er sich in den Gedanken in einem solchen Gewirre fühlen wie in einem Ameisenhaufen: alles würde Leben sein. Dieses Leben nehmen wir nicht wahr in dem menschlichen Denken, weil wiederum nur gleich­sam der Schaum davon uns zum Bewußtsein kommt und eben die Schattenbilder der Gedanken bildet, die da als unser Denken in uns auftauchen. Dagegen senkt sich in unseren Ätherleib ein dasjenige, was als lebendige Kräfte die Gedanken durchzieht. Wir nehmen die lebendigen Elementarwesen, die uns da durchschwirren, nicht wahr, sondern wir nehmen in den Gedanken gleichsam nur einen Extrakt",
      "wahr, etwas wie eine Abschattierung. Das andere aber, das Leben, zieht in uns ein, und indem es in uns einzieht, durchdringt es uns wiederum so, daß neuerdings in unserem Ätherleib ein Kampf entsteht, jetzt ein Kampf zwischen den fortschrittlichen Geistern und Ahriman, den ahrimanischen Wesenheiten. Und der Ausdruck dieses Kampfes ist, daß sich in uns die Gedanken nicht so abspielen, wie sie sich abspielen würden, wenn sie lebendige Wesen wären. Würden sie sich so ab­spielen, wie sie wirklich sind, so würden wir uns in dem Leben der Gedankenwesen fühlen: die würden sich hin und her bewegen - aber das nehmen wir nicht wahr. Dafür wird unser ätherischer Leib, der sonst ganz durchsichtig wäre, gleichsam undurchsichtig gemacht; ich möchte sagen, er wird so, wie etwa Rauchtopas ist, der durchzogen wird von dunklen Schichten, während der Quarz ganz durchsichtig und rein ist. So wird unser ätherischer Leib von geistiger Dunkelheit durchzogen. Das, was da unseren ätherischen Leib durchzieht, das ist unser Gedächtnisschatz.",
      "Der Gedächtnisschatz entsteht dadurch, daß wiederum in unserem ätherischen Leib, durch die erwähnten Vorgänge, sich die Gedanken gleichsam spiegeln, aber jetzt in der Zeit sich spiegeln, bis zu dem Punkte hin, bis zu dem wir uns eben erinnern im physischen Leben. Das sind die gespiegelten Gedanken, die wir im Gedächtnis haben, die aus der Zeit heraus gespiegelten Gedanken. Aber da tief unten in unserem Ätherleib, hinter dem Gedächtnis, da arbeiten die guten göttlich-geistigen Wesenheiten, deren Gegner Ahriman ist, und da schaffen sie, zimmern sie diejenigen Kräfte, die wiederum das beleben können, was im physischen Leib durch die vorher geschilderten Vorgänge abgestorben ist. Während also in unserem physischen Leib ein Leichnam geschaffen wird, der geschaffen werden muß, weil wir sonst den Drang hätten, uns zu vergeistigen mit all den Mängeln, die wir an uns tragen, geht etwas wie eine anfachende Lebenskraft vom Ätherleib aus. So daß wirklich nun in der Zukunft wiederum lebendig umgeschaffen werden kann, was da abgetötet worden ist.",
      "Aber jetzt sehen wir erst ein, welche Bedeutung das Vorher und das Nachher hat. Würden wir nämlich in unserer unmittelbaren Gegen­wart die Imaginationen, Inspirationen und Intuitionen, die in uns eindringen,",
      "ausleben, so würden wir uns vergeistigen. Dadurch aber, daß sie in die Zukunft geworfen werden von Ahriman, daß sie jetzt nicht zur Geltung kommen, sondern aufbewahrt werden als Keime für die Zukunft, dadurch gewinnen sie wieder ihre richtige Wesenheit. Was wir gegenwärtig mißbrauchen würden, werden wir in der Zukunft dazu verwenden, wenn wir durch die Pforte des Todes gegangen sind, um uns aus der geistigen Welt heraus ein neues Leben zu zimmern. Was uns, wenn wir es in der physischen Welt verwenden würden, an-leiten würde, uns zu vergeistigen mit unseren Mängeln, leitet uns nach dem Tode als Kräfte an, uns wiederum in das physische Erdenleben zu begeben. So entgegengesetzt wirken die Dinge in den ver­schiedenen Welten.",
      "So ist es mit unserem Denken. Und nun betrachten wir unser Fühlen. Ja, was wir so als inneres Gefühi, als innere Empfindung in uns tragen, das ist wiederum nicht so, wie es eigentlich nach seinem ganzen inneren Wesen sein könnte.",
      "Was wir da als Gefühi in uns tragen, was uns zum Bewußtsein kommt als unser Gefühl, das ist eigentlich wiederum nur ein Schattenbild von dem, was wirklich in uns lebt, denn auch in unserem Gefühi lebt geistige Wesenheit. Wenn Sie sich erinnern an das, was ich im ersten Vortrag gesagt habe, so werden Sie empfinden, daß darin die geistigen Wesenheiten leben, die eigentlich dem ganzen Planetensystem zugrunde liegen, nur kommen sie uns nicht zum Bewußtsein.",
      "Das Gefühi, so wie wir es eben kennen, kommt uns zum Bewußtsein, das andere bleibt außerhalb unseres Bewußtseins. Was heißt das eigentlich: das andere bleibt außerhalb unseres Bewußtseins? Es ist wirklich sehr schwierig, aus der gewöhn­lichen Sprache die Worte zu finden, die diese Dinge genau charakteri­sieren.",
      "Wie man sagen muß: Wahrnehmen und Denken erzeugen in uns etwas, was eigentlich wie ein Ertöten ist - beim Denken allerdings durch die Gegenwirkung zugleich eine Art Anfeuerung zu einem künftig Lebendigen -, so müssen wir sagen: Jedes Gefülil, das in uns sitzt, jedes Gefühl, das in uns auftritt, wird eigentlich nicht ganz ge­boren in uns, kommt nicht ganz zum Dasein. Würde alles, was in uns sitzt indem wir fühlen, herauskommen, so würde uns das, was da im Gefühle lebt, ganz anders ergreifen, ganz anders durchkraften.",
      "was hinter dem Gefühle sitzt, was das Gefühl zu einem Lebewesen macht, zu einem Lebewesen, dessen Leben gespeist wird aus dem ganzen Planetensystem, das kommt nicht unnittelbar heraus. Das Gefühl kommt wiederum nur wie ein Schatten dessen, was es eigent­lich ist, aus uns heraus. Das bewirkt, daß wenn man einmal so recht in seine Gefühiswelt mit einer tieferen Menschheitsempfindung Ein­gang findet, man eigentlich jedem Gefühle gegenüber etwas Unbe­friedigendes empfindet. Jedem Gefühle gegenüber empfindet man, es könnte gesteigert werden, es könnte stärker hervortreten. Namentlich muß man dem Gefühle gegenüber etwas wie ein geheimes Erlebnis haben: es könnte uns viel mehr verraten, als in ihm liegt, es verbirgt etwas, was in unserem Innern lebt, was in den Tiefen der Seele ist, und was nur halb geboren heraufkommt.",
      "Wenn wir auf unseren Willen eingehen, auf alles das, was in uns Wunsch und Wille sein kann, so ist es hier, nur in einem höheren Maße, ebenso wie es beim Gefühle ist. Nur daß hinter dem Willen die geistige Wesenheit, die Grundwesenheit steht, die eigentlich in der Sonne lebt. Nicht bloß das, was in den Planeten lebt, sondern das, was in der ganzen Sonne lebt, lebt da im Willen auch mit darin. Aber es verbirgt sich. Der Wille wird noch weniger ganz geboren als das Gefühl. Der Wille würde uns ganz, ganz anders durchdringen, wenn alles, was in ihm liegt, wirklich in unserem Bewußtsein zum Vorschein käme. Es kommt wirklich nur die alleräußerste Oberfläche des Willens, es kommen nur die alleroberflächlichsten Schaumgebilde des Willens zum Ausdruck. Das andere bleibt uns verborgen. Und warum bleibt uns im Gefühl und im Willen im Grunde genommen eine ganze Welt verborgen? Weil das, was uns verborgen bleibt, wenn es angeschaut würde vom physischen Plane aus, von uns nicht ertragen werden könnte. Vom physischen Plane aus nähme es sich so aus, daß wir es abwehren wollten, daß wir uns abwenden wollten davon.",
      "Das, was da im Gefühl und im Willen lebt und ungeboren ist, das ist werdendes Karma. Sagen wir, wir fühlen eine feindliche Empfin­dung gegen irgend jemand, um ein konkretes Beispiel zu wählen. Ja, was da in dieser feindlichen Empfindung zu unserem Bewußtsein kommt, das ist eben nur das äußerliche Wellenspiel. Da drinnen liegen",
      "Kräfte, die über das ganze Planetensystem ausgebreitet sind. Aber das, was uns verborgen bleibt, das ist gerade das, was uns sagt: Durch deine feindliche Empfindung pflanzest du in dich etwas UnvoW kommenes, das mußt du ausgleichen. - In dem Augenblicke, wo herauf-tauchen würde, was da unten mitlebt, würde vor uns die Imagination desjenigen auftauchen, was im Karma die feindliche Empfindung aus­gleichen muß. Und wir würden uns mit Luzifer und Ahriman ver­binden, um abzuwehren diesen Ausgleich, weil wir von dem Stand­punkt des physischen Planes aus urteilen würden. Aber es wird uns auf diesem physischen Plane das verborgen: der Hüter der Schwelle verbirgt es uns, aus dem einfachen Grunde, weil wir diese Dinge, die nicht geboren werden an unserem Qefühl, an unserem Willen, nur beurteilen können, wenn wir in der geistigen Welt zwischen dem Tod und einer neuen Geburt leben. Da wollen wir das, was wir sonst nie wollen würden, da wollen wir, daß das, was einer feindseligen Stimmung entspricht, wirklich ausgeglichen werde, weil wir da das rechte Interesse haben an dem Inhalt der Götter-Religion, an dem vollkommenen Menschheitsideal, das aus uns den vollkommenen Menschen machen will. Von dem wissen wir, daß durch einen ent­gegengesetzten Ausgleich das wettgemacht werden muß, was durch eine feindselige Empfindung verursacht worden ist. Es muß für die Zukunft nach dem Tode aufbewahrt bleiben, und dann erst darf herauskommen, was ungeboren ist an unserem Gefühle und unserem Willen.",
      "Nun, sehen Sie, ich habe Ihnen, ich möchte sagen, ein Vierfaches von dem menschlichen Seelenkern dargelegt. Das, was von unserem Gefühl ungeboren verbleibt, lebt im Astralleib; das, was vom Willen ungeboren bleibt, lebt im Ich. Wir haben also, indem wir die äußere Welt wahrnehmen, etwas wie einen physischen Phantomleichnam in uns, der eigentlich der Spiegelbelag ist für unseren physischen Leib. Wir haben in uns einen Einschluß, gleichsam eine Durchdunkelung des Ätherleibes. Wir haben in uns etwas im Astralleib, was nicht zur Geburt kommt in der Zeit zwischen der Geburt und dem Tode, und wir haben von unserem Willen etwas, was nicht in dieser Zeit zur Geburt kommt. - Dieses Vierfache, was der Mensch in sich trägt, das",
      "muß aufbewahrt werden für die Zeit zwischen dem Tod und einer neuen Geburt. Aber es lebt in uns als unser Seelenkern mit derselben Gewißheit, wie in der Pflanze der Keim für das nächste Jahr liegt. Sie sehen also, wir können nicht nur im allgemeinen von einem Seelen-kern sprechen, sondern wir können diesen Seelenkern sogar in seiner Viergliedrigkeit erfassen.",
      "Wenn wir, sagen wir, eine Empfindung in uns tragen, die uns Unbehagen namentlich von innen heraus verschafft, wenn wir mit unserem Leben nicht so recht einverstanden sind, so geschieht es dadurch, daß ein Druck von dem ungeborenen Teil der Empfindungen auf den bewußten Teil der Empfindungen ausgeübt wird. Wie kann dieser Druck abgehalten werden?",
      "Ja, sehen Sie, dieser Druck ist etwas, unter dessen Gefahr im Grunde genommen der Mensch fortwährend steht. Denn das, was ich Ihnen jetzt geschildert habe, das ist, insofern es sich auf Gefühl und Wille bezieht, also auf das, was eigentlich unser inneres Seelenleben im Sinne des ersten Vortrages so recht darstellt, dasjenige, was uns in innere Disharmonie bringt.",
      "Wir würden, wenn richtiger Einklang herrschte zwischen dem geborenen Teil von Gefühl und Wille und dem, was hinter der Schwelle des Bewußtseins bleibt, wenn richtiges Verhältnis, richtige Harmonie bestünde, als in der Sinneswelt befriedigte und tüchtige Menschen durch diese Sinneswelt gehen. Hier liegt eigentlich der Grund zu allen inneren Unzufriedenheiten.",
      "Wenn jemand innere Un­zufriedenheiten hat, so kommt es von dem Druck des unterbewußten Teiles des Fühlens und Wollens.",
      "Nun muß ich zu dem Auseinandergesetzten hinzufügen, daß sich in bezug auf alle diese Verhältnisse, die ich jetzt geschildert habe, allerdings die Wesenheit des Menschen im Laufe ihrer Entwickelung geändert hat. Genau so, wie ich die Dinge jetzt geschildert habe, ver­halten sie sich eigentlich in unserer Zeit. Sie verhielten sich nicht immer so. In älteren Zeiten der Menschheitsentwickelung, sagen wir während der urpersischen, ägyptischen, der altindischen Epoche, war das anders. Da flossen ja natürlich in genau derselben Weise die Wahr­nehmungen herein, und in ihnen waren enthalten die Imaginationen, Inspirationen, Intuitionen, aber es blieben für ältere Zeiten diese Imaginationen, Inspirationen, Intuitionen nicht so ganz wirkungslos",
      "auf den Menschen wie heute. Sie töteten nicht so völlig das innere Physische des Menschen, sie lieferten keinen so dichten mineralischen Einschlag, und das kam davon her, daß in diesen älteren Zeiten von der anderen Seite her, aus Gefühl und Wille etwas aufschoß, wenn die Wahrnehmungen von außen kamen unter gewissen Verhältnissen.",
      "Wenn wir zum Beispiel zurückgehen in die älteren Zeiten der ägypti­schen, der babylonischen Kultur und dort die Menschen betrachten, so nahmen eben diese Menschen ganz anders wahr. Sie standen aller­dings wie wir der äußeren Sinneswelt gegenüber, aber ihr Leib war noch so organlsiert, daß die in den Sinneswahrnehmungen verborge­nen Imaginationen nicht völlig ertötend wirkten, sondern daß sie mit einer gewissen Lebendigkeit an die Menschen herandrangen.",
      "Dadurch aber, daß sie lebendig hereindrangen, riefen sie innerlich im Menschen das Gegenbild heraus dessen, was nun für uns ganz ver­borgen bleibt im Ich und im astralischen Leib. Die geistigen Wesen­heiten des Sonnenhaften und des Planetensystems drängten sich von innen heraus entgegen und spiegelten gewissermaßen das, was sich belebte durch die Imagination.",
      "So daß es für den Angehörigen der älteren ägyptischen, der babylonischen Kultur gewisse Zeiten des Wahrnehmens gab, wo er, wenn er den Blick hinausrichtete in die physische Welt, nicht nur so die physischen Wahrnehmungen auf­nahm, wie wir sie haben, sondern wo sie sich belebten. Er wußte, dahinter steckt etwas, was in Imaginationen sich auslebt.",
      "Daher war er auch noch nicht so töricht, nach dem Muster unserer gegenwärtigen Physiker hinter den Wahrnehmungen materielle Atomschwingungen zu vermuten, sondern er wußte, daß da Leben dahinter ist, und aus seinem Innern tauchten auf entgegenstrahlend die Bilder des belebten Sternenhimmels, sogar die Sonne. Besonders stark war das während der persischen Kultur, wo wirklich beim äußeren Wahrnehmen etwas wie die innere geistige Sonnenkraft aufleuchtete - Ahura Mazdao I",
      "Wenn wir in noch ältere Zeiten zurückgehen, so finden wir dieses Zusammenwirken, dieses Entgegenkommen des Inneren und des Äußeren noch viel stärker ausgeprägt. Heute kann das nicht mehr sein, aber ein Ersatz kann da sein, und hier kommen wir an einen Punkt, wo wir, ich möchte sagen, aus der Sache selbst heraus unsere",
      "Aufgabe innerhalb der anthroposophischen Weltanschauung wirklich verstehen werden. Ein Ersatz muß geschaffen werden. Wir stehen der Außenwelt mit unseren Wahrnehmungen gegenüber. Wir denken über sie, indem uns ein Teil dieser Außenwelt verschlossen bleibt, der ertötend und durchdunkelnd auf uns wirkt. Aber wir können das, was da ertötet und durchdunkelt wird, durch die Geisteswissenschaft beleben. Und gerade durch die Belebung dessen, was sonst ertötet und durchdunkelt wird, entsteht solche Wissenschaft, wie sie dargestellt worden ist in der Entwickelung durch Saturn-, Sonnen- und Monden-entwickelung in meiner «Geheimwissenschaft». Dieses Wissen von der Saturn-, Sonnen- und Mondenentwickelung hat jeder Mensch, nur ist es in den Untergründen seines Bewußtseins. Er möchte nicht Erdenmensch sein, wenn er es so ohne weiteres schauen würde, ohne die genügende Vorbereitung. Er möchte, daß die Erde ihn gar nichts anginge und er mit der Mondenentwickelung abschliessen könnte. Alles das, was wir an Erkenntnissen erwerben können durch die Geistes­wissenschaft, erhellt uns das, was uns von der Entwickelung der Ver­gangenheit verborgen bleibt, indem es in uns eindringt. Denn was da an Imaginationen, Inspirationen und Intuitionen draußen lebt in den Sinnesempfindungen und nicht hereinkommt, das ist eigentlich, wenn man es durch den Schleier der Sinnesempfindungen anschaut, dasjenige, was wir an Vergangenheit durchgemacht haben.",
      "Etwas anderes ist es mit dem, was in unserem Fühlen und Wollen lebt. Der Mensch kann sagen - und viele Menschen der Gegenwart haben ja einen Drang, das zu tun -: Oh, was geht mich das alles an, was da diese vertrakten Köpfe aussinnen oder ausgesonnen haben über eine übersinnliche Welt. Ich nehme solche Vorstellungen nicht in mich auf - Wer das sagt, hat sich niemals einen Begriff davon er­worben, warum eigentlich in die Weltentwickelung Religionen ge­kommen sind. Das ist ja das Gemeinsame aller religiösen Vorstellun­gen, daß sie sich auf Dinge beziehen, die der Mensch nicht sinnlich wahrnehmen kann, daß der Mensch in religiösen Vorstellungen mit etwas sich erfüllen muß, was er nicht sinnlich wahrnehmen kann. Vorstellungen, die von dem kommen, was man sinnlich wahrnehmen kann, die können uns niemals für unser Fühlen und Wollen einen",
      "Impuls geben, der nach dem Tode Stoßkraft ist. Damit das wirken kann, was ungeboren in uns ist in unserem Gefühl, in unserem Willen, weil es ja wirken soll nach unserem Tode, brauchen wir dazu die Vor­stellungen nicht, die wir uns durch unsere Sinnesempfindungen an-eignen können oder durch den Verstand, der an das Gehirn gebunden ist; die helfen uns nichts. Einzig und allein diejenigen Vorstellungen, die dem entsprechen, was nicht äußerlich wirklich ist, die, wenn wir sie aufnehmen, uns fromm machen, durch die wir aufsehen in eine geistige Welt, die geben uns den Impuls, die Schwungkraft, die wir nach dem Tode brauchen. Religiös vorstellen heißt: das vorstellen, was jetzt noch nicht in uns wirken kann, was aber Wirkungskraft ist nach dem Tode. Mit den religiösen Vorstellungen nehmen wir nicht nur Erkenntnisvorsteliungen auf, sondern etwas, was wirksam werden kann nach unserem Tode, und was gerade deshalb jetzt so sein muß im physischen Leib, daß derjenige, der auf solche Wirkungskräfte nicht reflektieren will, darüber lachen kann und es abweisen kann in seinem Materialismus. Er hat aber nur eine gelähmte Kraft, um vor­wärts zu bringen, was ungeboren ist in seinem Fühlen und Wollen, wenn er sich nicht durchdringt mit den Vorstellungen über das Über-sinnliche.",
      "Daher muß es so oft betont werden: Was vergangen ist, wird er­leuchtet von dem hellsichtigen Bewußtsein. Es wird gegenwärtig wieder erkannt, auch insofern es hinter dem Schleier der Sinneswelt als Imagination, Inspiration und Intuition vorhanden ist und hinein-wirkt in die Sinneswelt. Früher wurde es den Menschen gegeben als religiöser Glaube, damit die Menschen nicht alle Schwungkraft für die Zeit nach dem Tode verlieren, damit sie etwas im Seelenkern haben, was ihn lebendig erhalten kann, auch wenn er den physischen Leib abgelegt hat. Jetzt ist die Zeit gekommen, wo die Menschen aus dem Verständnis heraus, aus dem Verständnis der Geisteswissenschäft heraus, sich Vorstellungen aneignen sollen über die übersinnlichen Welten. Deshalb kann es nicht oft genug betont werden: Erforschen kann man nur als Geistesforscher diese Dinge in der übersinnlichen Welt. Sind sie aber erforscht und werden sie mitgeteilt, so gibt es etwas in unserer tiefsten Seele, was eine geheime Sprache dieser Seele",
      "ist, und was verstehen, begreifen kann dasjenige, was von dem Geistesforscher erforscht wird. Nur wenn die Vorurteile des Verstan­des und der Sinne kommen, dann wird als Unsinn angesehen, als Torheit und als Phantasterei, was von der Geistesforschung als über­sinnliche Vorstellungen gegeben wird, und was, wenn es aufgenom­men wird, uns Schwungkraft gibt für den Seelenkern, damit er in alle Zukünfte seine Wege finden kann im Kosmos. Erforschen werden immer nur diejenigen den Inhalt der geistigen Welt, die eine esoteri­sche Entwickelung durchmachen. Diesen Inhalt wissen, ihn innerlich im Bewußtsein durcharbeiten, ihn in Ideen und Begriffen haben, ihn als eine Gewißheit des Seins der Seele in der geistigen Welt besitzen, das ist etwas, was immer mehr und mehr als eine notwendige geistige Nal:rung die Menschen brauchen werden.",
      "Das ist es, was uns zeigt, wie man aus der Sache heraus die Mission unserer anthroposophischen Bewegung verstehen kann. In alten Zeiten war es eben noch so, daß die Erkenntnis von oben sich belebte und der Inhalt zu dieser Erkenntnis von unten entgegenkam. Daher hatten die Alten von den geistigen Welten noch ein unmittelbares Bewußtsein, das sich aber immer mehr und mehr abdunkelte und ab­dumpfte. Hätte es sich nicht abgedunkelt und abgedumpft, so wäre der Mensch nicht zum vollen Bewußtsein seines Ich gekommen. Zum vollen Bewußtsein seines Ich kann der Mensch nur dadurch kommen, daß er im höchsten Maße innerhalb seines physischen Leibes jenes Leichnam-Phantom ausbildet, von dem ich gesprochen habe. Es muß sozusagen unser physischer Leib als durchsichtige Wesenheit ganz belegt werden mit Spiegelbelag, und erst, wenn er ganz belegt ist, dann können wir uns ganz so fühlen, daß wir sagen: Ich bin ein Ich. Dieses vollständige Belegen hat sich aber erst langsam und allmählich gebildet. Es hat sich im Laufe der Menschheitsentwickelung gebildet, und es war diese Bildung vollendet in der Zeit, in die das Mysterium von Golgatha fiel. Da war der Spiegelbelag fertig. Vorher, da begeg­neten sich noch immer Unteres und Oberes, da kamen in der Men­schenwesenheit Unteres und Oberes zusammen. Aber, man möchte sagen, ganz herausgedrängt würde Unteres und Oberes dadurch, daß der Spiegelbelag vollkommen war, und der Mensch nur die Spiegelung",
      "aus dem physischen Leibe wahrnahm. Das war erst, als das Ereignis von Golgatha in die Menschheitsentwickelung hereinkam.",
      "Was war denn da eigentlich geschehen? Ja, sehen wir nur ganz genau auf das hin, was da geschehen war! Stellen Sie sich so recht diese alten Menschen vor in den Zeiten vor dem Mysterium von Golgatha, stellen Sie sich dieses Bewußtsein vor! Da kommt von außen herein die Belebung von Imaginationen; von innen steigen auf Bilder der außermenschlichen geistigen Welt. Was sind diese Bilder, die da aufsteigen im Menschen? Wie wir wissen, war das in alten Zeiten bei herabgedämpftem menschlichen Bewußtseinszustand mög­lich. Diejenigen, die diese Dinge erkannten, die in alten Zeiten als Eingeweihte hinzublicken vermochten auf die menschliche Seele, wie in ihr noch lebte dieses Zusammenkommen der belebten Imagination von außen, und von innen das Schauen, die sagten nicht: Der Mensch schaut das allein, sondern diese alten Eingeweihten sagten: Es schaut an seine Welt im Menschen zum Beispiel Jahve oder Jehova, wie dies bei den alten Juden der Fall war. Der Gott denkt im Menschen. Wie wir heute sagen in unserem Entwickelungszyklus, wenn wir Gedanken haben: Ich denke, - so sagten diejenigen, die die Dinge wußten in alten Zeiten, wenn die Schmungen auftauchten aus der geistigen Welt: Die Götter denken in uns. Oder als man die Einheit des Gött­lichen im Monotheismus erkannte: Jahve denkt im Menschen. Der Mensch ist der Schauplatz der göttlichen Gedanken. Erfüllt wußten sich die Menschen, so daß sie sagten: In mir denken die Götter.",
      "Aber in der menschlichen Entwickelung lag die Notwendigkeit, daß dies immer unmöglicher wurde. Man möchte sagen, immer mehr und mehr traten Finsternis den Schauungen, den Gedanken der Götter entgegen in der menschlichen Natur. Das innere Leicbnam-Phantom wurde immer stärker, immer bedeutender. Die Zeit rückte heran, wo aus der menschlichen Natur heraus den Göttern keine Gedanken mehr entgegentauchten. Da fühlte diejenige göttliche Wesenheit, von der man sagen kann, sie dachte durch die menschliche Wesenheit, daß ihr Bewußtsein - denn dieses Bewußtsein besteht ja in ihren Gedanken -immer dumpfer, immer dämmeriger wurde. Und die Sehnsucht ent­stand in diesem göttlichen Wesen, eine neue Form des Bewußtseins",
      "zu erwecken. Menschen kommen zu einer anderen Form des Bewußt­seins. Götter, indem sie ein neues Bewußtsein schaffen, schaffen mit diesem etwas Wesentliches; für sie entsteht damit etwas Wesentliches. Und dieses Wesentliche, was da entstand, war für die jetzt gemeinte göttliche Wesenheit, die ihr Bewußtsein herabdämmern fühlte: der Christus. Der Christus ist das Kind der Gottheit, das wieder herstellt das Bewußtsein der Gottheit in der menschlichen Wirksamkeit. So mußte sich eingliedern in die menschliche Wesenheit die Christus­wesenheit.",
      "Und wir müssen das Bewußtsein in uns aufnehmen: Indem wir die Sinneswelt wahrnehmen, strömen wir fortwährend in uns ein - Ster­ben. Und Finsternis und Verdunkelung strömen wir in uns ein, indem wir diese Welt denken. Und Ungeborenes lassen wir, indem wir fühlen und wollen. Das alles sitzt unten in den Untergründen unseres Be­wußtseins, da lassen wir hineinfließen unser Sterben und unser noch Ungeborenes, das wir erst brauchen können, nachdem wir gestorben sein werden. Das aber würde lahm sein, wenn wir es nicht einsenken könnten in die Wesenheit, die sich die Gottheit wie die Wesenheit eines neuen Bewußtseins geboren hat, wenn wir es nicht einffießen lassen könnten in die Christus-Wesenheit.",
      "Dieses Bewußtsein können wir haben, indem wir den Sinn der ganzen Evolution wirklich erkennen durch die Geisteswissenschaft: Ja, wir senden da hinunter in die unterbewußten Gründe das, was in uns erstirbt. Aber aufgenommen wird es, dieses Sterben, das wir in unsere eigene Wesenheit immer mehr und mehr hineinsenken, auf­genommen wird es von dem uns entgegenlebenden Christus. In dem was in uns erstirbt, in uns erdunkelt, ungeboren bleibt, lebt uns der Christus auf. Wir lassen hinuntersterben in uns dasjenige, was sterben muß, damit wir dem wirklichen Menschheitsideal mit all unseren Anlagen uns nähern. Aber das, was wir als Sterben in uns hinein-gießen, gießen wir in die Christus-Wesenheit, so wie sie seit der Be­gründung des Christentums die menschliche Evolution durchzieht, hinein. Und das, was in uns ungeboren bleibt, unser Fühlen und Wollen, wir wissen, daß es aufgenommen wird von der Christus-Substanz, in die es eingesenkt wird nach dem Tode.",
      "Da, in uns, lebt der Christus, seitdem er das Mysterium von Gol­gatha durchlebt hat. In den Christus hinein senken wir das Sterben, das vorhanden ist mit jeder Wahrnehmung. Und wir senken in die Christus-Wesenheit hinein die Abdunkelung im Denken. In das Licht, in das geistige Sonnenlicht des Christus senden wir unsere abgedun­kelten Gedanken hinein. Und wenn wir durch die Pforte des Todes schreiten, dann tauchen ein unsere ungeborenen Gefühle und unser ungeborenes Wollen in die Christus-Substanz. Verstehen wir die Ent­wickelung recht, so sagen wir zu dieser Entwickelung: Wir sterben in den Christus hinein.",
      "In Christo morimur."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Zunächst werden wir heute aufmerksam zu machen haben auf einzelne positive okkulte Forschungsresultate, welche auf der einen Seite seht geeignet sind, uns in das Wesen des Menschen hineinzufühten, die aber auf der anderen Seite uns zeigen, als welch kompliziertes Wesen eigentlich dieser Mensch in der Welt darinnensteht.",
        "Aber können wir denn anders denken, als daß dieser Mensch als ein recht kompliziertes Wesen in der Welt darinnensteht, wenn wir erwägen, daß das eigent­liche Idealbild des Menschen, das, was der Mensch sein kann, wenn er alle in ihm liegenden Anlagen wirklich zur Entfaltung bringt, im Grunde der Inhalt der Götter-Religion ist, und daß im Grunde ge­nommen all die geistigen Wesenheiten der verschiedenen Hierarchien, die man im Zusammenhang mit der menschlichen Natur kennen­lernen kann, ihre Ziele zusammenwirken lassen, um aus dem gesamten Kosmos heraus den Menschen wie den Sinn dieses Kosmos aufzu­bauen!"
      ],
      [
        "Das erste, was zu sagen sein wird, ist, daß der Mensch mit den Wahrnehmungen, die er von der äußeren Welt empfängt, so wie sie ihm in seinem Bewußtsein erscheinen, eigentlich nur einen kleinen Teil dessen wirklich aufnimmt, was da auf ihn einstürmt.",
        "Indem der Mensch in der physischen Welt darinnensteht, seine Sinnesorgane geöffnet hat, mit seinem Verstand, der an sein Gehirn, an sein Nerven-system gebunden ist, die Welt betrachtet und sich zu erklären versucht, was da auf diese Weise an den Menschen herankommt, gelangt eigent­lich nur ein kleiner Teil dessen, was da heranstürmt, wirklich zur menschlichen Vorstellung, tritt nur ein kleiner Teil wirklich in das Bewußtsein des Menschen ein.",
        "Im Licht und in den Farben, im Ton und so weiter ist viel mehr enthalten, als dem Menschen zum Bewußt-sein kommt.",
        "Die äußerliche materialistische Physik spricht in ihrer kindlichen Weltauffassung davon, daß hinter den Farben, hinter dem Licht und so weiter materielle Vorgänge seien, Atomschwingungen und dergleichen.",
        "Das ist eben wirklich nur, man kann schon sagen,"
      ],
      [
        "eine kindliche Weltauffassung.",
        "Denn in Wahrheit stellt sich das Fol­gende ein."
      ],
      [
        "Wir müssen mit dem heliseherischen Blick das menschliche Wahr­nehmen erforschen, denn von diesem Beobachten des wirklichen Wahrnehmungsvorganges kann erst ein Verständnis über das Ver­hältnis des Menschen zu der Umwelt, die ihm vorliegt, ausgehen, wenn wir auch nur auf dem physischen Plane bleiben.",
        "Etwas höchst Eigentümliches zeigt sich, wenn man den Wahrnehmungsvorgang hellseherisch beobachtet."
      ],
      [
        "Sagen wir, irgend etwas wirke auf unser Auge, wir nehmen Licht oder Farbe wahr, wir haben also in unserem Bewußtsein die Empfindung des Lichtes oder der Farbe: das Merk­würdige, was man nun entdeckt durch die Geistesforschung, ist, daß im Menschenwesen nicht nur dieses Licht und diese Farbe auftreten, sondern daß da wie im Gefolge von Licht und Farbe gleichzeitig mit unserer Empfindung von Licht- und Farbenbildem, rlaan möchte sagen, eine Art von Licht- oder Farbenleichnam in uns auftritt.",
        "Unser Auge veranlaßt uns, daß wir die Licht- und Farbenempfindung haben."
      ],
      [
        "Man könnte also sagen: das Licht strömt zu und bereitet uns die Lichtempfindung, aber tiefer in unser Wesen hineinschauend, ent­decken wir, daß während in unserem Bewußtsein das Licht sitzt, unser Menschenwesen durchzogen wird von etwas, was in diesem Menschenwesen sterben maß, damit wir die Lichtempfindung haben können.",
        "Keine Wahrnehmung, keine Empfindung von außen können wir haben, ohne daß sich gleichsam durchdrückt durch diese Empfin­dung eine Art Leichenbildung, die wie im Gefolge dieser Empfindung auftritt."
      ],
      [
        "Geistesforschung muß eben sagen: Da schaue ich mir den Menschen an, ich weiß, jetzt empfindet er rot.",
        "Ich sehe aber, daß dieses Rot, das in seinem Bewußtsein lebt, von sich gleichsam etwas aus­gießt, sein ganzes Wesen, insofern es in seine Haut und in die Grenzen seines Ätherleibes eingeflossen ist, durchdringt mit etwas, was wie der Leichnam der Farbe ist, was etwas ertötet in dem Menschen."
      ],
      [
        "Denken Sie nur einmal, daß wir eigentlich immer, indem wir der physischen Welt gegenüberstehen und unsere Sinnesorgane offen haben, die Leichname aller unserer Wahrnehmungen wie Phantome, aber wirksame Phantome, in uns aufnehmen.",
        "Immer stirbt etwas in"
      ],
      [
        "uns, indem wir die Außenwelt wahrnehmen.",
        "Es ist das ein höchst eigentümliches Phänomen.",
        "Und der Geistesforscher muß sich fragen: Ja, was geschieht denn da?",
        "Was ist denn die Ursache von diesem höchst eigenartigen Phänomen?"
      ],
      [
        "Da muß man betrachten, wie es sich eigentlich mit dem verhält, was da wie Licht an uns heranstürmt.",
        "Dieses Licht hat eben vieles hinter sich.",
        "Es ist gleichsam das, was das Licht offenbart, nur der Vorposten desjenigen, was an uns heranstürmt.",
        "Hinter dem Licht steht allerdings nicht jene Wellenbewegung, von der die äußere Physik phantasiert, sondern hinter dem Licht, hinter allen Wahrnehmungen, hinter allen Eindrücken steht zunächst das, was wir nur erfassen, wenn wir geisteswissenschaftlich die Welt anschauen durch Imagina­tionen, durch schöpferische Bilder.",
        "In dem Augenblick, wo wir alles sehen würden, alles wahrnehmen würden, was in dem Licht oder in dem Tone oder in der Wärme lebt, würden wir hinter dem, was uns zum Bewußtsein kommt, die schöpferische Imagination wahrnehmen und in dieser sich wieder offenbarend die Inspiration, und in dieser die Intuition.",
        "Es ist dasjenige, was uns zum Bewußtsein kommt als Licht-und Tonempfindung, gleichsam die oberste Schicht, gleichsam nur der Schaum dessen, was an uns heranschwingt, aber es lebt darin, was, wenn es uns zum Bewußtsein käme, zur Imagination, Inspiration, Intuition in uns werden könnte."
      ],
      [
        "Also eigentlich haben wir nur ein Viertel von dem, was an uns heranstürmt, wirklich in der Wahrnehmung gegeben, die anderen drei Viertel dringen in uns ein, ohne daß es uns zum Bewußtsein kommt.",
        "Während wir also dastehen und eine Farbenempfindung haben, dringen, gleichsam durch die Fläche der Farbenempfindung, die schöpferische Imagination, die Inspiration, die Intuition in uns ein, versenken sich in uns.",
        "Wenn wir sie näher untersuchen, diese drei letzteren Eindringlinge, so finden wir, daß wenn diese Imagination, Inspiration, Intuition, so, wie sie sich durch die Sinnes-empfindungen in unseren Organismus hereindrängen wollen, wirklich in diesen hereinkämen, sie so wirken würden, daß sie auch noch während der Zeit unseres physischen Erdendaseins zwischen Geburt und Tod eine solche Vergeistigung in uns hervorrufen würden, wie"
      ],
      [
        "ich sie gestern angedeutet habe als ein mögliches Ergebnis der Ver­führung Luzifers.",
        "Es würden diese Imagination, Inspiration, Intuition so auf uns wirken, daß wir den Drang bekämen, alles, alles liegen zu lassen, was noch an Anlagen für unser Streben nach fernen Zukünften, zum Menschenideal, in uns vorhanden ist, und wir uns würden ver­geistigen wollen mit all dem, wie wir sind.",
        "Wir würden geistige Wesenheiten werden wollen auf dem Vollkommenheitsgrade, den wir bis dahin erlangt haben durch unser Vorleben.",
        "Wir würden uns gewissermaßen sagen: Mensch zu werden, das ist uns eine zu große Anstrengung, da müßten wir noch einen schwierigen Weg in die Zukunft gehen.",
        "Wir lassen das, was noch an Möglichkeiten zum Menschen hin in uns liegt.",
        "Wir werden lieber ein Engel mit all den Unvollkommenheiten, die wir an uns tragen, denn da kommen wir in die geistige Welt unmittelbar hinauf, da vergeistigen wir unser Wesen.",
        "Wir werden dann allerdings unvollkommener, als wir nach unseren Anlagen werden könnten im Kosmos, aber wir werden eben geistige, engelartige Wesen."
      ],
      [
        "Da ersehen Sie wiederum an einem Beispiel, wie wichtig das ist, was man nennt: die Schwelle der geistigen Welt, und wie wichtig die Wesenheit ist, die man den Hüter der Schwelle nennt.",
        "Denn da steht er schon an dem Punkt, von dem ich eben jetzt gesprochen habe.",
        "Er läßt in unser Bewußtsein nur die Empfindung selber herein und läßt nicht dasjenige hereinkommen, was als Imagination, als Inspiration, als Intuition, wenn es in unser Bewußtsein eintreten wurde, einen unmittelbaren Drang nach Vergeistigung, so wie wir sind, mit Ver­zicht auf alles folgende Menschheitsleben in uns erzeugen würde.",
        "Das muß uns verhüllt werden, davor wird die Türe unseres Bewußtseins zugeschlossen, aber in unsere Wesenheit dringt es ein.",
        "Und indem es in unsere Wesenheit eindringt, ohne daß wir es mit dem Lichte unseres Bewußtseins durchleuchten können, indem wir es hinuntersteigen lassen müssen in die finsteren Untergründe unseres Unterbewußtseins, kommen die geistigen Wesenheiten, deren Gegner Luzifer ist, von der anderen Seite in unser Wesen herein, und es entsteht jetzt in uns der Kampf zwischen Luzifer, der seine Imagination, Inspiration, Intuition hereinsendet, und denjenigen geistigen Wesenheiten, deren"
      ],
      [
        "Gegner Luzifer ist.",
        "Diesen Kampf würden wir immer schauen bei jeder Empfindung, bei jeder Wahrnehmung, wenn nicht für das äußere Wahrnehmen die Schwelle der geistigen Welt gesetzt wäre, der gegenüber sich nur der hellseherische Blick nicht verschließt."
      ],
      [
        "Daraus ersehen Sie was sich eigentlich alles abspielt in dem Innern der Menschennatur.",
        "Das Ergebnis dieses Kampfes, der sich da abspielt, ist das, was ich als eine Art von Leichnam, von partiellem Leichnam in uns charakterisiert habe."
      ],
      [
        "Dieser Leichnam ist der Ausdruck für das, was in uns ganz materiell werden muß, wie ein mineralischer Einschiuß, damit wir nicht in die Lage kommen, es zu vergeistigen.",
        "Würde sich dieser Leichnam durch den Kampf von Luzifer und seinen Gegnern nicht ausbilden, so würden wir statt dieses Leichnams das Ergebnis der Imagination, Inspiration und Intuition in uns haben, und wir würden unmittelbar in die geistige Welt aufsteigen."
      ],
      [
        "Dieser Leichnam bildet das Schwergewicht, durch das uns die guten geistigen Wesenheiten, deren Gegner Luzifer ist, in der physischen Welt zu-nächst erhalten, so erhalten, daß wir darin gleichsam verhüllt haben, was als Drang in uns entstehen müßte nach Vergeistigung, damit wir anstreben nach dieser Verhüllung das wirkliche Ideal der mensch­lichen Natur, all die Entfaltung der Anlagen, die in uns sein können.",
        "Dadurch daß also dieser Einschiuß, gleichsam dieses Leichnam-Phan­tom sich in uns bildet, daß wir, indem wir wahrnehmen, uns immer sozusagen durchdringen mit etwas, was zu gleicher Zeit Leichnam ist, dadurch ertöten wir in uns während des Wahrnehmens dieses immer aufsteigende Drängen nach Vergeistigung."
      ],
      [
        "Und während sich dieser Einschluß bildet, entsteht das, was ich öfter angedeutet habe und was wichtig ist, daß man es einsieht in seiner ganzen Bedeutung."
      ],
      [
        "Sehen Sie, wenn Sie in einen Spiegel hineinschauen, so haben Sie eine Glasscheibe vor sich, aber durch diese Scheibe würden Sie hindurchschauen, wenn sie nicht mit einem Spiegelbelage belegt wäre.",
        "Dadurch, daß die Glasscheibe einen Spiegelbelag hat, spiegelt sich, was vor dem Spiegel ist.",
        "Wenn Sie vor Ihrem physischen Körper so stehen würden, daß Sie erleben würden, wie außer den Wahrnehmun­gen auch die Imaginationen, Inspirationen, Intuitionen hineingehen, dann würden Sie durch den physischen Leib hindurchschauen, und"
      ],
      [
        "Sie würden ein solches Gefühi erleben, daß Sie sich etwa sagen wür­den: Ich will mit diesem physischen Leibe nichts zu tun haben, ich beachte ihn gar nicht, sondern ich erhebe mich, so wie ich bin, in die geistige Welt.",
        "Wirklich, es stünde der physische Leib vor Ihnen wie der Glasspiegel, der keinen Belag hat.",
        "Aber nun ist der physische Leib durchdrungen mit diesem Leichnam.",
        "Das ist wie der Belag des Spiegels.",
        "Und jetzt spiegelt sich alles das, was darauf fällt, aber eben nur so, wie wir es in den Sinneswahrnehmungen haben.",
        "Dadurch entstehen die Sinneswahrnehmungen.",
        "Unser ständiger Leichnam, den wir in uns tragen, der ist der Spiegelbelag unseres ganzen Leibes, und wir sehen uns dadurch selber in der physischen Welt.",
        "Dadurch sind wir als dieses einzelne physische Wesen in der physischen Welt da.",
        "So kompliziert schaut sich das menschliche Wesen an."
      ],
      [
        "Nehmen wir den andern Fall, daß wir nicht bloß wahrnehmen, sondern daß wir denken.",
        "Wenn wir denken, dann sind es ja nicht Sinneswahrnehmungen.",
        "Die Sinneswahrnehmungen können die Ver­anlassung dazu sein, aber das eigentliche Denken verläuft nicht in Sinneswahrnehmungen, sondern verläuft innerlicher.",
        "Wenn wir den­ken, machen wir mit dem wirklichen Denken keine Eindrücke auf unseren physischen Leib, wohi aber auf unseren Ätherleib.",
        "Aber indem wir denken, kommt wiederum nicht alles das, was in den Gedanken liegt, in uns herein.",
        "Würde alles das, was in den Gedanken liegt, in uns hereinkommen, dann würden wir jedesmal, wenn wir denken, zunächst lauter lebende Elementarwesen in uns pulsieren fühlen, wir würden uns ganz innerlich belebt fühien.",
        "In München habe ich einnal gesagt: Wenn jemand die Gedanken erlebte, wie sie sind, so würde er sich in den Gedanken in einem solchen Gewirre fühlen wie in einem Ameisenhaufen: alles würde Leben sein.",
        "Dieses Leben nehmen wir nicht wahr in dem menschlichen Denken, weil wiederum nur gleich­sam der Schaum davon uns zum Bewußtsein kommt und eben die Schattenbilder der Gedanken bildet, die da als unser Denken in uns auftauchen.",
        "Dagegen senkt sich in unseren Ätherleib ein dasjenige, was als lebendige Kräfte die Gedanken durchzieht.",
        "Wir nehmen die lebendigen Elementarwesen, die uns da durchschwirren, nicht wahr, sondern wir nehmen in den Gedanken gleichsam nur einen Extrakt"
      ],
      [
        "wahr, etwas wie eine Abschattierung.",
        "Das andere aber, das Leben, zieht in uns ein, und indem es in uns einzieht, durchdringt es uns wiederum so, daß neuerdings in unserem Ätherleib ein Kampf entsteht, jetzt ein Kampf zwischen den fortschrittlichen Geistern und Ahriman, den ahrimanischen Wesenheiten.",
        "Und der Ausdruck dieses Kampfes ist, daß sich in uns die Gedanken nicht so abspielen, wie sie sich abspielen würden, wenn sie lebendige Wesen wären.",
        "Würden sie sich so ab­spielen, wie sie wirklich sind, so würden wir uns in dem Leben der Gedankenwesen fühlen: die würden sich hin und her bewegen - aber das nehmen wir nicht wahr.",
        "Dafür wird unser ätherischer Leib, der sonst ganz durchsichtig wäre, gleichsam undurchsichtig gemacht; ich möchte sagen, er wird so, wie etwa Rauchtopas ist, der durchzogen wird von dunklen Schichten, während der Quarz ganz durchsichtig und rein ist.",
        "So wird unser ätherischer Leib von geistiger Dunkelheit durchzogen.",
        "Das, was da unseren ätherischen Leib durchzieht, das ist unser Gedächtnisschatz."
      ],
      [
        "Der Gedächtnisschatz entsteht dadurch, daß wiederum in unserem ätherischen Leib, durch die erwähnten Vorgänge, sich die Gedanken gleichsam spiegeln, aber jetzt in der Zeit sich spiegeln, bis zu dem Punkte hin, bis zu dem wir uns eben erinnern im physischen Leben.",
        "Das sind die gespiegelten Gedanken, die wir im Gedächtnis haben, die aus der Zeit heraus gespiegelten Gedanken.",
        "Aber da tief unten in unserem Ätherleib, hinter dem Gedächtnis, da arbeiten die guten göttlich-geistigen Wesenheiten, deren Gegner Ahriman ist, und da schaffen sie, zimmern sie diejenigen Kräfte, die wiederum das beleben können, was im physischen Leib durch die vorher geschilderten Vorgänge abgestorben ist.",
        "Während also in unserem physischen Leib ein Leichnam geschaffen wird, der geschaffen werden muß, weil wir sonst den Drang hätten, uns zu vergeistigen mit all den Mängeln, die wir an uns tragen, geht etwas wie eine anfachende Lebenskraft vom Ätherleib aus.",
        "So daß wirklich nun in der Zukunft wiederum lebendig umgeschaffen werden kann, was da abgetötet worden ist."
      ],
      [
        "Aber jetzt sehen wir erst ein, welche Bedeutung das Vorher und das Nachher hat.",
        "Würden wir nämlich in unserer unmittelbaren Gegen­wart die Imaginationen, Inspirationen und Intuitionen, die in uns eindringen,"
      ],
      [
        "ausleben, so würden wir uns vergeistigen.",
        "Dadurch aber, daß sie in die Zukunft geworfen werden von Ahriman, daß sie jetzt nicht zur Geltung kommen, sondern aufbewahrt werden als Keime für die Zukunft, dadurch gewinnen sie wieder ihre richtige Wesenheit.",
        "Was wir gegenwärtig mißbrauchen würden, werden wir in der Zukunft dazu verwenden, wenn wir durch die Pforte des Todes gegangen sind, um uns aus der geistigen Welt heraus ein neues Leben zu zimmern.",
        "Was uns, wenn wir es in der physischen Welt verwenden würden, an-leiten würde, uns zu vergeistigen mit unseren Mängeln, leitet uns nach dem Tode als Kräfte an, uns wiederum in das physische Erdenleben zu begeben.",
        "So entgegengesetzt wirken die Dinge in den ver­schiedenen Welten."
      ],
      [
        "So ist es mit unserem Denken.",
        "Und nun betrachten wir unser Fühlen.",
        "Ja, was wir so als inneres Gefühi, als innere Empfindung in uns tragen, das ist wiederum nicht so, wie es eigentlich nach seinem ganzen inneren Wesen sein könnte."
      ],
      [
        "Was wir da als Gefühi in uns tragen, was uns zum Bewußtsein kommt als unser Gefühl, das ist eigentlich wiederum nur ein Schattenbild von dem, was wirklich in uns lebt, denn auch in unserem Gefühi lebt geistige Wesenheit.",
        "Wenn Sie sich erinnern an das, was ich im ersten Vortrag gesagt habe, so werden Sie empfinden, daß darin die geistigen Wesenheiten leben, die eigentlich dem ganzen Planetensystem zugrunde liegen, nur kommen sie uns nicht zum Bewußtsein."
      ],
      [
        "Das Gefühi, so wie wir es eben kennen, kommt uns zum Bewußtsein, das andere bleibt außerhalb unseres Bewußtseins.",
        "Was heißt das eigentlich: das andere bleibt außerhalb unseres Bewußtseins?",
        "Es ist wirklich sehr schwierig, aus der gewöhn­lichen Sprache die Worte zu finden, die diese Dinge genau charakteri­sieren."
      ],
      [
        "Wie man sagen muß: Wahrnehmen und Denken erzeugen in uns etwas, was eigentlich wie ein Ertöten ist - beim Denken allerdings durch die Gegenwirkung zugleich eine Art Anfeuerung zu einem künftig Lebendigen -, so müssen wir sagen: Jedes Gefülil, das in uns sitzt, jedes Gefühl, das in uns auftritt, wird eigentlich nicht ganz ge­boren in uns, kommt nicht ganz zum Dasein.",
        "Würde alles, was in uns sitzt indem wir fühlen, herauskommen, so würde uns das, was da im Gefühle lebt, ganz anders ergreifen, ganz anders durchkraften."
      ],
      [
        "was hinter dem Gefühle sitzt, was das Gefühl zu einem Lebewesen macht, zu einem Lebewesen, dessen Leben gespeist wird aus dem ganzen Planetensystem, das kommt nicht unnittelbar heraus.",
        "Das Gefühl kommt wiederum nur wie ein Schatten dessen, was es eigent­lich ist, aus uns heraus.",
        "Das bewirkt, daß wenn man einmal so recht in seine Gefühiswelt mit einer tieferen Menschheitsempfindung Ein­gang findet, man eigentlich jedem Gefühle gegenüber etwas Unbe­friedigendes empfindet.",
        "Jedem Gefühle gegenüber empfindet man, es könnte gesteigert werden, es könnte stärker hervortreten.",
        "Namentlich muß man dem Gefühle gegenüber etwas wie ein geheimes Erlebnis haben: es könnte uns viel mehr verraten, als in ihm liegt, es verbirgt etwas, was in unserem Innern lebt, was in den Tiefen der Seele ist, und was nur halb geboren heraufkommt."
      ],
      [
        "Wenn wir auf unseren Willen eingehen, auf alles das, was in uns Wunsch und Wille sein kann, so ist es hier, nur in einem höheren Maße, ebenso wie es beim Gefühle ist.",
        "Nur daß hinter dem Willen die geistige Wesenheit, die Grundwesenheit steht, die eigentlich in der Sonne lebt.",
        "Nicht bloß das, was in den Planeten lebt, sondern das, was in der ganzen Sonne lebt, lebt da im Willen auch mit darin.",
        "Aber es verbirgt sich.",
        "Der Wille wird noch weniger ganz geboren als das Gefühl.",
        "Der Wille würde uns ganz, ganz anders durchdringen, wenn alles, was in ihm liegt, wirklich in unserem Bewußtsein zum Vorschein käme.",
        "Es kommt wirklich nur die alleräußerste Oberfläche des Willens, es kommen nur die alleroberflächlichsten Schaumgebilde des Willens zum Ausdruck.",
        "Das andere bleibt uns verborgen.",
        "Und warum bleibt uns im Gefühl und im Willen im Grunde genommen eine ganze Welt verborgen?",
        "Weil das, was uns verborgen bleibt, wenn es angeschaut würde vom physischen Plane aus, von uns nicht ertragen werden könnte.",
        "Vom physischen Plane aus nähme es sich so aus, daß wir es abwehren wollten, daß wir uns abwenden wollten davon."
      ],
      [
        "Das, was da im Gefühl und im Willen lebt und ungeboren ist, das ist werdendes Karma.",
        "Sagen wir, wir fühlen eine feindliche Empfin­dung gegen irgend jemand, um ein konkretes Beispiel zu wählen.",
        "Ja, was da in dieser feindlichen Empfindung zu unserem Bewußtsein kommt, das ist eben nur das äußerliche Wellenspiel.",
        "Da drinnen liegen"
      ],
      [
        "Kräfte, die über das ganze Planetensystem ausgebreitet sind.",
        "Aber das, was uns verborgen bleibt, das ist gerade das, was uns sagt: Durch deine feindliche Empfindung pflanzest du in dich etwas UnvoW kommenes, das mußt du ausgleichen. - In dem Augenblicke, wo herauf-tauchen würde, was da unten mitlebt, würde vor uns die Imagination desjenigen auftauchen, was im Karma die feindliche Empfindung aus­gleichen muß.",
        "Und wir würden uns mit Luzifer und Ahriman ver­binden, um abzuwehren diesen Ausgleich, weil wir von dem Stand­punkt des physischen Planes aus urteilen würden.",
        "Aber es wird uns auf diesem physischen Plane das verborgen: der Hüter der Schwelle verbirgt es uns, aus dem einfachen Grunde, weil wir diese Dinge, die nicht geboren werden an unserem Qefühl, an unserem Willen, nur beurteilen können, wenn wir in der geistigen Welt zwischen dem Tod und einer neuen Geburt leben.",
        "Da wollen wir das, was wir sonst nie wollen würden, da wollen wir, daß das, was einer feindseligen Stimmung entspricht, wirklich ausgeglichen werde, weil wir da das rechte Interesse haben an dem Inhalt der Götter-Religion, an dem vollkommenen Menschheitsideal, das aus uns den vollkommenen Menschen machen will.",
        "Von dem wissen wir, daß durch einen ent­gegengesetzten Ausgleich das wettgemacht werden muß, was durch eine feindselige Empfindung verursacht worden ist.",
        "Es muß für die Zukunft nach dem Tode aufbewahrt bleiben, und dann erst darf herauskommen, was ungeboren ist an unserem Gefühle und unserem Willen."
      ],
      [
        "Nun, sehen Sie, ich habe Ihnen, ich möchte sagen, ein Vierfaches von dem menschlichen Seelenkern dargelegt.",
        "Das, was von unserem Gefühl ungeboren verbleibt, lebt im Astralleib; das, was vom Willen ungeboren bleibt, lebt im Ich.",
        "Wir haben also, indem wir die äußere Welt wahrnehmen, etwas wie einen physischen Phantomleichnam in uns, der eigentlich der Spiegelbelag ist für unseren physischen Leib.",
        "Wir haben in uns einen Einschluß, gleichsam eine Durchdunkelung des Ätherleibes.",
        "Wir haben in uns etwas im Astralleib, was nicht zur Geburt kommt in der Zeit zwischen der Geburt und dem Tode, und wir haben von unserem Willen etwas, was nicht in dieser Zeit zur Geburt kommt. - Dieses Vierfache, was der Mensch in sich trägt, das"
      ],
      [
        "muß aufbewahrt werden für die Zeit zwischen dem Tod und einer neuen Geburt.",
        "Aber es lebt in uns als unser Seelenkern mit derselben Gewißheit, wie in der Pflanze der Keim für das nächste Jahr liegt.",
        "Sie sehen also, wir können nicht nur im allgemeinen von einem Seelen-kern sprechen, sondern wir können diesen Seelenkern sogar in seiner Viergliedrigkeit erfassen."
      ],
      [
        "Wenn wir, sagen wir, eine Empfindung in uns tragen, die uns Unbehagen namentlich von innen heraus verschafft, wenn wir mit unserem Leben nicht so recht einverstanden sind, so geschieht es dadurch, daß ein Druck von dem ungeborenen Teil der Empfindungen auf den bewußten Teil der Empfindungen ausgeübt wird.",
        "Wie kann dieser Druck abgehalten werden?"
      ],
      [
        "Ja, sehen Sie, dieser Druck ist etwas, unter dessen Gefahr im Grunde genommen der Mensch fortwährend steht.",
        "Denn das, was ich Ihnen jetzt geschildert habe, das ist, insofern es sich auf Gefühl und Wille bezieht, also auf das, was eigentlich unser inneres Seelenleben im Sinne des ersten Vortrages so recht darstellt, dasjenige, was uns in innere Disharmonie bringt."
      ],
      [
        "Wir würden, wenn richtiger Einklang herrschte zwischen dem geborenen Teil von Gefühl und Wille und dem, was hinter der Schwelle des Bewußtseins bleibt, wenn richtiges Verhältnis, richtige Harmonie bestünde, als in der Sinneswelt befriedigte und tüchtige Menschen durch diese Sinneswelt gehen.",
        "Hier liegt eigentlich der Grund zu allen inneren Unzufriedenheiten."
      ],
      [
        "Wenn jemand innere Un­zufriedenheiten hat, so kommt es von dem Druck des unterbewußten Teiles des Fühlens und Wollens."
      ],
      [
        "Nun muß ich zu dem Auseinandergesetzten hinzufügen, daß sich in bezug auf alle diese Verhältnisse, die ich jetzt geschildert habe, allerdings die Wesenheit des Menschen im Laufe ihrer Entwickelung geändert hat.",
        "Genau so, wie ich die Dinge jetzt geschildert habe, ver­halten sie sich eigentlich in unserer Zeit.",
        "Sie verhielten sich nicht immer so.",
        "In älteren Zeiten der Menschheitsentwickelung, sagen wir während der urpersischen, ägyptischen, der altindischen Epoche, war das anders.",
        "Da flossen ja natürlich in genau derselben Weise die Wahr­nehmungen herein, und in ihnen waren enthalten die Imaginationen, Inspirationen, Intuitionen, aber es blieben für ältere Zeiten diese Imaginationen, Inspirationen, Intuitionen nicht so ganz wirkungslos"
      ],
      [
        "auf den Menschen wie heute.",
        "Sie töteten nicht so völlig das innere Physische des Menschen, sie lieferten keinen so dichten mineralischen Einschlag, und das kam davon her, daß in diesen älteren Zeiten von der anderen Seite her, aus Gefühl und Wille etwas aufschoß, wenn die Wahrnehmungen von außen kamen unter gewissen Verhältnissen."
      ],
      [
        "Wenn wir zum Beispiel zurückgehen in die älteren Zeiten der ägypti­schen, der babylonischen Kultur und dort die Menschen betrachten, so nahmen eben diese Menschen ganz anders wahr.",
        "Sie standen aller­dings wie wir der äußeren Sinneswelt gegenüber, aber ihr Leib war noch so organlsiert, daß die in den Sinneswahrnehmungen verborge­nen Imaginationen nicht völlig ertötend wirkten, sondern daß sie mit einer gewissen Lebendigkeit an die Menschen herandrangen."
      ],
      [
        "Dadurch aber, daß sie lebendig hereindrangen, riefen sie innerlich im Menschen das Gegenbild heraus dessen, was nun für uns ganz ver­borgen bleibt im Ich und im astralischen Leib.",
        "Die geistigen Wesen­heiten des Sonnenhaften und des Planetensystems drängten sich von innen heraus entgegen und spiegelten gewissermaßen das, was sich belebte durch die Imagination."
      ],
      [
        "So daß es für den Angehörigen der älteren ägyptischen, der babylonischen Kultur gewisse Zeiten des Wahrnehmens gab, wo er, wenn er den Blick hinausrichtete in die physische Welt, nicht nur so die physischen Wahrnehmungen auf­nahm, wie wir sie haben, sondern wo sie sich belebten.",
        "Er wußte, dahinter steckt etwas, was in Imaginationen sich auslebt."
      ],
      [
        "Daher war er auch noch nicht so töricht, nach dem Muster unserer gegenwärtigen Physiker hinter den Wahrnehmungen materielle Atomschwingungen zu vermuten, sondern er wußte, daß da Leben dahinter ist, und aus seinem Innern tauchten auf entgegenstrahlend die Bilder des belebten Sternenhimmels, sogar die Sonne.",
        "Besonders stark war das während der persischen Kultur, wo wirklich beim äußeren Wahrnehmen etwas wie die innere geistige Sonnenkraft aufleuchtete - Ahura Mazdao I"
      ],
      [
        "Wenn wir in noch ältere Zeiten zurückgehen, so finden wir dieses Zusammenwirken, dieses Entgegenkommen des Inneren und des Äußeren noch viel stärker ausgeprägt.",
        "Heute kann das nicht mehr sein, aber ein Ersatz kann da sein, und hier kommen wir an einen Punkt, wo wir, ich möchte sagen, aus der Sache selbst heraus unsere"
      ],
      [
        "Aufgabe innerhalb der anthroposophischen Weltanschauung wirklich verstehen werden.",
        "Ein Ersatz muß geschaffen werden.",
        "Wir stehen der Außenwelt mit unseren Wahrnehmungen gegenüber.",
        "Wir denken über sie, indem uns ein Teil dieser Außenwelt verschlossen bleibt, der ertötend und durchdunkelnd auf uns wirkt.",
        "Aber wir können das, was da ertötet und durchdunkelt wird, durch die Geisteswissenschaft beleben.",
        "Und gerade durch die Belebung dessen, was sonst ertötet und durchdunkelt wird, entsteht solche Wissenschaft, wie sie dargestellt worden ist in der Entwickelung durch Saturn-, Sonnen- und Monden-entwickelung in meiner «Geheimwissenschaft».",
        "Dieses Wissen von der Saturn-, Sonnen- und Mondenentwickelung hat jeder Mensch, nur ist es in den Untergründen seines Bewußtseins.",
        "Er möchte nicht Erdenmensch sein, wenn er es so ohne weiteres schauen würde, ohne die genügende Vorbereitung.",
        "Er möchte, daß die Erde ihn gar nichts anginge und er mit der Mondenentwickelung abschliessen könnte.",
        "Alles das, was wir an Erkenntnissen erwerben können durch die Geistes­wissenschaft, erhellt uns das, was uns von der Entwickelung der Ver­gangenheit verborgen bleibt, indem es in uns eindringt.",
        "Denn was da an Imaginationen, Inspirationen und Intuitionen draußen lebt in den Sinnesempfindungen und nicht hereinkommt, das ist eigentlich, wenn man es durch den Schleier der Sinnesempfindungen anschaut, dasjenige, was wir an Vergangenheit durchgemacht haben."
      ],
      [
        "Etwas anderes ist es mit dem, was in unserem Fühlen und Wollen lebt.",
        "Der Mensch kann sagen - und viele Menschen der Gegenwart haben ja einen Drang, das zu tun -: Oh, was geht mich das alles an, was da diese vertrakten Köpfe aussinnen oder ausgesonnen haben über eine übersinnliche Welt.",
        "Ich nehme solche Vorstellungen nicht in mich auf - Wer das sagt, hat sich niemals einen Begriff davon er­worben, warum eigentlich in die Weltentwickelung Religionen ge­kommen sind.",
        "Das ist ja das Gemeinsame aller religiösen Vorstellun­gen, daß sie sich auf Dinge beziehen, die der Mensch nicht sinnlich wahrnehmen kann, daß der Mensch in religiösen Vorstellungen mit etwas sich erfüllen muß, was er nicht sinnlich wahrnehmen kann.",
        "Vorstellungen, die von dem kommen, was man sinnlich wahrnehmen kann, die können uns niemals für unser Fühlen und Wollen einen"
      ],
      [
        "Impuls geben, der nach dem Tode Stoßkraft ist.",
        "Damit das wirken kann, was ungeboren in uns ist in unserem Gefühl, in unserem Willen, weil es ja wirken soll nach unserem Tode, brauchen wir dazu die Vor­stellungen nicht, die wir uns durch unsere Sinnesempfindungen an-eignen können oder durch den Verstand, der an das Gehirn gebunden ist; die helfen uns nichts.",
        "Einzig und allein diejenigen Vorstellungen, die dem entsprechen, was nicht äußerlich wirklich ist, die, wenn wir sie aufnehmen, uns fromm machen, durch die wir aufsehen in eine geistige Welt, die geben uns den Impuls, die Schwungkraft, die wir nach dem Tode brauchen.",
        "Religiös vorstellen heißt: das vorstellen, was jetzt noch nicht in uns wirken kann, was aber Wirkungskraft ist nach dem Tode.",
        "Mit den religiösen Vorstellungen nehmen wir nicht nur Erkenntnisvorsteliungen auf, sondern etwas, was wirksam werden kann nach unserem Tode, und was gerade deshalb jetzt so sein muß im physischen Leib, daß derjenige, der auf solche Wirkungskräfte nicht reflektieren will, darüber lachen kann und es abweisen kann in seinem Materialismus.",
        "Er hat aber nur eine gelähmte Kraft, um vor­wärts zu bringen, was ungeboren ist in seinem Fühlen und Wollen, wenn er sich nicht durchdringt mit den Vorstellungen über das Über-sinnliche."
      ],
      [
        "Daher muß es so oft betont werden: Was vergangen ist, wird er­leuchtet von dem hellsichtigen Bewußtsein.",
        "Es wird gegenwärtig wieder erkannt, auch insofern es hinter dem Schleier der Sinneswelt als Imagination, Inspiration und Intuition vorhanden ist und hinein-wirkt in die Sinneswelt.",
        "Früher wurde es den Menschen gegeben als religiöser Glaube, damit die Menschen nicht alle Schwungkraft für die Zeit nach dem Tode verlieren, damit sie etwas im Seelenkern haben, was ihn lebendig erhalten kann, auch wenn er den physischen Leib abgelegt hat.",
        "Jetzt ist die Zeit gekommen, wo die Menschen aus dem Verständnis heraus, aus dem Verständnis der Geisteswissenschäft heraus, sich Vorstellungen aneignen sollen über die übersinnlichen Welten.",
        "Deshalb kann es nicht oft genug betont werden: Erforschen kann man nur als Geistesforscher diese Dinge in der übersinnlichen Welt.",
        "Sind sie aber erforscht und werden sie mitgeteilt, so gibt es etwas in unserer tiefsten Seele, was eine geheime Sprache dieser Seele"
      ],
      [
        "ist, und was verstehen, begreifen kann dasjenige, was von dem Geistesforscher erforscht wird.",
        "Nur wenn die Vorurteile des Verstan­des und der Sinne kommen, dann wird als Unsinn angesehen, als Torheit und als Phantasterei, was von der Geistesforschung als über­sinnliche Vorstellungen gegeben wird, und was, wenn es aufgenom­men wird, uns Schwungkraft gibt für den Seelenkern, damit er in alle Zukünfte seine Wege finden kann im Kosmos.",
        "Erforschen werden immer nur diejenigen den Inhalt der geistigen Welt, die eine esoteri­sche Entwickelung durchmachen.",
        "Diesen Inhalt wissen, ihn innerlich im Bewußtsein durcharbeiten, ihn in Ideen und Begriffen haben, ihn als eine Gewißheit des Seins der Seele in der geistigen Welt besitzen, das ist etwas, was immer mehr und mehr als eine notwendige geistige Nal:rung die Menschen brauchen werden."
      ],
      [
        "Das ist es, was uns zeigt, wie man aus der Sache heraus die Mission unserer anthroposophischen Bewegung verstehen kann.",
        "In alten Zeiten war es eben noch so, daß die Erkenntnis von oben sich belebte und der Inhalt zu dieser Erkenntnis von unten entgegenkam.",
        "Daher hatten die Alten von den geistigen Welten noch ein unmittelbares Bewußtsein, das sich aber immer mehr und mehr abdunkelte und ab­dumpfte.",
        "Hätte es sich nicht abgedunkelt und abgedumpft, so wäre der Mensch nicht zum vollen Bewußtsein seines Ich gekommen.",
        "Zum vollen Bewußtsein seines Ich kann der Mensch nur dadurch kommen, daß er im höchsten Maße innerhalb seines physischen Leibes jenes Leichnam-Phantom ausbildet, von dem ich gesprochen habe.",
        "Es muß sozusagen unser physischer Leib als durchsichtige Wesenheit ganz belegt werden mit Spiegelbelag, und erst, wenn er ganz belegt ist, dann können wir uns ganz so fühlen, daß wir sagen: Ich bin ein Ich.",
        "Dieses vollständige Belegen hat sich aber erst langsam und allmählich gebildet.",
        "Es hat sich im Laufe der Menschheitsentwickelung gebildet, und es war diese Bildung vollendet in der Zeit, in die das Mysterium von Golgatha fiel.",
        "Da war der Spiegelbelag fertig.",
        "Vorher, da begeg­neten sich noch immer Unteres und Oberes, da kamen in der Men­schenwesenheit Unteres und Oberes zusammen.",
        "Aber, man möchte sagen, ganz herausgedrängt würde Unteres und Oberes dadurch, daß der Spiegelbelag vollkommen war, und der Mensch nur die Spiegelung"
      ],
      [
        "aus dem physischen Leibe wahrnahm.",
        "Das war erst, als das Ereignis von Golgatha in die Menschheitsentwickelung hereinkam."
      ],
      [
        "Was war denn da eigentlich geschehen?",
        "Ja, sehen wir nur ganz genau auf das hin, was da geschehen war!",
        "Stellen Sie sich so recht diese alten Menschen vor in den Zeiten vor dem Mysterium von Golgatha, stellen Sie sich dieses Bewußtsein vor!",
        "Da kommt von außen herein die Belebung von Imaginationen; von innen steigen auf Bilder der außermenschlichen geistigen Welt.",
        "Was sind diese Bilder, die da aufsteigen im Menschen?",
        "Wie wir wissen, war das in alten Zeiten bei herabgedämpftem menschlichen Bewußtseinszustand mög­lich.",
        "Diejenigen, die diese Dinge erkannten, die in alten Zeiten als Eingeweihte hinzublicken vermochten auf die menschliche Seele, wie in ihr noch lebte dieses Zusammenkommen der belebten Imagination von außen, und von innen das Schauen, die sagten nicht: Der Mensch schaut das allein, sondern diese alten Eingeweihten sagten: Es schaut an seine Welt im Menschen zum Beispiel Jahve oder Jehova, wie dies bei den alten Juden der Fall war.",
        "Der Gott denkt im Menschen.",
        "Wie wir heute sagen in unserem Entwickelungszyklus, wenn wir Gedanken haben: Ich denke, - so sagten diejenigen, die die Dinge wußten in alten Zeiten, wenn die Schmungen auftauchten aus der geistigen Welt: Die Götter denken in uns.",
        "Oder als man die Einheit des Gött­lichen im Monotheismus erkannte: Jahve denkt im Menschen.",
        "Der Mensch ist der Schauplatz der göttlichen Gedanken.",
        "Erfüllt wußten sich die Menschen, so daß sie sagten: In mir denken die Götter."
      ],
      [
        "Aber in der menschlichen Entwickelung lag die Notwendigkeit, daß dies immer unmöglicher wurde.",
        "Man möchte sagen, immer mehr und mehr traten Finsternis den Schauungen, den Gedanken der Götter entgegen in der menschlichen Natur.",
        "Das innere Leicbnam-Phantom wurde immer stärker, immer bedeutender.",
        "Die Zeit rückte heran, wo aus der menschlichen Natur heraus den Göttern keine Gedanken mehr entgegentauchten.",
        "Da fühlte diejenige göttliche Wesenheit, von der man sagen kann, sie dachte durch die menschliche Wesenheit, daß ihr Bewußtsein - denn dieses Bewußtsein besteht ja in ihren Gedanken -immer dumpfer, immer dämmeriger wurde.",
        "Und die Sehnsucht ent­stand in diesem göttlichen Wesen, eine neue Form des Bewußtseins"
      ],
      [
        "zu erwecken.",
        "Menschen kommen zu einer anderen Form des Bewußt­seins.",
        "Götter, indem sie ein neues Bewußtsein schaffen, schaffen mit diesem etwas Wesentliches; für sie entsteht damit etwas Wesentliches.",
        "Und dieses Wesentliche, was da entstand, war für die jetzt gemeinte göttliche Wesenheit, die ihr Bewußtsein herabdämmern fühlte: der Christus.",
        "Der Christus ist das Kind der Gottheit, das wieder herstellt das Bewußtsein der Gottheit in der menschlichen Wirksamkeit.",
        "So mußte sich eingliedern in die menschliche Wesenheit die Christus­wesenheit."
      ],
      [
        "Und wir müssen das Bewußtsein in uns aufnehmen: Indem wir die Sinneswelt wahrnehmen, strömen wir fortwährend in uns ein - Ster­ben.",
        "Und Finsternis und Verdunkelung strömen wir in uns ein, indem wir diese Welt denken.",
        "Und Ungeborenes lassen wir, indem wir fühlen und wollen.",
        "Das alles sitzt unten in den Untergründen unseres Be­wußtseins, da lassen wir hineinfließen unser Sterben und unser noch Ungeborenes, das wir erst brauchen können, nachdem wir gestorben sein werden.",
        "Das aber würde lahm sein, wenn wir es nicht einsenken könnten in die Wesenheit, die sich die Gottheit wie die Wesenheit eines neuen Bewußtseins geboren hat, wenn wir es nicht einffießen lassen könnten in die Christus-Wesenheit."
      ],
      [
        "Dieses Bewußtsein können wir haben, indem wir den Sinn der ganzen Evolution wirklich erkennen durch die Geisteswissenschaft: Ja, wir senden da hinunter in die unterbewußten Gründe das, was in uns erstirbt.",
        "Aber aufgenommen wird es, dieses Sterben, das wir in unsere eigene Wesenheit immer mehr und mehr hineinsenken, auf­genommen wird es von dem uns entgegenlebenden Christus.",
        "In dem was in uns erstirbt, in uns erdunkelt, ungeboren bleibt, lebt uns der Christus auf.",
        "Wir lassen hinuntersterben in uns dasjenige, was sterben muß, damit wir dem wirklichen Menschheitsideal mit all unseren Anlagen uns nähern.",
        "Aber das, was wir als Sterben in uns hinein-gießen, gießen wir in die Christus-Wesenheit, so wie sie seit der Be­gründung des Christentums die menschliche Evolution durchzieht, hinein.",
        "Und das, was in uns ungeboren bleibt, unser Fühlen und Wollen, wir wissen, daß es aufgenommen wird von der Christus-Substanz, in die es eingesenkt wird nach dem Tode."
      ],
      [
        "Da, in uns, lebt der Christus, seitdem er das Mysterium von Gol­gatha durchlebt hat.",
        "In den Christus hinein senken wir das Sterben, das vorhanden ist mit jeder Wahrnehmung.",
        "Und wir senken in die Christus-Wesenheit hinein die Abdunkelung im Denken.",
        "In das Licht, in das geistige Sonnenlicht des Christus senden wir unsere abgedun­kelten Gedanken hinein.",
        "Und wenn wir durch die Pforte des Todes schreiten, dann tauchen ein unsere ungeborenen Gefühle und unser ungeborenes Wollen in die Christus-Substanz.",
        "Verstehen wir die Ent­wickelung recht, so sagen wir zu dieser Entwickelung: Wir sterben in den Christus hinein."
      ],
      [
        "In Christo morimur."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "VIERTER VORTRAG Wien, 12. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Bei dem zweiten hier gehaltenen öffentlichen Vortrage habe ich in großen Zügen zu schildern versucht, soweit das eben bei einem öffentlichen Vortrage möglich ist, das Leben, wie es für den Menschen zwischen dem Tod und einer neuen Geburt verfließt. Das, was uns da entgegengetreten ist, soll uns in den beiden nächsten Vorträgen in einer vertiefteren Art noch beschäftigen, vertieft namentlich da­durch, daß es uns so erscheinen soll, daß es das Leben auch hier in der physischen Welt immer mehr und mehr erklärt. Um aber zu einer solchen Vertiefung der Darstellung zu kommen, bedarf es der Vor­bereitung, die in den drei vorhergehenden Vorträgen gegeben wurde und in dem heutigen wiederum gegeben werden soll. Gerade diese Vorträge sollen uns die Mittel liefern, das öffentlich Vorgetragene weiter zu vertiefen.",
      "Es ist von mir da oder dort unseren Freunden öfter gesagt worden, daß der Mensch, wenn er die geistigen Welten kennen lernen und ver­stehen lernen will - und in den geistigen Welten leben wir ja zwischen dem Tod und einer neuen Geburt - in vieler Beziehung sich Begriffe und Vorstellungen aneignen muß, die man gar nicht aus den Erleb­nissen und Erfahrungen des physischen Planes heraus haben kann, die aber, wenn sie sich die Menschheit immer mehr und mehr aneignen wird, von unendlicher Wichtigkeit, von einer immer größer werdenden Wichtigkeit sein werden gerade auch für das Leben auf dem physischen Plan. Zunächst wollen wir uns heute einmal einen Unterschied des Erlebens in der geistigen Welt und des Erlebens auf dem physischen Plane klar machen, welcher im Grunde genommen wenn er uns zum erstenmale vor die Seele tritt, im höchsten Maße frappieren und sonderbar erscheinen muß, so daß es sehr leicht sein kann, daß wir den Glauben haben, wir könnten solche Dinge nur schwer verstehen. Je mehr wir uns aber in die Geisteswissenschaft einleben, desto mehr werden wir sehen, daß uns solche Dinge immer verständlicher und verständlicher werden.",
      "Wenn wir durch den physischen Plan gehen, wenn wir die Erleb­nisse des physischen Planes auf uns wirken lassen, so muß uns ja, wenn wir darüber nachdenken, eines ganz besonders auffallen. Das ist, daß wir auf diesem physischen Plane dasjenige vor uns haben, was wir die Realität nennen, was wir das Dasein, das Sein, die Wirk­lichkeit nennen.",
      "Man möchte sagen: Je ungeistiger ein Mensch ist, desto mehr baut er auf das, was er auf dem physischen Plan als die sich aufdrängende Realität vor sich hat. Anders steht es mit dem, was wir uns aneignen wollen auf dem physischen Plane als unser Wissen, unsere Erkenntnis von der Wirklichkeit.",
      "Wir müssen zunächst als Kinder überhaupt erst dazu erzogen werden, Fähigkeiten zu ent­wickeln, um uns ein Wissen, eine Erkenntnis von dem physischen Plane anzueignen, und wir müssen dann immer weiter und weiter arbeiten. Das Erwerben von Erkenntnissen setzt geistige Arbeit voraus.",
      "Die Natur, das heißt die äußere Wirklichkeit, gibt nicht von selber her, was in ihr als Weisheit steckt, was in ihr als ihre Gesetz­mäßigkeit steckt. Wir müssen uns die Kenntnis dieser Weisheit, dieser Gesetzmäßigkeit aneignen.",
      "Und darin besteht ja alles menschliche Wissensstreben, aktiv sich anzueignen aus den passiv empfangenen Erlebnissen und Erfahrungen dasjenige, was als Weisheit, als Gesetz­mäßigkeit in den Dingen steckt. Ganz anders sind nun die Dinge, wenn man sich entweder durch die zur Geistesforschung führenden Übungen oder durch den Durchgang durch die Pforte des Todes in die geistige Welt hineinbegibt.",
      "Es ist allerdings das Verhältnis des Menschen zur geistigen Umwelt nicht unter allen Umständen so, wie ich es jetzt schildern werde; aber in wichtigen Momenten, bei wichti­gen Erlebnissen ist es so. Es ist ja auch bei unserem Leben auf dem physischen Plan so, daß wir nicht immer uns abarbeiten nach Er­kenntnissen, sondern wir setzen auch in diesem Arbeiten aus.",
      "So ist auch das, was ich jetzt schildern werde, nicht eine fortwährende Nötigung in der geistigen Welt, sondern es ist zuzeiten in der geistigen Welt für uns erforderlich.",
      "Das nämlich ist das Überraschende, daß es dem Menschen in der geistigen Welt nicht an Weisheit fehlt. Man kann ein Tor sein in der Sinneswelt, und die Weisheit strömt einem in der geistigen Welt nur",
      "so zu in ihrer Realität, wenn man einfach in diese geistige Welt hineinversetzt wird. Weisheit, dasjenige, was wir uns in der physischen Welt mit Mühe aneignen, was wir uns erarbeiten müssen von Tag zu Tag, wenn wir es haben wollen, das haben wir in der geistigen Welt so, wie wir in der physischen Welt um uns herum die Natur haben. Es ist immer da und es ist in reichlichstem Maße da. Gewissermaßen können wir sagen: Je weniger Weisheit wir uns auf dem physischen Plan angeeignet haben, desto reichlicher strömt uns diese Weisheit auf dem geistigen Plane zu. Aber nun haben wir gegenüber dieser Weisheit auf dem geistigen Plane eine bestimmte Aufgabe.",
      "Ich habe Ihnen in den letzten Tagen davon gesprochen, daß man auf dem geistigen Plane das Menschheitsideal, den Inhalt der Götter-religion vor sich hat, daß man sich dahin durcharbeiten muß. Das kann man nicht, wenn man nicht in die Lage kommt auf dem geistigen Plan, sein Wollen dort, also jetzt das Wollen, das fühlende Wollen, das wollende Fühlen, Wollen und Fühlen so anzuwenden, daß man die Weisheit, die einem immer fort und fort zuströmt, die da ist wie die Erscheinungen der Natur in der physischen Welt, fortwährend vermindert, daß man fortwährend von ihr etwas wegnimmt.",
      "Man muß diese Fähigkeit haben, von der Weisheit, die dort einem entgegen-tritt, immer mehr und mehr wegzunehmen. Hier auf dem physischen Plan müssen wir immer weiser und weiser werden, dort müssen wir uns bemühen, unser Wollen, unser Fühlen so anzuwenden, daß wir von der Weisheit immer mehr und mehr wegnehmen, sie verdunkeln.",
      "Denn je weniger wir dort von der Weisheit wegnehmen können, desto weniger finden wir die Kräfte, um uns so mit diesen Kräften zu durchsetzen, daß wir uns als reale Wesen dem Menschheitsideale annähern. Dieses Annähern muß darin bestehen, daß wir immer mehr und mehr von der Weisheit wegnehmen.",
      "Was wir da wegnehmen, das können wir umwandeln in uns selber, so daß die umgewandelte Weisheit die Lebenskräfte sind, die uns zu dem Menschheitsideale hintreiben. Diese Lebenskräfte müssen wir uns in dieser Zeit zwischen dem Tod und einer neuen Geburt erwerben.",
      "Nur dadurch kommen wir in einer regelrechten Weise der neuen Verkörperung entgegen, daß wir die Weisheit, die uns reichlich zufließt, in Lebenskräfte umwandeln.",
      "Und wir müssen, wenn wir wieder auf der Erde ankommen, so viel Weisheit in Lebenskräfte umgewandelt haben, müssen soviel von Weisheit vermindert haben, daß wir genug Lebenskräfte haben, um die Vererbungssubstanz, die wir von Vater und Mutter bekommen, mit ge­nügend organisierenden geistigen Lebenskräften zu durchdringen. Wir müssen also von der Weisheit immer mehr und mehr wegnehmen.",
      "Wenn man einen rechten Materialisten, der dem Geiste gar keine Realität zuerkennt auf dem physischen Plane, nach dem Tode wieder auffindet, einen solchen Materialisten, der während seines Lebens gesagt hat: Das ist ja alles Torheit, was ihr da über den Geist sprecht. Eure Weisheit ist die reinste Phantasterei, die weise ich ganz von mir, ich lasse gar nichts anderes gelten als die Beschreibung dessen, was äußere Natur ist. - Bei einem solchen Menschen, wenn er nach dem Tode getroffen wird, sieht man so reichlich Weisheit zuströmen, daß er sich gar nicht retten kann.",
      "Von überallher strömt ihm der Geist zu. In demselben Maße, als er hier nicht geglaubt hat an den Geist, in demselben Maße ist er dort überall von Geist umflutet. Jetzt tritt an ihn die Aufgabe heran, diese Weisheit in Lebenskräfte umzuwan­deln, so daß er eine physische Realität schaffen kann in der nächsten Inkarnation.",
      "Er soll das, was er Realltät genannt hat, heraus erzeugen aus dieser Weisheit, er soll diese Weisheit vermindern. Sie will sich aber von ihm nicht vermindern lassen, sie bleibt wie sie ist. Er be­kommt es nicht fertig, Realität daraus zu machen.",
      "Die ungeheure Strafe des Geistes steht vor ihm, daß er, während er hier auf dem physischen Plan nur auf Realität gebaut hat in seinem letzten Leben, während er den Geist ganz geleugnet hat, er sich sozusagen vor dem Geist nicht retten kann, und er nichts von diesem Geiste realisieren kann. Er steht immer vor der Gefahr, daß er gar nicht in die physische Welt wiederum hereinkommen kann durch Kräfte, die er selbst erzeugt.",
      "Er lebt fortwährend in der Furcht: Der Geist wird mich hereindrängen in die physische Welt, und ich werde dann ein physi­sches Dasein haben, das alles das verleugnet, was ich im vorher­gehenden Leben als das Richtige anerkannt habe. Ich werde mich hereinstoßen lassen müssen von dem Geist in die physische Realität, ich werde es nicht selbst zu einer Realität bringen.",
      "Das ist allerdings etwas Frappierendes, aber die Sache ist so. Um sozusagen in dem Geiste zu ersticken nach dem Tode und keine Realität, wie man sie allein verehrt hat vor dem Tode, in ihm zu finden, dazu ist der Weg der, vor dem Tode ein rechter Materialist zu sein und den Geist abzuleugnen. Dann erstickt man oder ertrinkt man im Geiste.",
      "Das sind allerdings Vorstellungen, die wir uns im Laufe unseres Betriebes der geistigen Wissenschaft immer mehr und mehr aneignen müssen. Denn wenn wir uns solche Vorstellungen aneignen, führen sie uns auch im physischen Leben in einer harmonischen Weise weiter und zeigen uns gewissermaßen, wie die beiden Seiten des Lebens einander ergänzen und ausgleichen müssen. Wir begründen in uns den Instinkt, in unserer Lebensführung diesen Ausgleich wirklich herbeizuführen.",
      "Noch einen anderen Fall möchte ich vom Zusammenhang des physischen Lebens mit dem geistigen Leben anführen. Nehmen wir jetzt einmal einen ganz konkreten, einzelnen Fall. Nehmen wir an, wir haben auf dem physischen Plane jemand angelogen. Nicht wahr, ich rede also von einzelnen Fällen. Wenn wir jemanden angelogen haben, so fällt das in einen bestimmten Zeitpunkt. Das, was ich jetzt als Entsprechendes in der geistigen Welt schildern werde, fällt wie­derum in einen bestimmten Zeitpunkt zwischen dem Tod und einer neuen Geburt. Nehmen wir also an, wir hätten jemanden zu einer gewissen Zeit auf dem physischen Plan angelogen, dann kommt bei unserem Aufenthalt in der geistigen Welt, sei es, daß wir durch Initiation hineinkommen oder durch den Tod, ein Zeitpunkt, wo wir mit unserer Seele in der geistigen Welt ganz, ganz erfüllt sind von der Wahrheit, die wir hätten sagen sollen. Aber diese Wahrheit, die quält uns, diese Wahrheit steht vor uns, in demselben Maße uns quälend, als wir von ihr abgeirrt waren bei der Lüge. Man braucht also nur zu lügen auf dem physischen Plan, um einen Zeitpunkt herbeizuführen in der geistigen Welt, in dem wir durch die ent­sprechende Wahrheit, die der Lüge entgegengesetzt ist, gequält wer­den dadurch, daß diese Wahrheit in uns lebt und uns brennt und wir sie nicht ertragen können. Unser Leiden besteht namentlich darin, daß",
      "wir einsehen: das ist die Wahrheit. Wir sind aber so, daß uns diese Wahrheit keinen Genuß, keine Freude, keine Lust bereitet, sondern uns quält. Von den guten Sachen gequält zu werden, von dem, wovon man weiß, daß es einen erheben sollte, gequält zu werden, das gehört zu den Eigentümlichkeiten der Erlebnisse in der geistigen Welt.",
      "Man braucht zum Beispiel im Leben nur einmal bei einer Sache, gegenüber welcher Fleiß uns Pflicht gewesen wäre, faul gewesen zu sein, dann kommt eine Zeit in der geistigen Welt, wo der Fleiß, der uns dazumal gefehlt hat, in uns lebt. Er ist da, der Fleiß, er kommt ganz sicher, er lebt in uns, wenn wir einmal so recht faul gewesen sind auf dem physischen Plan. Es kommt dann eine Zeit, wo wir durch die inneren Notwendigkeiten diesen Fleiß unbedingt in uns anwenden müssen. Wir geben uns ganz diesem Fleiß hin, und wir wissen, er ist etwas ungeheuer Wertvolles, aber er quält uns, wir leiden unter ihm.",
      "Oder nehmen wir einen Fall, welcher vielleicht weniger in der menschlichen Willkür liegt, welcher in anderen Vorgängen des Lebens liegt, die mehr, ich möchte sagen, in den Untergründen des Daseins vor sich gehen und mit dem Verlauf unseres Karmas zusammen­hängen; nehmen wir den Fall, wir seien durch eine Krankheit durch­gegangen im physischen Leben. Wenn wir im physischen Leben durch eine Krankheit durchgegangen sind, die uns Schmerzen oder der­gleichen bereitet hat, so erleben wir zu irgend einem Zeitpunkt in der geistigen Welt die entgegengesetzte Stimmung, die entgegengesetzte",
      "Verfassung: die der Gesundheit, des Gesundseins. In demselben Maße, in dem uns die Krankheit geschwächt hat, stärkt uns diese Stimmung des Gesundseins bei unserem Aufenthalt in der geistigen Welt. Das ist ein Fall, der vielleicht nicht nur wie die anderen Dinge, die vorgebracht worden sind, unsern Verstand schockiert, sondern der viel tiefer in das Empfindungsgemäße unserer Seele eindringt, diese Seele irritiert. Wir wissen ja, daß geisteswissenschaftliche Dinge immer mit der Empfindung aufgefaßt werden müssen. Aber wir müssen bei diesem Fall das Folgende bedenken: Wir müssen uns klar machen, daß ja hier gleichsam etwas wie ein Schatten ist über dem Zusammen­hang zwischen der physischen Krankheit und der uns stärkenden Gesundheit in der geistigen Welt. Wahr ist der Zusammenhang, aber",
      "es gibt etwas in der Menschenbrust, was dem Gefühle nach mit diesem Zusammenhang nicht recht einverstanden sein kann. Das muß durch­aus zugegeben werden. Dafür aber hat dieser Zusammenhang noch eine andere Wirkung, wenn er wirklich von uns erfaßt wird. Und diese Wirkung kann in der folgenden Weise charakterisiert werden.",
      "Nehmen wir einmal an, ein Mensch durchdringt sich mit Geistes­wissenschaft, ein Mensch gibt sich ernstlich Mühe, Geisteswissen­schaft wirklich in sich aufzunehmen, nicht so, wie man eine andere Wissenschaft aufnimmt. Die kann man theoretisch studieren, in bloßen Gedanken, Begriffen kann man sich aneignen, was sie gibt.",
      "Geisteswissenschaft soll man niemals nur so aufnehmen. Sie soll wie ein geistiges Lebensblut in uns werden. Geisteswissenschaft soll in uns weben und leben, sie soll eigentlich in allen Begriffen, die sie uns gibt, in uns auch Empfindungen, Gefühle wachrufen.",
      "Es gibt eigent­lich für einen, der Geisteswissenschaft wirklich mit rechtem Ohr anhört, nichts in dieser Geisteswissenschaft, was uns nicht entweder auf der einen Seite erhebt oder auf der andern Seite in die Abgründe des Daseins schauen läßt, um uns gerade auch in diesen Abgründen zurechtfinden zu lassen. Man kann sagen: Wer Geisteswissenschaft richtig versteht, verfolgt das, was sie sagt, überallhin auch mit diesen und jenen Gefühlen.",
      "Wer Geisteswissenschaft in sich aufnimmt, der wird einfach dadurch, daß die geisteswissenschaftlichen Begriffe in ihm leben, daß er sich diejenigen Vorstellungs-Gewohnheiten an­eignet, die jetzt gerade angedeutet worden sind als notwendig gegen­über der Geisteswissenschaft, wirklich seine Seele schon in der physischen Welt umwandeln. Ich habe ja öfter darauf aufmerksam gemacht, wie zu den besten, eindringlichsten Übungen das Studium, das ernstliche Studium der Geisteswissenschaft selbst gehört.",
      "Nun stellt sich allmählich bei dem Menschen, der also in die Geisteswissenschaft eindringt, etwas Eigentümliches heraus. Ein sol­cher Mensch, der vielleicht Übungen macht, vielleicht nicht einmal Übungen macht, um selbst Geistesforscher zu werden, sondern der sich nur ernstlich bemüht, Geisteswissenschaft zu verstehen, ein solcher wird vielleicht lange, lange nicht daran denken können, selber etwas hellseherisch zu schauen. Er wird es einmal können, aber das",
      "kann vielleicht noch ein fernes Ideal bei ihm sein. Aber wer Geistes­wissenschaft in dem angedeuteten Sinne wirklich auf seine Seele wirken läßt, der wird sehen, daß sich in seiner Seele die Instinkte des Lebens, die mehr unbewußten Triebfedern des Lebens ändern.",
      "Seine Seele wird wirklich anders. Man begibt sich nicht in den Betrieb der Geisteswissenschaft hinein, ohne daß diese Geisteswissenschaft die Seele instinktiv beeinflußt, sie anders macht, ihr andere Sympathien und Antipathien gibt, sie gleichsam mit einem Licht durchgießt, so daß sie sicherer fühlt als sie vorher gefühlt hat.",
      "Das kann man auf jedem Gebiete des Lebens bemerken; auf jedem Gebiete des Lebens äußert sich die Geisteswissenschaft in der geschilderten Weise. Man kann ein ungeschickter Mensch sein im Leben und wird Geistes-wissenschafter, und man wird sehen, daß, ohne daß man irgend etwas anderes getan hat, als sich mit dieser Geisteswissenschaft zu durch­dringen, man bis in die Handgriffe hinein geschickter wird.",
      "Sagen Sie nicht: Ich kenne sehr ungeschickte Geisteswissenschafter, die sind noch lange nicht geschickt geworden! Versuchen Sie nachzudenken darüber, inwiefern diese doch noch nicht so, wie es eben nach ihrem Karma nötig ist, sich wirklich innerlich durchdrungen haben mit der Geisteswissenschaft.",
      "Man kann ein Maler sein, bis zu einem gewissen Grade die Malkunst handhaben. Wird man Geisteswissenschafter, so wird man sehen, daß das, was jetzt eben angedeutet worden ist, in die instinktive Handhabung der Malkunst einfließt.",
      "Man mischt leichter die Farben, Ideen, die man haben will, kommen einem eher. Oder nehmen wir an, man sei Gelehrter, man solle irgendwie etwas Wissen­schaftliches arbeiten. Gar mancher, der in diesem Falle ist, wird wissen, was es oft für Mühe kostet, die Literatur zusammenzusuchen, um irgend eine Frage zu lösen.",
      "Wird man Geisteswissenschafter, so geht man nicht mehr wie früher in die Bibliotheken und läßt sich erst fünfzig Bücher geben, die nichts nutzen, sondern man greift unmittel­bar an das Richtige. Es greift wirklich Geisteswissenschaft in das Leben ein, macht die Instinkte anders, versetzt in unsere Seele Triebfedern, die uns geschickter ins Leben hineinstellen.",
      "Natürlich muß das, was ich jetzt sagen werde, immer so betrachtet werden, daß es im Zusammenhang gedacht wird mit dem menschlichem",
      "Karma. Dem Karma ist der Mensch unter allen Umständen unterworfen; das muß stets berücksichtigt werden. Aber jetzt, mit Berücksichtigung des Karmas, ist doch das Folgende der Fall: Neh­men wir an, eine bestimmte Art von Erkrankung befällt denjenigen, der in die Geisteswissenschaft in der geschilderten Weise eingedrungen ist, und es liegt in seinem Karma, daß er geheilt werden kann.",
      "Es kann natürlich im Karma liegen, daß die Krankheit nicht geheilt werden kann. Aber Karma spricht niemals, wenn wir eine Krankheit vor uns haben, so, daß unter allen Umständen im fatalistischen Sinn &e Krankheit irgend einen Verlauf nehmen müßte, sie kann geheilt werden oder kann nicht geheilt werden.",
      "Derjenige, der sich nun durchdrungen hat mit Geisteswissenschaft, der bekommt in seine Seele eingepflanzt einen Instinkt, welcher ihm verhilft, aus sich selbst heraus der Krankheit und ihren Schwächen das entsprechende Stärkende oder Richtige entgegenzusetzen. Was man sonst erlebt als Folgen der Krankheit in der geistigen Welt, das wirkt noch in die Seelen zurück, insofern man noch im physischen Leibe ist, wirkt als Instinkt.",
      "Man beugt entweder der Krankheit vor oder aber findet in sich die Wege zu den Heilkräften. Wenn das hellseherische Bewußt­sein richtige Heilfaktoren findet für diese oder jene Krankheit, so geschieht dies auf folgendem Wege: Ein solcher Hellsehender hat die Möglichkeit, das Bild der Krankheit vor sich zu haben.",
      "Also nehmen wir an, er habe das Bild vor sich: das ist die Krankheit; so und so tritt sie schwächend an den Menschen heran. Dadurch, daß der Betreffende hellseherisches Bewußtsein hat, tritt ihm als Gegenbild das andere entgegen: die entsprechende Gesundungsstimmung und die Kräftigung, die aus der Stimmung herausquillt.",
      "Was über den Menschen, der krank war in der physischen Welt, dann als Ausgleich kommt in der geistigen Welt, das tritt dem Hellseher entgegen. Aus diesem kann er seine Ratschläge geben. Man braucht gar nicht einmal voll entwickelter Hellseher zu sein, sondern es kann das aus der Beobachtung des Krankheitsbildes instinktiv auftreten.",
      "Dasjenige aber, was in dem hellseherischen Bewußtsein das bewirkt, was als Ausgleich eben in der geistigen Welt wirklich kommt, das ist etwas, was zu dem Krank heitsbilde gehört, wie der Hinaufgang des Pendels auf der einen",
      "Seite zu dem Hinaufgang auf der andern Seite. Gerade aus diesem Bei­spiel sehen Sie, wie das Verhältnis des physischen Planes zur geistigen Welt ist, und wie fruchtbar für die Lebensführung auf dem physischen Plan das Wissen, das Erkennen der geistigen Welt sein kann.",
      "Gehen wir noch einmal zu dem zurück, was heute als ein konkreter Fall angeführt worden ist: daß, wie die Natur auf dem physischen Plan, so das Geistige, das weisheitsvoll Geistige uns umgibt in der geistigen Welt, das immer da ist. Nun, gerade wenn Sie dies in einer besonderen Weise noch verstehen, dann wird sich Ihnen auf die Vor­gänge der geistigen Welt ein Licht werfen, das außerordentlich wichtig ist.",
      "In der physischen Welt können wir so an den Dingen vorbeigehen, daß wir, indem wir die Dinge betrachten, sagen: Wie ist es mit dem Wesen dieses Dinges? Wie verhält es sich denn? Was ist das Gesetz dieses Wesens, dieses Vorgangs?",
      "Oder aber, wir gehen stumpf vorbei und fragen überhaupt nicht. Wir werden niemals auf dem physischen Plan etwas Vernünftiges lernen, wenn wir nicht so­zusagen von den Dingen veranlaßt werden, Erkennmisfragen zu stellen, wenn uns nicht die Dinge Rätsel aufgeben, so daß diese Rätsel in uns entstehen.",
      "Beim bloßen Anschauen der Dinge und Vorgänge werden wir auf dem physischen Plane niemals zu einer sich selbst führenden Seele kommen können. Auf dem geistigen Plan ist das wieder anders. Auf dem physischen Plan stellen wir die Fragen an die Dinge und Vorgänge, und wir müssen uns bemühen, die Dinge zu untersuchen, herauszubekommen, wie wir die Antwort auf die Frage, die wir uns stellen, aus den Dingen heraus bilden können.",
      "Wir müssen die Dinge untersuchen. Auf dem geistigen Plane ist es so, daß die Dinge und Wesenheiten um uns herum geistig sind; und die Dinge, die fragen uns, nicht wir fragen die Dinge. Die Dinge fragen uns, sie stehen da, die Vorgänge und Wesenheiten, und wir stehen ihnen gegenüber und werden fortwährend von ihnen gefragt.",
      "Wir müssen jetzt die Möglichkeit haben aus dem unendlichen Meer von Weisheit das herauszugreifen, was auf die Fragen antworten kann, die uns da gestellt werden. Wir müssen nicht aus den Dingen und Vorgängen heraus die Antworten suchen, sondern aus uns heraus, denn fragen tun uns die Dinge, überall um uns herum sind die fragenden Dinge.",
      "Dabei kommt noch das Folgende in Betracht: Nehmen wir an, wir stünden irgend einem Vorgang oder Wesen der geistigen Welt gegen­über, wir treten eigentlich ihm gar nicht anders gegenüber, als daß es an uns eine Frage stellt. Nehmen wir an, es stellt die Frage.",
      "Wir stehen da mit unserer Weisheit. Aber wir finden nicht die Möglichkeit, ein solches Wollen, fühlendes Wollen, wollendes Fühlen zu entwickeln, daß wir aus dieser Weisheit heraus die Antwort geben können, trotzdem wir wissen: die Antworten sind in uns.",
      "Unser Inneres ist von unendlicher Tiefe, alle Antworten sind in uns, aber wir finden nicht die Möglich­keit, wirklich die Antwort zu geben. Und die Folge davon ist, daß wir im Zeitenstrome vorbeisausen und die Möglichkeit, den rechten Zeitpunkt nämlich, versäumen, die Antwort zu geben, weil wir uns nicht die Fähigkeit erworben haben, vielleicht durch unsere vorher­gehende Entwicklung, die Reife zu haben, auf diese Frage schon in dem Zeitpunkt zu antworten.",
      "Wir haben uns in bezug auf das, was wir antworten sollten, zu langsam entwickelt: wir könnten erst später antworten. Aber die Gelegenheit kommt nicht wieder, wir haben sie versäumt. Wir haben nicht alle Gelegenheiten ausgenützt.",
      "So gehen wir vorbei an Dingen und Vorgängen, ohne ihnen Antwort zu geben. Solche Erlebnisse machen wir fortwährend in der geistigen Welt. Es kommt also vor, daß wir in dem Leben zwischen Tod und einer neuen Geburt vor einem Wesen stehen, das uns fragt.",
      "Wir haben es nicht dahin gebracht durch unsere Erdenleben und die dazwischenliegenden geistigen Leben, jetzt, wo es uns fragt, Antwort zu geben. Wir müssen vorbei, müssen in die nächste Inkarnation hinein.",
      "Die Folge davon ist, daß wir erst wiederum durch die guten Götter, ohne unser Bewußt­sein, in der nächsten Erdenverkörperung die Impulse bekommen müssen, damit wir beim nächsten Male nicht wieder an derselben Frage vorbeigehen. So sind die Zusammenhänge.",
      "Ich habe öfter erwähnt, daß, je weiter wir zurückgehen in der Menschheitsentwickelung, wir um so mehr gewahr werden, wie die Menschen die gegenwärtige Geistesverfassung nicht gehabt haben, sondern auf dem physischen Plan eine Art Hellsehen hatten. Aus einem dumpfen, traumhaften Hellsehen hat sich unser gegenwärtiges An­schauen der Dinge heraus entwickelt. Und je mehr wir Menschen",
      "finden, die noch auf primitiven Elementarstufen der Seelenentwick­lung stehen, desto verwandter finden wir noch ihr Denken und Fühlen mit dem ursprünglichen Hellsehen. Obzwar wirkliches Helisehen, ich meine primitives, atavistisches Hellsehen, immer seltener wird, so findet man doch, wenn man hinausgeht in elementare ländliche Zu­stände, immerhin Menschen, die sich etwas bewahrt haben aus früheren Zeiten, so daß man Anklänge an die Zeiten des früheren Hellsehens findet.",
      "Dieses Hellsehen zeigt uns, wenn auch eben in der dumpfen traumhaften Form, weil es ja ein Schauen in die geistigen Welten hinein ist, Eigentümlichkeiten, die uns wieder entgegentreten beim entwickelten Heilsehen, nur daß es eben da nicht dumpf, traum­haft, sondern klar und deutlich uns entgegentritt. Geisteswissenschaft zeigt uns, daß der Mensch, wie er jetzt in dem gegenwärtigen Zeiten-zyklus ist, wenn er durch das Leben zwischen dem Tod und einer neuen Geburt geht, immerfort und immer mehr und mehr vor den fragenden Wesenheiten zur rechten Zeit Antwort geben muß.",
      "Denn davon, ob er Antwort geben kann, hängt seine richtige Fortentwick­lung ab, seine Annäherung an das Ideal der Götter von dem voll­kommenen Menschen. Wie gesagt, ins Traumhafte umgesetzt hatten das früher die Menschen, und es ist ein Überrest davon geblieben in zahlreichen märchenartigen, sagenartigen Motiven.",
      "Sie werden immer weniger im Volk. Aber diese märchenartigen, sagenartigen Motive, die erzählen uns dann etwa: Der oder jener begegnet einem geistigen Wesen, das stellt immer wieder und wieder Fragen an ihn, und er steht ihm gegenüber, muß antworten.",
      "Aber er hat das Bewußtsein: bis zu einem gewissen Glockenschlage oder sonst etwas muß er antworten. Dieses, was man das Fragemotiv der Märchen und Sagen nennen könnte, ist sehr verbreitet. Das ist in dem früheren traumhaften Hell-sehen dasselbe gewesen, was nun wiederum in der geistigen Welt auftritt in der Form, wie ich es geschildert habe.",
      "Überhaupt kann dasjenige, was die geistige Welt charakterisiert, in allen Fällen ein wunderbarer Leitfaden sein, um Mythen, Sagen, Märchen und so weiter in der richtigen Weise zu verstehen und sie an ihren Ort hin-zustellen, wohin sie gehören. Das ist gerade ein Punkt, wo man sieht wie überall, auch in der Geisteskultur der Gegenwart, gewissermaßen",
      "die Entwickelung vor dem Tore der Geisteswissenschaft steht. Ganz interessant ist es, daß ein in vieler Beziehung in der Absicht schönes Buch wie das meines verstorbenen Freundes Ludwig Laistner, «Das Rätsel der Sphinx», deshalb ungenügend ist, weil, wenn es ge­nügend hätte werden sollen, es die Motive dieses Fragens, die Ludwig Laistner besonders ausführlich behandelt, aus einem geisteswissen­schaftlichen Wissen hätte behandeln müssen, weil also der Autor etwas hätte wissen müssen von dem Hineinspielen der geisteswissenschaft­lichen Wahrheit in die Sache.",
      "Wir sehen also, wenn wir uns gerade die charakteristischen aufge­zählten Fälle vor Augen stellen, daß es auf etwas ganz Bestimmtes ankommt in dem Verhalten in der geistigen Welt. Erkenntnisse zu sammeln in der geistigen Welt, wie hier auf dem physischen Plane, darauf kommt es nicht an.",
      "Es kommt darauf an, sogar diese Erkennt­nisse zu vermindern, nämlich die Erkenntniskraft umzuwandeln in Lebenskraft. Forscher kann man nicht sein in der geistigen Welt in dem Sinn, wie man es in der physischen Welt sein kann; das wäre dort sehr deplaciert Denn wissen kann man dort alles, es ist alles um einen herum.",
      "Das, worauf es ankommt, ist, daß man den Willen und die Empfindung gegenüber dem Wissen, gegenüber der Erkenntnis entwickeln kann, so daß man im Einzelfalle aus dem ganzen Schatze seines Woliens das gerade herausbringt, wodurch man die Weisheit anwenden kann, sonst erstickt oder ertrinkt man in der Weisheit. Also während es hier in der physischen Welt auf das Denken ankommt, kommt es dort in der geistigen Welt an auf das entsprechende Aus­bilden des Willens, des empfindenden Willens, des Willens, der aus der Weisheit heraus die Realität bereitet, formt, des Willens, der zur kreativen Kraft wird, zu einer Art schöpferischen Kraft.",
      "Den Geist haben wir dort, wie wir hier die Natur haben; aber den Geist zur Natur zu führen, das ist unsere Aufgabe. Ein schöner Satz ist erhalten aus der theosophischen Literatur der ersten Hälfte des 19.",
      "Jahr­hunderts von Ötinger, der in Murrhardt in Württemberg gelebt hat, und der in seiner eigenen spirituellen Entwicklung so weit war, daß er ganz bewußt in gewissen Zeiten geistigen Wesenheiten, also Seelen, die nicht auf dem physischen Plane sind, hat Helfer sein können.",
      "hat den merkwürdigen Satz geprägt, der sehr schön und sehr richtig ist: Natur und Naturgestalt ist das Ende der geistigen Schöpferkraft. -Das, was ich jetzt aus der geistigen Welt selber herausentwickelt habe, liegt in diesem Satz. Es strebt in der geistigen Welt die Schöpferkraft dahin, das, was in Weisheit zunächst wallt und wogt, hinauf zur Realität zu bringen. Wie man hier aus der physischen Realität die Weisheit herausbringt, macht man das dort umgekehrt. Aus der Weis­heit heraus hat man die Aufgabe, Realitäten zu schaffen, in Realitäten auszuleben das, was dort in Weisheit ist. Das Ende der Götterwege ist geformte Wirklichkeit.",
      "So sehen wir also, es kommt auf wiliensdurchtränktes Fühlen an, auf von Gefühl durchtränkten Willen, die sich umwandeln in kreative Kraft, schöpferische Kraft, die wir dort in der geistigen Welt so an-wenden müssen, wie wir uns hier auf der physischen Welt anstrengen müssen in unserem forschenden Denken, um in der physischen Welt zur Weisheit zu kommen.",
      "Nun handelt es sich darum, daß wir für diese Möglichkeit in der geistigen Welt das Fühlen und Denken richtig entwickeln, daß wir uns dafür schon hier auf dem physischen Plane in einer Weise, wie es für den gegenwärtigen Zeitenzyklus richtig ist, vorbereiten. Denn alles das, was in der geistigen Welt geschieht zwischen dem Tod und einer neuen Geburt, ist Folge desjenigen, was in der physischen Welt geschieht zwischen der Geburt und dem Tode. Zwar ist das, was in der geistigen Welt ist, wie wir gesehen haben, so anders, daß wir uns ganz neue Vorstellungen und Begriffe aneignen müssen, wenn wir die geistige Welt verstehen wollen. Aber dennoch: wie Ursache und Wirkung hängen die beiden gegenseitig zusammen. Nur dann ver­stehen wir die Zusammenhänge zwischen dem Geistigen und dem Physischen, wenn wir sie als Zusammenhänge von Ursache und Wir­kung wirklich erkennen. Vorbereiten müssen wir uns in der physischen Welt. Deshalb möchte ich jetzt die Frage ein wenig betrachten: Wie bereiten wir uns im gegenwärtigen Zeitenzyklus in der richtigen Weise auf dem physischen Plane vor, so daß wir genügend innere Impulse haben in der geistigen Welt, sei es, daß wir durch Initiation, sei es, daß wir durch die Pforte des Todes hineinkommen, um wirklich die",
      "geistige Schlagkraft zu haben, aus der gegebenen Weisheit das heraus­zuholen, was wir brauchen, um Realitäten herauszuwandeln aus der strömenden, wogenden Weisheit? Woher kommt uns solche Kraft? Es kommt überall darauf an, daß wir solche Dinge für unseren Zeiten-zyklus beantworten. In den Zeiten, in denen die Menschen so dachten, daß die ersten ursprünglichsten Quellen der genannten Sagenmotive sich bildeten, da war es anders. Aber woher kommt uns solche Seelen-kraft im gegenwärtigen Zeitenzyklus?",
      "Um uns einer Antwort nähern zu können, möchte ich Folgendes heranziehen. Man kann sich in verschiedenen Philosophien umsehen und kann bei den Philosophen suchen nach der Art, wie sie zu dem Gottesbegriffe kommen.",
      "Es müssen dann selbstverständlich solche Philosophen sein, die geistige Tiefe genug haben, um sich eben von der Welt überzeugen zu lassen, daß man von einem Göttlichen, das die Welt durchdringt, sprechen kann. Im neunzehnten Jahrhundert braucht nur Lotze genommen zu werden, der in seiner Religions­philosophie etwas zu schaffen suchte, was im Einklang steht mit seiner übrigen Philosophie.",
      "Aber es könnten auch andere Philosophen ge­nommen werden, die eben wirklich tief genug waren, um sozusagen auch eine Religionsphilosophie zu haben. Eine Eigentümlichkeit wird man bei allen diesen Philosophen finden, eine ganz bestimmte Eigen­tümlichkeit.",
      "Ja, zu dem Göttlichen dringen diese Philosophen mit ihren Erwägungen aus dem physischen Plane denkend vor; sie denken nach, forschen auf philosophische Art, kommen darauf, wie es gerade bei Lotze der Fall ist, daß die Erscheinungen und Wesen der Welt zusammengehalten werden von einem göttlichen Grund, der alles durchwebt und alles in eine gewisse Harmonie bringt. Wenn man aber näher auf solche Religionsphilosophien eingeht, so haben sie immer eine Eigentümlichkeit.",
      "Man kommt eben zu einem göttlichen Wesen, das alles durchtränkt und durchzieht, und wenn man dieses göttliche Wesen sich näher ansieht, diesen Gott der Philosophen, so kommt man darauf, daß es ungefähr der Gott ist, den die hebräische oder namentlich die christliche Religion den Vatergott nennt, Gott-Vater. Dazu kann die Philosophie kommen.",
      "Sie kann die Natur be­trachten und tief genug sein, um nicht in hohiköpfiger materialistischer",
      "Weise alles Göttliche abzuleugnen, sie kann zu dem Göttlichen kom­men, kommt aber dann zu dem Vatergott. Man kann ganz genau, wenn man die Philosophen verfolgt, zeigen, daß zu etwas anderem die bloße Philosophie als denkende Philosophie überhaupt nicht führen kann, als zu einem monotheistischen Vatergott. Wenn bei einzelnen Philosophen, bei Hegel zum Beispiel und anderen, der Christus auftritt, so ist er nicht aus der Philosophie heraus - das läßt sich nachweisen - er ist aus der positiven Religion herübergenommen. Die Leute haben gewußt, daß die positive Religion den Christus hat, dann konn­ten sie ihn besprechen. Der Unterschied ist der, daß man den Vatergott in der Philosophie finden kann; Christus kann man mit keiner Philosophie durch denkende Betrachtung finden. Das ist ganz un­möglich.",
      "Das ist ein Satz, von dem ich Ihnen raten möchte, ihn wohl zu erwägen und viel darüber nachzudenken. Wenn man ihn richtig ver­steht, führt er in sehr bedeutsame Tiefen menschlichen Forschens und Seelenstrebens hinein. Aber er hängt allerdings zusammen mit etwas, was in der christlichen Religion sogar sehr schön symbolisch, bildhaft, zum Ausdruck gebracht ist: nämlich damit, daß man das Verhältnis dieses anderen Gottes, des Christus, zu dem Vatergott als das Ver­hältnis des Sohnes zum Vater auffaßt. Das ist sehr bedeutsam, obwohl es nur ein Symbol ist. Es ist interessant, daß damit zum Beispiel Lotze gar nichts anfangen kann. Daß man dieses Symbol nicht wörtlich nehmen kann, ist selbstverständlich, sagt Lotze, denn es kann nicht der eine Gott der Sohn des anderen Gottes sein, meint er. Nun, es ist aber doch etwas sehr Bezeichnendes in diesem Symbolum. Zwischen dem Vater und dem Sohn ist so etwas wie das Verhältnis von Ursache und Wirkung. Denn in gewisser Weise kann man im Vater die Ur­sache des Sohnes suchen. Der Sohn wäre nicht da, wenn der Vater nicht da wäre. Aber ein Eigentümliches muß man beachten: daß nämlich derjenige Mensch, der einen Sohn eventuell haben kann, durchaus auch die Möglichkeit hat, keinen zu haben, er kann sohnlos sein. Er würde dann derselbe Mensch sein. Die Ursache ist der Mensch A, die Wirkung ist der Mensch B, der Sohn. Aber die Wirkung braucht nicht einzutreten, die Wirkung ist eine freie Tat, die Wirkung",
      "folgt aus der Ursache als eine freie Tat. Deshalb muß man, wenn man eine Ursache studiert und sie mit ihrer Wirkung im Zusammenhang faßt, nicht bloß fragen nach dem Wesen der Ursache, denn damit hat man noch gar nichts getan, sondern danach muß man fragen, ob die Ursache auch wirklich verursacht, und darauf kommt es an.",
      "Nun hat alle Philosophie das Eigentümliche, daß sie am Gedankenfaden fort­geht, ein Glied aus dem andern entwickelt, also gleichsam in dem Vorderen schon das Nachfolgende sucht. So haben sie recht als Philosophien.",
      "Aber man kommt dabei niemals auf dasjenige Verhält­nis, welches sich ergibt, wenn man berücksichtigt, daß die Ursache gar nicht zu verursachen braucht. Die Ursache kann ihrem Wesen nach, in ihrem Wesen dasselbe sein, ob sie als Ursache etwas verursacht oder nicht.",
      "Das ändert nichts in dem Wesen der Ursache. Und dieses Bedeutungsvolle ist uns hingestellt in dem Symbolum von Gott-Vater und Gott-Sohn: daß der Christus hinzukommt als eine freie Schöpfung zu dem Vatergott, als eine Schöpfung, die nicht unmittelbar aus ihm folgt, sondern die sich als freie Tat neben die vorhergehende Schöp­fnng hinstellt.",
      "Die auch die Möglichkeit hätte, nicht zu sein: die der Welt also nicht deshalb gegeben ist, weil der Vater den Sohn der Welt geben mußte, sondern der Sohn ist der Welt gegeben als eine freie Tat, durch Gnade, durch Freiheit, durch Liebe, die sich frei gibt in ihrer Schöpfung. Deshalb kann man niemals durch dieselbe Art von Wahrheit, durch die man zu dem Vatergott kommt wie die Philosophen, auch zum Sohnesgott, zu dem Christus kommen.",
      "Um zum Christus zu kommen, ist notwendig, daß man zu der philo­sophischen Wahrheit die Glaubenswahrheit hinzufügt, oder - weil die Zeit des Glaubens immer mehr und mehr abnimmt - die andere Wahrheit hinzunimmt, die durch hellseherische Forschung kommt, die sich als eine freie Tat ebenfalls erst in der menschlichen Seele entwickeln muß.",
      "Daher muß man sagen: So wie man aus der Anordnung der Natur­vorgänge beweist, daß es einen Gott überhaupt gibt, so kann man niemals äußerlich an der Kette von Ursachen und Wirkungen bewei­sen, daß es einen Christus gibt. Der Christus ist dagewesen und kann an den Menschenseelen vorbeigehen, wenn sie nicht aus sich selber",
      "heraus die Kraft empfinden, zu sagen: Ja, das ist der Christus. Es gehört ein aktives Sich-Aufraffen zum Wahrheitsimpuls dazu, um in dem, der da war als der Christus, den Christus zu erkennen. Zu den anderen Wahrheiten, die im Bereich des Vatergottes liegen, können wir gezwungen werden, wenn wir uns überhaupt nur in das Denken begeben und es konsequent anwenden, denn Materialist sein, heißt zu gleicher Zeit unlogisch sein.",
      "Religionsphilosophie im Sinne Lotzes, und wie überhaupt Religionsphilosophie sein kann, entsteht so, daß wir durch das Denken zu diesem Göttlichen der Religionsphilosophie gezwungen werden können. Niemals aber können wir in der gleichen Art durch bloße Philosophie dahin gebracht werden, den Christus anzuerkennen.",
      "Das muß unsere freie Tat sein. Da ist dann nur zweierlei möglich: entweder man zieht die letzte Konsequenz des Glaubens, oder man macht den Anfang mit der Erforschung der geistigen Welt mit Geisteswissenschaft.",
      "Die letzte Konsequenz des Glaubens zieht man, wenn man sagt, wie der russische Philosoph Solowjew: Ja, in bezug auf all die philosophischen Wahrheiten, die der Mensch über die Welt gewinnt, so daß er sich durch seine Logik zwingen läßt, steht der Mensch in keiner freien Wahrheit. Das ist eben gerade die höhere Wahrheit, die uns nicht zwingt, die unsere freie Tat ist: die höchste Glaubenswahrheit.",
      "Darin vollendet sich die höchste Würde für Solow­jew, daß er sagt: Die höhere Wahrheit, die den Christus anerkennt, das ist die Wahrheit, die als freie Tat schafft, die sich nicht zwingen läßt. -Für den Geistesforscher und für den, der die Geisteswissenschaft ver­steht, entsteht wiederum das Wissen. Aber das ist ein aktives Wissen, das sich vom Denken zur Imagination, Inspiration, Intuition erhebt, das innerlich schöpferisch wird, das im Schaffen sich einlebt in die geistigen Welten und dadurch dem, was wir entwickeln müssen, ähnlich wird, sei es, daß wir durch Initiation oder durch den Tod in die geistige Welt hineinkommen.",
      "Die Weisheit, die sich uns auf Erden aufzwingt, die haben wir in der geistigen Welt in Hülle und Fülle, wie wir hier auf dem physischen Plane die Naturerscheinungen haben. Das, worauf es in der geistigen Welt ankommt, ist, daß wir den Impuls, die Kraft haben, aus dieser Weisheit heraus etwas zu machen, durch sie Realität zu schaffen.",
      "Freies Schaffen aus der Weisheit heraus, geistiges Wirken als Tat, das ist es, was m uns als Impuls leben muß. Das können wir nur haben, wenn wir das richtige Verhältnis zu dem Christus finden. Der Christus ist diejenige Wesenheit, die sich nicht durch die äußere Logik des Verstandes, der an das Gehirn gebunden ist, beweisen läßt, die sich aber erweist, die sich realisiert in uns, indem wir uns geistiges Wissen erwerben.",
      "So wie als freie Tat Geisteswissenschaft sich hinzugesellt zu der anderen Wissenschaft, so kommt hinzu das Wissen um den Chri­stus, sobald wir uns derjenigen Welt nähern, in die wir durch die Geistesforschung hineinkommen, oder die wir betreten, indem wir durch die Pforte des Todes gehen. Im Augenblicke, wo wir im gegen­wärtigen Zeitenzyklus in einer segensvollen Weise in die geistige Welt hineinkommen wollen, das heißt, wo wir der physischen Welt absterben wollen, brauchen wir ein solches Verhältnis zur Welt, wie wir es gewinnen, wenn wir uns in der richtigen Weise zum Christus verhalten.",
      "Einen Gott, der sozusagen ist, wie der Vatergott der christlichen Religion, ihn können wir gewinnen durch die Betrachtung der Natur, ihn können wir gewinnen durch die Betrachtung, die sich uns ergibt, indem wir im physischen Leibe leben. Den Christus recht zu verstehen ohne die Tradition, ohne die Überlieferung, rein aus der Erkenntnis selber heraus, ist nur möglich durch die Geisteswissen­schaft.",
      "Sie führt in die Gebiete hinein, die der Mensch durch das Sterben betritt, sei es jenes Sterben, das eine symbolisches Sterben ist, das Herausgehen aus dem physischen Leibe, um in der Seele sich außerhalb des Leibes zu wissen, sei es das andere Sterben, durch die Pforte des Todes hindurch. Richtig statten wir uns aus mit den Im­pulsen, die wir brauchen, indem wir durch die Pforte des Todes gehen, wenn wir das rechte Verhältnis zum Christus finden.",
      "In dem Augenblick, wo es ans Verlassen des physischen Leibes geht, sei es, indem wir in die geisteswissenschaftliche Entwicklung eintreten, sei es, daß wir wirklich durch die Pforte des Todes gehen, in dem Augen­blick, wo es ans Sterben, ans Verlassen des physischen Leibes geht, kommt es darauf an, daß wir im gegenwärtigen Zeitenzyklus in der rechten Art derjenigen Wesenheit gegenüberstehen, die in die Welt gekommen ist, damit wir das Verhältnis zu ihr finden. Den Vatergott",
      "können wir als Lebende finden. Den Christus finden wir, wenn wir das Hineingehen in den Geist, wenn wir das Sterben in der richtigen Weise verstehen. In Christus sterben wir.",
      "In Christo morimur."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Bei dem zweiten hier gehaltenen öffentlichen Vortrage habe ich in großen Zügen zu schildern versucht, soweit das eben bei einem öffentlichen Vortrage möglich ist, das Leben, wie es für den Menschen zwischen dem Tod und einer neuen Geburt verfließt.",
        "Das, was uns da entgegengetreten ist, soll uns in den beiden nächsten Vorträgen in einer vertiefteren Art noch beschäftigen, vertieft namentlich da­durch, daß es uns so erscheinen soll, daß es das Leben auch hier in der physischen Welt immer mehr und mehr erklärt.",
        "Um aber zu einer solchen Vertiefung der Darstellung zu kommen, bedarf es der Vor­bereitung, die in den drei vorhergehenden Vorträgen gegeben wurde und in dem heutigen wiederum gegeben werden soll.",
        "Gerade diese Vorträge sollen uns die Mittel liefern, das öffentlich Vorgetragene weiter zu vertiefen."
      ],
      [
        "Es ist von mir da oder dort unseren Freunden öfter gesagt worden, daß der Mensch, wenn er die geistigen Welten kennen lernen und ver­stehen lernen will - und in den geistigen Welten leben wir ja zwischen dem Tod und einer neuen Geburt - in vieler Beziehung sich Begriffe und Vorstellungen aneignen muß, die man gar nicht aus den Erleb­nissen und Erfahrungen des physischen Planes heraus haben kann, die aber, wenn sie sich die Menschheit immer mehr und mehr aneignen wird, von unendlicher Wichtigkeit, von einer immer größer werdenden Wichtigkeit sein werden gerade auch für das Leben auf dem physischen Plan.",
        "Zunächst wollen wir uns heute einmal einen Unterschied des Erlebens in der geistigen Welt und des Erlebens auf dem physischen Plane klar machen, welcher im Grunde genommen wenn er uns zum erstenmale vor die Seele tritt, im höchsten Maße frappieren und sonderbar erscheinen muß, so daß es sehr leicht sein kann, daß wir den Glauben haben, wir könnten solche Dinge nur schwer verstehen.",
        "Je mehr wir uns aber in die Geisteswissenschaft einleben, desto mehr werden wir sehen, daß uns solche Dinge immer verständlicher und verständlicher werden."
      ],
      [
        "Wenn wir durch den physischen Plan gehen, wenn wir die Erleb­nisse des physischen Planes auf uns wirken lassen, so muß uns ja, wenn wir darüber nachdenken, eines ganz besonders auffallen.",
        "Das ist, daß wir auf diesem physischen Plane dasjenige vor uns haben, was wir die Realität nennen, was wir das Dasein, das Sein, die Wirk­lichkeit nennen."
      ],
      [
        "Man möchte sagen: Je ungeistiger ein Mensch ist, desto mehr baut er auf das, was er auf dem physischen Plan als die sich aufdrängende Realität vor sich hat.",
        "Anders steht es mit dem, was wir uns aneignen wollen auf dem physischen Plane als unser Wissen, unsere Erkenntnis von der Wirklichkeit."
      ],
      [
        "Wir müssen zunächst als Kinder überhaupt erst dazu erzogen werden, Fähigkeiten zu ent­wickeln, um uns ein Wissen, eine Erkenntnis von dem physischen Plane anzueignen, und wir müssen dann immer weiter und weiter arbeiten.",
        "Das Erwerben von Erkenntnissen setzt geistige Arbeit voraus."
      ],
      [
        "Die Natur, das heißt die äußere Wirklichkeit, gibt nicht von selber her, was in ihr als Weisheit steckt, was in ihr als ihre Gesetz­mäßigkeit steckt.",
        "Wir müssen uns die Kenntnis dieser Weisheit, dieser Gesetzmäßigkeit aneignen."
      ],
      [
        "Und darin besteht ja alles menschliche Wissensstreben, aktiv sich anzueignen aus den passiv empfangenen Erlebnissen und Erfahrungen dasjenige, was als Weisheit, als Gesetz­mäßigkeit in den Dingen steckt.",
        "Ganz anders sind nun die Dinge, wenn man sich entweder durch die zur Geistesforschung führenden Übungen oder durch den Durchgang durch die Pforte des Todes in die geistige Welt hineinbegibt."
      ],
      [
        "Es ist allerdings das Verhältnis des Menschen zur geistigen Umwelt nicht unter allen Umständen so, wie ich es jetzt schildern werde; aber in wichtigen Momenten, bei wichti­gen Erlebnissen ist es so.",
        "Es ist ja auch bei unserem Leben auf dem physischen Plan so, daß wir nicht immer uns abarbeiten nach Er­kenntnissen, sondern wir setzen auch in diesem Arbeiten aus."
      ],
      [
        "So ist auch das, was ich jetzt schildern werde, nicht eine fortwährende Nötigung in der geistigen Welt, sondern es ist zuzeiten in der geistigen Welt für uns erforderlich."
      ],
      [
        "Das nämlich ist das Überraschende, daß es dem Menschen in der geistigen Welt nicht an Weisheit fehlt.",
        "Man kann ein Tor sein in der Sinneswelt, und die Weisheit strömt einem in der geistigen Welt nur"
      ],
      [
        "so zu in ihrer Realität, wenn man einfach in diese geistige Welt hineinversetzt wird.",
        "Weisheit, dasjenige, was wir uns in der physischen Welt mit Mühe aneignen, was wir uns erarbeiten müssen von Tag zu Tag, wenn wir es haben wollen, das haben wir in der geistigen Welt so, wie wir in der physischen Welt um uns herum die Natur haben.",
        "Es ist immer da und es ist in reichlichstem Maße da.",
        "Gewissermaßen können wir sagen: Je weniger Weisheit wir uns auf dem physischen Plan angeeignet haben, desto reichlicher strömt uns diese Weisheit auf dem geistigen Plane zu.",
        "Aber nun haben wir gegenüber dieser Weisheit auf dem geistigen Plane eine bestimmte Aufgabe."
      ],
      [
        "Ich habe Ihnen in den letzten Tagen davon gesprochen, daß man auf dem geistigen Plane das Menschheitsideal, den Inhalt der Götter-religion vor sich hat, daß man sich dahin durcharbeiten muß.",
        "Das kann man nicht, wenn man nicht in die Lage kommt auf dem geistigen Plan, sein Wollen dort, also jetzt das Wollen, das fühlende Wollen, das wollende Fühlen, Wollen und Fühlen so anzuwenden, daß man die Weisheit, die einem immer fort und fort zuströmt, die da ist wie die Erscheinungen der Natur in der physischen Welt, fortwährend vermindert, daß man fortwährend von ihr etwas wegnimmt."
      ],
      [
        "Man muß diese Fähigkeit haben, von der Weisheit, die dort einem entgegen-tritt, immer mehr und mehr wegzunehmen.",
        "Hier auf dem physischen Plan müssen wir immer weiser und weiser werden, dort müssen wir uns bemühen, unser Wollen, unser Fühlen so anzuwenden, daß wir von der Weisheit immer mehr und mehr wegnehmen, sie verdunkeln."
      ],
      [
        "Denn je weniger wir dort von der Weisheit wegnehmen können, desto weniger finden wir die Kräfte, um uns so mit diesen Kräften zu durchsetzen, daß wir uns als reale Wesen dem Menschheitsideale annähern.",
        "Dieses Annähern muß darin bestehen, daß wir immer mehr und mehr von der Weisheit wegnehmen."
      ],
      [
        "Was wir da wegnehmen, das können wir umwandeln in uns selber, so daß die umgewandelte Weisheit die Lebenskräfte sind, die uns zu dem Menschheitsideale hintreiben.",
        "Diese Lebenskräfte müssen wir uns in dieser Zeit zwischen dem Tod und einer neuen Geburt erwerben."
      ],
      [
        "Nur dadurch kommen wir in einer regelrechten Weise der neuen Verkörperung entgegen, daß wir die Weisheit, die uns reichlich zufließt, in Lebenskräfte umwandeln."
      ],
      [
        "Und wir müssen, wenn wir wieder auf der Erde ankommen, so viel Weisheit in Lebenskräfte umgewandelt haben, müssen soviel von Weisheit vermindert haben, daß wir genug Lebenskräfte haben, um die Vererbungssubstanz, die wir von Vater und Mutter bekommen, mit ge­nügend organisierenden geistigen Lebenskräften zu durchdringen.",
        "Wir müssen also von der Weisheit immer mehr und mehr wegnehmen."
      ],
      [
        "Wenn man einen rechten Materialisten, der dem Geiste gar keine Realität zuerkennt auf dem physischen Plane, nach dem Tode wieder auffindet, einen solchen Materialisten, der während seines Lebens gesagt hat: Das ist ja alles Torheit, was ihr da über den Geist sprecht.",
        "Eure Weisheit ist die reinste Phantasterei, die weise ich ganz von mir, ich lasse gar nichts anderes gelten als die Beschreibung dessen, was äußere Natur ist. - Bei einem solchen Menschen, wenn er nach dem Tode getroffen wird, sieht man so reichlich Weisheit zuströmen, daß er sich gar nicht retten kann."
      ],
      [
        "Von überallher strömt ihm der Geist zu.",
        "In demselben Maße, als er hier nicht geglaubt hat an den Geist, in demselben Maße ist er dort überall von Geist umflutet.",
        "Jetzt tritt an ihn die Aufgabe heran, diese Weisheit in Lebenskräfte umzuwan­deln, so daß er eine physische Realität schaffen kann in der nächsten Inkarnation."
      ],
      [
        "Er soll das, was er Realltät genannt hat, heraus erzeugen aus dieser Weisheit, er soll diese Weisheit vermindern.",
        "Sie will sich aber von ihm nicht vermindern lassen, sie bleibt wie sie ist.",
        "Er be­kommt es nicht fertig, Realität daraus zu machen."
      ],
      [
        "Die ungeheure Strafe des Geistes steht vor ihm, daß er, während er hier auf dem physischen Plan nur auf Realität gebaut hat in seinem letzten Leben, während er den Geist ganz geleugnet hat, er sich sozusagen vor dem Geist nicht retten kann, und er nichts von diesem Geiste realisieren kann.",
        "Er steht immer vor der Gefahr, daß er gar nicht in die physische Welt wiederum hereinkommen kann durch Kräfte, die er selbst erzeugt."
      ],
      [
        "Er lebt fortwährend in der Furcht: Der Geist wird mich hereindrängen in die physische Welt, und ich werde dann ein physi­sches Dasein haben, das alles das verleugnet, was ich im vorher­gehenden Leben als das Richtige anerkannt habe.",
        "Ich werde mich hereinstoßen lassen müssen von dem Geist in die physische Realität, ich werde es nicht selbst zu einer Realität bringen."
      ],
      [
        "Das ist allerdings etwas Frappierendes, aber die Sache ist so.",
        "Um sozusagen in dem Geiste zu ersticken nach dem Tode und keine Realität, wie man sie allein verehrt hat vor dem Tode, in ihm zu finden, dazu ist der Weg der, vor dem Tode ein rechter Materialist zu sein und den Geist abzuleugnen.",
        "Dann erstickt man oder ertrinkt man im Geiste."
      ],
      [
        "Das sind allerdings Vorstellungen, die wir uns im Laufe unseres Betriebes der geistigen Wissenschaft immer mehr und mehr aneignen müssen.",
        "Denn wenn wir uns solche Vorstellungen aneignen, führen sie uns auch im physischen Leben in einer harmonischen Weise weiter und zeigen uns gewissermaßen, wie die beiden Seiten des Lebens einander ergänzen und ausgleichen müssen.",
        "Wir begründen in uns den Instinkt, in unserer Lebensführung diesen Ausgleich wirklich herbeizuführen."
      ],
      [
        "Noch einen anderen Fall möchte ich vom Zusammenhang des physischen Lebens mit dem geistigen Leben anführen.",
        "Nehmen wir jetzt einmal einen ganz konkreten, einzelnen Fall.",
        "Nehmen wir an, wir haben auf dem physischen Plane jemand angelogen.",
        "Nicht wahr, ich rede also von einzelnen Fällen.",
        "Wenn wir jemanden angelogen haben, so fällt das in einen bestimmten Zeitpunkt.",
        "Das, was ich jetzt als Entsprechendes in der geistigen Welt schildern werde, fällt wie­derum in einen bestimmten Zeitpunkt zwischen dem Tod und einer neuen Geburt.",
        "Nehmen wir also an, wir hätten jemanden zu einer gewissen Zeit auf dem physischen Plan angelogen, dann kommt bei unserem Aufenthalt in der geistigen Welt, sei es, daß wir durch Initiation hineinkommen oder durch den Tod, ein Zeitpunkt, wo wir mit unserer Seele in der geistigen Welt ganz, ganz erfüllt sind von der Wahrheit, die wir hätten sagen sollen.",
        "Aber diese Wahrheit, die quält uns, diese Wahrheit steht vor uns, in demselben Maße uns quälend, als wir von ihr abgeirrt waren bei der Lüge.",
        "Man braucht also nur zu lügen auf dem physischen Plan, um einen Zeitpunkt herbeizuführen in der geistigen Welt, in dem wir durch die ent­sprechende Wahrheit, die der Lüge entgegengesetzt ist, gequält wer­den dadurch, daß diese Wahrheit in uns lebt und uns brennt und wir sie nicht ertragen können.",
        "Unser Leiden besteht namentlich darin, daß"
      ],
      [
        "wir einsehen: das ist die Wahrheit.",
        "Wir sind aber so, daß uns diese Wahrheit keinen Genuß, keine Freude, keine Lust bereitet, sondern uns quält.",
        "Von den guten Sachen gequält zu werden, von dem, wovon man weiß, daß es einen erheben sollte, gequält zu werden, das gehört zu den Eigentümlichkeiten der Erlebnisse in der geistigen Welt."
      ],
      [
        "Man braucht zum Beispiel im Leben nur einmal bei einer Sache, gegenüber welcher Fleiß uns Pflicht gewesen wäre, faul gewesen zu sein, dann kommt eine Zeit in der geistigen Welt, wo der Fleiß, der uns dazumal gefehlt hat, in uns lebt.",
        "Er ist da, der Fleiß, er kommt ganz sicher, er lebt in uns, wenn wir einmal so recht faul gewesen sind auf dem physischen Plan.",
        "Es kommt dann eine Zeit, wo wir durch die inneren Notwendigkeiten diesen Fleiß unbedingt in uns anwenden müssen.",
        "Wir geben uns ganz diesem Fleiß hin, und wir wissen, er ist etwas ungeheuer Wertvolles, aber er quält uns, wir leiden unter ihm."
      ],
      [
        "Oder nehmen wir einen Fall, welcher vielleicht weniger in der menschlichen Willkür liegt, welcher in anderen Vorgängen des Lebens liegt, die mehr, ich möchte sagen, in den Untergründen des Daseins vor sich gehen und mit dem Verlauf unseres Karmas zusammen­hängen; nehmen wir den Fall, wir seien durch eine Krankheit durch­gegangen im physischen Leben.",
        "Wenn wir im physischen Leben durch eine Krankheit durchgegangen sind, die uns Schmerzen oder der­gleichen bereitet hat, so erleben wir zu irgend einem Zeitpunkt in der geistigen Welt die entgegengesetzte Stimmung, die entgegengesetzte"
      ],
      [
        "Verfassung: die der Gesundheit, des Gesundseins.",
        "In demselben Maße, in dem uns die Krankheit geschwächt hat, stärkt uns diese Stimmung des Gesundseins bei unserem Aufenthalt in der geistigen Welt.",
        "Das ist ein Fall, der vielleicht nicht nur wie die anderen Dinge, die vorgebracht worden sind, unsern Verstand schockiert, sondern der viel tiefer in das Empfindungsgemäße unserer Seele eindringt, diese Seele irritiert.",
        "Wir wissen ja, daß geisteswissenschaftliche Dinge immer mit der Empfindung aufgefaßt werden müssen.",
        "Aber wir müssen bei diesem Fall das Folgende bedenken: Wir müssen uns klar machen, daß ja hier gleichsam etwas wie ein Schatten ist über dem Zusammen­hang zwischen der physischen Krankheit und der uns stärkenden Gesundheit in der geistigen Welt.",
        "Wahr ist der Zusammenhang, aber"
      ],
      [
        "es gibt etwas in der Menschenbrust, was dem Gefühle nach mit diesem Zusammenhang nicht recht einverstanden sein kann.",
        "Das muß durch­aus zugegeben werden.",
        "Dafür aber hat dieser Zusammenhang noch eine andere Wirkung, wenn er wirklich von uns erfaßt wird.",
        "Und diese Wirkung kann in der folgenden Weise charakterisiert werden."
      ],
      [
        "Nehmen wir einmal an, ein Mensch durchdringt sich mit Geistes­wissenschaft, ein Mensch gibt sich ernstlich Mühe, Geisteswissen­schaft wirklich in sich aufzunehmen, nicht so, wie man eine andere Wissenschaft aufnimmt.",
        "Die kann man theoretisch studieren, in bloßen Gedanken, Begriffen kann man sich aneignen, was sie gibt."
      ],
      [
        "Geisteswissenschaft soll man niemals nur so aufnehmen.",
        "Sie soll wie ein geistiges Lebensblut in uns werden.",
        "Geisteswissenschaft soll in uns weben und leben, sie soll eigentlich in allen Begriffen, die sie uns gibt, in uns auch Empfindungen, Gefühle wachrufen."
      ],
      [
        "Es gibt eigent­lich für einen, der Geisteswissenschaft wirklich mit rechtem Ohr anhört, nichts in dieser Geisteswissenschaft, was uns nicht entweder auf der einen Seite erhebt oder auf der andern Seite in die Abgründe des Daseins schauen läßt, um uns gerade auch in diesen Abgründen zurechtfinden zu lassen.",
        "Man kann sagen: Wer Geisteswissenschaft richtig versteht, verfolgt das, was sie sagt, überallhin auch mit diesen und jenen Gefühlen."
      ],
      [
        "Wer Geisteswissenschaft in sich aufnimmt, der wird einfach dadurch, daß die geisteswissenschaftlichen Begriffe in ihm leben, daß er sich diejenigen Vorstellungs-Gewohnheiten an­eignet, die jetzt gerade angedeutet worden sind als notwendig gegen­über der Geisteswissenschaft, wirklich seine Seele schon in der physischen Welt umwandeln.",
        "Ich habe ja öfter darauf aufmerksam gemacht, wie zu den besten, eindringlichsten Übungen das Studium, das ernstliche Studium der Geisteswissenschaft selbst gehört."
      ],
      [
        "Nun stellt sich allmählich bei dem Menschen, der also in die Geisteswissenschaft eindringt, etwas Eigentümliches heraus.",
        "Ein sol­cher Mensch, der vielleicht Übungen macht, vielleicht nicht einmal Übungen macht, um selbst Geistesforscher zu werden, sondern der sich nur ernstlich bemüht, Geisteswissenschaft zu verstehen, ein solcher wird vielleicht lange, lange nicht daran denken können, selber etwas hellseherisch zu schauen.",
        "Er wird es einmal können, aber das"
      ],
      [
        "kann vielleicht noch ein fernes Ideal bei ihm sein.",
        "Aber wer Geistes­wissenschaft in dem angedeuteten Sinne wirklich auf seine Seele wirken läßt, der wird sehen, daß sich in seiner Seele die Instinkte des Lebens, die mehr unbewußten Triebfedern des Lebens ändern."
      ],
      [
        "Seine Seele wird wirklich anders.",
        "Man begibt sich nicht in den Betrieb der Geisteswissenschaft hinein, ohne daß diese Geisteswissenschaft die Seele instinktiv beeinflußt, sie anders macht, ihr andere Sympathien und Antipathien gibt, sie gleichsam mit einem Licht durchgießt, so daß sie sicherer fühlt als sie vorher gefühlt hat."
      ],
      [
        "Das kann man auf jedem Gebiete des Lebens bemerken; auf jedem Gebiete des Lebens äußert sich die Geisteswissenschaft in der geschilderten Weise.",
        "Man kann ein ungeschickter Mensch sein im Leben und wird Geistes-wissenschafter, und man wird sehen, daß, ohne daß man irgend etwas anderes getan hat, als sich mit dieser Geisteswissenschaft zu durch­dringen, man bis in die Handgriffe hinein geschickter wird."
      ],
      [
        "Sagen Sie nicht: Ich kenne sehr ungeschickte Geisteswissenschafter, die sind noch lange nicht geschickt geworden!",
        "Versuchen Sie nachzudenken darüber, inwiefern diese doch noch nicht so, wie es eben nach ihrem Karma nötig ist, sich wirklich innerlich durchdrungen haben mit der Geisteswissenschaft."
      ],
      [
        "Man kann ein Maler sein, bis zu einem gewissen Grade die Malkunst handhaben.",
        "Wird man Geisteswissenschafter, so wird man sehen, daß das, was jetzt eben angedeutet worden ist, in die instinktive Handhabung der Malkunst einfließt."
      ],
      [
        "Man mischt leichter die Farben, Ideen, die man haben will, kommen einem eher.",
        "Oder nehmen wir an, man sei Gelehrter, man solle irgendwie etwas Wissen­schaftliches arbeiten.",
        "Gar mancher, der in diesem Falle ist, wird wissen, was es oft für Mühe kostet, die Literatur zusammenzusuchen, um irgend eine Frage zu lösen."
      ],
      [
        "Wird man Geisteswissenschafter, so geht man nicht mehr wie früher in die Bibliotheken und läßt sich erst fünfzig Bücher geben, die nichts nutzen, sondern man greift unmittel­bar an das Richtige.",
        "Es greift wirklich Geisteswissenschaft in das Leben ein, macht die Instinkte anders, versetzt in unsere Seele Triebfedern, die uns geschickter ins Leben hineinstellen."
      ],
      [
        "Natürlich muß das, was ich jetzt sagen werde, immer so betrachtet werden, daß es im Zusammenhang gedacht wird mit dem menschlichem"
      ],
      [
        "Karma.",
        "Dem Karma ist der Mensch unter allen Umständen unterworfen; das muß stets berücksichtigt werden.",
        "Aber jetzt, mit Berücksichtigung des Karmas, ist doch das Folgende der Fall: Neh­men wir an, eine bestimmte Art von Erkrankung befällt denjenigen, der in die Geisteswissenschaft in der geschilderten Weise eingedrungen ist, und es liegt in seinem Karma, daß er geheilt werden kann."
      ],
      [
        "Es kann natürlich im Karma liegen, daß die Krankheit nicht geheilt werden kann.",
        "Aber Karma spricht niemals, wenn wir eine Krankheit vor uns haben, so, daß unter allen Umständen im fatalistischen Sinn &e Krankheit irgend einen Verlauf nehmen müßte, sie kann geheilt werden oder kann nicht geheilt werden."
      ],
      [
        "Derjenige, der sich nun durchdrungen hat mit Geisteswissenschaft, der bekommt in seine Seele eingepflanzt einen Instinkt, welcher ihm verhilft, aus sich selbst heraus der Krankheit und ihren Schwächen das entsprechende Stärkende oder Richtige entgegenzusetzen.",
        "Was man sonst erlebt als Folgen der Krankheit in der geistigen Welt, das wirkt noch in die Seelen zurück, insofern man noch im physischen Leibe ist, wirkt als Instinkt."
      ],
      [
        "Man beugt entweder der Krankheit vor oder aber findet in sich die Wege zu den Heilkräften.",
        "Wenn das hellseherische Bewußt­sein richtige Heilfaktoren findet für diese oder jene Krankheit, so geschieht dies auf folgendem Wege: Ein solcher Hellsehender hat die Möglichkeit, das Bild der Krankheit vor sich zu haben."
      ],
      [
        "Also nehmen wir an, er habe das Bild vor sich: das ist die Krankheit; so und so tritt sie schwächend an den Menschen heran.",
        "Dadurch, daß der Betreffende hellseherisches Bewußtsein hat, tritt ihm als Gegenbild das andere entgegen: die entsprechende Gesundungsstimmung und die Kräftigung, die aus der Stimmung herausquillt."
      ],
      [
        "Was über den Menschen, der krank war in der physischen Welt, dann als Ausgleich kommt in der geistigen Welt, das tritt dem Hellseher entgegen.",
        "Aus diesem kann er seine Ratschläge geben.",
        "Man braucht gar nicht einmal voll entwickelter Hellseher zu sein, sondern es kann das aus der Beobachtung des Krankheitsbildes instinktiv auftreten."
      ],
      [
        "Dasjenige aber, was in dem hellseherischen Bewußtsein das bewirkt, was als Ausgleich eben in der geistigen Welt wirklich kommt, das ist etwas, was zu dem Krank heitsbilde gehört, wie der Hinaufgang des Pendels auf der einen"
      ],
      [
        "Seite zu dem Hinaufgang auf der andern Seite.",
        "Gerade aus diesem Bei­spiel sehen Sie, wie das Verhältnis des physischen Planes zur geistigen Welt ist, und wie fruchtbar für die Lebensführung auf dem physischen Plan das Wissen, das Erkennen der geistigen Welt sein kann."
      ],
      [
        "Gehen wir noch einmal zu dem zurück, was heute als ein konkreter Fall angeführt worden ist: daß, wie die Natur auf dem physischen Plan, so das Geistige, das weisheitsvoll Geistige uns umgibt in der geistigen Welt, das immer da ist.",
        "Nun, gerade wenn Sie dies in einer besonderen Weise noch verstehen, dann wird sich Ihnen auf die Vor­gänge der geistigen Welt ein Licht werfen, das außerordentlich wichtig ist."
      ],
      [
        "In der physischen Welt können wir so an den Dingen vorbeigehen, daß wir, indem wir die Dinge betrachten, sagen: Wie ist es mit dem Wesen dieses Dinges?",
        "Wie verhält es sich denn?",
        "Was ist das Gesetz dieses Wesens, dieses Vorgangs?"
      ],
      [
        "Oder aber, wir gehen stumpf vorbei und fragen überhaupt nicht.",
        "Wir werden niemals auf dem physischen Plan etwas Vernünftiges lernen, wenn wir nicht so­zusagen von den Dingen veranlaßt werden, Erkennmisfragen zu stellen, wenn uns nicht die Dinge Rätsel aufgeben, so daß diese Rätsel in uns entstehen."
      ],
      [
        "Beim bloßen Anschauen der Dinge und Vorgänge werden wir auf dem physischen Plane niemals zu einer sich selbst führenden Seele kommen können.",
        "Auf dem geistigen Plan ist das wieder anders.",
        "Auf dem physischen Plan stellen wir die Fragen an die Dinge und Vorgänge, und wir müssen uns bemühen, die Dinge zu untersuchen, herauszubekommen, wie wir die Antwort auf die Frage, die wir uns stellen, aus den Dingen heraus bilden können."
      ],
      [
        "Wir müssen die Dinge untersuchen.",
        "Auf dem geistigen Plane ist es so, daß die Dinge und Wesenheiten um uns herum geistig sind; und die Dinge, die fragen uns, nicht wir fragen die Dinge.",
        "Die Dinge fragen uns, sie stehen da, die Vorgänge und Wesenheiten, und wir stehen ihnen gegenüber und werden fortwährend von ihnen gefragt."
      ],
      [
        "Wir müssen jetzt die Möglichkeit haben aus dem unendlichen Meer von Weisheit das herauszugreifen, was auf die Fragen antworten kann, die uns da gestellt werden.",
        "Wir müssen nicht aus den Dingen und Vorgängen heraus die Antworten suchen, sondern aus uns heraus, denn fragen tun uns die Dinge, überall um uns herum sind die fragenden Dinge."
      ],
      [
        "Dabei kommt noch das Folgende in Betracht: Nehmen wir an, wir stünden irgend einem Vorgang oder Wesen der geistigen Welt gegen­über, wir treten eigentlich ihm gar nicht anders gegenüber, als daß es an uns eine Frage stellt.",
        "Nehmen wir an, es stellt die Frage."
      ],
      [
        "Wir stehen da mit unserer Weisheit.",
        "Aber wir finden nicht die Möglichkeit, ein solches Wollen, fühlendes Wollen, wollendes Fühlen zu entwickeln, daß wir aus dieser Weisheit heraus die Antwort geben können, trotzdem wir wissen: die Antworten sind in uns."
      ],
      [
        "Unser Inneres ist von unendlicher Tiefe, alle Antworten sind in uns, aber wir finden nicht die Möglich­keit, wirklich die Antwort zu geben.",
        "Und die Folge davon ist, daß wir im Zeitenstrome vorbeisausen und die Möglichkeit, den rechten Zeitpunkt nämlich, versäumen, die Antwort zu geben, weil wir uns nicht die Fähigkeit erworben haben, vielleicht durch unsere vorher­gehende Entwicklung, die Reife zu haben, auf diese Frage schon in dem Zeitpunkt zu antworten."
      ],
      [
        "Wir haben uns in bezug auf das, was wir antworten sollten, zu langsam entwickelt: wir könnten erst später antworten.",
        "Aber die Gelegenheit kommt nicht wieder, wir haben sie versäumt.",
        "Wir haben nicht alle Gelegenheiten ausgenützt."
      ],
      [
        "So gehen wir vorbei an Dingen und Vorgängen, ohne ihnen Antwort zu geben.",
        "Solche Erlebnisse machen wir fortwährend in der geistigen Welt.",
        "Es kommt also vor, daß wir in dem Leben zwischen Tod und einer neuen Geburt vor einem Wesen stehen, das uns fragt."
      ],
      [
        "Wir haben es nicht dahin gebracht durch unsere Erdenleben und die dazwischenliegenden geistigen Leben, jetzt, wo es uns fragt, Antwort zu geben.",
        "Wir müssen vorbei, müssen in die nächste Inkarnation hinein."
      ],
      [
        "Die Folge davon ist, daß wir erst wiederum durch die guten Götter, ohne unser Bewußt­sein, in der nächsten Erdenverkörperung die Impulse bekommen müssen, damit wir beim nächsten Male nicht wieder an derselben Frage vorbeigehen.",
        "So sind die Zusammenhänge."
      ],
      [
        "Ich habe öfter erwähnt, daß, je weiter wir zurückgehen in der Menschheitsentwickelung, wir um so mehr gewahr werden, wie die Menschen die gegenwärtige Geistesverfassung nicht gehabt haben, sondern auf dem physischen Plan eine Art Hellsehen hatten.",
        "Aus einem dumpfen, traumhaften Hellsehen hat sich unser gegenwärtiges An­schauen der Dinge heraus entwickelt.",
        "Und je mehr wir Menschen"
      ],
      [
        "finden, die noch auf primitiven Elementarstufen der Seelenentwick­lung stehen, desto verwandter finden wir noch ihr Denken und Fühlen mit dem ursprünglichen Hellsehen.",
        "Obzwar wirkliches Helisehen, ich meine primitives, atavistisches Hellsehen, immer seltener wird, so findet man doch, wenn man hinausgeht in elementare ländliche Zu­stände, immerhin Menschen, die sich etwas bewahrt haben aus früheren Zeiten, so daß man Anklänge an die Zeiten des früheren Hellsehens findet."
      ],
      [
        "Dieses Hellsehen zeigt uns, wenn auch eben in der dumpfen traumhaften Form, weil es ja ein Schauen in die geistigen Welten hinein ist, Eigentümlichkeiten, die uns wieder entgegentreten beim entwickelten Heilsehen, nur daß es eben da nicht dumpf, traum­haft, sondern klar und deutlich uns entgegentritt.",
        "Geisteswissenschaft zeigt uns, daß der Mensch, wie er jetzt in dem gegenwärtigen Zeiten-zyklus ist, wenn er durch das Leben zwischen dem Tod und einer neuen Geburt geht, immerfort und immer mehr und mehr vor den fragenden Wesenheiten zur rechten Zeit Antwort geben muß."
      ],
      [
        "Denn davon, ob er Antwort geben kann, hängt seine richtige Fortentwick­lung ab, seine Annäherung an das Ideal der Götter von dem voll­kommenen Menschen.",
        "Wie gesagt, ins Traumhafte umgesetzt hatten das früher die Menschen, und es ist ein Überrest davon geblieben in zahlreichen märchenartigen, sagenartigen Motiven."
      ],
      [
        "Sie werden immer weniger im Volk.",
        "Aber diese märchenartigen, sagenartigen Motive, die erzählen uns dann etwa: Der oder jener begegnet einem geistigen Wesen, das stellt immer wieder und wieder Fragen an ihn, und er steht ihm gegenüber, muß antworten."
      ],
      [
        "Aber er hat das Bewußtsein: bis zu einem gewissen Glockenschlage oder sonst etwas muß er antworten.",
        "Dieses, was man das Fragemotiv der Märchen und Sagen nennen könnte, ist sehr verbreitet.",
        "Das ist in dem früheren traumhaften Hell-sehen dasselbe gewesen, was nun wiederum in der geistigen Welt auftritt in der Form, wie ich es geschildert habe."
      ],
      [
        "Überhaupt kann dasjenige, was die geistige Welt charakterisiert, in allen Fällen ein wunderbarer Leitfaden sein, um Mythen, Sagen, Märchen und so weiter in der richtigen Weise zu verstehen und sie an ihren Ort hin-zustellen, wohin sie gehören.",
        "Das ist gerade ein Punkt, wo man sieht wie überall, auch in der Geisteskultur der Gegenwart, gewissermaßen"
      ],
      [
        "die Entwickelung vor dem Tore der Geisteswissenschaft steht.",
        "Ganz interessant ist es, daß ein in vieler Beziehung in der Absicht schönes Buch wie das meines verstorbenen Freundes Ludwig Laistner, «Das Rätsel der Sphinx», deshalb ungenügend ist, weil, wenn es ge­nügend hätte werden sollen, es die Motive dieses Fragens, die Ludwig Laistner besonders ausführlich behandelt, aus einem geisteswissen­schaftlichen Wissen hätte behandeln müssen, weil also der Autor etwas hätte wissen müssen von dem Hineinspielen der geisteswissenschaft­lichen Wahrheit in die Sache."
      ],
      [
        "Wir sehen also, wenn wir uns gerade die charakteristischen aufge­zählten Fälle vor Augen stellen, daß es auf etwas ganz Bestimmtes ankommt in dem Verhalten in der geistigen Welt.",
        "Erkenntnisse zu sammeln in der geistigen Welt, wie hier auf dem physischen Plane, darauf kommt es nicht an."
      ],
      [
        "Es kommt darauf an, sogar diese Erkennt­nisse zu vermindern, nämlich die Erkenntniskraft umzuwandeln in Lebenskraft.",
        "Forscher kann man nicht sein in der geistigen Welt in dem Sinn, wie man es in der physischen Welt sein kann; das wäre dort sehr deplaciert Denn wissen kann man dort alles, es ist alles um einen herum."
      ],
      [
        "Das, worauf es ankommt, ist, daß man den Willen und die Empfindung gegenüber dem Wissen, gegenüber der Erkenntnis entwickeln kann, so daß man im Einzelfalle aus dem ganzen Schatze seines Woliens das gerade herausbringt, wodurch man die Weisheit anwenden kann, sonst erstickt oder ertrinkt man in der Weisheit.",
        "Also während es hier in der physischen Welt auf das Denken ankommt, kommt es dort in der geistigen Welt an auf das entsprechende Aus­bilden des Willens, des empfindenden Willens, des Willens, der aus der Weisheit heraus die Realität bereitet, formt, des Willens, der zur kreativen Kraft wird, zu einer Art schöpferischen Kraft."
      ],
      [
        "Den Geist haben wir dort, wie wir hier die Natur haben; aber den Geist zur Natur zu führen, das ist unsere Aufgabe.",
        "Ein schöner Satz ist erhalten aus der theosophischen Literatur der ersten Hälfte des 19."
      ],
      [
        "Jahr­hunderts von Ötinger, der in Murrhardt in Württemberg gelebt hat, und der in seiner eigenen spirituellen Entwicklung so weit war, daß er ganz bewußt in gewissen Zeiten geistigen Wesenheiten, also Seelen, die nicht auf dem physischen Plane sind, hat Helfer sein können."
      ],
      [
        "hat den merkwürdigen Satz geprägt, der sehr schön und sehr richtig ist: Natur und Naturgestalt ist das Ende der geistigen Schöpferkraft. -Das, was ich jetzt aus der geistigen Welt selber herausentwickelt habe, liegt in diesem Satz.",
        "Es strebt in der geistigen Welt die Schöpferkraft dahin, das, was in Weisheit zunächst wallt und wogt, hinauf zur Realität zu bringen.",
        "Wie man hier aus der physischen Realität die Weisheit herausbringt, macht man das dort umgekehrt.",
        "Aus der Weis­heit heraus hat man die Aufgabe, Realitäten zu schaffen, in Realitäten auszuleben das, was dort in Weisheit ist.",
        "Das Ende der Götterwege ist geformte Wirklichkeit."
      ],
      [
        "So sehen wir also, es kommt auf wiliensdurchtränktes Fühlen an, auf von Gefühl durchtränkten Willen, die sich umwandeln in kreative Kraft, schöpferische Kraft, die wir dort in der geistigen Welt so an-wenden müssen, wie wir uns hier auf der physischen Welt anstrengen müssen in unserem forschenden Denken, um in der physischen Welt zur Weisheit zu kommen."
      ],
      [
        "Nun handelt es sich darum, daß wir für diese Möglichkeit in der geistigen Welt das Fühlen und Denken richtig entwickeln, daß wir uns dafür schon hier auf dem physischen Plane in einer Weise, wie es für den gegenwärtigen Zeitenzyklus richtig ist, vorbereiten.",
        "Denn alles das, was in der geistigen Welt geschieht zwischen dem Tod und einer neuen Geburt, ist Folge desjenigen, was in der physischen Welt geschieht zwischen der Geburt und dem Tode.",
        "Zwar ist das, was in der geistigen Welt ist, wie wir gesehen haben, so anders, daß wir uns ganz neue Vorstellungen und Begriffe aneignen müssen, wenn wir die geistige Welt verstehen wollen.",
        "Aber dennoch: wie Ursache und Wirkung hängen die beiden gegenseitig zusammen.",
        "Nur dann ver­stehen wir die Zusammenhänge zwischen dem Geistigen und dem Physischen, wenn wir sie als Zusammenhänge von Ursache und Wir­kung wirklich erkennen.",
        "Vorbereiten müssen wir uns in der physischen Welt.",
        "Deshalb möchte ich jetzt die Frage ein wenig betrachten: Wie bereiten wir uns im gegenwärtigen Zeitenzyklus in der richtigen Weise auf dem physischen Plane vor, so daß wir genügend innere Impulse haben in der geistigen Welt, sei es, daß wir durch Initiation, sei es, daß wir durch die Pforte des Todes hineinkommen, um wirklich die"
      ],
      [
        "geistige Schlagkraft zu haben, aus der gegebenen Weisheit das heraus­zuholen, was wir brauchen, um Realitäten herauszuwandeln aus der strömenden, wogenden Weisheit?",
        "Woher kommt uns solche Kraft?",
        "Es kommt überall darauf an, daß wir solche Dinge für unseren Zeiten-zyklus beantworten.",
        "In den Zeiten, in denen die Menschen so dachten, daß die ersten ursprünglichsten Quellen der genannten Sagenmotive sich bildeten, da war es anders.",
        "Aber woher kommt uns solche Seelen-kraft im gegenwärtigen Zeitenzyklus?"
      ],
      [
        "Um uns einer Antwort nähern zu können, möchte ich Folgendes heranziehen.",
        "Man kann sich in verschiedenen Philosophien umsehen und kann bei den Philosophen suchen nach der Art, wie sie zu dem Gottesbegriffe kommen."
      ],
      [
        "Es müssen dann selbstverständlich solche Philosophen sein, die geistige Tiefe genug haben, um sich eben von der Welt überzeugen zu lassen, daß man von einem Göttlichen, das die Welt durchdringt, sprechen kann.",
        "Im neunzehnten Jahrhundert braucht nur Lotze genommen zu werden, der in seiner Religions­philosophie etwas zu schaffen suchte, was im Einklang steht mit seiner übrigen Philosophie."
      ],
      [
        "Aber es könnten auch andere Philosophen ge­nommen werden, die eben wirklich tief genug waren, um sozusagen auch eine Religionsphilosophie zu haben.",
        "Eine Eigentümlichkeit wird man bei allen diesen Philosophen finden, eine ganz bestimmte Eigen­tümlichkeit."
      ],
      [
        "Ja, zu dem Göttlichen dringen diese Philosophen mit ihren Erwägungen aus dem physischen Plane denkend vor; sie denken nach, forschen auf philosophische Art, kommen darauf, wie es gerade bei Lotze der Fall ist, daß die Erscheinungen und Wesen der Welt zusammengehalten werden von einem göttlichen Grund, der alles durchwebt und alles in eine gewisse Harmonie bringt.",
        "Wenn man aber näher auf solche Religionsphilosophien eingeht, so haben sie immer eine Eigentümlichkeit."
      ],
      [
        "Man kommt eben zu einem göttlichen Wesen, das alles durchtränkt und durchzieht, und wenn man dieses göttliche Wesen sich näher ansieht, diesen Gott der Philosophen, so kommt man darauf, daß es ungefähr der Gott ist, den die hebräische oder namentlich die christliche Religion den Vatergott nennt, Gott-Vater.",
        "Dazu kann die Philosophie kommen."
      ],
      [
        "Sie kann die Natur be­trachten und tief genug sein, um nicht in hohiköpfiger materialistischer"
      ],
      [
        "Weise alles Göttliche abzuleugnen, sie kann zu dem Göttlichen kom­men, kommt aber dann zu dem Vatergott.",
        "Man kann ganz genau, wenn man die Philosophen verfolgt, zeigen, daß zu etwas anderem die bloße Philosophie als denkende Philosophie überhaupt nicht führen kann, als zu einem monotheistischen Vatergott.",
        "Wenn bei einzelnen Philosophen, bei Hegel zum Beispiel und anderen, der Christus auftritt, so ist er nicht aus der Philosophie heraus - das läßt sich nachweisen - er ist aus der positiven Religion herübergenommen.",
        "Die Leute haben gewußt, daß die positive Religion den Christus hat, dann konn­ten sie ihn besprechen.",
        "Der Unterschied ist der, daß man den Vatergott in der Philosophie finden kann; Christus kann man mit keiner Philosophie durch denkende Betrachtung finden.",
        "Das ist ganz un­möglich."
      ],
      [
        "Das ist ein Satz, von dem ich Ihnen raten möchte, ihn wohl zu erwägen und viel darüber nachzudenken.",
        "Wenn man ihn richtig ver­steht, führt er in sehr bedeutsame Tiefen menschlichen Forschens und Seelenstrebens hinein.",
        "Aber er hängt allerdings zusammen mit etwas, was in der christlichen Religion sogar sehr schön symbolisch, bildhaft, zum Ausdruck gebracht ist: nämlich damit, daß man das Verhältnis dieses anderen Gottes, des Christus, zu dem Vatergott als das Ver­hältnis des Sohnes zum Vater auffaßt.",
        "Das ist sehr bedeutsam, obwohl es nur ein Symbol ist.",
        "Es ist interessant, daß damit zum Beispiel Lotze gar nichts anfangen kann.",
        "Daß man dieses Symbol nicht wörtlich nehmen kann, ist selbstverständlich, sagt Lotze, denn es kann nicht der eine Gott der Sohn des anderen Gottes sein, meint er.",
        "Nun, es ist aber doch etwas sehr Bezeichnendes in diesem Symbolum.",
        "Zwischen dem Vater und dem Sohn ist so etwas wie das Verhältnis von Ursache und Wirkung.",
        "Denn in gewisser Weise kann man im Vater die Ur­sache des Sohnes suchen.",
        "Der Sohn wäre nicht da, wenn der Vater nicht da wäre.",
        "Aber ein Eigentümliches muß man beachten: daß nämlich derjenige Mensch, der einen Sohn eventuell haben kann, durchaus auch die Möglichkeit hat, keinen zu haben, er kann sohnlos sein.",
        "Er würde dann derselbe Mensch sein.",
        "Die Ursache ist der Mensch A, die Wirkung ist der Mensch B, der Sohn.",
        "Aber die Wirkung braucht nicht einzutreten, die Wirkung ist eine freie Tat, die Wirkung"
      ],
      [
        "folgt aus der Ursache als eine freie Tat.",
        "Deshalb muß man, wenn man eine Ursache studiert und sie mit ihrer Wirkung im Zusammenhang faßt, nicht bloß fragen nach dem Wesen der Ursache, denn damit hat man noch gar nichts getan, sondern danach muß man fragen, ob die Ursache auch wirklich verursacht, und darauf kommt es an."
      ],
      [
        "Nun hat alle Philosophie das Eigentümliche, daß sie am Gedankenfaden fort­geht, ein Glied aus dem andern entwickelt, also gleichsam in dem Vorderen schon das Nachfolgende sucht.",
        "So haben sie recht als Philosophien."
      ],
      [
        "Aber man kommt dabei niemals auf dasjenige Verhält­nis, welches sich ergibt, wenn man berücksichtigt, daß die Ursache gar nicht zu verursachen braucht.",
        "Die Ursache kann ihrem Wesen nach, in ihrem Wesen dasselbe sein, ob sie als Ursache etwas verursacht oder nicht."
      ],
      [
        "Das ändert nichts in dem Wesen der Ursache.",
        "Und dieses Bedeutungsvolle ist uns hingestellt in dem Symbolum von Gott-Vater und Gott-Sohn: daß der Christus hinzukommt als eine freie Schöpfung zu dem Vatergott, als eine Schöpfung, die nicht unmittelbar aus ihm folgt, sondern die sich als freie Tat neben die vorhergehende Schöp­fnng hinstellt."
      ],
      [
        "Die auch die Möglichkeit hätte, nicht zu sein: die der Welt also nicht deshalb gegeben ist, weil der Vater den Sohn der Welt geben mußte, sondern der Sohn ist der Welt gegeben als eine freie Tat, durch Gnade, durch Freiheit, durch Liebe, die sich frei gibt in ihrer Schöpfung.",
        "Deshalb kann man niemals durch dieselbe Art von Wahrheit, durch die man zu dem Vatergott kommt wie die Philosophen, auch zum Sohnesgott, zu dem Christus kommen."
      ],
      [
        "Um zum Christus zu kommen, ist notwendig, daß man zu der philo­sophischen Wahrheit die Glaubenswahrheit hinzufügt, oder - weil die Zeit des Glaubens immer mehr und mehr abnimmt - die andere Wahrheit hinzunimmt, die durch hellseherische Forschung kommt, die sich als eine freie Tat ebenfalls erst in der menschlichen Seele entwickeln muß."
      ],
      [
        "Daher muß man sagen: So wie man aus der Anordnung der Natur­vorgänge beweist, daß es einen Gott überhaupt gibt, so kann man niemals äußerlich an der Kette von Ursachen und Wirkungen bewei­sen, daß es einen Christus gibt.",
        "Der Christus ist dagewesen und kann an den Menschenseelen vorbeigehen, wenn sie nicht aus sich selber"
      ],
      [
        "heraus die Kraft empfinden, zu sagen: Ja, das ist der Christus.",
        "Es gehört ein aktives Sich-Aufraffen zum Wahrheitsimpuls dazu, um in dem, der da war als der Christus, den Christus zu erkennen.",
        "Zu den anderen Wahrheiten, die im Bereich des Vatergottes liegen, können wir gezwungen werden, wenn wir uns überhaupt nur in das Denken begeben und es konsequent anwenden, denn Materialist sein, heißt zu gleicher Zeit unlogisch sein."
      ],
      [
        "Religionsphilosophie im Sinne Lotzes, und wie überhaupt Religionsphilosophie sein kann, entsteht so, daß wir durch das Denken zu diesem Göttlichen der Religionsphilosophie gezwungen werden können.",
        "Niemals aber können wir in der gleichen Art durch bloße Philosophie dahin gebracht werden, den Christus anzuerkennen."
      ],
      [
        "Das muß unsere freie Tat sein.",
        "Da ist dann nur zweierlei möglich: entweder man zieht die letzte Konsequenz des Glaubens, oder man macht den Anfang mit der Erforschung der geistigen Welt mit Geisteswissenschaft."
      ],
      [
        "Die letzte Konsequenz des Glaubens zieht man, wenn man sagt, wie der russische Philosoph Solowjew: Ja, in bezug auf all die philosophischen Wahrheiten, die der Mensch über die Welt gewinnt, so daß er sich durch seine Logik zwingen läßt, steht der Mensch in keiner freien Wahrheit.",
        "Das ist eben gerade die höhere Wahrheit, die uns nicht zwingt, die unsere freie Tat ist: die höchste Glaubenswahrheit."
      ],
      [
        "Darin vollendet sich die höchste Würde für Solow­jew, daß er sagt: Die höhere Wahrheit, die den Christus anerkennt, das ist die Wahrheit, die als freie Tat schafft, die sich nicht zwingen läßt. -Für den Geistesforscher und für den, der die Geisteswissenschaft ver­steht, entsteht wiederum das Wissen.",
        "Aber das ist ein aktives Wissen, das sich vom Denken zur Imagination, Inspiration, Intuition erhebt, das innerlich schöpferisch wird, das im Schaffen sich einlebt in die geistigen Welten und dadurch dem, was wir entwickeln müssen, ähnlich wird, sei es, daß wir durch Initiation oder durch den Tod in die geistige Welt hineinkommen."
      ],
      [
        "Die Weisheit, die sich uns auf Erden aufzwingt, die haben wir in der geistigen Welt in Hülle und Fülle, wie wir hier auf dem physischen Plane die Naturerscheinungen haben.",
        "Das, worauf es in der geistigen Welt ankommt, ist, daß wir den Impuls, die Kraft haben, aus dieser Weisheit heraus etwas zu machen, durch sie Realität zu schaffen."
      ],
      [
        "Freies Schaffen aus der Weisheit heraus, geistiges Wirken als Tat, das ist es, was m uns als Impuls leben muß.",
        "Das können wir nur haben, wenn wir das richtige Verhältnis zu dem Christus finden.",
        "Der Christus ist diejenige Wesenheit, die sich nicht durch die äußere Logik des Verstandes, der an das Gehirn gebunden ist, beweisen läßt, die sich aber erweist, die sich realisiert in uns, indem wir uns geistiges Wissen erwerben."
      ],
      [
        "So wie als freie Tat Geisteswissenschaft sich hinzugesellt zu der anderen Wissenschaft, so kommt hinzu das Wissen um den Chri­stus, sobald wir uns derjenigen Welt nähern, in die wir durch die Geistesforschung hineinkommen, oder die wir betreten, indem wir durch die Pforte des Todes gehen.",
        "Im Augenblicke, wo wir im gegen­wärtigen Zeitenzyklus in einer segensvollen Weise in die geistige Welt hineinkommen wollen, das heißt, wo wir der physischen Welt absterben wollen, brauchen wir ein solches Verhältnis zur Welt, wie wir es gewinnen, wenn wir uns in der richtigen Weise zum Christus verhalten."
      ],
      [
        "Einen Gott, der sozusagen ist, wie der Vatergott der christlichen Religion, ihn können wir gewinnen durch die Betrachtung der Natur, ihn können wir gewinnen durch die Betrachtung, die sich uns ergibt, indem wir im physischen Leibe leben.",
        "Den Christus recht zu verstehen ohne die Tradition, ohne die Überlieferung, rein aus der Erkenntnis selber heraus, ist nur möglich durch die Geisteswissen­schaft."
      ],
      [
        "Sie führt in die Gebiete hinein, die der Mensch durch das Sterben betritt, sei es jenes Sterben, das eine symbolisches Sterben ist, das Herausgehen aus dem physischen Leibe, um in der Seele sich außerhalb des Leibes zu wissen, sei es das andere Sterben, durch die Pforte des Todes hindurch.",
        "Richtig statten wir uns aus mit den Im­pulsen, die wir brauchen, indem wir durch die Pforte des Todes gehen, wenn wir das rechte Verhältnis zum Christus finden."
      ],
      [
        "In dem Augenblick, wo es ans Verlassen des physischen Leibes geht, sei es, indem wir in die geisteswissenschaftliche Entwicklung eintreten, sei es, daß wir wirklich durch die Pforte des Todes gehen, in dem Augen­blick, wo es ans Sterben, ans Verlassen des physischen Leibes geht, kommt es darauf an, daß wir im gegenwärtigen Zeitenzyklus in der rechten Art derjenigen Wesenheit gegenüberstehen, die in die Welt gekommen ist, damit wir das Verhältnis zu ihr finden.",
        "Den Vatergott"
      ],
      [
        "können wir als Lebende finden.",
        "Den Christus finden wir, wenn wir das Hineingehen in den Geist, wenn wir das Sterben in der richtigen Weise verstehen.",
        "In Christus sterben wir."
      ],
      [
        "In Christo morimur."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "FÜNFTER VORTRAG Wien, 13. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Es wird mir nun obliegen, von den Vorgängen zwischen dem Tod und einer neuen Geburt noch einmal zu sprechen, aber mit Benutzung derjenigen Vorstellungen, die wir in den vier letzten Vorträgen haben gewinnen können. Es wird natürlich dadurch, daß es mit einer gewissen Kürze wird behandelt werden müssen, manches von dem umfassenden Thema nur angedeutet werden können, es wird man­ches, was vielleicht aus der bildlichen Darstellung nicht folgt, herausgearbeitet werden müssen. Aber das, was unsere anthropo­sophischen Freunde heute nicht schon vollständig finden werden, wird dann im Laufe der weiteren Erkenntnis der Geisteswissenschaft sich zeigen.",
      "Wenn der Mensch durch die Pforte des Todes getreten ist, so hat er seinen physischen Leib abgelegt, der physische Leib ist den Ele­menten der Erde übergeben. Mit anderen Worten könnte auch über ihn gesagt werden: Der physische Leib hat sich herausgehoben aus den Kräften und Gesetzen, die ihn zwischen der Geburt und dem Tode vom eigentlichen Menschen heraus durchdringen, und die an­dere Gesetze sind als die bloß chemischen und physikalischen Gesetze, denen er dann nach dem Tode als physischer Leib verfällt. Vom Ge­sichtspunkt der physischen Welt aus hat der Mensch ja selbstver­ständlich die Anschauung: Von der menschlichen Wesenheit ist zurückgeblieben auf dem physischen Plane das, was diesem physischen Plane angehört. Es wird dieses dem physischen Plane Angehörige nun auch dem physischen Plane übergeben. Für den Menschen selbst aber und für alle Auffassung der geistigen Welt kommt der Gesichts­punkt in Betracht, den der Tote, der Mensch, der durch die Pforte des Todes geschritten ist, hat einnehmen müssen. Für ihn bedeutet das Verlassen des physischen Leibes einen inneren Vorgang, einen Seelenvorgang, für die Hinterbliebenen ist das, was mit dem physi­schen Leibe nach dem Tode geschieht, ein äußerer Vorgang. Das Innere des Menschen, das Menschlich-Seelenhafte des verstorbenen",
      "Menschen drückt sich ja innerhalb dessen, was als sterblicher Über­rest zurückgeblieben ist, nicht mehr aus. Für den Menschen selbst aber, der durch die Pforte des Todes gegangen ist, ist dennoch etwas verbunden mit dem Verlassen des Leibes. Es bedeutet ein innetes Seelenerlebnis: Du bist aus deinem physischen Leibe herausgegangen und lässest diesen physischen Leib zurück.",
      "Es ist außerordentlich schwierig, ich möchte sagen, vom Stand­punkt des physischen Planes aus dieses, was da im Innern der Seele des Menschen vorgeht, wirklich sachgemäß zu schildern. Denn es ist ein innerer Vorgang, der im Grunde etwas ungeheuer Umfassendes, etwas ungeheuer Bedeutsames hat.",
      "Es ist ein innerer Vorgang, der ja im Grunde kurz dauert, aber von einer für das gesamte menschliche Leben universalen Bedeutung ist. Nun, wenn man den Vorstellungs­inhalt dessen schildern möchte, was da mit der Seele vorgeht, diesen Vorstellungsinhalt, den man natürlich heute in einem öffentlichen Vortrag noch nicht berühren kann, denn er würde die Öffentlichkeit zu seht frappieren - vielleicht kommt aber auch dazu die Zeit - wenn man den äußeren, also jetzt geistig äußerlichen Vorstellungsvorgang schildern wollte, mit dem sozusagen der Lebensweg beginnt, der zwischen dem Tod und einer neuen Geburt verläuft, so könnte man sagen, der durch die Pforte des Todes Geschrittene hat zunächst das Gefühl: Du bist jetzt in einem ganz anderen Verhältnisse zur Welt als du vorher warst, und das ganze frühere Verhältnis, das du zur Welt hattest, ist im Grunde genommen umgekehrt, radikal umgekehrt.",
      "Man müßte eigentlich in der folgenden Weise schildern, wenn man das, was da vorstellungsmäßig erlebt wird, schildern wollte. Man müßte sagen: Der Mensch hat bis zu seinem Tode auf der Erde gelebt, er ist gewohnt gewesen in dieser Zeit auf der festen, materiellen Erde zu stehen, auf dieser materiellen Erde die Wesen des mineralischen, pflanzlichen, tierischen Reiches, Berge, Flüsse, Wolken, Sterne, Sonne und Mond zu sehen, und ist gewohnt worden, durch seinen eigenen Gesichtspunkt und durch seine im physischen Leib vorhandenen Fähigkeiten, sich dieses Ganze so vorzustellen, wie man es sich ja doch vorstellt, trotzdem man heute durch den Kopernikanismus weiß, daß es im Grunde ein Scheinbild ist: da oben ist das blaue Himmelsgewölbe",
      "wie eine Himmelsschale, da sind die Sterne darauf, darüber gehen Sonne und Mond und so weiter, man selber ist wie in dieser Schale, in dieser Hohlkugel, im Innern da drinnen in der Mitte auf der Erde mit dem, was einem die Erde für die Wahrnehmung zeigt.",
      "Es kommt uns jetzt nicht darauf an, daß das ein Scheinbild ist, daß wir selber nur durch die Beschränktheit unserer Fähigkeiten uns diesen blauen Umkreis bilden, sondern darauf, daß wir ja gar nicht anders können als das zu sehen. Wir sehen eben das, was nur durch die Beschränktheit unserer Fähigkeiten so ist, sehen eben eine blaue Kugel als Firmament über uns gebildet.",
      "Wenn nun der Mensch durch die Pforte des Todes gegangen ist, so ist das erste, daß er die Vor­stellung seiner Seele ausbilden muß: Du bist jetzt außerhalb dieser blauen Kugel, in der du warst. Du siehst sie von außen an, aber so, als ob sie zu einem Stern zusammengeschrumpft wäre.",
      "Man hat zu­nächst kein Bewußtsein von der Sternenwelt, in die man sich eigent­lich ausbreitet, sondern man hat zunächst nur ein Bewußtsein von dem, was man verlassen hat: daß man seine Bewußtseinssphäre, die man gehabt hat im physischen Leibe, verlassen hat, daß man das ver­lassen hat, bis wohin einen die menschlichen Fähigkeiten, die im physischen Leibe ausgebildet sind, haben schauen lassen. Es ist wirk­lich, aber geistig, etwas Ähnliches vorgegangen, wie es vorgehen müßte, wenn mit bewußtem Erleben ein Küchlein, das in der Eier­schale drinnen ist, diese zerbricht und nachher die zerbrochene Ei­schale, die es bisher umschlossen hat, seine bisherige Welt, von außen statt von innen ansieht.",
      "Natürlich ist diese Vorstellung wiederum Maja, die da durch die menschliche Seele zieht, aber eine notwendige Maja. Wie gesagt: zusammengeschrumpft wie zu einem Sterne ist das, was uns vorher den Inhalt unseres Bewußtseins gab, nur daß sich, von diesem Sterne ausgehend, dasjenige ausbreitet, was man nennen könnte: erstrahlende kosmische Weisheit.",
      "Diese erstrahlende kosmische Weisheit ist dasselbe, welches ich auch gestern im letzten Vortrag behandelt habe, und von dem ich gesagt habe, daß wir es in Fülle haben. Das glimmt und glitzert uns entgegen wie von einem feurigen Stern. Jetzt ist es nicht blau wie das Firmament, sondern jetzt ist es feurig, rötlich erglimmend, und davon",
      "ausstrahlend in den Raum die Fülle von Weisheit, die uns aber zuerst zeigt - sie ist in sich ganz beweglich - das, was man ein Erinnerungs­tableau unseres letzten Erdenlebens nennen könnte. All die Vorgänge, die wir mit unserem inneren Seelenerleben durchmessen haben zwi­schen der Geburt und dem Tode, wo wir bewußt dabei waren, treten vor unsere Seele hin, aber so, daß wir wissen: Du siehst das alles, weil der Stern, der da vor dir aufglänzt, der Hintergrund ist, der durch seine innere Tätigkeit bewirkt, daß du das alles sehen kannst, was sich als ein Erinnerungstableau ausbreitet.",
      "Das ist so mehr vom Stand-punkt der Imagination aus gesprochen. Vom Standpunkt der Inner­lichkeit gesprochen ist das Erlebnis etwa dieses, daß derjenige, der durch die Pforte des Todes gegangen ist, nunmehr ganz erfüllt ist von dem Gedanken: Ja, du hast deinen Leib verlassen.",
      "Jetzt, in der geisti­gen Welt, ist dieser Leib lauter Wille. Ein Willensstern, ein Stern, dessen Substanz Wille ist, das ist dein Leib. Und dieser Wille erglüht in Wärme und strahlt dir in den Weltenweiten, in die du dich jetzt selber ergossen hast, dein eigenes Leben zwischen der Geburt und dem Tode wie ein großes Tableau zurück.",
      "Und du verdankst dem Umstande, daß du innen verweilen konntest in diesem Stern, daß du alles das aus der Welt ziehen und saugen konntest, was du auf dem physischen Plan aus der Welt eben gezogen und gesaugt hast. Denn dieser Stern, dieser Willensstern, der jetzt den Hintergrund bildet, das ist das Geistige deines physischen Leibes, dieser Willensstern ist der Geist, der deinen physischen Leib durchtränkt und durchkraftet.",
      "Das, was dir als Weisheit erstrahlt, das ist die Tätigkeit, die Beweglichkeit deines Ätherleibes.",
      "Es vergeht die Zeit, das ist ja auch schon im öffentlichen Vortrag charakterisiert worden, die eigentlich nur nach Tagen dauert, wo man den Eindruck hat: das Leben spielt sich ab wie ein Erinnerungs­tableau. Unsere Gedanken, die zu unseren Erinnerungen während des Lebens auf der Erde geworden sind, rollen da gleichsam ab in diesem Erinnerungstableau, die treten noch einmal vor unsere Seele hin. Und wir können es so lange aufrecht erhalten, als wir die Kraft haben, unter normalen Verhältnissen uns im physischen Leibe wach zu er­halten. Es kommt ja nicht darauf an, wie lange wir einmal im Leben",
      "wach geblieben sind in abnormen Verhältnissen, es kommt darauf an, welche Kräfte wir in uns haben, um eben uns wach zu erhalten. Diese sind bei dem einen so, daß er kaum eine Nacht durchwachen kann, ohne daß ihn Müdigkeit überkommt, bei dem anderen, daß er es länger aushalten kann, ohne müde zu werden. Von dem Maße dieser Kräfte ist es abhängig, wie lange der Mensch braucht, um mit diesem Erinnerungstableau fertig zu werden. Aber man hat auch das ganz deutliche innere Bewußtsein, daß dadurch, daß der Willensstern im Hintergrunde ist, in diesem Erinnerungstableau dasjenige ist, was wir uns im letzten Erdenleben errungen haben. Daß darin das ist, um was wir reifer geworden sind, was wir sozusagen durch den Tod als ein Mehr hinausgetragen haben gegenüber dem, was wir beim Eintritt in unsere Geburt als ein Geringeres gehabt haben. Dieses, was wir wie eine Frucht des letzten Lebens bezeichnen können, das fühlen wir so, als wenn es nicht bleiben würde, wie es war während des Erinnerungs­tableaus, sondern wie wenn es sich fernte, wie wenn es fortginge, wie wenn es in der Zeiten Zukunft hineinginge und in der Zeiten Zukunft entschwände.",
      "Ich werde heute vorzugsweise davon reden, wie es sich mit dem Leben zwischen dem Tod und einer neuen Geburt verhält bei solchen Menschen, die eine normale Lebensdauer erreicht haben und in normalen Verhältnissen gestorben sind. Für Ausnahmefälle soll dann morgen das Nähere gesagt werden.",
      "Also es fernt sich unsere Lebensfrucht, wenn wir eine solche er­langt haben, und wir wissen in der Seele: diese Frucht ist irgendwie vorhanden, aber wir sind hinter ihr zurückgeblieben. Man hat das Bewußtsein, man ist an einem früheren Zeitpunkt verblieben, die Lebensfrucht zieht schnell fort, so daß sie früher ankommt an einem späteren Zeitpunkt, und wir müssen ihr nachziehen, dieser Lebens-frucht. Das, was ich jetzt gesagt habe, dieses innere Erlebnis, daß die Lebensfrucht im Weltenall weilt, vorhanden ist, das müssen wir uns so recht vorstellen, denn das ist es, was den Grund bildet für unser Bewußtsein, für den Beginn unseres Bewußtseins nach dem Tode. Unser Bewußtsein muß ja sozusagen immer durch etwas angeregt werden. Wenn wir des Morgens aufwachen, so wird unser Bewußtsein",
      "neuerdings angefacht - während wir beim Schlaf bewußtlos sind - durch das Eintauchen in den physischen Leib und dadurch, daß uns die äußeren Dinge gegenübertreten, dadurch daß etwas von außen wirkt. In den Verhältnissen unmittelbar nach dem Tode wird dieses Bewußt­sein angefacht durch das innere Erfühlen und Erleben dessen, was die Frucht unseres letzten Lebens ist, was wir uns errungen, erobert haben. Das ist vorhanden, aber außer uns vorhanden. Durch dieses Erfühlen und Erleben unseres innersten irdischen Wesens außer uns haben wir die erste Entzündung unseres Bewußtseins nach dem Tode, daran belebt sich dieses Bewußtsein.",
      "Dann beginnt die Zeit, in welcher es notwendig ist, daß wir Seelen-kräfte entwickeln, welche während des Lebens auf dem physischen Plane eigentlich unentwickelt bleiben müssen, weil sie alle dazu ver­wendet werden, den physischen Leib und das, was zu ihm gehört, das ganze physische Leben, durchzuorganisieren, Seelenkräfte, die während des physischen Lebens in etwas anderes verwandelt sein müssen. Diese Kräfte müssen allmählich erwachen nach dem Tode.",
      "Schon in den Tagen, während welcher wir das Erinnerungstableau erleben, haben wir ein solches Erwachen von Seelenfähigkeiten zu verzeichnen. Wenn das Erinnerungstableau nach und nach abflutet und abdämmert, so geschieht das eigentlich dadurch, daß wir während dieser Tage schon diejenigen Kräfte entwickeln, welche der Erinne­rungsfähigkeit zwar zugrunde liegen, aber nicht bewußt werden während des physischen Lebens, und zwar deshalb nicht, weil wir während dieses physischen Lebens sie gerade umwandeln müssen, um Erinnerungen bilden zu können.",
      "Die letzte große Erinnerung, die wir nach dem Tode in Form des Tableaus haben, die muß erst ab-fluten, die muß nach und nach verdämmern, dann entwickelt sich aus der Verdämmerung heraus das, was wir bewußt nicht haben durften vor dem Tode. Denn hätten wir es bewußt gehabt vor dem Tode, so hätten sich niemals in uns die Erinnerungskräfte bilden können.",
      "Um­gewandelt in diese Fähigkeit uns zu erinnern haben sich die Kräfte, die sich jetzt in der Seele während des Abdämmerns der Erinnerung des Lebenstableaus heraus entwickeln. Umgesetzt in die Erinnerungs­kraft haben sich diese vor dem Tode, und jetzt kommen sie heraus,",
      "indem die Möglichkeit, sich in gewöhnlicher Weise an irdische Ge­danken zu erinnern, überwunden wird. Diese gleichsam ins Geistige umgewandelte Gedächtniskraft erwacht als eine erste geistig-seelische Kraft in uns, die nach dem Tode aus der menschlichen Seele so heraus­kommt, wie die Seelenkräfte beim heranwachsenden Kinde in den ersten Lebenswochen herauskommen. Indern diese Seelenkraft heran­wächst, zeigt sich uns eben, daß hinter den Gedanken, die, während wir auf dem physischen Plane waren, nur Schattenbilder waren, Lebendiges steckt, daß ein Leben und Weben in der Gedankenwelt ist. Wir werden gewahr, daß das, was wir innerhalb des physischen Leibes als unser Gedankentableau haben, eben nur ein Schattenbild ist, daß es in Wahrheit eine Summe, eine Ausbreitung von Elementarwesen ist. Wir sehen gleichsam unsere Erinnerungen abglimmen und sehen dafür aus dem allgemeinen Weisheitskosmos heraus eine ganze Anzahl von Elementarwesen erwachen.",
      "Sie könnten fragen, meine lieben Freunde: Ja, geht uns denn das nicht ab nach dem Tode, daß wir gerade die Erinnerungskraft über­winden und etwas anderes dann haben? Es geht uns nicht ab, denn wir haben reichlichen Ersatz dafür nach dem Tode. Statt daß wir uns wie im Leben an unsere Gedanken erinnern, merken wir nach dem Tode, daß diese Gedanken, die wir als Gedächtnisgedanken im Leben hatten, für uns sich nur so ausnehmen wie Erinnerungen. Oh, dieser Gedächtnisschatz während des Lebens, er ist etwas ganz anderes als ein bloßer Gedächtnisschatz! Sind wir aus dem physischen Leibe heraus, dann sehen wir diesen ganzen Gedächtnisschatz als lebendige Gegenwart, dann ist er da. Jeder Gedanke lebt als ein Elementarwesen. Wir wissen jetzt: Du hast gedacht während deines physischen Lebens, dir sind deine Gedanken erschienen. Aber während du in dem Wahne warst, du bildetest dir Gedanken, hast du lauter Elementarwesen ge­schaffen. Das ist das Neue, was du zum ganzen Kosmos hinzugefügt hast. Jetzt ist etwas da, was in den Geist hinein von dir geboren worden ist, jetzt taucht vor dir auf, was deine Gedanken in Wirklich­keit waren. Man lernt zunächst in unmittelbarer Anschauung er­kennen, was Elementarwesen sind, weil man diejenigen Elementar-wesen zuerst erkennen lernt, die man selber geschaffen hat. Das",
      "ist der bedeutungsvolle Eindruck der ersten Zeit nach dem Tode, daß man das Erinnerungstableau hat. Aber dieses fängt an zu leben, richtig zu leben, und indem es anfängt zu leben, verwandelt es sich in lauter Elementarwesen. Jetzt zeigt es sozusagen sein wahres Antlitz, und darin besteht sein Verschwinden, daß es etwas ganz anderes wird. Wir brauchen, wenn wir zum Beispiel mit sechzig oder achtzig Jahren gestorben sind, jetzt nicht mehr für irgend einen Gedanken, den wir etwa im zwanzigsten Jahre unseres Lebens gehabt haben, Erinnerungskraft, denn er ist da als lebendiges Elementar-wesen, er hat gewartet und wir brauchen uns nicht an ihn zu erinnern. Denn wären wir zum Beispiel in unserem vierzigsten Lebensjahre gestorben, so wäre der Gedanke erst zwanzig Jahre alt - und das sehen wir ihm deutlich an. Diese Elementarwesen sagen uns selber, wie lange es her ist, seit sie sich gebildet haben. Die Zeit wird zum Raum. Sie steht vor uns, indem die lebendigen Wesen ihre eigenen Zeitensignaturen zeigen. Die Zeit wird zur unmittelbaren Gegenwart für diese Verhältnisse.",
      "Wir lernen aus diesen unseren eigenen Elementarwesen, von denen wir im Leben schon umgeben waren, die wir im Tode erblicken, die Natur der elementarischen Welt überhaupt kennen und bereiten uns dadurch vor, auch solche Elementarwesen der Außenwelt zu verstehen im allmählichen Anschauen, die nicht wir geschaffen haben, sondern die ohne uns im geistigen Kosmos vorhanden sind. Durch unsere eigene elementare Schöpfung lernen wir die anderen kennen. Denken Sie sich einmal, wie unendlich verschieden eigentlich dieses Leben zwischen dem Tod und einer neuen Geburt ist von dem irdischen Leben. Das erste, was vorgeht nach der Geburt, ist, daß sich der Mensch noch nicht selber erkennt. Das, was er erlebt als ganz kleines Kind, das erleben die anderen mit ihm. Er ist geboren worden, und die anderen, seine Eltern, schauen dieses Geborene an. Nach dem Tode schaut man sich zunächst allerdings nicht selber an, aber sein Geborenes schaut man als eine Außenwelt an. Das, was draußen ist, was man geboren hat mit dem Augenblick des Todes, das schaut man selber an. So wahr der Mensch, wenn er durch die physische Geburt ins Dasein tritt, eine ihm unverständliche Außenwelt vor sich hat und",
      "eigentlich ein Wesen ist, welches nur für die anderen zappelt und weint und auch lacht, so ist man nach dem Tode, nach der Geburt für die geistige Welt, die für die physische Welt der Tod ist, zunächst so, daß man beginnt selber in der Umgebung zu sein, die n:an sich selber ge­boren hat, die man sich selber um sich herum aufrichtet, weil man sie geboren hat. Man hat die Welt geboren, während man, wenn man ins Physische geboren wird, von der Welt geboren wird. So ist es mit unseren Gedanken und mit dem, was aus den Gedanken wird mit der Erinnerung, dem Gedächtnisschatz.",
      "Anders ist es mit dem, was unserer Gefühis- und unserer Willens-sphäre angehört. Ich habe im ersten der Vorträge hier ausgeführt, daß das, was unserer Gefühis- und unserer Willenssphäre angehört, eigent­lich in seiner vollen Wesenheit noch nicht geboren ist in uns, daß Wille und Gefühl in gewisser Beziehung etwas darstellen, was nicht zu seinem vollen Ausgebären kommt.",
      "Das zeigt sich insbesondere nach dem Tode, denn Wille und Gefühl, so wie sie den physischen Leib durch­dringen, sind noch vorhanden nach dem Tode. So daß der Mensch also nach einiger Zeit, nachdem sich der Willensstern mit den Früchten seines letzten Erdenlebens gefernt hat, in einer Elementarwelt lebt, die seine Umgebung ist, und der er selbst sozusagen den Grundton gibt durch seine umgewandelten Erinnerungen.",
      "Es lebt der Mensch so in dieser Welt darinnen, die eigentlich er ist in dem Sinn, wie eben auseinandergesetzt worden ist, daß er weiß: Ja, aber dein Gefühl und dein Wille leben noch in dir, die haben jetzt eine Art von Erinnerung, eine Art von Zusammenhang mit dem nächsten Erdenleben. Das dauert durch Jahrzehnte.",
      "Wenn wir im Erdenleben stehen zwischen der Geburt und dem Tode, dann genießen wir und leiden wir, dann leben wir in Leidenschaften, entwickeln Willensimpulse dadurch, daß wir die fühlende und wollende Seele in unserem Leibe tragen. Aber niemals ist es so, daß durch den Leib all die Kräfte, die in Gefühl und Wille liegen, wirklich herauskommen können.",
      "Wenn man auch das höchste Alter erreicht hat, so stirbt man doch so, daß man hätte noch mehr genießen können, noch mehr leiden können, noch mehr Willens-impulse hätte entwickeln können. Das aber muß erst überwunden werden, was an Möglichkeiten des Fühlens und Wollens noch in der",
      "Seele ist. Solange das nicht vollständig überwunden ist, so lange haben wir einen Begierdenzusammenhang mit dem letzten Erdenleben. Wir schauen gleichsam auf dieses letzte Erdenleben zurück. Es ist, wie ich es öfter mit einem trivialen Wort genannt habe, eine Art Abgewöhnen von dem Zusammenhang mit dem physischen Erdenleben. In die Natur dieser Kraft, die man da zu überwinden hat, zu deren Über­windung man eigentlich jahrzehntelang braucht, in die Natur dieser Kraft dringt derjenige, der nur ein wenig wirklicher Geistesforscher wird, sehr bald ein, denn sie offenbart sich eigentlich verhältnismäßig leicht der Geistesforschung.",
      "Wenn wir jeden Tag aus den Erlebnissen des Tages heraus ein­schlafen, eine Zeit zubringen zwischen dem Einschlafen und dem Er­wachen, dann sind wir in unserem Seelisch-Geistigen außerhalb unseres Leibes. Wir kehren zurück, weil wir im Seelisch-Geistigen einen Trieb zu diesem Zurückkehren haben, weil wir wirklich nach unserem Leib begehren. Wir begehren durchaus nach unserem Leib, und wer das Aufwachen bewußt erleben kann, der weiß: Du willst aufwachen und du mußt aufwachen wollen. Es besteht eben eine Anziehungskraft im Geistig-Seelischen nach dem Leibe hin. Diese muß nach und nach abglimmen, muß ganz und gar überwunden werden. Das dauert Jahr­zehnte. Es ist die Zeit, in der wir nach und nach unseren Zusammen­hang mit dem letzten Erdenieben überwinden. Das macht es, daß wir in bezug auf die Erlebnisse nach dem Tode in der Zeit, die also ver­fließt, wie ich es eben geschildert habe, eigentlich alles auf dem Umweg durch unser Erdenieben erleben müssen.",
      "Ich bin jetzt in der Lage, nachdem die vorhergehenden Vorträge gehalten worden sind, Ihnen mancherlei Verhältnisse genauer zu schildern als sonst, wo man mehr im Überblick schildern mußte, denn es müssen für die genaue Schilderung immer erst die Begriffe herbei-getragen werden.",
      "Nehmen wir einmal an, wir haben einen Menschen auf der Erde zurückgelassen und sind selber durch die Pforte des Todes gegangen. Wir stehen also in der Zeit darinnen, wo wir uns die Fähigkeit an-geeignet haben, in die elementaren Wesenheiten hineinzuschauen und uns selber zu erfühlen, so daß wir wissen: Unsere Erdenfrüchte haben",
      "sich gefernt Aber wir hängen noch zusammen mit unserem letzten Erdenleben. Nehmen wir an, wir haben einen Menschen zurückge­lassen, wenn wir durch die Pforte des Todes geschritten sind, den wir sehr lieb gehabt haben.",
      "Ja, jetzt nach dem Tode kommen wir allmäh­lich dazu, indem wir uns von unseren eigenen elementaren Schöpfun­gen aus hineingewöhnen, die elementaren Wesenheiten von anderen zu schauen, jetzt können wir uns hineinfinden, Gedanken anderer als Elementarwesen zu schauen. Das lernen wir allmählich an unseren eigenen Elementarwesen, auch bei den andern Menschen, die wir zurückgelassen haben, zu sehen, was er denkt, was in seiner Seele an Gedanken lebt; wir sehen es.",
      "Denn es drückt sich in den Elementar-wesen aus, die uns in mächtigen Imaginationen vor die Seele treten. Wir können also in dieser Beziehung jetzt schon viel mehr Zusammen­hang haben mit dem Innerlichen des betreffenden Menschen, als wir mit ihm in der physischen Welt hatten.",
      "Denn während wir selber im physischen Leibe waren, konnten wir ja nicht auf das Gedankliche des andern hinschauen; jetzt können wir es. Aber wir brauchen gleichsam die Gefühlserinnerung - bitte auf das Wort wohl acht zu geben - die Gefühiserinnerung, den Gefühiszusammenhang mit unserem eigenen letzten Erdenleben.",
      "Wir müssen gleichsam so fühlen, wie wir im Leibe gefühlt haben, und dieses Gefühl muß in uns nachklingen, dann belebt sich das Verhältnis, das wir sonst nur wie zu einem Bilde haben wür­den, als das uns die Gedanken des andern erscheinen. Einen lebendigen Zusammenhang bekommen wir also auf dem Umwege durch unsere Gefühle.",
      "Und so ist es im Grunde genommen mit allem.",
      "Sie sehen, es ist ein Herausarbeiten aus einem Zustand, den man dadurch charakterisieren kann, daß man sagt: Es ist eine Zeit, in der wir die Kräfte noch aus unserem letzten Erdenleben beziehen müssen, um in lebendige Beziehungen zu kommen zu unserer geistigen Um­welt, wir müssen mit diesem Erdenleben noch zusammenhängen. Wir lieben die Seelen, die wir zurückgelassen haben, deren Seeleninhalt uns als Gedanken, als Elementarwesen erscheint, aber wir lieben sie, weil wir selber noch leben von der Liebe, die wir für sie während unseres Erdenlebens entwickelt haben. Es ist ja unangenehm, möchte ich fast sagen, solche Ausdrücke zu gebrauchen, aber einige von Ihnen",
      "werden mich verstehen, wenn ich sage: Das Erdenleben - also nicht das Gedankenieben - das Erdenleben als gefühlter und mit Willensimpuls durchsetzter Seeleninhalt, mit dem wir noch zusammenhängen, das wird wie eine Art elektrischer Umschalter der eigenen Individualität mit dem, was um uns herum geistig uns umwallt. Wie eine Art elektrischer Umschalter: wir nehmen alles wahr auf dem Umweg durch das letzte Erdenleben.",
      "Aber nur durch das, was im letzten Erdenleben Fühlen und Wollen war, nehmen wir wahr, was in der geistigen Welt zu uns gehört. Es ist wirklich jetzt so, daß wir uns in der Zeit weiter-lebend fühlen, wie eine Art Komet der Zeit.",
      "Unser Erdenleben ist noch da wie ein Kern, aber der Kern entwickelt in die nächste Zukunft hinein eine Art von Schweif, den wir durchleben. Wir hängen noch zusammen mit unserem Erdenleben, insoferne dieses erfüllt ist von Gefühl und Wille.",
      "In unserem Seeleninnern muß sich herausgebären aus diesem Erleben, wie ich es Ihnen geschildert habe, etwas, was jetzt nicht unmittelbar Gefühl und Wille ist. Denn die Seelenkräfte, die wir hier in der physischen Welt entwickeln, auch die Kraft des Fühlens, wie wir sie eben in der physischen Welt als Gefühlskraft haben, die Kraft des Willens, wie wir sie in der physischen Welt als Willenskraft haben, haben wir in dieser Form dadurch, daß wir eben im physischen Leibe leben.",
      "Wenn die Seele nun nicht mehr im physi­schen Leibe lebt, so muß sie andere Fähigkeiten entwickeln, die wäh­rend des physischen Lebens nur schlummern, sie muß, während noch der Nachkiang von Gefühl und Wille Jahre hindurch in ihr wirkt, aus diesem Zusammenhang das herausreifen, was sie nun für die geistige Welt auch in dieser Beziehung brauchen kann, Kräfte, die ich be­zeichnet habe, indem ich sagte: es ist etwas wie ein fühlendes Begehren oder ein begehrendes Fühlen. Von unserem Gefühl und unserem Willen wissen wir, die sitzen in unserer Seele darinnen.",
      "Doch von einem solchen Gefühl und Begehren, wie sie in unserer Seele sitzen, da haben wir nach dem Tode im Grunde genommen nichts, die müssen nach und nach abdämmern und abdumpfen; und das tun sie eben nach Jahren. Aber während dieses Abdämmerns und Abdumpfens muß sich von Gefühl und Wille etwas entwickeln, wovon wir nach dem Tode etwas haben.",
      "Unsere Gedanken leben draußen als Elementarwesen. Von einem Gefühl und einem Willen, wie sie in uns lebten, wurden wir nichts haben für diese Welt, die wir selber sind und die da d':außen ist. Wir müssen nach und nach einen Willen entwickeln - und den entwickeln wir auch -, der von uns ausströmt, der sich wie von uns ergießt und hinwallt und hinwogt dorthin, wo unsere lebendigen Gedanken sind. Diese durchdringt er, weil auf den Wogen des Willens das Gefühl schwimmt, das im physischen Leben nur in uns ist. Auf den Wogen des Willens schwimmt das Gefühl, da draußen wallt und wogt das Meer unseres Willens, und auf diesem schwimmt das Gefühl. Nämlich es schwimmt dann, wenn der Wille heranstößt an ein Gedanken­elementarwesen, dann geschieht durch diesen Zusammenstoß des Willens mit den Gedankenelementarwesen em Aufglimmen des Ge­fühis, und wir nehmen wahr als eine reale Wirklichkeit der geistigen Welt dieses Zurückgeworfenwerden unseres Willens.",
      "Ich will so sagen: Nehmen wir an, in der geistigen Außenwelt sei ein Elementarwesen. Wenn wir uns herausgearbeitet haben aus dem Zustand, den wir zuerst durchmachen müssen, dann brandet unser Wille, der jetzt aus uns herausgeht, zu dem Elementarwesen hin. Da, wo er heranstößt an das Elementarwesen, wird er zurückgeworfen: jetzt kommt er nicht als Wille zurück, jetzt kommt er als Gefühl zurück, welches in diesem Meer des Willens zurückflutet zu uns. Als Gefühl, welches in den Fluten des Willens zu uns zurückkommt, lebt unser eigenes Wesen ausgegossen in den Kosmos. Dadurch werden die Elementarwesen real für uns, dadurch nehmen wir allmählich immer mehr und mehr wahr, was wirklich da draußen an geistiger Außenwelt außer uns vorhanden ist.",
      "Aber noch eine Seelenkraft muß aus uns herauskommen, die noch in viel tieferen Schichten der Seele schlummert als das fühlende Wollen oder wollende Fühlen: die kreative Seelenkraft, die wie ein inneres Seelenlicht ist, die hinausleuchten muß über die geistige Welt, damit wir nicht nur auf den Gefühiswogen, die da zurückkommen in dem Meer unseres Willens, schwimmend schauen die lebend wehenden objektiven Gedankenwesen, sondern damit wir auch mit geistigem Licht diese geistige Welt durchleuchtet haben. Kreative geistige",
      "Leuchtekraft muß von unserer Seele hinausgehen in die geistige Welt. Die erwacht allmählich.",
      "Sehen Sie, meine lieben Freunde, von dem fühlenden Wollen und wollenden Fühlen haben wir, während wir im physischen Leibe leben, wenigstens, ich möchte sagen, das Geschwisterpaar Fühlen und Wollen in uns differenziert. Zu zweien haben wir das, während es eine Einheit ist, wenn wir durch die Pforte des Todes durchgegangen sind.",
      "Diese kreative Seelenkraft, die wir wie ein Seelenlicht ausstrahlen in den geistigen Raum hinaus, wenn ich den Ausdruck «Raum» hier gebrauchen darf, denn es ist eigentlich kein Raum, aber man muß diese Verhältnisse in gewisser Weise dadurch zum Verständnis bringen, daß man sich bildlich ausdrückt, dieses Seelerlicht schlummert tief unten in uns, weil es zusammenhängt mit dem, wovon wir im Leben nichts wissen dürfen und können. Ganz tief unten schlummert in uns wäh­rend des Lebens im physischen Plan, was dann als Licht wie erlöst ist und dann die geistige Welt erleuchtet und erhellt.",
      "Was da von uns ausstrahlt, muß umgewandelt und verwendet werden während unseres physischen Lebens dazu, daß unser Leib wirklich lebt und Bewußtsein in sich bergen kann. Aber ganz unterhalb der Schwelle des Bewußt­seins wirkt diese geistige Leuchtekraft in unserem physischen Leib als die Leben und Bewußtsein organisierende Kraft.",
      "Wir dürfen sie nicht ins Erdenbewußtsein hereinbringen, sonst würden wir unserem Leibe die Kraft rauben, die ihn durchorganisieren muß. Jetzt, wo wir keinen Leib zu versorgen haben, wird sie geistige Leuchtekraft und durch-strahlt und durchleuchtet und durchhellt und durchglitzert alles - die Worte bedeuten reale Wirklichkeiten.",
      "So arbeiten wir uns allmählich hinein, in der geistigen Welt ebenso zu Haus zu werden, sie als eine Realität zu erleben, wie wir hier die physische Welt als eine Realität erleben. Wir arbeiten uns allmählich hinein, wirklich auch die toten Menschenseelen, insofern sie real leben in der geistigen Welt, als unsere Genossen in der geistigen Welt zu haben. Wir leben unter den Seelen, wie wir hier im physischen Leibe unter Leibern leben. Und indem man immer mehr und mehr vordringt in den eigentlichen inneren Geist der Geisteswissenschaft, wird die Behauptung, die jemand etwa tun wollte, daß wir nach dem Tode",
      "nicht mit all den Menschen, mit denen wir gelebt haben, wiederum zusammenkommen würden, diese Behauptung wird für den, der tiefer eindringt in die Sache, so töricht, wie für den physischen Plan die Behauptung töricht wäre, daß, wenn wir durch die Geburt herein-treten in diese Erde, wir keinen Menschen darin finden. Die Menschen sind eben um uns herum. Genau dasselbe ist es für den Kenner des geistigen Lebens, wie wenn jemand sagen wollte: Das Kind lebt sich in die Welt herein, aber Menschen sieht es nicht. Das ist ein offenbarer Unsinn. Ebenso ist es ein Unsinn, wenn gesagt wird: Wir finden, wenn wir uns in die geistige Welt hineinleben, nicht all die Seelen wieder, mit denen wir in Zusammenhang gestanden haben, und wir finden nicht Wesenheiten der höheren Hierarchien, die wir stufenweise kennenlernen, wie hier auf der Erde die Mineralien, Pflanzen und Tiere. Das aber ist der Unterschied, daß wir hier in der physischen Welt wissen: Indem wir die Dinge sehen, hören, kommt die Möglichkeit, sie zu sehen und zu hören durch die Sinne, von der Außenwelt. In der geistigen Welt, wissen wir, kommt diese Möglichkeit von uns, indem das, was wir Seelenlicht, Seelenleuchte nennen können, von unserer Seele ausstrahlt und die Dinge erhellt, erleuchtet und durch­leuchtet.",
      "So leben wir in die Zeit hinein, die man die erste Hälfte des Lebens zwischen dem Tod und einer neuen Geburt nennen kann. Indem wir in diese Zeit hineinleben, machen wir die zwei Zustände durch, von denen ich auch im öffentlichen Vortrag gesprochen habe, eine Zeit, die eben nach Jahren dauert, in der wir so, wie es geschildert worden ist, durch die Ausstrahlung unserer Seelenleuchtekraft mit der geisti­gen Welt zusammenhängen, in der wir also das schauen, was an Geistern und Seelen um uns herum ist. Das dämmert dann ab, wir fühlen: Du kannst jetzt immer weniger deine Seelenleuchtekraft ent­wickeln, du mußt es dämmeriger und immer finsterer werden lassen im geistigen Sinn. Dadurch siehst du immer weniger die geistigen Wesenheiten. Das wird immer mehr und mehr so, daß man abwechselt mit einer Zeit, in der man sich sagt: Da, um dich sind die Wesenheiten, aber du wirst immer einsamer, du hast nur deinen eigenen Seelen-inhalt, und dieser Seeleninhalt wird in dem Maße reicher, in dem man",
      "aufhört, da draußen die Wesen beleuchten zu können. Es gibt Zeiten der geistigen Geselligkeit und Zeiten der geistigen Einsamkeit, in der ein Nacherleben dessen ist, was man in den Zeiten der geistigen Geselligkeiten erlebt hat, aber alles dann in der Seele: das schwingt ab und wechselt ab. So leben wir uns hinein in die geistige Welt: geistige Geselligkeit - geistige Einsamkeit. In den Zeiten geistiger Einsamkeit, da wissen wir: Was du sonst in der geistigen Welt rings um dich herum erlebt hast, das war ja alles da, von all dem weißt du, aber jetzt sind nur die Nachklänge davon in deinem Innern. Man könnte sagen:",
      "Erinnerungen sind es in den Zeiten geistiger Einsamkeit. Allein, wenn man sölche Worte gebraucht, trifft man die Sache nicht richtig. Ich will daher versuchen, es Ihnen noch von einer anderen Seite her zu schildern.",
      "Es ist nicht so, als wenn man in der geistigen Dunkelheit, in der man nichts Geselliges hat, sich erinnern würde an das, was man früher in der geistigen Welt erlebt hat, sondern als wenn man das in jedem Augenblick frisch hervorbringen müßte: es ist ein fortwährendes inneres Schaffen. Aber man weiß: Während da draußen die Außenwelt ist, mußt du mit dir selber sein und schaffen und schaffen. Was du schaffst, ist die Welt, die da draußen dich umbrandet jenseits der Ufer deines eigenen Wesens.",
      "Aber indem man so in der ersten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt weiterlebt und sich der Mitte der Zeit zwischen dem Tod und einer neuen Geburt nähert, fühlt man das einsame Leben immer reicher werden und die Ausblicke auf die geistige Umgebung gleichsam kürzer und dämmeriger werden, bis die Zeit herankommt in der Mitte zwischen dem Tod und einer neuen Geburt, die ich versucht habe, in meinem letzten Mysterienspiel « Der Seelen Erwachen» als die Weltenmitternacht darzustellen, wo der Mensch das stärkste Leben in seinem Innern hat, aber nicht mehr die kreative Seelenkraft, um seine geistige Umgebung zu beleuchten, wo sozusagen unendliche Welten aus unserem Innern uns innerlich geistig erfüllen können, aber wir von anderem Sein als unserem eigenen Sein nichts wissen können. Das ist die Mitte in den Erlebnissen zwischen dem Tod und einer neuen Geburt: die Weltenmitternacht.",
      "Nun beginnt die Zeit, in der im Menschen die Sehnsucht zu einer positiven schöpferischen Kraft wird. Denn obzwar wir ein Unend­liches als ein inneres Leben haben, erwacht in uns die Sehnsucht, eine Außenwelt wieder zu haben. So verschieden sind die Verhältnisse der geistigen Welt von denen der physischen Welt, daß, während die Sehnsucht in der physischen Welt die passivste Kraft ist - wenn wir etwas haben, nach dem wir uns sehnen, so ist es dieses Etwas, was uns bestimmt -, ist das Gegenteil in der geistigen Welt der Fall. Da wird die Sehnsucht eine schöpferische Kraft, sie verwandelt sich in das, was jetzt als eine neue Art von Seelenlicht uns eine Außenwelt geben kann, eine Außenwelt, die aber doch eine Innenwelt ist, indem sich uns der Blick eröffnet auf unsere früheren Erdeninkarnationen. Die liegen jetzt beleuchtet von dem aus unserer Sehnsucht heraus geborenen Licht, vor uns ausgebreitet. Es gibt im geistigen Kosmos eine Kraft, die aus der Sehnsucht heraus diesen Rückblick uns erleuchten und erleben lassen kann. Dazu ist aber in unserem gegenwärtigen Zeitenzyklus eines notwendig.",
      "Ich habe Ihnen gesagt: In dieser ganzen Zeit der ersten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt wechseln wir ab zwischen Innenleben und Außenleben, zwischen Einsamkeit und geistiger Geselligkeit. Die Verhältnisse der geistigen Welt sind zu­nächst so, daß jedesmal, wenn wir in dieser geistigen Welt wieder in unsere Einsamkeit zurückkommen, wir in unserer inneren Tätigkeit immer wiederum das vor unsere Seele bringen, was wir in der äußeren Welt durchlebt haben. Dadurch ist ein Bewußtsein vorhanden, das sich ausbreitet wie mit Schwingen der Unendlichkeit über die ganze geistige Welt. Die Schwingen ziehen sich wiederum zusammen in der Einsamkeit.",
      "Aber eines müssen wir uns erhalten, das da vorhanden bleiben muß, gleichgültig, ob wir uns ausbreiten in die große geistige Welt oder uns zurückziehen. Bevor das Mysterium von Golgatha geschah, war es möglich, durch die Kräfte, durch die der Mensch mit den Urzeiten zusammengehangen hat, den festen Ichzusammenhalt zu haben, nicht zu verlieren diesen Ichzusammenhalt, das heißt, an das verflossene Erdenleben das eine als Erinnerung vollständig deutlich zurück zu",
      "behalten: man war auf der Erde in diesem Leben ein Ich. Das muß sich durchdehnen durch die Zeiten der Einsamkeit und der Gesellig­keit. Vor dem Mysterium von Golgatha war durch die vererbten Kräfte dafür gesorgt. Jetzt kann dafür nur dadurch gesorgt wer­den, daß mit dem, was wir als unser Erdengut von uns losgelöst haben, was wir sich fernend empfunden haben gleich beim Verlassen des physischen Leibes, daß mit diesem eine Seelenerfüllung verbunden bleibt, die Seelenerfüllung, die wir dadurch haben können, daß der Christus ausgeflossen ist in die Erdenaura. Dieses Durchdrungen-sein mit dem Christus-Substantiellen, das ist es, was uns in der Gegenwart bei dem Übergang aus dem physischen Leben in den Tod die Möglichkeit gibt, bis zur Weltenmitternacht hin die Erinnerung an unser Ich zu bewahren trotz alles Ausbreitens in die geistige Welt, trotz alles Zusammenziehens in die Einsamkeit. Bis dahin reicht der Impuls, der von der Christuskraft ausgeht, so daß wir uns selber nicht verlieren. Dann aber muß aus der Sehnsucht heraus eine neue geistige Kraft unsere Sehnsucht zu einem neuen Licht anfachen. Diese Kraft ist nur im Geiste, im geistigen Leben vorhanden.",
      "Meine lieben Freunde, es gibt in der physischen Welt die Natur und das diese Natur durchdringende Göttliche, aus dem wir in die physi­sche Welt hineingeboren werden. Es gibt den Christusimpuls, der in der Erdenaura, das heißt in der Aura der physischen Natur, vorhanden ist. Aber die Kraft, die in der Weltenmitternacht an uns herankommt, um unsere Sehnsucht leuchtend zu machen über unsere ganze Ver­gangenheit hin, die gibt es nur in der geistigen Welt, die gibt es nur da, wo keine Leiber leben können. Und hat uns der Christusimpuls bis in die Weltenmitternacht gebracht, und ist die Weitenmitternacht in geistiger Einsamkeit von der Seele erlebt worden, weil das Seelen-licht jetzt nicht erstrahlen kann von uns selber aus, ist Weltenfinsternis eingetreten, hat uns der Christus bis dahin geführt, so tritt jetzt aus der Weltenmitternacht, aus unserer Sehnsucht, ein Geistiges heraus, erschaffend ein neues Weltenlicht, über unsere eigene Wesenheit hin ein Leuchten verbreitend, durch das wir uns neu ergreifen im Weltendasein, durch das wir neu erwachen im Weltendasein. Den Geist der geistigen Welt, der uns erweckt, wir lernen ihn kennen, indem aus",
      "der Weltenmitternacht ein neues Licht hervorleuchtet, über unsere verflossene Menschheit erstrahlend. In dem Christus sind wir gestor­ben - durch den Geist, durch den leiblosen Geist, der mit einem technischen Wort der Heilige Geist genannt wird, das heißt, der ohne den Leib Lebende, denn das ist mit dem Wort «hellig» gemeint, ohne die Schwächen eines im Leibe lebenden Geistes, durch diesen Geist werden wir in unserer Wesenheit wiedererweckt aus der Welten-mitternacht heraus.",
      "Durch den Heiligen Geist werden wir also in der Weltenmitternacht erweckt.",
      "Per spiritum sanetum reviviscimus."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Es wird mir nun obliegen, von den Vorgängen zwischen dem Tod und einer neuen Geburt noch einmal zu sprechen, aber mit Benutzung derjenigen Vorstellungen, die wir in den vier letzten Vorträgen haben gewinnen können.",
        "Es wird natürlich dadurch, daß es mit einer gewissen Kürze wird behandelt werden müssen, manches von dem umfassenden Thema nur angedeutet werden können, es wird man­ches, was vielleicht aus der bildlichen Darstellung nicht folgt, herausgearbeitet werden müssen.",
        "Aber das, was unsere anthropo­sophischen Freunde heute nicht schon vollständig finden werden, wird dann im Laufe der weiteren Erkenntnis der Geisteswissenschaft sich zeigen."
      ],
      [
        "Wenn der Mensch durch die Pforte des Todes getreten ist, so hat er seinen physischen Leib abgelegt, der physische Leib ist den Ele­menten der Erde übergeben.",
        "Mit anderen Worten könnte auch über ihn gesagt werden: Der physische Leib hat sich herausgehoben aus den Kräften und Gesetzen, die ihn zwischen der Geburt und dem Tode vom eigentlichen Menschen heraus durchdringen, und die an­dere Gesetze sind als die bloß chemischen und physikalischen Gesetze, denen er dann nach dem Tode als physischer Leib verfällt.",
        "Vom Ge­sichtspunkt der physischen Welt aus hat der Mensch ja selbstver­ständlich die Anschauung: Von der menschlichen Wesenheit ist zurückgeblieben auf dem physischen Plane das, was diesem physischen Plane angehört.",
        "Es wird dieses dem physischen Plane Angehörige nun auch dem physischen Plane übergeben.",
        "Für den Menschen selbst aber und für alle Auffassung der geistigen Welt kommt der Gesichts­punkt in Betracht, den der Tote, der Mensch, der durch die Pforte des Todes geschritten ist, hat einnehmen müssen.",
        "Für ihn bedeutet das Verlassen des physischen Leibes einen inneren Vorgang, einen Seelenvorgang, für die Hinterbliebenen ist das, was mit dem physi­schen Leibe nach dem Tode geschieht, ein äußerer Vorgang.",
        "Das Innere des Menschen, das Menschlich-Seelenhafte des verstorbenen"
      ],
      [
        "Menschen drückt sich ja innerhalb dessen, was als sterblicher Über­rest zurückgeblieben ist, nicht mehr aus.",
        "Für den Menschen selbst aber, der durch die Pforte des Todes gegangen ist, ist dennoch etwas verbunden mit dem Verlassen des Leibes.",
        "Es bedeutet ein innetes Seelenerlebnis: Du bist aus deinem physischen Leibe herausgegangen und lässest diesen physischen Leib zurück."
      ],
      [
        "Es ist außerordentlich schwierig, ich möchte sagen, vom Stand­punkt des physischen Planes aus dieses, was da im Innern der Seele des Menschen vorgeht, wirklich sachgemäß zu schildern.",
        "Denn es ist ein innerer Vorgang, der im Grunde etwas ungeheuer Umfassendes, etwas ungeheuer Bedeutsames hat."
      ],
      [
        "Es ist ein innerer Vorgang, der ja im Grunde kurz dauert, aber von einer für das gesamte menschliche Leben universalen Bedeutung ist.",
        "Nun, wenn man den Vorstellungs­inhalt dessen schildern möchte, was da mit der Seele vorgeht, diesen Vorstellungsinhalt, den man natürlich heute in einem öffentlichen Vortrag noch nicht berühren kann, denn er würde die Öffentlichkeit zu seht frappieren - vielleicht kommt aber auch dazu die Zeit - wenn man den äußeren, also jetzt geistig äußerlichen Vorstellungsvorgang schildern wollte, mit dem sozusagen der Lebensweg beginnt, der zwischen dem Tod und einer neuen Geburt verläuft, so könnte man sagen, der durch die Pforte des Todes Geschrittene hat zunächst das Gefühl: Du bist jetzt in einem ganz anderen Verhältnisse zur Welt als du vorher warst, und das ganze frühere Verhältnis, das du zur Welt hattest, ist im Grunde genommen umgekehrt, radikal umgekehrt."
      ],
      [
        "Man müßte eigentlich in der folgenden Weise schildern, wenn man das, was da vorstellungsmäßig erlebt wird, schildern wollte.",
        "Man müßte sagen: Der Mensch hat bis zu seinem Tode auf der Erde gelebt, er ist gewohnt gewesen in dieser Zeit auf der festen, materiellen Erde zu stehen, auf dieser materiellen Erde die Wesen des mineralischen, pflanzlichen, tierischen Reiches, Berge, Flüsse, Wolken, Sterne, Sonne und Mond zu sehen, und ist gewohnt worden, durch seinen eigenen Gesichtspunkt und durch seine im physischen Leib vorhandenen Fähigkeiten, sich dieses Ganze so vorzustellen, wie man es sich ja doch vorstellt, trotzdem man heute durch den Kopernikanismus weiß, daß es im Grunde ein Scheinbild ist: da oben ist das blaue Himmelsgewölbe"
      ],
      [
        "wie eine Himmelsschale, da sind die Sterne darauf, darüber gehen Sonne und Mond und so weiter, man selber ist wie in dieser Schale, in dieser Hohlkugel, im Innern da drinnen in der Mitte auf der Erde mit dem, was einem die Erde für die Wahrnehmung zeigt."
      ],
      [
        "Es kommt uns jetzt nicht darauf an, daß das ein Scheinbild ist, daß wir selber nur durch die Beschränktheit unserer Fähigkeiten uns diesen blauen Umkreis bilden, sondern darauf, daß wir ja gar nicht anders können als das zu sehen.",
        "Wir sehen eben das, was nur durch die Beschränktheit unserer Fähigkeiten so ist, sehen eben eine blaue Kugel als Firmament über uns gebildet."
      ],
      [
        "Wenn nun der Mensch durch die Pforte des Todes gegangen ist, so ist das erste, daß er die Vor­stellung seiner Seele ausbilden muß: Du bist jetzt außerhalb dieser blauen Kugel, in der du warst.",
        "Du siehst sie von außen an, aber so, als ob sie zu einem Stern zusammengeschrumpft wäre."
      ],
      [
        "Man hat zu­nächst kein Bewußtsein von der Sternenwelt, in die man sich eigent­lich ausbreitet, sondern man hat zunächst nur ein Bewußtsein von dem, was man verlassen hat: daß man seine Bewußtseinssphäre, die man gehabt hat im physischen Leibe, verlassen hat, daß man das ver­lassen hat, bis wohin einen die menschlichen Fähigkeiten, die im physischen Leibe ausgebildet sind, haben schauen lassen.",
        "Es ist wirk­lich, aber geistig, etwas Ähnliches vorgegangen, wie es vorgehen müßte, wenn mit bewußtem Erleben ein Küchlein, das in der Eier­schale drinnen ist, diese zerbricht und nachher die zerbrochene Ei­schale, die es bisher umschlossen hat, seine bisherige Welt, von außen statt von innen ansieht."
      ],
      [
        "Natürlich ist diese Vorstellung wiederum Maja, die da durch die menschliche Seele zieht, aber eine notwendige Maja.",
        "Wie gesagt: zusammengeschrumpft wie zu einem Sterne ist das, was uns vorher den Inhalt unseres Bewußtseins gab, nur daß sich, von diesem Sterne ausgehend, dasjenige ausbreitet, was man nennen könnte: erstrahlende kosmische Weisheit."
      ],
      [
        "Diese erstrahlende kosmische Weisheit ist dasselbe, welches ich auch gestern im letzten Vortrag behandelt habe, und von dem ich gesagt habe, daß wir es in Fülle haben.",
        "Das glimmt und glitzert uns entgegen wie von einem feurigen Stern.",
        "Jetzt ist es nicht blau wie das Firmament, sondern jetzt ist es feurig, rötlich erglimmend, und davon"
      ],
      [
        "ausstrahlend in den Raum die Fülle von Weisheit, die uns aber zuerst zeigt - sie ist in sich ganz beweglich - das, was man ein Erinnerungs­tableau unseres letzten Erdenlebens nennen könnte.",
        "All die Vorgänge, die wir mit unserem inneren Seelenerleben durchmessen haben zwi­schen der Geburt und dem Tode, wo wir bewußt dabei waren, treten vor unsere Seele hin, aber so, daß wir wissen: Du siehst das alles, weil der Stern, der da vor dir aufglänzt, der Hintergrund ist, der durch seine innere Tätigkeit bewirkt, daß du das alles sehen kannst, was sich als ein Erinnerungstableau ausbreitet."
      ],
      [
        "Das ist so mehr vom Stand-punkt der Imagination aus gesprochen.",
        "Vom Standpunkt der Inner­lichkeit gesprochen ist das Erlebnis etwa dieses, daß derjenige, der durch die Pforte des Todes gegangen ist, nunmehr ganz erfüllt ist von dem Gedanken: Ja, du hast deinen Leib verlassen."
      ],
      [
        "Jetzt, in der geisti­gen Welt, ist dieser Leib lauter Wille.",
        "Ein Willensstern, ein Stern, dessen Substanz Wille ist, das ist dein Leib.",
        "Und dieser Wille erglüht in Wärme und strahlt dir in den Weltenweiten, in die du dich jetzt selber ergossen hast, dein eigenes Leben zwischen der Geburt und dem Tode wie ein großes Tableau zurück."
      ],
      [
        "Und du verdankst dem Umstande, daß du innen verweilen konntest in diesem Stern, daß du alles das aus der Welt ziehen und saugen konntest, was du auf dem physischen Plan aus der Welt eben gezogen und gesaugt hast.",
        "Denn dieser Stern, dieser Willensstern, der jetzt den Hintergrund bildet, das ist das Geistige deines physischen Leibes, dieser Willensstern ist der Geist, der deinen physischen Leib durchtränkt und durchkraftet."
      ],
      [
        "Das, was dir als Weisheit erstrahlt, das ist die Tätigkeit, die Beweglichkeit deines Ätherleibes."
      ],
      [
        "Es vergeht die Zeit, das ist ja auch schon im öffentlichen Vortrag charakterisiert worden, die eigentlich nur nach Tagen dauert, wo man den Eindruck hat: das Leben spielt sich ab wie ein Erinnerungs­tableau.",
        "Unsere Gedanken, die zu unseren Erinnerungen während des Lebens auf der Erde geworden sind, rollen da gleichsam ab in diesem Erinnerungstableau, die treten noch einmal vor unsere Seele hin.",
        "Und wir können es so lange aufrecht erhalten, als wir die Kraft haben, unter normalen Verhältnissen uns im physischen Leibe wach zu er­halten.",
        "Es kommt ja nicht darauf an, wie lange wir einmal im Leben"
      ],
      [
        "wach geblieben sind in abnormen Verhältnissen, es kommt darauf an, welche Kräfte wir in uns haben, um eben uns wach zu erhalten.",
        "Diese sind bei dem einen so, daß er kaum eine Nacht durchwachen kann, ohne daß ihn Müdigkeit überkommt, bei dem anderen, daß er es länger aushalten kann, ohne müde zu werden.",
        "Von dem Maße dieser Kräfte ist es abhängig, wie lange der Mensch braucht, um mit diesem Erinnerungstableau fertig zu werden.",
        "Aber man hat auch das ganz deutliche innere Bewußtsein, daß dadurch, daß der Willensstern im Hintergrunde ist, in diesem Erinnerungstableau dasjenige ist, was wir uns im letzten Erdenleben errungen haben.",
        "Daß darin das ist, um was wir reifer geworden sind, was wir sozusagen durch den Tod als ein Mehr hinausgetragen haben gegenüber dem, was wir beim Eintritt in unsere Geburt als ein Geringeres gehabt haben.",
        "Dieses, was wir wie eine Frucht des letzten Lebens bezeichnen können, das fühlen wir so, als wenn es nicht bleiben würde, wie es war während des Erinnerungs­tableaus, sondern wie wenn es sich fernte, wie wenn es fortginge, wie wenn es in der Zeiten Zukunft hineinginge und in der Zeiten Zukunft entschwände."
      ],
      [
        "Ich werde heute vorzugsweise davon reden, wie es sich mit dem Leben zwischen dem Tod und einer neuen Geburt verhält bei solchen Menschen, die eine normale Lebensdauer erreicht haben und in normalen Verhältnissen gestorben sind.",
        "Für Ausnahmefälle soll dann morgen das Nähere gesagt werden."
      ],
      [
        "Also es fernt sich unsere Lebensfrucht, wenn wir eine solche er­langt haben, und wir wissen in der Seele: diese Frucht ist irgendwie vorhanden, aber wir sind hinter ihr zurückgeblieben.",
        "Man hat das Bewußtsein, man ist an einem früheren Zeitpunkt verblieben, die Lebensfrucht zieht schnell fort, so daß sie früher ankommt an einem späteren Zeitpunkt, und wir müssen ihr nachziehen, dieser Lebens-frucht.",
        "Das, was ich jetzt gesagt habe, dieses innere Erlebnis, daß die Lebensfrucht im Weltenall weilt, vorhanden ist, das müssen wir uns so recht vorstellen, denn das ist es, was den Grund bildet für unser Bewußtsein, für den Beginn unseres Bewußtseins nach dem Tode.",
        "Unser Bewußtsein muß ja sozusagen immer durch etwas angeregt werden.",
        "Wenn wir des Morgens aufwachen, so wird unser Bewußtsein"
      ],
      [
        "neuerdings angefacht - während wir beim Schlaf bewußtlos sind - durch das Eintauchen in den physischen Leib und dadurch, daß uns die äußeren Dinge gegenübertreten, dadurch daß etwas von außen wirkt.",
        "In den Verhältnissen unmittelbar nach dem Tode wird dieses Bewußt­sein angefacht durch das innere Erfühlen und Erleben dessen, was die Frucht unseres letzten Lebens ist, was wir uns errungen, erobert haben.",
        "Das ist vorhanden, aber außer uns vorhanden.",
        "Durch dieses Erfühlen und Erleben unseres innersten irdischen Wesens außer uns haben wir die erste Entzündung unseres Bewußtseins nach dem Tode, daran belebt sich dieses Bewußtsein."
      ],
      [
        "Dann beginnt die Zeit, in welcher es notwendig ist, daß wir Seelen-kräfte entwickeln, welche während des Lebens auf dem physischen Plane eigentlich unentwickelt bleiben müssen, weil sie alle dazu ver­wendet werden, den physischen Leib und das, was zu ihm gehört, das ganze physische Leben, durchzuorganisieren, Seelenkräfte, die während des physischen Lebens in etwas anderes verwandelt sein müssen.",
        "Diese Kräfte müssen allmählich erwachen nach dem Tode."
      ],
      [
        "Schon in den Tagen, während welcher wir das Erinnerungstableau erleben, haben wir ein solches Erwachen von Seelenfähigkeiten zu verzeichnen.",
        "Wenn das Erinnerungstableau nach und nach abflutet und abdämmert, so geschieht das eigentlich dadurch, daß wir während dieser Tage schon diejenigen Kräfte entwickeln, welche der Erinne­rungsfähigkeit zwar zugrunde liegen, aber nicht bewußt werden während des physischen Lebens, und zwar deshalb nicht, weil wir während dieses physischen Lebens sie gerade umwandeln müssen, um Erinnerungen bilden zu können."
      ],
      [
        "Die letzte große Erinnerung, die wir nach dem Tode in Form des Tableaus haben, die muß erst ab-fluten, die muß nach und nach verdämmern, dann entwickelt sich aus der Verdämmerung heraus das, was wir bewußt nicht haben durften vor dem Tode.",
        "Denn hätten wir es bewußt gehabt vor dem Tode, so hätten sich niemals in uns die Erinnerungskräfte bilden können."
      ],
      [
        "Um­gewandelt in diese Fähigkeit uns zu erinnern haben sich die Kräfte, die sich jetzt in der Seele während des Abdämmerns der Erinnerung des Lebenstableaus heraus entwickeln.",
        "Umgesetzt in die Erinnerungs­kraft haben sich diese vor dem Tode, und jetzt kommen sie heraus,"
      ],
      [
        "indem die Möglichkeit, sich in gewöhnlicher Weise an irdische Ge­danken zu erinnern, überwunden wird.",
        "Diese gleichsam ins Geistige umgewandelte Gedächtniskraft erwacht als eine erste geistig-seelische Kraft in uns, die nach dem Tode aus der menschlichen Seele so heraus­kommt, wie die Seelenkräfte beim heranwachsenden Kinde in den ersten Lebenswochen herauskommen.",
        "Indern diese Seelenkraft heran­wächst, zeigt sich uns eben, daß hinter den Gedanken, die, während wir auf dem physischen Plane waren, nur Schattenbilder waren, Lebendiges steckt, daß ein Leben und Weben in der Gedankenwelt ist.",
        "Wir werden gewahr, daß das, was wir innerhalb des physischen Leibes als unser Gedankentableau haben, eben nur ein Schattenbild ist, daß es in Wahrheit eine Summe, eine Ausbreitung von Elementarwesen ist.",
        "Wir sehen gleichsam unsere Erinnerungen abglimmen und sehen dafür aus dem allgemeinen Weisheitskosmos heraus eine ganze Anzahl von Elementarwesen erwachen."
      ],
      [
        "Sie könnten fragen, meine lieben Freunde: Ja, geht uns denn das nicht ab nach dem Tode, daß wir gerade die Erinnerungskraft über­winden und etwas anderes dann haben?",
        "Es geht uns nicht ab, denn wir haben reichlichen Ersatz dafür nach dem Tode.",
        "Statt daß wir uns wie im Leben an unsere Gedanken erinnern, merken wir nach dem Tode, daß diese Gedanken, die wir als Gedächtnisgedanken im Leben hatten, für uns sich nur so ausnehmen wie Erinnerungen.",
        "Oh, dieser Gedächtnisschatz während des Lebens, er ist etwas ganz anderes als ein bloßer Gedächtnisschatz!",
        "Sind wir aus dem physischen Leibe heraus, dann sehen wir diesen ganzen Gedächtnisschatz als lebendige Gegenwart, dann ist er da.",
        "Jeder Gedanke lebt als ein Elementarwesen.",
        "Wir wissen jetzt: Du hast gedacht während deines physischen Lebens, dir sind deine Gedanken erschienen.",
        "Aber während du in dem Wahne warst, du bildetest dir Gedanken, hast du lauter Elementarwesen ge­schaffen.",
        "Das ist das Neue, was du zum ganzen Kosmos hinzugefügt hast.",
        "Jetzt ist etwas da, was in den Geist hinein von dir geboren worden ist, jetzt taucht vor dir auf, was deine Gedanken in Wirklich­keit waren.",
        "Man lernt zunächst in unmittelbarer Anschauung er­kennen, was Elementarwesen sind, weil man diejenigen Elementar-wesen zuerst erkennen lernt, die man selber geschaffen hat."
      ],
      [
        "ist der bedeutungsvolle Eindruck der ersten Zeit nach dem Tode, daß man das Erinnerungstableau hat.",
        "Aber dieses fängt an zu leben, richtig zu leben, und indem es anfängt zu leben, verwandelt es sich in lauter Elementarwesen.",
        "Jetzt zeigt es sozusagen sein wahres Antlitz, und darin besteht sein Verschwinden, daß es etwas ganz anderes wird.",
        "Wir brauchen, wenn wir zum Beispiel mit sechzig oder achtzig Jahren gestorben sind, jetzt nicht mehr für irgend einen Gedanken, den wir etwa im zwanzigsten Jahre unseres Lebens gehabt haben, Erinnerungskraft, denn er ist da als lebendiges Elementar-wesen, er hat gewartet und wir brauchen uns nicht an ihn zu erinnern.",
        "Denn wären wir zum Beispiel in unserem vierzigsten Lebensjahre gestorben, so wäre der Gedanke erst zwanzig Jahre alt - und das sehen wir ihm deutlich an.",
        "Diese Elementarwesen sagen uns selber, wie lange es her ist, seit sie sich gebildet haben.",
        "Die Zeit wird zum Raum.",
        "Sie steht vor uns, indem die lebendigen Wesen ihre eigenen Zeitensignaturen zeigen.",
        "Die Zeit wird zur unmittelbaren Gegenwart für diese Verhältnisse."
      ],
      [
        "Wir lernen aus diesen unseren eigenen Elementarwesen, von denen wir im Leben schon umgeben waren, die wir im Tode erblicken, die Natur der elementarischen Welt überhaupt kennen und bereiten uns dadurch vor, auch solche Elementarwesen der Außenwelt zu verstehen im allmählichen Anschauen, die nicht wir geschaffen haben, sondern die ohne uns im geistigen Kosmos vorhanden sind.",
        "Durch unsere eigene elementare Schöpfung lernen wir die anderen kennen.",
        "Denken Sie sich einmal, wie unendlich verschieden eigentlich dieses Leben zwischen dem Tod und einer neuen Geburt ist von dem irdischen Leben.",
        "Das erste, was vorgeht nach der Geburt, ist, daß sich der Mensch noch nicht selber erkennt.",
        "Das, was er erlebt als ganz kleines Kind, das erleben die anderen mit ihm.",
        "Er ist geboren worden, und die anderen, seine Eltern, schauen dieses Geborene an.",
        "Nach dem Tode schaut man sich zunächst allerdings nicht selber an, aber sein Geborenes schaut man als eine Außenwelt an.",
        "Das, was draußen ist, was man geboren hat mit dem Augenblick des Todes, das schaut man selber an.",
        "So wahr der Mensch, wenn er durch die physische Geburt ins Dasein tritt, eine ihm unverständliche Außenwelt vor sich hat und"
      ],
      [
        "eigentlich ein Wesen ist, welches nur für die anderen zappelt und weint und auch lacht, so ist man nach dem Tode, nach der Geburt für die geistige Welt, die für die physische Welt der Tod ist, zunächst so, daß man beginnt selber in der Umgebung zu sein, die n:an sich selber ge­boren hat, die man sich selber um sich herum aufrichtet, weil man sie geboren hat.",
        "Man hat die Welt geboren, während man, wenn man ins Physische geboren wird, von der Welt geboren wird.",
        "So ist es mit unseren Gedanken und mit dem, was aus den Gedanken wird mit der Erinnerung, dem Gedächtnisschatz."
      ],
      [
        "Anders ist es mit dem, was unserer Gefühis- und unserer Willens-sphäre angehört.",
        "Ich habe im ersten der Vorträge hier ausgeführt, daß das, was unserer Gefühis- und unserer Willenssphäre angehört, eigent­lich in seiner vollen Wesenheit noch nicht geboren ist in uns, daß Wille und Gefühl in gewisser Beziehung etwas darstellen, was nicht zu seinem vollen Ausgebären kommt."
      ],
      [
        "Das zeigt sich insbesondere nach dem Tode, denn Wille und Gefühl, so wie sie den physischen Leib durch­dringen, sind noch vorhanden nach dem Tode.",
        "So daß der Mensch also nach einiger Zeit, nachdem sich der Willensstern mit den Früchten seines letzten Erdenlebens gefernt hat, in einer Elementarwelt lebt, die seine Umgebung ist, und der er selbst sozusagen den Grundton gibt durch seine umgewandelten Erinnerungen."
      ],
      [
        "Es lebt der Mensch so in dieser Welt darinnen, die eigentlich er ist in dem Sinn, wie eben auseinandergesetzt worden ist, daß er weiß: Ja, aber dein Gefühl und dein Wille leben noch in dir, die haben jetzt eine Art von Erinnerung, eine Art von Zusammenhang mit dem nächsten Erdenleben.",
        "Das dauert durch Jahrzehnte."
      ],
      [
        "Wenn wir im Erdenleben stehen zwischen der Geburt und dem Tode, dann genießen wir und leiden wir, dann leben wir in Leidenschaften, entwickeln Willensimpulse dadurch, daß wir die fühlende und wollende Seele in unserem Leibe tragen.",
        "Aber niemals ist es so, daß durch den Leib all die Kräfte, die in Gefühl und Wille liegen, wirklich herauskommen können."
      ],
      [
        "Wenn man auch das höchste Alter erreicht hat, so stirbt man doch so, daß man hätte noch mehr genießen können, noch mehr leiden können, noch mehr Willens-impulse hätte entwickeln können.",
        "Das aber muß erst überwunden werden, was an Möglichkeiten des Fühlens und Wollens noch in der"
      ],
      [
        "Seele ist.",
        "Solange das nicht vollständig überwunden ist, so lange haben wir einen Begierdenzusammenhang mit dem letzten Erdenleben.",
        "Wir schauen gleichsam auf dieses letzte Erdenleben zurück.",
        "Es ist, wie ich es öfter mit einem trivialen Wort genannt habe, eine Art Abgewöhnen von dem Zusammenhang mit dem physischen Erdenleben.",
        "In die Natur dieser Kraft, die man da zu überwinden hat, zu deren Über­windung man eigentlich jahrzehntelang braucht, in die Natur dieser Kraft dringt derjenige, der nur ein wenig wirklicher Geistesforscher wird, sehr bald ein, denn sie offenbart sich eigentlich verhältnismäßig leicht der Geistesforschung."
      ],
      [
        "Wenn wir jeden Tag aus den Erlebnissen des Tages heraus ein­schlafen, eine Zeit zubringen zwischen dem Einschlafen und dem Er­wachen, dann sind wir in unserem Seelisch-Geistigen außerhalb unseres Leibes.",
        "Wir kehren zurück, weil wir im Seelisch-Geistigen einen Trieb zu diesem Zurückkehren haben, weil wir wirklich nach unserem Leib begehren.",
        "Wir begehren durchaus nach unserem Leib, und wer das Aufwachen bewußt erleben kann, der weiß: Du willst aufwachen und du mußt aufwachen wollen.",
        "Es besteht eben eine Anziehungskraft im Geistig-Seelischen nach dem Leibe hin.",
        "Diese muß nach und nach abglimmen, muß ganz und gar überwunden werden.",
        "Das dauert Jahr­zehnte.",
        "Es ist die Zeit, in der wir nach und nach unseren Zusammen­hang mit dem letzten Erdenieben überwinden.",
        "Das macht es, daß wir in bezug auf die Erlebnisse nach dem Tode in der Zeit, die also ver­fließt, wie ich es eben geschildert habe, eigentlich alles auf dem Umweg durch unser Erdenieben erleben müssen."
      ],
      [
        "Ich bin jetzt in der Lage, nachdem die vorhergehenden Vorträge gehalten worden sind, Ihnen mancherlei Verhältnisse genauer zu schildern als sonst, wo man mehr im Überblick schildern mußte, denn es müssen für die genaue Schilderung immer erst die Begriffe herbei-getragen werden."
      ],
      [
        "Nehmen wir einmal an, wir haben einen Menschen auf der Erde zurückgelassen und sind selber durch die Pforte des Todes gegangen.",
        "Wir stehen also in der Zeit darinnen, wo wir uns die Fähigkeit an-geeignet haben, in die elementaren Wesenheiten hineinzuschauen und uns selber zu erfühlen, so daß wir wissen: Unsere Erdenfrüchte haben"
      ],
      [
        "sich gefernt Aber wir hängen noch zusammen mit unserem letzten Erdenleben.",
        "Nehmen wir an, wir haben einen Menschen zurückge­lassen, wenn wir durch die Pforte des Todes geschritten sind, den wir sehr lieb gehabt haben."
      ],
      [
        "Ja, jetzt nach dem Tode kommen wir allmäh­lich dazu, indem wir uns von unseren eigenen elementaren Schöpfun­gen aus hineingewöhnen, die elementaren Wesenheiten von anderen zu schauen, jetzt können wir uns hineinfinden, Gedanken anderer als Elementarwesen zu schauen.",
        "Das lernen wir allmählich an unseren eigenen Elementarwesen, auch bei den andern Menschen, die wir zurückgelassen haben, zu sehen, was er denkt, was in seiner Seele an Gedanken lebt; wir sehen es."
      ],
      [
        "Denn es drückt sich in den Elementar-wesen aus, die uns in mächtigen Imaginationen vor die Seele treten.",
        "Wir können also in dieser Beziehung jetzt schon viel mehr Zusammen­hang haben mit dem Innerlichen des betreffenden Menschen, als wir mit ihm in der physischen Welt hatten."
      ],
      [
        "Denn während wir selber im physischen Leibe waren, konnten wir ja nicht auf das Gedankliche des andern hinschauen; jetzt können wir es.",
        "Aber wir brauchen gleichsam die Gefühlserinnerung - bitte auf das Wort wohl acht zu geben - die Gefühiserinnerung, den Gefühiszusammenhang mit unserem eigenen letzten Erdenleben."
      ],
      [
        "Wir müssen gleichsam so fühlen, wie wir im Leibe gefühlt haben, und dieses Gefühl muß in uns nachklingen, dann belebt sich das Verhältnis, das wir sonst nur wie zu einem Bilde haben wür­den, als das uns die Gedanken des andern erscheinen.",
        "Einen lebendigen Zusammenhang bekommen wir also auf dem Umwege durch unsere Gefühle."
      ],
      [
        "Und so ist es im Grunde genommen mit allem."
      ],
      [
        "Sie sehen, es ist ein Herausarbeiten aus einem Zustand, den man dadurch charakterisieren kann, daß man sagt: Es ist eine Zeit, in der wir die Kräfte noch aus unserem letzten Erdenleben beziehen müssen, um in lebendige Beziehungen zu kommen zu unserer geistigen Um­welt, wir müssen mit diesem Erdenleben noch zusammenhängen.",
        "Wir lieben die Seelen, die wir zurückgelassen haben, deren Seeleninhalt uns als Gedanken, als Elementarwesen erscheint, aber wir lieben sie, weil wir selber noch leben von der Liebe, die wir für sie während unseres Erdenlebens entwickelt haben.",
        "Es ist ja unangenehm, möchte ich fast sagen, solche Ausdrücke zu gebrauchen, aber einige von Ihnen"
      ],
      [
        "werden mich verstehen, wenn ich sage: Das Erdenleben - also nicht das Gedankenieben - das Erdenleben als gefühlter und mit Willensimpuls durchsetzter Seeleninhalt, mit dem wir noch zusammenhängen, das wird wie eine Art elektrischer Umschalter der eigenen Individualität mit dem, was um uns herum geistig uns umwallt.",
        "Wie eine Art elektrischer Umschalter: wir nehmen alles wahr auf dem Umweg durch das letzte Erdenleben."
      ],
      [
        "Aber nur durch das, was im letzten Erdenleben Fühlen und Wollen war, nehmen wir wahr, was in der geistigen Welt zu uns gehört.",
        "Es ist wirklich jetzt so, daß wir uns in der Zeit weiter-lebend fühlen, wie eine Art Komet der Zeit."
      ],
      [
        "Unser Erdenleben ist noch da wie ein Kern, aber der Kern entwickelt in die nächste Zukunft hinein eine Art von Schweif, den wir durchleben.",
        "Wir hängen noch zusammen mit unserem Erdenleben, insoferne dieses erfüllt ist von Gefühl und Wille."
      ],
      [
        "In unserem Seeleninnern muß sich herausgebären aus diesem Erleben, wie ich es Ihnen geschildert habe, etwas, was jetzt nicht unmittelbar Gefühl und Wille ist.",
        "Denn die Seelenkräfte, die wir hier in der physischen Welt entwickeln, auch die Kraft des Fühlens, wie wir sie eben in der physischen Welt als Gefühlskraft haben, die Kraft des Willens, wie wir sie in der physischen Welt als Willenskraft haben, haben wir in dieser Form dadurch, daß wir eben im physischen Leibe leben."
      ],
      [
        "Wenn die Seele nun nicht mehr im physi­schen Leibe lebt, so muß sie andere Fähigkeiten entwickeln, die wäh­rend des physischen Lebens nur schlummern, sie muß, während noch der Nachkiang von Gefühl und Wille Jahre hindurch in ihr wirkt, aus diesem Zusammenhang das herausreifen, was sie nun für die geistige Welt auch in dieser Beziehung brauchen kann, Kräfte, die ich be­zeichnet habe, indem ich sagte: es ist etwas wie ein fühlendes Begehren oder ein begehrendes Fühlen.",
        "Von unserem Gefühl und unserem Willen wissen wir, die sitzen in unserer Seele darinnen."
      ],
      [
        "Doch von einem solchen Gefühl und Begehren, wie sie in unserer Seele sitzen, da haben wir nach dem Tode im Grunde genommen nichts, die müssen nach und nach abdämmern und abdumpfen; und das tun sie eben nach Jahren.",
        "Aber während dieses Abdämmerns und Abdumpfens muß sich von Gefühl und Wille etwas entwickeln, wovon wir nach dem Tode etwas haben."
      ],
      [
        "Unsere Gedanken leben draußen als Elementarwesen.",
        "Von einem Gefühl und einem Willen, wie sie in uns lebten, wurden wir nichts haben für diese Welt, die wir selber sind und die da d':außen ist.",
        "Wir müssen nach und nach einen Willen entwickeln - und den entwickeln wir auch -, der von uns ausströmt, der sich wie von uns ergießt und hinwallt und hinwogt dorthin, wo unsere lebendigen Gedanken sind.",
        "Diese durchdringt er, weil auf den Wogen des Willens das Gefühl schwimmt, das im physischen Leben nur in uns ist.",
        "Auf den Wogen des Willens schwimmt das Gefühl, da draußen wallt und wogt das Meer unseres Willens, und auf diesem schwimmt das Gefühl.",
        "Nämlich es schwimmt dann, wenn der Wille heranstößt an ein Gedanken­elementarwesen, dann geschieht durch diesen Zusammenstoß des Willens mit den Gedankenelementarwesen em Aufglimmen des Ge­fühis, und wir nehmen wahr als eine reale Wirklichkeit der geistigen Welt dieses Zurückgeworfenwerden unseres Willens."
      ],
      [
        "Ich will so sagen: Nehmen wir an, in der geistigen Außenwelt sei ein Elementarwesen.",
        "Wenn wir uns herausgearbeitet haben aus dem Zustand, den wir zuerst durchmachen müssen, dann brandet unser Wille, der jetzt aus uns herausgeht, zu dem Elementarwesen hin.",
        "Da, wo er heranstößt an das Elementarwesen, wird er zurückgeworfen: jetzt kommt er nicht als Wille zurück, jetzt kommt er als Gefühl zurück, welches in diesem Meer des Willens zurückflutet zu uns.",
        "Als Gefühl, welches in den Fluten des Willens zu uns zurückkommt, lebt unser eigenes Wesen ausgegossen in den Kosmos.",
        "Dadurch werden die Elementarwesen real für uns, dadurch nehmen wir allmählich immer mehr und mehr wahr, was wirklich da draußen an geistiger Außenwelt außer uns vorhanden ist."
      ],
      [
        "Aber noch eine Seelenkraft muß aus uns herauskommen, die noch in viel tieferen Schichten der Seele schlummert als das fühlende Wollen oder wollende Fühlen: die kreative Seelenkraft, die wie ein inneres Seelenlicht ist, die hinausleuchten muß über die geistige Welt, damit wir nicht nur auf den Gefühiswogen, die da zurückkommen in dem Meer unseres Willens, schwimmend schauen die lebend wehenden objektiven Gedankenwesen, sondern damit wir auch mit geistigem Licht diese geistige Welt durchleuchtet haben.",
        "Kreative geistige"
      ],
      [
        "Leuchtekraft muß von unserer Seele hinausgehen in die geistige Welt.",
        "Die erwacht allmählich."
      ],
      [
        "Sehen Sie, meine lieben Freunde, von dem fühlenden Wollen und wollenden Fühlen haben wir, während wir im physischen Leibe leben, wenigstens, ich möchte sagen, das Geschwisterpaar Fühlen und Wollen in uns differenziert.",
        "Zu zweien haben wir das, während es eine Einheit ist, wenn wir durch die Pforte des Todes durchgegangen sind."
      ],
      [
        "Diese kreative Seelenkraft, die wir wie ein Seelenlicht ausstrahlen in den geistigen Raum hinaus, wenn ich den Ausdruck «Raum» hier gebrauchen darf, denn es ist eigentlich kein Raum, aber man muß diese Verhältnisse in gewisser Weise dadurch zum Verständnis bringen, daß man sich bildlich ausdrückt, dieses Seelerlicht schlummert tief unten in uns, weil es zusammenhängt mit dem, wovon wir im Leben nichts wissen dürfen und können.",
        "Ganz tief unten schlummert in uns wäh­rend des Lebens im physischen Plan, was dann als Licht wie erlöst ist und dann die geistige Welt erleuchtet und erhellt."
      ],
      [
        "Was da von uns ausstrahlt, muß umgewandelt und verwendet werden während unseres physischen Lebens dazu, daß unser Leib wirklich lebt und Bewußtsein in sich bergen kann.",
        "Aber ganz unterhalb der Schwelle des Bewußt­seins wirkt diese geistige Leuchtekraft in unserem physischen Leib als die Leben und Bewußtsein organisierende Kraft."
      ],
      [
        "Wir dürfen sie nicht ins Erdenbewußtsein hereinbringen, sonst würden wir unserem Leibe die Kraft rauben, die ihn durchorganisieren muß.",
        "Jetzt, wo wir keinen Leib zu versorgen haben, wird sie geistige Leuchtekraft und durch-strahlt und durchleuchtet und durchhellt und durchglitzert alles - die Worte bedeuten reale Wirklichkeiten."
      ],
      [
        "So arbeiten wir uns allmählich hinein, in der geistigen Welt ebenso zu Haus zu werden, sie als eine Realität zu erleben, wie wir hier die physische Welt als eine Realität erleben.",
        "Wir arbeiten uns allmählich hinein, wirklich auch die toten Menschenseelen, insofern sie real leben in der geistigen Welt, als unsere Genossen in der geistigen Welt zu haben.",
        "Wir leben unter den Seelen, wie wir hier im physischen Leibe unter Leibern leben.",
        "Und indem man immer mehr und mehr vordringt in den eigentlichen inneren Geist der Geisteswissenschaft, wird die Behauptung, die jemand etwa tun wollte, daß wir nach dem Tode"
      ],
      [
        "nicht mit all den Menschen, mit denen wir gelebt haben, wiederum zusammenkommen würden, diese Behauptung wird für den, der tiefer eindringt in die Sache, so töricht, wie für den physischen Plan die Behauptung töricht wäre, daß, wenn wir durch die Geburt herein-treten in diese Erde, wir keinen Menschen darin finden.",
        "Die Menschen sind eben um uns herum.",
        "Genau dasselbe ist es für den Kenner des geistigen Lebens, wie wenn jemand sagen wollte: Das Kind lebt sich in die Welt herein, aber Menschen sieht es nicht.",
        "Das ist ein offenbarer Unsinn.",
        "Ebenso ist es ein Unsinn, wenn gesagt wird: Wir finden, wenn wir uns in die geistige Welt hineinleben, nicht all die Seelen wieder, mit denen wir in Zusammenhang gestanden haben, und wir finden nicht Wesenheiten der höheren Hierarchien, die wir stufenweise kennenlernen, wie hier auf der Erde die Mineralien, Pflanzen und Tiere.",
        "Das aber ist der Unterschied, daß wir hier in der physischen Welt wissen: Indem wir die Dinge sehen, hören, kommt die Möglichkeit, sie zu sehen und zu hören durch die Sinne, von der Außenwelt.",
        "In der geistigen Welt, wissen wir, kommt diese Möglichkeit von uns, indem das, was wir Seelenlicht, Seelenleuchte nennen können, von unserer Seele ausstrahlt und die Dinge erhellt, erleuchtet und durch­leuchtet."
      ],
      [
        "So leben wir in die Zeit hinein, die man die erste Hälfte des Lebens zwischen dem Tod und einer neuen Geburt nennen kann.",
        "Indem wir in diese Zeit hineinleben, machen wir die zwei Zustände durch, von denen ich auch im öffentlichen Vortrag gesprochen habe, eine Zeit, die eben nach Jahren dauert, in der wir so, wie es geschildert worden ist, durch die Ausstrahlung unserer Seelenleuchtekraft mit der geisti­gen Welt zusammenhängen, in der wir also das schauen, was an Geistern und Seelen um uns herum ist.",
        "Das dämmert dann ab, wir fühlen: Du kannst jetzt immer weniger deine Seelenleuchtekraft ent­wickeln, du mußt es dämmeriger und immer finsterer werden lassen im geistigen Sinn.",
        "Dadurch siehst du immer weniger die geistigen Wesenheiten.",
        "Das wird immer mehr und mehr so, daß man abwechselt mit einer Zeit, in der man sich sagt: Da, um dich sind die Wesenheiten, aber du wirst immer einsamer, du hast nur deinen eigenen Seelen-inhalt, und dieser Seeleninhalt wird in dem Maße reicher, in dem man"
      ],
      [
        "aufhört, da draußen die Wesen beleuchten zu können.",
        "Es gibt Zeiten der geistigen Geselligkeit und Zeiten der geistigen Einsamkeit, in der ein Nacherleben dessen ist, was man in den Zeiten der geistigen Geselligkeiten erlebt hat, aber alles dann in der Seele: das schwingt ab und wechselt ab.",
        "So leben wir uns hinein in die geistige Welt: geistige Geselligkeit - geistige Einsamkeit.",
        "In den Zeiten geistiger Einsamkeit, da wissen wir: Was du sonst in der geistigen Welt rings um dich herum erlebt hast, das war ja alles da, von all dem weißt du, aber jetzt sind nur die Nachklänge davon in deinem Innern.",
        "Man könnte sagen:"
      ],
      [
        "Erinnerungen sind es in den Zeiten geistiger Einsamkeit.",
        "Allein, wenn man sölche Worte gebraucht, trifft man die Sache nicht richtig.",
        "Ich will daher versuchen, es Ihnen noch von einer anderen Seite her zu schildern."
      ],
      [
        "Es ist nicht so, als wenn man in der geistigen Dunkelheit, in der man nichts Geselliges hat, sich erinnern würde an das, was man früher in der geistigen Welt erlebt hat, sondern als wenn man das in jedem Augenblick frisch hervorbringen müßte: es ist ein fortwährendes inneres Schaffen.",
        "Aber man weiß: Während da draußen die Außenwelt ist, mußt du mit dir selber sein und schaffen und schaffen.",
        "Was du schaffst, ist die Welt, die da draußen dich umbrandet jenseits der Ufer deines eigenen Wesens."
      ],
      [
        "Aber indem man so in der ersten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt weiterlebt und sich der Mitte der Zeit zwischen dem Tod und einer neuen Geburt nähert, fühlt man das einsame Leben immer reicher werden und die Ausblicke auf die geistige Umgebung gleichsam kürzer und dämmeriger werden, bis die Zeit herankommt in der Mitte zwischen dem Tod und einer neuen Geburt, die ich versucht habe, in meinem letzten Mysterienspiel « Der Seelen Erwachen» als die Weltenmitternacht darzustellen, wo der Mensch das stärkste Leben in seinem Innern hat, aber nicht mehr die kreative Seelenkraft, um seine geistige Umgebung zu beleuchten, wo sozusagen unendliche Welten aus unserem Innern uns innerlich geistig erfüllen können, aber wir von anderem Sein als unserem eigenen Sein nichts wissen können.",
        "Das ist die Mitte in den Erlebnissen zwischen dem Tod und einer neuen Geburt: die Weltenmitternacht."
      ],
      [
        "Nun beginnt die Zeit, in der im Menschen die Sehnsucht zu einer positiven schöpferischen Kraft wird.",
        "Denn obzwar wir ein Unend­liches als ein inneres Leben haben, erwacht in uns die Sehnsucht, eine Außenwelt wieder zu haben.",
        "So verschieden sind die Verhältnisse der geistigen Welt von denen der physischen Welt, daß, während die Sehnsucht in der physischen Welt die passivste Kraft ist - wenn wir etwas haben, nach dem wir uns sehnen, so ist es dieses Etwas, was uns bestimmt -, ist das Gegenteil in der geistigen Welt der Fall.",
        "Da wird die Sehnsucht eine schöpferische Kraft, sie verwandelt sich in das, was jetzt als eine neue Art von Seelenlicht uns eine Außenwelt geben kann, eine Außenwelt, die aber doch eine Innenwelt ist, indem sich uns der Blick eröffnet auf unsere früheren Erdeninkarnationen.",
        "Die liegen jetzt beleuchtet von dem aus unserer Sehnsucht heraus geborenen Licht, vor uns ausgebreitet.",
        "Es gibt im geistigen Kosmos eine Kraft, die aus der Sehnsucht heraus diesen Rückblick uns erleuchten und erleben lassen kann.",
        "Dazu ist aber in unserem gegenwärtigen Zeitenzyklus eines notwendig."
      ],
      [
        "Ich habe Ihnen gesagt: In dieser ganzen Zeit der ersten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt wechseln wir ab zwischen Innenleben und Außenleben, zwischen Einsamkeit und geistiger Geselligkeit.",
        "Die Verhältnisse der geistigen Welt sind zu­nächst so, daß jedesmal, wenn wir in dieser geistigen Welt wieder in unsere Einsamkeit zurückkommen, wir in unserer inneren Tätigkeit immer wiederum das vor unsere Seele bringen, was wir in der äußeren Welt durchlebt haben.",
        "Dadurch ist ein Bewußtsein vorhanden, das sich ausbreitet wie mit Schwingen der Unendlichkeit über die ganze geistige Welt.",
        "Die Schwingen ziehen sich wiederum zusammen in der Einsamkeit."
      ],
      [
        "Aber eines müssen wir uns erhalten, das da vorhanden bleiben muß, gleichgültig, ob wir uns ausbreiten in die große geistige Welt oder uns zurückziehen.",
        "Bevor das Mysterium von Golgatha geschah, war es möglich, durch die Kräfte, durch die der Mensch mit den Urzeiten zusammengehangen hat, den festen Ichzusammenhalt zu haben, nicht zu verlieren diesen Ichzusammenhalt, das heißt, an das verflossene Erdenleben das eine als Erinnerung vollständig deutlich zurück zu"
      ],
      [
        "behalten: man war auf der Erde in diesem Leben ein Ich.",
        "Das muß sich durchdehnen durch die Zeiten der Einsamkeit und der Gesellig­keit.",
        "Vor dem Mysterium von Golgatha war durch die vererbten Kräfte dafür gesorgt.",
        "Jetzt kann dafür nur dadurch gesorgt wer­den, daß mit dem, was wir als unser Erdengut von uns losgelöst haben, was wir sich fernend empfunden haben gleich beim Verlassen des physischen Leibes, daß mit diesem eine Seelenerfüllung verbunden bleibt, die Seelenerfüllung, die wir dadurch haben können, daß der Christus ausgeflossen ist in die Erdenaura.",
        "Dieses Durchdrungen-sein mit dem Christus-Substantiellen, das ist es, was uns in der Gegenwart bei dem Übergang aus dem physischen Leben in den Tod die Möglichkeit gibt, bis zur Weltenmitternacht hin die Erinnerung an unser Ich zu bewahren trotz alles Ausbreitens in die geistige Welt, trotz alles Zusammenziehens in die Einsamkeit.",
        "Bis dahin reicht der Impuls, der von der Christuskraft ausgeht, so daß wir uns selber nicht verlieren.",
        "Dann aber muß aus der Sehnsucht heraus eine neue geistige Kraft unsere Sehnsucht zu einem neuen Licht anfachen.",
        "Diese Kraft ist nur im Geiste, im geistigen Leben vorhanden."
      ],
      [
        "Meine lieben Freunde, es gibt in der physischen Welt die Natur und das diese Natur durchdringende Göttliche, aus dem wir in die physi­sche Welt hineingeboren werden.",
        "Es gibt den Christusimpuls, der in der Erdenaura, das heißt in der Aura der physischen Natur, vorhanden ist.",
        "Aber die Kraft, die in der Weltenmitternacht an uns herankommt, um unsere Sehnsucht leuchtend zu machen über unsere ganze Ver­gangenheit hin, die gibt es nur in der geistigen Welt, die gibt es nur da, wo keine Leiber leben können.",
        "Und hat uns der Christusimpuls bis in die Weltenmitternacht gebracht, und ist die Weitenmitternacht in geistiger Einsamkeit von der Seele erlebt worden, weil das Seelen-licht jetzt nicht erstrahlen kann von uns selber aus, ist Weltenfinsternis eingetreten, hat uns der Christus bis dahin geführt, so tritt jetzt aus der Weltenmitternacht, aus unserer Sehnsucht, ein Geistiges heraus, erschaffend ein neues Weltenlicht, über unsere eigene Wesenheit hin ein Leuchten verbreitend, durch das wir uns neu ergreifen im Weltendasein, durch das wir neu erwachen im Weltendasein.",
        "Den Geist der geistigen Welt, der uns erweckt, wir lernen ihn kennen, indem aus"
      ],
      [
        "der Weltenmitternacht ein neues Licht hervorleuchtet, über unsere verflossene Menschheit erstrahlend.",
        "In dem Christus sind wir gestor­ben - durch den Geist, durch den leiblosen Geist, der mit einem technischen Wort der Heilige Geist genannt wird, das heißt, der ohne den Leib Lebende, denn das ist mit dem Wort «hellig» gemeint, ohne die Schwächen eines im Leibe lebenden Geistes, durch diesen Geist werden wir in unserer Wesenheit wiedererweckt aus der Welten-mitternacht heraus."
      ],
      [
        "Durch den Heiligen Geist werden wir also in der Weltenmitternacht erweckt."
      ],
      [
        "Per spiritum sanetum reviviscimus."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "SECHSTER VORTRAG Wien, 14. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "In diesem meinem letzten Vortrag möchte ich da fortfahren, wo wir gestern geendet haben. Geendet haben wir bei dem, was ich mir zu benennen erlaubte «die große Weltenmitternachtsstunde des geistigen Daseins zwischen dem Tod und einer neuen Geburt», jene Mitter­nachtsstunde, wo das menschliche innere Erleben am intensivsten wird und das, was wir geistige Geselligkeit nennen können, das Zu­sammenhängen mit der geistigen Außenwelt, den niedrigsten Grad erreicht hat, so daß in gewisser Beziehung während dieser Mitter­nachtsstunde des geistigen Daseins geistige Finsternis um uns ist.",
      "Aber gesagt worden ist, daß die Sehnsucht nach Außenwelt wiederum in uns wirkt, und daß diese Sehnsucht durch den Geist, der in geistigen Welten wirkt, aktiv wird, und daß diese Sehnsucht ein neues Seelen-licht aus uns erzeugt, sodaß es uns möglich wird, jetzt eine Außenwelt von ganz besonderer Art zu erblicken. Diese Außenwelt, die wir dann erblicken, ist unsere eigene Vergangenheit, wie sie durch frühere Inkarnationen und die Zwischenzeiten zwischen den Toden und den neuen Geburten sich vollzogen hat, und die wir jetzt als eine äußere Welt überschauen, indem wir zurückblicken auf das, was wir aus dem Weltendasein gehabt haben, genossen haben, und auf das, was wir diesem Weltendasein schuldig geblieben sind.",
      "Insbesondere tritt uns dann, wenn wir diesen Rückblick in unsere früheren Erlebnisse haben, zweierlei mit großer Intensität entgegen. Wir haben - das zeigt sich uns gleichsam durch ein geistiges Anschauen - dieses und jenes ge­nossen, dieses und jenes ist uns beschert worden an Freude, an Lust des Daseins.",
      "Das alles können wir übersehen, was uns jemals geworden ist an Freude, an Lust des Daseins. Aber wir übersehen es so, daß es uns gleichsam in seinem spirituellen Wert erscheint, daß es uns in bezug darauf erscheint, was es aus uns gemacht hat.",
      "Nehmen wir einen konkreten Fall an. Wir blicken zurück auf etwas, was uns als Genuß, als Befriedigang in der verflossenen Zeit in irgend einem unserer Daseinsleben zuteil geworden ist. Dann fühlen wir:",
      "Das ist nicht etwas Vergangenes, es ist zwar in der Zeit zurückliegend, daß du davon den Genuß hattest, aber es ist nicht etwas, was absolut vergangen ist. Es ist etwas, was seine Wirkung in alle Zeiten hinein fortsetzt, so fortsetzt, daß es darauf wartet, was wir daraus machen.",
      "Wenn wir eine Befriedigung, einen Genuß gehabt haben, so fühlen wir in uns, wir erleben es unmittelbar in unserem Seelensein bei diesem Zurückschauen: Das muß eine Kraft in dir werden, eine Kraft deiner Seele, und diese Kraft deiner Seele, die kannst du in zweierlei Weise in dir wirken lassen. Jetzt in diesem geistigen Dasein nach der Weltenmitternacht, in dem du stehst, hast du diese zweifache Möglich­keit.",
      "Die geistige Welt gibt dir einfach Fähigkeiten, eine von diesen Möglichkeiten zur Wirklichkeit zu machen. Du kannst diesen ver­gangenen Genuß, diese vergangene Befriedigung in dir umwandeln in eine Fähigkeit, so daß du eine gewisse Kraft in deiner Seele ent­wickelst durch den verflossenen Genuß, die dich zu diesem oder jenem befähigt, wodurch du irgend etwas in der Welt, sei es das Kleinste, sei es das Größte, schaffst, das einen Wert für die Welt hat.",
      "Das ist das eine. Das andere ist, daß wir uns sagen können: Nun, den Genuß habe ich gehabt, ich will mit dem Genuß zufrieden sein, ich will den Genuß in meine Seele hereinnehmen und will mich laben daran, daß ich in der Vergangenheit diesen Genuß gehabt habe.",
      "Wenn wir mit vielem, was wir genossen haben, was uns befriedigt hat, eine solche Möglichkeit herbeiführen, dann kommt es dazu, daß wir in unserem Innern eine Kraft schaffen, an der wir nach und nach geistig degenerieren, ersticken. Und das gehört zu dem Wichtigsten, was wir lernen können in der geistigen Welt, daß wir auch durch den Genuß, durch das, wodurch wir befriedigt werden, Schuldner werden des Weltendaseins.",
      "Die Aussicht tritt vor unser geistiges Auge, zu ersticken in den Nachwirkungen der Befriedigungen, der Genüsse, wenn wir uns nicht im rechten Zeitpunkt entschließen, aus verflosse­nen Befriedigungen, aus verflossenen Genüssen Fähigkeiten zu schaffen, die Wertvolles im Leben hervorbringen können. Sie sehen daraus wiederum, wie das Geistige und das, was auf dem physischen Plan geschieht, in Wechselwirkung steht.",
      "Wer sich, im Sinne des vorgestrigen Vortrags, immer mehr und",
      "mehr mit den Erkenntnissen der Geisteswissenschaft durchdringt, bei dem wird diese Geisteswissenschaft in das instinktive Leben seiner Seele übergehen, und er wird gewissermaßen wie die Regung eines inneren Gewissens auch gegenüber den Genüssen, gegenüber den Befriedigungen, die er auf dem physischen Plane hat, die Stimmung entwickeln: Du darfst nicht nur um deiner 6elbst willen irgend einen Genuß, eine Freude, eine Lust hinnehmen, sondern er wird diese Lust durchdringen mit einer Art von Dankbarkeitsgefühl gegenüber dem Weltenall, gegenüber den geistigen Mächten des Weltenalls. Denn er wird wissen, daß er durch jeden Genuß, durch jede Befriedigung ein Schuldner des Weltenalls wird. Am leichtesten und sichersten kommen wir zurecht mit der Umwandlung derjenigen Genüsse und Freuden, welche geistiger Art sind. Solche Genüsse und Lüste, welche nur be­friedigt werden können durch die leiblichen Werkzeuge oder über­haupt nur dadurch, daß der Mensch auf dem physischen Plan einen Leib an sich trägt, stehen zwar auch in der angedeuteten Zeit zwischen dem Tod und einer neuen Geburt als etwas vor uns, was umgewandelt werden muß, wenn wir nicht nach und nach gewissermaßen darin ersticken wollen. Wir fühlen die Notwendigkeit der Umwandlung, aber wir fühlen auch das eine, daß viele Inkarnationen notwendig sein werden, damit wir zwischen diesen Inkarnationen immer wieder in der geistigen Welt sind und endlich die Umwandlung bewirken können.",
      "Dann finden wir in der geistigen Welt noch etwas anderes. Wir finden das, daß wir in unserem gegenwärtigen Menschheitszyklus mit solchen Genüssen, mit solchen Freuden, in denen auf dem physischen Plan gleichsam unser Seelisch-Geistiges ganz untergeht, und der Genuß, die Befriedigung einen untermenschlichen, ich will nicht sagen, tierischen Charakter annimmt - denn Freude und Genuß können untermenschlichen Charakter annehmen -, daß wir in der Tat mit solchen Genüssen gewissen Wesenheiten der geistigen Welt unendli­chen Schmerz bereiten, die uns erst dann entgegentreten, wenn wir eben in diese geistige Welt eintreten. Und der Anblick dieses Schmer­zes, den wir in der geistigen Welt gewissen Wesenheiten bereiten, der ist so ungeheuer bestürzend, bedrückend, unsere Seele mit solchen Kräften durchziehend, daß wir mit dem harmonischen Ausbilden der",
      "Zusammenhänge für die nächste Inkarnation keineswegs gut zurecht­kommen.",
      "Gegenüber dem, um das andere zu erörtern, was wir auf Erden an Schmerzen, an Leiden erleben, zeigt sich auf dem geistigen Plan, daß auf dem physischen Plane erduldete Schmerzen, erduldetes Leid fort-wirken und auf dem geistigen Plan unsere Seele so durchdringen mit Kräften, daß diese Kräfte Willenskräfte werden, daß wir dadurch in der Seele stärker werden und die Möglichkeit haben, diese Stärke in moralische Kraft umzuwandeln, die wir dann wiederum auf den physischen Plan mitbringen können, um nicht nur gewisse Fähig­keiten zu haben, durch die wir Wertvolles schaffen können für die Umwelt, sondern um auch die moralische Kraft zu haben, charakter­voll diese Fähigkeiten auszuleben.",
      "Solche und viele andere Erlebnisse haben wir unmittelbar nach der geistigen Mitternachtsstunde des Daseins. Wir erfühlen, erleben, was wir wert geworden sind durch unser verflossenes Dasein, wir erfühlen, erleben, zu welchen Fähigkeiten wir kommen können in der Zukunft. Nachdem wir dann eine Weile weiterleben in der geistigen Welt, tritt aus dem Dämmerdunkel der geistigen Umgebung heraus eine deut­liche Anschauung, jetzt nicht nur unserer eigenen verflossenen Leben, sondern namentlich alles des Menschlichen, was mit diesen Leben verbunden war, und zwar alles desjenigen Menschlichen, was näher mit diesen Leben verbunden war. Menschen treten in geistige Be­ziehungen zu uns, mit denen wir in früheren Daseinsstufen diese oder jene Beziehung hatten. Nicht als ob früher die Gemeinsamkeit mit diesen Menschen nicht da gewesen wäre - wir erleben uns immer zusammen mit den Menschen, die uns im Leben nahegestanden haben, in der weitaus größten Zeit zwischen dem Tod und einer neuen Ge­burt -, aber jetzt tritt, indem wir diese Menschen nach der Mitter­nachtsstunde des geistigen Daseins wieder treffen, deutlich und klar an diesen Menschen hervor, was wir ihnen schuldig geworden sind, oder was sie uns schuldig geworden sind. Wir erleben jetzt nicht bloß eine Anschauung: So standest du mit diesen Menschen zwischen dieser und jener Zeit - das hatten wir früher auch -, sondern diese Menschen werden für uns der Ausdruck für das, was Ausgleich ist für die früheren",
      "Erlebnisse. Wir sehen es den Menschen an, 50 wie sie uns entgegen­treten, durch welche neuen Erlebnisse auf dem physischen Plane wir für Früheres Ausgleich schaffen können, was wir ihnen schuldig geblieben sind oder dergleichen. Wir schauen sozusagen, indem wir den Seelen der Menschen gegenüberstehen, auf die Wirkungen, welche in der Zu­kunft die Folgen sein werden von Beziehungen, die wir zu den Men­schen in der Vergangenheit gehabt haben. Natürlich sieht man das am besten ein, wenn man einen möglichst konkreten Einzelfall nimmt.",
      "Nehmen wir also noch einmal an, wir hätten einen Menschen ange­logen. Jetzt ist die Zeit, wo die Möglichkeit in der geistigen Welt geboten ist, daß wir durch die unserer Lüge entgegengesetzte Wahr­heit gequält werden.",
      "Aber dadurch werden wir gequält, daß sich die Beziehung zu dem Menschen, den wir angelogen haben, in der jetzt geschilderten Zeit so verändert, so oft wir den Menschen erblicken -und wir werden ihn genügend oft mit dem geistigen Auge erblicken -, daß er die Ursache wird, daß die der vollbrachten Lüge entgegen­gesetzte Wahrheit, die uns quält, in uns aufsteigt. Dadurch taucht aus unseren Tiefen die Tendenz herauf: Diesem Menschen mußt du unten auf der Erde wieder begegnen, und du mußt etwas tun, was das Un­recht ausgleicht, das du durch die vollzogene Lüge begangen hast.",
      "Denn hier in der geistigen Welt kann das nicht ausgeglichen werden, was durch deine Lüge geschaffen worden ist, da im Kosmos kannst du nur völlige Klarheit gewinnen über die Wirkung einer Lüge. Was auf Erden geschaffen worden ist von dieser Art, das muß auch wie­derum auf der Erde ausgeglichen werden.",
      "Man weiß, man braucht zum Ausgleich Kräfte in sich selber, die einem nur werden können, wenn man wiederum einen Erdenleib bezieht. Dadurch entsteht in unserer Seele die Tendenz: Du mußt einen Erdenleib beziehen, der die Möglichkeit bietet, eine solche Tat zu vollbringen, wodurch die Unvollkommenheiten ausgeglichen werden, die du auf Erden ver­ursacht hast, sonst wird, wenn du durch den nächsten Tod gegangen bist, dieser Mensch wiederum dir erscheinen und die Qual der Wahr­heit hervorrufen.",
      "Sie sehen die ganze geistige Technik, wie in der geistigen Welt der Trieb in uns geschaffen wird, einen karmischen Ausgleich für das oder jenes zu schaffen.",
      "Diese Ausgleiche geschehen auch durch andere Voraussetzungen; aber ich müßte natürlich tausend und abertausend konkrete Fälle auf­zählen, wenn ich alles zum Vorschein bringen wollte, was für diese bedeutsame karmische Frage in Betracht kommt. Nehmen wir zum Beispiel den folgenden Fall.",
      "Nehmen wir an, wir sind in der Zeit, die auf die Mitternachtsstunde des Daseins folgt, so in der geistigen Welt, daß wir zurückblicken auf gewisse Freuden, die wir gehabt haben und sagen: Wir können die Wirkungen dieser Erlebnisse in Fähigkeiten umwandeln, die wir dann ausdrücken können, wenn wir wieder ver­leiblicht sein werden. Ja, dann kann aber folgendes geschehen.",
      "Wir können bemerken: Indem du dir jetzt in deiner gegenwärtigen Lage diese verflossenen Erlebnisse umwandelst in Fähigkeiten, da stören dich gewisse Elementarwesen. Das kann so sein. Diese Elementarwesen lassen es nicht dazu kommen, daß du dir diese Fähigkeiten wirklich aneignest.",
      "Jetzt kann man sich fragen: Was ist nun zu tun? Wenn ich diesen Elementarwesen wilifahre, die da herankommen und die mcht leiden können, daß in mir diese Fähigkeiten entstehen, dann werde ich mir diese Fähigkeiten nicht bilden können.",
      "Aber diese Fähigkeiten muß ich mir bilden. Ich weiß, daß ich nur dadurch in der nächsten Inkarnation gewissen Menschen, denen ich Dienste leisten kann, diese Dienste wirklich werde leisten können, wenn ich diese Fähigkeiten habe.",
      "Man wird in einem solchen Falle in der Regel so entscheiden, daß man sich diese Fähigkeiten aneignet. Damit aber verletzt man diese Elementarwesen, die da rings herum sind. Die fühlen sich in einer gewissen Weise durch uns attackiert.",
      "Namentlich fühlen sie sich, wenn das geschieht, was gerade gesagt worden ist, daß wir uns gewisse Fähigkeiten aneignen, dadurch so verfinstert in ihrem Dasein, wie wenn ihnen an ihrer eigenen Weisheit etwas genommen wäre. Eine der Folgen, die oft eintritt, ist dann diese, daß, wenn wir wiedergeboren werden, wir einen oder mehrere Menschen auf der Erde besessen finden von diesen Elementarwesen, und ihnen be­sonders feindliche Absichten gegen uns eingegeben finden.",
      "Denken Sie sich, wie tief uns das hineinschauen läßt in das mensch­liche Erleben, und wie gründlich es uns lehrt, das menschliche Leben zu begreifen, uns wirklich den rechten Instinkt anzueignen, uns richtig",
      "zu verhalten auf dem physischen Plan. Das bedingt aber nicht, daß wir etwa immer, wenn wir nun auf dem physischen Plane sind, sagen:",
      "Nun ja, ich habe mich dazumal schützen müssen. Dadurch habe ich diese Feinde gegen mich heraufbeschworen, ich muß sie jetzt gewähren lassen. Es kann ja der Fall eintreten, wo es gut ist, sie gewähren zu lassen, es kann aber auch der andere Fall eintreten, daß, wenn wir sie gewähren lassen, diese feindlichen Elementarwesen, die durch diesen oder jenen Menschen wirken, sie durch das, was sie nun auf dem physischen Plan erreichen, sich reichlich Ausgleich schaffen für das, was man ihnen sozusagen durch den eigenen Schutz weggenommen hat; sie gehen über das hinaus, was man ihnen weggenommen hat. Und die Folge davon wurde sein, daß man sich ihnen gegenüber nicht retten kann, wenn man wiederum in der entsprechenden Zeit in den Zeitenstrom zwischen dem Tod und einer neuen Geburt eintritt, daß sie einen da in gewisser Weise für gewisse Fähigkeiten totschlagen würden.",
      "Immer komplizierter und komplizierter wird die Welt, wenn wir wirklich Einsicht in sie gewinnen. Aber das kann uns eigentlich im Grunde genommen gar nicht verwundern. Nur einzelne Fälle möchte ich noch aus dem karmischen Zusammenhang zwischen dem Leben auf der Erde und dem Leben zwischen dem Tod und einer neuen Geburt hervorheben. So sei der Fall hervorgehoben, daß bei einem Menschen, sagen wir, durch eine Krankheit, der Tod früher eintritt, als er nach einem normalen Menschenleben eintreten wurde. Da geht der Mensch so durch die Pforte des Todes durch, daß er durch die Krankheit zum Tode geführt worden ist, daß er aber gewisse Kräfte eigentlich bei sich behält, die er ausgelebt haben würde, wenn er ein normales Menschenleben erreicht hätte. Diese Kräfte, die auf diese Weise gleichsam dem Menschen als Restkräfte verbleiben, die er noch hätte verbrauchen können, wenn er nicht früher zugrunde gegangen wäre, die bleiben. Und es zeigt sich für die Geistesforschung, wenn man das Leben nach dem Tode untersucht, daß diese Kräfte zu den Willens- und Gefühiskräften des Menschen hinzugeschlagen werden, daß sie diese verstärken, erkraften. So daß ein solcher Mensch in der Lage ist, das, was ihm durch diese Kräfte vor der Mitternachtsstunde",
      "des Daseins zugeführt wird, nach der Mitternachtsstunde des Daseins so zu benutzen, daß er ins Erdenieben als ein stärkerer, in seinem Willen charaktervollerer und kraftvollerer Mensch eintritt, als er ein­getreten wäre, wenn er nicht einen so frühen Tod gefunden hätte. Daß das aber gerade so sein muß, hängt mit früherern Karma zu­sammen, und es wäre natürlich die größte Torheit, wenn jemand glauben wollte, daß er durch künstliches Herbeiführen eines frühen Todes das erreichen würde, was geschildert worden ist; dann würde er das nicht erreichen. Was durch dieses künstliche Herbeiführen eines frühen Todes erreicht wird, das finden Sie in meiner «Theosophie» beschrieben, soweit es notwendig ist, Aufschluß darüber zu erhalten. Auch habe ich auf den Fall hingedeutet, wo der Mensch einen frühen Tod durch einen Unglücksfall findet. Wenn er durch einen Unglücks­fall herausgerissen wird aus dem Erleben des physischen Planes, für den seine Kräfte noch zugereicht hätten, um ein höheres Alter zu erreichen, so bleibt ihm wiederum ein solcher Rest von Kräften, der ihm jetzt so zugesetzt wird, daß er, wenn die Mitternachtsstunde des Daseins verflossen ist, das, was ihm da zufließt, zu seinen intellektuellen Kräften, zu seinen Erkenntniskräften verwenden kann. Man findet durch die Geistesforschung, daß große Erfinder oftmals gerade solche Menschen sind, die in früheren Inkarnationen durch einen Unglücks­fall zugrunde gegangen sind.",
      "Wir sehen an solchen Fällen, daß, wenn wir diese Dinge wirklich verständnisvoll überblicken wollen, wir uns schon damit bekannt machen müssen, daß eben der Gesichtspunkt in der geistigen Welt wirklich ein anderer wird, als er es in der physischen Welt sein kann. Es wird Ihnen immer mehr und mehr begreiflich werden, daß man, um die geistige Welt zu verstehen, neue Vorstellungen und Begriffe herantragen muß, weil die geistigen Welten eben etwas ganz anderes sind als die physische Welt. Daher darf sich niemand wundern, wenn zunächst etwas, was von den geistigen Welten geschildert wird, so erscheint, daß, wenn man die Begriffe der physischen Welt auf das Geschilderte anwendet, man die Sache als unbefriedigend empfindet. Zum Beispiel ist es eine Tatsache, die die Geistesforschung in vielen Fällen bekräftigt, daß jemand, der mit materialistischer Gesinnung",
      "stirbt und Hinterbliebene zurückläßt, die auch materialistisch gesinnt sind, zunächst in der geistigen Welt eine gewisse Entbehrung erleidet. Wenn er durch die Pforte des Todes gegangen ist ohne spirituelle Gesinnung und zurückblicken will auf seine Lieben auf der Erde, so kann er, wenn in deren Seelen gar kein spiritueller Gedanke ist, nicht unmittelbar auf sie hinsehen; er weiß von ihnen nur bis zu dem Zeitpunkte, wo er durch den Tod gegangen ist. Was sie jetzt erleben unten auf der Erde, das kann sein geistiges Auge nicht sehen, weil in ihren Seelen nicht spirituelles Leben ist, denn nur spirituelles Leben wirft Licht hinauf in die geistigen Welten. Solch ein Mensch muß dann warten, bis ihm selber die Kräfte in der geistigen Welt erwachsen sind, um die Sache ganz klar zu sehen. Um nämlich zu sehen: diese Seelen, die er da unten zurückgelassen hat, die sind materialistisch gesinnt, weil sie von Ahriman befallen sind. Würde man das unmittelbar nach dem Tode gleich erleben, so würde man es nicht ertragen können. Man muß erst hineinwachsen in dieses von Ahriman Besessensein materialistisch gesinnter Seelen, dann kann ein Schauen dieser Seelen beginnen, bis auch sie durch die Pforte des Todes gegangen sind und sich dann selber frei machen in der geistigen Welt von ihrer materiali­stischen Gesinnung. Dann erlebt man erst später den Zusammenhang mit ihnen.",
      "Es könnte jemand sagen: Ja, aber das sind doch gar keine tröstlichen Verhältnisse, die du da schilderst als nach dem Tode verlaufend. Ja, meine lieben Freunde, das ist eben eine Vorstellung, die auf dem physischen Plan gewonnen ist, wenn wir so sprechen. Das ist keine Vorstellung, die schon von dem Verständnis der spitituelien Welten durchdrungen ist. Der Tote kommt zwischen dem Tod und einer neuen Geburt zu einem Zeitpunkt, wo er sich sagt: Oh, wie trostlos müßte es sein, gleich nach dem Tode diese Seelen zu sehen, wenn man materialistisch gesinnt ist! Wie ist es für all diese Seelen doch am besten, daß sie diese Prüfungszeit erst durchmachen! Sie würden sich selber verlieren, sie würden das nicht erreichen können, was erreicht werden soll, wenn es nicht so wäre. Der Gesichtspunkt wird eben ein ganz anderer, wenn man die Dinge der Welt von der geistigen Seite her betrachtet, und eine Zeit wird kommen, wo die Menschen notwendig",
      "haben werden, schon auf dem physischen Plan wirklich Ver­ständnis zu gewinnen für die Wahrheiten der Geisteswissenschaft.",
      "Darum tritt diese Geisteswissenschaft jetzt in der Welt auf, weil die Menschheitsentwicklung es notwendig macht, daß diese Durch­dringung der geistigen Welten und ihrer Daseinsbedingungen in den Seelen immer mehr und mehr, zuerst instinktiv und dann bewußt leben wird. Ich will Ihnen eine reine Äußerlichkeit mitteilen, damit Sie sehen, wie man immer mehr dazu kommen wird, auch das Leben auf dem physischen Plan nur dadurch in seinem wahren Gehalt beurteilen zu können, daß man die Gesetze des geistigen Daseins begreift, eine reine Äußerlichkeit, die aber ungeheuer wichtig ist.",
      "Wenn wir auf die Natur hinblicken, so sehen wir das merkwürdige Schauspiel, daß über­all nur eine geringe Anzahl von Keimen verwendet wird, um das gleichartige Leben fortzupflanzen, daß aber eine ungeheuer große Anzahl von Keimen zugrunde geht. Wir blicken hin auf das Heer der ungeheuer vielen Fischkeime, die im Meere vorhanden sind.",
      "Nur we­nige von ihnen werden Fische, die anderen gehen zugrunde. Wir sehen hinaus auf das Feld und sehen die ungeheuer vielen Kornkeime. Nur wenige werden wieder zu Kornpflanzen, die anderen gehen als Ge­treidekörner zugrunde, indem sie zu menschlicher Nahrung und ande­rem verwendet werden.",
      "Ungeheuer viel mehr muß in der Natur erzeugt werden als was sozusagen im gleichmäßig fortfließenden Strom des Daseins wirklich Frucht wird und wieder keimt. So ist es gut in der Natur, denn da draußen in der Natur herrscht die Ordnung und Not­wendigkeit, daß das, was so abfließt von seinem zu ihm gehörigen, in sich selbst begründeten Strom des Daseins und Fruchtens, ver­wendet wird, so verwendet wird, daß es dem anderen fortlaufenden Strom des Daseins dient.",
      "Die Wesen würden nicht leben können, wenn alle Keime wirklich fruchteten und zu der in ihnen liegenden Entwicklung kämen. Es müssen Keime da sein, welche dazu verwen­det werden, daß sozusagen Boden gegründet wird, aus dem die Wesen herauswachsen können.",
      "Nur scheinbar, der Maja nach, geht etwas verloren, in Wirklichkeit geht innerhalb des Naturschaffens doch nichts verloren. In dieser Natur waltet der Geist, und daß so scheinbar etwas vom fortlaufenden Strom der Entwicklung verlorengeht, das",
      "ist in der Weisheit des Geistes begründet, das ist geistiges Gesetz, und wir mussen diese Sache vom Standpunkt des Geistes ansehen. Dann kommen wir schon darauf, inwiefern auch das seine gute Daseins­berechtigung hat, was scheinbar vom fortlaufenden Strom des Welt­geschehens hinweggeführt wird. Geistgegründet ist dieses; daher kann es auch, insoferne wir geistiges Leben führen, auf dem physischen Plane Geltung haben.",
      "Meine lieben Freunde, nehmen Sie den uns ganz naheliegenden konkreten Fall: Es müssen öffentliche Vorträge gehalten werden über unsere Geisteswissenschaft. Die werden vor einem Publikum gehalten, das eben einfach durch die Veröffentlichungen zusammengetragen wird. Da geht etwas Ähnliches vor wie mit den Getreidekörnern, die nur zum Teil im fortlaufenden Strom des Daseins verwendet werden. Man darf nicht zurückschrecken davor, daß man unter Umständen vor viele, viele Menschen scheinbar ohne Wahl die Ströme des spiri­tuellen Lebens bringen muß, und daß sich dann nur wenige heraus-sondern und wirklich eintreten in dieses spirituelle Leben, Anthro­posophen werden und im fortlaufenden Strome mitgehen. Auf diesem Gebiete ist es noch so, daß diese verstreuten Keime an viele heran-dringen, welche zum Beispiel nach einem öffentlichen Vortrage weg­gehen und sagen: Was hat der Kerl da für tollen Unsinn geschwatzt! Unmittelbar angeschaut in bezug auf das äußere Leben, ist das so wie, sagen wir, die Keime, die im Meer als Fischkeime verlorengehen; aber vom Standpunkt einer tieferen Forschung ist es nicht so. Die Seelen, die da gekommen sind durch ihr Karma, die dann fortgehen und sagen:",
      "Was hat der Kerl da für tollen Unsinn geschwatzt! - die sind noch nicht reif, die Wahrheit des Geistes zu empfangen, aber notwendig haben es ihre Seelen in der jetzigen Inkarnation, heranschwingen zu fühlen das, was als Kraft in dieser Geisteswissenschaft liegt. Und das bleibt doch in ihren Seelen, sie mögen noch so schimpfen, es bleibt als Kraft in ihren Seelen für ihre nächste Inkarnation, und dann sind die Keime nicht verloren, sie finden Wege. Es unterliegt das Dasein in bezug auf das Geistige den gleichen Gesetzen, ob wir dieses Geistige in der Naturordnung verfolgen oder in dem Fall, den wir als unseren eigenen Fall anführen konnten.",
      "Aber nehmen wir jetzt an, wir wollten die Sache auch auf das äußere materielle Leben übertragen und man wollte sagen: Nun, man macht es im äußeren Leben ebenso. Ja, meine lieben Freunde, das ist es gerade, daß man es macht, was ich jetzt schildern werde, daß wir einer Zukunft entgegenleben, wo sich das immer mehr herausbildet! Man produziert immer mehr und mehr darauf los, man gründet Fabriken, man fragt nicht: Wieviel wird gebraucht? - wie es einmal der Fall war, als es Schneider im Dorf gab, die nur dann einen Anzug machten, wenn er bestellt wurde. Da war es der Konsument, der angab, wieviel erzeugt werden soll, jetzt wird für den Markt produziert, die Waren werden zusammengestapelt, soviel als nur möglich. Die Produktion arbeitet ganz nach dem Prinzip, nach dem die Natur schafft. Die Natur wird in die soziale Ordnung hinein fortgesetzt. Das wird zunächst immer mehr überhandnehmen. Aber hier betreten wir das Feld des Materiel­len. Im äußeren Leben hat das geistige Gesetz, weil es eben für die geistige Welt gilt, keine Anwendung, und es entsteht etwas sehr Merk­würdiges. Da wir unter uns sind, können wir ja solche Dinge sagen. Die Welt freilich wird uns heute darin kein Verständnis entgegen­bringen.",
      "Es wird also heute für den Markt ohne Rücksicht auf den Konsum produziert, nicht im Sinne dessen, was in meinem Aufsatz «Geistes­wissenschaft und soziale Frage» ausgeführt worden ist, sondern man stapelt in den Lagerhäusern und durch die Geldmärkte alles zusammen, was produziert wird, und dann wartet man, wieviel gekauft wird. Diese Tendenz wird immer größer werden, bis sie sich - wenn ich jetzt das Folgende sagen werde, werden Sie finden, warum - in sich selber vernichten wird. Es entsteht dadurch, daß diese Art von Pro­duktion im sozialen Leben eintritt, im sozialen Zusammenhang der Menschen auf der Erde genau dasselbe, was im Organismus entsteht, wenn so ein Karzinom entsteht. Ganz genau dasselbe, eine Krebsbil­dung, eine Karzinombildung, Kulturkrebs, Kulturkarzinom! So eine Krebsbildung schaut derjenige, der das soziale Leben geistig durchblickt, wie überall furchtbare Anlagen zu sozialen Geschwürbildungen aufsprossen. Das ist die große Kultursorge, die auftritt für den, der das Dasein durchschaut. Das ist das Furchtbare, was so bedrückend",
      "wirkt, und was selbst dann, wenn man sonst allen Enthusiasmus für Geisteswissenschaft unterdrücken könnte, wenn man unterdrücken könnte das, was den Mund öffnen kann für die Geisteswissenschaft, einen dahin bringt, das Heilmittel der Welt gleichsam entgegenzu­schreien für das, was so stark schon im Anzug ist und was immer stärker und stärker werden wird. Was auf seinem Felde in dem Ver­breiten geistiger Wahrheiten in einer Sphäre sein muß, die wie die Natur schafft, das wird zur Krebsbildung, wenn es in der geschilderten Weise in die Kultur eintritt.",
      "Das zu durchschauen und dann Abhilfe zu schaffen wird erst mög­lich sein, wenn Geisteswissenschaft die Herzen ergreift, die Seelen durchdringt. Und man möchte, wenn man diese Dinge durchschaut, das allerintensivste Feuer haben, um es in seine Worte zu legen, um unsere Zeitgenossen, so viele es verstehen können, aufmerksam zu machen, welcher Zeit wir entgegengehen! Einsehen kann man diese Dinge nur, wenn man sich bekannt macht mit den verschiedenen Gesichtspunkten, welche existieren, einmal für das eine Feld des Da­seins, das andere Mal für das andere. Demjenigen, der in dem Erleben zwischen der Mitternachtsstunde und einer neuen Geburt steht, dem treten diese anderen Gesichtspunkte entgegen, denn aus diesen ande­ren Gesichtspunkten heraus muß er selber schaffend werden.",
      "Wenn der Mensch die Tendenzen gebildet hat zum Vollzuge des Karmas in bezug auf die ihm nächststehenden Erlebnisse, dann treten die weiteren Erlebnisse, die mehr ferne stehen, vor der Seele auf. Religionsgemeinschaft, andere Gemeinschaften, denen man angehört hat, die erlebt man dann so, daß sie zeigen: Du mußt nun, damit du nicht einseitig wirst, das oder jenes in der folgenden Inkarnation tun. Kurz, dieses Leben verfließt dann so, daß es zwar auch noch ab-wechselt zwischen geistiger Geselligkeit und geistiger Einsamkeit, daß es aber wesentlich dahin geht, daß man sich das Urbild für ein neues Erdenleben, rein geistig zunächst, aufbaut.",
      "Lange bevor man zu diesem Erdenleben heruntersteigt, hat man aus der geistigen Welt heraus, ein geistig-ätherisches Urbild auferbaut, das die Kräfte in sich trägt, die man geistig-magnetische Kräfte nennen könnte, die einen hinunterziehen zu einem Elternpaar, von",
      "dem man fühlt: Es gibt uns die Vererbungsmerkraale, damit wir in einem neuen Erdenleben auftreten können. Ich habe schon angedeutet, daß der normale Zeitpunkt der ist, in dem wir das Gefühl haben:",
      "Wir vereinigen uns mit dem, was sich gefernt hat als unsere Lebens-frucht des letzten Erdenlebens. Aber der Mensch kommt nicht immer bis zu diesem. Unser Leben verfließt dann so, daß wir vollständig den Zusammenhang fühlen würden zwischen dem Leiblichen und Geisti­gen, wenn wir bis zu diesem Zeitpunkt gelangten, aber der Mensch tritt meistens früher ins Dasein. Die meisten Menschen sind geistige Frühgeburten, und es gleicht sich erst später dadurch aus, daß wir solche Erlebnisse haben, in denen wir vollständig harmonisch wieder zusammenfließen mit den Früchten unserer früheren Erdenleben.",
      "Eines aber ist von ganz besonderer Wichtigkeit. Ich habe es gestern dargestellt: Da, wo unsere Sehnsucht am größten sein muß nach Außenwelt, weil wir am meisten in die Einsamkeit eingetreten sind in der Mitternachtsstunde des geistigen Daseins, da ist es dasjenige, was eigentlich nur in den geistigen Welten wallt und wogt und lebt, da ist es der Geist, der an uns herantritt und unsere Sehnsucht in eine Art von Seelenlicht verwandelt.",
      "Bis zu diesem Zeitpunkt müssen wir den Zusammenhang mit unserem Ich bewahren. Wir müssen gleich­sam die eine Erinnerung bewahren: Du warst auf Erden dieses Ich. Dieses Ich muß einem als Erinnerung bleiben.",
      "Daß man das kann in unserem Zeitenzyklus, hängt davon ab, daß der Christus die Kraft in die Erdenaura hineingebracht hat, welche sonst nicht aus dem irdi­schen Leben mitgebracht würde, die Kraft, die uns befähigt, die Er­innerung bis zur Mitternachtsstunde zu bewahren. Es würde zer­reißend, sozusagen eine Kluft sein, die unser Dasein zu einem un­harmonischen in der Mitte zwischen dem Tod und einer neuen Geburt machen würde, wenn der Christusimpuls nicht durch die Erdenwelt flösse.",
      "Lange bevor die Mitternachtsstunde eintritt, würden wir ver­gessen, daß wir ein Ich gewesen sind im letzten Leben. Wir würden den Zusammenhang mit der geistigen Welt fühlen, würden aber uns vergessen. Und das ist dadurch bewirkt, daß wir auf Erden eben wirklich unser Ich so stark entwickeln.",
      "Daß wir immer mehr und mehr zu diesem Ichbewußtsein kommen, das ist notwendig geworden",
      "seit dem Mysterium von Golgatha. Aber indem wir auf Erden immer mehr und mehr zu unserem Ichbewußtsein kommen, verbrauchen wir die Kräfte, die wir nötig haben nach dem Tode, damit wir wirklich bis zur Mitternachtsstunde des Daseins uns nicht vergessen. Daß wir diese Erinnerung bewahren können, dazu müssen wir in den Christus hinein sterben. So mußte der Christusimpuls da sein: er erhält uns bis zur Mitternachtsstunde des Daseins die Möglichkeit, unser Ich nicht zu vergessen.",
      "Dann kommt in der Mitternachtsstunde des Daseins der Geist an uns heran. Nun haben wir die Erinnerung an unser Ich bewahrt. Wenn wir sie hineintragen bis zur Mitternachtsstunde des Daseins, bis dahin, wo der Heilige Geist an uns herankommt und uns den Rückblick und den Zusammenhang mit unserer eigenen inneren Welt wie mit einer äußeren Welt gibt, wenn wir diesen Zusammenhang bewahrt haben, dann kann uns der Geist nunmehr bis zu unserer Wiederverkörperung leiten, die wir dadurch herbeiführen, daß wir unser Urbild in der geistigen Welt bilden.",
      "Aber nun geschehen ja die Dinge in der Wirklichkeit nicht so, daß man gewissermaßen nur das Allernotwendigste tut. Denn, wie der Pendel nicht ruhig ist, sondern ausschlägt, um wiederum nach der anderen Seite auszuschlagen, und wie es richtig ist, daß es so geschieht, so ist es auch mit dem Geistes­leben.",
      "Der Christusimpuls stattet uns nicht bloß mit solcher Kraft aus, daß wir gerade knapp den Anschluß finden, sondern er gibt uns unter Umständen so viel, daß, wenn der Geist nicht an uns heran-treten würde, der Christusimpuls uns hinüberschnellen könnte. Mit der Erinnerung allerdings würden wir den Anschluß nicht finden können, aber hinüberschnellen würde uns der Christusimpuls.",
      "Das hat seine große Bedeutung, und daß wir einen solchen, das notwen­digste Maß überschreitenden Impuls von dem Christus her aufnehmen, das wird dem Menschen immer mehr und mehr nötig sein, indem er sich in die Zukunft hinein entwickelt. Jetzt schon ist es notwendig, daß der Mensch gewissermaßen während seines Erdenlebens nicht nur das Allernotwendigste über den Christus erfährt, sondern daß der Christusimpuls als mächtiger Impuls in seine Seele sich setzt, so daß er ihn noch hinüberschnellt über die Mitternachtsstunde des Daseins.",
      "Denn dadurch verstärkt sich der Impuls des Geistes durch den Impuls des Christus, und wir tragen den Impuls des Geistes stärker durch die zweite Hälfte des Lebens zwischen dem Tod und einer neuen Geburt hindurch, als wir ihn sonst hindurchtragen würden, wenn der Chri­stusimpuls nicht wäre.",
      "Was uns übrig bleibt von dem Impuls des Christus, das verstärkt den Impuls des Geistes. Der Geist wäre Sonst nur für den Geist und er würde aufhören zu wirken, indem wir geboren würden. Indem wir uns mit dem Christusimpuls durchdringen, verstärkt der Christus-impuls den Impuls des Heiligen Geistes.",
      "Und dadurch kann auch in unsere Seele ein solcher Impuls des Geistes hereingebracht werden, der dann, wenn wir in die irdische Inkarnation eintreten, eine Kraft ist, die wir nicht verbrauchen wie sonst die Kräfte, die wir mitbringen durch die Geburt, in der irdischen Inkarnation. Das habe ich ja be­tont, daß wir die Kräfte, die wir aus der geistigen Welt heraus bringen, umwandeln zu unserer inneren Organisation.",
      "Aber das, was wir auf diese Weise als ein Plus bekommen, als ein Mehr, indem der Christus-impuls den Geistesimpuls verstärkt, das tragen wir herein ins Dasein, das braucht nun nicht umgewandelt zu werden während des irdischen Erlebens. Immer mehr und mehr Menschen werden für die Erden-entwicklung notwendig sein, je mehr wir der Zukunft entgegengehen, die so etwas von der Durchdringung des Christus-Impulses und des geistigen Impulses hereintragen in das irdische Leben durch ihre Ge­burt bei einer neuen Inkarnation.",
      "Der Geist, er muß stärker wirken, damit er nicht nur wirkt bis zu der Geburt hin und alles aus dem geistigen Leben heraus umgesetzt wird in innere organisierende Kräfte, so daß uns nur das bißchen Bewußtsein bleibt, das uns Er­kenntnis lehrt über unsere physische Umgebung und über das, was der Verstand ergreifen kann, der an das Gehirn gebunden ist. Würden wir als Menschen, indem wir uns der Zukunft entgegen entwickeln, nicht nach und nach einen Überschuß an Geist, der auf die geschilderte Weise entsteht, mitbringen, dann würde die Menschheit auf der Erde immer mehr dazu kommen, während des irdischen Lebens nichts mehr davon zu ahnen, daß es einen Geist gibt.",
      "Dann würde während des irdischen Lebens nur der ungeistige Geist, Ahriman, herrschen und",
      "die Menschen würden nur wissen können von der sinnlich-physischen Welt, die man mit den Sinnen wahrnimmt, und von dem, was man mit dem Verstande begreifen kann, der an das Gehirn gebunden ist. Alle solche Dinge erleben in einer gewissen Weise doch in der Fort­entwicklung der Menschen eine Ausbildung gerade jetzt, wo die Menschheit vor der Gefahr steht, den Heiligen Geist zu verlieren.",
      "Aber sie wird ihn nicht verlieren. Wächter dafür will die Geistes­wissenschaft sein, daß die Menschheit diesen Geist nicht verliert, die­sen Geist, der in der Mitternachtsstunde des Daseins an die Seele herantritt, um in ihr die Sehnsucht zu beleben, daß sie sich selbst in ihrer Vergangenheit in ihrem ganzen Wert erblicke.",
      "Nein, Geistes­wissenschaft wird von dem Christus-Impuls immer mehr, immer ein­dringlicher reden müssen, so daß immer mehr und mehr Geist in immer mehr und mehr Menschen durch die Geburt auch ins physische Dasein hereinkommt, und daß in diesem physischen Dasein immer mehr Menschen erstehen, die fühlen: Ich habe allerdings in mir die Kräfte, die umgewandelt werden müssen in organisierende Kräfte, aber da leuchtet etwas auf in meiner Seele, das nicht umgewandelt zu werden braucht. Der Geist, der nur für die geistigen Welten ist, ich habe etwas von ihm mitgenommen in diese physische Welt, trotzdem ich in meinem Leibe lebe.",
      "Der Geist wird es sein, der die Menschen dazu bringt, zu schauen, was in meinem Mysteriendrama «Die Pforte der Einweihung» von der Theodora gesagt wird: Daß Menschen die Äthergestalt des Christus schauen werden. Die Kraft des Geistes, die so in die Leiber hereinkommt, die wird das geistige Auge abgeben, um die geistigen Welten zu sehen und zu verstehen.",
      "Zuerst wird man sie verstehen müssen, dann wird man beginnen, sie mit Verständnis zu schauen. Denn das Schauen wird herankommen, weil der Geist die Seelen so ergreift, daß sie diesen Geist hereinbringen werden in die Leiber, und auch in ihren irdischen Inkarnationen wird der Geist aufleuchten: erst bei wenigen, dann bei mehreren wird der Geist auf­leuchten.",
      "Und können wir auf der einen Seite sagen: Durch den Geist, durch den Heiligen Geist werden wir erweckt in der großen Mitter­nachtsstunde des Daseins, so müssen wir auf der andern Seite sagen, hinblickend auf das, was der Geist in der Erdenentwicklung für die",
      "Zukunft leistet: Auch im physischen Leib wird das Beste der Seele, das, was den Ausblick gibt in die geistigen Welten, durch den Heiligen Geist immer mehr und mehr auferweckt werden. Auferweckt durch den Heiligen Geist in der Mitternachtsstunde des Daseins, wird der Mensch auch auferweckt werden, wenn er in seinem physischen Leibe lebt, wenn er sich hereiniebt in das physische Dasein. Er wird innerlich erwachen, indem ihn der Geist auferweckt aus dem Schlafe, in dem er sonst befangen wäre mit dem bloßen Anschauen der Sinneswelt und mit dem Verstande, der an das Gehirn gebunden ist. Schlafen würden die Menschen immer durch die bloße Sinnesanschauung und durch den an das Gehirn gebundenen Verstand. Aber hineinleuchten in diesen Menschenschlaf, der sonst die Menschheit gegen die Zukunft hin immer mehr umdüsternd überkommen würde, hineinleuchten in diesen Schlaf wird der Geist im Menschen auch während des physi­schen Daseins. Mitten in dem absterbenden geistigen Leben, mitten in dem durch die bloße Sinnesanschauung, durch die Verstandeswelt absterbenden Geistesleben auf dem physischen Plan werden die Menschenseelen auferweckt werden auch im physischen Dasein durch den Heiligen Geist.",
      "Per spiritum sanctum reviviscimus."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "In diesem meinem letzten Vortrag möchte ich da fortfahren, wo wir gestern geendet haben.",
        "Geendet haben wir bei dem, was ich mir zu benennen erlaubte «die große Weltenmitternachtsstunde des geistigen Daseins zwischen dem Tod und einer neuen Geburt», jene Mitter­nachtsstunde, wo das menschliche innere Erleben am intensivsten wird und das, was wir geistige Geselligkeit nennen können, das Zu­sammenhängen mit der geistigen Außenwelt, den niedrigsten Grad erreicht hat, so daß in gewisser Beziehung während dieser Mitter­nachtsstunde des geistigen Daseins geistige Finsternis um uns ist."
      ],
      [
        "Aber gesagt worden ist, daß die Sehnsucht nach Außenwelt wiederum in uns wirkt, und daß diese Sehnsucht durch den Geist, der in geistigen Welten wirkt, aktiv wird, und daß diese Sehnsucht ein neues Seelen-licht aus uns erzeugt, sodaß es uns möglich wird, jetzt eine Außenwelt von ganz besonderer Art zu erblicken.",
        "Diese Außenwelt, die wir dann erblicken, ist unsere eigene Vergangenheit, wie sie durch frühere Inkarnationen und die Zwischenzeiten zwischen den Toden und den neuen Geburten sich vollzogen hat, und die wir jetzt als eine äußere Welt überschauen, indem wir zurückblicken auf das, was wir aus dem Weltendasein gehabt haben, genossen haben, und auf das, was wir diesem Weltendasein schuldig geblieben sind."
      ],
      [
        "Insbesondere tritt uns dann, wenn wir diesen Rückblick in unsere früheren Erlebnisse haben, zweierlei mit großer Intensität entgegen.",
        "Wir haben - das zeigt sich uns gleichsam durch ein geistiges Anschauen - dieses und jenes ge­nossen, dieses und jenes ist uns beschert worden an Freude, an Lust des Daseins."
      ],
      [
        "Das alles können wir übersehen, was uns jemals geworden ist an Freude, an Lust des Daseins.",
        "Aber wir übersehen es so, daß es uns gleichsam in seinem spirituellen Wert erscheint, daß es uns in bezug darauf erscheint, was es aus uns gemacht hat."
      ],
      [
        "Nehmen wir einen konkreten Fall an.",
        "Wir blicken zurück auf etwas, was uns als Genuß, als Befriedigang in der verflossenen Zeit in irgend einem unserer Daseinsleben zuteil geworden ist.",
        "Dann fühlen wir:"
      ],
      [
        "Das ist nicht etwas Vergangenes, es ist zwar in der Zeit zurückliegend, daß du davon den Genuß hattest, aber es ist nicht etwas, was absolut vergangen ist.",
        "Es ist etwas, was seine Wirkung in alle Zeiten hinein fortsetzt, so fortsetzt, daß es darauf wartet, was wir daraus machen."
      ],
      [
        "Wenn wir eine Befriedigung, einen Genuß gehabt haben, so fühlen wir in uns, wir erleben es unmittelbar in unserem Seelensein bei diesem Zurückschauen: Das muß eine Kraft in dir werden, eine Kraft deiner Seele, und diese Kraft deiner Seele, die kannst du in zweierlei Weise in dir wirken lassen.",
        "Jetzt in diesem geistigen Dasein nach der Weltenmitternacht, in dem du stehst, hast du diese zweifache Möglich­keit."
      ],
      [
        "Die geistige Welt gibt dir einfach Fähigkeiten, eine von diesen Möglichkeiten zur Wirklichkeit zu machen.",
        "Du kannst diesen ver­gangenen Genuß, diese vergangene Befriedigung in dir umwandeln in eine Fähigkeit, so daß du eine gewisse Kraft in deiner Seele ent­wickelst durch den verflossenen Genuß, die dich zu diesem oder jenem befähigt, wodurch du irgend etwas in der Welt, sei es das Kleinste, sei es das Größte, schaffst, das einen Wert für die Welt hat."
      ],
      [
        "Das ist das eine.",
        "Das andere ist, daß wir uns sagen können: Nun, den Genuß habe ich gehabt, ich will mit dem Genuß zufrieden sein, ich will den Genuß in meine Seele hereinnehmen und will mich laben daran, daß ich in der Vergangenheit diesen Genuß gehabt habe."
      ],
      [
        "Wenn wir mit vielem, was wir genossen haben, was uns befriedigt hat, eine solche Möglichkeit herbeiführen, dann kommt es dazu, daß wir in unserem Innern eine Kraft schaffen, an der wir nach und nach geistig degenerieren, ersticken.",
        "Und das gehört zu dem Wichtigsten, was wir lernen können in der geistigen Welt, daß wir auch durch den Genuß, durch das, wodurch wir befriedigt werden, Schuldner werden des Weltendaseins."
      ],
      [
        "Die Aussicht tritt vor unser geistiges Auge, zu ersticken in den Nachwirkungen der Befriedigungen, der Genüsse, wenn wir uns nicht im rechten Zeitpunkt entschließen, aus verflosse­nen Befriedigungen, aus verflossenen Genüssen Fähigkeiten zu schaffen, die Wertvolles im Leben hervorbringen können.",
        "Sie sehen daraus wiederum, wie das Geistige und das, was auf dem physischen Plan geschieht, in Wechselwirkung steht."
      ],
      [
        "Wer sich, im Sinne des vorgestrigen Vortrags, immer mehr und"
      ],
      [
        "mehr mit den Erkenntnissen der Geisteswissenschaft durchdringt, bei dem wird diese Geisteswissenschaft in das instinktive Leben seiner Seele übergehen, und er wird gewissermaßen wie die Regung eines inneren Gewissens auch gegenüber den Genüssen, gegenüber den Befriedigungen, die er auf dem physischen Plane hat, die Stimmung entwickeln: Du darfst nicht nur um deiner 6elbst willen irgend einen Genuß, eine Freude, eine Lust hinnehmen, sondern er wird diese Lust durchdringen mit einer Art von Dankbarkeitsgefühl gegenüber dem Weltenall, gegenüber den geistigen Mächten des Weltenalls.",
        "Denn er wird wissen, daß er durch jeden Genuß, durch jede Befriedigung ein Schuldner des Weltenalls wird.",
        "Am leichtesten und sichersten kommen wir zurecht mit der Umwandlung derjenigen Genüsse und Freuden, welche geistiger Art sind.",
        "Solche Genüsse und Lüste, welche nur be­friedigt werden können durch die leiblichen Werkzeuge oder über­haupt nur dadurch, daß der Mensch auf dem physischen Plan einen Leib an sich trägt, stehen zwar auch in der angedeuteten Zeit zwischen dem Tod und einer neuen Geburt als etwas vor uns, was umgewandelt werden muß, wenn wir nicht nach und nach gewissermaßen darin ersticken wollen.",
        "Wir fühlen die Notwendigkeit der Umwandlung, aber wir fühlen auch das eine, daß viele Inkarnationen notwendig sein werden, damit wir zwischen diesen Inkarnationen immer wieder in der geistigen Welt sind und endlich die Umwandlung bewirken können."
      ],
      [
        "Dann finden wir in der geistigen Welt noch etwas anderes.",
        "Wir finden das, daß wir in unserem gegenwärtigen Menschheitszyklus mit solchen Genüssen, mit solchen Freuden, in denen auf dem physischen Plan gleichsam unser Seelisch-Geistiges ganz untergeht, und der Genuß, die Befriedigung einen untermenschlichen, ich will nicht sagen, tierischen Charakter annimmt - denn Freude und Genuß können untermenschlichen Charakter annehmen -, daß wir in der Tat mit solchen Genüssen gewissen Wesenheiten der geistigen Welt unendli­chen Schmerz bereiten, die uns erst dann entgegentreten, wenn wir eben in diese geistige Welt eintreten.",
        "Und der Anblick dieses Schmer­zes, den wir in der geistigen Welt gewissen Wesenheiten bereiten, der ist so ungeheuer bestürzend, bedrückend, unsere Seele mit solchen Kräften durchziehend, daß wir mit dem harmonischen Ausbilden der"
      ],
      [
        "Zusammenhänge für die nächste Inkarnation keineswegs gut zurecht­kommen."
      ],
      [
        "Gegenüber dem, um das andere zu erörtern, was wir auf Erden an Schmerzen, an Leiden erleben, zeigt sich auf dem geistigen Plan, daß auf dem physischen Plane erduldete Schmerzen, erduldetes Leid fort-wirken und auf dem geistigen Plan unsere Seele so durchdringen mit Kräften, daß diese Kräfte Willenskräfte werden, daß wir dadurch in der Seele stärker werden und die Möglichkeit haben, diese Stärke in moralische Kraft umzuwandeln, die wir dann wiederum auf den physischen Plan mitbringen können, um nicht nur gewisse Fähig­keiten zu haben, durch die wir Wertvolles schaffen können für die Umwelt, sondern um auch die moralische Kraft zu haben, charakter­voll diese Fähigkeiten auszuleben."
      ],
      [
        "Solche und viele andere Erlebnisse haben wir unmittelbar nach der geistigen Mitternachtsstunde des Daseins.",
        "Wir erfühlen, erleben, was wir wert geworden sind durch unser verflossenes Dasein, wir erfühlen, erleben, zu welchen Fähigkeiten wir kommen können in der Zukunft.",
        "Nachdem wir dann eine Weile weiterleben in der geistigen Welt, tritt aus dem Dämmerdunkel der geistigen Umgebung heraus eine deut­liche Anschauung, jetzt nicht nur unserer eigenen verflossenen Leben, sondern namentlich alles des Menschlichen, was mit diesen Leben verbunden war, und zwar alles desjenigen Menschlichen, was näher mit diesen Leben verbunden war.",
        "Menschen treten in geistige Be­ziehungen zu uns, mit denen wir in früheren Daseinsstufen diese oder jene Beziehung hatten.",
        "Nicht als ob früher die Gemeinsamkeit mit diesen Menschen nicht da gewesen wäre - wir erleben uns immer zusammen mit den Menschen, die uns im Leben nahegestanden haben, in der weitaus größten Zeit zwischen dem Tod und einer neuen Ge­burt -, aber jetzt tritt, indem wir diese Menschen nach der Mitter­nachtsstunde des geistigen Daseins wieder treffen, deutlich und klar an diesen Menschen hervor, was wir ihnen schuldig geworden sind, oder was sie uns schuldig geworden sind.",
        "Wir erleben jetzt nicht bloß eine Anschauung: So standest du mit diesen Menschen zwischen dieser und jener Zeit - das hatten wir früher auch -, sondern diese Menschen werden für uns der Ausdruck für das, was Ausgleich ist für die früheren"
      ],
      [
        "Erlebnisse.",
        "Wir sehen es den Menschen an, 50 wie sie uns entgegen­treten, durch welche neuen Erlebnisse auf dem physischen Plane wir für Früheres Ausgleich schaffen können, was wir ihnen schuldig geblieben sind oder dergleichen.",
        "Wir schauen sozusagen, indem wir den Seelen der Menschen gegenüberstehen, auf die Wirkungen, welche in der Zu­kunft die Folgen sein werden von Beziehungen, die wir zu den Men­schen in der Vergangenheit gehabt haben.",
        "Natürlich sieht man das am besten ein, wenn man einen möglichst konkreten Einzelfall nimmt."
      ],
      [
        "Nehmen wir also noch einmal an, wir hätten einen Menschen ange­logen.",
        "Jetzt ist die Zeit, wo die Möglichkeit in der geistigen Welt geboten ist, daß wir durch die unserer Lüge entgegengesetzte Wahr­heit gequält werden."
      ],
      [
        "Aber dadurch werden wir gequält, daß sich die Beziehung zu dem Menschen, den wir angelogen haben, in der jetzt geschilderten Zeit so verändert, so oft wir den Menschen erblicken -und wir werden ihn genügend oft mit dem geistigen Auge erblicken -, daß er die Ursache wird, daß die der vollbrachten Lüge entgegen­gesetzte Wahrheit, die uns quält, in uns aufsteigt.",
        "Dadurch taucht aus unseren Tiefen die Tendenz herauf: Diesem Menschen mußt du unten auf der Erde wieder begegnen, und du mußt etwas tun, was das Un­recht ausgleicht, das du durch die vollzogene Lüge begangen hast."
      ],
      [
        "Denn hier in der geistigen Welt kann das nicht ausgeglichen werden, was durch deine Lüge geschaffen worden ist, da im Kosmos kannst du nur völlige Klarheit gewinnen über die Wirkung einer Lüge.",
        "Was auf Erden geschaffen worden ist von dieser Art, das muß auch wie­derum auf der Erde ausgeglichen werden."
      ],
      [
        "Man weiß, man braucht zum Ausgleich Kräfte in sich selber, die einem nur werden können, wenn man wiederum einen Erdenleib bezieht.",
        "Dadurch entsteht in unserer Seele die Tendenz: Du mußt einen Erdenleib beziehen, der die Möglichkeit bietet, eine solche Tat zu vollbringen, wodurch die Unvollkommenheiten ausgeglichen werden, die du auf Erden ver­ursacht hast, sonst wird, wenn du durch den nächsten Tod gegangen bist, dieser Mensch wiederum dir erscheinen und die Qual der Wahr­heit hervorrufen."
      ],
      [
        "Sie sehen die ganze geistige Technik, wie in der geistigen Welt der Trieb in uns geschaffen wird, einen karmischen Ausgleich für das oder jenes zu schaffen."
      ],
      [
        "Diese Ausgleiche geschehen auch durch andere Voraussetzungen; aber ich müßte natürlich tausend und abertausend konkrete Fälle auf­zählen, wenn ich alles zum Vorschein bringen wollte, was für diese bedeutsame karmische Frage in Betracht kommt.",
        "Nehmen wir zum Beispiel den folgenden Fall."
      ],
      [
        "Nehmen wir an, wir sind in der Zeit, die auf die Mitternachtsstunde des Daseins folgt, so in der geistigen Welt, daß wir zurückblicken auf gewisse Freuden, die wir gehabt haben und sagen: Wir können die Wirkungen dieser Erlebnisse in Fähigkeiten umwandeln, die wir dann ausdrücken können, wenn wir wieder ver­leiblicht sein werden.",
        "Ja, dann kann aber folgendes geschehen."
      ],
      [
        "Wir können bemerken: Indem du dir jetzt in deiner gegenwärtigen Lage diese verflossenen Erlebnisse umwandelst in Fähigkeiten, da stören dich gewisse Elementarwesen.",
        "Das kann so sein.",
        "Diese Elementarwesen lassen es nicht dazu kommen, daß du dir diese Fähigkeiten wirklich aneignest."
      ],
      [
        "Jetzt kann man sich fragen: Was ist nun zu tun?",
        "Wenn ich diesen Elementarwesen wilifahre, die da herankommen und die mcht leiden können, daß in mir diese Fähigkeiten entstehen, dann werde ich mir diese Fähigkeiten nicht bilden können."
      ],
      [
        "Aber diese Fähigkeiten muß ich mir bilden.",
        "Ich weiß, daß ich nur dadurch in der nächsten Inkarnation gewissen Menschen, denen ich Dienste leisten kann, diese Dienste wirklich werde leisten können, wenn ich diese Fähigkeiten habe."
      ],
      [
        "Man wird in einem solchen Falle in der Regel so entscheiden, daß man sich diese Fähigkeiten aneignet.",
        "Damit aber verletzt man diese Elementarwesen, die da rings herum sind.",
        "Die fühlen sich in einer gewissen Weise durch uns attackiert."
      ],
      [
        "Namentlich fühlen sie sich, wenn das geschieht, was gerade gesagt worden ist, daß wir uns gewisse Fähigkeiten aneignen, dadurch so verfinstert in ihrem Dasein, wie wenn ihnen an ihrer eigenen Weisheit etwas genommen wäre.",
        "Eine der Folgen, die oft eintritt, ist dann diese, daß, wenn wir wiedergeboren werden, wir einen oder mehrere Menschen auf der Erde besessen finden von diesen Elementarwesen, und ihnen be­sonders feindliche Absichten gegen uns eingegeben finden."
      ],
      [
        "Denken Sie sich, wie tief uns das hineinschauen läßt in das mensch­liche Erleben, und wie gründlich es uns lehrt, das menschliche Leben zu begreifen, uns wirklich den rechten Instinkt anzueignen, uns richtig"
      ],
      [
        "zu verhalten auf dem physischen Plan.",
        "Das bedingt aber nicht, daß wir etwa immer, wenn wir nun auf dem physischen Plane sind, sagen:"
      ],
      [
        "Nun ja, ich habe mich dazumal schützen müssen.",
        "Dadurch habe ich diese Feinde gegen mich heraufbeschworen, ich muß sie jetzt gewähren lassen.",
        "Es kann ja der Fall eintreten, wo es gut ist, sie gewähren zu lassen, es kann aber auch der andere Fall eintreten, daß, wenn wir sie gewähren lassen, diese feindlichen Elementarwesen, die durch diesen oder jenen Menschen wirken, sie durch das, was sie nun auf dem physischen Plan erreichen, sich reichlich Ausgleich schaffen für das, was man ihnen sozusagen durch den eigenen Schutz weggenommen hat; sie gehen über das hinaus, was man ihnen weggenommen hat.",
        "Und die Folge davon wurde sein, daß man sich ihnen gegenüber nicht retten kann, wenn man wiederum in der entsprechenden Zeit in den Zeitenstrom zwischen dem Tod und einer neuen Geburt eintritt, daß sie einen da in gewisser Weise für gewisse Fähigkeiten totschlagen würden."
      ],
      [
        "Immer komplizierter und komplizierter wird die Welt, wenn wir wirklich Einsicht in sie gewinnen.",
        "Aber das kann uns eigentlich im Grunde genommen gar nicht verwundern.",
        "Nur einzelne Fälle möchte ich noch aus dem karmischen Zusammenhang zwischen dem Leben auf der Erde und dem Leben zwischen dem Tod und einer neuen Geburt hervorheben.",
        "So sei der Fall hervorgehoben, daß bei einem Menschen, sagen wir, durch eine Krankheit, der Tod früher eintritt, als er nach einem normalen Menschenleben eintreten wurde.",
        "Da geht der Mensch so durch die Pforte des Todes durch, daß er durch die Krankheit zum Tode geführt worden ist, daß er aber gewisse Kräfte eigentlich bei sich behält, die er ausgelebt haben würde, wenn er ein normales Menschenleben erreicht hätte.",
        "Diese Kräfte, die auf diese Weise gleichsam dem Menschen als Restkräfte verbleiben, die er noch hätte verbrauchen können, wenn er nicht früher zugrunde gegangen wäre, die bleiben.",
        "Und es zeigt sich für die Geistesforschung, wenn man das Leben nach dem Tode untersucht, daß diese Kräfte zu den Willens- und Gefühiskräften des Menschen hinzugeschlagen werden, daß sie diese verstärken, erkraften.",
        "So daß ein solcher Mensch in der Lage ist, das, was ihm durch diese Kräfte vor der Mitternachtsstunde"
      ],
      [
        "des Daseins zugeführt wird, nach der Mitternachtsstunde des Daseins so zu benutzen, daß er ins Erdenieben als ein stärkerer, in seinem Willen charaktervollerer und kraftvollerer Mensch eintritt, als er ein­getreten wäre, wenn er nicht einen so frühen Tod gefunden hätte.",
        "Daß das aber gerade so sein muß, hängt mit früherern Karma zu­sammen, und es wäre natürlich die größte Torheit, wenn jemand glauben wollte, daß er durch künstliches Herbeiführen eines frühen Todes das erreichen würde, was geschildert worden ist; dann würde er das nicht erreichen.",
        "Was durch dieses künstliche Herbeiführen eines frühen Todes erreicht wird, das finden Sie in meiner «Theosophie» beschrieben, soweit es notwendig ist, Aufschluß darüber zu erhalten.",
        "Auch habe ich auf den Fall hingedeutet, wo der Mensch einen frühen Tod durch einen Unglücksfall findet.",
        "Wenn er durch einen Unglücks­fall herausgerissen wird aus dem Erleben des physischen Planes, für den seine Kräfte noch zugereicht hätten, um ein höheres Alter zu erreichen, so bleibt ihm wiederum ein solcher Rest von Kräften, der ihm jetzt so zugesetzt wird, daß er, wenn die Mitternachtsstunde des Daseins verflossen ist, das, was ihm da zufließt, zu seinen intellektuellen Kräften, zu seinen Erkenntniskräften verwenden kann.",
        "Man findet durch die Geistesforschung, daß große Erfinder oftmals gerade solche Menschen sind, die in früheren Inkarnationen durch einen Unglücks­fall zugrunde gegangen sind."
      ],
      [
        "Wir sehen an solchen Fällen, daß, wenn wir diese Dinge wirklich verständnisvoll überblicken wollen, wir uns schon damit bekannt machen müssen, daß eben der Gesichtspunkt in der geistigen Welt wirklich ein anderer wird, als er es in der physischen Welt sein kann.",
        "Es wird Ihnen immer mehr und mehr begreiflich werden, daß man, um die geistige Welt zu verstehen, neue Vorstellungen und Begriffe herantragen muß, weil die geistigen Welten eben etwas ganz anderes sind als die physische Welt.",
        "Daher darf sich niemand wundern, wenn zunächst etwas, was von den geistigen Welten geschildert wird, so erscheint, daß, wenn man die Begriffe der physischen Welt auf das Geschilderte anwendet, man die Sache als unbefriedigend empfindet.",
        "Zum Beispiel ist es eine Tatsache, die die Geistesforschung in vielen Fällen bekräftigt, daß jemand, der mit materialistischer Gesinnung"
      ],
      [
        "stirbt und Hinterbliebene zurückläßt, die auch materialistisch gesinnt sind, zunächst in der geistigen Welt eine gewisse Entbehrung erleidet.",
        "Wenn er durch die Pforte des Todes gegangen ist ohne spirituelle Gesinnung und zurückblicken will auf seine Lieben auf der Erde, so kann er, wenn in deren Seelen gar kein spiritueller Gedanke ist, nicht unmittelbar auf sie hinsehen; er weiß von ihnen nur bis zu dem Zeitpunkte, wo er durch den Tod gegangen ist.",
        "Was sie jetzt erleben unten auf der Erde, das kann sein geistiges Auge nicht sehen, weil in ihren Seelen nicht spirituelles Leben ist, denn nur spirituelles Leben wirft Licht hinauf in die geistigen Welten.",
        "Solch ein Mensch muß dann warten, bis ihm selber die Kräfte in der geistigen Welt erwachsen sind, um die Sache ganz klar zu sehen.",
        "Um nämlich zu sehen: diese Seelen, die er da unten zurückgelassen hat, die sind materialistisch gesinnt, weil sie von Ahriman befallen sind.",
        "Würde man das unmittelbar nach dem Tode gleich erleben, so würde man es nicht ertragen können.",
        "Man muß erst hineinwachsen in dieses von Ahriman Besessensein materialistisch gesinnter Seelen, dann kann ein Schauen dieser Seelen beginnen, bis auch sie durch die Pforte des Todes gegangen sind und sich dann selber frei machen in der geistigen Welt von ihrer materiali­stischen Gesinnung.",
        "Dann erlebt man erst später den Zusammenhang mit ihnen."
      ],
      [
        "Es könnte jemand sagen: Ja, aber das sind doch gar keine tröstlichen Verhältnisse, die du da schilderst als nach dem Tode verlaufend.",
        "Ja, meine lieben Freunde, das ist eben eine Vorstellung, die auf dem physischen Plan gewonnen ist, wenn wir so sprechen.",
        "Das ist keine Vorstellung, die schon von dem Verständnis der spitituelien Welten durchdrungen ist.",
        "Der Tote kommt zwischen dem Tod und einer neuen Geburt zu einem Zeitpunkt, wo er sich sagt: Oh, wie trostlos müßte es sein, gleich nach dem Tode diese Seelen zu sehen, wenn man materialistisch gesinnt ist!",
        "Wie ist es für all diese Seelen doch am besten, daß sie diese Prüfungszeit erst durchmachen!",
        "Sie würden sich selber verlieren, sie würden das nicht erreichen können, was erreicht werden soll, wenn es nicht so wäre.",
        "Der Gesichtspunkt wird eben ein ganz anderer, wenn man die Dinge der Welt von der geistigen Seite her betrachtet, und eine Zeit wird kommen, wo die Menschen notwendig"
      ],
      [
        "haben werden, schon auf dem physischen Plan wirklich Ver­ständnis zu gewinnen für die Wahrheiten der Geisteswissenschaft."
      ],
      [
        "Darum tritt diese Geisteswissenschaft jetzt in der Welt auf, weil die Menschheitsentwicklung es notwendig macht, daß diese Durch­dringung der geistigen Welten und ihrer Daseinsbedingungen in den Seelen immer mehr und mehr, zuerst instinktiv und dann bewußt leben wird.",
        "Ich will Ihnen eine reine Äußerlichkeit mitteilen, damit Sie sehen, wie man immer mehr dazu kommen wird, auch das Leben auf dem physischen Plan nur dadurch in seinem wahren Gehalt beurteilen zu können, daß man die Gesetze des geistigen Daseins begreift, eine reine Äußerlichkeit, die aber ungeheuer wichtig ist."
      ],
      [
        "Wenn wir auf die Natur hinblicken, so sehen wir das merkwürdige Schauspiel, daß über­all nur eine geringe Anzahl von Keimen verwendet wird, um das gleichartige Leben fortzupflanzen, daß aber eine ungeheuer große Anzahl von Keimen zugrunde geht.",
        "Wir blicken hin auf das Heer der ungeheuer vielen Fischkeime, die im Meere vorhanden sind."
      ],
      [
        "Nur we­nige von ihnen werden Fische, die anderen gehen zugrunde.",
        "Wir sehen hinaus auf das Feld und sehen die ungeheuer vielen Kornkeime.",
        "Nur wenige werden wieder zu Kornpflanzen, die anderen gehen als Ge­treidekörner zugrunde, indem sie zu menschlicher Nahrung und ande­rem verwendet werden."
      ],
      [
        "Ungeheuer viel mehr muß in der Natur erzeugt werden als was sozusagen im gleichmäßig fortfließenden Strom des Daseins wirklich Frucht wird und wieder keimt.",
        "So ist es gut in der Natur, denn da draußen in der Natur herrscht die Ordnung und Not­wendigkeit, daß das, was so abfließt von seinem zu ihm gehörigen, in sich selbst begründeten Strom des Daseins und Fruchtens, ver­wendet wird, so verwendet wird, daß es dem anderen fortlaufenden Strom des Daseins dient."
      ],
      [
        "Die Wesen würden nicht leben können, wenn alle Keime wirklich fruchteten und zu der in ihnen liegenden Entwicklung kämen.",
        "Es müssen Keime da sein, welche dazu verwen­det werden, daß sozusagen Boden gegründet wird, aus dem die Wesen herauswachsen können."
      ],
      [
        "Nur scheinbar, der Maja nach, geht etwas verloren, in Wirklichkeit geht innerhalb des Naturschaffens doch nichts verloren.",
        "In dieser Natur waltet der Geist, und daß so scheinbar etwas vom fortlaufenden Strom der Entwicklung verlorengeht, das"
      ],
      [
        "ist in der Weisheit des Geistes begründet, das ist geistiges Gesetz, und wir mussen diese Sache vom Standpunkt des Geistes ansehen.",
        "Dann kommen wir schon darauf, inwiefern auch das seine gute Daseins­berechtigung hat, was scheinbar vom fortlaufenden Strom des Welt­geschehens hinweggeführt wird.",
        "Geistgegründet ist dieses; daher kann es auch, insoferne wir geistiges Leben führen, auf dem physischen Plane Geltung haben."
      ],
      [
        "Meine lieben Freunde, nehmen Sie den uns ganz naheliegenden konkreten Fall: Es müssen öffentliche Vorträge gehalten werden über unsere Geisteswissenschaft.",
        "Die werden vor einem Publikum gehalten, das eben einfach durch die Veröffentlichungen zusammengetragen wird.",
        "Da geht etwas Ähnliches vor wie mit den Getreidekörnern, die nur zum Teil im fortlaufenden Strom des Daseins verwendet werden.",
        "Man darf nicht zurückschrecken davor, daß man unter Umständen vor viele, viele Menschen scheinbar ohne Wahl die Ströme des spiri­tuellen Lebens bringen muß, und daß sich dann nur wenige heraus-sondern und wirklich eintreten in dieses spirituelle Leben, Anthro­posophen werden und im fortlaufenden Strome mitgehen.",
        "Auf diesem Gebiete ist es noch so, daß diese verstreuten Keime an viele heran-dringen, welche zum Beispiel nach einem öffentlichen Vortrage weg­gehen und sagen: Was hat der Kerl da für tollen Unsinn geschwatzt!",
        "Unmittelbar angeschaut in bezug auf das äußere Leben, ist das so wie, sagen wir, die Keime, die im Meer als Fischkeime verlorengehen; aber vom Standpunkt einer tieferen Forschung ist es nicht so.",
        "Die Seelen, die da gekommen sind durch ihr Karma, die dann fortgehen und sagen:"
      ],
      [
        "Was hat der Kerl da für tollen Unsinn geschwatzt! - die sind noch nicht reif, die Wahrheit des Geistes zu empfangen, aber notwendig haben es ihre Seelen in der jetzigen Inkarnation, heranschwingen zu fühlen das, was als Kraft in dieser Geisteswissenschaft liegt.",
        "Und das bleibt doch in ihren Seelen, sie mögen noch so schimpfen, es bleibt als Kraft in ihren Seelen für ihre nächste Inkarnation, und dann sind die Keime nicht verloren, sie finden Wege.",
        "Es unterliegt das Dasein in bezug auf das Geistige den gleichen Gesetzen, ob wir dieses Geistige in der Naturordnung verfolgen oder in dem Fall, den wir als unseren eigenen Fall anführen konnten."
      ],
      [
        "Aber nehmen wir jetzt an, wir wollten die Sache auch auf das äußere materielle Leben übertragen und man wollte sagen: Nun, man macht es im äußeren Leben ebenso.",
        "Ja, meine lieben Freunde, das ist es gerade, daß man es macht, was ich jetzt schildern werde, daß wir einer Zukunft entgegenleben, wo sich das immer mehr herausbildet!",
        "Man produziert immer mehr und mehr darauf los, man gründet Fabriken, man fragt nicht: Wieviel wird gebraucht? - wie es einmal der Fall war, als es Schneider im Dorf gab, die nur dann einen Anzug machten, wenn er bestellt wurde.",
        "Da war es der Konsument, der angab, wieviel erzeugt werden soll, jetzt wird für den Markt produziert, die Waren werden zusammengestapelt, soviel als nur möglich.",
        "Die Produktion arbeitet ganz nach dem Prinzip, nach dem die Natur schafft.",
        "Die Natur wird in die soziale Ordnung hinein fortgesetzt.",
        "Das wird zunächst immer mehr überhandnehmen.",
        "Aber hier betreten wir das Feld des Materiel­len.",
        "Im äußeren Leben hat das geistige Gesetz, weil es eben für die geistige Welt gilt, keine Anwendung, und es entsteht etwas sehr Merk­würdiges.",
        "Da wir unter uns sind, können wir ja solche Dinge sagen.",
        "Die Welt freilich wird uns heute darin kein Verständnis entgegen­bringen."
      ],
      [
        "Es wird also heute für den Markt ohne Rücksicht auf den Konsum produziert, nicht im Sinne dessen, was in meinem Aufsatz «Geistes­wissenschaft und soziale Frage» ausgeführt worden ist, sondern man stapelt in den Lagerhäusern und durch die Geldmärkte alles zusammen, was produziert wird, und dann wartet man, wieviel gekauft wird.",
        "Diese Tendenz wird immer größer werden, bis sie sich - wenn ich jetzt das Folgende sagen werde, werden Sie finden, warum - in sich selber vernichten wird.",
        "Es entsteht dadurch, daß diese Art von Pro­duktion im sozialen Leben eintritt, im sozialen Zusammenhang der Menschen auf der Erde genau dasselbe, was im Organismus entsteht, wenn so ein Karzinom entsteht.",
        "Ganz genau dasselbe, eine Krebsbil­dung, eine Karzinombildung, Kulturkrebs, Kulturkarzinom!",
        "So eine Krebsbildung schaut derjenige, der das soziale Leben geistig durchblickt, wie überall furchtbare Anlagen zu sozialen Geschwürbildungen aufsprossen.",
        "Das ist die große Kultursorge, die auftritt für den, der das Dasein durchschaut.",
        "Das ist das Furchtbare, was so bedrückend"
      ],
      [
        "wirkt, und was selbst dann, wenn man sonst allen Enthusiasmus für Geisteswissenschaft unterdrücken könnte, wenn man unterdrücken könnte das, was den Mund öffnen kann für die Geisteswissenschaft, einen dahin bringt, das Heilmittel der Welt gleichsam entgegenzu­schreien für das, was so stark schon im Anzug ist und was immer stärker und stärker werden wird.",
        "Was auf seinem Felde in dem Ver­breiten geistiger Wahrheiten in einer Sphäre sein muß, die wie die Natur schafft, das wird zur Krebsbildung, wenn es in der geschilderten Weise in die Kultur eintritt."
      ],
      [
        "Das zu durchschauen und dann Abhilfe zu schaffen wird erst mög­lich sein, wenn Geisteswissenschaft die Herzen ergreift, die Seelen durchdringt.",
        "Und man möchte, wenn man diese Dinge durchschaut, das allerintensivste Feuer haben, um es in seine Worte zu legen, um unsere Zeitgenossen, so viele es verstehen können, aufmerksam zu machen, welcher Zeit wir entgegengehen!",
        "Einsehen kann man diese Dinge nur, wenn man sich bekannt macht mit den verschiedenen Gesichtspunkten, welche existieren, einmal für das eine Feld des Da­seins, das andere Mal für das andere.",
        "Demjenigen, der in dem Erleben zwischen der Mitternachtsstunde und einer neuen Geburt steht, dem treten diese anderen Gesichtspunkte entgegen, denn aus diesen ande­ren Gesichtspunkten heraus muß er selber schaffend werden."
      ],
      [
        "Wenn der Mensch die Tendenzen gebildet hat zum Vollzuge des Karmas in bezug auf die ihm nächststehenden Erlebnisse, dann treten die weiteren Erlebnisse, die mehr ferne stehen, vor der Seele auf.",
        "Religionsgemeinschaft, andere Gemeinschaften, denen man angehört hat, die erlebt man dann so, daß sie zeigen: Du mußt nun, damit du nicht einseitig wirst, das oder jenes in der folgenden Inkarnation tun.",
        "Kurz, dieses Leben verfließt dann so, daß es zwar auch noch ab-wechselt zwischen geistiger Geselligkeit und geistiger Einsamkeit, daß es aber wesentlich dahin geht, daß man sich das Urbild für ein neues Erdenleben, rein geistig zunächst, aufbaut."
      ],
      [
        "Lange bevor man zu diesem Erdenleben heruntersteigt, hat man aus der geistigen Welt heraus, ein geistig-ätherisches Urbild auferbaut, das die Kräfte in sich trägt, die man geistig-magnetische Kräfte nennen könnte, die einen hinunterziehen zu einem Elternpaar, von"
      ],
      [
        "dem man fühlt: Es gibt uns die Vererbungsmerkraale, damit wir in einem neuen Erdenleben auftreten können.",
        "Ich habe schon angedeutet, daß der normale Zeitpunkt der ist, in dem wir das Gefühl haben:"
      ],
      [
        "Wir vereinigen uns mit dem, was sich gefernt hat als unsere Lebens-frucht des letzten Erdenlebens.",
        "Aber der Mensch kommt nicht immer bis zu diesem.",
        "Unser Leben verfließt dann so, daß wir vollständig den Zusammenhang fühlen würden zwischen dem Leiblichen und Geisti­gen, wenn wir bis zu diesem Zeitpunkt gelangten, aber der Mensch tritt meistens früher ins Dasein.",
        "Die meisten Menschen sind geistige Frühgeburten, und es gleicht sich erst später dadurch aus, daß wir solche Erlebnisse haben, in denen wir vollständig harmonisch wieder zusammenfließen mit den Früchten unserer früheren Erdenleben."
      ],
      [
        "Eines aber ist von ganz besonderer Wichtigkeit.",
        "Ich habe es gestern dargestellt: Da, wo unsere Sehnsucht am größten sein muß nach Außenwelt, weil wir am meisten in die Einsamkeit eingetreten sind in der Mitternachtsstunde des geistigen Daseins, da ist es dasjenige, was eigentlich nur in den geistigen Welten wallt und wogt und lebt, da ist es der Geist, der an uns herantritt und unsere Sehnsucht in eine Art von Seelenlicht verwandelt."
      ],
      [
        "Bis zu diesem Zeitpunkt müssen wir den Zusammenhang mit unserem Ich bewahren.",
        "Wir müssen gleich­sam die eine Erinnerung bewahren: Du warst auf Erden dieses Ich.",
        "Dieses Ich muß einem als Erinnerung bleiben."
      ],
      [
        "Daß man das kann in unserem Zeitenzyklus, hängt davon ab, daß der Christus die Kraft in die Erdenaura hineingebracht hat, welche sonst nicht aus dem irdi­schen Leben mitgebracht würde, die Kraft, die uns befähigt, die Er­innerung bis zur Mitternachtsstunde zu bewahren.",
        "Es würde zer­reißend, sozusagen eine Kluft sein, die unser Dasein zu einem un­harmonischen in der Mitte zwischen dem Tod und einer neuen Geburt machen würde, wenn der Christusimpuls nicht durch die Erdenwelt flösse."
      ],
      [
        "Lange bevor die Mitternachtsstunde eintritt, würden wir ver­gessen, daß wir ein Ich gewesen sind im letzten Leben.",
        "Wir würden den Zusammenhang mit der geistigen Welt fühlen, würden aber uns vergessen.",
        "Und das ist dadurch bewirkt, daß wir auf Erden eben wirklich unser Ich so stark entwickeln."
      ],
      [
        "Daß wir immer mehr und mehr zu diesem Ichbewußtsein kommen, das ist notwendig geworden"
      ],
      [
        "seit dem Mysterium von Golgatha.",
        "Aber indem wir auf Erden immer mehr und mehr zu unserem Ichbewußtsein kommen, verbrauchen wir die Kräfte, die wir nötig haben nach dem Tode, damit wir wirklich bis zur Mitternachtsstunde des Daseins uns nicht vergessen.",
        "Daß wir diese Erinnerung bewahren können, dazu müssen wir in den Christus hinein sterben.",
        "So mußte der Christusimpuls da sein: er erhält uns bis zur Mitternachtsstunde des Daseins die Möglichkeit, unser Ich nicht zu vergessen."
      ],
      [
        "Dann kommt in der Mitternachtsstunde des Daseins der Geist an uns heran.",
        "Nun haben wir die Erinnerung an unser Ich bewahrt.",
        "Wenn wir sie hineintragen bis zur Mitternachtsstunde des Daseins, bis dahin, wo der Heilige Geist an uns herankommt und uns den Rückblick und den Zusammenhang mit unserer eigenen inneren Welt wie mit einer äußeren Welt gibt, wenn wir diesen Zusammenhang bewahrt haben, dann kann uns der Geist nunmehr bis zu unserer Wiederverkörperung leiten, die wir dadurch herbeiführen, daß wir unser Urbild in der geistigen Welt bilden."
      ],
      [
        "Aber nun geschehen ja die Dinge in der Wirklichkeit nicht so, daß man gewissermaßen nur das Allernotwendigste tut.",
        "Denn, wie der Pendel nicht ruhig ist, sondern ausschlägt, um wiederum nach der anderen Seite auszuschlagen, und wie es richtig ist, daß es so geschieht, so ist es auch mit dem Geistes­leben."
      ],
      [
        "Der Christusimpuls stattet uns nicht bloß mit solcher Kraft aus, daß wir gerade knapp den Anschluß finden, sondern er gibt uns unter Umständen so viel, daß, wenn der Geist nicht an uns heran-treten würde, der Christusimpuls uns hinüberschnellen könnte.",
        "Mit der Erinnerung allerdings würden wir den Anschluß nicht finden können, aber hinüberschnellen würde uns der Christusimpuls."
      ],
      [
        "Das hat seine große Bedeutung, und daß wir einen solchen, das notwen­digste Maß überschreitenden Impuls von dem Christus her aufnehmen, das wird dem Menschen immer mehr und mehr nötig sein, indem er sich in die Zukunft hinein entwickelt.",
        "Jetzt schon ist es notwendig, daß der Mensch gewissermaßen während seines Erdenlebens nicht nur das Allernotwendigste über den Christus erfährt, sondern daß der Christusimpuls als mächtiger Impuls in seine Seele sich setzt, so daß er ihn noch hinüberschnellt über die Mitternachtsstunde des Daseins."
      ],
      [
        "Denn dadurch verstärkt sich der Impuls des Geistes durch den Impuls des Christus, und wir tragen den Impuls des Geistes stärker durch die zweite Hälfte des Lebens zwischen dem Tod und einer neuen Geburt hindurch, als wir ihn sonst hindurchtragen würden, wenn der Chri­stusimpuls nicht wäre."
      ],
      [
        "Was uns übrig bleibt von dem Impuls des Christus, das verstärkt den Impuls des Geistes.",
        "Der Geist wäre Sonst nur für den Geist und er würde aufhören zu wirken, indem wir geboren würden.",
        "Indem wir uns mit dem Christusimpuls durchdringen, verstärkt der Christus-impuls den Impuls des Heiligen Geistes."
      ],
      [
        "Und dadurch kann auch in unsere Seele ein solcher Impuls des Geistes hereingebracht werden, der dann, wenn wir in die irdische Inkarnation eintreten, eine Kraft ist, die wir nicht verbrauchen wie sonst die Kräfte, die wir mitbringen durch die Geburt, in der irdischen Inkarnation.",
        "Das habe ich ja be­tont, daß wir die Kräfte, die wir aus der geistigen Welt heraus bringen, umwandeln zu unserer inneren Organisation."
      ],
      [
        "Aber das, was wir auf diese Weise als ein Plus bekommen, als ein Mehr, indem der Christus-impuls den Geistesimpuls verstärkt, das tragen wir herein ins Dasein, das braucht nun nicht umgewandelt zu werden während des irdischen Erlebens.",
        "Immer mehr und mehr Menschen werden für die Erden-entwicklung notwendig sein, je mehr wir der Zukunft entgegengehen, die so etwas von der Durchdringung des Christus-Impulses und des geistigen Impulses hereintragen in das irdische Leben durch ihre Ge­burt bei einer neuen Inkarnation."
      ],
      [
        "Der Geist, er muß stärker wirken, damit er nicht nur wirkt bis zu der Geburt hin und alles aus dem geistigen Leben heraus umgesetzt wird in innere organisierende Kräfte, so daß uns nur das bißchen Bewußtsein bleibt, das uns Er­kenntnis lehrt über unsere physische Umgebung und über das, was der Verstand ergreifen kann, der an das Gehirn gebunden ist.",
        "Würden wir als Menschen, indem wir uns der Zukunft entgegen entwickeln, nicht nach und nach einen Überschuß an Geist, der auf die geschilderte Weise entsteht, mitbringen, dann würde die Menschheit auf der Erde immer mehr dazu kommen, während des irdischen Lebens nichts mehr davon zu ahnen, daß es einen Geist gibt."
      ],
      [
        "Dann würde während des irdischen Lebens nur der ungeistige Geist, Ahriman, herrschen und"
      ],
      [
        "die Menschen würden nur wissen können von der sinnlich-physischen Welt, die man mit den Sinnen wahrnimmt, und von dem, was man mit dem Verstande begreifen kann, der an das Gehirn gebunden ist.",
        "Alle solche Dinge erleben in einer gewissen Weise doch in der Fort­entwicklung der Menschen eine Ausbildung gerade jetzt, wo die Menschheit vor der Gefahr steht, den Heiligen Geist zu verlieren."
      ],
      [
        "Aber sie wird ihn nicht verlieren.",
        "Wächter dafür will die Geistes­wissenschaft sein, daß die Menschheit diesen Geist nicht verliert, die­sen Geist, der in der Mitternachtsstunde des Daseins an die Seele herantritt, um in ihr die Sehnsucht zu beleben, daß sie sich selbst in ihrer Vergangenheit in ihrem ganzen Wert erblicke."
      ],
      [
        "Nein, Geistes­wissenschaft wird von dem Christus-Impuls immer mehr, immer ein­dringlicher reden müssen, so daß immer mehr und mehr Geist in immer mehr und mehr Menschen durch die Geburt auch ins physische Dasein hereinkommt, und daß in diesem physischen Dasein immer mehr Menschen erstehen, die fühlen: Ich habe allerdings in mir die Kräfte, die umgewandelt werden müssen in organisierende Kräfte, aber da leuchtet etwas auf in meiner Seele, das nicht umgewandelt zu werden braucht.",
        "Der Geist, der nur für die geistigen Welten ist, ich habe etwas von ihm mitgenommen in diese physische Welt, trotzdem ich in meinem Leibe lebe."
      ],
      [
        "Der Geist wird es sein, der die Menschen dazu bringt, zu schauen, was in meinem Mysteriendrama «Die Pforte der Einweihung» von der Theodora gesagt wird: Daß Menschen die Äthergestalt des Christus schauen werden.",
        "Die Kraft des Geistes, die so in die Leiber hereinkommt, die wird das geistige Auge abgeben, um die geistigen Welten zu sehen und zu verstehen."
      ],
      [
        "Zuerst wird man sie verstehen müssen, dann wird man beginnen, sie mit Verständnis zu schauen.",
        "Denn das Schauen wird herankommen, weil der Geist die Seelen so ergreift, daß sie diesen Geist hereinbringen werden in die Leiber, und auch in ihren irdischen Inkarnationen wird der Geist aufleuchten: erst bei wenigen, dann bei mehreren wird der Geist auf­leuchten."
      ],
      [
        "Und können wir auf der einen Seite sagen: Durch den Geist, durch den Heiligen Geist werden wir erweckt in der großen Mitter­nachtsstunde des Daseins, so müssen wir auf der andern Seite sagen, hinblickend auf das, was der Geist in der Erdenentwicklung für die"
      ],
      [
        "Zukunft leistet: Auch im physischen Leib wird das Beste der Seele, das, was den Ausblick gibt in die geistigen Welten, durch den Heiligen Geist immer mehr und mehr auferweckt werden.",
        "Auferweckt durch den Heiligen Geist in der Mitternachtsstunde des Daseins, wird der Mensch auch auferweckt werden, wenn er in seinem physischen Leibe lebt, wenn er sich hereiniebt in das physische Dasein.",
        "Er wird innerlich erwachen, indem ihn der Geist auferweckt aus dem Schlafe, in dem er sonst befangen wäre mit dem bloßen Anschauen der Sinneswelt und mit dem Verstande, der an das Gehirn gebunden ist.",
        "Schlafen würden die Menschen immer durch die bloße Sinnesanschauung und durch den an das Gehirn gebundenen Verstand.",
        "Aber hineinleuchten in diesen Menschenschlaf, der sonst die Menschheit gegen die Zukunft hin immer mehr umdüsternd überkommen würde, hineinleuchten in diesen Schlaf wird der Geist im Menschen auch während des physi­schen Daseins.",
        "Mitten in dem absterbenden geistigen Leben, mitten in dem durch die bloße Sinnesanschauung, durch die Verstandeswelt absterbenden Geistesleben auf dem physischen Plan werden die Menschenseelen auferweckt werden auch im physischen Dasein durch den Heiligen Geist."
      ],
      [
        "Per spiritum sanctum reviviscimus."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "ÜBER DEN JOHANNESBAU IN DORNACH Ansprache in Wien vor dem Vortrag am 14. April 1914",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Bevor ich heute zu dem Vortrag selbst komme, möchte ich ein paar Worte an Sie richten, die nur besagen wollen, daß wir in diesem Jahre leider nicht, so wie in den verflossenen Jahren, in der Mitte des Sommers die Veranstaltungen haben werden, die sonst in München stattgefunden haben, da die nächste derartige Veranstaltung eben schon im Johannesbau stattfinden soll, und dieser Bau sich etwas länger hinauszieht, als ursprünglich hat gedacht werden können. Es steht zu hoffen, daß wir in den letzten zwei Monaten dieses Jahres so weit sein werden, daß dann eine feierliche, festliche Eröffnung des Johannesbaues stattfinden kann.",
      "Dieser Bau macht uns ja mehr Arbeit, als man sich gewöhnlich vorstellt, und Sie werden es daher begreiflich finden, daß jetzt schon einmal eine gewisse Zeit hindurch die persönlichen Besprechungen ausfallen mußten.",
      "Für unsere lieben österreichischen Freunde ist es ganz gewiß in vieler Beziehung nicht leicht gewesen, sich mit dem Gedanken ver­traut zu machen, daß der Johannesbau in so großer Ferne liegt. Allein, trotzdem ich jetzt nicht in der Lage bin das des weiteren aus­einanderzusetzen, denn dazu mangelt die Zeit, so war es eben schon einmal so, daß uns das Karma dazu geführt hat, den Johannesbau dort zu errichten, wo er errichtet wird; und das wird gut sein.",
      "Es wird uns ja schon vor Augen stehen müssen, daß wir in diesem Bau eine Art Zentralstätte und Wahrzeichen unserer spirituellen Be­wegung sehen. Was für den einen weit ist, ist für den andern nahe; das ließ sich von vornherein nicht anders machen. Es steht aber doch wohl zu hoffen, daß auch unsere österreichischen Freunde Mittel und Wege finden, durch persönliche Anwesenheit bei der entsprechenden Veranstaltung des Johannesbaues dieses Wahrzeichen unserer anthroposophischen",
      "Bewegung als das ihrige, ic'l möchte ausdrücklich sagen, zu erleben. Es ist in Wirklichkeit nicht nur ein Wahrzeichen durch das, was es sein wird als Monumentalbau, sondern es ist gewissermaßen ein Wahrzeichen dadurch, daß es, wenn es wirklich zustande kommt, nur zustande kommen kann und konnte durch das, was als große Opferwilligkeit einiger unserer Freunde geleistet wurde, die wirklich das Äußerste an Opferwilligkeit geleistet haben, um den schwierigen und vor allen Dingen kostspieligen Bau, so wie er nun einmal sein soll, zu Ende zu bringen.",
      "Was entstehen soll, das soll in jeder Beziehung eigentlich zum Aus­druck bringen, was unsere spirituelle Bewegung sein wird. Und dem muß der ganze Baustil auch entsprechen. Alles, was in den Bau hinein-fließt, muß so sein, daß es nicht in symbolischer oder allegorischer Art und Weise hineinkommt, sondern es muß in wirklich künstleri­scher Weise in diesen Bau hineinfließen. Vor allen Dingen war dieses notwendig: einmal einen solchen Bau aufzuführen, der in allen seinen Formen eine Verkörperung des spirituellen Wesens ist, dem wir zu-getan sind. Die verschiedenen Zeiten, die verschiedenen Kulturen der Menschheitsentwicklung hatten auch die ihnen entsprechenden eige­nen Bauten. Der Bau, der in Dornach aufgerichtet werden soll, der soll in allen seinen Formen, aus denen er zusammengesetzt ist, und mit denen er gleichsam eine Hülle unserer spirutellen Arbeit bilden soll, durch die Art, wie diese Hülle sich nach außen und nach innen ein- und abschließt und zusammenschließt, zeigen, daß in ihren Formen sich etwas ausdrückt, das etwas ist, wie es für einen solchen Bau im Grunde in der Architektur noch nie gedacht war.",
      "Wie der griechische Tempel dasteht, um eine Wohnung des Gottes zu sein, der darinnen ist, wie der gotische Dom dasteht, um zusammen mit der Gemeinde, die darin versammelt ist, ein Ganzes zu bilden, so soll unser Bau sich so darstellen, daß die Formen unmittelbar, ich möchte sagen, in spiritueller geisteswissenschaftlicher Beziehung den Bau so gestalten, daß er spirituell durchsichtig ist. Das heißt: wenn man in dem Bau drinnen sein wird, so wird man durch die Architektur und durch dasjenige, was von der Architektur in die Plastik übergeht, das Gefühl haben: diese Wände sind nicht so, wie andere architektonische",
      "Wände bisher waren, abschließend, bloß einschließend, sondern sie sind zugleich die Kommunil::atoren, welche das geistige Leben eröffnen in unendliche spirituelle Weiten. Es sind Wände, die sich zu gleicher Zeit durch ihre Formen selbst aufheben, die zu gleicher Zeit eben nicht da sind in dem, was sie physisch sind. Das soll erreicht werden, daß jeder, der drinnen ist und nach und nach sich gewöhnen wird, diese Formen, aber nicht allegorisch und symbolisch, sondern in lebendiger Empfindung zu verstehen, etwas hat wie einen Ausblick in die Welt von der wir sprechen, einfach durch das Erleben der Form.",
      "Das ist ja natürlich etwas ganz Neues in der Architektur, das ist etwas Ungewöhnliches; und das braucht Zeit und Arbeit, und wie es schon einmal in unserer Zeit ist, - verzeihen Sie den harten Aus­druck - das braucht auch und hat gebraucht: Geld! Und dazu war die Opferwilligkeit einzelner unserer Freunde uns wirklich so ent­gegengekommen, daß wir sagen können: auch diese Opferwilligkeit ist in gewisser Beziehung ein Wahrzeichen für die Art, wie unsere spirituelle Bewegung in das Verständnis der Seelen eingedrungen ist.",
      "Nur das wollte ich mit diesen Worten erwähnen, daß Sie diesen Bau in Ihr Herz aufnehmen, daß Sie ihn wie einen Mittelpunkt unserer Bewegung erfühlen, sodaß Sie sich mit ihm vereint denken können, und daß Sie Ihre persönliche Anwesenheit ihm gönnen, so viel das von der Eröffnung ab in der Zukunft einmal wird der Fall sein können."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Bevor ich heute zu dem Vortrag selbst komme, möchte ich ein paar Worte an Sie richten, die nur besagen wollen, daß wir in diesem Jahre leider nicht, so wie in den verflossenen Jahren, in der Mitte des Sommers die Veranstaltungen haben werden, die sonst in München stattgefunden haben, da die nächste derartige Veranstaltung eben schon im Johannesbau stattfinden soll, und dieser Bau sich etwas länger hinauszieht, als ursprünglich hat gedacht werden können.",
        "Es steht zu hoffen, daß wir in den letzten zwei Monaten dieses Jahres so weit sein werden, daß dann eine feierliche, festliche Eröffnung des Johannesbaues stattfinden kann."
      ],
      [
        "Dieser Bau macht uns ja mehr Arbeit, als man sich gewöhnlich vorstellt, und Sie werden es daher begreiflich finden, daß jetzt schon einmal eine gewisse Zeit hindurch die persönlichen Besprechungen ausfallen mußten."
      ],
      [
        "Für unsere lieben österreichischen Freunde ist es ganz gewiß in vieler Beziehung nicht leicht gewesen, sich mit dem Gedanken ver­traut zu machen, daß der Johannesbau in so großer Ferne liegt.",
        "Allein, trotzdem ich jetzt nicht in der Lage bin das des weiteren aus­einanderzusetzen, denn dazu mangelt die Zeit, so war es eben schon einmal so, daß uns das Karma dazu geführt hat, den Johannesbau dort zu errichten, wo er errichtet wird; und das wird gut sein."
      ],
      [
        "Es wird uns ja schon vor Augen stehen müssen, daß wir in diesem Bau eine Art Zentralstätte und Wahrzeichen unserer spirituellen Be­wegung sehen.",
        "Was für den einen weit ist, ist für den andern nahe; das ließ sich von vornherein nicht anders machen.",
        "Es steht aber doch wohl zu hoffen, daß auch unsere österreichischen Freunde Mittel und Wege finden, durch persönliche Anwesenheit bei der entsprechenden Veranstaltung des Johannesbaues dieses Wahrzeichen unserer anthroposophischen"
      ],
      [
        "Bewegung als das ihrige, ic'l möchte ausdrücklich sagen, zu erleben.",
        "Es ist in Wirklichkeit nicht nur ein Wahrzeichen durch das, was es sein wird als Monumentalbau, sondern es ist gewissermaßen ein Wahrzeichen dadurch, daß es, wenn es wirklich zustande kommt, nur zustande kommen kann und konnte durch das, was als große Opferwilligkeit einiger unserer Freunde geleistet wurde, die wirklich das Äußerste an Opferwilligkeit geleistet haben, um den schwierigen und vor allen Dingen kostspieligen Bau, so wie er nun einmal sein soll, zu Ende zu bringen."
      ],
      [
        "Was entstehen soll, das soll in jeder Beziehung eigentlich zum Aus­druck bringen, was unsere spirituelle Bewegung sein wird.",
        "Und dem muß der ganze Baustil auch entsprechen.",
        "Alles, was in den Bau hinein-fließt, muß so sein, daß es nicht in symbolischer oder allegorischer Art und Weise hineinkommt, sondern es muß in wirklich künstleri­scher Weise in diesen Bau hineinfließen.",
        "Vor allen Dingen war dieses notwendig: einmal einen solchen Bau aufzuführen, der in allen seinen Formen eine Verkörperung des spirituellen Wesens ist, dem wir zu-getan sind.",
        "Die verschiedenen Zeiten, die verschiedenen Kulturen der Menschheitsentwicklung hatten auch die ihnen entsprechenden eige­nen Bauten.",
        "Der Bau, der in Dornach aufgerichtet werden soll, der soll in allen seinen Formen, aus denen er zusammengesetzt ist, und mit denen er gleichsam eine Hülle unserer spirutellen Arbeit bilden soll, durch die Art, wie diese Hülle sich nach außen und nach innen ein- und abschließt und zusammenschließt, zeigen, daß in ihren Formen sich etwas ausdrückt, das etwas ist, wie es für einen solchen Bau im Grunde in der Architektur noch nie gedacht war."
      ],
      [
        "Wie der griechische Tempel dasteht, um eine Wohnung des Gottes zu sein, der darinnen ist, wie der gotische Dom dasteht, um zusammen mit der Gemeinde, die darin versammelt ist, ein Ganzes zu bilden, so soll unser Bau sich so darstellen, daß die Formen unmittelbar, ich möchte sagen, in spiritueller geisteswissenschaftlicher Beziehung den Bau so gestalten, daß er spirituell durchsichtig ist.",
        "Das heißt: wenn man in dem Bau drinnen sein wird, so wird man durch die Architektur und durch dasjenige, was von der Architektur in die Plastik übergeht, das Gefühl haben: diese Wände sind nicht so, wie andere architektonische"
      ],
      [
        "Wände bisher waren, abschließend, bloß einschließend, sondern sie sind zugleich die Kommunil::atoren, welche das geistige Leben eröffnen in unendliche spirituelle Weiten.",
        "Es sind Wände, die sich zu gleicher Zeit durch ihre Formen selbst aufheben, die zu gleicher Zeit eben nicht da sind in dem, was sie physisch sind.",
        "Das soll erreicht werden, daß jeder, der drinnen ist und nach und nach sich gewöhnen wird, diese Formen, aber nicht allegorisch und symbolisch, sondern in lebendiger Empfindung zu verstehen, etwas hat wie einen Ausblick in die Welt von der wir sprechen, einfach durch das Erleben der Form."
      ],
      [
        "Das ist ja natürlich etwas ganz Neues in der Architektur, das ist etwas Ungewöhnliches; und das braucht Zeit und Arbeit, und wie es schon einmal in unserer Zeit ist, - verzeihen Sie den harten Aus­druck - das braucht auch und hat gebraucht: Geld!",
        "Und dazu war die Opferwilligkeit einzelner unserer Freunde uns wirklich so ent­gegengekommen, daß wir sagen können: auch diese Opferwilligkeit ist in gewisser Beziehung ein Wahrzeichen für die Art, wie unsere spirituelle Bewegung in das Verständnis der Seelen eingedrungen ist."
      ],
      [
        "Nur das wollte ich mit diesen Worten erwähnen, daß Sie diesen Bau in Ihr Herz aufnehmen, daß Sie ihn wie einen Mittelpunkt unserer Bewegung erfühlen, sodaß Sie sich mit ihm vereint denken können, und daß Sie Ihre persönliche Anwesenheit ihm gönnen, so viel das von der Eröffnung ab in der Zukunft einmal wird der Fall sein können."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Das innere Wesen des Menschen",
      "Gewisse Veränderungen und Erweiterungen des Textes wurden auf Grund einer in­zwischen zum Vorschein gekommenen, etwas ausführlicheren Nachschrift vorgenommen.",
      "9    Nikolaus Kopernikus 1473",
      "29 Ihr werdet sein wie Gott... Moses 1, 3, 5.",
      "30    Goethes «Faust» I. Teil, 5. Auerbachs Keller.",
      "31    Rekttor der Universitätt Wien: Prof. Dr. Laurenz Müliner (1848-1911). Inaugurations­rede: 8. November 1894 «Die Bedeutung Galileis für die Philosophie». Siehe Rudolf",
      "Steiner «Mein Lebensgang» Kapitel VII (1925) 6. Auflage Dornach 1949",
      "Müllners Rede wurde wiedergedruckt in der Zeitschrift «Anthroposophie»",
      "Jg. 1933/34, S.29 ff.",
      "32    den Sehillerschen Worten: «Die Künstler » (Jetzt fiel der Tierheit dumpfe Schranke)",
      "33    Ernst Freiherr von Feuchtersieben 1804-1849.",
      "37    «Wie erlangt man Erkenntnisse der höheren Welten?» (1904-1905) Rudolf Steiner Gesamtausgabe",
      "«Die Geheimwissenschaft im Umriß » (1910). Rudolf Steiner Gesamtausgabe 38 Henri Bergson 1895-1941, französischer Philosoph.",
      "49    «Die Schwelle der geistigen Welt» (1913) Rudolf Steiner Gesamtausgabe «Der Seelen Erwachen» (1913) im Bande «Vier Mysteriendramen» der Rudolf Steiner Gesamtausgabe",
      "52    Gewisse niedere Tiere...: Die Nachschrift, an die sich der vorliegende Druck hält, hat hier eine Lücke, die durch den Text einer anderen Nachsehrift geschlossen wurde.",
      "57 Giord,no Bruno 1548-1600.",
      "59    Goethe-Zitat: Siehe Eckermann, Gespräche mit Goethe. 25. Februar 1824.",
      "79    was Sie in den ersten Sätzen der ,Prüfung der Seele'... geschildert finden: Rudolf Steiner «Die Prüfung der Seele» I. Bild (1911) In «Vier Mysteriendramen» s.o.",
      "82    ich habe in meinem öffentlichen Vortrage darauf hingewiesen: Erster Vortrag dieses Bandes.",
      "89    «Der Seelen Erwachen», 5. und 6. Bild s.o.",
      "114    Bei dem zweiten hier gehaltenen öffentlichen Vortrag: Zweiter Vortrag dieses Bandes.",
      "126    Ludwig Laistuer, Das Rätsel der Sphinx Siehe: Rudolf Steiner « Mein Lebensgang» Kapitel XV.",
      "Friedrich Christoph Ötinger 1702",
      "128 Hermann Latze 1817",
      "154    vorgestriger Vortrag: Vierter Vortrag dieses Zyklus, 12. Aprll 1914",
      "160    in meiner «Theosophie»: Rudolf Steiner «Theosophie' Einführung in übersinnliche Welterkenntnis und Menschenbestimmung» Kapitel: « Die Seele in der Seelenwelt nach dem Tode» (1904) Rudolf Steiner Gesamtausgabe",
      "164    «Geisteswissenschaft und soziale Frage» (1905) Dornach 1957.",
      "171    Diese Worte wurden dem Vortrag vom 14. April 1914 vorangestellt. Johannesbau: Der Bau sollte erst diesen Namen haben. Der Name « Goethcanum» wurde ihm später von Rudolf Steiner gegeben."
    ],
    "sentences": [
      [
        "Das innere Wesen des Menschen"
      ],
      [
        "Gewisse Veränderungen und Erweiterungen des Textes wurden auf Grund einer in­zwischen zum Vorschein gekommenen, etwas ausführlicheren Nachschrift vorgenommen."
      ],
      [
        "9 Nikolaus Kopernikus 1473"
      ],
      [
        "29 Ihr werdet sein wie Gott...",
        "Moses 1, 3, 5."
      ],
      [
        "30 Goethes «Faust» I.",
        "Teil, 5.",
        "Auerbachs Keller."
      ],
      [
        "31 Rekttor der Universitätt Wien: Prof.",
        "Laurenz Müliner (1848-1911).",
        "Inaugurations­rede: 8.",
        "November 1894 «Die Bedeutung Galileis für die Philosophie».",
        "Siehe Rudolf"
      ],
      [
        "Steiner «Mein Lebensgang» Kapitel VII (1925) 6.",
        "Auflage Dornach 1949"
      ],
      [
        "Müllners Rede wurde wiedergedruckt in der Zeitschrift «Anthroposophie»"
      ],
      [
        "Jg. 1933/34, S.29 ff."
      ],
      [
        "32 den Sehillerschen Worten: «Die Künstler » (Jetzt fiel der Tierheit dumpfe Schranke)"
      ],
      [
        "33 Ernst Freiherr von Feuchtersieben 1804-1849."
      ],
      [
        "37 «Wie erlangt man Erkenntnisse der höheren Welten?» (1904-1905) Rudolf Steiner Gesamtausgabe"
      ],
      [
        "«Die Geheimwissenschaft im Umriß » (1910).",
        "Rudolf Steiner Gesamtausgabe 38 Henri Bergson 1895-1941, französischer Philosoph."
      ],
      [
        "49 «Die Schwelle der geistigen Welt» (1913) Rudolf Steiner Gesamtausgabe «Der Seelen Erwachen» (1913) im Bande «Vier Mysteriendramen» der Rudolf Steiner Gesamtausgabe"
      ],
      [
        "52 Gewisse niedere Tiere...: Die Nachschrift, an die sich der vorliegende Druck hält, hat hier eine Lücke, die durch den Text einer anderen Nachsehrift geschlossen wurde."
      ],
      [
        "57 Giord,no Bruno 1548-1600."
      ],
      [
        "59 Goethe-Zitat: Siehe Eckermann, Gespräche mit Goethe. 25.",
        "Februar 1824."
      ],
      [
        "79 was Sie in den ersten Sätzen der ,Prüfung der Seele'... geschildert finden: Rudolf Steiner «Die Prüfung der Seele» I.",
        "Bild (1911) In «Vier Mysteriendramen» s.o."
      ],
      [
        "82 ich habe in meinem öffentlichen Vortrage darauf hingewiesen: Erster Vortrag dieses Bandes."
      ],
      [
        "89 «Der Seelen Erwachen», 5. und 6.",
        "Bild s.o."
      ],
      [
        "114 Bei dem zweiten hier gehaltenen öffentlichen Vortrag: Zweiter Vortrag dieses Bandes."
      ],
      [
        "126 Ludwig Laistuer, Das Rätsel der Sphinx Siehe: Rudolf Steiner « Mein Lebensgang» Kapitel XV."
      ],
      [
        "Friedrich Christoph Ötinger 1702"
      ],
      [
        "128 Hermann Latze 1817"
      ],
      [
        "154 vorgestriger Vortrag: Vierter Vortrag dieses Zyklus, 12.",
        "Aprll 1914"
      ],
      [
        "160 in meiner «Theosophie»: Rudolf Steiner «Theosophie' Einführung in übersinnliche Welterkenntnis und Menschenbestimmung» Kapitel: « Die Seele in der Seelenwelt nach dem Tode» (1904) Rudolf Steiner Gesamtausgabe"
      ],
      [
        "164 «Geisteswissenschaft und soziale Frage» (1905) Dornach 1957."
      ],
      [
        "171 Diese Worte wurden dem Vortrag vom 14.",
        "April 1914 vorangestellt.",
        "Johannesbau: Der Bau sollte erst diesen Namen haben.",
        "Der Name « Goethcanum» wurde ihm später von Rudolf Steiner gegeben."
      ]
    ]
  }
]

# === SQL GENERATION ===
def generate_sql():
    """Generate SQL using PL/pgSQL DO block."""
    sql_lines = []
    sql_lines.append("-- Auto-generated import for " + GA_NUMBER)
    sql_lines.append("BEGIN;")
    sql_lines.append("")
    sql_lines.append("DO $$")
    sql_lines.append("DECLARE")
    sql_lines.append("    v_book_id INT;")
    sql_lines.append("    v_lecture_id INT;")
    sql_lines.append("    v_para_id INT;")
    sql_lines.append("BEGIN")
    sql_lines.append("    -- Create or get book")
    te = BOOK_TITLE.replace("'", "''")
    sql_lines.append("    v_book_id := (SELECT id FROM books WHERE ga_number = '%s');" % GA_NUMBER)
    sql_lines.append("    IF v_book_id IS NULL THEN")
    sql_lines.append("        INSERT INTO books (ga_number, title_de, pdf_filename)")
    sql_lines.append("        VALUES ('%s', '%s', '%s.epub')" % (GA_NUMBER, te, GA_NUMBER))
    sql_lines.append("        RETURNING id INTO v_book_id;")
    sql_lines.append("    ELSE")
    sql_lines.append("        UPDATE books SET title_de = '%s' WHERE id = v_book_id;" % te)
    sql_lines.append("    END IF;")
    sql_lines.append("")
    sql_lines.append("    -- Delete old data (cascades to paragraphs/sentences)")
    sql_lines.append("    DELETE FROM lectures WHERE book_id = v_book_id;")
    sql_lines.append("")

    for ch in CHAPTERS:
        te = ch["title_de"].replace("'", "''")
        sql_lines.append("    -- Chapter %d: %s" % (ch["order"], te))
        sql_lines.append("    INSERT INTO lectures (book_id, title_de, order_index, level)")
        sql_lines.append("    VALUES (v_book_id, '%s', %d, 'lecture')" % (te, ch["order"]))
        sql_lines.append("    RETURNING id INTO v_lecture_id;")
        sql_lines.append("")

        for pi, para_text in enumerate(ch["paragraphs"], 1):
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else []
            if not sentences:
                continue

            sql_lines.append("    INSERT INTO paragraphs (lecture_id, order_index)")
            sql_lines.append("    VALUES (v_lecture_id, %d)" % pi)
            sql_lines.append("    RETURNING id INTO v_para_id;")
            sql_lines.append("")

            for si, sent in enumerate(sentences, 1):
                se = sent.replace("'", "''")
                sql_lines.append("    INSERT INTO sentences (paragraph_id, order_index, text_de)")
                sql_lines.append("    VALUES (v_para_id, %d, '%s');" % (si, se))
                sql_lines.append("")

    sql_lines.append("END $$;")
    sql_lines.append("COMMIT;")
    sql_lines.append("")

    return "\n".join(sql_lines)


def import_to_db():
    """Run the SQL import via docker exec psql."""
    print("Generating SQL for %s..." % GA_NUMBER)
    sql = generate_sql()
    sql_path = "/tmp/%s_import.sql" % GA_NUMBER
    Path(sql_path).write_text(sql, encoding='utf-8')
    ln = len(sql.split('\n'))
    sk = len(sql) / 1024
    print("  SQL written: %s (%d lines, %d KB)" % (sql_path, ln, sk))

    result = subprocess.run(
        ["docker", "cp", sql_path, "%s:/tmp/%s_import.sql" % (DOCKER_CONTAINER, GA_NUMBER)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("  FAILED COPY: %s" % result.stderr)
        return False

    print("  Importing into Docker PostgreSQL...")
    with open(sql_path, 'r') as f:
        proc = subprocess.Popen(
            ["docker", "exec", "-i", DOCKER_CONTAINER, "psql", "-U", DB_USER, "-d", DB_NAME],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input=sql)

    if proc.returncode != 0:
        sl = stderr.strip().split('\n')
        print("  psql error (exit=%d):" % proc.returncode)
        for line in sl[-5:]:
            print("     %s" % line)
        return False
    else:
        print("  IMPORTED %s successfully!" % GA_NUMBER)
        if stdout.strip():
            for line in stdout.strip().split('\n')[-3:]:
                print("     %s" % line)
        return True


if __name__ == "__main__":
    print()
    print("=" * 60)
    print("Importing %s: %s" % (GA_NUMBER, BOOK_TITLE))
    print("=" * 60)

    tp = sum(len(c["paragraphs"]) for c in CHAPTERS)
    ts = sum(sum(len(s) for s in c["sentences"]) for c in CHAPTERS)
    print("  %d chapters, %d paragraphs, %d sentences" % (len(CHAPTERS), tp, ts))

    success = import_to_db()
    sys.exit(0 if success else 1)

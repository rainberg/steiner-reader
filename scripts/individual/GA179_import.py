#!/usr/bin/env python3
"""Standalone import script for GA179 — GA179 - Geschichtliche Notwendigkeit und Freiheit. Schicksalseinwirkungen aus der Welt der Toten"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA179 - Geschichtliche Notwendigkeit und Freiheit. Schicksalseinwirkungen aus der Welt der Toten"""
GA_NUMBER = "GA179"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG Dornach, 2. Dezember 1917",
    "paragraphs": [
      "Wir werden heute fortfahren, einiges hinzuzutragen zu den Betrach­tungen, die wir angestellt haben. Es war mir in dieser Zeit viel darum zu tun, begreiflich zu machen, von welchen Bedingungen das mensch­liche Leben abhängt im einzelnen und in dem großen Zusammenhange. Sie haben gesehen, wie auch in den öffentlichen Vorträgen, die ich in dieser Zeit halten durfte, es mir darauf ankam, gerade jetzt auf die­jenigen Probleme der Geisteswissenschaft hinzuweisen, welche für das Begreifen der Menschheit notwendig sind, um aus gewissen Vorstel­lungskreisen herauszukommen, in die sich die Menschheit gewisser­maßen über den ganzen Erdkreis hin eingesponnen hat und die letzten Endes doch mit zu den Veranlassungen der jetzigen katastrophalen Ereignisse gehören.",
      "Vor allen Dingen wird es sich darum handeln, daß die Menschen einsehen lernen müssen, wo die Grenze zwischen der sogenannten phy­sischen und der geistigen Welt liegt. Diese Grenze liegt eigentlich mitten im Menschen drinnen. Gerade dieser Satz ist wichtig für das Verständ­nis der Welt: daß wir die Grenze zwischen der physischen und geistigen Welt in dem Menschen selber drinnen sehen. Die naturwissenschaftliche Denkungsweise, deren große Bedeutung für die Gegenwart und die Zu­kunft ich vom Gesichtspunkt der Geisteswissenschaft oftmals hervor­gehoben habe, ist aber jetzt, wo sie noch mehr oder weniger immer an ihrem Ausgangspunkte steht, eigentlich dazu geeignet, über gewisse wichtige Lebenswahrheiten, man könnte schon sagen, zunächst sogar Finsternis zu verbreiten.",
      "Machen wir uns nur klar, daß sich die Zeitentwickelung eigentlich heute erst dazu anschickt, das naturwissenschaftliche Denken allmäh­lich in die Welt- und Lebensanschauungen ganz einzuführen. Heute beschäftigen sich - in einer oftmals haarsträubend dilettantischen Weise - gewisse Monisten- oder andere Vereine damit, naturwissen­schaftliche Weltanschauung dem Allgemeinbewußtsein zuzuführen. Allein dies ist ja nur der eine Weg, durch den allmählich dieses naturwissenschaftliche",
      "Denken in die Menschenseele fließt. Der viel wirk­samere, einschneidendere Weg ist der durch die Publizistik.",
      "Nicht umsonst, sondern durchaus innerlich zusammengehörig fallen in die Menschheitsentwickelung der Einschnitt der neueren naturwis­senschaftlichen Denkungsweise und die Erfindung der Buchdrucker-kunst zusammen. Denn dasjenige, was bisher durch den Druck als Ursprüngliches in die Menschheit eingegangen ist, selbstverständlich abgesehen von dem, was man von früher schon Dagewesenem gedruckt hat, ist im wesentlichen aus naturwissenschaftlichem Bewußtsein her­vorgegangen. Ich meine, das Neue ist aus naturwissenschaftlichem Bewußtsein hervorgegangen, und vor allen Dingen die Art und Weise, in die man die Gedanken eingefangen hat, ist aus naturwissenschaft­licher Denkweise hervorgegangen.",
      "Nun werden natürlich Theologen gegenüber einem solchen Aus­spruch sagen: Ja, haben wir denn nicht auch unsere theologische Weis­heit und alle möglichen frommen Dinge in den letzten Jahren und Jahrzehnten und Jahrhunderten gedruckt? - Ja, das ist allerdings wahr, aber wozu hat es geführt? Diese Art und Weise, wie unter der Flagge des Druckes das geistige Leben sich eingelebt hat in die Seelen der Men­schen, hat dazu geführt, daß nach und nach ganz geschwunden ist auch aus dem Gebiete des religiösen Bewußtseins das spirituelle Element. Und selbst aus dem Christus Jesus, das wissen Sie ja, hat man unter dem Einfluß der naturwissenschaftlichen Denkweise den «schlichten Mann aus Nazareth» gemacht, den man zwar versucht in der ver­schiedensten Weise zu charakterisieren, der aber doch eigentlich schon dabei angelangt ist, mit den andern großen Persönlichkeiten der Welt in eine Linie gestellt zu werden, wenn auch vorläufig noch auf einem besonderen Gipfel. Das eigentlich Geistige, das mit dem Mysterium von Golgatha verknüpft ist, das ist nach und nach dahingeschwunden, wenigstens für diejenigen, die da glauben, mit der Zeitenbildung vor-wärtsgeschritten zu sein.",
      "Ich sagte, die naturwissenschaftliche Denkweise hat zunächst ge­radezu mitwirken müssen zu einer gewissen Verfinsterung, zu einer Unterstützung desjenigen, was nun seit 1879 durch die Geister der Finsternis in das menschliche Denken hineingebracht werden soll.",
      "Und auf naturwissenschaftlichem Gebiete zeigt sich die Sache in einer recht raffinierten Art, raffiniert deshalb, weil der naturwissenschaft­lich nicht nur Durchgebildete, sondern der naturwissenschaftlich fachmännisch Gebildete, wenn er heute mitarbeitet an der allgemeinen Bildung der Zeit, an der Gestaltung der Weltanschauung, gar nicht anders kann, so wie heute die Wissenschaft einmal ist - lassen Sie mich das triviale Wort anwenden -, als «aus bestem Wissen und Gewissen heraus» so zu wirken, daß durch die Popularisierung der naturwissenschaftlichen Denkweise der Mensch geradezu abgebracht wird davon, den Blick hinwerfen zu können auf die Grenze, die in ihm selber ist zwischen der physischen Welt und der geistigen Welt. Es wird eine Zukunft des Menschendenkens anbrechen, es ist fürchterlich, daß dies heute gesagt werden muß, fürchterlich für die nach einer gewissen Richtung heute Gebildeten, da werden gewisse Vorstellungen, die heute in der Wissenschaft herrschen - und die zwar nicht im populären Be­wußtsein sehr vorhanden sind, aber auf das populäre Bewußtsein da­durch wirken, daß man heute die Wissenschafter als, verzeihen Sie, Autoritäten ansieht -, gewisseVorstellungen der Gegenwart werden vor einem künftigen Zeitbewußtsein geradezu komisch anmuten müssen.",
      "Auf eine Vorstellung habe ich öfters hingewiesen, öffentlich nun auch in meinem Buch «Von Seelenrätseln»: Es ist eine gangbare natur­wissenschaftliche Vorstellung heute, daß man im Nervensystem - blei­ben wir zunächst beim Menschen, aber in ähnlicher Weise, nur in ähn­licher Weise ist das auch beim Tiere gültig -, daß man im Nervensystem unterscheidet zwischen sogenannten sensitiven Nerven, Sinnesnerven, Wahrnehmungsnerven und motorischen Nerven. Schematisch kann das nur so dargestellt werden, daß zum Beispiel irgendein Nerv, sagen wir ein Tastnerv, die Tastempfindung hineinträgt bis zum Zentralorgan, sagen wir bis zum Rückenmark (gelb), da mündet dasjenige, was da aus der Peripherie des Leibes geleitet wird, in einem Horn des Rücken­marks. Und dann geht von einem andern Horn, Vorderhorn, der so­genannte motorische Nerv aus, da wird wiederum weitergeleitet der Willensimpuls (siehe Zeichnung S. 12).",
      "Beim Gehirn ist das nur komplizierter dargestellt, so etwa, wie wenn die Nerven eine Art Telegraphendrähte wären. Der Sinneseindruck,",
      "# Bild s. 12",
      "der Hauteindruck wird bis zum Zentralorgan geleitet, dort wird ge­wissermaßen der Befehl erteilt, daß eine Bewegung ausgeführt werden soll. Eine Fliege setzt sich irgendwo auf einen Körperteil, das macht einen Eindruck, das wird geleitet bis zum Zentralorgan; dort wird der Befehl gegeben, die Hand bis zu der Stirne zu erheben und die Fliege wird weggejagt. Es ist eine, schematisch angedeutet, sehr gangbare Vorstellung. Künftigen Zeiten wird diese Vorstellung außerordentlich komisch erscheinen, denn sie ist ja nur komisch für denjenigen, der die Tatsache durchschaut. Aber es ist eine Vorstellung, von der heute ein großer Teil der fachmännischen und fachmännischesten Wissenschaft beherrscht ist. Sie können das nächstbeste Elementarbuch, das Sie über solche Dinge unterrichtet, aufschlagen, und Sie werden finden, man habe zu unterscheiden zwischen Sinneswahrnehmungsnerven und mo­torischen Nerven. Und man wird besonders das urkomische Bild von den Telegraphenleitungen - wie der Eindruck bis zum Zentralorgan geleitet und dort der Befehl gegeben wird, daß die Bewegung entstehe -gerade in populären Werken heute noch immer sehr verbreitet finden können.",
      "Die Wirklichkeit ist allerdings schwieriger zu durchschauen, als die an die primitivsten Vorstellungen erinnernden Vergleichsvorstellungen von den Telegraphendrähten. Die Wirklichkeit kann nur durchschaut werden, wenn sie eben mit Geisteswissenschaft durchschaut wird. Daß ein Willensimpuls erfolgt, hat mit einem solchen Vorgange, den man in kindischer Weise so ausdrückt, als ob da irgendwo in einem materiellen",
      "Zentralorgan ein Befehl erteilt würde, wirklich gar nichts zu tun. Die Nerven sind nur da, um einer einheitlichen Funktion zu dienen, sowohl diejenigen Nerven, die man heute sensitive Nerven nennt, wie auch diejenigen, die man motorische Nerven nennt. Und ob nun im Rücken­mark oder im Gehirn der Nervenstrang durchbrochen ist, beides weist auf dasselbe hin; im Gehirn ist er nur in komplizierterer Weise durch­brochen.",
      "Diese Durchbrechung ist nicht deshalb da, damit durch die eine Hälfte, wenn ich so sagen darf, von der Außenwelt etwas zum Zentral­organ geleitet wird und dann, nachdem sie vom Zentralorgan durch die andere Hälfte in einen Willen umgewandelt worden ist, weiter­geleitet würde. Diese Unterbrechung ist aus einem ganz andern Grunde da.",
      "Daß unser Nervensystem so gebaut und in dieser regelmäßigen Weise durchbrochen ist, hat seinen Grund darin: An der Stelle, wo unsere Nerven durchbrochen sind, da liegt im Abbilde im Menschen -allerdings nur im körperlichen Abbilde einer komplizierten geistigen Wirklichkeit - die Grenze zwischen physischem und geistigem Er­fahren, physischem und geistigem Erleben. Sie ist allerdings im Men­schen auf eine merkwürdige Weise enthalten.",
      "Sie ist so enthalten, daß der Mensch mit der ihm zunächstliegenden physischen Welt in eine solche Beziehung tritt, daß mit dieser Beziehung der Teil des Nerven-stranges, der bis zu jener Unterbrechung geht, etwas zu tun hat. Aber der Mensch muß auch als seelisches Wesen eine Beziehung haben zu seinem eigenen physischen Leib.",
      "Diese Beziehung, die er zu seinem eigenen physischen Leib hat, ist durch den andern Teil vermittelt. Wenn ich eine Hand bewege, dadurch veranlaßt, daß ein äußerer Sinnesein­druck auf mich gemacht worden ist, dann liegt der Impuls, daß diese Hand bewegt wird, vereinigt von der Seele mit dem Sinneseindruck, schematisch dargestellt, schon bereits hier (siehe Zeichnung, a).",
      "Und dasjenige, was geleitet wird, wird auf den ganzen sensitiven Nerven und den sogenannten motorischen Nerven entlang geleitet von a bis zu b. Das ist nicht so, daß der Sinneseindruck erst bis zu c geht und dann von da aus einen Befehl gibt, damit b dazu veranlaßt werde - nein, wenn ein Willensimpuls stattfindet, lebt das Seelische schon befruchtet bei a und geht durch den ganzen unterbrochenen Nervenweg durch.",
      "Es ist keine Rede davon, daß solche kindischen Vorstellungen, als ob die Seele da irgendwo säße zwischen den sensitiven und motorischen Nerven und wie ein Telegraphist die Eindrücke der Außenwelt emp­fangen und dann Befehle aussenden würde, es ist keine Rede davon, daß diese kindischen Vorstellungen irgendeiner auch wie immer ge­arteten Wirklichkeit entsprechen würden. Diese kindische Vorstellung, die wir immer hören, nimmt sich recht sonderbar komisch aus neben der Forderung, man soll ja in der Naturwissenschaft nicht anthropo­morphistisch sein! Da fordern nun die Leute, man solle ja nicht anthro­pomorphistisch sein und merken nicht, wie anthropomorphistisch sie sind, wenn sie Worte gebrauchen wie: Ein Eindruck wird empfangen, ein Befehl wird ausgegeben und so weiter. - Sie reden darauf los, ohne auch nur eine Ahnung davon zu haben, was sie alles für mythologische Wesen - wenn sie die Worte ernst nehmen würden - hineinträumen in den menschlichen Organismus.",
      "Nun entsteht aber die Frage: Warum ist der Nervenstrang unter­brochen? - Er ist unterbrochen aus dem Grunde, weil wir, wenn er nicht unterbrochen wäre, nicht eingeschaltet wären in den ganzen Vor­gang. Nur dadurch, daß gewissermaßen der Impuls an der Unter­brechungsstelle überspringt - der gleiche Impuls, wenn es ein Willens-impuls ist, geht schon von a aus -, dadurch sind wir selbst drinnen in der Welt, dadurch sind wir bei diesem Impuls dabei. Würde er einheit­lich sein, würde hier nicht eine Unterbrechung sein, so wäre das ganze ein Naturvorgang, ohne daß wir dabei wären.",
      "Stellen Sie sich denselben Vorgang, den Sie bei einer sogenannten Reflexbewegung haben, vor: Eine Fliege setzt sich Ihnen irgendwo hin, der ganze Vorgang kommt Ihnen gar nicht voll zum Bewußtsein, aber Sie wehren die Fliege ab. Dieser ganze Vorgang hat sein Analogon, sein ganz gerechtfertigtes Analogon auf physikalischem Gebiete. Inso­fern dieser Vorgang physikalische Erklärung herausfordert, muß diese Erklärung nur etwas komplizierter sein als ein anderer physikalischer Vorgang. Nehmen Sie an, Sie haben hier einen Kautschukball, Sie stoßen hinein, Sie deformieren den Kautschukball: das geht wieder heraus, richtet sich wieder her. Sie stoßen nochmals hinein; er stößt wieder heraus. Das ist der einfache physikalische Vorgang: eine Reflexbewegung.",
      "# Bild s. 15",
      "Nur ist kein Wahrnehmungsorgan eingeschaltet, nichts Geistiges ist eingeschaltet. Schalten Sie hier etwas Geistiges ein (innerer Kreis) und unterbrechen Sie hier (Zentrum), dann fühlt sich die Kaut­schukkugel als ein Eigenwesen. Die Kautschukkugel müßte dann aller­dings, um sowohl die Welt wie sich zu empfinden, ein Nervensystem einschalten. Aber das Nervensystem ist immer da, um die Welt in sich zu empfinden, niemals irgendwie da, um auf der einen Seite des Drahtes eine Sensation zu leiten und auf der andern Seite des Drahtes einen motorischen Impuls zu leiten.",
      "Ich deute dieses an aus dem Grunde, weil dies, wenn es weiter ver­folgt wird, auf einen der zahlreichen Punkte hinführt, wo Naturwissen­schaft korrigiert werden muß, wenn sie zu Vorstellungen führen soll, die einigermaßen der Wirklichkeit gewachsen sind. Die Vorstellungen, die heute herrschen, sind eben weiter nichts als solche Vorstellungen, die den Impulsen der Geister der Finsternis dienen. Im Menschen selber ist die Grenze zwischen dem physischen Erleben und dem geistigen Erleben.",
      "Dieses Stück des Nervs, das ich rot bezeichnet habe, dient im wesentlichen dazu, um uns hineinzustellen in die physische Welt, um uns Empfindung zu vermitteln innerhalb der physischen Welt. Das andere Stück des Nervs, das ich blau bezeichnet habe, dient im we­sentlichen dazu, um uns selbst uns empfinden zu lassen als Leib. Und es ist kein wesentlicher Unterschied, ob wir eine Farbe außen bewußt",
      "erleben durch den Strang a-c, oder ob wir innerlich ein Organ oder eine Organlage oder dergleichen erleben durch den Strang d-b; das ist im wesentlichen dasselbe. Das eine Mal erleben wir ein Physisches, das nicht in uns zu sein scheint, das andere Mal erleben wir ein Physisches, das in uns ist, das heißt innerhalb unserer Haut. Dadurch aber sind wir eingeschaltet, daß wir bei einem Willensvorgang alles das erleben kön­nen, was nicht nur außen ist, sondern auch was innerlich an uns ist. Aber die Stärke der Wahrnehmung ist verschieden vermittelt durch den Strang a-c und durch den Strang d-b. Dasjenige, was eintritt, ist allerdings eine wesentliche Abschwächung der Intensität. Wenn wir eine Vorstellung mit einem Willensimpuls zusammen formen in a, so wird dieser Impuls von a aus weitergeleitet. Indem er von c auf d über­springt, schwächt sich das Ganze so ab für unser Bewußtsein, für unser bewußtes Erleben, daß wir das weitere, was wir nun in uns erleben, die Hebung der Hand und so weiter, nur mit der geringen Intensität des Bewußtseins erleben, die wir sonst auch im Schlafe haben. Wir sehen das Wollen erst wiederum, wenn die Hand sich bewegt, wenn wir wieder von einer andern Seite her eine Sensation haben.",
      "Der Schlaf dehnt sich in der Tat anatomisch, physiologisch in das wache Leben fortwährend hinein. Wir stehen mit der äußeren physi­schen Welt in Verbindung und wachen eigentlich immer nur mit dem­jenigen Teil unseres Wesens, welcher bis zu der Unterbrechung der Nerven geht. Was jenseits der Unterbrechung der Nerven in uns selber liegt, das verschlafen wir auch am Tage. Das ist aber ein Vorgang, der noch nicht physisch ist in der jetzigen Phase der Erdenentwickelung, sondern noch in einer gewissen geistigen Höhe vor sich geht, wenn das auch vielfach zu tun hat mit den niederen Eigenschaften der Menschen-natur. Aber ich habe hier schon öfter von dem Geheimnis gesprochen, daß, was im Menschen niedere Natur ist, gerade zusammenhängt mit den höheren Außerungen gewisser geistiger Wesenheiten.",
      "Würde man im Menschen alle diejenigen Stellen sammeln, wo Ner­venunterbrechungen sind, und würde man das aufzeichnen, dann würde man zeichnungsgemäß die Grenze bekommen zwischen dem Erleben in der physischen Welt und dem Erleben aus einer höheren Welt heraus. Daher kann ich auch folgendes Schema gebrauchen. Nehmen Sie einmal",
      "# Bild s. 17",
      "an - ich zeichne hier alle Nervenunterbrechungen schematisch auf -, nehmen Sie an, da wäre der Kopf und da wäre ein Bein. Nun nehmen wir an, von hier aus ginge ein sogenannter Eindruck, und hier wäre die Nervenunterbrechungsstelle «Gehen» erfolgt. Was real ist, ist dann dieses: hier ist alles dasjenige, was der Mensch durch den Nerv erlebt, wachend bei Tag erlebt; hier ist das, was der Mensch erlebt als einen unterbewußten Willen, auch im Wachen schlafend erlebt. Und alles dasjenige, was nun unter der Nervenunterbrechungsstelle liegt, wird von der geistigen Welt heraus direkt gebildet, geschaffen.",
      "Die Vorstellungen werden Ihnen, wenn Sie sie das erste Mal hören, vielleicht etwas schwierig sein. Allein sie sollen in Ihnen auch die Vor­stellung hervorrufen, daß man ohne gewisse Schwierigkeiten in die intimeren Dinge der Erkenntnis des Menschen doch nicht hineinkom­men kann.",
      "Wenn Sie das so ansehen, daß hier (rot) alles dasjenige ist, was den Menschen mit der physischen Welt verbindet, unter dieser Grenze alles dasjenige, was den Menschen mit einer geistigen Welt verbindet, die nur heute ein untergeordnetes physisches Abbild hat in ihm - wenn Sie dies ins Auge fassen, dann können Sie eine andere Vorstellung damit verbinden. Diese andere Vorstellung, die Sie damit verbinden sollen, ist die folgende: Denken Sie sich einmal die Pflanzenwelt. Die Pflanzen wachsen aus der Erde heraus; aber sie würden nicht aus der Erde her-auswachsen, wenn sie nicht aus dem Kosmos herein Kräfte empfingen, Kräfte, die mit dem Sonnenleben innig zusammenhängen, welche alles das in Empfang nehmen, was von der Erde heraus gekraftet wird. Lesen Sie, um das besser zu verstehen, noch einmal die Abhandlung über «Das menschliche Leben vom Standpunkte der Geisteswissenschaft». Zum Leben der Pflanzenwelt gehört dieses ganze Kosmische, das von dem Kosmos herein vom Sonnenleben kommt, zusammen mit dem, was von der Erde herauf kommt.",
      "# Bild s. 18",
      "Dieses Zusammenwirken aber des Kosmischen mit demjenigen, was tellurisch, was irdisch ist, das gehört überhaupt zum Leben, zum Dasein innerhalb der physischen Welt, so wie wir sie aufzufassen haben. Und dieselben Kräfte, die unter diesem Strich (siehe Zeichnung) aus der Erde heraus auf die Pflanze wirken, zusammen mit der Samenkraft der Pflanze - der Same wird ja auch in die Erde hineingetan -, diese selbe",
      "Masse von Kräften derselben Art, die müssen Sie hier suchen, hier, wo die roten Striche sind. Diesseits der Grenze, die ich schematisch ange­deutet habe, müssen Sie meinetwillen die Kräfte suchen, die Sie sonst durch die Wurzeln von der Erde kommend für die Pflanzen suchen.",
      "Der Mensch nimmt durch seine Augen, durch seine Ohren, nament­lich durch seine Haut, von der Erde in verfeinerter Art dasjenige auf, was die Pflanze durch ihre Wurzeln aus dem Boden der Erde aufsaugt. Die Pflanze ist ein Erdenwesen durch ihre Wurzeln. Der Mensch ist ein Erdenwesen durch seine Nerven und durch dasjenige, was er als das Irdische, das Tellurische aufnimmt durch seine Lungen, durch seine Nahrung, die er von der Erde hereinbekommt. Alles das, was für die Pflanze von der Erde kommt - nur daß die Pflanze die Wurzeln in die Erde hineinversenkt -, nimmt der Mensch auf durch seine Organe, nur daß er das in verfeinerter Weise aufnimmt, die Pflanze gröber durch die Wurzeln.",
      "Aber die Pflanze nimmt noch andere Kräfte auf. Die Pflanze nimmt die Kräfte auf, welche ihr aus dem Sonnenreiche, aus dem himmlischen Reiche - räumlich-himmlischen Reiche -, aus dem Kosmos zukommen. Dieses Gebiet habe ich blau schraffiert: das sind die Kräfte, welche die Pflanze aus dem Kosmos aufnimmt. Diese Kräfte sind von derselben Art, wie die blau schraffierten Kräfte jenseits der Grenze, die ich an­gegeben habe. Der Mensch zieht aus seinem Leibe heraus das, was die Pflanze aus dem Kosmos hereinzieht. Von der Erde zieht der Mensch verfeinert diejenigen Kräfte und Substanzen, welche die Pflanze durch ihre Wurzeln vergröbert aus dem Boden zieht. Aus seinem Leibe heraus zieht der Mensch dieselben Kräfte und Substanzen vergröbert, welche die Pflanze verfeinert aus dem Kosmos zieht. Denn so, wie er sie heute aus dem eigenen Leibe herauszieht, so sind sie nicht als Kräfte unmittel­bar gegenwärtig im Kosmos vorhanden, sondern sie sind so vorhanden gewesen während der alten Mondenzeit. Von dieser hat sie der Mensch bewahrt. Der Mensch nimmt durch das, was jenseits dieser Grenze im hier gezeichneten blauen Teile enthalten ist, nicht unmittelbar aus der Gegenwart wahr, sondern aus dem, was er durch die Vererbschaft der alten Mondenzeit bewahrt hat. Er hat das Kosmische einer alten Zeit in die Gegenwart hereingetragen. In seinem Leib hat der Mensch die",
      "Mondenverhältnisse aufbewahrt. Und so sehen Sie, daß wir in einer gewissen Weise kosmisch sind; sogar so mit dem Kosmos zusammen­hängen, daß wir in uns tragen ein Abbild desjenigen, was der Kosmos draußen schon überwunden hat.",
      "Wiederum ein Beispiel für das, was ich das letzte Mal hier ange­schlagen habe: daß nichts dienlich sein wird, wenn man nur so vom allgemeinen, verschwommenen, nebelnden Standpunkte aus davon redet, daß der Mensch wiederum ein kosmisches Empfinden oder kos­mische Vorstellungen in sich aufnehmen müsse. Diese Dinge haben nur Wert, wenn sie völlig konkret an den Menschen herantreten, wenn wirklich gewußt wird, wie die Dinge liegen, wie sich die Dinge ver­halten. Dadurch wird dasjenige, was heute nur ein Probieren ist, eben auf eine gesunde, wirkliche gesunde Grundlage gestellt. Und wenn man weiß, wie alles das, was jenseits der Nervenunterbrechungen im Innern des menschlichen Leibes liegt, mit dem mondartigen Wesen zusammen­hängt, dann wird man herausfinden können aus den Verwandtschaften heraus, welche krankmachenden oder heilenden Kräfte im Kosmos und im Erdenleben zu finden sind. Und wenn man wissen wird, in welcher Weise das, was diesseits der Grenze liegt, so zusammenhängt mit den Erdenverhältnissen, nur im verfeinerten Sinne, wie die Pflanze durch ihre Bodenverhältnisse mit den Wurzeln zusammenhängt, dann wird man die Beziehung zwischen Krankheit und Gesundheit und zwischen dem Wesen gewisser Pflanzen wirklich in bewußter Art auffinden können.",
      "Heute sind die Dinge ein Probieren. Auf gesunde Grundlage muß zuerst das menschliche Erkennen gestellt werden, und dann wird auf gesunde Grundlage auch gestellt werden können, was der Mensch an Begriffen und Vorstellungen entwickelt, um das soziale, das sittliche, das pädagogische, das politische Leben irgendwie mit seinen eigenen Vorstellungen zu regeln, durchdringen zu können, ihm eine Struktur verleihen zu können.",
      "Wir machen auf vielen Gebieten die Wahrnehmung, daß gerade die­jenigen, die naturwissenschaftlich groß, fachmännisch gediegen denken, ganz gräßlich zu fabulieren, zu schwätzen anfangen, wenn sie ihre ge­wohnten Vorstellungen übertragen auf das Gebiet des sozialen Lebens.",
      "Aber dieses Gebiet des sozialen Lebens ist ja nicht ein ganz selbstän­diges Gebiet. Der Mensch steht darinnen mit seiner physischen, see­lischen, geistigen Natur, und man kann die Dinge nicht voneinander trennen. Und es darf nicht bei der Tatsache bleiben, daß die Mensch­heit auf dem sozialen Gebiet naturwissenschaftlich dumm gemacht wird, damit sie auf dem sozialen Gebiet nur zu schwätzen vermag.",
      "Man kann heute ohne Schwierigkeit leicht nachweisen, wie gedie­gene Naturforscher ins Schwätzen hineinkommen, wenn sie die Grenze zwischen Naturwissenschaft und dem geistigen Leben überschreiten. Besonders Mediziner sind auf diesem Gebiet außerordentlich produk­tiv im Hervorbringen von allerlei Geschwätz, wenn es sich darum han­delt, mit den Vorstellungen, die auf naturwissenschaftlichem Gebiete heute gewonnen werden, ins geistige Gebiet herüberzugehen. Man braucht nur irgend etwas herauszugreifen. Greift nur hinein ins volle Menschenleben - wo ihr es nur anfaßt, ist es in dieser Beziehung heute konfus.",
      "Da habe ich zum Beispiel eine Broschüre: «Die Schädigungen der Nerven und des geistigen Lebens durch den Krieg», von einem ausge­zeichneten Mediziner. Ich will gar nicht, um Ihr Vorurteil nicht zu erregen, sagen von einem wie ausgezeichneten Mediziner. Aber dieser ausgezeichnete Mediziner, er betrachtete nun dieses Nervensystem, über das die Naturwissenschaft ja eigentlich nicht einmal einen Schim­mer von einer richtigen Vorstellung hat - nach den paar Andeutungen, die ich heute gegeben habe, können Sie das sehen -, er betrachtete nun dieses Nervensystem, wie es malträtiert wird durch die gegenwärtigen Kriegsverhältnisse. Ja, man braucht nur an das Allerprimitivste zu denken und man kann darauf hinweisen, wie das wirklich vernünftige Denken aufhört, wenn herübergeleitet werden die naturwissenschaft­lichen Vorstellungen auf das, was mit dem geistigen Gebiete, ich will nur sagen, etwas zu tun hat, gar nicht einmal noch das geistige Gebiet selber ist. Nicht wahr, wenn man so etwas bespricht wie «Die Schädi­gungen der Nerven und des geistigen Lebens durch den Krieg>, dann hat man die Notwendigkeit vor sich, dasjenige, was angeblich in den Nerven vor sich gehen soll, auszudrücken durch allerlei vom geistigen Leben Entnommenem - natürlich von dem geistigen Leben, das hier",
      "auf dem physischen Plane verläuft -, durch allerlei Vorstellungen, die diesem geistigen Leben entnommen sind.",
      "Nun gibt zum Beispiel dieser Herr hier die Vorstellung - die unter gewissen Verhältnissen des abnormen Nervenlebens berechtigt sein soll -, die Vorstellung von «überwertigen Ideen». Uberwertige Ideen sind ein Symptom für kranke Nerven. Uberwertige Ideen - was ist eine überwertige Idee? Wenn man einen solchen Begriff aufstellt, dann muß man sich klar sein, daß ein solcher Begriff lebenswirklich sein muß. Aber was ist eine überwertige Idee? Eine überwertige Idee ist für jenen Mann etwas, das entsteht, wenn die Empfindungs- und Gefühls­betonung der Idee zu stark ist, wenn sie einseitig ist. Allerlei so vage Vorstellungen bringt er eben heran. Ich kann Ihnen natürlich keine bestimmte Vorstellung davon geben. Schreiben Sie, wenn ich das nicht bestimmt definiere, es nicht der Geisteswissenschaft zu, denn ich muß ja referieren. Eine überwertige Idee entsteht zum Beispiel, wenn man, durch den Krieg veranlaßt, eine fremde Nation zu viel haßt. Eine «wertige Idee» ist die richtige Vaterlandsliebe. Aber diese richtige Vaterlandsliebe wird, wenn das Nervensystem irritiert ist, überwertig. Man liebt nicht nur sein Vaterland, sondern man haßt die andern Völ­ker: jetzt ist die Idee überwertig geworden. Die wertige Idee ist gesund, und man muß aus der wertigen Idee schließen, daß auch die Nerven gesund sind. Wenn aber die Idee überwertig ist, so sind auch die Ner­ven geschädigt.",
      "Trifft man irgendwo die Wirklichkeit, wenn man auf der einen Seite so einen Nervenvorgang charakterisiert, auf der andern Seite eine Idee, die nun eine gewisse Eigenschaft haben soll? Sie soll überwertig als Idee sein. Auf der einen Seite ist der Nervenvorgang, auf der andern Seite ist Ideeüberwertiges. Die Leute würden gut tun, solche Dinge immer zu Ende zu denken, denn ein Gedanke zeigt sich nur dann in seiner Richtigkeit oder Unrichtigkeit beziehungsweise in seiner Wirk­lichkeitsgemäßheit oder Wirklichkeitsungemäßheit, wenn man ihn zu Ende denkt. Eine überwertige Idee wäre es, wenn ich mir vorstellen würde, ich wäre der König von Spanien. Nicht wahr, ganz zweifellos wäre das eine überwertige Idee. Aber jene Idee brauchte durchaus nicht überwertig zu sein, wenn ich es wirklich wäre. Dann wäre mein Nervensystem",
      "ganz gesund und ich hätte dieselbe Idee. Die Idee hat den­selben Inhalt. Die Idee als solche ist also doch wohl nicht überwertig, denn sonst müßte man den König von Spanien als krank ansehen in seinem Nervensystem, weil er denkt, er wäre der König von Spanien, nicht wahr? Also auf diesen Zusammenhang kommt es überhaupt gar nicht an. Dennoch wird herumgeschwätzt über diese Dinge. Und man redet nicht nur herum, sondern man bildet auch Begriffe, Definitionen aus und so weiter, und man kommt dann zu Merkwürdigem, was nicht mehr ist als Geschwätz.",
      "Denn nun hat der gute Herr diesen Begriff von überwertigen Ideen ausgebildet. Die Überwertigkeit der Idee ist nun das Symptom für das unrichtige Nervenleben. Na, schön! Aber seinem Unterbewußten ist nicht recht wohl dabei, weil er unterbewußt doch fühlt: während er die ganze Sache von der Uberwertigkeit der Ideen den Leuten vorträgt, haben die wiederum allerlei unterbewußte Ideen von dem, daß die Sache doch nicht recht stimmt. Bei den Zuhörern bleibt die Sache heute selbstverständlich unterbewußt, denn der Herr ist eine Autorität - ver­zeihen Sie! -, da dürfen die Eindrücke nicht ins Bewußtsein dringen. «Denn mit der Bezeichnung der  soll nicht nur die an sich lebhafte hohe Bewertung der betreffenden Vorstellungen, sondern eben auch ihre  im Verhältnis zur realen Bedeutung der ihnen wirklich zugrunde liegenden Tatsächlichkeiten ausgedrückt wer­den. Die überwertige Idee beherrscht das Bewußtsein so sehr, daß neben ihr nicht genügend Platz für andere, objektiv ebenfalls berechtigte Ideen vorhanden ist. Darum werden letztere verdrängt, verlieren ihre Wirksamkeit im Bewußtsein und ihren Einfluß auf die Beschränkung und Zügelung der überwertigen Vorstellungen. So entsteht die einseitige Übertreibung in der Urteilsbildung, die einseitige Richtung derWillens­bestrebungen, die Abkehr von allen andern Gedankenkreisen, die mit dem Zentrum der überwertigen Ideen nicht unmittelbar zusammen­hängen.» So wie wenn man sagt: Die Armut kommt von der Pauvreté -so ungefähr ist es!",
      "«Daher erscheint dem ruhig urteilenden Beobachter das nervös er­regte Bewußtsein stets als etwas Unvernünftiges, als etwas geistig Halt­loses, und es entspricht daher durchaus der Tatsächlichkeit, wenn der",
      "ruhige Zuschauer den nervös erregten Menschen mit den Worten: , wieder auf die rechte Bahn des Denkens und Urteilens zu bringen versucht.»",
      "Nun also hat er von der Überwertigkeit der Ideen gesprochen, von ihrem Zusammenhang mit dem Nervensystem. Aber nun wird ihm etwas schwül im Unterbewußtsein, denn die Geschichte ist ja nur ein Gerede, und es paßt schlecht. Na, da setzt er denn die Rede fort: «Wir dürfen aber die  nicht ohne weiteres jeder überhaupt gefühlsbetonten und ungewöhnlich lebhaften Vorstellungsweise gleich­stellen. Auch alles Edle und Hohe, was den Menschengeist bewegt und ihn zu großen Taten befähigt, was Hingabe und Begeisterung für eine große Tat und für die Anspannung aller Kräfte zu Erreichung eines großen Zieles erweckt, auch dies entspringt nur aus großen Ideen, die den Geist beherrschen und ihm die Kraft und Ausdauer des Willens geben, ohne die ein zielbewußtes Handeln nicht möglich ist.»",
      "Überwertige Ideen, sie zerstören das Nervensystem, sind wenigstens ein Symptom dafür; aber alles Hohe und Edle ist eigentlich ebenso. Es gibt keinen rechten Unterschied. Aber er muß wenigstens erwähnen, daß die Geschichte eigentlich ebenso ist.",
      "«Überall in der Geschichte des Einzelnen und in der Geschichte der Völker sehen wir die großen Taten vollbracht unter dem Einfluß einer großen leitenden Idee, die ihren Träger unaufhaltsam und auf der gleichen Bahn und in derselben Richtung festhielt und vorwärtstrieb, ihn erst befähigte zu jener unermüdlichen Ausdauer, die trotz Hinder­nissen und Widerständen das einmal erkannte und erstrebte Ziel er­reichen konnte. Was wäre aus Galilei, aus Richard Wagner, aus Bis­marck und aus vielen andern großen Männern geworden ohne die Schwungkraft einer großen leitenden Idee, die den Geist jahre- und jahrzehntelang trotz aller Kämpfe und Widerstände in eine bestimmte Richtung des Wollens vorwärtstrieb!» - die also «überwertig» war, die ganz ausgesprochen «überwertig» war!",
      "Da wird manchmal solch ein Anflug von Ehrlichkeit vollzogen. Es gibt eine naturwissenschaftliche Richtung, die alle Genies zugleich für etwas verrückt erklärt, weil ja auf diesem Boden so ein richtiger Unter­schied zwischen der Genialität und der Verrücktheit ohnedies nicht",
      "herauszufinden ist. Und ich habe Ihnen gesagt, daß es heute auch schon Werke gibt, die den Christus Jesus als einen pathologisch Kranken hin­stellen, so daß eigentlich das ganze Christentum der Ausfluß der Tat­sache ist, daß einmal einer in Palästina, der den Namen Jesus geführt hat, nicht recht gescheit war. Das ist heute Gegenstand von verschie­denen ernst gemeinten, als wissenschaftlich angesehenen Persönlich­keiten.",
      "Die Leerheit solchen Denkens, die tritt manchmal in krasser Art zutage, so wenn der betreffende Herr dann gleich fortfährt: «Aber darin liegt die Tragik des Menschengeistes, daß die Vorstellungen, wel­che mit größter Stärke das Bewußtsein erfüllen, nicht immer die rich­tigen sind» - sehr tief ist hier die Tragik des Menschengeistes erklärt, außerordentlich tief! - «und sich nicht immer einfügen in den geord­neten Zusammenhang der äußeren Welt.»",
      "Nun haben wir es! Wie weit ist es von solchen Vorstellungen zu der Erkenntnis, die nur erreicht werden kann auf Grundlage von solchen Betrachtungen, wie wir sie hier anstellen. Gewiß, es kann in zwei Men­schen dieselbe Vorstellungsmasse anwesend sein, nur ist sie das eine Mal, sagen wir luziferisch, das andere Mal ahrimanisch, das dritte Mal ist sie im Sinne der normalen Menschheitsentwickelung. Statt das in­haltsleere Wort «überwertige Ideen» zu bilden, muß der Begriff einer Geistigkeit eingeführt werden, wie die luziferische oder ahrimanische Geistigkeit, so daß man weiß: darauf kommt es an, daß man erkennt, ob der Mensch selbst will, oder ob ein anderes in ihm will. Aber davor schreckt natürlich solche angebliche Wissenschaft heute noch zurück.",
      "Sehr nett werden dann die Dinge, wenn man erwarten will, daß nun wirklich etwas Substantielles vorgebracht wird: «Da nenne ich zu­nächst» - er will zunächst das angeben, wodurch sich gewisse nervöse Störungen beim Menschen ankündigen -, «da nenne ich zunächst die­selben Vorstellungen, welche auch bei der Nervosität des einzelnen oft die größte Rolle spielen:» - er meint, beim heutigen Völkerwahn eben auch - «die Vorstellungen der Verzagtheit, der Sorge, des Kleinmuts, der Mutlosigkeit, des mangelnden Selbstvertrauens.»",
      "Das sind also diejenigen Dinge, welche das gestörte Nervensystem charakterisieren beim nervösen Leben, das unter überwertigen Ideen",
      "steht. Verzagtheit, Sorge, Kleinmut, Mutlosigkeit, mangelndes Selbst­vertrauen. Nicht wahr, solch ein Vortrag ist doch Mittel dazu, daß er irgendwie nützlich sein könnte. Denn um bloß die Luftwellen zu er­regen, wird wahrscheinlich die betreffende Autorität nicht sprechen, sondern um irgendwie nützlich zu sein. Man sollte also erwarten, daß der betreffende Herr nun sagt, wie die Menschheit darüber hinaus-kommt, da er wie beim einzelnen Menschen, so auch in der Menschheit findet, daß heute Mutlosigkeit, Verzagtheit, Sorge, mangelndes Selbst­vertrauen Symptome sind für die Nervenstörung. Man sollte glauben, daß er nun sagt, wie diese Geschichten zu beheben sind, wie man über diese Mutlosigkeit, Sorge, Verzagtheit, mangelndes Selbstvertrauen hin-auskommt. Man sollte das voraussetzen. Er setzt es eigentlich auch voraus. Er sagt daher: «Und so kann, wenigstens zeitweise, in großen Volksschichten jene mutlose unzufriedene Stimmung einreißen, die wir mehr zu fürchten haben als alles andere. Denn sie führt zum Nach­lassen kräftiger Willensregungen, zur Lockerung der festen einheit­lichen Zielstrebigkeit, zur Schwächung der Energie und Ausdauer.»",
      "Nun erwartet man also etwas, nicht wahr? Da sagt er: «Nicht ner­vös werden heißt daher in erster Linie Mut, Zuversicht und Vertrauen auf die eigene Kraft und das als richtig erkannte Handeln nicht ver­lieren.»",
      "Na, schön, jetzt haben wir es. Man ist nervös, wenn man die Sorge, Mutlosigkeit, Verzagtheit, mangelndes Selbstvertrauen hat. Wie kriegt man es weg? Wenn man es nicht hat! Es ist ganz klar, nicht wahr, wenn man es nicht hat!",
      "Diese Nichtigkeit des Denkens überträgt sich auf das Substantielle auch in der Wissenschaft, und solche Autoritäten haben alles Material zur Verfügung, haben alles Material okkupiert, es konfisziert, wenn irgendwie versucht werden soll, mit Vernunft das Material zu bear­beiten - aber indem sie das Material bearbeiten, bearbeiten sie es mit nichtigen Gedanken. Das anatomische, physiologische, physikalische Material geht verloren. Nichts wird geschaffen, weil an demjenigen Tisch, wo das Nützliche für die Menschheit geschaffen werden soll, Leute stehen mit solchen Nichtigkeitsgedanken! Selbstverständlich kann bei der Sektion einer Leiche nichts herauskommen, wenn - verzeihen",
      "Sie den harten Gedanken - ein Hohlkopf seziert. Hier werden die Dinge schon sozial. Von diesem Gesichtspunkte aus müssen schon die Dinge angesehen werden. Und eine so vielversprechende Abhand­lung, die einen Vortrag wiedergibt, endet auf solche Weise!",
      "Ich habe Ihnen das eine Beispiel angeführt: Nicht nervös werden heißt daher in erster Linie Mut, Zuversicht und Vertrauen nicht ver­lieren. Aber wenn heute der Durchschnittsleser solch eine Abhandlung in die Hand nimmt und liest: «Die Schädigungen der Nerven und des geistigen Lebens durch den Krieg», denkt er: Da kann ich aufgeklärt werden, denn das ist von Professor Dr. Soundso, Direktor der medi­zinischen Klinik in Soundso. - Nun ja, da ist er sich also klar darüber: jetzt wird er natürlich aufgeklärt.",
      "Doch da steht zum Beispiel auf Seite 27, wo der Völkerhaß bespro­chen wird: «Aber freilich auch in uns selbst loderten ähnliche Erregun­gen auf, und wir empfanden es fast als eine erleichternde Genugtuung, nun auch unsererseits unserem Hauptfeinde mit ähnlichen Gesinnungen gegenüberzutreten. Und doch bedarf es nur geringer ruhiger Über­legung, um zu erkennen, daß dieser allgemeine Völkerhaß nur der Aus­fluß einer krankhaften, überreizten Seelenstimmung ist, in welche die Volksmassen durch gegenseitige Anfeuerung, Aufhetzung und Nach­ahmung geraten sind.»",
      "Nun, wie ist also nach diesem Satz die Geschichte mit dem Völker-haß eigentlich gekommen? Da sind Volker: A, B, C; eigentlich ist weder A noch B noch C irgendwie geeignet, von sich aus zu hassen, denn davon ist ja die ganze Geschichte nicht gekommen, sondern ge­kommen ist dieser allgemeine Völkerhaß durch eine krankhaft über­reizte Seelenstimmung, in welche die Völkermassen durch gegenseitige Anfeuerung, Aufhetzung und Nachahmung geraten sind. Also der A kann es nicht; der B auch nicht; der C kann es auch nicht machen; aber was jeder nicht machen kann, dazu reizen sie sich nun gegenseitig auf. Denken Sie sich, wie scharfsinnig der Gedanke ist! Ich erkläre etwas, ich habe vor mir A, B, C; das alles ist nicht geeignet zur Erklärung -aber sie machen es doch. Ich erkläre also etwas aus dem Nichts heraus auf die schönste Weise. Diese Dinge nehmen die Menschen in die Hand, lesen sie, werden nicht aufmerksam, daß das ein bloßer Unsinn ist.",
      "Es ist schon nötig, auf solche Dinge hinzuweisen, denn sie zeigen, wie verrenkt, wie nichtig das Denken ist, das heute die Autorität in Anspruch nimmt. Natürlich, in der Wissenschaft, die sich auf das schon Vorhandene bezieht, da tritt das nicht so stark zutage, denn da kann man die Geschichte nicht kontrollieren. Aber so wie die Leute da in der Wissenschaft denken, so denken sie auch im sozialen, im pädagogischen, im politischen Leben. Und so hat sich das seit vier Jahrhunderten vor­bereitet. So ist die Sache. Und so ist es gekommen, daß aus dem ver­renkten, nichtigen Denken eben allmählich jene Impulse geworden sind, welche wir in den heutigen katastrophalen Ereignissen uns ent­gegentreten fühlen. Da muß man schon in das Tiefere der Sache eben durchaus hineinsehen. Und erst wenn die Menschen dann an die Ober­fläche der Dinge kommen, da wo, ich möchte sagen, die Sache unmittel­bar aktuell für den einzelnen Menschen wird und auch für die soziale Struktur ganzer Völker es werden kann, da wird die Sache ganz be­sonders gräßlich traurig!",
      "Nicht wahr, man hat die Aufgabe, auf der einen Seite die Dinge zu begreifen; man muß sie in ihrer gegenseitigen Abgegrenztheit kennen­lernen,wenn man sie verstehen will. Will man ein solches Ereignis selbst wie den gegenwärtigen Krieg, das so kompliziert ist und heute eben wirklich in seinen Einzelheiten selbstverständlich nicht erfaßt werden kann vom physischen Plane aus, verstehen, muß man ihn, wie man sagt, auf seine Ursachen zurückführen und so weiter. Aber jeder glaubt daran: wenn er eine Sache auf seine Ursache zurückgeführt hat, wenn er sie in einer solchen Weise verstanden hat, so sei sie auch notwendig, hätte so geschehen müssen, wie sie da ist. Heute zum Beispiel merkt man nicht einmal im geringsten, daß das eine mit dem andern gar nichts zu tun hat. Dadurch daß man eine Sache in ihren Zusammen­hängen erkennt, ist nicht etwa festgestellt, daß das Ereignis hat ein­treten müssen, wie man sagt, daß es nicht hätte unterbleiben können. Derjenige, der versucht, sich in einer mehr oder weniger gescheiten Weise klarzumachen, warum der gegenwärtige Krieg hat kommen müssen, warum er nicht etwas ist, was ein paar Leute beschlossen haben, sondern was schon mit tieferen Ursachen in der Menschheitsentwicke­lung zusammenhängt, der geht dann oftmals befriedigt von dannen",
      "und sagt: Also habe ich begriffen, daß es gar nicht anders möglich war, als daß dieser Krieg hat kommen müssen! - Er ist selbstverständlich eine Notwendigkeit in dem Sinne, daß, wenn man seine Ursachen kennt, er aus diesen Ursachen, aus diesen konkreten Bedingungen mit aller Notwendigkeit sich entwickelt hat. Aber das besagt nicht, daß man daraus den Schluß ziehen darf: die Sache hat unmittelbar so kom­men müssen, wie sie gekommen ist. Kein Ereignis, das in der Welt­geschichte auftritt, ist in diesem letzteren Sinne notwendig, obzwar es im ersteren Sinne notwendig ist - kein Ereignis ist in diesem letzteren Sinne notwendig. Jedes könnte anders sein; und jedes könnte auch nicht sein!",
      "Und derjenige, der dann von der absoluten Notwendigkeit spricht, der könnte mit demselben Rechte sich überlegen: Ich möchte gerne wissen, wann ich sterben werde. Ich gehe also zu einer Versicherungs­gesellschaft; die Leute rechnen aus, danach bestimmen sie die Versiche­rungspolicenhöhe: wieviel von einer gewissen Anzahl von Menschen nach einer gewissen Zeit gestorben sind und wie viele noch lebend sind. Danach werden die Quoten ausgezahlt. Ich gehe also einmal, erkundige mich bei einer Versicherungsgesellschaft; nach deren Ausrechnungen muß es sich ergeben, ob ich nun 1920 schon gestorben sein werde.",
      "Das ist natürlich ein absoluter Unsinn. Aber derselbe Unsinn ist es, wenn man die Notwendigkeit eines Geschehens herleiten will aus dem andern, dem Begreifen der Ursache, die zu diesem Geschehen führen muß. Und hiermit schlage ich ein Thema an, das allerdings nicht leicht ist, aus dem Grunde, weil gerade auf diesem Gebiete die allerverrenk­testen Ideen herrschen, weil auf diesem Gebiete auch heute noch nicht sehr viel Wille besteht, sich über die Dinge klarzuwerden.",
      "Die Sache ist diese: Man muß, wenn man sich gerade über die Frage klarwerden will, die hiermit angeschlagen ist, ins Auge fassen, daß, wenn irgend etwas eintritt, dieses unter dem Einfluß von gewissen Be­dingungen eintritt. Man kommt in der Reihe der Bedingungen immer zu einem Punkte, wo in der Welt Anfänge, richtige Anfänge sind. Wenn Sie heute ein Bäumchen sehen, das noch klein ist, so wissen Sie: in spä­terer Zeit wird es größer sein. Mit Notwendigkeit entwickelt sich die Größe des Bäumchens aus seiner Kleinheit heraus. Und Sie können",
      "nach einiger Zeit sagen: Es ist eine Notwendigkeit, daß dieses Bäum­chen sich so entwickelt hat; ich konnte sehen, wie es sich mit Notwen­digkeit entwickelte aus einem ganz kleinen heraus, vielleicht als es eben die ersten Triebkräfte aus der Erde hervor entwickelte. Wenn ich Botaniker bin, kann ich sehen, daß da mit Notwendigkeit ein großer Baum nach einiger Zeit entstehen muß. Wenn aber das Samenkorn nicht dort an jener Stelle hineingefallen wäre, wie dann? Vielleicht hat es ein Mensch hineingetan. Wenn er es nicht getan hätte, dann wäre da ein Punkt, wo die Notwendigkeit nicht eingeleitet worden wäre. Nun aber muß da die Notwendigkeit beginnen. Und, sagen wir, Sie haben hier eine mächtige Eiche - sie ist ja nicht in Wirklichkeit da -, Sie schauen sie an und bewundern sie. Diese Eiche war selbstverständlich einmal ein kleines Bäumchen, sie hat sich mit Notwendigkeit aus einem kleinen Bäumchen entwickelt. Aber nehmen Sie an, ein nichtsnutziger Bube oder - pardon, um nicht unhöflich zu werden - ein nichtsnutziges Mädchen wäre, als das Bäumchen noch ganz klein war, dahin ge­kommen, wo das kleine Bäumchen stand und hätte es ausgerissen:",
      "durch dieses Ausreißen hätte sich jene ganze Notwendigkeit nicht er­geben. Auch in negativer Weise können Sie die Notwendigkeit weg­nehmen.",
      "Anfangspunkte, wo die Notwendigkeiten beginnen, stellen sich dem wirklichkeitsgemäßen Denken ein, das ist das Wesentliche. Aber zu diesen Anfangspunkten kommt man nicht, wenn man nur den äußeren Verlauf der Tatsachen betrachtet. Man kommt nur zu ihnen, wenn man die geistige Grundlage wenigstens erfühlen kann. Denn geradeso wie Sie hier einen Rosenstrauß haben und wie der, wenn Sie ihn vorstellen, für den Abstraktling eine Vorstellung gibt, welche Wirklichkeit ab-bildet - denn der Rosenstrauß ist ihm wirklich, und seine Vorstellung bildet Wirklichkeit ab -, für den Okkultisten ist der Rosenstrauß, wenn er ihn vorstellt, gar nichts Wirkliches, weil der Rosenstrauß nicht exi­stiert; die Rosen können nur existieren, wenn sie mit der Wurzel zu­sammen in dem Erdboden sind und so weiter. Die wirklicheVorstellung ist nicht gegeben, wenn man von vornherein etwas Außerliches nach-bildet, sondern wenn man aus der Wirklichkeit heraus diese erlebte Vorstellung nachgebildet hat. Diese erlebte Vorstellung ergibt sich aber",
      "auch gegenüber der äußeren sinnlichen Wirklichkeit nur der geistes­wissenschaftlichen Betrachtung.",
      "Und so ergibt sich auch für ein weltgeschichtliches Ereignis nur dann eine gültige Vorstellung, wenn man geisteswissenschaftlich dieses weltgeschichtliche Ereignis überblicken kann. Da findet man, daß es in bezug auf seine Notwendigkeit allerdings sich verfolgen läßt.",
      "Man fin­det seine Verästelungen, seine Wurzeln in der Wirklichkeit drinnen. Aber nur mit diesem konkreten Verfolgen der Wurzeln ist etwas getan, nicht mit der allgemeinen Konstatierung von einer abstrakten Not­wendigkeit.",
      "Wären aber zum Beispiel gewisse Ereignisse in den acht­ziger Jahren des 19. Jahrhunderts anders gewesen, dann wären die Er­eignisse 1914 auch anders geworden. Aber darauf kommt es eben an, daß man nicht so wie die Historiker vorgeht: Jetzt geschieht etwas, das die Wirkung zum Vorhergehenden ist, das ist wiederum die Wirkung vom Vorhergehenden, dieses wiederum die Wirkung vom Vorher­gehenden und so weiter.",
      "Da kommt man nicht nur bis zum Anfang der Welt, sondern noch weiter ins völlige Nichts hinunter. Da kugelt so eine Vorstellung hinter der andern daher. Darauf kann es nicht an­kommen, sondern auf das konkrete Verfolgen dieser Sache, auf das wirkliche Einwurzeln.",
      "So wie die Pflanzenwurzel irgendwo anfängt, so fangen die Ereignisse auch irgendwo an. Keime werden gelegt im Laufe der Zeit. Wenn die Keime nicht gelegt werden, dann entstehen auch die Ereignisse nicht.",
      "Ich schlage damit ein Thema an, das ich selbstverständlich heute nicht erschöpfen kann. Wir werden am näch­sten Sonntag über dieses Thema, welches ich im wesentlichen dadurch bezeichnen will: Trotz aller Betrachtung der Notwendigkeit ist kein einziges Ereignis absolut notwendig - noch zu sprechen haben.",
      "Es ist wirklich notwendig, daß die Menschheit der Gegenwart auch der Gesinnung nach aus diesem furchtbaren Dogmatischen, das heute die sogenannte Wissenschaft durchzieht, herauskommt, daß die Dinge ernst genommen werden. Ich will Ihnen ein richtiges Beispiel anführen. Damit will ich dann die heutigen Betrachtungen abschließen. Ich habe in Zürich und in Basel versucht, klarzumachen, daß es ein Unsinn ist, die welthistorischen Ereignisse so hintereinander zu betrachten, als ob eines aus dem andern hervorgehe. Ich habe gesagt, es sei ein Unding,",
      "wenn ein Ereignis aus dem andern folge, nur 50 eins aus dem andern hervorgehend zu betrachten. Das sei so, wie wenn ich hier eine Licht­quelle habe, welche zuerst den Gegenstand a beleuchtet, dann den Ge­genstand b beleuchtet, endlich den Gegenstand c beleuchtet. Da sehe ich in meiner Beobachtung zuerst a, dann b, dann c beleuchtet, wenn ich die Lichtquelle gar nicht wahrnehme. Jetzt würde ich einen Fehler machen, nicht wahr, wenn ich zuerst a beleuchtet sehe, dann b, und würde sagen, das b wird von a her beleuchtet; und wenn ich dann c beleuchtet sehe und würde sagen, das c wird von b her beleuchtet. Ich würde etwas ganz Unrichtiges sagen, denn die Beleuchtung von b und c hat gar nichts damit zu tun, sondern es wird von einer gemeinsamen Lichtquelle aus beleuchtet. Ich habe dieses Beispiel gebraucht, um die historischen Ereignisse zu erläutern.",
      "Nehmen Sie nun an, es würde jemand diesen Begriff, den ich damit gegeben habe, diese Idee nett finden. Es könnte sein, daß auch einmal ein auf anthroposophischem Boden entwachsener Begriff nett befunden würde. Es ist sogar in der letzten Zeit hie und da vorgekommen, daß gerade Gegner diese Begriffe genommen haben, um sie ihrerseits nun zu verwenden. Manche sind sogar Gegner geworden, weil so etwas moniert werden mußte. Also es könnte einmal sein, daß auch eine auf anthroposophischer Seite vorgebrachte Analogie nicht gerade Blödsinn wäre. Nehmen wir an, es griffe es jemand auf, aber er brächte es dann vor in einem andern Zusammenhang, als ich es vorgebracht habe; er brächte es dogmatisch vor - nicht wie ich symptomatisch -, mit einer andern Gesinnung, und ich hörte einen Vortrag, in dem er sagte: Es wird ganz falsch die Aufeinanderfolge von Ursache und Wirkung dar­gestellt, wenn man immerfort sagt, Wirkung b ist die Folge von Ur­sache a, Wirkung c die Folge von Ursache b und so weiter; denn damit begeht man denselben Fehler, wie wenn man sagen würde, wenn das a beleuchtet wird, das b beleuchtet wird, das c beleuchtet wird, so ist das b infolge von a beleuchtet und das c infolge von b beleuchtet. Wenn ich das anhöre und das nicht in demselben Zusammenhang vorgebracht würde wie von mir in Basel und in Zürich, so würde ich dem Mann vielleicht aus seinem Zusammenhange einwenden können: Wenn die Sache aber so ist, daß a, b und c sogenannte nachleuchtende Materien",
      "sind - es gibt ja solche Materien, man exponiert sie einer Lichtquelle, da fangen sie dann selber an zu leuchten, die Lichtquelle kann entfernt sein -, wenn dann a tatsächlich, weil es nachleuchtet, das b beleuchtet, und b wiederum, weil es nachleuchtet, das c beleuchtet: nun, dann kann die Geschichte so sein, daß das b infolge von a, und das c infolge von b beleuchtet ist. Also die ganze Analogie könnte eine sehr brüchige sein, wenn sie einer vertritt, der nicht im Verlaufe seines Vortrages vor­gebracht hat, daß Begriffe für die Wirklichkeit im geistigen Leben so sind wie Photographien. Wenn man von der einen Seite die Photogra­phie aufnimmt, nimmt es sich anders aus, als wenn man von der andern Seite die Photographie aufnimmt. Wenn man das nicht voraussetzt, wenn man nicht hinführt zu wirklichkeitsgemäßen Begriffen, so daß diese wirklichkeitsgemäßen Begriffe immer perspektivische Begriffe sind, dann kann man unter Umständen mit demselben, was absolut richtig ist, wenn man es perspektivisch meint, einen Unsinn sagen, sobald man es absolut sagt.",
      "Das ist der Unterschied, ob einer von der Wirklichkeit ausgeht, oder ob einer von Begriffen ausgeht. Wenn einer von Begriffen ausgeht, so wird er immer in eine Einseitigkeit verfallen. Wenn aber einer von der Wirklichkeit ausgeht, so darf er - weil er nichts anderes kann, als Be­griffe vorbringen, und jeder Begriff ist einseitig -, so darf und muß er einseitige Begriffe vorbringen, denn das ist nur ganz selbstverständlich. Also Sie sehen, es kommt auf eine vollständige Umänderung des see­lischen Lebens, eine tiefgehende Umänderung des seelischen Lebens an. Daher ist es natürlich auch gar nicht schwer, zahlreiche Begriffe, die vorgebracht werden von mir, zu kritisieren. Ich weiß nicht, ob einer auf diese Kritik gerade gekommen wäre, aber ich selber komme schon auf alles dasjenige, was notwendig ist zu kritisieren.",
      "Man muß das Bewußtsein haben, wie sich die Vorstellung zu der Wirklichkeit verhält. Dann erst hat man die Möglichkeit, in die Wirk­lichkeit einzudringen, sonst streitet man immer über Vorstellungen. Und die ganze Welt streitet heute über Vorstellungen auf sozialem Ge­biete,wenn auch dieses Streiten eben sich umgesetzt hat in äußere Taten. Und sehr häufig setzt sich das Streiten über äußere Vorstellungen in äußere Taten um. Diese Dinge führen schon in große Intimitäten hinein,",
      "Intimitäten des geistigen Lebens. Aber man muß sich solche Dinge überlegen, wenn man das Dasein verstehen will.",
      "Nachdem ich Sie heute in mehr theoretischer Weise auf solche Dinge aufmerksam gemacht habe, werde ich das nächste Mal über Zeitge­schichte von diesem Standpunkte sprechen, werde zeigen, inwiefern es notwendig war, daß gewisse Ereignisse gekommen sind; aber inwiefern diese Ereignisse gar nicht notwendig waren, sondern ganz andere Er­eignisse hätten kommen können. Ereignisse, unter deren katastrophaler Art wir alle leiden, hätten gar nicht zu kommen brauchen. Diese wich­tige Frage wollen wir dann am nächsten Sonntag weiter besprechen."
    ],
    "sentences": [
      [
        "Wir werden heute fortfahren, einiges hinzuzutragen zu den Betrach­tungen, die wir angestellt haben.",
        "Es war mir in dieser Zeit viel darum zu tun, begreiflich zu machen, von welchen Bedingungen das mensch­liche Leben abhängt im einzelnen und in dem großen Zusammenhange.",
        "Sie haben gesehen, wie auch in den öffentlichen Vorträgen, die ich in dieser Zeit halten durfte, es mir darauf ankam, gerade jetzt auf die­jenigen Probleme der Geisteswissenschaft hinzuweisen, welche für das Begreifen der Menschheit notwendig sind, um aus gewissen Vorstel­lungskreisen herauszukommen, in die sich die Menschheit gewisser­maßen über den ganzen Erdkreis hin eingesponnen hat und die letzten Endes doch mit zu den Veranlassungen der jetzigen katastrophalen Ereignisse gehören."
      ],
      [
        "Vor allen Dingen wird es sich darum handeln, daß die Menschen einsehen lernen müssen, wo die Grenze zwischen der sogenannten phy­sischen und der geistigen Welt liegt.",
        "Diese Grenze liegt eigentlich mitten im Menschen drinnen.",
        "Gerade dieser Satz ist wichtig für das Verständ­nis der Welt: daß wir die Grenze zwischen der physischen und geistigen Welt in dem Menschen selber drinnen sehen.",
        "Die naturwissenschaftliche Denkungsweise, deren große Bedeutung für die Gegenwart und die Zu­kunft ich vom Gesichtspunkt der Geisteswissenschaft oftmals hervor­gehoben habe, ist aber jetzt, wo sie noch mehr oder weniger immer an ihrem Ausgangspunkte steht, eigentlich dazu geeignet, über gewisse wichtige Lebenswahrheiten, man könnte schon sagen, zunächst sogar Finsternis zu verbreiten."
      ],
      [
        "Machen wir uns nur klar, daß sich die Zeitentwickelung eigentlich heute erst dazu anschickt, das naturwissenschaftliche Denken allmäh­lich in die Welt- und Lebensanschauungen ganz einzuführen.",
        "Heute beschäftigen sich - in einer oftmals haarsträubend dilettantischen Weise - gewisse Monisten- oder andere Vereine damit, naturwissen­schaftliche Weltanschauung dem Allgemeinbewußtsein zuzuführen.",
        "Allein dies ist ja nur der eine Weg, durch den allmählich dieses naturwissenschaftliche"
      ],
      [
        "Denken in die Menschenseele fließt.",
        "Der viel wirk­samere, einschneidendere Weg ist der durch die Publizistik."
      ],
      [
        "Nicht umsonst, sondern durchaus innerlich zusammengehörig fallen in die Menschheitsentwickelung der Einschnitt der neueren naturwis­senschaftlichen Denkungsweise und die Erfindung der Buchdrucker-kunst zusammen.",
        "Denn dasjenige, was bisher durch den Druck als Ursprüngliches in die Menschheit eingegangen ist, selbstverständlich abgesehen von dem, was man von früher schon Dagewesenem gedruckt hat, ist im wesentlichen aus naturwissenschaftlichem Bewußtsein her­vorgegangen.",
        "Ich meine, das Neue ist aus naturwissenschaftlichem Bewußtsein hervorgegangen, und vor allen Dingen die Art und Weise, in die man die Gedanken eingefangen hat, ist aus naturwissenschaft­licher Denkweise hervorgegangen."
      ],
      [
        "Nun werden natürlich Theologen gegenüber einem solchen Aus­spruch sagen: Ja, haben wir denn nicht auch unsere theologische Weis­heit und alle möglichen frommen Dinge in den letzten Jahren und Jahrzehnten und Jahrhunderten gedruckt? - Ja, das ist allerdings wahr, aber wozu hat es geführt?",
        "Diese Art und Weise, wie unter der Flagge des Druckes das geistige Leben sich eingelebt hat in die Seelen der Men­schen, hat dazu geführt, daß nach und nach ganz geschwunden ist auch aus dem Gebiete des religiösen Bewußtseins das spirituelle Element.",
        "Und selbst aus dem Christus Jesus, das wissen Sie ja, hat man unter dem Einfluß der naturwissenschaftlichen Denkweise den «schlichten Mann aus Nazareth» gemacht, den man zwar versucht in der ver­schiedensten Weise zu charakterisieren, der aber doch eigentlich schon dabei angelangt ist, mit den andern großen Persönlichkeiten der Welt in eine Linie gestellt zu werden, wenn auch vorläufig noch auf einem besonderen Gipfel.",
        "Das eigentlich Geistige, das mit dem Mysterium von Golgatha verknüpft ist, das ist nach und nach dahingeschwunden, wenigstens für diejenigen, die da glauben, mit der Zeitenbildung vor-wärtsgeschritten zu sein."
      ],
      [
        "Ich sagte, die naturwissenschaftliche Denkweise hat zunächst ge­radezu mitwirken müssen zu einer gewissen Verfinsterung, zu einer Unterstützung desjenigen, was nun seit 1879 durch die Geister der Finsternis in das menschliche Denken hineingebracht werden soll."
      ],
      [
        "Und auf naturwissenschaftlichem Gebiete zeigt sich die Sache in einer recht raffinierten Art, raffiniert deshalb, weil der naturwissenschaft­lich nicht nur Durchgebildete, sondern der naturwissenschaftlich fachmännisch Gebildete, wenn er heute mitarbeitet an der allgemeinen Bildung der Zeit, an der Gestaltung der Weltanschauung, gar nicht anders kann, so wie heute die Wissenschaft einmal ist - lassen Sie mich das triviale Wort anwenden -, als «aus bestem Wissen und Gewissen heraus» so zu wirken, daß durch die Popularisierung der naturwissenschaftlichen Denkweise der Mensch geradezu abgebracht wird davon, den Blick hinwerfen zu können auf die Grenze, die in ihm selber ist zwischen der physischen Welt und der geistigen Welt.",
        "Es wird eine Zukunft des Menschendenkens anbrechen, es ist fürchterlich, daß dies heute gesagt werden muß, fürchterlich für die nach einer gewissen Richtung heute Gebildeten, da werden gewisse Vorstellungen, die heute in der Wissenschaft herrschen - und die zwar nicht im populären Be­wußtsein sehr vorhanden sind, aber auf das populäre Bewußtsein da­durch wirken, daß man heute die Wissenschafter als, verzeihen Sie, Autoritäten ansieht -, gewisseVorstellungen der Gegenwart werden vor einem künftigen Zeitbewußtsein geradezu komisch anmuten müssen."
      ],
      [
        "Auf eine Vorstellung habe ich öfters hingewiesen, öffentlich nun auch in meinem Buch «Von Seelenrätseln»: Es ist eine gangbare natur­wissenschaftliche Vorstellung heute, daß man im Nervensystem - blei­ben wir zunächst beim Menschen, aber in ähnlicher Weise, nur in ähn­licher Weise ist das auch beim Tiere gültig -, daß man im Nervensystem unterscheidet zwischen sogenannten sensitiven Nerven, Sinnesnerven, Wahrnehmungsnerven und motorischen Nerven.",
        "Schematisch kann das nur so dargestellt werden, daß zum Beispiel irgendein Nerv, sagen wir ein Tastnerv, die Tastempfindung hineinträgt bis zum Zentralorgan, sagen wir bis zum Rückenmark (gelb), da mündet dasjenige, was da aus der Peripherie des Leibes geleitet wird, in einem Horn des Rücken­marks.",
        "Und dann geht von einem andern Horn, Vorderhorn, der so­genannte motorische Nerv aus, da wird wiederum weitergeleitet der Willensimpuls (siehe Zeichnung S. 12)."
      ],
      [
        "Beim Gehirn ist das nur komplizierter dargestellt, so etwa, wie wenn die Nerven eine Art Telegraphendrähte wären.",
        "Der Sinneseindruck,"
      ],
      [
        "# Bild s. 12"
      ],
      [
        "der Hauteindruck wird bis zum Zentralorgan geleitet, dort wird ge­wissermaßen der Befehl erteilt, daß eine Bewegung ausgeführt werden soll.",
        "Eine Fliege setzt sich irgendwo auf einen Körperteil, das macht einen Eindruck, das wird geleitet bis zum Zentralorgan; dort wird der Befehl gegeben, die Hand bis zu der Stirne zu erheben und die Fliege wird weggejagt.",
        "Es ist eine, schematisch angedeutet, sehr gangbare Vorstellung.",
        "Künftigen Zeiten wird diese Vorstellung außerordentlich komisch erscheinen, denn sie ist ja nur komisch für denjenigen, der die Tatsache durchschaut.",
        "Aber es ist eine Vorstellung, von der heute ein großer Teil der fachmännischen und fachmännischesten Wissenschaft beherrscht ist.",
        "Sie können das nächstbeste Elementarbuch, das Sie über solche Dinge unterrichtet, aufschlagen, und Sie werden finden, man habe zu unterscheiden zwischen Sinneswahrnehmungsnerven und mo­torischen Nerven.",
        "Und man wird besonders das urkomische Bild von den Telegraphenleitungen - wie der Eindruck bis zum Zentralorgan geleitet und dort der Befehl gegeben wird, daß die Bewegung entstehe -gerade in populären Werken heute noch immer sehr verbreitet finden können."
      ],
      [
        "Die Wirklichkeit ist allerdings schwieriger zu durchschauen, als die an die primitivsten Vorstellungen erinnernden Vergleichsvorstellungen von den Telegraphendrähten.",
        "Die Wirklichkeit kann nur durchschaut werden, wenn sie eben mit Geisteswissenschaft durchschaut wird.",
        "Daß ein Willensimpuls erfolgt, hat mit einem solchen Vorgange, den man in kindischer Weise so ausdrückt, als ob da irgendwo in einem materiellen"
      ],
      [
        "Zentralorgan ein Befehl erteilt würde, wirklich gar nichts zu tun.",
        "Die Nerven sind nur da, um einer einheitlichen Funktion zu dienen, sowohl diejenigen Nerven, die man heute sensitive Nerven nennt, wie auch diejenigen, die man motorische Nerven nennt.",
        "Und ob nun im Rücken­mark oder im Gehirn der Nervenstrang durchbrochen ist, beides weist auf dasselbe hin; im Gehirn ist er nur in komplizierterer Weise durch­brochen."
      ],
      [
        "Diese Durchbrechung ist nicht deshalb da, damit durch die eine Hälfte, wenn ich so sagen darf, von der Außenwelt etwas zum Zentral­organ geleitet wird und dann, nachdem sie vom Zentralorgan durch die andere Hälfte in einen Willen umgewandelt worden ist, weiter­geleitet würde.",
        "Diese Unterbrechung ist aus einem ganz andern Grunde da."
      ],
      [
        "Daß unser Nervensystem so gebaut und in dieser regelmäßigen Weise durchbrochen ist, hat seinen Grund darin: An der Stelle, wo unsere Nerven durchbrochen sind, da liegt im Abbilde im Menschen -allerdings nur im körperlichen Abbilde einer komplizierten geistigen Wirklichkeit - die Grenze zwischen physischem und geistigem Er­fahren, physischem und geistigem Erleben.",
        "Sie ist allerdings im Men­schen auf eine merkwürdige Weise enthalten."
      ],
      [
        "Sie ist so enthalten, daß der Mensch mit der ihm zunächstliegenden physischen Welt in eine solche Beziehung tritt, daß mit dieser Beziehung der Teil des Nerven-stranges, der bis zu jener Unterbrechung geht, etwas zu tun hat.",
        "Aber der Mensch muß auch als seelisches Wesen eine Beziehung haben zu seinem eigenen physischen Leib."
      ],
      [
        "Diese Beziehung, die er zu seinem eigenen physischen Leib hat, ist durch den andern Teil vermittelt.",
        "Wenn ich eine Hand bewege, dadurch veranlaßt, daß ein äußerer Sinnesein­druck auf mich gemacht worden ist, dann liegt der Impuls, daß diese Hand bewegt wird, vereinigt von der Seele mit dem Sinneseindruck, schematisch dargestellt, schon bereits hier (siehe Zeichnung, a)."
      ],
      [
        "Und dasjenige, was geleitet wird, wird auf den ganzen sensitiven Nerven und den sogenannten motorischen Nerven entlang geleitet von a bis zu b.",
        "Das ist nicht so, daß der Sinneseindruck erst bis zu c geht und dann von da aus einen Befehl gibt, damit b dazu veranlaßt werde - nein, wenn ein Willensimpuls stattfindet, lebt das Seelische schon befruchtet bei a und geht durch den ganzen unterbrochenen Nervenweg durch."
      ],
      [
        "Es ist keine Rede davon, daß solche kindischen Vorstellungen, als ob die Seele da irgendwo säße zwischen den sensitiven und motorischen Nerven und wie ein Telegraphist die Eindrücke der Außenwelt emp­fangen und dann Befehle aussenden würde, es ist keine Rede davon, daß diese kindischen Vorstellungen irgendeiner auch wie immer ge­arteten Wirklichkeit entsprechen würden.",
        "Diese kindische Vorstellung, die wir immer hören, nimmt sich recht sonderbar komisch aus neben der Forderung, man soll ja in der Naturwissenschaft nicht anthropo­morphistisch sein!",
        "Da fordern nun die Leute, man solle ja nicht anthro­pomorphistisch sein und merken nicht, wie anthropomorphistisch sie sind, wenn sie Worte gebrauchen wie: Ein Eindruck wird empfangen, ein Befehl wird ausgegeben und so weiter. - Sie reden darauf los, ohne auch nur eine Ahnung davon zu haben, was sie alles für mythologische Wesen - wenn sie die Worte ernst nehmen würden - hineinträumen in den menschlichen Organismus."
      ],
      [
        "Nun entsteht aber die Frage: Warum ist der Nervenstrang unter­brochen? - Er ist unterbrochen aus dem Grunde, weil wir, wenn er nicht unterbrochen wäre, nicht eingeschaltet wären in den ganzen Vor­gang.",
        "Nur dadurch, daß gewissermaßen der Impuls an der Unter­brechungsstelle überspringt - der gleiche Impuls, wenn es ein Willens-impuls ist, geht schon von a aus -, dadurch sind wir selbst drinnen in der Welt, dadurch sind wir bei diesem Impuls dabei.",
        "Würde er einheit­lich sein, würde hier nicht eine Unterbrechung sein, so wäre das ganze ein Naturvorgang, ohne daß wir dabei wären."
      ],
      [
        "Stellen Sie sich denselben Vorgang, den Sie bei einer sogenannten Reflexbewegung haben, vor: Eine Fliege setzt sich Ihnen irgendwo hin, der ganze Vorgang kommt Ihnen gar nicht voll zum Bewußtsein, aber Sie wehren die Fliege ab.",
        "Dieser ganze Vorgang hat sein Analogon, sein ganz gerechtfertigtes Analogon auf physikalischem Gebiete.",
        "Inso­fern dieser Vorgang physikalische Erklärung herausfordert, muß diese Erklärung nur etwas komplizierter sein als ein anderer physikalischer Vorgang.",
        "Nehmen Sie an, Sie haben hier einen Kautschukball, Sie stoßen hinein, Sie deformieren den Kautschukball: das geht wieder heraus, richtet sich wieder her.",
        "Sie stoßen nochmals hinein; er stößt wieder heraus.",
        "Das ist der einfache physikalische Vorgang: eine Reflexbewegung."
      ],
      [
        "# Bild s. 15"
      ],
      [
        "Nur ist kein Wahrnehmungsorgan eingeschaltet, nichts Geistiges ist eingeschaltet.",
        "Schalten Sie hier etwas Geistiges ein (innerer Kreis) und unterbrechen Sie hier (Zentrum), dann fühlt sich die Kaut­schukkugel als ein Eigenwesen.",
        "Die Kautschukkugel müßte dann aller­dings, um sowohl die Welt wie sich zu empfinden, ein Nervensystem einschalten.",
        "Aber das Nervensystem ist immer da, um die Welt in sich zu empfinden, niemals irgendwie da, um auf der einen Seite des Drahtes eine Sensation zu leiten und auf der andern Seite des Drahtes einen motorischen Impuls zu leiten."
      ],
      [
        "Ich deute dieses an aus dem Grunde, weil dies, wenn es weiter ver­folgt wird, auf einen der zahlreichen Punkte hinführt, wo Naturwissen­schaft korrigiert werden muß, wenn sie zu Vorstellungen führen soll, die einigermaßen der Wirklichkeit gewachsen sind.",
        "Die Vorstellungen, die heute herrschen, sind eben weiter nichts als solche Vorstellungen, die den Impulsen der Geister der Finsternis dienen.",
        "Im Menschen selber ist die Grenze zwischen dem physischen Erleben und dem geistigen Erleben."
      ],
      [
        "Dieses Stück des Nervs, das ich rot bezeichnet habe, dient im wesentlichen dazu, um uns hineinzustellen in die physische Welt, um uns Empfindung zu vermitteln innerhalb der physischen Welt.",
        "Das andere Stück des Nervs, das ich blau bezeichnet habe, dient im we­sentlichen dazu, um uns selbst uns empfinden zu lassen als Leib.",
        "Und es ist kein wesentlicher Unterschied, ob wir eine Farbe außen bewußt"
      ],
      [
        "erleben durch den Strang a-c, oder ob wir innerlich ein Organ oder eine Organlage oder dergleichen erleben durch den Strang d-b; das ist im wesentlichen dasselbe.",
        "Das eine Mal erleben wir ein Physisches, das nicht in uns zu sein scheint, das andere Mal erleben wir ein Physisches, das in uns ist, das heißt innerhalb unserer Haut.",
        "Dadurch aber sind wir eingeschaltet, daß wir bei einem Willensvorgang alles das erleben kön­nen, was nicht nur außen ist, sondern auch was innerlich an uns ist.",
        "Aber die Stärke der Wahrnehmung ist verschieden vermittelt durch den Strang a-c und durch den Strang d-b.",
        "Dasjenige, was eintritt, ist allerdings eine wesentliche Abschwächung der Intensität.",
        "Wenn wir eine Vorstellung mit einem Willensimpuls zusammen formen in a, so wird dieser Impuls von a aus weitergeleitet.",
        "Indem er von c auf d über­springt, schwächt sich das Ganze so ab für unser Bewußtsein, für unser bewußtes Erleben, daß wir das weitere, was wir nun in uns erleben, die Hebung der Hand und so weiter, nur mit der geringen Intensität des Bewußtseins erleben, die wir sonst auch im Schlafe haben.",
        "Wir sehen das Wollen erst wiederum, wenn die Hand sich bewegt, wenn wir wieder von einer andern Seite her eine Sensation haben."
      ],
      [
        "Der Schlaf dehnt sich in der Tat anatomisch, physiologisch in das wache Leben fortwährend hinein.",
        "Wir stehen mit der äußeren physi­schen Welt in Verbindung und wachen eigentlich immer nur mit dem­jenigen Teil unseres Wesens, welcher bis zu der Unterbrechung der Nerven geht.",
        "Was jenseits der Unterbrechung der Nerven in uns selber liegt, das verschlafen wir auch am Tage.",
        "Das ist aber ein Vorgang, der noch nicht physisch ist in der jetzigen Phase der Erdenentwickelung, sondern noch in einer gewissen geistigen Höhe vor sich geht, wenn das auch vielfach zu tun hat mit den niederen Eigenschaften der Menschen-natur.",
        "Aber ich habe hier schon öfter von dem Geheimnis gesprochen, daß, was im Menschen niedere Natur ist, gerade zusammenhängt mit den höheren Außerungen gewisser geistiger Wesenheiten."
      ],
      [
        "Würde man im Menschen alle diejenigen Stellen sammeln, wo Ner­venunterbrechungen sind, und würde man das aufzeichnen, dann würde man zeichnungsgemäß die Grenze bekommen zwischen dem Erleben in der physischen Welt und dem Erleben aus einer höheren Welt heraus.",
        "Daher kann ich auch folgendes Schema gebrauchen.",
        "Nehmen Sie einmal"
      ],
      [
        "# Bild s. 17"
      ],
      [
        "an - ich zeichne hier alle Nervenunterbrechungen schematisch auf -, nehmen Sie an, da wäre der Kopf und da wäre ein Bein.",
        "Nun nehmen wir an, von hier aus ginge ein sogenannter Eindruck, und hier wäre die Nervenunterbrechungsstelle «Gehen» erfolgt.",
        "Was real ist, ist dann dieses: hier ist alles dasjenige, was der Mensch durch den Nerv erlebt, wachend bei Tag erlebt; hier ist das, was der Mensch erlebt als einen unterbewußten Willen, auch im Wachen schlafend erlebt.",
        "Und alles dasjenige, was nun unter der Nervenunterbrechungsstelle liegt, wird von der geistigen Welt heraus direkt gebildet, geschaffen."
      ],
      [
        "Die Vorstellungen werden Ihnen, wenn Sie sie das erste Mal hören, vielleicht etwas schwierig sein.",
        "Allein sie sollen in Ihnen auch die Vor­stellung hervorrufen, daß man ohne gewisse Schwierigkeiten in die intimeren Dinge der Erkenntnis des Menschen doch nicht hineinkom­men kann."
      ],
      [
        "Wenn Sie das so ansehen, daß hier (rot) alles dasjenige ist, was den Menschen mit der physischen Welt verbindet, unter dieser Grenze alles dasjenige, was den Menschen mit einer geistigen Welt verbindet, die nur heute ein untergeordnetes physisches Abbild hat in ihm - wenn Sie dies ins Auge fassen, dann können Sie eine andere Vorstellung damit verbinden.",
        "Diese andere Vorstellung, die Sie damit verbinden sollen, ist die folgende: Denken Sie sich einmal die Pflanzenwelt.",
        "Die Pflanzen wachsen aus der Erde heraus; aber sie würden nicht aus der Erde her-auswachsen, wenn sie nicht aus dem Kosmos herein Kräfte empfingen, Kräfte, die mit dem Sonnenleben innig zusammenhängen, welche alles das in Empfang nehmen, was von der Erde heraus gekraftet wird.",
        "Lesen Sie, um das besser zu verstehen, noch einmal die Abhandlung über «Das menschliche Leben vom Standpunkte der Geisteswissenschaft».",
        "Zum Leben der Pflanzenwelt gehört dieses ganze Kosmische, das von dem Kosmos herein vom Sonnenleben kommt, zusammen mit dem, was von der Erde herauf kommt."
      ],
      [
        "# Bild s. 18"
      ],
      [
        "Dieses Zusammenwirken aber des Kosmischen mit demjenigen, was tellurisch, was irdisch ist, das gehört überhaupt zum Leben, zum Dasein innerhalb der physischen Welt, so wie wir sie aufzufassen haben.",
        "Und dieselben Kräfte, die unter diesem Strich (siehe Zeichnung) aus der Erde heraus auf die Pflanze wirken, zusammen mit der Samenkraft der Pflanze - der Same wird ja auch in die Erde hineingetan -, diese selbe"
      ],
      [
        "Masse von Kräften derselben Art, die müssen Sie hier suchen, hier, wo die roten Striche sind.",
        "Diesseits der Grenze, die ich schematisch ange­deutet habe, müssen Sie meinetwillen die Kräfte suchen, die Sie sonst durch die Wurzeln von der Erde kommend für die Pflanzen suchen."
      ],
      [
        "Der Mensch nimmt durch seine Augen, durch seine Ohren, nament­lich durch seine Haut, von der Erde in verfeinerter Art dasjenige auf, was die Pflanze durch ihre Wurzeln aus dem Boden der Erde aufsaugt.",
        "Die Pflanze ist ein Erdenwesen durch ihre Wurzeln.",
        "Der Mensch ist ein Erdenwesen durch seine Nerven und durch dasjenige, was er als das Irdische, das Tellurische aufnimmt durch seine Lungen, durch seine Nahrung, die er von der Erde hereinbekommt.",
        "Alles das, was für die Pflanze von der Erde kommt - nur daß die Pflanze die Wurzeln in die Erde hineinversenkt -, nimmt der Mensch auf durch seine Organe, nur daß er das in verfeinerter Weise aufnimmt, die Pflanze gröber durch die Wurzeln."
      ],
      [
        "Aber die Pflanze nimmt noch andere Kräfte auf.",
        "Die Pflanze nimmt die Kräfte auf, welche ihr aus dem Sonnenreiche, aus dem himmlischen Reiche - räumlich-himmlischen Reiche -, aus dem Kosmos zukommen.",
        "Dieses Gebiet habe ich blau schraffiert: das sind die Kräfte, welche die Pflanze aus dem Kosmos aufnimmt.",
        "Diese Kräfte sind von derselben Art, wie die blau schraffierten Kräfte jenseits der Grenze, die ich an­gegeben habe.",
        "Der Mensch zieht aus seinem Leibe heraus das, was die Pflanze aus dem Kosmos hereinzieht.",
        "Von der Erde zieht der Mensch verfeinert diejenigen Kräfte und Substanzen, welche die Pflanze durch ihre Wurzeln vergröbert aus dem Boden zieht.",
        "Aus seinem Leibe heraus zieht der Mensch dieselben Kräfte und Substanzen vergröbert, welche die Pflanze verfeinert aus dem Kosmos zieht.",
        "Denn so, wie er sie heute aus dem eigenen Leibe herauszieht, so sind sie nicht als Kräfte unmittel­bar gegenwärtig im Kosmos vorhanden, sondern sie sind so vorhanden gewesen während der alten Mondenzeit.",
        "Von dieser hat sie der Mensch bewahrt.",
        "Der Mensch nimmt durch das, was jenseits dieser Grenze im hier gezeichneten blauen Teile enthalten ist, nicht unmittelbar aus der Gegenwart wahr, sondern aus dem, was er durch die Vererbschaft der alten Mondenzeit bewahrt hat.",
        "Er hat das Kosmische einer alten Zeit in die Gegenwart hereingetragen.",
        "In seinem Leib hat der Mensch die"
      ],
      [
        "Mondenverhältnisse aufbewahrt.",
        "Und so sehen Sie, daß wir in einer gewissen Weise kosmisch sind; sogar so mit dem Kosmos zusammen­hängen, daß wir in uns tragen ein Abbild desjenigen, was der Kosmos draußen schon überwunden hat."
      ],
      [
        "Wiederum ein Beispiel für das, was ich das letzte Mal hier ange­schlagen habe: daß nichts dienlich sein wird, wenn man nur so vom allgemeinen, verschwommenen, nebelnden Standpunkte aus davon redet, daß der Mensch wiederum ein kosmisches Empfinden oder kos­mische Vorstellungen in sich aufnehmen müsse.",
        "Diese Dinge haben nur Wert, wenn sie völlig konkret an den Menschen herantreten, wenn wirklich gewußt wird, wie die Dinge liegen, wie sich die Dinge ver­halten.",
        "Dadurch wird dasjenige, was heute nur ein Probieren ist, eben auf eine gesunde, wirkliche gesunde Grundlage gestellt.",
        "Und wenn man weiß, wie alles das, was jenseits der Nervenunterbrechungen im Innern des menschlichen Leibes liegt, mit dem mondartigen Wesen zusammen­hängt, dann wird man herausfinden können aus den Verwandtschaften heraus, welche krankmachenden oder heilenden Kräfte im Kosmos und im Erdenleben zu finden sind.",
        "Und wenn man wissen wird, in welcher Weise das, was diesseits der Grenze liegt, so zusammenhängt mit den Erdenverhältnissen, nur im verfeinerten Sinne, wie die Pflanze durch ihre Bodenverhältnisse mit den Wurzeln zusammenhängt, dann wird man die Beziehung zwischen Krankheit und Gesundheit und zwischen dem Wesen gewisser Pflanzen wirklich in bewußter Art auffinden können."
      ],
      [
        "Heute sind die Dinge ein Probieren.",
        "Auf gesunde Grundlage muß zuerst das menschliche Erkennen gestellt werden, und dann wird auf gesunde Grundlage auch gestellt werden können, was der Mensch an Begriffen und Vorstellungen entwickelt, um das soziale, das sittliche, das pädagogische, das politische Leben irgendwie mit seinen eigenen Vorstellungen zu regeln, durchdringen zu können, ihm eine Struktur verleihen zu können."
      ],
      [
        "Wir machen auf vielen Gebieten die Wahrnehmung, daß gerade die­jenigen, die naturwissenschaftlich groß, fachmännisch gediegen denken, ganz gräßlich zu fabulieren, zu schwätzen anfangen, wenn sie ihre ge­wohnten Vorstellungen übertragen auf das Gebiet des sozialen Lebens."
      ],
      [
        "Aber dieses Gebiet des sozialen Lebens ist ja nicht ein ganz selbstän­diges Gebiet.",
        "Der Mensch steht darinnen mit seiner physischen, see­lischen, geistigen Natur, und man kann die Dinge nicht voneinander trennen.",
        "Und es darf nicht bei der Tatsache bleiben, daß die Mensch­heit auf dem sozialen Gebiet naturwissenschaftlich dumm gemacht wird, damit sie auf dem sozialen Gebiet nur zu schwätzen vermag."
      ],
      [
        "Man kann heute ohne Schwierigkeit leicht nachweisen, wie gedie­gene Naturforscher ins Schwätzen hineinkommen, wenn sie die Grenze zwischen Naturwissenschaft und dem geistigen Leben überschreiten.",
        "Besonders Mediziner sind auf diesem Gebiet außerordentlich produk­tiv im Hervorbringen von allerlei Geschwätz, wenn es sich darum han­delt, mit den Vorstellungen, die auf naturwissenschaftlichem Gebiete heute gewonnen werden, ins geistige Gebiet herüberzugehen.",
        "Man braucht nur irgend etwas herauszugreifen.",
        "Greift nur hinein ins volle Menschenleben - wo ihr es nur anfaßt, ist es in dieser Beziehung heute konfus."
      ],
      [
        "Da habe ich zum Beispiel eine Broschüre: «Die Schädigungen der Nerven und des geistigen Lebens durch den Krieg», von einem ausge­zeichneten Mediziner.",
        "Ich will gar nicht, um Ihr Vorurteil nicht zu erregen, sagen von einem wie ausgezeichneten Mediziner.",
        "Aber dieser ausgezeichnete Mediziner, er betrachtete nun dieses Nervensystem, über das die Naturwissenschaft ja eigentlich nicht einmal einen Schim­mer von einer richtigen Vorstellung hat - nach den paar Andeutungen, die ich heute gegeben habe, können Sie das sehen -, er betrachtete nun dieses Nervensystem, wie es malträtiert wird durch die gegenwärtigen Kriegsverhältnisse.",
        "Ja, man braucht nur an das Allerprimitivste zu denken und man kann darauf hinweisen, wie das wirklich vernünftige Denken aufhört, wenn herübergeleitet werden die naturwissenschaft­lichen Vorstellungen auf das, was mit dem geistigen Gebiete, ich will nur sagen, etwas zu tun hat, gar nicht einmal noch das geistige Gebiet selber ist.",
        "Nicht wahr, wenn man so etwas bespricht wie «Die Schädi­gungen der Nerven und des geistigen Lebens durch den Krieg>, dann hat man die Notwendigkeit vor sich, dasjenige, was angeblich in den Nerven vor sich gehen soll, auszudrücken durch allerlei vom geistigen Leben Entnommenem - natürlich von dem geistigen Leben, das hier"
      ],
      [
        "auf dem physischen Plane verläuft -, durch allerlei Vorstellungen, die diesem geistigen Leben entnommen sind."
      ],
      [
        "Nun gibt zum Beispiel dieser Herr hier die Vorstellung - die unter gewissen Verhältnissen des abnormen Nervenlebens berechtigt sein soll -, die Vorstellung von «überwertigen Ideen».",
        "Uberwertige Ideen sind ein Symptom für kranke Nerven.",
        "Uberwertige Ideen - was ist eine überwertige Idee?",
        "Wenn man einen solchen Begriff aufstellt, dann muß man sich klar sein, daß ein solcher Begriff lebenswirklich sein muß.",
        "Aber was ist eine überwertige Idee?",
        "Eine überwertige Idee ist für jenen Mann etwas, das entsteht, wenn die Empfindungs- und Gefühls­betonung der Idee zu stark ist, wenn sie einseitig ist.",
        "Allerlei so vage Vorstellungen bringt er eben heran.",
        "Ich kann Ihnen natürlich keine bestimmte Vorstellung davon geben.",
        "Schreiben Sie, wenn ich das nicht bestimmt definiere, es nicht der Geisteswissenschaft zu, denn ich muß ja referieren.",
        "Eine überwertige Idee entsteht zum Beispiel, wenn man, durch den Krieg veranlaßt, eine fremde Nation zu viel haßt.",
        "Eine «wertige Idee» ist die richtige Vaterlandsliebe.",
        "Aber diese richtige Vaterlandsliebe wird, wenn das Nervensystem irritiert ist, überwertig.",
        "Man liebt nicht nur sein Vaterland, sondern man haßt die andern Völ­ker: jetzt ist die Idee überwertig geworden.",
        "Die wertige Idee ist gesund, und man muß aus der wertigen Idee schließen, daß auch die Nerven gesund sind.",
        "Wenn aber die Idee überwertig ist, so sind auch die Ner­ven geschädigt."
      ],
      [
        "Trifft man irgendwo die Wirklichkeit, wenn man auf der einen Seite so einen Nervenvorgang charakterisiert, auf der andern Seite eine Idee, die nun eine gewisse Eigenschaft haben soll?",
        "Sie soll überwertig als Idee sein.",
        "Auf der einen Seite ist der Nervenvorgang, auf der andern Seite ist Ideeüberwertiges.",
        "Die Leute würden gut tun, solche Dinge immer zu Ende zu denken, denn ein Gedanke zeigt sich nur dann in seiner Richtigkeit oder Unrichtigkeit beziehungsweise in seiner Wirk­lichkeitsgemäßheit oder Wirklichkeitsungemäßheit, wenn man ihn zu Ende denkt.",
        "Eine überwertige Idee wäre es, wenn ich mir vorstellen würde, ich wäre der König von Spanien.",
        "Nicht wahr, ganz zweifellos wäre das eine überwertige Idee.",
        "Aber jene Idee brauchte durchaus nicht überwertig zu sein, wenn ich es wirklich wäre.",
        "Dann wäre mein Nervensystem"
      ],
      [
        "ganz gesund und ich hätte dieselbe Idee.",
        "Die Idee hat den­selben Inhalt.",
        "Die Idee als solche ist also doch wohl nicht überwertig, denn sonst müßte man den König von Spanien als krank ansehen in seinem Nervensystem, weil er denkt, er wäre der König von Spanien, nicht wahr?",
        "Also auf diesen Zusammenhang kommt es überhaupt gar nicht an.",
        "Dennoch wird herumgeschwätzt über diese Dinge.",
        "Und man redet nicht nur herum, sondern man bildet auch Begriffe, Definitionen aus und so weiter, und man kommt dann zu Merkwürdigem, was nicht mehr ist als Geschwätz."
      ],
      [
        "Denn nun hat der gute Herr diesen Begriff von überwertigen Ideen ausgebildet.",
        "Die Überwertigkeit der Idee ist nun das Symptom für das unrichtige Nervenleben.",
        "Na, schön!",
        "Aber seinem Unterbewußten ist nicht recht wohl dabei, weil er unterbewußt doch fühlt: während er die ganze Sache von der Uberwertigkeit der Ideen den Leuten vorträgt, haben die wiederum allerlei unterbewußte Ideen von dem, daß die Sache doch nicht recht stimmt.",
        "Bei den Zuhörern bleibt die Sache heute selbstverständlich unterbewußt, denn der Herr ist eine Autorität - ver­zeihen Sie! -, da dürfen die Eindrücke nicht ins Bewußtsein dringen.",
        "«Denn mit der Bezeichnung der soll nicht nur die an sich lebhafte hohe Bewertung der betreffenden Vorstellungen, sondern eben auch ihre im Verhältnis zur realen Bedeutung der ihnen wirklich zugrunde liegenden Tatsächlichkeiten ausgedrückt wer­den.",
        "Die überwertige Idee beherrscht das Bewußtsein so sehr, daß neben ihr nicht genügend Platz für andere, objektiv ebenfalls berechtigte Ideen vorhanden ist.",
        "Darum werden letztere verdrängt, verlieren ihre Wirksamkeit im Bewußtsein und ihren Einfluß auf die Beschränkung und Zügelung der überwertigen Vorstellungen.",
        "So entsteht die einseitige Übertreibung in der Urteilsbildung, die einseitige Richtung derWillens­bestrebungen, die Abkehr von allen andern Gedankenkreisen, die mit dem Zentrum der überwertigen Ideen nicht unmittelbar zusammen­hängen.» So wie wenn man sagt: Die Armut kommt von der Pauvreté -so ungefähr ist es!"
      ],
      [
        "«Daher erscheint dem ruhig urteilenden Beobachter das nervös er­regte Bewußtsein stets als etwas Unvernünftiges, als etwas geistig Halt­loses, und es entspricht daher durchaus der Tatsächlichkeit, wenn der"
      ],
      [
        "ruhige Zuschauer den nervös erregten Menschen mit den Worten: , wieder auf die rechte Bahn des Denkens und Urteilens zu bringen versucht.»"
      ],
      [
        "Nun also hat er von der Überwertigkeit der Ideen gesprochen, von ihrem Zusammenhang mit dem Nervensystem.",
        "Aber nun wird ihm etwas schwül im Unterbewußtsein, denn die Geschichte ist ja nur ein Gerede, und es paßt schlecht.",
        "Na, da setzt er denn die Rede fort: «Wir dürfen aber die nicht ohne weiteres jeder überhaupt gefühlsbetonten und ungewöhnlich lebhaften Vorstellungsweise gleich­stellen.",
        "Auch alles Edle und Hohe, was den Menschengeist bewegt und ihn zu großen Taten befähigt, was Hingabe und Begeisterung für eine große Tat und für die Anspannung aller Kräfte zu Erreichung eines großen Zieles erweckt, auch dies entspringt nur aus großen Ideen, die den Geist beherrschen und ihm die Kraft und Ausdauer des Willens geben, ohne die ein zielbewußtes Handeln nicht möglich ist.»"
      ],
      [
        "Überwertige Ideen, sie zerstören das Nervensystem, sind wenigstens ein Symptom dafür; aber alles Hohe und Edle ist eigentlich ebenso.",
        "Es gibt keinen rechten Unterschied.",
        "Aber er muß wenigstens erwähnen, daß die Geschichte eigentlich ebenso ist."
      ],
      [
        "«Überall in der Geschichte des Einzelnen und in der Geschichte der Völker sehen wir die großen Taten vollbracht unter dem Einfluß einer großen leitenden Idee, die ihren Träger unaufhaltsam und auf der gleichen Bahn und in derselben Richtung festhielt und vorwärtstrieb, ihn erst befähigte zu jener unermüdlichen Ausdauer, die trotz Hinder­nissen und Widerständen das einmal erkannte und erstrebte Ziel er­reichen konnte.",
        "Was wäre aus Galilei, aus Richard Wagner, aus Bis­marck und aus vielen andern großen Männern geworden ohne die Schwungkraft einer großen leitenden Idee, die den Geist jahre- und jahrzehntelang trotz aller Kämpfe und Widerstände in eine bestimmte Richtung des Wollens vorwärtstrieb!» - die also «überwertig» war, die ganz ausgesprochen «überwertig» war!"
      ],
      [
        "Da wird manchmal solch ein Anflug von Ehrlichkeit vollzogen.",
        "Es gibt eine naturwissenschaftliche Richtung, die alle Genies zugleich für etwas verrückt erklärt, weil ja auf diesem Boden so ein richtiger Unter­schied zwischen der Genialität und der Verrücktheit ohnedies nicht"
      ],
      [
        "herauszufinden ist.",
        "Und ich habe Ihnen gesagt, daß es heute auch schon Werke gibt, die den Christus Jesus als einen pathologisch Kranken hin­stellen, so daß eigentlich das ganze Christentum der Ausfluß der Tat­sache ist, daß einmal einer in Palästina, der den Namen Jesus geführt hat, nicht recht gescheit war.",
        "Das ist heute Gegenstand von verschie­denen ernst gemeinten, als wissenschaftlich angesehenen Persönlich­keiten."
      ],
      [
        "Die Leerheit solchen Denkens, die tritt manchmal in krasser Art zutage, so wenn der betreffende Herr dann gleich fortfährt: «Aber darin liegt die Tragik des Menschengeistes, daß die Vorstellungen, wel­che mit größter Stärke das Bewußtsein erfüllen, nicht immer die rich­tigen sind» - sehr tief ist hier die Tragik des Menschengeistes erklärt, außerordentlich tief! - «und sich nicht immer einfügen in den geord­neten Zusammenhang der äußeren Welt.»"
      ],
      [
        "Nun haben wir es!",
        "Wie weit ist es von solchen Vorstellungen zu der Erkenntnis, die nur erreicht werden kann auf Grundlage von solchen Betrachtungen, wie wir sie hier anstellen.",
        "Gewiß, es kann in zwei Men­schen dieselbe Vorstellungsmasse anwesend sein, nur ist sie das eine Mal, sagen wir luziferisch, das andere Mal ahrimanisch, das dritte Mal ist sie im Sinne der normalen Menschheitsentwickelung.",
        "Statt das in­haltsleere Wort «überwertige Ideen» zu bilden, muß der Begriff einer Geistigkeit eingeführt werden, wie die luziferische oder ahrimanische Geistigkeit, so daß man weiß: darauf kommt es an, daß man erkennt, ob der Mensch selbst will, oder ob ein anderes in ihm will.",
        "Aber davor schreckt natürlich solche angebliche Wissenschaft heute noch zurück."
      ],
      [
        "Sehr nett werden dann die Dinge, wenn man erwarten will, daß nun wirklich etwas Substantielles vorgebracht wird: «Da nenne ich zu­nächst» - er will zunächst das angeben, wodurch sich gewisse nervöse Störungen beim Menschen ankündigen -, «da nenne ich zunächst die­selben Vorstellungen, welche auch bei der Nervosität des einzelnen oft die größte Rolle spielen:» - er meint, beim heutigen Völkerwahn eben auch - «die Vorstellungen der Verzagtheit, der Sorge, des Kleinmuts, der Mutlosigkeit, des mangelnden Selbstvertrauens.»"
      ],
      [
        "Das sind also diejenigen Dinge, welche das gestörte Nervensystem charakterisieren beim nervösen Leben, das unter überwertigen Ideen"
      ],
      [
        "steht.",
        "Verzagtheit, Sorge, Kleinmut, Mutlosigkeit, mangelndes Selbst­vertrauen.",
        "Nicht wahr, solch ein Vortrag ist doch Mittel dazu, daß er irgendwie nützlich sein könnte.",
        "Denn um bloß die Luftwellen zu er­regen, wird wahrscheinlich die betreffende Autorität nicht sprechen, sondern um irgendwie nützlich zu sein.",
        "Man sollte also erwarten, daß der betreffende Herr nun sagt, wie die Menschheit darüber hinaus-kommt, da er wie beim einzelnen Menschen, so auch in der Menschheit findet, daß heute Mutlosigkeit, Verzagtheit, Sorge, mangelndes Selbst­vertrauen Symptome sind für die Nervenstörung.",
        "Man sollte glauben, daß er nun sagt, wie diese Geschichten zu beheben sind, wie man über diese Mutlosigkeit, Sorge, Verzagtheit, mangelndes Selbstvertrauen hin-auskommt.",
        "Man sollte das voraussetzen.",
        "Er setzt es eigentlich auch voraus.",
        "Er sagt daher: «Und so kann, wenigstens zeitweise, in großen Volksschichten jene mutlose unzufriedene Stimmung einreißen, die wir mehr zu fürchten haben als alles andere.",
        "Denn sie führt zum Nach­lassen kräftiger Willensregungen, zur Lockerung der festen einheit­lichen Zielstrebigkeit, zur Schwächung der Energie und Ausdauer.»"
      ],
      [
        "Nun erwartet man also etwas, nicht wahr?",
        "Da sagt er: «Nicht ner­vös werden heißt daher in erster Linie Mut, Zuversicht und Vertrauen auf die eigene Kraft und das als richtig erkannte Handeln nicht ver­lieren.»"
      ],
      [
        "Na, schön, jetzt haben wir es.",
        "Man ist nervös, wenn man die Sorge, Mutlosigkeit, Verzagtheit, mangelndes Selbstvertrauen hat.",
        "Wie kriegt man es weg?",
        "Wenn man es nicht hat!",
        "Es ist ganz klar, nicht wahr, wenn man es nicht hat!"
      ],
      [
        "Diese Nichtigkeit des Denkens überträgt sich auf das Substantielle auch in der Wissenschaft, und solche Autoritäten haben alles Material zur Verfügung, haben alles Material okkupiert, es konfisziert, wenn irgendwie versucht werden soll, mit Vernunft das Material zu bear­beiten - aber indem sie das Material bearbeiten, bearbeiten sie es mit nichtigen Gedanken.",
        "Das anatomische, physiologische, physikalische Material geht verloren.",
        "Nichts wird geschaffen, weil an demjenigen Tisch, wo das Nützliche für die Menschheit geschaffen werden soll, Leute stehen mit solchen Nichtigkeitsgedanken!",
        "Selbstverständlich kann bei der Sektion einer Leiche nichts herauskommen, wenn - verzeihen"
      ],
      [
        "Sie den harten Gedanken - ein Hohlkopf seziert.",
        "Hier werden die Dinge schon sozial.",
        "Von diesem Gesichtspunkte aus müssen schon die Dinge angesehen werden.",
        "Und eine so vielversprechende Abhand­lung, die einen Vortrag wiedergibt, endet auf solche Weise!"
      ],
      [
        "Ich habe Ihnen das eine Beispiel angeführt: Nicht nervös werden heißt daher in erster Linie Mut, Zuversicht und Vertrauen nicht ver­lieren.",
        "Aber wenn heute der Durchschnittsleser solch eine Abhandlung in die Hand nimmt und liest: «Die Schädigungen der Nerven und des geistigen Lebens durch den Krieg», denkt er: Da kann ich aufgeklärt werden, denn das ist von Professor Dr.",
        "Soundso, Direktor der medi­zinischen Klinik in Soundso. - Nun ja, da ist er sich also klar darüber: jetzt wird er natürlich aufgeklärt."
      ],
      [
        "Doch da steht zum Beispiel auf Seite 27, wo der Völkerhaß bespro­chen wird: «Aber freilich auch in uns selbst loderten ähnliche Erregun­gen auf, und wir empfanden es fast als eine erleichternde Genugtuung, nun auch unsererseits unserem Hauptfeinde mit ähnlichen Gesinnungen gegenüberzutreten.",
        "Und doch bedarf es nur geringer ruhiger Über­legung, um zu erkennen, daß dieser allgemeine Völkerhaß nur der Aus­fluß einer krankhaften, überreizten Seelenstimmung ist, in welche die Volksmassen durch gegenseitige Anfeuerung, Aufhetzung und Nach­ahmung geraten sind.»"
      ],
      [
        "Nun, wie ist also nach diesem Satz die Geschichte mit dem Völker-haß eigentlich gekommen?",
        "Da sind Volker: A, B, C; eigentlich ist weder A noch B noch C irgendwie geeignet, von sich aus zu hassen, denn davon ist ja die ganze Geschichte nicht gekommen, sondern ge­kommen ist dieser allgemeine Völkerhaß durch eine krankhaft über­reizte Seelenstimmung, in welche die Völkermassen durch gegenseitige Anfeuerung, Aufhetzung und Nachahmung geraten sind.",
        "Also der A kann es nicht; der B auch nicht; der C kann es auch nicht machen; aber was jeder nicht machen kann, dazu reizen sie sich nun gegenseitig auf.",
        "Denken Sie sich, wie scharfsinnig der Gedanke ist!",
        "Ich erkläre etwas, ich habe vor mir A, B, C; das alles ist nicht geeignet zur Erklärung -aber sie machen es doch.",
        "Ich erkläre also etwas aus dem Nichts heraus auf die schönste Weise.",
        "Diese Dinge nehmen die Menschen in die Hand, lesen sie, werden nicht aufmerksam, daß das ein bloßer Unsinn ist."
      ],
      [
        "Es ist schon nötig, auf solche Dinge hinzuweisen, denn sie zeigen, wie verrenkt, wie nichtig das Denken ist, das heute die Autorität in Anspruch nimmt.",
        "Natürlich, in der Wissenschaft, die sich auf das schon Vorhandene bezieht, da tritt das nicht so stark zutage, denn da kann man die Geschichte nicht kontrollieren.",
        "Aber so wie die Leute da in der Wissenschaft denken, so denken sie auch im sozialen, im pädagogischen, im politischen Leben.",
        "Und so hat sich das seit vier Jahrhunderten vor­bereitet.",
        "So ist die Sache.",
        "Und so ist es gekommen, daß aus dem ver­renkten, nichtigen Denken eben allmählich jene Impulse geworden sind, welche wir in den heutigen katastrophalen Ereignissen uns ent­gegentreten fühlen.",
        "Da muß man schon in das Tiefere der Sache eben durchaus hineinsehen.",
        "Und erst wenn die Menschen dann an die Ober­fläche der Dinge kommen, da wo, ich möchte sagen, die Sache unmittel­bar aktuell für den einzelnen Menschen wird und auch für die soziale Struktur ganzer Völker es werden kann, da wird die Sache ganz be­sonders gräßlich traurig!"
      ],
      [
        "Nicht wahr, man hat die Aufgabe, auf der einen Seite die Dinge zu begreifen; man muß sie in ihrer gegenseitigen Abgegrenztheit kennen­lernen,wenn man sie verstehen will.",
        "Will man ein solches Ereignis selbst wie den gegenwärtigen Krieg, das so kompliziert ist und heute eben wirklich in seinen Einzelheiten selbstverständlich nicht erfaßt werden kann vom physischen Plane aus, verstehen, muß man ihn, wie man sagt, auf seine Ursachen zurückführen und so weiter.",
        "Aber jeder glaubt daran: wenn er eine Sache auf seine Ursache zurückgeführt hat, wenn er sie in einer solchen Weise verstanden hat, so sei sie auch notwendig, hätte so geschehen müssen, wie sie da ist.",
        "Heute zum Beispiel merkt man nicht einmal im geringsten, daß das eine mit dem andern gar nichts zu tun hat.",
        "Dadurch daß man eine Sache in ihren Zusammen­hängen erkennt, ist nicht etwa festgestellt, daß das Ereignis hat ein­treten müssen, wie man sagt, daß es nicht hätte unterbleiben können.",
        "Derjenige, der versucht, sich in einer mehr oder weniger gescheiten Weise klarzumachen, warum der gegenwärtige Krieg hat kommen müssen, warum er nicht etwas ist, was ein paar Leute beschlossen haben, sondern was schon mit tieferen Ursachen in der Menschheitsentwicke­lung zusammenhängt, der geht dann oftmals befriedigt von dannen"
      ],
      [
        "und sagt: Also habe ich begriffen, daß es gar nicht anders möglich war, als daß dieser Krieg hat kommen müssen! - Er ist selbstverständlich eine Notwendigkeit in dem Sinne, daß, wenn man seine Ursachen kennt, er aus diesen Ursachen, aus diesen konkreten Bedingungen mit aller Notwendigkeit sich entwickelt hat.",
        "Aber das besagt nicht, daß man daraus den Schluß ziehen darf: die Sache hat unmittelbar so kom­men müssen, wie sie gekommen ist.",
        "Kein Ereignis, das in der Welt­geschichte auftritt, ist in diesem letzteren Sinne notwendig, obzwar es im ersteren Sinne notwendig ist - kein Ereignis ist in diesem letzteren Sinne notwendig.",
        "Jedes könnte anders sein; und jedes könnte auch nicht sein!"
      ],
      [
        "Und derjenige, der dann von der absoluten Notwendigkeit spricht, der könnte mit demselben Rechte sich überlegen: Ich möchte gerne wissen, wann ich sterben werde.",
        "Ich gehe also zu einer Versicherungs­gesellschaft; die Leute rechnen aus, danach bestimmen sie die Versiche­rungspolicenhöhe: wieviel von einer gewissen Anzahl von Menschen nach einer gewissen Zeit gestorben sind und wie viele noch lebend sind.",
        "Danach werden die Quoten ausgezahlt.",
        "Ich gehe also einmal, erkundige mich bei einer Versicherungsgesellschaft; nach deren Ausrechnungen muß es sich ergeben, ob ich nun 1920 schon gestorben sein werde."
      ],
      [
        "Das ist natürlich ein absoluter Unsinn.",
        "Aber derselbe Unsinn ist es, wenn man die Notwendigkeit eines Geschehens herleiten will aus dem andern, dem Begreifen der Ursache, die zu diesem Geschehen führen muß.",
        "Und hiermit schlage ich ein Thema an, das allerdings nicht leicht ist, aus dem Grunde, weil gerade auf diesem Gebiete die allerverrenk­testen Ideen herrschen, weil auf diesem Gebiete auch heute noch nicht sehr viel Wille besteht, sich über die Dinge klarzuwerden."
      ],
      [
        "Die Sache ist diese: Man muß, wenn man sich gerade über die Frage klarwerden will, die hiermit angeschlagen ist, ins Auge fassen, daß, wenn irgend etwas eintritt, dieses unter dem Einfluß von gewissen Be­dingungen eintritt.",
        "Man kommt in der Reihe der Bedingungen immer zu einem Punkte, wo in der Welt Anfänge, richtige Anfänge sind.",
        "Wenn Sie heute ein Bäumchen sehen, das noch klein ist, so wissen Sie: in spä­terer Zeit wird es größer sein.",
        "Mit Notwendigkeit entwickelt sich die Größe des Bäumchens aus seiner Kleinheit heraus.",
        "Und Sie können"
      ],
      [
        "nach einiger Zeit sagen: Es ist eine Notwendigkeit, daß dieses Bäum­chen sich so entwickelt hat; ich konnte sehen, wie es sich mit Notwen­digkeit entwickelte aus einem ganz kleinen heraus, vielleicht als es eben die ersten Triebkräfte aus der Erde hervor entwickelte.",
        "Wenn ich Botaniker bin, kann ich sehen, daß da mit Notwendigkeit ein großer Baum nach einiger Zeit entstehen muß.",
        "Wenn aber das Samenkorn nicht dort an jener Stelle hineingefallen wäre, wie dann?",
        "Vielleicht hat es ein Mensch hineingetan.",
        "Wenn er es nicht getan hätte, dann wäre da ein Punkt, wo die Notwendigkeit nicht eingeleitet worden wäre.",
        "Nun aber muß da die Notwendigkeit beginnen.",
        "Und, sagen wir, Sie haben hier eine mächtige Eiche - sie ist ja nicht in Wirklichkeit da -, Sie schauen sie an und bewundern sie.",
        "Diese Eiche war selbstverständlich einmal ein kleines Bäumchen, sie hat sich mit Notwendigkeit aus einem kleinen Bäumchen entwickelt.",
        "Aber nehmen Sie an, ein nichtsnutziger Bube oder - pardon, um nicht unhöflich zu werden - ein nichtsnutziges Mädchen wäre, als das Bäumchen noch ganz klein war, dahin ge­kommen, wo das kleine Bäumchen stand und hätte es ausgerissen:"
      ],
      [
        "durch dieses Ausreißen hätte sich jene ganze Notwendigkeit nicht er­geben.",
        "Auch in negativer Weise können Sie die Notwendigkeit weg­nehmen."
      ],
      [
        "Anfangspunkte, wo die Notwendigkeiten beginnen, stellen sich dem wirklichkeitsgemäßen Denken ein, das ist das Wesentliche.",
        "Aber zu diesen Anfangspunkten kommt man nicht, wenn man nur den äußeren Verlauf der Tatsachen betrachtet.",
        "Man kommt nur zu ihnen, wenn man die geistige Grundlage wenigstens erfühlen kann.",
        "Denn geradeso wie Sie hier einen Rosenstrauß haben und wie der, wenn Sie ihn vorstellen, für den Abstraktling eine Vorstellung gibt, welche Wirklichkeit ab-bildet - denn der Rosenstrauß ist ihm wirklich, und seine Vorstellung bildet Wirklichkeit ab -, für den Okkultisten ist der Rosenstrauß, wenn er ihn vorstellt, gar nichts Wirkliches, weil der Rosenstrauß nicht exi­stiert; die Rosen können nur existieren, wenn sie mit der Wurzel zu­sammen in dem Erdboden sind und so weiter.",
        "Die wirklicheVorstellung ist nicht gegeben, wenn man von vornherein etwas Außerliches nach-bildet, sondern wenn man aus der Wirklichkeit heraus diese erlebte Vorstellung nachgebildet hat.",
        "Diese erlebte Vorstellung ergibt sich aber"
      ],
      [
        "auch gegenüber der äußeren sinnlichen Wirklichkeit nur der geistes­wissenschaftlichen Betrachtung."
      ],
      [
        "Und so ergibt sich auch für ein weltgeschichtliches Ereignis nur dann eine gültige Vorstellung, wenn man geisteswissenschaftlich dieses weltgeschichtliche Ereignis überblicken kann.",
        "Da findet man, daß es in bezug auf seine Notwendigkeit allerdings sich verfolgen läßt."
      ],
      [
        "Man fin­det seine Verästelungen, seine Wurzeln in der Wirklichkeit drinnen.",
        "Aber nur mit diesem konkreten Verfolgen der Wurzeln ist etwas getan, nicht mit der allgemeinen Konstatierung von einer abstrakten Not­wendigkeit."
      ],
      [
        "Wären aber zum Beispiel gewisse Ereignisse in den acht­ziger Jahren des 19.",
        "Jahrhunderts anders gewesen, dann wären die Er­eignisse 1914 auch anders geworden.",
        "Aber darauf kommt es eben an, daß man nicht so wie die Historiker vorgeht: Jetzt geschieht etwas, das die Wirkung zum Vorhergehenden ist, das ist wiederum die Wirkung vom Vorhergehenden, dieses wiederum die Wirkung vom Vorher­gehenden und so weiter."
      ],
      [
        "Da kommt man nicht nur bis zum Anfang der Welt, sondern noch weiter ins völlige Nichts hinunter.",
        "Da kugelt so eine Vorstellung hinter der andern daher.",
        "Darauf kann es nicht an­kommen, sondern auf das konkrete Verfolgen dieser Sache, auf das wirkliche Einwurzeln."
      ],
      [
        "So wie die Pflanzenwurzel irgendwo anfängt, so fangen die Ereignisse auch irgendwo an.",
        "Keime werden gelegt im Laufe der Zeit.",
        "Wenn die Keime nicht gelegt werden, dann entstehen auch die Ereignisse nicht."
      ],
      [
        "Ich schlage damit ein Thema an, das ich selbstverständlich heute nicht erschöpfen kann.",
        "Wir werden am näch­sten Sonntag über dieses Thema, welches ich im wesentlichen dadurch bezeichnen will: Trotz aller Betrachtung der Notwendigkeit ist kein einziges Ereignis absolut notwendig - noch zu sprechen haben."
      ],
      [
        "Es ist wirklich notwendig, daß die Menschheit der Gegenwart auch der Gesinnung nach aus diesem furchtbaren Dogmatischen, das heute die sogenannte Wissenschaft durchzieht, herauskommt, daß die Dinge ernst genommen werden.",
        "Ich will Ihnen ein richtiges Beispiel anführen.",
        "Damit will ich dann die heutigen Betrachtungen abschließen.",
        "Ich habe in Zürich und in Basel versucht, klarzumachen, daß es ein Unsinn ist, die welthistorischen Ereignisse so hintereinander zu betrachten, als ob eines aus dem andern hervorgehe.",
        "Ich habe gesagt, es sei ein Unding,"
      ],
      [
        "wenn ein Ereignis aus dem andern folge, nur 50 eins aus dem andern hervorgehend zu betrachten.",
        "Das sei so, wie wenn ich hier eine Licht­quelle habe, welche zuerst den Gegenstand a beleuchtet, dann den Ge­genstand b beleuchtet, endlich den Gegenstand c beleuchtet.",
        "Da sehe ich in meiner Beobachtung zuerst a, dann b, dann c beleuchtet, wenn ich die Lichtquelle gar nicht wahrnehme.",
        "Jetzt würde ich einen Fehler machen, nicht wahr, wenn ich zuerst a beleuchtet sehe, dann b, und würde sagen, das b wird von a her beleuchtet; und wenn ich dann c beleuchtet sehe und würde sagen, das c wird von b her beleuchtet.",
        "Ich würde etwas ganz Unrichtiges sagen, denn die Beleuchtung von b und c hat gar nichts damit zu tun, sondern es wird von einer gemeinsamen Lichtquelle aus beleuchtet.",
        "Ich habe dieses Beispiel gebraucht, um die historischen Ereignisse zu erläutern."
      ],
      [
        "Nehmen Sie nun an, es würde jemand diesen Begriff, den ich damit gegeben habe, diese Idee nett finden.",
        "Es könnte sein, daß auch einmal ein auf anthroposophischem Boden entwachsener Begriff nett befunden würde.",
        "Es ist sogar in der letzten Zeit hie und da vorgekommen, daß gerade Gegner diese Begriffe genommen haben, um sie ihrerseits nun zu verwenden.",
        "Manche sind sogar Gegner geworden, weil so etwas moniert werden mußte.",
        "Also es könnte einmal sein, daß auch eine auf anthroposophischer Seite vorgebrachte Analogie nicht gerade Blödsinn wäre.",
        "Nehmen wir an, es griffe es jemand auf, aber er brächte es dann vor in einem andern Zusammenhang, als ich es vorgebracht habe; er brächte es dogmatisch vor - nicht wie ich symptomatisch -, mit einer andern Gesinnung, und ich hörte einen Vortrag, in dem er sagte: Es wird ganz falsch die Aufeinanderfolge von Ursache und Wirkung dar­gestellt, wenn man immerfort sagt, Wirkung b ist die Folge von Ur­sache a, Wirkung c die Folge von Ursache b und so weiter; denn damit begeht man denselben Fehler, wie wenn man sagen würde, wenn das a beleuchtet wird, das b beleuchtet wird, das c beleuchtet wird, so ist das b infolge von a beleuchtet und das c infolge von b beleuchtet.",
        "Wenn ich das anhöre und das nicht in demselben Zusammenhang vorgebracht würde wie von mir in Basel und in Zürich, so würde ich dem Mann vielleicht aus seinem Zusammenhange einwenden können: Wenn die Sache aber so ist, daß a, b und c sogenannte nachleuchtende Materien"
      ],
      [
        "sind - es gibt ja solche Materien, man exponiert sie einer Lichtquelle, da fangen sie dann selber an zu leuchten, die Lichtquelle kann entfernt sein -, wenn dann a tatsächlich, weil es nachleuchtet, das b beleuchtet, und b wiederum, weil es nachleuchtet, das c beleuchtet: nun, dann kann die Geschichte so sein, daß das b infolge von a, und das c infolge von b beleuchtet ist.",
        "Also die ganze Analogie könnte eine sehr brüchige sein, wenn sie einer vertritt, der nicht im Verlaufe seines Vortrages vor­gebracht hat, daß Begriffe für die Wirklichkeit im geistigen Leben so sind wie Photographien.",
        "Wenn man von der einen Seite die Photogra­phie aufnimmt, nimmt es sich anders aus, als wenn man von der andern Seite die Photographie aufnimmt.",
        "Wenn man das nicht voraussetzt, wenn man nicht hinführt zu wirklichkeitsgemäßen Begriffen, so daß diese wirklichkeitsgemäßen Begriffe immer perspektivische Begriffe sind, dann kann man unter Umständen mit demselben, was absolut richtig ist, wenn man es perspektivisch meint, einen Unsinn sagen, sobald man es absolut sagt."
      ],
      [
        "Das ist der Unterschied, ob einer von der Wirklichkeit ausgeht, oder ob einer von Begriffen ausgeht.",
        "Wenn einer von Begriffen ausgeht, so wird er immer in eine Einseitigkeit verfallen.",
        "Wenn aber einer von der Wirklichkeit ausgeht, so darf er - weil er nichts anderes kann, als Be­griffe vorbringen, und jeder Begriff ist einseitig -, so darf und muß er einseitige Begriffe vorbringen, denn das ist nur ganz selbstverständlich.",
        "Also Sie sehen, es kommt auf eine vollständige Umänderung des see­lischen Lebens, eine tiefgehende Umänderung des seelischen Lebens an.",
        "Daher ist es natürlich auch gar nicht schwer, zahlreiche Begriffe, die vorgebracht werden von mir, zu kritisieren.",
        "Ich weiß nicht, ob einer auf diese Kritik gerade gekommen wäre, aber ich selber komme schon auf alles dasjenige, was notwendig ist zu kritisieren."
      ],
      [
        "Man muß das Bewußtsein haben, wie sich die Vorstellung zu der Wirklichkeit verhält.",
        "Dann erst hat man die Möglichkeit, in die Wirk­lichkeit einzudringen, sonst streitet man immer über Vorstellungen.",
        "Und die ganze Welt streitet heute über Vorstellungen auf sozialem Ge­biete,wenn auch dieses Streiten eben sich umgesetzt hat in äußere Taten.",
        "Und sehr häufig setzt sich das Streiten über äußere Vorstellungen in äußere Taten um.",
        "Diese Dinge führen schon in große Intimitäten hinein,"
      ],
      [
        "Intimitäten des geistigen Lebens.",
        "Aber man muß sich solche Dinge überlegen, wenn man das Dasein verstehen will."
      ],
      [
        "Nachdem ich Sie heute in mehr theoretischer Weise auf solche Dinge aufmerksam gemacht habe, werde ich das nächste Mal über Zeitge­schichte von diesem Standpunkte sprechen, werde zeigen, inwiefern es notwendig war, daß gewisse Ereignisse gekommen sind; aber inwiefern diese Ereignisse gar nicht notwendig waren, sondern ganz andere Er­eignisse hätten kommen können.",
        "Ereignisse, unter deren katastrophaler Art wir alle leiden, hätten gar nicht zu kommen brauchen.",
        "Diese wich­tige Frage wollen wir dann am nächsten Sonntag weiter besprechen."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG Dornach, 9. Dezember 1917",
    "paragraphs": [
      "Wie ich schon bemerkt habe, werden wir in diesen Tagen Betrachtungen anstellen, die dann morgen oder übermorgen gipfeln werden in einer Auseinandersetzung über geschichtliche Notwendigkeit und Freiheit, gipfeln werden darinnen, daß gezeigt werden soll, in welchem Sinne ein geschichtliches Ereignis notwendig ist, und in welchem Sinne ein geschichtliches Ereignis, überhaupt irgend etwas, das in das Menschen­leben seelisch hereingreift, auch anders sein könnte. Es ist dieses ein Problem, das in der Gegenwart, wo so bedeutungsvolle Ereignisse her-eingreifen in das Menschenleben, von ganz besonders tiefgehender Be­deutung ist. Denn angesichts der traurigen, katastrophalen Ereignisse der Gegenwart muß sich jeder Mensch die Frage stellen: Inwiefern sind solche Ereignisse und ist gerade dieses Ereignis abhängig von einer gewissen Notwendigkeit, und inwiefern hätte es auch ganz anders aus­fallen können, hätte es sich ganz anders gestalten können?",
      "Wie gesagt, wir werden in diesen Tagen darauf hinzielen, uns diese große, umfassende Frage zu beantworten mit den Mitteln, die man gegenwärtig in den öffentlich zu besprechenden okkulten Grundlagen haben kann. Aber wir müssen ausgehen von einer umfassenderen Be­trachtung des menschlichen Lebens. Wir müssen uns etwas vertiefen von einer gewissen Seite her in die menschliche Natur selbst. Das müs­sen wir vorausgehen lassen. Denn, wie Sie vielleicht gerade aus den in der letzten Zeit gehaltenen öffentlichen Vorträgen entnehmen können, in das menschliche Leben spielen fortwährend die Kräfte jener Welt herein, in welcher der Mensch sich befindet zwischen dem Tode und einer neuen Geburt. Viel intensiver, als man denkt, spielen die Kräfte, in die der Mensch als sogenannter Toter eingebettet ist, in das Leben herein. Wir sind - ich habe das letzte Mal, ich möchte sagen, mehr physisch darauf aufmerksam gemacht - als Menschen so geartet, daß im Grunde genommen die Schwelle zwischen der gewöhnlichen phy­sischen Welt und der geistigen Welt mitten durch uns geht. Wenn wir unser gewöhnliches Leben ins Auge fassen und das, was wir das letzte",
      "Mal mehr physisch betrachtet haben, heute mehr seelisch betrachten, so können wir sagen: unser menschliches Leben, wenn wir hier im physischen Leibe verkörpert sind, verläuft so, daß wir erstens alles das in uns wirksam haben, was durch unsere Sinne während unseres Lebens erfahren werden kann, alles das, was sich gewissermaßen als der Sinnes-teppich um uns herum ausbreitet und wovon wir durch unsere Sinne Kunde erhalten. Auf diese Welt baut sich dann alles das auf, was wir aus dieser Sinneswelt herausarbeiten, was wir aber auch unabhängig von dieser Sinneswelt durchdringen können in unserem Vorstellungs­leben. Wenn wir aber Sinnesleben und Vorstellungsleben zusammen­fassen, so haben wir im Grunde schon alles dasjenige, worin wir mit unserem gewöhnlichen wachen Bewußtsein leben.",
      "Von dem Augenblicke an, wo wir morgens aufwachen, bis zu dem Augenblicke, wo wir einschlafen, wachen wir in Wirklichkeit nur voll­ständig in unseren Sinneseindrücken und in unseren Vorstellungen. In unseren Gefühlen, in unserem Gefühlsleben wachen wir eigentlich nicht im vollen Sinne des Wortes.",
      "Und zwischen dem Vorstellungsleben und dem Gefühlsleben liegt für das gewöhnliche Bewußtsein ziemlich un­vermerkt die Schwelle. Denn das, was unser Gefühlsleben als tiefere Realität durchdringt, das kommt eigentlich dem Menschen in Wirk­lichkeit gar nicht zum Bewußtsein.",
      "Die Gefühle selbst kommen ihm zum Bewußtsein. Die Gefühle wogen herauf aus einer unterbewußten Welt, aber das Bewußtsein hat mit den Gefühlen wirklich nichts mehr zu tun, als wir im Schlafe mit unseren Träumen zu tun haben.",
      "Deshalb konnte auch in den öffentlichen Vorträgen hier in der Schweiz jetzt gesagt werden: Indem der Mensch in seinem Gefühlsleben lebt, schläft er eigentlich träumend. Das Traumleben dehnt sich herein in unser Wachleben.",
      "Wir sind vom Einschlafen bis zum Aufwachen eigentlich immer in Träumen; aber nur die am allerstärksten mit unserem phy­sischen Dasein zusammenhängenden Träume kommen zum Bewußtsein oder zur Erinnerung. Das Träumen geht durch das ganze Schlafleben weiter, und nur in den tieferen Schichten unseres Bewußtseins schlafen wir gewissermaßen traumlos.",
      "Aber dieses träumende und traumlos schlafende Leben geht auch in unser Wachleben herein. Das Traum-leben geht in unser Gefühlsleben herein, in das Affektleben. Und wir",
      "wissen von der Wirklichkeit, von dem wirklichen Inhalte im gewöhn­lichen Bewußtsein, im nichthellseherischen Bewußtsein nicht mehr von unserem Gefühlsleben, als wir von dem wissen, was eigentlich geschieht, wenn die Bilder des Traumlebens vor uns ablaufen. Daher konnte auch gesagt werden, daß der Mensch den Inhalt dessen,was man <(Geschichte» nennt, nicht mit wachem Bewußtsein erlebt, sondern durchträumt. Was Geschichte ist, ist ein Weltentraum des Menschen. Denn die Impulse, die in der Geschichte leben, leben eigentlich in den Gefühls-, in den Affektimpulsen; der Mensch träumt, indem er Geschichte erlebt. Also das Gefühlsleben liegt schon unterhalb der Schwelle des eigentlich wachen Bewußtseins. Auch in dieser seelischen Beziehung geht die Grenze zwischen bewußtem und unterbewußtem Leben mitten durch den Menschen.",
      "Und im Willensleben schläft der Mensch vollständig. Denn was eigentlich im Willen lebt, davon weiß der Mensch mit dem gewöhn­lichen Bewußtsein nichts. Sein gewöhnliches Bewußtsein lebt in der Realität, die sich im Willen ausspricht, genau so, wie es lebt im tiefen Schlafe. Bewußt verfolgt der Mensch eigentlich nur dasjenige, was schon aus dem Willen heraus und in die Handlung übergegangen ist; darinnen wacht er, im Vollziehen des Willens kann er nicht wachen. Daher stritten sich die Philosophen immer über die Freiheit und Un­freiheit des Willens, weil sie nicht eindringen konnten in das Gebiet -das nur mit hellseherischem Bewußtsein durchschaut werden kann -, aus dem der Wille eigentlich seine Impulse holt. So liegt also, ich betone es noch einmal, auch in seelischer Beziehung für diesen Menschen die Schwelle zwischen der eigentlichen physischen wachen Welt und der dem Menschen unterbewußt bleibenden Welt mitten im Menschen drinnen.",
      "Nun spielt in unser Leben herein, insofern es Gefühls- und Willens-leben ist, also verträumt und verschlafen wird, alles dasjenige, was der Mensch miterlebt zwischen dem Tod und einer neuen Geburt. Die Er­lebnisse der Toten sind eigentlich in der Welt, in der wir lebend auch sind, indem wir fühlen und wollen. Nur kennen wir mit dem gewöhn­lichen Bewußtsein die Realitäten, die im Fühlen und Willen leben, nicht. Würden wir das dem Gefühlsleben zugrunde liegende Reale,",
      "würden wir namentlich das dem Willensleben zugrunde liegende Wirk­liche so durchleben, wie wir das Wirkliche der Sinneswahrnehmungen und des Vorstellens - des Vorstellens schon weniger, aber doch bis zu einem gewissen Grade - wachend durchleben, dann wäre der Tote, der Mensch, der durch die Todespforte gegangen ist, genau ebenso neben uns, mit uns in fortwährender Verbindung, wie derjenige, der mit uns noch auf dem physischen Plane so herumwandelt, daß wir von ihm Eindrücke empfangen können im wachen Bewußtsein durch unsere Sinne und durch unser Vorstellungsleben. Dasjenige, was in den Im­pulsen der Toten lebt, das ragt fortwährend herein in unser Gefühls­leben, in das Leben unserer Willensimpulse. Und nur weil wir dies ver­träumen und verschlafen, fühlen wir uns von den Toten, mit denen wir verbunden waren, getrennt.",
      "Aber im Grunde ist die Welt, in der die sogenannten Toten leben, auch recht verschieden von der Welt, in der wir leben, wenn wir im physischen Leibe verkörpert sind. Denn fragen Sie sich mit voller Be­sonnenheit: Was liegt denn eigentlich vor für das wache Bewußtsein, für das nicht heilseherisch gewordene Bewußtsein vom Aufwachen bis zum Einschlafen? Es liegt nur dasjenige vor, was erlebt werden kann in der Welt, die sich als Sinnenteppich ausbreitet, und in der Welt, die wir uns durch unsere Vorstellungen aus dieser Sinneswelt machen. Von dieser Welt ist zunächst alles das, was dem sogenannten mineralischen Reiche angehört, wozu man Sinnesorgane braucht, um es wahrzu­nehmen, für den Toten unmittelbar nicht vorhanden. Zu dieser mine­ralischen Welt gehören zum Beispiel auch die Sterne, gehören Sonne und Mond, gehört überhaupt alles das, was mit den Sinnen wahr­genommen wird, und es gehört ein großes Gebiet der Pflanzenwelt dazu. Das sind zunächst Gebiete, die nicht aufgeschlossen liegen vor dem Geistes- und Seelenauge des Toten.",
      "Dagegen beginnt aufgeschlossen zu sein für das Seelenauge des Toten bereits die Welt, die auch mehr oder weniger unbewußt vor uns liegt, indem wir den Blick lenken - hier allerdings den durch die Sinneswelt verschleierten Blick - auf die tierische Welt. Die tierische Welt, das heißt die Welt der Impulse, der Kräfte, die in den Tieren leben, die ist für den Toten genauso die unterste Welt, wie für uns im physischen",
      "Leibe die mineralische Welt die unterste Welt ist. Wie sich für uns auf­baut die pflanzliche Welt, die hervorsprießt aus der mineralischen Welt, so baut sich für den Toten aus der Grundlage, die in der tierischen Welt lebt, die menschliche Welt auf, die menschliche Welt als seelische Welt. Und wie für uns das Tierreich erst die dritte Kategorie bildet, die sich aufbaut auf mineralischer, auf pflanzlicher Welt, so für den Toten als das weiter hinaufliegende Reich das Reich der Angeloi, Archangeloi und so weiter.",
      "Die ganze Umgebung, in die der Tote hineinversetzt ist, ist damit eine andere als die Umgebung, in der wir selbst im physischen Leibe leben. Denn stellen Sie sich einmal vor: aus der Welt, die Sie wahr­nehmen in Ihrem physischen Leibe, über die Sie sich Vorstellungen machen in Ihrem physischen Leibe, wäre alles dasjenige weg, was Sie durch die Sinne wahrnehmen: es bliebe überhaupt zunächst für das nichthellseherische Bewußtsein etwas übrig, was sich nur wie eine Traumeswelt ausnehmen könnte, was nur erträumt werden könnte, was nicht stärker im Bewußtsein leben könnte als ein Traum.",
      "Deutlicher aber wird der Unterschied, wenn wir ihn in einer andern Weise noch ins Auge fassen. Das wesentlichste Charakteristikum un­seres Lebens in der Umwelt, so lange wir im physischen Leibe verkör­pert sind, ist - obwohl innerlich die Sache anders ist, das wissen Sie aus andern Vorträgen -, daß wir, indem wir zu den mineralischen und pflanzlichen Wesen in eine Beziehung treten, das Bewußtsein haben können: diesen Wesen bleibt es verhältnismäßig gleichgültig, was wir mit ihnen anstellen. Wir handeln ja auch unter dem Einflusse dieses eben ausgesprochenen Gedankens. Wir zerschlagen ruhig Steine und haben zunächst das Bewußtsein, daß wir dem Stein nicht weh tun oder auch keine Lust bereiten. Sie wissen, innerlich ist die Sache etwas anders. Aber insofern wir Menschen mit der mineralischen Umwelt in Berührung stehen, denken wir mit einem gewissen Rechte: Lust und Leid wird nicht gleich aufgerührt, wenn wir einen Stein zerschlagen oder dergleichen.",
      "In ähnlicher Weise verhalten wir uns gegenüber der Pflanzenwelt. Und diejenigen Menschen sind schon sehr selten, welche zum Beispiel eine Art Schmerz, eine Art Mitgefühl empfinden, wenn eine Blume",
      "gepflückt wird. Die Menschen, welche in einem gewissen Sinne doch lieber die Rosen am Rosenstrauch haben als im Rosenbouquet im Zim­mer, die sind nicht gar so häufig. Erst bei der tierischen Welt fangen wir an, unser Menschliches unmittelbar mit der Umwelt in Beziehung zu bringen. Und noch einmal sei es gesagt, die Menschen, die mit einem auch nur entfernt ähnlichen Gefühle Rosen vom Rosenstrauch pflücken, wie sie Köpfe von Tieren abreißen würden, um sie zu Sträußchen zu­sammenzufügen, diese Menschen sind eben doch unter den Gegenwarts­menschen selten. Selbst unter Anthroposophen habe ich gefunden, daß nicht alle immer die Rosen am Rosenstrauch am allerliebsten haben, obwohl das Gefühl schon so weit fortgeschritten ist, daß noch niemals in einem Saale mir zum Beispiel ein Bouquet mit Nachtigallenköpfen überreicht worden ist! Da fangen wir an zu fühlen, wie das Leben, das sich in uns selbst ausdehnt, sich in unsere Umwelt hinein fortsetzt.",
      "Der Tote hat es nicht so. Für den Toten gibt es gar nichts in der Umgebung, für das er nicht das Gefühl haben könnte, wenn er nur einen Finger ausstreckt - es ist jetzt ganz symbolisch, bildlich gespro­chen -, durch das, was sich durch das Ausstrecken des Fingers, also durch irgendeine Aktion vollzieht, ja durch alles, was der Tote tut, löst sich Lust und Leid in der Umgebung aus. Er kommt gar nicht anders mit seiner Umwelt in Beziehung, als daß er Lust und Leid erweckt, daß überall ein Echo von Lust und Leid ist. Tun Sie etwas, nachdem Sie durch die Pforte des Todes gegangen sind, so geschieht immer durch das, was Sie tun, irgendwo Schmerz oder Freude, Entspannung oder Anspannung von so etwas, was dem Gefühlsleben ähnlich ist. Wenn wir an einen Tisch klopfen, haben wir eben das Gefühl, dem Tisch tut es nicht weh. Der Tote kann nie eine Aktion ausführen, ohne daß er weiß, er lebt und webt nicht nur in Lebendigem, sondern in gefühls­mäßig Lebendigem. Gefühlsmäßiger Reiz ist ausgebreitet über seine ganze Umgebung.",
      "Von einer andern Seite finden Sie das ja selbst geschildert in den entsprechenden Kapiteln meiner «Theosophie». Diese gefühlsmäßige Reizwelt lebt also oben im tierischen Reich auf einer untersten Stufe. Und so bekannt wir sind mit einer gewissen Außenseite des minerali­schen Reiches durch unsere Sinneswahrnehmungen, so bekannt ist der",
      "Tote mit der Innenseite - nicht mit der Außenform, aber mit der Innen­seite - des tierischen Lebens über seine ganze Welt hin. Das ist die unterste Grundlage, auf der er lebt, auf der er sich aufbaut, auf der er sein Dasein aufbaut. Und ein großes Stück Arbeit für den Toten besteht darinnen, sich in unmittelbare Beziehung zu der Welt des Tierisch-Lebendigen zu setzen.",
      "Wie wir uns hier von Kindheit auf in Beziehung setzen zu der Welt des Mineralisch-Toten, so leben wir uns nach dem Tode ein in eine all­mählich immer mehr an Breite und an Ausdehnung wachsende Bezie­hung zu der Welt des Tierisch-Lebendigen Die lernt der Tote nach allen Seiten kennen. Die lernt der Tote kennen, indem er stufenweise alle die Geheimnisse zu durchdringen hat, welche ihm hier so verborgen sind, wie seelisch dasjenige, was unter seinem Gefühlsleben schlummert; denn es ist dasselbe.",
      "Es kann selbstverständlich eine solche Frage wie diejenige, die ich jetzt aufwerfen will, nicht als eine ordentlich wissenschaftliche Frage gelten. Allein sie kann doch hinweisen auf irgend etwas, hinter dem reale Beziehungen sind. Gefragt werden kann, warum denn eigentlich dem Menschen hier in der physischen Welt manches verborgen ist beim Walten der alles durchdringenden Weltenweisheit. Man kann fragen, warum das verborgen ist, in das der Tote eingeweiht werden muß: in die Geheimnisse des Aufbaues der gesamten tierischen Welt.",
      "Gerade wenn man solch eine Frage zu beantworten versucht, greift man hinein in die tiefsten Geheimnisse des Daseins überhaupt. Und auch mit dieser Frage werden wir uns noch etwas zu befassen haben in diesen Betrachtungen. Zunächst aber haben wir den Blick darauf zu lenken, wie denn dieses Erfassen der Innenseite des tierischen Lebens eigentlich ist.",
      "Da könnte ich zunächst, um nicht theoretisch zu werden, vielleicht ausgehen von einer zeitgeschichtlichen Tatsache. Sie wissen, daß in einer gewissen äußerlichen Weise das menschliche historische Bewußt­sein in der neueren Zeit eine Umänderung erfahren hat durch den Darwinismus. Man hat versucht, die Kräfte zu finden, durch die sich die Organismen von sogenannten unvollkommenen zu vollkommenen Zuständen entwickeln. Die Darwinisten haben ja mancherlei genannt:",
      "zunächst das Prinzip der zweckmäßigen Auslese, der Anpassung an die Verhältnisse und so weiter. Ich will Ihnen mit diesen Dingen, die Sie in jedem Handbuch des Darwinismus nachlesen können, sogar in jedem Lexikon, nicht kommen. Aber hinweisen will ich darauf, daß das äußerliche, abstrakte Prinzipien sind; daß für den, der tiefer blickt, gar nichts damit gesagt ist. Was eigentlich geschieht, ist nicht gezeigt, wenn man sagt: die Vervollkommnung geschieht dadurch, daß die Passendsten ausgewählt werden und die andern allmählich absterben, während die Passendsten die Überlebenden sind. Damit ist natürlich nichts gesagt über die Kräfte, über die Impulse, die eigentlich im tie­rischen Reiche leben, damit die Tiere erst sich vervollkommnen, aber auch in der gewöhnlichen gegenwärtigen Welt ihr Leben entsprechend zimmern können.",
      "Was wirkt denn wirklich in den Kräften, die vom Darwinismus als Selektionskräfte, als Kräfte einer reinen mechanischen Zweckmäßig­keit und so weiter angesprochen werden? Darinnen wirken die Toten. Es gehört zu den überraschendsten, eindringlichsten Erfahrungen, die im Kreise derToten gemacht werden können, wenn man darauf kommt, wie - ebenso wie es hier Schmiede und Tischler und andere Leute gibt, welche in der mechanischen Welt handwerksmäßig arbeiten und da­durch die physisch-sinnliche Grundlage des Lebens hier schaffen - in der geistigen Welt, vom Tierreich angefangen nach aufwärts, die Toten arbeiten. Während das tierische Reich hier in vieler Beziehung ein sol­ches ist, das der Mensch als ein niedriges empfindet, aber das minera­lische liegt noch niedriger, ist die Grundlage der Arbeit der Toten die Fortführung des tierischen Reiches. Daher lebt sich der Tote gewisser­maßen ein in alle die Geschicklichkeiten, die ihm hier für das Leben zwischen der Geburt und deni Tode verborgen sind.",
      "Hier kommen wir dann an den Punkt, der vielfach geheimgehalten wurde bis in unsere Zeit von den Brüderschaften, welche zum Teil mit Recht, zum Teil mit Unrecht glauben, daß die andern Menschen für solche Dinge nicht reif sind. Lernt man erkennen, was sich auf die tierische Natur bezieht in der Welt der Toten, hält man da Umschau, so ist das alles Gefühlsmäßig-Lebendiges. Der Mensch hat auch in sei­ner Seele Gefühlsmäßig-Lebendiges. Aber wie? Zwischen der Geburt",
      "und dem Tod hat er es so, daß, wäre es nicht eingeschlossen in seine Unbewußtheit, der Mensch jederzeit dieses Gefühlsmäßig-Lebendige, das zwischen Geburt und Tod liegt, zum Verderb des übrigen Gefühls-mäßig-Lebendigen in der Welt verwenden könnte. Also bedenken Sie, was das eigentlich heißt! Sie leben selbst in Ihrem persönlichen Leben ein Gefühlsmäßig-Lebendiges, das aber eingeschlossen ist in die Gren­zen, die eben dem physischen Menschen gezogen sind. Hätten die Men­schen im allgemeinen das frei zur Verfügung - Anthroposophen werden in dieser Beziehung schon kultivierter sein -, so könnte der Mensch jederzeit die Kräfte, die da gerade verborgen sind, verwenden, um das um ihn liegende Gefühlsmäßig-Lebendige zu zerstören. Die tierische Natur im Menschen ist zunächst sogar im vorzüglichen Sinne eine zer­störerische, und sie ist sogar angelegt, zu zerstören. Und wenn der Mensch durch die Pforte des Todes gegangen ist, so ist es vor allen Dingen seine Aufgabe, alle die Impulse aus seiner Seele herauszu­reißen, welche dann in der Weise frei geworden sind, daß eigentlich sehr viel vorliegt von dem Bedürfnis, Lebendiges zu zerstören, Leben­diges zu töten. Und man kann sagen, zu dem, was der Tote lernen muß, gehört vor allen Dingen Achtung, Heiligachtung vor allem Le­bendigen.",
      "Diese Heiligachtung vor allem Lebendigen ist etwas, was man beob­achten kann als die selbstverständliche Entwickelung des Toten. So wie wir hier mit innigem Anteil ein Kind verfolgen, das sich von klein auf, allmählich, von Tag zu Tag, von Woche zu Woche selbstverständlich entwickelt, wie wir bei diesem Kinde verfolgen, wie das Seelische er­greift das Fleischlich-Leibliche, wie wir innige Freude haben an dem, was da geschieht, ohne daß der sogenannte freie Wille mitwirkt, was da rein durch seelisch-organische Kräfte geschieht: so hat man, wenn man den Toten von seinem Todestage an weiterhin durch sein Leben verfolgt, eben wiederum die Anschauung eines dem freien Willen zu­nächst entzogenen Einlebens in die Heilighaltung alles in der Umgebung befindlichen Lebendigen. Das ist gewissermaßen etwas, was wie eine Außenseite im Toten geschieht, so wie im Kinde es als Außenseite ge­schieht, daß es wächst, daß seine Züge ausdrucksvoller werden. Was so äußerlich am Kinde zu unserer Freude heranwächst, das wächst am",
      "Toten heran, indem wir von ihm immer mehr und mehr ausstrahlend finden das so erhebende Heilighalten alles Lebendigen.",
      "Und in dieser Beziehung unterscheidet sich gewichtig das Leben nach dem Tode von dem Leben hier. Das Leben hier hat gerade das­jenige durch einen Schleier verdeckt, in das sich der Tote vertiefen muß. Wir nehmen die Welt durch unsere Sinne wahr und bilden uns gewisse Gesetze, die wir Naturgesetze nennen, nach denen wir dann unsere mechanischen Werkzeuge, unsere Geräte ringsherum bilden. Das, was wir nach dem Gesetze der Natur um uns herum als eine Welt aufbauen, ist im wesentlichen eine Welt des Todes. Selbst die Pflanze, selbst den Baum müssen wir töten, wenn wir sein Holz in den Dienst unserer mechanischen Künste stellen wollen. Und es gehört wiederum zu den erschütterndsten Erkenntnissen, daß im Grunde genommen alles dasjenige, was uns unsere Sinne lehren, wenn wir es anwenden durch unseren Willen, ein Zerstörendes ist und gar nicht anders sein kann als ein Zerstörendes.",
      "Ja, selbst wenn wir Künstlerisches schaffen, müssen wir uns betei­ligen an der Welt des Zerstörens. Was wir da aufbauen, geht erst aus der Zerstörung hervor. Eine gütige Weltenweisheit hat nur bewirkt, daß wir in der Regel zunächst noch als Menschen zurückscheuen, von der tierischen Natur nach aufwärts dasjenige in den Dienst der me­chanischen Kunst zu stellen, was da lebt. In einem gewissen höheren Sinne lebt aber in der Welt eigentlich alles. Das können Sie aus den verschiedenen Darstellungen, die im Laufe der Jahre gegeben worden sind, schon erkennen. Was tun wir aber eigentlich, indem wir das in den Dienst der mechanischen Kunst stellen, was wir durch unsere Sinne wahrnehmen und durch unseren Verstand kombinieren? Wir tragen fortwährend den Tod in das Leben hinein. Ein Raffaelisches Gemälde selbst kann nicht zustande kommen, ohne daß der Tod in das Leben hineingetragen wird. Bevor ein Raffaelisches Gemälde entsteht, lebt mehr, als da lebt, nachdem ein Raffaelisches Gemälde entstanden ist. Die Abschlagszahlung im Universum besteht nur darin, daß Seelen kommen, die dieses Raffaelische Gemälde genießen, die von diesem Raffaelischen Gemälde einen Impuls, einen Eindruck bekommen. Der Impuls, der Eindruck, den die schaffende oder die genießende Seele",
      "bekommt, das ist dasjenige, was einzig und allein hinweghelfen kann über das Wirken des Todes - selbst in dem Fall, wenn die höchsten Güter, die sogenannten höchsten Güter der Menschheit hier auf dem physischen Plan geschaffen werden. Die Erde wird im wesentlichen dadurch zerstört werden, daß die Menschen den Tod mit ihren mecha­nischen Künsten in die Erde in einem so starken Maß hineintragen. Sie wird nicht mehr leben können, weil der Tod dasjenige überwiegt, was hinübergerettet werden kann über den Untergang der physischen Erde in die Jupiterwelt. Aber aus dem, was Menschen geschaffen haben, indem sie den Tod mit dem Leben verwoben haben, werden sie see­lischen Inhalt wiederum erhalten haben, den sie nun hinübertragen in die Jupiterwelt.",
      "Mehr als man sagen kann, webt sich durch menschliches Tun selber, dadurch daß dieses menschliche Tun zwischen Geburt und Tod innig verwoben ist mit dem Sinnessein, mehr als man sagen kann, webt sich fortwährend der Tod, webt sich fortwährend die Vernichtung des Lebendigen in das Leben ein. Allerdings beruht darauf, daß sich der Tod in das Leben einverwebt, die Entstehung des Bewußtseins über­haupt, und der Mensch würde gar nicht seine Erdenaufgabe in bezug auf das Bewußtsein absolvieren können, wenn er nicht dazu berufen wäre, den Tod in das Leben einzuweben. Selbst in unserem Innern töten wir in dem Augenblicke das Leben der Nerven, in welchem wir vorstellen wollen. Denn ein richtig lebender Nerv kann nicht vor-stellen. In unser Nervenleben hinein ersterben wir fortwährend, habe ich in öffentlichen Vorträgen in der letzten Zeit gesagt.",
      "In dieser Beziehung ist das Leben zwischen dem Tod und einer neuen Geburt ein völlig entgegengesetztes. Da handelt es sich darum, daß die Menschenseele vollständig sich einlebt in die Heilighaltung des Leben­digen, in die Durchdringung des Lebendigen mit immer mehr und mehr Leben. So hängt das Leben zwischen der Geburt und dem Tode zu­sammen mit dem Tode, und es hängt das Leben zwischen dem Tod und einer neuen Geburt zusammen mit dem Leben des Ganzen. Denn nur dadurch, daß der Mensch stirbt und von der geistigen Welt heraus seine Impulse in das Leben der Tiere sendet, lebt über die Erde hin eine tie­rische Welt.",
      "Das zweite, in das sich der Mensch nach dem Tode einlebt, ist das Reich der Menschenseelen selbst, gleichgültig, ob diese Menschenseelen hier im physischen Leibe verkörpert sind, oder ob sie selbst schon durch die Pforte des Todes gegangen sind. Der tierischen Welt gegenüber hat der Mensch nach dem Tode das Gefühl, wenn er eine Aktion ausführt: etwas hat Freude, oder etwas tut weh einem Wesen oder wenigstens einem Wesenhaften. Er weiß: Stößt du nur mit deiner Geisteskraft, so stößt du an Lebendiges.",
      "Hier ist es mehr ein allgemeines Leben und Weben im Lebendigen. Gegenüber der Bekanntschaft mit dem, was in unsere Sphäre, die menschliche Sphäre tritt, wenn wir tot sind, ist es so, daß, wenn eine andere Seele in Beziehung zu uns tritt, nachdem wir selbst durch die Pforte des Todes gegangen sind, wir dann fühlen, durch die Art, wie wir zu dieser Seele in Beziehung treten, wird unser eigenes Lebensgefühl entweder verstärkt oder abgeschwächt. Zu der einen Seele, gleichgültig ob sie hier auf Erden weilt oder drüben in den geistigen Welten, treten wir so in Beziehung, daß wir fühlen, wir werden stärker innerlich, nach einer gewissen Beziehung stärkt uns das Zusammensein mit der Seele, unsere inneren Kräfte werden stärker gemacht, wir leben gleich­sam mehr auf. Wir begegnen einer Seele und fühlen, wir wachen an ihr mehr auf, als wir ohne sie aufgewacht wären. Lebensinnigkeit fließt uns in einer gewissen Stärke zu durch die Bekanntschaft mit der einen Seele. Durch die Bekanntschaft mit einer andern Seele werden wir schwächer nach einer gewissen Kraftrichtung hin; sie dämpft unser Leben gewissermaßen ab. Und darin besteht das Zusammenleben mit Seelen, daß wir unser eigenes Leben lebendig wogen fühlen in der Ver­bindung mit andern Seelen.",
      "Wir leben als Menschen zwischen Geburt und Tod unser Gefühls-und Willensleben hin und wissen gar nicht, daß durch die Wogen un­seres Gefühls- und Willenslebens, die wir verschlafen und verträumen, die Totenseelen leben. Sie sind immer da; sie leben in unseren eigenen Gefühls- und Willenswogen, und sie leben so, daß sie mitleben dieses Leben. Während wir mit unseren Sinnen die Umwelt gewissermaßen doch als etwas Äußerliches erleben, leben in unseren Gefühlen und in unseren Willensimpulsen die Toten intimer mit uns verbunden, als wir",
      "mit unserer Umwelt hier, insofern wir physisch verkörpert sind, innig verbunden leben.",
      "Aber das ist so, daß dieses Leben, dieses Erleben, besser gesagt, dieses Leben-Innesein der Toten langsam und allmählich sich entwickelt, und zwar nach Maßgabe derjenigen Verhältnisse, die angesponnen sind hier im Leben. Gewiß, wir sind nach dem Tode mit allen Seelen zusammen, das ist schon wahr, aber wir wissen nichts davon. Langsam und all­mählich stellen sich Beziehungen her, und zwar zu denjenigen Seelen, mit denen wir Beziehungen angeknüpft haben in dem Leben zwischen Geburt und Tod. Neue Beziehungen, ursprüngliche Beziehungen kann der Mensch zum Menschen nicht anknüpfen in dem Leben zwischen dem Tod und einer neuen Geburt, ursprünglich, unmittelbar kann er nicht anknüpfen. Wenn wir hier jemand lieb gehabt haben, oder einen gehaßt haben, also mit ihm in irgendeiner positiven oder negativen Verbindung waren, so tritt das wiederum aus einer grauen Geistestiefe im allmählichen Heraufleben des Lebens nach dem Tode auf, in der Art, wie ich es eben angedeutet habe, daß wir drinnen leben in diesen Seelen.",
      "Und so besteht ein großer Teil dieses Erlebens, dieses Leben-Inne-seins der Toten darinnen, daß allmählich auftaucht eben aus grauer Geistestiefe alles dasjenige, was an Banden da war aus dem letzten oder vorletzten oder früheren Leben, an Verhältnissen mit andern Seelen. Das kann sich weiter ausdehnen, dehnt sich für manchen Toten ver­hältnismäßig sehr früh, sehr bald nach dem Tode aus, doch mittelbar.",
      "Es kann so sein, daß jemand stirbt; er hat mit einer Seele, die ent­weder noch auf Erden weilt, oder in der geistigen Welt weilt, in Be­ziehung gestanden, in irgendeiner Beziehung. Diese Beziehung tritt in ihrer Wirklichkeit nach dem Tode ihm wiederum in der angedeuteten Weise entgegen. Aber diese Seele, mit der er in Beziehung gestanden hat, hat Beziehungen zu andern Seelen, mit denen er vielleicht nicht in Beziehung gestanden hat in irgendeinem Leben zwischen Geburt und Tod. Da, indirekt, mittelbar können dann auch solche Seelen an den sogenannten Toten herantreten, mit ihm in eine Beziehung treten. Nur allerdings sind das niemals unmittelbare Beziehungen, wie ich schon sagte, sondern sie sind immer vermittelt durch diejenigen Seelen, mit",
      "denen man durch das physische Leben karmisch verbunden ist. Die Verbindung mit solchen Seelen, mit denen man die Verbindung nicht im physischen Leben begründet hat, ist doch immer eine ganz andere, und sie wird vermittelt durch die Seelen, mit denen man im physischen Leben in Beziehung gestanden hat.",
      "Sie können sich auch jetzt leicht vorstellen, daß zunächst die un­mittelbaren Beziehungen vorliegen, dann die mittelbaren Beziehungen. Dadurch aber, daß über die Erde hin doch die Seelen alle mehr oder weniger miteinander verbunden sind, der Mensch in dem langen Leben zwischen dem Tod und einer neuen Geburt wenigstens indirekt in viele Beziehungen hineingerät, lebt sich der Mensch in der Tat, wenn man die mittelbaren Beziehungen mitrechnet, in ein weites Miterleben mit andern Seelen hinein. Dieses Hineinleben in andere Seelen haben wir immer in uns, auch wenn wir hier auf der Erde stehen. Wir haben mit unzähligen Seelen immer wieder und wiederum gelebt in der geistigen Welt. Dieses Sich-Einsfühlen mit allen Seelen, das eine abstrakte Philo­sophie eben auch nur abstrakt behandelt und als abstraktes Einssein bespricht, das hat seine sehr konkrete Seite: es gibt eigentlich über die Erde hin kaum Seelen, mit denen nicht wenigstens eine entfernte, in­direkte Verbindung doch besteht.",
      "Diese Sache muß man so konkret fassen wie möglich, dann kommt man mit ihr zum Realen. Das, was der Tote so erlebt, ist also ein all­mähliches Hineinwachen, Hineinaufwachen in eine Welt, die aber zur Grundlage sein Karma im weiteren Sinne hat. Über diese Welt hin wird es gleichsam immer mehr innerlich licht und lichter, indem wir immer Reicheres und Reicheres erleben in diesem zweiten Reiche, das sich auf dem Reich des Tierischen aufbaut, wie unser Erleben mit dem Pflanzenreich auf dem Reich des Mineralischen. Reicheres und Rei­cheres erlebt man immer mehr.",
      "Dieses Erleben denken Sie sich in all den konkreten Beziehungen ausgestaltet, dann haben Sie vieles von dem, was die Seele der Toten zwischen Tod und neuer Geburt durchdringt. Denn verbunden mit diesem Erleben sind ja alle Gedanken, die uns karmisch irgendwie ver­binden mit den andern Seelen. Eine unendlich reiche Welt liegt dar­innen. Und es ist im wesentlichen - das können Sie schon aus dem",
      "Zyklus über das Leben zwischen dem Tod und einer neuen Geburt ent­nehmen - in der ersten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt so, daß die Entwickelung eine mehr weisheitsvolle ist. Der Mensch lebt sich weisheitsvoll ein in die Verbindungen, die er sich allmählich wiederum herausholt aus grauer Geistestiefe; weisheitsvoll lebt er sich da hinein.",
      "Von dem, was ich in den Mysterien «Mitternachtsstunde des Da­seins» genannt habe, sind im wesentlichen die Fäden gezogen zu all den karmischen direkten und indirekten Verbindungen hin, zu denen sie zu ziehen sind. Dann kommt das Verarbeiten. Dann tritt in das mensch­liche Seelenleben ein mehr dem Willen ähnliches Kraftelement ein, aber nur ein ähnliches, nicht ein gleiches. Dieses dem Willen ähnliche Kraft-element macht den Menschen immer stärker und stärker. Es verstärkt vor allen Dingen die Impulse in ihm, welche zu dem weisheitsvollen Überblicken der Welt als willensmäßige Elemente, willensmäßige Im­pulse, als Kraftimpulse dazukommen.",
      "Nun tritt etwas Merkwürdiges ein. Im Menschen lebt ein gewisser Wille in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt auf. Wenn man diesen Willen beobachtet - man kann das insbesondere bei denjenigen Menschen, welche durch irgendwelche Verhältnisse ein gewissermaßen kurzes Leben zwischen dem Tod und einer neuen Geburt, ein abgekürztes Leben, haben -, da tritt eine merk­würdige Willensrichtung ein, die man etwa charakterisieren kann da­durch, daß man sagt: Es tritt der Wille ein, die Spuren des Lebens, die Spuren des Karma in einer gewissen Weise zu verwischen.",
      "Ich bitte Sie, das recht deutlich aufzufassen. Solch ein Wille: die Spuren des Karma zu verwischen, tritt im Menschen immer mehr und mehr auf. Dieses Verwischen der Spuren des Karma, das hängt mit den tiefsten Geheimnissen des Menschenlebens zusammen. Und würde der Mensch immerfort den vollen Überblick über die Weisheit haben, den er nach seinem Tode verhältnismäßig bald haben kann, so würden un­zählig viele Menschen lieber die Spuren ihres Daseins verwischen, als in neue Erdenleben eintreten. Die Verarbeitung der früheren Erden-leben im karmischen Zusammenhang, die wir ja vollziehen, kann sich im wesentlichen nur dadurch entwickeln, daß wir durch gewisse Wesen",
      "der höheren Hierarchien in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt mit Bezug auf das Weisheitslicht ab-getrübt werden, abgelähmt werden, so daß wir unsere Tätigkeit, unsere Willensimpulse immer mehr und mehr einschränken. Und man kann nur sagen: das Ziel geht dann dahin, sie so einzuschränken, daß wir eben dasjenige schaffen, was sich dann in der Vererbungsströmung mit einem physischen Menschenleib verbinden und in diesem physischen Menschenleib sein Erdenschicksal ausleben kann.",
      "Vollständig versteht man diesen Gedanken allerdings nur dann, wenn man dieses Erdenschicksal selbst ins Auge faßt. Wie ist doch die­ses Erdenschicksal selbst etwas Traumhaftes für den Erdenmenschen! Er lebt sich ein als Kind in die Verhältnisse des Erdenlebens. Dasjenige, was man Schicksal nennt, tritt in Form von einzelnen Lebenserfahrun­gen an ihn heran. Aus dem Gewebe, das diese Lebenserfahrungen bilden, gestaltet sich etwas, was eigentlich wir selbst sind. Denn bedenken Sie alle, was Sie wären bis zu Ihrem heutigen Tage, wenn Sie nicht gerade das Schicksalsleben erlebt hätten, das Sie eben erlebt haben. Sie können schon sagen: Das, was ich als Schicksal erlebt habe, bin ich selber. -Denn ein ganz anderer wären Sie, wenn Sie eben etwas anderes als Schicksal erlebt hätten.",
      "Und dennoch, wie fremd fühlt der Mensch eigentlich sein Schick­sal, wie wenig fühlt er es mit dem verwoben, was er sein Ich nennt. In wie unzähligen Fällen fühlt sich das Ich eben getroffen vom Schick­sal. Warum? Weil das, was wir selbst aus uns heraus arbeiten an der Zimmerung unseres Schicksals, eben im Unterbewußten bleibt. Das, was wir erleben, das stellt sich hinein in die Welt der Sinneserfahrung und in die Welt der Vorstellungen. Es schlägt ja nur an unser Gefühls­leben an. Unser Gefühlsleben verhält sich dazu passiv. Aber aktiv aus diesem Gefühlsleben und aus diesem Leben der Willensimpulse kraftet dasjenige heraus, was wir nun auch mit dem Reich der Toten gemein­schaftlich haben. Was da aber herauskraftet und was wir selber tun ohne unser Bewußtsein, was wir wiederum verschlafen und verträu­men, das bildet unser Schicksal, das sind wir selbst. Was wir an unserem Schicksal tun, verschlafen und verträumen wir. Was wir an unserem Schicksal erleben, das leben wir allerdings wachend durch, aber eben",
      "nur, weil es unterbewußt bleibt. Was bleibt da eigentlich unterbewußt? Dasjenige, was als Impulse herüberschlägt aus den früheren Erden-verkörperungen und aus dem Leben zwischen dem Tod und einer neuen Geburt auf eine rein geistige Weise aus dem Reiche, in dem die Toten auch sind, aus dem Reiche, das wir verträumen und verschlafen. Das sind zugleich Kräfte, die auch von uns selbst kommen. Es sind die Kräfte, mit denen wir unser Schicksal zimmern. Wir weben unser Schicksal aus demselben Reiche heraus, das mit uns gemeinschaftlich die Toten beleben.",
      "Denken Sie sich, wie wir da zusammenwachsen mit dem Reiche, von dem wir bis zu einem gewissen Grade jetzt wissen, wie es ver­schlafen wird: Wie wir es erleben! - obwohl wir noch nicht haben besprechen können, wie nun das Erleben gegenüber den Wesen der höheren Hierarchien ist; das wird auch noch dazukommen. Aber was man hervorrufen möchte durch eine solche Auseinandersetzung, wie ich sie eben gegeben habe, das ist, daß wir das Reich der sogenannten Toten hereinrücken in das Reich, in dem wir selber leben. Und bewußt werden wir uns, wie wir uns nur durch den Umstand von den Toten getrennt fühlen - aber nicht von ihnen getrennt sind -, daß wir unser Gefühlsleben, in dem die Toten auch sind, und unser Willensleben, in dem die Toten auch sind, verträumen und verschlafen.",
      "In dieser Welt, die wir verträumen und verschlafen, liegt aber noch etwas anderes, etwas, was der Mensch im gewöhnlichen Bewußtsein im Grunde gar nicht verfolgt. Er wird manchmal darauf aufmerksam, wenn es ihm in besonders eklatanten Fällen entgegentritt; aber das sind sensationelle einzelne Fälle, die nur auf dasjenige hinweisen, was das Leben fortwährend durchdringt und durchzieht. Wieviel werden Sie selbst von solchen Fällen gehört haben, wie der folgende ist!",
      "Ein Mensch ist gewöhnt, täglich einen Spaziergang zu machen; et führt ihn auf einen Berghang. Da geht er täglich hin, das ist seine Lust. Eines Tages geht er wiederum hin. Plötzlich, während er geht, hört er etwas wie eine Stimme, die aber nicht physisch da ist, die ihm sagt:",
      "Warum gehst du eigentlich diesen Weg? Kannst du diese Lust nicht auch entbehren? - So ungefähr sagt sie zu ihm. Da wird er stutzig. Er tritt etwas zur Seite und denkt nach über das, was ihm geschehen ist.",
      "In dem Augenblicke rollt ein Felsstück in die Tiefe, das ihn ganz sicher erschlagen hätte, wenn er nicht beiseite getreten wäre.",
      "Das ist eine wahre Geschichte, aber eine von denjenigen Geschichten, die eben nur sensationell, möchte ich sagen, auf etwas hinweisen, was fortwährend in unserem Leben da ist. Wie oft kommt es vor, daß Sie sich vornehmen, dies oder jenes zu tun. Sie werden durch dies oder jenes abgehalten. Malen Sie sich einmal aus,wie vieles manchmal anders geworden wäre im kleinen Erleben des Tages, wenn Sie einen Ausgang zu einer festgesetzten Stunde unternommen hätten, den Sie dann eine halbe Stunde später unternommen haben, weil Sie durch irgend etwas abgehalten worden sind, malen Sie sich aus, was da als Veränderung in Ihr Leben hineingekommen ist, was sogar als Veränderung in das Leben vieler anderer Menschen hineingekommen ist! Leicht kann man sich so etwas ausmalen. Nehmen wir einmal an: Sie haben sich vorgenommen, an einem Tage um viertel Vier Uhr nachmittags einen gewissen Gang zu machen, da wären Sie mit einem andern Menschen zusammengetrof­fen; dem hätten Sie eine Mitteilung gemacht, der wiederum diese Mit­teilung einem andern gemacht hätte. Sie machen, weil Sie zu spät kom­men, diese Mitteilung dem andern Menschen nicht und sehen: es wird hintangehalten, gewisse recht wichtige Dinge geschehen nicht.",
      "Da sieht man eine Weltenordnung, die anderer Art ist als die Wel­tenordnung, die wir als natürliche Notwendigkeit bezeichnen. Darin, daß jemand von dem Weiterschreiten auf einem Spazierwege abgehal­ten wird, weil er eine Stimme hört, durch die er beiseite tritt, was ver­hindert, daß er von einem Felsblock erschlagen wird, darin fühlen wir eine andere Weltenordnung hereinragen. Aber diese andere Welten-ordnung ragt ja in jedem Augenblick unseres Daseins herein, nur nicht durch so sensationelle Ereignisse. Der Mensch ist nur gewöhnt, den Blick aufs Sensationelle zu richten auch in diesen Dingen. Wir beach­ten jene Welt nur nicht. Warum? Weil wir den Blick richten auf das, was geschieht in unserem Leben und in unserer Umwelt, und nicht richten den Blick auf dasjenige, was nicht geschieht, was immerfort abgehalten wird, was immerfort zurückgehalten wird.",
      "Von einem gewissen Momente des geistigen Erlebens an kann das­jenige, was nicht geschieht, wovor wir gewissermaßen bewahrt oder",
      "zurückgehalten worden sind, uns ebenso zum Bewußtsein kommen wie dasjenige, was geschehen ist. Nur kommt es uns zum Bewußtsein als eine andere Weltenordnung. Versuchen Sie, jene Weltenordnung sich einmal recht zur Seele zu bringen, indem Sie sich sagen: Der Mensch ist gewöhnt, nur auf dasjenige zu sehen, was geschieht, und nicht auf dasjenige, was vom Geschehen abgehalten wurde. - Was er da nicht beachtet, das hängt innig zusammen mit dem Reiche, in dem die Toten sind, in dem wir selbst sind mit unserem träumenden Fühlen, mit unserem schlafenden Willen. Wir trennen uns in uns selber von einer ganz andern Welt dadurch ab, daß auch in das wache Leben der Traum, der Schlaf hereinspielen. Und was da alles brodelt und lebt und webt unter der Grenze, die unser Vorstellen von unserem Fühlen trennt, das ist zugleich dasjenige, was einschließt die Geheimnisse, welche die Brücke bilden zwischen den sogenannten Lebendigen und den sogenann­ten Toten, aber auch die Brücke bilden zwischen dem Reich der Not­wendigkeit und dem Reich der Freiheit und dem sogenannten Zufall."
    ],
    "sentences": [
      [
        "Wie ich schon bemerkt habe, werden wir in diesen Tagen Betrachtungen anstellen, die dann morgen oder übermorgen gipfeln werden in einer Auseinandersetzung über geschichtliche Notwendigkeit und Freiheit, gipfeln werden darinnen, daß gezeigt werden soll, in welchem Sinne ein geschichtliches Ereignis notwendig ist, und in welchem Sinne ein geschichtliches Ereignis, überhaupt irgend etwas, das in das Menschen­leben seelisch hereingreift, auch anders sein könnte.",
        "Es ist dieses ein Problem, das in der Gegenwart, wo so bedeutungsvolle Ereignisse her-eingreifen in das Menschenleben, von ganz besonders tiefgehender Be­deutung ist.",
        "Denn angesichts der traurigen, katastrophalen Ereignisse der Gegenwart muß sich jeder Mensch die Frage stellen: Inwiefern sind solche Ereignisse und ist gerade dieses Ereignis abhängig von einer gewissen Notwendigkeit, und inwiefern hätte es auch ganz anders aus­fallen können, hätte es sich ganz anders gestalten können?"
      ],
      [
        "Wie gesagt, wir werden in diesen Tagen darauf hinzielen, uns diese große, umfassende Frage zu beantworten mit den Mitteln, die man gegenwärtig in den öffentlich zu besprechenden okkulten Grundlagen haben kann.",
        "Aber wir müssen ausgehen von einer umfassenderen Be­trachtung des menschlichen Lebens.",
        "Wir müssen uns etwas vertiefen von einer gewissen Seite her in die menschliche Natur selbst.",
        "Das müs­sen wir vorausgehen lassen.",
        "Denn, wie Sie vielleicht gerade aus den in der letzten Zeit gehaltenen öffentlichen Vorträgen entnehmen können, in das menschliche Leben spielen fortwährend die Kräfte jener Welt herein, in welcher der Mensch sich befindet zwischen dem Tode und einer neuen Geburt.",
        "Viel intensiver, als man denkt, spielen die Kräfte, in die der Mensch als sogenannter Toter eingebettet ist, in das Leben herein.",
        "Wir sind - ich habe das letzte Mal, ich möchte sagen, mehr physisch darauf aufmerksam gemacht - als Menschen so geartet, daß im Grunde genommen die Schwelle zwischen der gewöhnlichen phy­sischen Welt und der geistigen Welt mitten durch uns geht.",
        "Wenn wir unser gewöhnliches Leben ins Auge fassen und das, was wir das letzte"
      ],
      [
        "Mal mehr physisch betrachtet haben, heute mehr seelisch betrachten, so können wir sagen: unser menschliches Leben, wenn wir hier im physischen Leibe verkörpert sind, verläuft so, daß wir erstens alles das in uns wirksam haben, was durch unsere Sinne während unseres Lebens erfahren werden kann, alles das, was sich gewissermaßen als der Sinnes-teppich um uns herum ausbreitet und wovon wir durch unsere Sinne Kunde erhalten.",
        "Auf diese Welt baut sich dann alles das auf, was wir aus dieser Sinneswelt herausarbeiten, was wir aber auch unabhängig von dieser Sinneswelt durchdringen können in unserem Vorstellungs­leben.",
        "Wenn wir aber Sinnesleben und Vorstellungsleben zusammen­fassen, so haben wir im Grunde schon alles dasjenige, worin wir mit unserem gewöhnlichen wachen Bewußtsein leben."
      ],
      [
        "Von dem Augenblicke an, wo wir morgens aufwachen, bis zu dem Augenblicke, wo wir einschlafen, wachen wir in Wirklichkeit nur voll­ständig in unseren Sinneseindrücken und in unseren Vorstellungen.",
        "In unseren Gefühlen, in unserem Gefühlsleben wachen wir eigentlich nicht im vollen Sinne des Wortes."
      ],
      [
        "Und zwischen dem Vorstellungsleben und dem Gefühlsleben liegt für das gewöhnliche Bewußtsein ziemlich un­vermerkt die Schwelle.",
        "Denn das, was unser Gefühlsleben als tiefere Realität durchdringt, das kommt eigentlich dem Menschen in Wirk­lichkeit gar nicht zum Bewußtsein."
      ],
      [
        "Die Gefühle selbst kommen ihm zum Bewußtsein.",
        "Die Gefühle wogen herauf aus einer unterbewußten Welt, aber das Bewußtsein hat mit den Gefühlen wirklich nichts mehr zu tun, als wir im Schlafe mit unseren Träumen zu tun haben."
      ],
      [
        "Deshalb konnte auch in den öffentlichen Vorträgen hier in der Schweiz jetzt gesagt werden: Indem der Mensch in seinem Gefühlsleben lebt, schläft er eigentlich träumend.",
        "Das Traumleben dehnt sich herein in unser Wachleben."
      ],
      [
        "Wir sind vom Einschlafen bis zum Aufwachen eigentlich immer in Träumen; aber nur die am allerstärksten mit unserem phy­sischen Dasein zusammenhängenden Träume kommen zum Bewußtsein oder zur Erinnerung.",
        "Das Träumen geht durch das ganze Schlafleben weiter, und nur in den tieferen Schichten unseres Bewußtseins schlafen wir gewissermaßen traumlos."
      ],
      [
        "Aber dieses träumende und traumlos schlafende Leben geht auch in unser Wachleben herein.",
        "Das Traum-leben geht in unser Gefühlsleben herein, in das Affektleben.",
        "Und wir"
      ],
      [
        "wissen von der Wirklichkeit, von dem wirklichen Inhalte im gewöhn­lichen Bewußtsein, im nichthellseherischen Bewußtsein nicht mehr von unserem Gefühlsleben, als wir von dem wissen, was eigentlich geschieht, wenn die Bilder des Traumlebens vor uns ablaufen.",
        "Daher konnte auch gesagt werden, daß der Mensch den Inhalt dessen,was man <(Geschichte» nennt, nicht mit wachem Bewußtsein erlebt, sondern durchträumt.",
        "Was Geschichte ist, ist ein Weltentraum des Menschen.",
        "Denn die Impulse, die in der Geschichte leben, leben eigentlich in den Gefühls-, in den Affektimpulsen; der Mensch träumt, indem er Geschichte erlebt.",
        "Also das Gefühlsleben liegt schon unterhalb der Schwelle des eigentlich wachen Bewußtseins.",
        "Auch in dieser seelischen Beziehung geht die Grenze zwischen bewußtem und unterbewußtem Leben mitten durch den Menschen."
      ],
      [
        "Und im Willensleben schläft der Mensch vollständig.",
        "Denn was eigentlich im Willen lebt, davon weiß der Mensch mit dem gewöhn­lichen Bewußtsein nichts.",
        "Sein gewöhnliches Bewußtsein lebt in der Realität, die sich im Willen ausspricht, genau so, wie es lebt im tiefen Schlafe.",
        "Bewußt verfolgt der Mensch eigentlich nur dasjenige, was schon aus dem Willen heraus und in die Handlung übergegangen ist; darinnen wacht er, im Vollziehen des Willens kann er nicht wachen.",
        "Daher stritten sich die Philosophen immer über die Freiheit und Un­freiheit des Willens, weil sie nicht eindringen konnten in das Gebiet -das nur mit hellseherischem Bewußtsein durchschaut werden kann -, aus dem der Wille eigentlich seine Impulse holt.",
        "So liegt also, ich betone es noch einmal, auch in seelischer Beziehung für diesen Menschen die Schwelle zwischen der eigentlichen physischen wachen Welt und der dem Menschen unterbewußt bleibenden Welt mitten im Menschen drinnen."
      ],
      [
        "Nun spielt in unser Leben herein, insofern es Gefühls- und Willens-leben ist, also verträumt und verschlafen wird, alles dasjenige, was der Mensch miterlebt zwischen dem Tod und einer neuen Geburt.",
        "Die Er­lebnisse der Toten sind eigentlich in der Welt, in der wir lebend auch sind, indem wir fühlen und wollen.",
        "Nur kennen wir mit dem gewöhn­lichen Bewußtsein die Realitäten, die im Fühlen und Willen leben, nicht.",
        "Würden wir das dem Gefühlsleben zugrunde liegende Reale,"
      ],
      [
        "würden wir namentlich das dem Willensleben zugrunde liegende Wirk­liche so durchleben, wie wir das Wirkliche der Sinneswahrnehmungen und des Vorstellens - des Vorstellens schon weniger, aber doch bis zu einem gewissen Grade - wachend durchleben, dann wäre der Tote, der Mensch, der durch die Todespforte gegangen ist, genau ebenso neben uns, mit uns in fortwährender Verbindung, wie derjenige, der mit uns noch auf dem physischen Plane so herumwandelt, daß wir von ihm Eindrücke empfangen können im wachen Bewußtsein durch unsere Sinne und durch unser Vorstellungsleben.",
        "Dasjenige, was in den Im­pulsen der Toten lebt, das ragt fortwährend herein in unser Gefühls­leben, in das Leben unserer Willensimpulse.",
        "Und nur weil wir dies ver­träumen und verschlafen, fühlen wir uns von den Toten, mit denen wir verbunden waren, getrennt."
      ],
      [
        "Aber im Grunde ist die Welt, in der die sogenannten Toten leben, auch recht verschieden von der Welt, in der wir leben, wenn wir im physischen Leibe verkörpert sind.",
        "Denn fragen Sie sich mit voller Be­sonnenheit: Was liegt denn eigentlich vor für das wache Bewußtsein, für das nicht heilseherisch gewordene Bewußtsein vom Aufwachen bis zum Einschlafen?",
        "Es liegt nur dasjenige vor, was erlebt werden kann in der Welt, die sich als Sinnenteppich ausbreitet, und in der Welt, die wir uns durch unsere Vorstellungen aus dieser Sinneswelt machen.",
        "Von dieser Welt ist zunächst alles das, was dem sogenannten mineralischen Reiche angehört, wozu man Sinnesorgane braucht, um es wahrzu­nehmen, für den Toten unmittelbar nicht vorhanden.",
        "Zu dieser mine­ralischen Welt gehören zum Beispiel auch die Sterne, gehören Sonne und Mond, gehört überhaupt alles das, was mit den Sinnen wahr­genommen wird, und es gehört ein großes Gebiet der Pflanzenwelt dazu.",
        "Das sind zunächst Gebiete, die nicht aufgeschlossen liegen vor dem Geistes- und Seelenauge des Toten."
      ],
      [
        "Dagegen beginnt aufgeschlossen zu sein für das Seelenauge des Toten bereits die Welt, die auch mehr oder weniger unbewußt vor uns liegt, indem wir den Blick lenken - hier allerdings den durch die Sinneswelt verschleierten Blick - auf die tierische Welt.",
        "Die tierische Welt, das heißt die Welt der Impulse, der Kräfte, die in den Tieren leben, die ist für den Toten genauso die unterste Welt, wie für uns im physischen"
      ],
      [
        "Leibe die mineralische Welt die unterste Welt ist.",
        "Wie sich für uns auf­baut die pflanzliche Welt, die hervorsprießt aus der mineralischen Welt, so baut sich für den Toten aus der Grundlage, die in der tierischen Welt lebt, die menschliche Welt auf, die menschliche Welt als seelische Welt.",
        "Und wie für uns das Tierreich erst die dritte Kategorie bildet, die sich aufbaut auf mineralischer, auf pflanzlicher Welt, so für den Toten als das weiter hinaufliegende Reich das Reich der Angeloi, Archangeloi und so weiter."
      ],
      [
        "Die ganze Umgebung, in die der Tote hineinversetzt ist, ist damit eine andere als die Umgebung, in der wir selbst im physischen Leibe leben.",
        "Denn stellen Sie sich einmal vor: aus der Welt, die Sie wahr­nehmen in Ihrem physischen Leibe, über die Sie sich Vorstellungen machen in Ihrem physischen Leibe, wäre alles dasjenige weg, was Sie durch die Sinne wahrnehmen: es bliebe überhaupt zunächst für das nichthellseherische Bewußtsein etwas übrig, was sich nur wie eine Traumeswelt ausnehmen könnte, was nur erträumt werden könnte, was nicht stärker im Bewußtsein leben könnte als ein Traum."
      ],
      [
        "Deutlicher aber wird der Unterschied, wenn wir ihn in einer andern Weise noch ins Auge fassen.",
        "Das wesentlichste Charakteristikum un­seres Lebens in der Umwelt, so lange wir im physischen Leibe verkör­pert sind, ist - obwohl innerlich die Sache anders ist, das wissen Sie aus andern Vorträgen -, daß wir, indem wir zu den mineralischen und pflanzlichen Wesen in eine Beziehung treten, das Bewußtsein haben können: diesen Wesen bleibt es verhältnismäßig gleichgültig, was wir mit ihnen anstellen.",
        "Wir handeln ja auch unter dem Einflusse dieses eben ausgesprochenen Gedankens.",
        "Wir zerschlagen ruhig Steine und haben zunächst das Bewußtsein, daß wir dem Stein nicht weh tun oder auch keine Lust bereiten.",
        "Sie wissen, innerlich ist die Sache etwas anders.",
        "Aber insofern wir Menschen mit der mineralischen Umwelt in Berührung stehen, denken wir mit einem gewissen Rechte: Lust und Leid wird nicht gleich aufgerührt, wenn wir einen Stein zerschlagen oder dergleichen."
      ],
      [
        "In ähnlicher Weise verhalten wir uns gegenüber der Pflanzenwelt.",
        "Und diejenigen Menschen sind schon sehr selten, welche zum Beispiel eine Art Schmerz, eine Art Mitgefühl empfinden, wenn eine Blume"
      ],
      [
        "gepflückt wird.",
        "Die Menschen, welche in einem gewissen Sinne doch lieber die Rosen am Rosenstrauch haben als im Rosenbouquet im Zim­mer, die sind nicht gar so häufig.",
        "Erst bei der tierischen Welt fangen wir an, unser Menschliches unmittelbar mit der Umwelt in Beziehung zu bringen.",
        "Und noch einmal sei es gesagt, die Menschen, die mit einem auch nur entfernt ähnlichen Gefühle Rosen vom Rosenstrauch pflücken, wie sie Köpfe von Tieren abreißen würden, um sie zu Sträußchen zu­sammenzufügen, diese Menschen sind eben doch unter den Gegenwarts­menschen selten.",
        "Selbst unter Anthroposophen habe ich gefunden, daß nicht alle immer die Rosen am Rosenstrauch am allerliebsten haben, obwohl das Gefühl schon so weit fortgeschritten ist, daß noch niemals in einem Saale mir zum Beispiel ein Bouquet mit Nachtigallenköpfen überreicht worden ist!",
        "Da fangen wir an zu fühlen, wie das Leben, das sich in uns selbst ausdehnt, sich in unsere Umwelt hinein fortsetzt."
      ],
      [
        "Der Tote hat es nicht so.",
        "Für den Toten gibt es gar nichts in der Umgebung, für das er nicht das Gefühl haben könnte, wenn er nur einen Finger ausstreckt - es ist jetzt ganz symbolisch, bildlich gespro­chen -, durch das, was sich durch das Ausstrecken des Fingers, also durch irgendeine Aktion vollzieht, ja durch alles, was der Tote tut, löst sich Lust und Leid in der Umgebung aus.",
        "Er kommt gar nicht anders mit seiner Umwelt in Beziehung, als daß er Lust und Leid erweckt, daß überall ein Echo von Lust und Leid ist.",
        "Tun Sie etwas, nachdem Sie durch die Pforte des Todes gegangen sind, so geschieht immer durch das, was Sie tun, irgendwo Schmerz oder Freude, Entspannung oder Anspannung von so etwas, was dem Gefühlsleben ähnlich ist.",
        "Wenn wir an einen Tisch klopfen, haben wir eben das Gefühl, dem Tisch tut es nicht weh.",
        "Der Tote kann nie eine Aktion ausführen, ohne daß er weiß, er lebt und webt nicht nur in Lebendigem, sondern in gefühls­mäßig Lebendigem.",
        "Gefühlsmäßiger Reiz ist ausgebreitet über seine ganze Umgebung."
      ],
      [
        "Von einer andern Seite finden Sie das ja selbst geschildert in den entsprechenden Kapiteln meiner «Theosophie».",
        "Diese gefühlsmäßige Reizwelt lebt also oben im tierischen Reich auf einer untersten Stufe.",
        "Und so bekannt wir sind mit einer gewissen Außenseite des minerali­schen Reiches durch unsere Sinneswahrnehmungen, so bekannt ist der"
      ],
      [
        "Tote mit der Innenseite - nicht mit der Außenform, aber mit der Innen­seite - des tierischen Lebens über seine ganze Welt hin.",
        "Das ist die unterste Grundlage, auf der er lebt, auf der er sich aufbaut, auf der er sein Dasein aufbaut.",
        "Und ein großes Stück Arbeit für den Toten besteht darinnen, sich in unmittelbare Beziehung zu der Welt des Tierisch-Lebendigen zu setzen."
      ],
      [
        "Wie wir uns hier von Kindheit auf in Beziehung setzen zu der Welt des Mineralisch-Toten, so leben wir uns nach dem Tode ein in eine all­mählich immer mehr an Breite und an Ausdehnung wachsende Bezie­hung zu der Welt des Tierisch-Lebendigen Die lernt der Tote nach allen Seiten kennen.",
        "Die lernt der Tote kennen, indem er stufenweise alle die Geheimnisse zu durchdringen hat, welche ihm hier so verborgen sind, wie seelisch dasjenige, was unter seinem Gefühlsleben schlummert; denn es ist dasselbe."
      ],
      [
        "Es kann selbstverständlich eine solche Frage wie diejenige, die ich jetzt aufwerfen will, nicht als eine ordentlich wissenschaftliche Frage gelten.",
        "Allein sie kann doch hinweisen auf irgend etwas, hinter dem reale Beziehungen sind.",
        "Gefragt werden kann, warum denn eigentlich dem Menschen hier in der physischen Welt manches verborgen ist beim Walten der alles durchdringenden Weltenweisheit.",
        "Man kann fragen, warum das verborgen ist, in das der Tote eingeweiht werden muß: in die Geheimnisse des Aufbaues der gesamten tierischen Welt."
      ],
      [
        "Gerade wenn man solch eine Frage zu beantworten versucht, greift man hinein in die tiefsten Geheimnisse des Daseins überhaupt.",
        "Und auch mit dieser Frage werden wir uns noch etwas zu befassen haben in diesen Betrachtungen.",
        "Zunächst aber haben wir den Blick darauf zu lenken, wie denn dieses Erfassen der Innenseite des tierischen Lebens eigentlich ist."
      ],
      [
        "Da könnte ich zunächst, um nicht theoretisch zu werden, vielleicht ausgehen von einer zeitgeschichtlichen Tatsache.",
        "Sie wissen, daß in einer gewissen äußerlichen Weise das menschliche historische Bewußt­sein in der neueren Zeit eine Umänderung erfahren hat durch den Darwinismus.",
        "Man hat versucht, die Kräfte zu finden, durch die sich die Organismen von sogenannten unvollkommenen zu vollkommenen Zuständen entwickeln.",
        "Die Darwinisten haben ja mancherlei genannt:"
      ],
      [
        "zunächst das Prinzip der zweckmäßigen Auslese, der Anpassung an die Verhältnisse und so weiter.",
        "Ich will Ihnen mit diesen Dingen, die Sie in jedem Handbuch des Darwinismus nachlesen können, sogar in jedem Lexikon, nicht kommen.",
        "Aber hinweisen will ich darauf, daß das äußerliche, abstrakte Prinzipien sind; daß für den, der tiefer blickt, gar nichts damit gesagt ist.",
        "Was eigentlich geschieht, ist nicht gezeigt, wenn man sagt: die Vervollkommnung geschieht dadurch, daß die Passendsten ausgewählt werden und die andern allmählich absterben, während die Passendsten die Überlebenden sind.",
        "Damit ist natürlich nichts gesagt über die Kräfte, über die Impulse, die eigentlich im tie­rischen Reiche leben, damit die Tiere erst sich vervollkommnen, aber auch in der gewöhnlichen gegenwärtigen Welt ihr Leben entsprechend zimmern können."
      ],
      [
        "Was wirkt denn wirklich in den Kräften, die vom Darwinismus als Selektionskräfte, als Kräfte einer reinen mechanischen Zweckmäßig­keit und so weiter angesprochen werden?",
        "Darinnen wirken die Toten.",
        "Es gehört zu den überraschendsten, eindringlichsten Erfahrungen, die im Kreise derToten gemacht werden können, wenn man darauf kommt, wie - ebenso wie es hier Schmiede und Tischler und andere Leute gibt, welche in der mechanischen Welt handwerksmäßig arbeiten und da­durch die physisch-sinnliche Grundlage des Lebens hier schaffen - in der geistigen Welt, vom Tierreich angefangen nach aufwärts, die Toten arbeiten.",
        "Während das tierische Reich hier in vieler Beziehung ein sol­ches ist, das der Mensch als ein niedriges empfindet, aber das minera­lische liegt noch niedriger, ist die Grundlage der Arbeit der Toten die Fortführung des tierischen Reiches.",
        "Daher lebt sich der Tote gewisser­maßen ein in alle die Geschicklichkeiten, die ihm hier für das Leben zwischen der Geburt und deni Tode verborgen sind."
      ],
      [
        "Hier kommen wir dann an den Punkt, der vielfach geheimgehalten wurde bis in unsere Zeit von den Brüderschaften, welche zum Teil mit Recht, zum Teil mit Unrecht glauben, daß die andern Menschen für solche Dinge nicht reif sind.",
        "Lernt man erkennen, was sich auf die tierische Natur bezieht in der Welt der Toten, hält man da Umschau, so ist das alles Gefühlsmäßig-Lebendiges.",
        "Der Mensch hat auch in sei­ner Seele Gefühlsmäßig-Lebendiges.",
        "Aber wie?",
        "Zwischen der Geburt"
      ],
      [
        "und dem Tod hat er es so, daß, wäre es nicht eingeschlossen in seine Unbewußtheit, der Mensch jederzeit dieses Gefühlsmäßig-Lebendige, das zwischen Geburt und Tod liegt, zum Verderb des übrigen Gefühls-mäßig-Lebendigen in der Welt verwenden könnte.",
        "Also bedenken Sie, was das eigentlich heißt!",
        "Sie leben selbst in Ihrem persönlichen Leben ein Gefühlsmäßig-Lebendiges, das aber eingeschlossen ist in die Gren­zen, die eben dem physischen Menschen gezogen sind.",
        "Hätten die Men­schen im allgemeinen das frei zur Verfügung - Anthroposophen werden in dieser Beziehung schon kultivierter sein -, so könnte der Mensch jederzeit die Kräfte, die da gerade verborgen sind, verwenden, um das um ihn liegende Gefühlsmäßig-Lebendige zu zerstören.",
        "Die tierische Natur im Menschen ist zunächst sogar im vorzüglichen Sinne eine zer­störerische, und sie ist sogar angelegt, zu zerstören.",
        "Und wenn der Mensch durch die Pforte des Todes gegangen ist, so ist es vor allen Dingen seine Aufgabe, alle die Impulse aus seiner Seele herauszu­reißen, welche dann in der Weise frei geworden sind, daß eigentlich sehr viel vorliegt von dem Bedürfnis, Lebendiges zu zerstören, Leben­diges zu töten.",
        "Und man kann sagen, zu dem, was der Tote lernen muß, gehört vor allen Dingen Achtung, Heiligachtung vor allem Le­bendigen."
      ],
      [
        "Diese Heiligachtung vor allem Lebendigen ist etwas, was man beob­achten kann als die selbstverständliche Entwickelung des Toten.",
        "So wie wir hier mit innigem Anteil ein Kind verfolgen, das sich von klein auf, allmählich, von Tag zu Tag, von Woche zu Woche selbstverständlich entwickelt, wie wir bei diesem Kinde verfolgen, wie das Seelische er­greift das Fleischlich-Leibliche, wie wir innige Freude haben an dem, was da geschieht, ohne daß der sogenannte freie Wille mitwirkt, was da rein durch seelisch-organische Kräfte geschieht: so hat man, wenn man den Toten von seinem Todestage an weiterhin durch sein Leben verfolgt, eben wiederum die Anschauung eines dem freien Willen zu­nächst entzogenen Einlebens in die Heilighaltung alles in der Umgebung befindlichen Lebendigen.",
        "Das ist gewissermaßen etwas, was wie eine Außenseite im Toten geschieht, so wie im Kinde es als Außenseite ge­schieht, daß es wächst, daß seine Züge ausdrucksvoller werden.",
        "Was so äußerlich am Kinde zu unserer Freude heranwächst, das wächst am"
      ],
      [
        "Toten heran, indem wir von ihm immer mehr und mehr ausstrahlend finden das so erhebende Heilighalten alles Lebendigen."
      ],
      [
        "Und in dieser Beziehung unterscheidet sich gewichtig das Leben nach dem Tode von dem Leben hier.",
        "Das Leben hier hat gerade das­jenige durch einen Schleier verdeckt, in das sich der Tote vertiefen muß.",
        "Wir nehmen die Welt durch unsere Sinne wahr und bilden uns gewisse Gesetze, die wir Naturgesetze nennen, nach denen wir dann unsere mechanischen Werkzeuge, unsere Geräte ringsherum bilden.",
        "Das, was wir nach dem Gesetze der Natur um uns herum als eine Welt aufbauen, ist im wesentlichen eine Welt des Todes.",
        "Selbst die Pflanze, selbst den Baum müssen wir töten, wenn wir sein Holz in den Dienst unserer mechanischen Künste stellen wollen.",
        "Und es gehört wiederum zu den erschütterndsten Erkenntnissen, daß im Grunde genommen alles dasjenige, was uns unsere Sinne lehren, wenn wir es anwenden durch unseren Willen, ein Zerstörendes ist und gar nicht anders sein kann als ein Zerstörendes."
      ],
      [
        "Ja, selbst wenn wir Künstlerisches schaffen, müssen wir uns betei­ligen an der Welt des Zerstörens.",
        "Was wir da aufbauen, geht erst aus der Zerstörung hervor.",
        "Eine gütige Weltenweisheit hat nur bewirkt, daß wir in der Regel zunächst noch als Menschen zurückscheuen, von der tierischen Natur nach aufwärts dasjenige in den Dienst der me­chanischen Kunst zu stellen, was da lebt.",
        "In einem gewissen höheren Sinne lebt aber in der Welt eigentlich alles.",
        "Das können Sie aus den verschiedenen Darstellungen, die im Laufe der Jahre gegeben worden sind, schon erkennen.",
        "Was tun wir aber eigentlich, indem wir das in den Dienst der mechanischen Kunst stellen, was wir durch unsere Sinne wahrnehmen und durch unseren Verstand kombinieren?",
        "Wir tragen fortwährend den Tod in das Leben hinein.",
        "Ein Raffaelisches Gemälde selbst kann nicht zustande kommen, ohne daß der Tod in das Leben hineingetragen wird.",
        "Bevor ein Raffaelisches Gemälde entsteht, lebt mehr, als da lebt, nachdem ein Raffaelisches Gemälde entstanden ist.",
        "Die Abschlagszahlung im Universum besteht nur darin, daß Seelen kommen, die dieses Raffaelische Gemälde genießen, die von diesem Raffaelischen Gemälde einen Impuls, einen Eindruck bekommen.",
        "Der Impuls, der Eindruck, den die schaffende oder die genießende Seele"
      ],
      [
        "bekommt, das ist dasjenige, was einzig und allein hinweghelfen kann über das Wirken des Todes - selbst in dem Fall, wenn die höchsten Güter, die sogenannten höchsten Güter der Menschheit hier auf dem physischen Plan geschaffen werden.",
        "Die Erde wird im wesentlichen dadurch zerstört werden, daß die Menschen den Tod mit ihren mecha­nischen Künsten in die Erde in einem so starken Maß hineintragen.",
        "Sie wird nicht mehr leben können, weil der Tod dasjenige überwiegt, was hinübergerettet werden kann über den Untergang der physischen Erde in die Jupiterwelt.",
        "Aber aus dem, was Menschen geschaffen haben, indem sie den Tod mit dem Leben verwoben haben, werden sie see­lischen Inhalt wiederum erhalten haben, den sie nun hinübertragen in die Jupiterwelt."
      ],
      [
        "Mehr als man sagen kann, webt sich durch menschliches Tun selber, dadurch daß dieses menschliche Tun zwischen Geburt und Tod innig verwoben ist mit dem Sinnessein, mehr als man sagen kann, webt sich fortwährend der Tod, webt sich fortwährend die Vernichtung des Lebendigen in das Leben ein.",
        "Allerdings beruht darauf, daß sich der Tod in das Leben einverwebt, die Entstehung des Bewußtseins über­haupt, und der Mensch würde gar nicht seine Erdenaufgabe in bezug auf das Bewußtsein absolvieren können, wenn er nicht dazu berufen wäre, den Tod in das Leben einzuweben.",
        "Selbst in unserem Innern töten wir in dem Augenblicke das Leben der Nerven, in welchem wir vorstellen wollen.",
        "Denn ein richtig lebender Nerv kann nicht vor-stellen.",
        "In unser Nervenleben hinein ersterben wir fortwährend, habe ich in öffentlichen Vorträgen in der letzten Zeit gesagt."
      ],
      [
        "In dieser Beziehung ist das Leben zwischen dem Tod und einer neuen Geburt ein völlig entgegengesetztes.",
        "Da handelt es sich darum, daß die Menschenseele vollständig sich einlebt in die Heilighaltung des Leben­digen, in die Durchdringung des Lebendigen mit immer mehr und mehr Leben.",
        "So hängt das Leben zwischen der Geburt und dem Tode zu­sammen mit dem Tode, und es hängt das Leben zwischen dem Tod und einer neuen Geburt zusammen mit dem Leben des Ganzen.",
        "Denn nur dadurch, daß der Mensch stirbt und von der geistigen Welt heraus seine Impulse in das Leben der Tiere sendet, lebt über die Erde hin eine tie­rische Welt."
      ],
      [
        "Das zweite, in das sich der Mensch nach dem Tode einlebt, ist das Reich der Menschenseelen selbst, gleichgültig, ob diese Menschenseelen hier im physischen Leibe verkörpert sind, oder ob sie selbst schon durch die Pforte des Todes gegangen sind.",
        "Der tierischen Welt gegenüber hat der Mensch nach dem Tode das Gefühl, wenn er eine Aktion ausführt: etwas hat Freude, oder etwas tut weh einem Wesen oder wenigstens einem Wesenhaften.",
        "Er weiß: Stößt du nur mit deiner Geisteskraft, so stößt du an Lebendiges."
      ],
      [
        "Hier ist es mehr ein allgemeines Leben und Weben im Lebendigen.",
        "Gegenüber der Bekanntschaft mit dem, was in unsere Sphäre, die menschliche Sphäre tritt, wenn wir tot sind, ist es so, daß, wenn eine andere Seele in Beziehung zu uns tritt, nachdem wir selbst durch die Pforte des Todes gegangen sind, wir dann fühlen, durch die Art, wie wir zu dieser Seele in Beziehung treten, wird unser eigenes Lebensgefühl entweder verstärkt oder abgeschwächt.",
        "Zu der einen Seele, gleichgültig ob sie hier auf Erden weilt oder drüben in den geistigen Welten, treten wir so in Beziehung, daß wir fühlen, wir werden stärker innerlich, nach einer gewissen Beziehung stärkt uns das Zusammensein mit der Seele, unsere inneren Kräfte werden stärker gemacht, wir leben gleich­sam mehr auf.",
        "Wir begegnen einer Seele und fühlen, wir wachen an ihr mehr auf, als wir ohne sie aufgewacht wären.",
        "Lebensinnigkeit fließt uns in einer gewissen Stärke zu durch die Bekanntschaft mit der einen Seele.",
        "Durch die Bekanntschaft mit einer andern Seele werden wir schwächer nach einer gewissen Kraftrichtung hin; sie dämpft unser Leben gewissermaßen ab.",
        "Und darin besteht das Zusammenleben mit Seelen, daß wir unser eigenes Leben lebendig wogen fühlen in der Ver­bindung mit andern Seelen."
      ],
      [
        "Wir leben als Menschen zwischen Geburt und Tod unser Gefühls-und Willensleben hin und wissen gar nicht, daß durch die Wogen un­seres Gefühls- und Willenslebens, die wir verschlafen und verträumen, die Totenseelen leben.",
        "Sie sind immer da; sie leben in unseren eigenen Gefühls- und Willenswogen, und sie leben so, daß sie mitleben dieses Leben.",
        "Während wir mit unseren Sinnen die Umwelt gewissermaßen doch als etwas Äußerliches erleben, leben in unseren Gefühlen und in unseren Willensimpulsen die Toten intimer mit uns verbunden, als wir"
      ],
      [
        "mit unserer Umwelt hier, insofern wir physisch verkörpert sind, innig verbunden leben."
      ],
      [
        "Aber das ist so, daß dieses Leben, dieses Erleben, besser gesagt, dieses Leben-Innesein der Toten langsam und allmählich sich entwickelt, und zwar nach Maßgabe derjenigen Verhältnisse, die angesponnen sind hier im Leben.",
        "Gewiß, wir sind nach dem Tode mit allen Seelen zusammen, das ist schon wahr, aber wir wissen nichts davon.",
        "Langsam und all­mählich stellen sich Beziehungen her, und zwar zu denjenigen Seelen, mit denen wir Beziehungen angeknüpft haben in dem Leben zwischen Geburt und Tod.",
        "Neue Beziehungen, ursprüngliche Beziehungen kann der Mensch zum Menschen nicht anknüpfen in dem Leben zwischen dem Tod und einer neuen Geburt, ursprünglich, unmittelbar kann er nicht anknüpfen.",
        "Wenn wir hier jemand lieb gehabt haben, oder einen gehaßt haben, also mit ihm in irgendeiner positiven oder negativen Verbindung waren, so tritt das wiederum aus einer grauen Geistestiefe im allmählichen Heraufleben des Lebens nach dem Tode auf, in der Art, wie ich es eben angedeutet habe, daß wir drinnen leben in diesen Seelen."
      ],
      [
        "Und so besteht ein großer Teil dieses Erlebens, dieses Leben-Inne-seins der Toten darinnen, daß allmählich auftaucht eben aus grauer Geistestiefe alles dasjenige, was an Banden da war aus dem letzten oder vorletzten oder früheren Leben, an Verhältnissen mit andern Seelen.",
        "Das kann sich weiter ausdehnen, dehnt sich für manchen Toten ver­hältnismäßig sehr früh, sehr bald nach dem Tode aus, doch mittelbar."
      ],
      [
        "Es kann so sein, daß jemand stirbt; er hat mit einer Seele, die ent­weder noch auf Erden weilt, oder in der geistigen Welt weilt, in Be­ziehung gestanden, in irgendeiner Beziehung.",
        "Diese Beziehung tritt in ihrer Wirklichkeit nach dem Tode ihm wiederum in der angedeuteten Weise entgegen.",
        "Aber diese Seele, mit der er in Beziehung gestanden hat, hat Beziehungen zu andern Seelen, mit denen er vielleicht nicht in Beziehung gestanden hat in irgendeinem Leben zwischen Geburt und Tod.",
        "Da, indirekt, mittelbar können dann auch solche Seelen an den sogenannten Toten herantreten, mit ihm in eine Beziehung treten.",
        "Nur allerdings sind das niemals unmittelbare Beziehungen, wie ich schon sagte, sondern sie sind immer vermittelt durch diejenigen Seelen, mit"
      ],
      [
        "denen man durch das physische Leben karmisch verbunden ist.",
        "Die Verbindung mit solchen Seelen, mit denen man die Verbindung nicht im physischen Leben begründet hat, ist doch immer eine ganz andere, und sie wird vermittelt durch die Seelen, mit denen man im physischen Leben in Beziehung gestanden hat."
      ],
      [
        "Sie können sich auch jetzt leicht vorstellen, daß zunächst die un­mittelbaren Beziehungen vorliegen, dann die mittelbaren Beziehungen.",
        "Dadurch aber, daß über die Erde hin doch die Seelen alle mehr oder weniger miteinander verbunden sind, der Mensch in dem langen Leben zwischen dem Tod und einer neuen Geburt wenigstens indirekt in viele Beziehungen hineingerät, lebt sich der Mensch in der Tat, wenn man die mittelbaren Beziehungen mitrechnet, in ein weites Miterleben mit andern Seelen hinein.",
        "Dieses Hineinleben in andere Seelen haben wir immer in uns, auch wenn wir hier auf der Erde stehen.",
        "Wir haben mit unzähligen Seelen immer wieder und wiederum gelebt in der geistigen Welt.",
        "Dieses Sich-Einsfühlen mit allen Seelen, das eine abstrakte Philo­sophie eben auch nur abstrakt behandelt und als abstraktes Einssein bespricht, das hat seine sehr konkrete Seite: es gibt eigentlich über die Erde hin kaum Seelen, mit denen nicht wenigstens eine entfernte, in­direkte Verbindung doch besteht."
      ],
      [
        "Diese Sache muß man so konkret fassen wie möglich, dann kommt man mit ihr zum Realen.",
        "Das, was der Tote so erlebt, ist also ein all­mähliches Hineinwachen, Hineinaufwachen in eine Welt, die aber zur Grundlage sein Karma im weiteren Sinne hat.",
        "Über diese Welt hin wird es gleichsam immer mehr innerlich licht und lichter, indem wir immer Reicheres und Reicheres erleben in diesem zweiten Reiche, das sich auf dem Reich des Tierischen aufbaut, wie unser Erleben mit dem Pflanzenreich auf dem Reich des Mineralischen.",
        "Reicheres und Rei­cheres erlebt man immer mehr."
      ],
      [
        "Dieses Erleben denken Sie sich in all den konkreten Beziehungen ausgestaltet, dann haben Sie vieles von dem, was die Seele der Toten zwischen Tod und neuer Geburt durchdringt.",
        "Denn verbunden mit diesem Erleben sind ja alle Gedanken, die uns karmisch irgendwie ver­binden mit den andern Seelen.",
        "Eine unendlich reiche Welt liegt dar­innen.",
        "Und es ist im wesentlichen - das können Sie schon aus dem"
      ],
      [
        "Zyklus über das Leben zwischen dem Tod und einer neuen Geburt ent­nehmen - in der ersten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt so, daß die Entwickelung eine mehr weisheitsvolle ist.",
        "Der Mensch lebt sich weisheitsvoll ein in die Verbindungen, die er sich allmählich wiederum herausholt aus grauer Geistestiefe; weisheitsvoll lebt er sich da hinein."
      ],
      [
        "Von dem, was ich in den Mysterien «Mitternachtsstunde des Da­seins» genannt habe, sind im wesentlichen die Fäden gezogen zu all den karmischen direkten und indirekten Verbindungen hin, zu denen sie zu ziehen sind.",
        "Dann kommt das Verarbeiten.",
        "Dann tritt in das mensch­liche Seelenleben ein mehr dem Willen ähnliches Kraftelement ein, aber nur ein ähnliches, nicht ein gleiches.",
        "Dieses dem Willen ähnliche Kraft-element macht den Menschen immer stärker und stärker.",
        "Es verstärkt vor allen Dingen die Impulse in ihm, welche zu dem weisheitsvollen Überblicken der Welt als willensmäßige Elemente, willensmäßige Im­pulse, als Kraftimpulse dazukommen."
      ],
      [
        "Nun tritt etwas Merkwürdiges ein.",
        "Im Menschen lebt ein gewisser Wille in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt auf.",
        "Wenn man diesen Willen beobachtet - man kann das insbesondere bei denjenigen Menschen, welche durch irgendwelche Verhältnisse ein gewissermaßen kurzes Leben zwischen dem Tod und einer neuen Geburt, ein abgekürztes Leben, haben -, da tritt eine merk­würdige Willensrichtung ein, die man etwa charakterisieren kann da­durch, daß man sagt: Es tritt der Wille ein, die Spuren des Lebens, die Spuren des Karma in einer gewissen Weise zu verwischen."
      ],
      [
        "Ich bitte Sie, das recht deutlich aufzufassen.",
        "Solch ein Wille: die Spuren des Karma zu verwischen, tritt im Menschen immer mehr und mehr auf.",
        "Dieses Verwischen der Spuren des Karma, das hängt mit den tiefsten Geheimnissen des Menschenlebens zusammen.",
        "Und würde der Mensch immerfort den vollen Überblick über die Weisheit haben, den er nach seinem Tode verhältnismäßig bald haben kann, so würden un­zählig viele Menschen lieber die Spuren ihres Daseins verwischen, als in neue Erdenleben eintreten.",
        "Die Verarbeitung der früheren Erden-leben im karmischen Zusammenhang, die wir ja vollziehen, kann sich im wesentlichen nur dadurch entwickeln, daß wir durch gewisse Wesen"
      ],
      [
        "der höheren Hierarchien in der zweiten Hälfte des Lebens zwischen dem Tod und einer neuen Geburt mit Bezug auf das Weisheitslicht ab-getrübt werden, abgelähmt werden, so daß wir unsere Tätigkeit, unsere Willensimpulse immer mehr und mehr einschränken.",
        "Und man kann nur sagen: das Ziel geht dann dahin, sie so einzuschränken, daß wir eben dasjenige schaffen, was sich dann in der Vererbungsströmung mit einem physischen Menschenleib verbinden und in diesem physischen Menschenleib sein Erdenschicksal ausleben kann."
      ],
      [
        "Vollständig versteht man diesen Gedanken allerdings nur dann, wenn man dieses Erdenschicksal selbst ins Auge faßt.",
        "Wie ist doch die­ses Erdenschicksal selbst etwas Traumhaftes für den Erdenmenschen!",
        "Er lebt sich ein als Kind in die Verhältnisse des Erdenlebens.",
        "Dasjenige, was man Schicksal nennt, tritt in Form von einzelnen Lebenserfahrun­gen an ihn heran.",
        "Aus dem Gewebe, das diese Lebenserfahrungen bilden, gestaltet sich etwas, was eigentlich wir selbst sind.",
        "Denn bedenken Sie alle, was Sie wären bis zu Ihrem heutigen Tage, wenn Sie nicht gerade das Schicksalsleben erlebt hätten, das Sie eben erlebt haben.",
        "Sie können schon sagen: Das, was ich als Schicksal erlebt habe, bin ich selber. -Denn ein ganz anderer wären Sie, wenn Sie eben etwas anderes als Schicksal erlebt hätten."
      ],
      [
        "Und dennoch, wie fremd fühlt der Mensch eigentlich sein Schick­sal, wie wenig fühlt er es mit dem verwoben, was er sein Ich nennt.",
        "In wie unzähligen Fällen fühlt sich das Ich eben getroffen vom Schick­sal.",
        "Warum?",
        "Weil das, was wir selbst aus uns heraus arbeiten an der Zimmerung unseres Schicksals, eben im Unterbewußten bleibt.",
        "Das, was wir erleben, das stellt sich hinein in die Welt der Sinneserfahrung und in die Welt der Vorstellungen.",
        "Es schlägt ja nur an unser Gefühls­leben an.",
        "Unser Gefühlsleben verhält sich dazu passiv.",
        "Aber aktiv aus diesem Gefühlsleben und aus diesem Leben der Willensimpulse kraftet dasjenige heraus, was wir nun auch mit dem Reich der Toten gemein­schaftlich haben.",
        "Was da aber herauskraftet und was wir selber tun ohne unser Bewußtsein, was wir wiederum verschlafen und verträu­men, das bildet unser Schicksal, das sind wir selbst.",
        "Was wir an unserem Schicksal tun, verschlafen und verträumen wir.",
        "Was wir an unserem Schicksal erleben, das leben wir allerdings wachend durch, aber eben"
      ],
      [
        "nur, weil es unterbewußt bleibt.",
        "Was bleibt da eigentlich unterbewußt?",
        "Dasjenige, was als Impulse herüberschlägt aus den früheren Erden-verkörperungen und aus dem Leben zwischen dem Tod und einer neuen Geburt auf eine rein geistige Weise aus dem Reiche, in dem die Toten auch sind, aus dem Reiche, das wir verträumen und verschlafen.",
        "Das sind zugleich Kräfte, die auch von uns selbst kommen.",
        "Es sind die Kräfte, mit denen wir unser Schicksal zimmern.",
        "Wir weben unser Schicksal aus demselben Reiche heraus, das mit uns gemeinschaftlich die Toten beleben."
      ],
      [
        "Denken Sie sich, wie wir da zusammenwachsen mit dem Reiche, von dem wir bis zu einem gewissen Grade jetzt wissen, wie es ver­schlafen wird: Wie wir es erleben! - obwohl wir noch nicht haben besprechen können, wie nun das Erleben gegenüber den Wesen der höheren Hierarchien ist; das wird auch noch dazukommen.",
        "Aber was man hervorrufen möchte durch eine solche Auseinandersetzung, wie ich sie eben gegeben habe, das ist, daß wir das Reich der sogenannten Toten hereinrücken in das Reich, in dem wir selber leben.",
        "Und bewußt werden wir uns, wie wir uns nur durch den Umstand von den Toten getrennt fühlen - aber nicht von ihnen getrennt sind -, daß wir unser Gefühlsleben, in dem die Toten auch sind, und unser Willensleben, in dem die Toten auch sind, verträumen und verschlafen."
      ],
      [
        "In dieser Welt, die wir verträumen und verschlafen, liegt aber noch etwas anderes, etwas, was der Mensch im gewöhnlichen Bewußtsein im Grunde gar nicht verfolgt.",
        "Er wird manchmal darauf aufmerksam, wenn es ihm in besonders eklatanten Fällen entgegentritt; aber das sind sensationelle einzelne Fälle, die nur auf dasjenige hinweisen, was das Leben fortwährend durchdringt und durchzieht.",
        "Wieviel werden Sie selbst von solchen Fällen gehört haben, wie der folgende ist!"
      ],
      [
        "Ein Mensch ist gewöhnt, täglich einen Spaziergang zu machen; et führt ihn auf einen Berghang.",
        "Da geht er täglich hin, das ist seine Lust.",
        "Eines Tages geht er wiederum hin.",
        "Plötzlich, während er geht, hört er etwas wie eine Stimme, die aber nicht physisch da ist, die ihm sagt:"
      ],
      [
        "Warum gehst du eigentlich diesen Weg?",
        "Kannst du diese Lust nicht auch entbehren? - So ungefähr sagt sie zu ihm.",
        "Da wird er stutzig.",
        "Er tritt etwas zur Seite und denkt nach über das, was ihm geschehen ist."
      ],
      [
        "In dem Augenblicke rollt ein Felsstück in die Tiefe, das ihn ganz sicher erschlagen hätte, wenn er nicht beiseite getreten wäre."
      ],
      [
        "Das ist eine wahre Geschichte, aber eine von denjenigen Geschichten, die eben nur sensationell, möchte ich sagen, auf etwas hinweisen, was fortwährend in unserem Leben da ist.",
        "Wie oft kommt es vor, daß Sie sich vornehmen, dies oder jenes zu tun.",
        "Sie werden durch dies oder jenes abgehalten.",
        "Malen Sie sich einmal aus,wie vieles manchmal anders geworden wäre im kleinen Erleben des Tages, wenn Sie einen Ausgang zu einer festgesetzten Stunde unternommen hätten, den Sie dann eine halbe Stunde später unternommen haben, weil Sie durch irgend etwas abgehalten worden sind, malen Sie sich aus, was da als Veränderung in Ihr Leben hineingekommen ist, was sogar als Veränderung in das Leben vieler anderer Menschen hineingekommen ist!",
        "Leicht kann man sich so etwas ausmalen.",
        "Nehmen wir einmal an: Sie haben sich vorgenommen, an einem Tage um viertel Vier Uhr nachmittags einen gewissen Gang zu machen, da wären Sie mit einem andern Menschen zusammengetrof­fen; dem hätten Sie eine Mitteilung gemacht, der wiederum diese Mit­teilung einem andern gemacht hätte.",
        "Sie machen, weil Sie zu spät kom­men, diese Mitteilung dem andern Menschen nicht und sehen: es wird hintangehalten, gewisse recht wichtige Dinge geschehen nicht."
      ],
      [
        "Da sieht man eine Weltenordnung, die anderer Art ist als die Wel­tenordnung, die wir als natürliche Notwendigkeit bezeichnen.",
        "Darin, daß jemand von dem Weiterschreiten auf einem Spazierwege abgehal­ten wird, weil er eine Stimme hört, durch die er beiseite tritt, was ver­hindert, daß er von einem Felsblock erschlagen wird, darin fühlen wir eine andere Weltenordnung hereinragen.",
        "Aber diese andere Welten-ordnung ragt ja in jedem Augenblick unseres Daseins herein, nur nicht durch so sensationelle Ereignisse.",
        "Der Mensch ist nur gewöhnt, den Blick aufs Sensationelle zu richten auch in diesen Dingen.",
        "Wir beach­ten jene Welt nur nicht.",
        "Warum?",
        "Weil wir den Blick richten auf das, was geschieht in unserem Leben und in unserer Umwelt, und nicht richten den Blick auf dasjenige, was nicht geschieht, was immerfort abgehalten wird, was immerfort zurückgehalten wird."
      ],
      [
        "Von einem gewissen Momente des geistigen Erlebens an kann das­jenige, was nicht geschieht, wovor wir gewissermaßen bewahrt oder"
      ],
      [
        "zurückgehalten worden sind, uns ebenso zum Bewußtsein kommen wie dasjenige, was geschehen ist.",
        "Nur kommt es uns zum Bewußtsein als eine andere Weltenordnung.",
        "Versuchen Sie, jene Weltenordnung sich einmal recht zur Seele zu bringen, indem Sie sich sagen: Der Mensch ist gewöhnt, nur auf dasjenige zu sehen, was geschieht, und nicht auf dasjenige, was vom Geschehen abgehalten wurde. - Was er da nicht beachtet, das hängt innig zusammen mit dem Reiche, in dem die Toten sind, in dem wir selbst sind mit unserem träumenden Fühlen, mit unserem schlafenden Willen.",
        "Wir trennen uns in uns selber von einer ganz andern Welt dadurch ab, daß auch in das wache Leben der Traum, der Schlaf hereinspielen.",
        "Und was da alles brodelt und lebt und webt unter der Grenze, die unser Vorstellen von unserem Fühlen trennt, das ist zugleich dasjenige, was einschließt die Geheimnisse, welche die Brücke bilden zwischen den sogenannten Lebendigen und den sogenann­ten Toten, aber auch die Brücke bilden zwischen dem Reich der Not­wendigkeit und dem Reich der Freiheit und dem sogenannten Zufall."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG Dornach, 10. Dezember 1917",
    "paragraphs": [
      "Ich Will kurz einige Tatsachen, die angeführt worden sind, noch ein­mal einleitungsweise berühren, weil wir sie für den Fortgang unserer Betrachtungen brauchen werden. Ich habe gesagt, daß im Menschen selber, auch seelisch, dasjenige liegt, was wir die Schwelle der gewöhn­lichen sinnlich-physischen Welt und der seelisch geistigen Welt nennen können.",
      "Und zwar so, daß wir im gewöhnlichen Wachbewußtsein, mit dem der Mensch ausgerüstet ist zwischen der Geburt und dem Tode, eigentlich nur in bezug auf die sinnlichen Wahrnehmungen völlig wachen, in bezug also auf die Wahrnehmung alles desjenigen, was durch unsere Sinne an uns herankommt, ferner in bezug auf alles das, was wir an Vorstellungen entwickeln, seien es Vorstellungen, die wir uns machen über das sinnlich Wahrgenommene, seien es Vorstellungen, die aus unserem Innern auftauchen zum Begreifen, zum Beleben der Welt. Schon eine ganz gewöhnliche Selbstbesinnung lehrt uns - keines­wegs ist dazu hellseherische Begabung notwendig -, daß das gewöhn­liche Menschheitsbewußtsein völlig wachend nicht mehr umfassen kann als das Gebiet des Vorstellungslebens und das Gebiet der Sinnes­wahrnehmungen.",
      "In unserer Seele selbst erleben wir außerdem unsere Gefühlswelt und unsere Willenswelt. Aber wir haben gesagt, daß wir unsere Gefühlswelt nur so durchleben, wie wir etwa einenTraum durch-leben, daß das Traumleben sich in das gewöhnliche Wachbewußtsein herein erstreckt, und wir eigentlich, indem wir fühlende Menschen sind, Träumer des Lebens sind.",
      "Denn auf dem Grunde des Gefühlslebens gehen Dinge vor, von denen das Wachbewußtsein im Vorstellen und im Sinneswahrnehmen nichts weiß. Noch weniger weiß das wache Be­wußtsein etwas von den wirklichen Vorgängen des Willenslebens.",
      "Das Gefühlsleben verträumt der Mensch im gewöhnlichen Wachbewußt­sein, das Willensleben verschläft er. So daß also unter unserem Vor­stellungsleben ein Reich lebt, in das wir selber eingebettet sind, und das uns nur zum Teil bekannt ist, uns nur bekannt ist durch die Wogen, die heraufschlagen über seine Oberfläche.",
      "Ferner haben wir betont, daß in diesem Reich, das also der Mensch verträumt, verschläft, mit uns gemeinschaftlich leben die Menschen­seelen in dem Dasein zwischen dem Tod und einer neuen Geburt. Wir sind also von den sogenannten Toten nur dadurch getrennt, daß wir nicht in der Lage sind, mit dem gewöhnlichen Bewußtsein wahrzu­nehmen, wie die Kräfte der Toten, das Leben der Toten, die Hand­lungen der Toten in unser eigenes Leben hereinspielen. Denn diese Kräfte, diese Handlungen der Toten durchdringen unser Gefühls­leben und unser Willensleben fortwährend. Wir leben also mit den Toten. Und es ist schon von Bedeutung, sich klarzumachen in dieser unserer Gegenwart, wie Geisteswissenschaft die Aufgabe hat, dieses Bewußtsein des Zusammengehörens mit den Totenseelen zu entwik­keln.",
      "Der Rest der Erdenentwickelung wird nicht verfließen können, wenn er zum Heile der Menschheit verfließen soll, ohne daß die Mensch­heit dieses lebendige Gefühl von dem Zusammensein mit den Toten ent­wickelt. Denn das Leben der Toten spielt auf mannigfaltigen Umwegen herein in das Leben der sogenannten Lebendigen.",
      "Und eben nicht umsonst ist im Verlauf der öffentlichen Vorträge aufmerksam darauf gemacht worden, wie das geschichtliche Leben, wie das, was der Mensch historisch durchlebt, sozial durchlebt, wie das, was er in bezug auf die ethischen Vorgänge unter den Menschen durch-lebt, eigentlich den Wert eines Traumes, eines Schlafes hat; daß die Impulse, welche der Mensch entwickelt, wenn er aus seiner Persönlich­keit herausgeht, wenn er also in der menschlichen Gemeinschaft wirkt, Traumes-, Schlafesimpulse sind.",
      "Die Menschen werden Geschichte ganz anders ansehen, wenn ihnen dies zum lebendigen Bewußtsein gekommen ist. Sie werden als Ge­schichte nicht mehr jene Fable convenue ansehen, welche man heute allgemein Geschichte nennt, sondern sie werden einsehen, daß geschicht­liches Leben nur verstanden werden kann, wenn in diesem geschicht­lichen Leben dasjenige gesucht wird, was für das gewöhnliche Bewußt­sein verträumt, verschlafen wird, in das aber hineinspielen zunächst, wie wir gesehen haben, die Impulse, die Taten, die Handlungen der sogenannten Toten. Es verweben sich die Handlungen der Toten mit",
      "dem Fühlen, mit den Willensimpulsen der sogenannten Lebendigen. Und das ist eigentlich Geschichte.",
      "Der Mensch hört nicht auf, tätig zu sein innerhalb der menschlichen Gemeinschaft, wenn er durch des Todes Pforte gegangen ist. Er fährt fort, tätig zu sein, wenn auch in einer andern Weise, als er hier im phy­sischen Leib tätig sein muß. Aber vieles von dem, wovon der Mensch wegen seiner Illusionen glaubt, daß er es tue, weil es aus seinen Ge­fühlen, aus seinen Willensimpulsen fließt, fließt in Wahrheit bis in unsere eigenen Tage, wo wir die entsprechenden Handlungen voll­ziehen, aus den Handlungen derer, die hinübergegangen sind.",
      "Zu wissen, daß der Mensch in dem Augenblicke, wo es sich um sein Leben in menschlicher Gemeinschaft handelt, auch in Gemeinschaft mit den Toten handelt, das wird ein Bedeutsames sein in der Entwicke­lung der Menschen in der Zukunft. Nur muß selbstverständlich ein solches Bewußtsein, das sich im wesentlichen auf das Gefühls-, auf das Willensleben bezieht, auch vom Fühlen und Willen erfaßt werden. Die abstrakten, die trockenen Vorstellungen werden das niemals erfassen können, aber Vorstellungen, die genommen sind aus dem Umfange der Geisteswissenschaft, die werden das erfassen können. Über vieles aller­dings werden sich die Menschen gewöhnen müssen, ganz andere Be­griffe zu bilden.",
      "Sie wissen ja alle, daß derjenige, der fest drinnensteht im Erfassen der geisteswissenschaftlichen Impulse, versuchen kann, mit denjenigen in Verbindung zu bleiben, die hingegangen sind durch die Pforte des Todes. Und an den Gedanken der Geisteswissenschaft, an den Ideen, die wir uns bilden über die Vorgänge in den geistigen Welten, haben wir solche Gedanken, die uns Erdenmenschen verständlich sind, die aber auch den toten Seelen verständlich sind. Und daraus ergibt sich dasjenige, was wir nennen: Vorlesen den Toten. Wenn wir gerade über Materien der Geisteswissenschaft im Gedanken an die Toten vorlesen, dann ist das ein wirkliches Gemeinschaftsleben mit den Toten. Denn die Geisteswissenschaft spricht eine Sprache, die den lebenden und den toten Seelen gemeinschaftlich ist. Aber es handelt sich darum, immer mehr und mehr gerade mit dem Gefühlsleben, mit dem durchleuch­teten Gefühlsleben an diese Dinge heranzukommen.",
      "Denn bedenken Sie einiges von dem, was ich gestern gesagt habe. Der Mensch lebt zwischen Tod und einer neuen Geburt in einer Um­gebung, die im wesentlichen ganz durchsetzt ist nicht nur von Leben­digkeit, sondern von fühlender Lebendigkeit.",
      "Das ist schon sein unter­stes Reich, habe ich gesagt. Wie für uns das fühllose Mineralreich das­jenige ist, was uns während unseres Sinnenlebens umgibt, ist um den Toten ein so geartetes Reich, daß, wenn er nur irgend etwas darin berührt, er Schmerz oder Freude hervorruft.",
      "So ist es bei den Toten, wie wenn wir im Leben wissen müßten, sobald wir irgendeinen Stein berühren, ein Baumblatt berühren, so rufen wir Gefühle hervor. Nichts kann der Tote tun, ohne daß er in seiner Umgebung Gefühle der Freude, Gefühle des Schmerzes, Gefühle der Spannung, Gefühle der Entspannung und so weiter hervorbringt.",
      "Indem wir mit dem Toten in einer Verbindung stehen, wie sie durch das Vorlesen gegeben ist, tritt dann für den Toten selbst jene Gemeinschaft auf, von der wir auch schon gesprochen haben, aber eben für diesen besonderen Fall des Vor-lesens. Dadurch tritt der Tote in Verbindung mit der Seele, die ihm hier vorliest, mit der Seele, die ihm irgendwie karmisch besonders verbunden ist.",
      "Und so wie der Tote in seinem untersten Reiche, das wir mit dem Tierreich in Verbindung bringen mußten, in einem solchen Verhältnisse steht, daß alles, was er tut, Freude, Leid und so weiter hervorbringt, so steht er mit alledem, was Zusammenhang mit Menschenseelen her­vorruft - seien es Menschenseelen, die hier auf der Erde leben, seien es Menschenseelen, die schon entkörpert sind und zwischen dem Tod und einer neuen Geburt leben -, in einer solchen Verbindung, daß er durch dasjenige, was in andern Seelen vorgeht, entweder ein gehobenes oder ein abgelähmtes Lebensgefühl erhält.",
      "Machen Sie sich das einmal klar. Wenn Sie hier einem sogenannten Lebenden vorlesen, so wissen Sie, der versteht in dem Sinne, wie man vom menschlichen Verständnisse spricht, dasjenige, was Sie ihm vor­lesen. Der Tote lebt darinnen, der Tote lebt in jedem Wort, das Sie ihm vorlesen, der Tote dringt ein in dasjenige, was durch Ihr eigenes Gemüt zieht. Der Tote lebt mit Ihnen, er lebt intensiver mit Ihnen, als er jemals in dem Leben zwischen der Geburt und dem Tode hat leben können. Das kann sich Ihnen steigern zum Verständnisse der Gemeinschaft",
      "mit dem Toten. Und diese Gemeinschaft mit dem Toten ist eigentlich, wenn sie gesucht wird, eine recht innige, und es steigert sich dieses Zusammensein mit dem Toten durch schauendes Bewußtsein.",
      "Tritt der Mensch wirklich bewußt in jenes Reich, das wir mit den Toten gemeinschaftlich bewohnen, dann ist der Verkehr mit den Toten so: Wenn Sie dem Toten zum Beispiel vorlesen oder vorsprechen, so hören Sie von ihm wie von einem Geisterecho das, was Sie selber vor­lesen. Mit solchen Begriffen muß man sich bekanntmachen, wenn man eine wirkliche Vorstellung von der konkreten geistigen Welt gewinnen will. Die Dinge sind in der geistigen Welt anders als hier. Hier hören Sie sich sprechen, oder wissen sich denkend, wenn Sie sprechen, oder wenn Sie denken. Sprechen Sie zu Toten, oder gehen Sie mit dem Toten denkend eine Verbindung ein, so tönt Ihnen, wenn die Ver­bindung bewußt ist im Schauen, aus dem Toten selbst dasjenige her­aus, was Sie zu ihm sprechen, oder was Sie denkend, vorstellend an ihn richten.",
      "Und weiter, wenn Sie dem Toten eine Mitteilung machen, dann haben Sie das Gefühl des innigen Verbundenseins. Und antwortet er Ihnen auf diese Mitteilung, dann ist das so, daß Sie zunächst das un­bestimmte Bewußtsein haben: der Tote spricht. Sie haben das unbe­stimmte Bewußtsein: der Tote hat gesprochen, und Sie müssen nun aus der eigenen Seele hervorholen, was er gesprochen hat. Sie erkennen daraus, wie notwendig es zu einem wirklichen Geistverkehr ist, von dem andern zu hören dasjenige, was man selber denkt und vorstellt, aus sich selbst zu hören dasjenige, was der andere spricht. Dies ist eine Art von Umkehrung des ganzen Verhältnisses von Wesen zu Wesen. Aber diese Umkehrung findet statt, wenn wirklich eingetreten wird in die geistige Welt.",
      "Weil die geistige Welt so durchaus anders ist als die physische Welt und die Menschen seit dem 15.Jahrhundert ungefähr sich nur Vor­stellungen bilden wollen, die im Sinne der physischen Welt geartet sind, so verlegen sich, verbauen sich die Menschen den Zugang zur geistigen Welt. Wenn die Menschen sich einmal herbeilassen werden, wenigstens die Möglichkeit vor sich hinzustellen, daß es eine Welt geben kann, die in gewissem Sinne, nicht in allem, entgegengesetzt ist derjenigen, die",
      "der Mensch hier die wahre Welt nennt, wenn sich die Menschen einmal werden Vorstellungen bilden wollen, die vielleicht demjenigen als die allerverrücktesten erscheinen, der nur in materialistischer Welt leben will, dann erst werden die Menschen ihre Seelen so umformen, daß sie die Möglichkeit erhalten, wirklich hineinzuschauen in diese geistige Welt, die ja fortwährend um uns herum ist. Es ist nicht so, daß die Menschen unbedingt durch ihre Natur getrennt wären von der gei­stigen Welt, sondern es ist deshalb so, weil die Menschen durch Ge­wöhnung, durch Vererbungsverhältnisse, seit dem 14. und 15.Jahr-hundert sich ganz abgewöhnt haben, andere Vorstellungen zu bilden als diejenigen, die hier der physischen Welt entlehnt sind.",
      "Ist es ja sogar so für die Kunst geworden! Was will denn die heutige Kunst noch anderes bilden als das, was nach dem Modell gebildet ist, was sich draußen in der Natur auch bildet. Selbst in der Kunst wollen die Men­schen nicht mehr gelten lassen das, was auch als ein Reales frei aufsteigt aus dem Geistesleben der Seele.",
      "Aber die Menschen können nicht das tilgen, was in den geschichtlichen Ereignissen, im ethisch-moralischen Zusammenleben, im sozialen Zusammenleben selbst als frei Aufsteigen­des wirksam und tätig ist, wenn sie es auch verträumen, verschlafen. Sobald der Mensch auch nur im geringsten über das hinausgeht, was seine ureigensten, persönlichsten Angelegenheiten sind - und er geht ja in jedem Augenblicke des Lebens darüber hinaus -, so wirkt durch seinen Arm, durch seine Hand, durch sein Wort, durch seinen Blick die geistige Welt, jene Welt, die wir - das muß ich immer wieder betonen -mit den Toten gemeinschaftlich haben.",
      "Der Tote lebt sich nun in das Reich ein, von dem ich schon gespro­chen habe, so wie wir uns, indem wir von Kindheit auf wachsen, in dem Leben zwischen Geburt und Tod einleben in die mineralische, die pflanzliche, die tierische, die menschliche physische Welt. Indem er sich so einlebt in das unterste Gebiet, das mit dem Tierreich etwas zu tun hat, in das zweite Gebiet, worin sich die Gemeinschaft ausbildet mit all den Seelen, mit denen der Tote in einer unmittelbaren oder mittelbaren karmischen Verbindung steht, so entwickelt sich der Tote zugleich dazu, sich in das Reich derjenigen Wesen einzuleben, die nun -wenn ich den Ausdruck gebrauchen darf, obwohl er nur etwas uneigentlich",
      "gemeint sein kann - über dem Menschen stehen: in das Reich der Angeloi, Archangeloi, Archai zunächst.",
      "Hier in der physischen Welt steht der Mensch da - viele betonen das so gern - als die Krone der physischen Schöpfung. Er fühlt sich hier als das höchste der Wesen. Die mineralischen Wesen sind die untersten, dann die pflanzlichen Wesen, dann die tierischen Wesen, dann er, der Mensch. Er fühlt sich als dem höchsten Reiche angehörig. So ist es nicht mit den Toten im geistigen Reiche; denn der Tote fühlt sich als sich anschließend an die Hierarchien, die über ihm stehen: die Hierarchien der Angeloi, Archangeloi, Archai und so weiter. So wie der Mensch sich hier in der physischen Welt gewissermaßen hervorgehend, hervor-wachsend fühlt aus dem mineralischen, dem pflanzlichen und tierischen Reiche, dem physischen Menschenreich, so fühlt der Tote sich gehalten, getragen von den über ihm stehenden Hierarchien in dem Leben zwi­schen dem Tod und einer neuen Geburt.",
      "Die Art, wie sich der Mensch allmählich in diese Reiche einlebt, in die Reiche der Angeloi, Archangeloi, Archai und so weiter, kann man so bezeichnen, daß man sagt: Man fühlt es wie ein Loslösen von sich. -Wiederum mussen wir uns eineVorstellung aneignen von diesen Dingen, die man in der physisch-sinnlichen Welt gar nicht gewinnen kann. In der physisch-sinnlichen Welt lernen wir, wenn wir von Kindheit auf wachsen, allmählich die Dinge kennen: zuerst unsere nächste Um­gebung, dann dasjenige, was im weiteren Umkreise unsere Lebenserfah­rung werden soll und so weiter. Wir lernen die Dinge so kennen, daß wir wissen, sie treten nach und nach an uns heran. Das ist nicht der Fall zwischen dem Tod und einer neuen Geburt. Da fühlen wir von dem Momente an, wo wir wissen, jetzt stehen wir in Beziehung zu den Angeloi, da fühlen wir, wie wenn wir mit ihnen schon von Ewigkeit her verbunden gewesen wären, wie wenn wir zu ihnen gehörten, eines mit ihnen wären, aber wie wenn das Bewußtsein sich nur dadurch ent­wickeln kann, daß wir gewissermaßen es dahin bringen, die Vorstel­lung von den Angeloi von uns loszulösen. Hier in der physischen Welt machen wir unsere Erfahrungen dadurch, daß wir die Vorstellungen aufnehmen. In der geistigen Welt machen wir unsere Erfahrungen da­durch, daß wir die Vorstellungen gewissermaßen aus uns heraus loslösen.",
      "Wir wissen, wir tragen sie in uns; und wir wissen, wir sind ganz und gar von ihnen erfüllt. Aber wir müssen sie, damit wir sie zum Be­wußtsein bringen können, von uns loslösen. Und so lösen wir los die Vorstellungen der Angeloi, der Archangeloi, der Archai.",
      "Gleichsam durch das unterste Reich ist der Mensch mit dem Wesen des Tierischen verbunden, das er in dem Sinne, wie ich es schon aus­einandergesetzt habe, zu bemeistern hat. Dann bildet sich das darüber-stehende Reich zu den Seelen, mit denen der Mensch karmisch, mittel­bar oder unmittelbar, verbunden ist. Dann erfährt er seine Beziehungen zum Reiche der Angeloi. Durch die Beziehungen zum Reiche der An­geloi tritt vieles von dem erst ein, was die rechten Beziehungen gibt zu dem Reich der Menschenseelen. So daß man eigentlich schwer für das Leben zwischen dem Tod und einer neuen Geburt trennen kann das, was der Mensch zu tun hat mit den andern Menschenseelen, und das­jenige, was er zu tun hat mit den Wesen aus dem Reiche der Angeloi. Menschen und Wesen aus dem Reiche der Angeloi, sie haben ja viel miteinander zu tun. Man kann sagen - obwohl man natürlich über diese Dinge nur vergleichsweise sprechen kann, obwohl alles Sprechen nur Andeutungen geben kann, ist es doch richtig -, so wie uns hier im physischen Leben die Erinnerung wieder hinträgt zu irgendeinem Er­eignisse, das wir durchgemacht haben, so trägt in dem Leben zwischen dem Tod und einer neuen Geburt ein Wesen aus dem Reich der Angeloi uns hin zu irgend etwas, zu dem wir getragen werden sollen, das wir erleben sollen. Die Wesen aus dem Reich der Angeloi sind eigentlich die Vermittler für alles dasjenige, was sich ausbildet im Leben des soge­nannten Toten.",
      "Und für alles das, was der Mensch zu tun hat zwischen dem Tod und einer neuen Geburt mit Bezug auf die Bemeisterung desTierischen -er hat ja seine eigene tierische Natur einzupflanzen seinem Geistwesen, damit er sich vorbereitet zu der nächsten Inkarnation -, helfen die Archangeloi. Dann, wenn Sie dies in rechtem Sinne erfassen, werden Sie sich sagen: Dadurch, daß der Mensch zwischen dem Tode und einer neuen Geburt teilhaftig wird des Verkehrs mit den Angeloi, kommt er in die Lage, seine rechten Beziehungen, seine rechten Verhältnisse an­zuknüpfen zu den Seelen, mit denen er eben Verhältnisse anknüpfen",
      "soll. Dadurch, daß der Mensch in Beziehung tritt zu dem Reich der Archangeloi, wird der Mensch in die Lage versetzt, in der richtigen Weise sich vorzubereiten für das, was ablaufen soll für die nächste Erdeninkarnation.",
      "Archai, jene Wesen, welche wir auch genannt haben die Wesen des Zeitgeistes, sind aber jene Wesen, welche gemeinschaftlich tätig sind in ihren Aufgaben für die Toten und für die Lebendigen. Aus meinen Andeutungen können Sie entnehmen, daß im wesentlichen der Tote mit den Angeloi so zu tun hat, daß diese sein Verhältnis zu andern Seelen regeln; daß die Archangeloi sein Verhältnis zu seinen fort­laufenden Inkarnationen regeln. Was der Tote zu tun hat mit jenen Wesen, die der Hierarchie der Archai angehören, das hat er - auf dem gemeinschaftlichen Boden mit den sogenannten Lebendigen - mit denen zu tun, die hier im physischen Leibe inkarniert sind. Der Tote in dem Leben zwischen dem Tod und einer neuen Geburt und der sogenannte Lebende hier zwischen der Geburt und dem Tode, sie sind in gleicher Weise eingebettet in etwas, was wie eine fortströmende Weltenweisheit und Weltenwillenstätigkeit gewoben wird von den Zeitgeistern. Was wiederum gewoben wird von den Zeitgeistern, ist Geschichte, ist ethisch­moralisches Leben eines Zeitalters, ist soziales Leben eines Zeitalters.",
      "Man möchte sagen, hinaufblicken können wir in das Reich des Gei­stes und uns sagen: Da sind die sogenannten Toten; was sie in ihrem Reiche erleben, das wird geregelt, insoferne dieses Erlebte ihre eigenen Angelegenheiten sind, durch die Angeloi und Archangeloi; was sie gemeinschaftlich mit den sogenannten Lebendigen erleben, das wird gewoben von den Wesen, die zu der Hierarchie der Archai gehören. -Und so können wir gar nicht fruchtbar im sozialen, im geschichtlichen, im ethisch-moralischen Leben wirken, ohne daß wir uns bewußt sind:",
      "dieses Wirken muß heraus erwachsen aus dem mit den Toten gemein­schaftlichen Elemente, muß heraus erwachsen aus dem Elemente der Archai, der Zeitgeister.",
      "Diese Zeitgeister aber lösen sich ab in bezug auf ihre Aufgabe. Dar­über haben wir ja wiederholt gesprochen. Ein solcher Zeitgeist webt an dem Geschicke des fortgehenden geschichtlichen Stromes und sozialen Stromes, des moralisch-ethischen Stromes im Menschengeschehen gewisse",
      "Jahrhunderte hindurch, dann wird er durch einen andern Zeit­geist abgelöst. Die Zeitpunkte, in denen ein Zeitgeist den andern ablöst, sind die allerwichtigsten für die Beobachtung desjenigen, was eigentlich innerhalb der Menschheitsentwickelung vor sich geht. Denn man kann die Menschheitsentwickelung nicht verstehen, wenn man nicht das lebendige Hereinwirken der Zeitgeister und damit überhaupt der gan­zen geistigen Welt ins Seelenauge faßt; man kann nicht verstehen, was eigentlich zwischen den Menschen geschieht, wenn man nicht das Reich des Geistes in Erwägung zieht.",
      "Abstrakt, höchst abstrakt denkt der Mensch über das, was sozial, was ethisch-moralisch, was historisch abläuft. So wie wenn die Ge­schichte ein fortlaufender Strom wäre, wo immer eins aufs andere folgt, so stellt sich der Mensch den Zeitenstrom des Geschehens vor. Er frägt: Warum sind die Ereignisse im Beginne des 20. Jahrhunderts so, wie sie eben sind? - Weil sie verursacht sind von den Ereignissen am Ende des 19. Jahrhunderts. Warum sind die Ereignisse am Ende des 19. Jahrhunderts so geworden? - Weil sie verursacht sind von denen in der Mitte des 19. Jahrhunderts. Und die Ereignisse in der Mitte des 19. Jahrhunderts sind wiederum verursacht durch die Ereignisse im Beginn des 19.Jahrhunderts und so fort.",
      "Es ist diese Betrachtungsweise, die immer die geschichtlichen Ereig­nisse als Folgen der unmittelbaren früheren betrachtet, ungefähr ebenso gescheit, als wenn der Bauer sagen würde: Der Weizen, den ich dieses Jahr haben werde, ist die Folge des Weizens vom vorigen Jahre, die Samen sind geblieben; der vom vorigen Jahre ist wiederum die Folge des Weizens vom vorvorigen Jahre. - Eins schließt sich an das andere, Wirkung immer an die Ursache. Es tut es nur nicht, wenn nicht nach­geholfen wird! Denn der Bauer muß selbstverständlich persönlich ein­greifen: er muß die Saat erst aussäen, damit Wirkung wird aus der Ursache. Von selbst wird nicht Wirkung aus der Ursache. Das ist von einem gewissen Gesichtspunkte aus sogar die schrecklichste Illusion des materialistischen Zeitalters, daß die Menschen glauben: Wirkung ent­steht aus der Ursache, und daß die Menschen sich nicht die einfachsten Gedanken bilden wollen über die Wahrheit dieser Verhältnisse.",
      "Ich habe Ihnen schon ein Ereignis als Beispiel angeführt, das ein",
      "sensationelles Ereignis im Menschengeschehen ist. Aber es ist schon ein­mal so, daß die Menschen auf solche sensationellen Ereignisse leichter hinschauen als auf die andern Ereignisse, die von genau derselben Art sind, aber sich stündlich, ja augenblicklich innerhalb unseres Lebens immer vollziehen. Ich habe Sie aufmerksam gemacht darauf, wie so ein Ereignis verfließt: Ein Mann ist gewöhnt, einen Spaziergang zu machen an einem Berghang; er machte ihn durch lange Zeit hindurch täglich. Aber eines Tages, als er ausgeht und an eine bestimmte Stelle des Weges kommt, hört er,wie wenn eine Stimme ihm zutönen würde, so ungefähr:",
      "Warum gehst du denn eigentlich diesen Weg? Hast du es denn nötig, dies zu tun? - so ähnlich. Er wird bedenklich, als er diese Stimme hört; er tritt zur Seite, besinnt sich einen Augenblick über das Sonderbare, das sich zugetragen hat - ein Felsblock stürzt herab, der ihn ganz sicher zerschmettert hätte, wenn er nicht durch die Stimme auf die Seite ge­treten wäre. Es ist ein sensationelles Ereignis. Aber für denjenigen, der die Welt nüchtern und doch geistig betrachtet, ist es nichts anderes als ein solches Ereignis, wie es sich in jedem Augenblick unseres Lebens vollzieht. Denn in jedem Augenblick unseres Lebens könnte auch etwas anderes geschehen, wenn dies oder jenes eintreten würde.",
      "Der sehr gescheite Mensch - wir wissen, daß insbesondere die Men­schen der Gegenwart sehr gescheit sind -, er sagt: Ja, warum ist jener Mensch nicht erschlagen worden? - Weil er weggegangen ist! Das ist die Ursache. - Na schön; aber nehmen wir an, er wäre nicht weg­gegangen, er wäre erschlagen worden, dann würde der sehr gescheite Mensch der Gegenwart sagen: Der herabfallende Stein ist die Ursache, daß der Mensch erschlagen worden ist.",
      "Rein formell, äußerlich abstrakt ist es schon richtig: der herabfallende Stein ist die Ursache, und der Tod des Menschen ist die Wir­kung. Aber daß die Ursache mit der Wirkung nicht das geringste zu tun hat - denn für den herabfallenden Stein gilt genau dasselbe, ob der Mensch dort steht oder nicht dort steht -, bedenkt er nicht. Diese Ur­sache hat mit jener Wirkung nicht das geringste zu tun. Bedenken Sie das nur einmal ordentlich und versuchen Sie sich dann klarzumachen, was es mit aller Ursache und Wirkung Rederei eigentlich für eine Be­deutung hat. Die sogenannte Ursache braucht nicht das geringste mit",
      "ihrer Wirkung zu tun zu haben. Für den Stein würde sich genau der­selbe Vorgang abspielen, wenn der Mann nicht dort stehen würde, und er spielt sich auch ab: es ist für den Stein, als der Mann gewarnt wurde und weggegangen ist, nichts anderes geschehen.",
      "Ich führte Ihnen dies als ein Beispiel dafür an, daß selbst in solchen äußeren, rein formellen Dingen die sogenannte Ursache mit der soge­nannten Wirkung nichts zu tun zu haben braucht. Diese ganze Betrach­tung von Ursache und Wirkung kommt nur aus der Abstraktion her­aus.",
      "Von Ursache und Wirkung zu sprechen ist nur angängig innerhalb gewisser Grenzen. Nehmen Sie einmal an: Sie hätten hier einen Baum, der habe hier seine Wurzeln. Nun, was in den Wurzeln vorgeht, das ist in einer gewissen Beziehung sicherlich als Ursache zu bezeichnen für dasjenige, was da wächst; was in den Zweigen vorgeht, ist mit einem gewissen Rechte wiederum als Ursache dessen zu bezeichnen, was in den Blättern vorgeht.",
      "Der Baum ist in einer gewissen Beziehung ein Ganzes; und die konkrete Lebensbetrachtung geht auf Totalitäten, geht aufs Ganze; die abstrakte Lebensbetrachtung, die schließt immer eins an das andere an, ohne sich zu fragen: wo ist ein abgeschlossenes Ganzes? Für die geistige Lebensbetrachtung ist dies aber von Bedeu­tung, daß man sich einer Ganzheit bewußt wird.",
      "Denn sehen Sie, da wo die äußersten Blätter sind, da hört der Baum auf mit dem, was innerliche Ursachen sind für das, was da geschieht. Wo die Blätter auf­hören, da hören auch die verursachenden Kräfte auf.",
      "Wo aber die ver­ursachenden Kräfte aufhören, da greift anderes ein. Hier, wo die ver­ursachenden Kräfte aufhören, sehen Sie, wenn Sie geistig schauen, den Baum umspielt von geistiger Wesenhaftigkeit, von geistigen Elementar­wesen, da beginnt, wenn ich so sagen darf, ein negativer Baum, der sich ins Unendliche hinausdehnt - nur scheinbar ins Unendliche, denn er verliert sich nach einiger Zeit.",
      "Dem Hinauswachsen des Baumes begeg­net ein elementarisches Dasein, und da, wo der Baum aufhört, berührt er sich mit elementarisch ihm entgegenwachsendem Dasein (Siehe Zeichnung S.66). So ist es in der Natur.",
      "Die Pflanze, indem sie aus dem Boden herausschießt, hört auf. Die Ursachen hören da auf, wo die Pflanze aufhört. Aber entgegen wächst der Pflanze aus dem Wel­tenall herein ein elementarisches Dasein.",
      "# Bild s. 66",
      "Ich habe das gerade in dem Vortrage, der über «Das menschliche Leben vom Gesichtspunkte der Geisteswissenschaft» handelt, in einigem angedeutet. Die Pflanzen wachsen aus dem Boden von unten hinauf, Geistiges wächst von oben herunter den Pflanzen entgegen. So ist es mit allen Wesen. Was Sie hier für die Natur sehen, das ist aber in allem Dasein vorhanden. Vor allen Dingen ist ein Strom des sozialen, des ethisch-moralischen, des geschichtlichen Werdens vorhanden. Nicht solch ein fortlaufender Strom ist das Geschehene, sondern ein Zeitgeist regiert während einer gewissen Zeit, ein anderer löst ihn ab, ein dritter löst ihn ab, ein vierter löst ihn ab und so weiter. Und an den Stellen, wo ein Zeitgeist den andern ablöst, da ist auch im Strom des fortlaufenden",
      "Geschehens ein Unterschied, ein solcher Einschnitt, daß man nicht sagen kann, das, was da folgt, ist unmittelbar die Wirkung des Vorhergehenden. Es ist nicht die Wirkung des Vorhergehenden in dem Sinne, wie man sich das vorstellt.",
      "Gesetzmäßigkeit ist schon vorhanden in dem, was aufeinander­folgend auftritt. Aber das, was man gewöhnlich «Notwendigkeit» nennt, das ist eine Illusion, wenn man es so auffaßt, wie es heute viel­fach aufgefaßt wird. Im Strom des fortlaufenden Geschehens ist es ganz ähnlich, wie an einer solchen Stelle, wo der Baum aufhört und der elementare Baum beginnt; nur daß in der Natur hier ein Wesen des sichtbaren, des sinnlich-sichtbaren Reiches angrenzt an ein Wesen, das sinnlich-unsichtbar ist, das übersinnlich ist. Hier grenzt Sinnliches an Übersinnliches - hier im Zeitenstrom grenzt Gleichartiges anein­ander; aber ebenso wie hier der sichtbare Baum aufhört und der Ele­mentarbaum beginnt, so hört auch hier etwas auf und ein anderes beginnt.",
      "So gibt es Zeitepochen, in denen die alten Geschehnisse, die alten Impulse, gewissermaßen aufhören und neue eingreifen müssen. Die Menschen halten sich in solchen Zeitpunkten oftmals gern an Luzifer und Ahriman und behalten das noch fort, was in Wirklichkeit eigent­lich schon abgestorben ist. Im Bewußtsein kann man das noch fort­behalten, was in Wirklichkeit schon abgestorben ist. In der Natur kann man das nicht. Wenn jemand im Jahre 1914 Ideen genau derselben Art kultivieren will, wie sie berechtigt waren im Jahre 1876, so kann er das. Er kann es aus dem Grunde, weil man im fortlaufenden Strom des Menschengeschehens, in dem man sich an Ahriman und Luzifer klam­mert, das Alte bewahren kann, wenn es auch in Wirklichkeit schon tot ist. Aber es ist dasselbe, wie wenn einer wollte den Baum fortwachsen machen, so daß er nicht aufhört, wenn er seine natürlichen Grenzen erreicht hat. In der Geschichte geschieht es in der Regel, daß die Men­schen nicht die Möglichkeit finden, einer neuen Epoche sich in der ent­sprechenden Weise richtig entgegenzusetzen, das heißt, sich in den Dienst des neuen Zeitgeistes zu stellen.",
      "Und gerade für unsere Zeit ist dies von einer ganz besonderen, durch­dringenden Wichtigkeit. Wir haben in diesen ganzen Wochen gesprochen",
      "# Bild s. 68",
      "von dem, was geistig Wichtiges vorgegangen ist 1879 (siehe Zeich­nung, gelb). Da ging ein Zeitalter zu Ende, da starb etwas ab, da hörte etwas auf, so wie hier der Baum aufhört. Von da ab war es notig - und ist bis heute nötig geblieben selbstverständlich, und wird noch lange nötig sein -, daß die Menschen zugänglich werden für Ideen, für Im­pulse, die aus der geistigen Welt selbst heraus sind. Sonst verwandelt sich das Alte in Ahrimanisches, Luziferisches.",
      "Mit dieser Andeutung ist außerordentlich Wichtiges gesagt. Denn in diesem letzten Drittel des 19. Jahrhunderts war eine wichtige Zeit in der Menschheitsentwickelung. Notwendig war es und notwendig bleibt es, daß die Menschen den Sinn sich eröffnen für das Eingreifen in­spirierter Ideen; dafür müssen die Menschen empfänglich werden. Allerdings, äußerlich betrachtet - wir werden aber die Sache nicht bloß äußerlich betrachten, sondern wir werden auf die tiefere, innerliche Betrachtung eingehen -, äußerlich betrachtet sieht es zunächst so aus, als wenn eigentlich die Dinge recht trostlos lägen. Aus den geistigen Welten kamen schon die Impulse, die hereinströmten, hereinwirkten, um die Menschen über diesen Zeitpunkt des Jahres 1879 hinwegzu­führen so, daß sie für inspirierte Ideen empfänglich geworden wären. Es waren schon die Impulse da, um den Menschen Gedanken zu geben, daß sie schon am Ende des 19. Jahrhunderts hätten das Bewußtsein haben können: Wenn wir geschichtlich, wenn wir sozial, wenn wir ethisch-moralisch im Gemeinschaftsleben handeln, dann handeln un­sere Toten, handeln die Angeloi, handeln die Archangeloi, handeln die Archai unter uns. - Das war da. Die Impulse waren da, sie gingen nur an vielen Menschen zunächst spurlos vorüber.",
      "Ich sage, ich betrachte das heute zunächst äußerlich, und es ist gut, wenn man sich einmal klarmacht, wie scheinbar spurlos alles vorbeigegangen",
      "ist. Wichtige Dinge, wichtige Impulse hat es schon gegeben in dieser zweiten Hälfte des 19.Jahrhunderts, indem Menschen schon da waren, die bedeutungsvolle Gedanken gehabt, bedeutungsvolle Ge­danken dargelegt haben. Wenn Sie diese heute ansehen werden, so sehen diese Gedanken selbst wie abstrakte Gedanken aus, gewiß, aber sie sind keine abstrakten Gedanken. Auch sollten sie nicht so bleiben, wie sie dazumal waren. Ich wiederhole es noch einmal, äußerlich ist das jetzt betrachtet, morgen werden wir es innerlich betrachten.",
      "In allen Gebieten der heutigen Bildungswelt fast war das so. Wer betrachtet denn zum Beispiel, um ein Nächstes zu berühren, hier in diesem Lande, der Schweiz, dieses Leben so, daß er sich sagen würde:",
      "Hier in der Schweiz hat im 19. Jahrhundert in den fünfziger Jahren ein Mensch gewirkt, der bedeutungsvolle Gedanken hegte, die dazumal allerdings philosophische Gedanken waren, die aber von zwei oder drei andern hätten aufgenommen, popularisiert zu werden gebraucht, und die in der fruchtbarsten Weise hätten eingreifen und die ganze Geschichte der Schweiz durchgeistigen können! - Wer denkt zum Bei­spiel, daß ein Geist ersten Ranges in Otto Heinrich Jäger geschaffen hat in der Mitte des 19. Jahrhunderts, einer der größten, die hier in der Schweiz geschaffen haben? Wo ist sein Name, wo wird er genannt? Wo ist das Bewußtsein dafür vorhanden, daß, obzwar die Gedanken abstrakt zutage getreten sind, scheinbar abstrakt, sie doch hätten kon­kret werden und blühen und Früchte tragen können, weil ein Größtes durch diesen Kopf gegangen ist, der an der Universität in Zürich ge­lehrt hat, der Bücher geschrieben hat über die wichtigsten Ideen - die hineingeweht werden müßten in das Leben der Gegenwart -, über die Idee der menschlichen Freiheit und ihres Zusammenhanges mit der ganzen geistigen Welt. Von einem andern Gesichtspunkte, als dann meine Freiheitsphilosophie in den neunziger Jahren entstanden ist, hat Otto Heinrich Jäger hier in der Schweiz eine Art Freiheitsphilosophie geschaffen.",
      "Und so wie dieses eine Beispiel könnte man überall unzählige an­führen. Es sprießten und sproßten die fruchtbarsten Ideen. Aber das, was man heute erzählt als Geistesgeschichte des 19.Jahrhunderts und bis in das 20. Jahrhundert herein, ist das Allerunbedeutendste von dem,",
      "was sich wirklich zugetragen hat. Und das Allerbedeutendste, das Ein­drücklichste, ist nicht berücksichtigt worden. So sehen die Dinge, zu­nächst äußerlich betrachtet, aus. Die innerlichen Betrachtungen wer­den vielleicht trostreicher aussehen."
    ],
    "sentences": [
      [
        "Ich Will kurz einige Tatsachen, die angeführt worden sind, noch ein­mal einleitungsweise berühren, weil wir sie für den Fortgang unserer Betrachtungen brauchen werden.",
        "Ich habe gesagt, daß im Menschen selber, auch seelisch, dasjenige liegt, was wir die Schwelle der gewöhn­lichen sinnlich-physischen Welt und der seelisch geistigen Welt nennen können."
      ],
      [
        "Und zwar so, daß wir im gewöhnlichen Wachbewußtsein, mit dem der Mensch ausgerüstet ist zwischen der Geburt und dem Tode, eigentlich nur in bezug auf die sinnlichen Wahrnehmungen völlig wachen, in bezug also auf die Wahrnehmung alles desjenigen, was durch unsere Sinne an uns herankommt, ferner in bezug auf alles das, was wir an Vorstellungen entwickeln, seien es Vorstellungen, die wir uns machen über das sinnlich Wahrgenommene, seien es Vorstellungen, die aus unserem Innern auftauchen zum Begreifen, zum Beleben der Welt.",
        "Schon eine ganz gewöhnliche Selbstbesinnung lehrt uns - keines­wegs ist dazu hellseherische Begabung notwendig -, daß das gewöhn­liche Menschheitsbewußtsein völlig wachend nicht mehr umfassen kann als das Gebiet des Vorstellungslebens und das Gebiet der Sinnes­wahrnehmungen."
      ],
      [
        "In unserer Seele selbst erleben wir außerdem unsere Gefühlswelt und unsere Willenswelt.",
        "Aber wir haben gesagt, daß wir unsere Gefühlswelt nur so durchleben, wie wir etwa einenTraum durch-leben, daß das Traumleben sich in das gewöhnliche Wachbewußtsein herein erstreckt, und wir eigentlich, indem wir fühlende Menschen sind, Träumer des Lebens sind."
      ],
      [
        "Denn auf dem Grunde des Gefühlslebens gehen Dinge vor, von denen das Wachbewußtsein im Vorstellen und im Sinneswahrnehmen nichts weiß.",
        "Noch weniger weiß das wache Be­wußtsein etwas von den wirklichen Vorgängen des Willenslebens."
      ],
      [
        "Das Gefühlsleben verträumt der Mensch im gewöhnlichen Wachbewußt­sein, das Willensleben verschläft er.",
        "So daß also unter unserem Vor­stellungsleben ein Reich lebt, in das wir selber eingebettet sind, und das uns nur zum Teil bekannt ist, uns nur bekannt ist durch die Wogen, die heraufschlagen über seine Oberfläche."
      ],
      [
        "Ferner haben wir betont, daß in diesem Reich, das also der Mensch verträumt, verschläft, mit uns gemeinschaftlich leben die Menschen­seelen in dem Dasein zwischen dem Tod und einer neuen Geburt.",
        "Wir sind also von den sogenannten Toten nur dadurch getrennt, daß wir nicht in der Lage sind, mit dem gewöhnlichen Bewußtsein wahrzu­nehmen, wie die Kräfte der Toten, das Leben der Toten, die Hand­lungen der Toten in unser eigenes Leben hereinspielen.",
        "Denn diese Kräfte, diese Handlungen der Toten durchdringen unser Gefühls­leben und unser Willensleben fortwährend.",
        "Wir leben also mit den Toten.",
        "Und es ist schon von Bedeutung, sich klarzumachen in dieser unserer Gegenwart, wie Geisteswissenschaft die Aufgabe hat, dieses Bewußtsein des Zusammengehörens mit den Totenseelen zu entwik­keln."
      ],
      [
        "Der Rest der Erdenentwickelung wird nicht verfließen können, wenn er zum Heile der Menschheit verfließen soll, ohne daß die Mensch­heit dieses lebendige Gefühl von dem Zusammensein mit den Toten ent­wickelt.",
        "Denn das Leben der Toten spielt auf mannigfaltigen Umwegen herein in das Leben der sogenannten Lebendigen."
      ],
      [
        "Und eben nicht umsonst ist im Verlauf der öffentlichen Vorträge aufmerksam darauf gemacht worden, wie das geschichtliche Leben, wie das, was der Mensch historisch durchlebt, sozial durchlebt, wie das, was er in bezug auf die ethischen Vorgänge unter den Menschen durch-lebt, eigentlich den Wert eines Traumes, eines Schlafes hat; daß die Impulse, welche der Mensch entwickelt, wenn er aus seiner Persönlich­keit herausgeht, wenn er also in der menschlichen Gemeinschaft wirkt, Traumes-, Schlafesimpulse sind."
      ],
      [
        "Die Menschen werden Geschichte ganz anders ansehen, wenn ihnen dies zum lebendigen Bewußtsein gekommen ist.",
        "Sie werden als Ge­schichte nicht mehr jene Fable convenue ansehen, welche man heute allgemein Geschichte nennt, sondern sie werden einsehen, daß geschicht­liches Leben nur verstanden werden kann, wenn in diesem geschicht­lichen Leben dasjenige gesucht wird, was für das gewöhnliche Bewußt­sein verträumt, verschlafen wird, in das aber hineinspielen zunächst, wie wir gesehen haben, die Impulse, die Taten, die Handlungen der sogenannten Toten.",
        "Es verweben sich die Handlungen der Toten mit"
      ],
      [
        "dem Fühlen, mit den Willensimpulsen der sogenannten Lebendigen.",
        "Und das ist eigentlich Geschichte."
      ],
      [
        "Der Mensch hört nicht auf, tätig zu sein innerhalb der menschlichen Gemeinschaft, wenn er durch des Todes Pforte gegangen ist.",
        "Er fährt fort, tätig zu sein, wenn auch in einer andern Weise, als er hier im phy­sischen Leib tätig sein muß.",
        "Aber vieles von dem, wovon der Mensch wegen seiner Illusionen glaubt, daß er es tue, weil es aus seinen Ge­fühlen, aus seinen Willensimpulsen fließt, fließt in Wahrheit bis in unsere eigenen Tage, wo wir die entsprechenden Handlungen voll­ziehen, aus den Handlungen derer, die hinübergegangen sind."
      ],
      [
        "Zu wissen, daß der Mensch in dem Augenblicke, wo es sich um sein Leben in menschlicher Gemeinschaft handelt, auch in Gemeinschaft mit den Toten handelt, das wird ein Bedeutsames sein in der Entwicke­lung der Menschen in der Zukunft.",
        "Nur muß selbstverständlich ein solches Bewußtsein, das sich im wesentlichen auf das Gefühls-, auf das Willensleben bezieht, auch vom Fühlen und Willen erfaßt werden.",
        "Die abstrakten, die trockenen Vorstellungen werden das niemals erfassen können, aber Vorstellungen, die genommen sind aus dem Umfange der Geisteswissenschaft, die werden das erfassen können.",
        "Über vieles aller­dings werden sich die Menschen gewöhnen müssen, ganz andere Be­griffe zu bilden."
      ],
      [
        "Sie wissen ja alle, daß derjenige, der fest drinnensteht im Erfassen der geisteswissenschaftlichen Impulse, versuchen kann, mit denjenigen in Verbindung zu bleiben, die hingegangen sind durch die Pforte des Todes.",
        "Und an den Gedanken der Geisteswissenschaft, an den Ideen, die wir uns bilden über die Vorgänge in den geistigen Welten, haben wir solche Gedanken, die uns Erdenmenschen verständlich sind, die aber auch den toten Seelen verständlich sind.",
        "Und daraus ergibt sich dasjenige, was wir nennen: Vorlesen den Toten.",
        "Wenn wir gerade über Materien der Geisteswissenschaft im Gedanken an die Toten vorlesen, dann ist das ein wirkliches Gemeinschaftsleben mit den Toten.",
        "Denn die Geisteswissenschaft spricht eine Sprache, die den lebenden und den toten Seelen gemeinschaftlich ist.",
        "Aber es handelt sich darum, immer mehr und mehr gerade mit dem Gefühlsleben, mit dem durchleuch­teten Gefühlsleben an diese Dinge heranzukommen."
      ],
      [
        "Denn bedenken Sie einiges von dem, was ich gestern gesagt habe.",
        "Der Mensch lebt zwischen Tod und einer neuen Geburt in einer Um­gebung, die im wesentlichen ganz durchsetzt ist nicht nur von Leben­digkeit, sondern von fühlender Lebendigkeit."
      ],
      [
        "Das ist schon sein unter­stes Reich, habe ich gesagt.",
        "Wie für uns das fühllose Mineralreich das­jenige ist, was uns während unseres Sinnenlebens umgibt, ist um den Toten ein so geartetes Reich, daß, wenn er nur irgend etwas darin berührt, er Schmerz oder Freude hervorruft."
      ],
      [
        "So ist es bei den Toten, wie wenn wir im Leben wissen müßten, sobald wir irgendeinen Stein berühren, ein Baumblatt berühren, so rufen wir Gefühle hervor.",
        "Nichts kann der Tote tun, ohne daß er in seiner Umgebung Gefühle der Freude, Gefühle des Schmerzes, Gefühle der Spannung, Gefühle der Entspannung und so weiter hervorbringt."
      ],
      [
        "Indem wir mit dem Toten in einer Verbindung stehen, wie sie durch das Vorlesen gegeben ist, tritt dann für den Toten selbst jene Gemeinschaft auf, von der wir auch schon gesprochen haben, aber eben für diesen besonderen Fall des Vor-lesens.",
        "Dadurch tritt der Tote in Verbindung mit der Seele, die ihm hier vorliest, mit der Seele, die ihm irgendwie karmisch besonders verbunden ist."
      ],
      [
        "Und so wie der Tote in seinem untersten Reiche, das wir mit dem Tierreich in Verbindung bringen mußten, in einem solchen Verhältnisse steht, daß alles, was er tut, Freude, Leid und so weiter hervorbringt, so steht er mit alledem, was Zusammenhang mit Menschenseelen her­vorruft - seien es Menschenseelen, die hier auf der Erde leben, seien es Menschenseelen, die schon entkörpert sind und zwischen dem Tod und einer neuen Geburt leben -, in einer solchen Verbindung, daß er durch dasjenige, was in andern Seelen vorgeht, entweder ein gehobenes oder ein abgelähmtes Lebensgefühl erhält."
      ],
      [
        "Machen Sie sich das einmal klar.",
        "Wenn Sie hier einem sogenannten Lebenden vorlesen, so wissen Sie, der versteht in dem Sinne, wie man vom menschlichen Verständnisse spricht, dasjenige, was Sie ihm vor­lesen.",
        "Der Tote lebt darinnen, der Tote lebt in jedem Wort, das Sie ihm vorlesen, der Tote dringt ein in dasjenige, was durch Ihr eigenes Gemüt zieht.",
        "Der Tote lebt mit Ihnen, er lebt intensiver mit Ihnen, als er jemals in dem Leben zwischen der Geburt und dem Tode hat leben können.",
        "Das kann sich Ihnen steigern zum Verständnisse der Gemeinschaft"
      ],
      [
        "mit dem Toten.",
        "Und diese Gemeinschaft mit dem Toten ist eigentlich, wenn sie gesucht wird, eine recht innige, und es steigert sich dieses Zusammensein mit dem Toten durch schauendes Bewußtsein."
      ],
      [
        "Tritt der Mensch wirklich bewußt in jenes Reich, das wir mit den Toten gemeinschaftlich bewohnen, dann ist der Verkehr mit den Toten so: Wenn Sie dem Toten zum Beispiel vorlesen oder vorsprechen, so hören Sie von ihm wie von einem Geisterecho das, was Sie selber vor­lesen.",
        "Mit solchen Begriffen muß man sich bekanntmachen, wenn man eine wirkliche Vorstellung von der konkreten geistigen Welt gewinnen will.",
        "Die Dinge sind in der geistigen Welt anders als hier.",
        "Hier hören Sie sich sprechen, oder wissen sich denkend, wenn Sie sprechen, oder wenn Sie denken.",
        "Sprechen Sie zu Toten, oder gehen Sie mit dem Toten denkend eine Verbindung ein, so tönt Ihnen, wenn die Ver­bindung bewußt ist im Schauen, aus dem Toten selbst dasjenige her­aus, was Sie zu ihm sprechen, oder was Sie denkend, vorstellend an ihn richten."
      ],
      [
        "Und weiter, wenn Sie dem Toten eine Mitteilung machen, dann haben Sie das Gefühl des innigen Verbundenseins.",
        "Und antwortet er Ihnen auf diese Mitteilung, dann ist das so, daß Sie zunächst das un­bestimmte Bewußtsein haben: der Tote spricht.",
        "Sie haben das unbe­stimmte Bewußtsein: der Tote hat gesprochen, und Sie müssen nun aus der eigenen Seele hervorholen, was er gesprochen hat.",
        "Sie erkennen daraus, wie notwendig es zu einem wirklichen Geistverkehr ist, von dem andern zu hören dasjenige, was man selber denkt und vorstellt, aus sich selbst zu hören dasjenige, was der andere spricht.",
        "Dies ist eine Art von Umkehrung des ganzen Verhältnisses von Wesen zu Wesen.",
        "Aber diese Umkehrung findet statt, wenn wirklich eingetreten wird in die geistige Welt."
      ],
      [
        "Weil die geistige Welt so durchaus anders ist als die physische Welt und die Menschen seit dem 15.Jahrhundert ungefähr sich nur Vor­stellungen bilden wollen, die im Sinne der physischen Welt geartet sind, so verlegen sich, verbauen sich die Menschen den Zugang zur geistigen Welt.",
        "Wenn die Menschen sich einmal herbeilassen werden, wenigstens die Möglichkeit vor sich hinzustellen, daß es eine Welt geben kann, die in gewissem Sinne, nicht in allem, entgegengesetzt ist derjenigen, die"
      ],
      [
        "der Mensch hier die wahre Welt nennt, wenn sich die Menschen einmal werden Vorstellungen bilden wollen, die vielleicht demjenigen als die allerverrücktesten erscheinen, der nur in materialistischer Welt leben will, dann erst werden die Menschen ihre Seelen so umformen, daß sie die Möglichkeit erhalten, wirklich hineinzuschauen in diese geistige Welt, die ja fortwährend um uns herum ist.",
        "Es ist nicht so, daß die Menschen unbedingt durch ihre Natur getrennt wären von der gei­stigen Welt, sondern es ist deshalb so, weil die Menschen durch Ge­wöhnung, durch Vererbungsverhältnisse, seit dem 14. und 15.Jahr-hundert sich ganz abgewöhnt haben, andere Vorstellungen zu bilden als diejenigen, die hier der physischen Welt entlehnt sind."
      ],
      [
        "Ist es ja sogar so für die Kunst geworden!",
        "Was will denn die heutige Kunst noch anderes bilden als das, was nach dem Modell gebildet ist, was sich draußen in der Natur auch bildet.",
        "Selbst in der Kunst wollen die Men­schen nicht mehr gelten lassen das, was auch als ein Reales frei aufsteigt aus dem Geistesleben der Seele."
      ],
      [
        "Aber die Menschen können nicht das tilgen, was in den geschichtlichen Ereignissen, im ethisch-moralischen Zusammenleben, im sozialen Zusammenleben selbst als frei Aufsteigen­des wirksam und tätig ist, wenn sie es auch verträumen, verschlafen.",
        "Sobald der Mensch auch nur im geringsten über das hinausgeht, was seine ureigensten, persönlichsten Angelegenheiten sind - und er geht ja in jedem Augenblicke des Lebens darüber hinaus -, so wirkt durch seinen Arm, durch seine Hand, durch sein Wort, durch seinen Blick die geistige Welt, jene Welt, die wir - das muß ich immer wieder betonen -mit den Toten gemeinschaftlich haben."
      ],
      [
        "Der Tote lebt sich nun in das Reich ein, von dem ich schon gespro­chen habe, so wie wir uns, indem wir von Kindheit auf wachsen, in dem Leben zwischen Geburt und Tod einleben in die mineralische, die pflanzliche, die tierische, die menschliche physische Welt.",
        "Indem er sich so einlebt in das unterste Gebiet, das mit dem Tierreich etwas zu tun hat, in das zweite Gebiet, worin sich die Gemeinschaft ausbildet mit all den Seelen, mit denen der Tote in einer unmittelbaren oder mittelbaren karmischen Verbindung steht, so entwickelt sich der Tote zugleich dazu, sich in das Reich derjenigen Wesen einzuleben, die nun -wenn ich den Ausdruck gebrauchen darf, obwohl er nur etwas uneigentlich"
      ],
      [
        "gemeint sein kann - über dem Menschen stehen: in das Reich der Angeloi, Archangeloi, Archai zunächst."
      ],
      [
        "Hier in der physischen Welt steht der Mensch da - viele betonen das so gern - als die Krone der physischen Schöpfung.",
        "Er fühlt sich hier als das höchste der Wesen.",
        "Die mineralischen Wesen sind die untersten, dann die pflanzlichen Wesen, dann die tierischen Wesen, dann er, der Mensch.",
        "Er fühlt sich als dem höchsten Reiche angehörig.",
        "So ist es nicht mit den Toten im geistigen Reiche; denn der Tote fühlt sich als sich anschließend an die Hierarchien, die über ihm stehen: die Hierarchien der Angeloi, Archangeloi, Archai und so weiter.",
        "So wie der Mensch sich hier in der physischen Welt gewissermaßen hervorgehend, hervor-wachsend fühlt aus dem mineralischen, dem pflanzlichen und tierischen Reiche, dem physischen Menschenreich, so fühlt der Tote sich gehalten, getragen von den über ihm stehenden Hierarchien in dem Leben zwi­schen dem Tod und einer neuen Geburt."
      ],
      [
        "Die Art, wie sich der Mensch allmählich in diese Reiche einlebt, in die Reiche der Angeloi, Archangeloi, Archai und so weiter, kann man so bezeichnen, daß man sagt: Man fühlt es wie ein Loslösen von sich. -Wiederum mussen wir uns eineVorstellung aneignen von diesen Dingen, die man in der physisch-sinnlichen Welt gar nicht gewinnen kann.",
        "In der physisch-sinnlichen Welt lernen wir, wenn wir von Kindheit auf wachsen, allmählich die Dinge kennen: zuerst unsere nächste Um­gebung, dann dasjenige, was im weiteren Umkreise unsere Lebenserfah­rung werden soll und so weiter.",
        "Wir lernen die Dinge so kennen, daß wir wissen, sie treten nach und nach an uns heran.",
        "Das ist nicht der Fall zwischen dem Tod und einer neuen Geburt.",
        "Da fühlen wir von dem Momente an, wo wir wissen, jetzt stehen wir in Beziehung zu den Angeloi, da fühlen wir, wie wenn wir mit ihnen schon von Ewigkeit her verbunden gewesen wären, wie wenn wir zu ihnen gehörten, eines mit ihnen wären, aber wie wenn das Bewußtsein sich nur dadurch ent­wickeln kann, daß wir gewissermaßen es dahin bringen, die Vorstel­lung von den Angeloi von uns loszulösen.",
        "Hier in der physischen Welt machen wir unsere Erfahrungen dadurch, daß wir die Vorstellungen aufnehmen.",
        "In der geistigen Welt machen wir unsere Erfahrungen da­durch, daß wir die Vorstellungen gewissermaßen aus uns heraus loslösen."
      ],
      [
        "Wir wissen, wir tragen sie in uns; und wir wissen, wir sind ganz und gar von ihnen erfüllt.",
        "Aber wir müssen sie, damit wir sie zum Be­wußtsein bringen können, von uns loslösen.",
        "Und so lösen wir los die Vorstellungen der Angeloi, der Archangeloi, der Archai."
      ],
      [
        "Gleichsam durch das unterste Reich ist der Mensch mit dem Wesen des Tierischen verbunden, das er in dem Sinne, wie ich es schon aus­einandergesetzt habe, zu bemeistern hat.",
        "Dann bildet sich das darüber-stehende Reich zu den Seelen, mit denen der Mensch karmisch, mittel­bar oder unmittelbar, verbunden ist.",
        "Dann erfährt er seine Beziehungen zum Reiche der Angeloi.",
        "Durch die Beziehungen zum Reiche der An­geloi tritt vieles von dem erst ein, was die rechten Beziehungen gibt zu dem Reich der Menschenseelen.",
        "So daß man eigentlich schwer für das Leben zwischen dem Tod und einer neuen Geburt trennen kann das, was der Mensch zu tun hat mit den andern Menschenseelen, und das­jenige, was er zu tun hat mit den Wesen aus dem Reiche der Angeloi.",
        "Menschen und Wesen aus dem Reiche der Angeloi, sie haben ja viel miteinander zu tun.",
        "Man kann sagen - obwohl man natürlich über diese Dinge nur vergleichsweise sprechen kann, obwohl alles Sprechen nur Andeutungen geben kann, ist es doch richtig -, so wie uns hier im physischen Leben die Erinnerung wieder hinträgt zu irgendeinem Er­eignisse, das wir durchgemacht haben, so trägt in dem Leben zwischen dem Tod und einer neuen Geburt ein Wesen aus dem Reich der Angeloi uns hin zu irgend etwas, zu dem wir getragen werden sollen, das wir erleben sollen.",
        "Die Wesen aus dem Reich der Angeloi sind eigentlich die Vermittler für alles dasjenige, was sich ausbildet im Leben des soge­nannten Toten."
      ],
      [
        "Und für alles das, was der Mensch zu tun hat zwischen dem Tod und einer neuen Geburt mit Bezug auf die Bemeisterung desTierischen -er hat ja seine eigene tierische Natur einzupflanzen seinem Geistwesen, damit er sich vorbereitet zu der nächsten Inkarnation -, helfen die Archangeloi.",
        "Dann, wenn Sie dies in rechtem Sinne erfassen, werden Sie sich sagen: Dadurch, daß der Mensch zwischen dem Tode und einer neuen Geburt teilhaftig wird des Verkehrs mit den Angeloi, kommt er in die Lage, seine rechten Beziehungen, seine rechten Verhältnisse an­zuknüpfen zu den Seelen, mit denen er eben Verhältnisse anknüpfen"
      ],
      [
        "soll.",
        "Dadurch, daß der Mensch in Beziehung tritt zu dem Reich der Archangeloi, wird der Mensch in die Lage versetzt, in der richtigen Weise sich vorzubereiten für das, was ablaufen soll für die nächste Erdeninkarnation."
      ],
      [
        "Archai, jene Wesen, welche wir auch genannt haben die Wesen des Zeitgeistes, sind aber jene Wesen, welche gemeinschaftlich tätig sind in ihren Aufgaben für die Toten und für die Lebendigen.",
        "Aus meinen Andeutungen können Sie entnehmen, daß im wesentlichen der Tote mit den Angeloi so zu tun hat, daß diese sein Verhältnis zu andern Seelen regeln; daß die Archangeloi sein Verhältnis zu seinen fort­laufenden Inkarnationen regeln.",
        "Was der Tote zu tun hat mit jenen Wesen, die der Hierarchie der Archai angehören, das hat er - auf dem gemeinschaftlichen Boden mit den sogenannten Lebendigen - mit denen zu tun, die hier im physischen Leibe inkarniert sind.",
        "Der Tote in dem Leben zwischen dem Tod und einer neuen Geburt und der sogenannte Lebende hier zwischen der Geburt und dem Tode, sie sind in gleicher Weise eingebettet in etwas, was wie eine fortströmende Weltenweisheit und Weltenwillenstätigkeit gewoben wird von den Zeitgeistern.",
        "Was wiederum gewoben wird von den Zeitgeistern, ist Geschichte, ist ethisch­moralisches Leben eines Zeitalters, ist soziales Leben eines Zeitalters."
      ],
      [
        "Man möchte sagen, hinaufblicken können wir in das Reich des Gei­stes und uns sagen: Da sind die sogenannten Toten; was sie in ihrem Reiche erleben, das wird geregelt, insoferne dieses Erlebte ihre eigenen Angelegenheiten sind, durch die Angeloi und Archangeloi; was sie gemeinschaftlich mit den sogenannten Lebendigen erleben, das wird gewoben von den Wesen, die zu der Hierarchie der Archai gehören. -Und so können wir gar nicht fruchtbar im sozialen, im geschichtlichen, im ethisch-moralischen Leben wirken, ohne daß wir uns bewußt sind:"
      ],
      [
        "dieses Wirken muß heraus erwachsen aus dem mit den Toten gemein­schaftlichen Elemente, muß heraus erwachsen aus dem Elemente der Archai, der Zeitgeister."
      ],
      [
        "Diese Zeitgeister aber lösen sich ab in bezug auf ihre Aufgabe.",
        "Dar­über haben wir ja wiederholt gesprochen.",
        "Ein solcher Zeitgeist webt an dem Geschicke des fortgehenden geschichtlichen Stromes und sozialen Stromes, des moralisch-ethischen Stromes im Menschengeschehen gewisse"
      ],
      [
        "Jahrhunderte hindurch, dann wird er durch einen andern Zeit­geist abgelöst.",
        "Die Zeitpunkte, in denen ein Zeitgeist den andern ablöst, sind die allerwichtigsten für die Beobachtung desjenigen, was eigentlich innerhalb der Menschheitsentwickelung vor sich geht.",
        "Denn man kann die Menschheitsentwickelung nicht verstehen, wenn man nicht das lebendige Hereinwirken der Zeitgeister und damit überhaupt der gan­zen geistigen Welt ins Seelenauge faßt; man kann nicht verstehen, was eigentlich zwischen den Menschen geschieht, wenn man nicht das Reich des Geistes in Erwägung zieht."
      ],
      [
        "Abstrakt, höchst abstrakt denkt der Mensch über das, was sozial, was ethisch-moralisch, was historisch abläuft.",
        "So wie wenn die Ge­schichte ein fortlaufender Strom wäre, wo immer eins aufs andere folgt, so stellt sich der Mensch den Zeitenstrom des Geschehens vor.",
        "Er frägt: Warum sind die Ereignisse im Beginne des 20.",
        "Jahrhunderts so, wie sie eben sind? - Weil sie verursacht sind von den Ereignissen am Ende des 19.",
        "Jahrhunderts.",
        "Warum sind die Ereignisse am Ende des 19.",
        "Jahrhunderts so geworden? - Weil sie verursacht sind von denen in der Mitte des 19.",
        "Jahrhunderts.",
        "Und die Ereignisse in der Mitte des 19.",
        "Jahrhunderts sind wiederum verursacht durch die Ereignisse im Beginn des 19.Jahrhunderts und so fort."
      ],
      [
        "Es ist diese Betrachtungsweise, die immer die geschichtlichen Ereig­nisse als Folgen der unmittelbaren früheren betrachtet, ungefähr ebenso gescheit, als wenn der Bauer sagen würde: Der Weizen, den ich dieses Jahr haben werde, ist die Folge des Weizens vom vorigen Jahre, die Samen sind geblieben; der vom vorigen Jahre ist wiederum die Folge des Weizens vom vorvorigen Jahre. - Eins schließt sich an das andere, Wirkung immer an die Ursache.",
        "Es tut es nur nicht, wenn nicht nach­geholfen wird!",
        "Denn der Bauer muß selbstverständlich persönlich ein­greifen: er muß die Saat erst aussäen, damit Wirkung wird aus der Ursache.",
        "Von selbst wird nicht Wirkung aus der Ursache.",
        "Das ist von einem gewissen Gesichtspunkte aus sogar die schrecklichste Illusion des materialistischen Zeitalters, daß die Menschen glauben: Wirkung ent­steht aus der Ursache, und daß die Menschen sich nicht die einfachsten Gedanken bilden wollen über die Wahrheit dieser Verhältnisse."
      ],
      [
        "Ich habe Ihnen schon ein Ereignis als Beispiel angeführt, das ein"
      ],
      [
        "sensationelles Ereignis im Menschengeschehen ist.",
        "Aber es ist schon ein­mal so, daß die Menschen auf solche sensationellen Ereignisse leichter hinschauen als auf die andern Ereignisse, die von genau derselben Art sind, aber sich stündlich, ja augenblicklich innerhalb unseres Lebens immer vollziehen.",
        "Ich habe Sie aufmerksam gemacht darauf, wie so ein Ereignis verfließt: Ein Mann ist gewöhnt, einen Spaziergang zu machen an einem Berghang; er machte ihn durch lange Zeit hindurch täglich.",
        "Aber eines Tages, als er ausgeht und an eine bestimmte Stelle des Weges kommt, hört er,wie wenn eine Stimme ihm zutönen würde, so ungefähr:"
      ],
      [
        "Warum gehst du denn eigentlich diesen Weg?",
        "Hast du es denn nötig, dies zu tun? - so ähnlich.",
        "Er wird bedenklich, als er diese Stimme hört; er tritt zur Seite, besinnt sich einen Augenblick über das Sonderbare, das sich zugetragen hat - ein Felsblock stürzt herab, der ihn ganz sicher zerschmettert hätte, wenn er nicht durch die Stimme auf die Seite ge­treten wäre.",
        "Es ist ein sensationelles Ereignis.",
        "Aber für denjenigen, der die Welt nüchtern und doch geistig betrachtet, ist es nichts anderes als ein solches Ereignis, wie es sich in jedem Augenblick unseres Lebens vollzieht.",
        "Denn in jedem Augenblick unseres Lebens könnte auch etwas anderes geschehen, wenn dies oder jenes eintreten würde."
      ],
      [
        "Der sehr gescheite Mensch - wir wissen, daß insbesondere die Men­schen der Gegenwart sehr gescheit sind -, er sagt: Ja, warum ist jener Mensch nicht erschlagen worden? - Weil er weggegangen ist!",
        "Das ist die Ursache. - Na schön; aber nehmen wir an, er wäre nicht weg­gegangen, er wäre erschlagen worden, dann würde der sehr gescheite Mensch der Gegenwart sagen: Der herabfallende Stein ist die Ursache, daß der Mensch erschlagen worden ist."
      ],
      [
        "Rein formell, äußerlich abstrakt ist es schon richtig: der herabfallende Stein ist die Ursache, und der Tod des Menschen ist die Wir­kung.",
        "Aber daß die Ursache mit der Wirkung nicht das geringste zu tun hat - denn für den herabfallenden Stein gilt genau dasselbe, ob der Mensch dort steht oder nicht dort steht -, bedenkt er nicht.",
        "Diese Ur­sache hat mit jener Wirkung nicht das geringste zu tun.",
        "Bedenken Sie das nur einmal ordentlich und versuchen Sie sich dann klarzumachen, was es mit aller Ursache und Wirkung Rederei eigentlich für eine Be­deutung hat.",
        "Die sogenannte Ursache braucht nicht das geringste mit"
      ],
      [
        "ihrer Wirkung zu tun zu haben.",
        "Für den Stein würde sich genau der­selbe Vorgang abspielen, wenn der Mann nicht dort stehen würde, und er spielt sich auch ab: es ist für den Stein, als der Mann gewarnt wurde und weggegangen ist, nichts anderes geschehen."
      ],
      [
        "Ich führte Ihnen dies als ein Beispiel dafür an, daß selbst in solchen äußeren, rein formellen Dingen die sogenannte Ursache mit der soge­nannten Wirkung nichts zu tun zu haben braucht.",
        "Diese ganze Betrach­tung von Ursache und Wirkung kommt nur aus der Abstraktion her­aus."
      ],
      [
        "Von Ursache und Wirkung zu sprechen ist nur angängig innerhalb gewisser Grenzen.",
        "Nehmen Sie einmal an: Sie hätten hier einen Baum, der habe hier seine Wurzeln.",
        "Nun, was in den Wurzeln vorgeht, das ist in einer gewissen Beziehung sicherlich als Ursache zu bezeichnen für dasjenige, was da wächst; was in den Zweigen vorgeht, ist mit einem gewissen Rechte wiederum als Ursache dessen zu bezeichnen, was in den Blättern vorgeht."
      ],
      [
        "Der Baum ist in einer gewissen Beziehung ein Ganzes; und die konkrete Lebensbetrachtung geht auf Totalitäten, geht aufs Ganze; die abstrakte Lebensbetrachtung, die schließt immer eins an das andere an, ohne sich zu fragen: wo ist ein abgeschlossenes Ganzes?",
        "Für die geistige Lebensbetrachtung ist dies aber von Bedeu­tung, daß man sich einer Ganzheit bewußt wird."
      ],
      [
        "Denn sehen Sie, da wo die äußersten Blätter sind, da hört der Baum auf mit dem, was innerliche Ursachen sind für das, was da geschieht.",
        "Wo die Blätter auf­hören, da hören auch die verursachenden Kräfte auf."
      ],
      [
        "Wo aber die ver­ursachenden Kräfte aufhören, da greift anderes ein.",
        "Hier, wo die ver­ursachenden Kräfte aufhören, sehen Sie, wenn Sie geistig schauen, den Baum umspielt von geistiger Wesenhaftigkeit, von geistigen Elementar­wesen, da beginnt, wenn ich so sagen darf, ein negativer Baum, der sich ins Unendliche hinausdehnt - nur scheinbar ins Unendliche, denn er verliert sich nach einiger Zeit."
      ],
      [
        "Dem Hinauswachsen des Baumes begeg­net ein elementarisches Dasein, und da, wo der Baum aufhört, berührt er sich mit elementarisch ihm entgegenwachsendem Dasein (Siehe Zeichnung S.66).",
        "So ist es in der Natur."
      ],
      [
        "Die Pflanze, indem sie aus dem Boden herausschießt, hört auf.",
        "Die Ursachen hören da auf, wo die Pflanze aufhört.",
        "Aber entgegen wächst der Pflanze aus dem Wel­tenall herein ein elementarisches Dasein."
      ],
      [
        "# Bild s. 66"
      ],
      [
        "Ich habe das gerade in dem Vortrage, der über «Das menschliche Leben vom Gesichtspunkte der Geisteswissenschaft» handelt, in einigem angedeutet.",
        "Die Pflanzen wachsen aus dem Boden von unten hinauf, Geistiges wächst von oben herunter den Pflanzen entgegen.",
        "So ist es mit allen Wesen.",
        "Was Sie hier für die Natur sehen, das ist aber in allem Dasein vorhanden.",
        "Vor allen Dingen ist ein Strom des sozialen, des ethisch-moralischen, des geschichtlichen Werdens vorhanden.",
        "Nicht solch ein fortlaufender Strom ist das Geschehene, sondern ein Zeitgeist regiert während einer gewissen Zeit, ein anderer löst ihn ab, ein dritter löst ihn ab, ein vierter löst ihn ab und so weiter.",
        "Und an den Stellen, wo ein Zeitgeist den andern ablöst, da ist auch im Strom des fortlaufenden"
      ],
      [
        "Geschehens ein Unterschied, ein solcher Einschnitt, daß man nicht sagen kann, das, was da folgt, ist unmittelbar die Wirkung des Vorhergehenden.",
        "Es ist nicht die Wirkung des Vorhergehenden in dem Sinne, wie man sich das vorstellt."
      ],
      [
        "Gesetzmäßigkeit ist schon vorhanden in dem, was aufeinander­folgend auftritt.",
        "Aber das, was man gewöhnlich «Notwendigkeit» nennt, das ist eine Illusion, wenn man es so auffaßt, wie es heute viel­fach aufgefaßt wird.",
        "Im Strom des fortlaufenden Geschehens ist es ganz ähnlich, wie an einer solchen Stelle, wo der Baum aufhört und der elementare Baum beginnt; nur daß in der Natur hier ein Wesen des sichtbaren, des sinnlich-sichtbaren Reiches angrenzt an ein Wesen, das sinnlich-unsichtbar ist, das übersinnlich ist.",
        "Hier grenzt Sinnliches an Übersinnliches - hier im Zeitenstrom grenzt Gleichartiges anein­ander; aber ebenso wie hier der sichtbare Baum aufhört und der Ele­mentarbaum beginnt, so hört auch hier etwas auf und ein anderes beginnt."
      ],
      [
        "So gibt es Zeitepochen, in denen die alten Geschehnisse, die alten Impulse, gewissermaßen aufhören und neue eingreifen müssen.",
        "Die Menschen halten sich in solchen Zeitpunkten oftmals gern an Luzifer und Ahriman und behalten das noch fort, was in Wirklichkeit eigent­lich schon abgestorben ist.",
        "Im Bewußtsein kann man das noch fort­behalten, was in Wirklichkeit schon abgestorben ist.",
        "In der Natur kann man das nicht.",
        "Wenn jemand im Jahre 1914 Ideen genau derselben Art kultivieren will, wie sie berechtigt waren im Jahre 1876, so kann er das.",
        "Er kann es aus dem Grunde, weil man im fortlaufenden Strom des Menschengeschehens, in dem man sich an Ahriman und Luzifer klam­mert, das Alte bewahren kann, wenn es auch in Wirklichkeit schon tot ist.",
        "Aber es ist dasselbe, wie wenn einer wollte den Baum fortwachsen machen, so daß er nicht aufhört, wenn er seine natürlichen Grenzen erreicht hat.",
        "In der Geschichte geschieht es in der Regel, daß die Men­schen nicht die Möglichkeit finden, einer neuen Epoche sich in der ent­sprechenden Weise richtig entgegenzusetzen, das heißt, sich in den Dienst des neuen Zeitgeistes zu stellen."
      ],
      [
        "Und gerade für unsere Zeit ist dies von einer ganz besonderen, durch­dringenden Wichtigkeit.",
        "Wir haben in diesen ganzen Wochen gesprochen"
      ],
      [
        "# Bild s. 68"
      ],
      [
        "von dem, was geistig Wichtiges vorgegangen ist 1879 (siehe Zeich­nung, gelb).",
        "Da ging ein Zeitalter zu Ende, da starb etwas ab, da hörte etwas auf, so wie hier der Baum aufhört.",
        "Von da ab war es notig - und ist bis heute nötig geblieben selbstverständlich, und wird noch lange nötig sein -, daß die Menschen zugänglich werden für Ideen, für Im­pulse, die aus der geistigen Welt selbst heraus sind.",
        "Sonst verwandelt sich das Alte in Ahrimanisches, Luziferisches."
      ],
      [
        "Mit dieser Andeutung ist außerordentlich Wichtiges gesagt.",
        "Denn in diesem letzten Drittel des 19.",
        "Jahrhunderts war eine wichtige Zeit in der Menschheitsentwickelung.",
        "Notwendig war es und notwendig bleibt es, daß die Menschen den Sinn sich eröffnen für das Eingreifen in­spirierter Ideen; dafür müssen die Menschen empfänglich werden.",
        "Allerdings, äußerlich betrachtet - wir werden aber die Sache nicht bloß äußerlich betrachten, sondern wir werden auf die tiefere, innerliche Betrachtung eingehen -, äußerlich betrachtet sieht es zunächst so aus, als wenn eigentlich die Dinge recht trostlos lägen.",
        "Aus den geistigen Welten kamen schon die Impulse, die hereinströmten, hereinwirkten, um die Menschen über diesen Zeitpunkt des Jahres 1879 hinwegzu­führen so, daß sie für inspirierte Ideen empfänglich geworden wären.",
        "Es waren schon die Impulse da, um den Menschen Gedanken zu geben, daß sie schon am Ende des 19.",
        "Jahrhunderts hätten das Bewußtsein haben können: Wenn wir geschichtlich, wenn wir sozial, wenn wir ethisch-moralisch im Gemeinschaftsleben handeln, dann handeln un­sere Toten, handeln die Angeloi, handeln die Archangeloi, handeln die Archai unter uns. - Das war da.",
        "Die Impulse waren da, sie gingen nur an vielen Menschen zunächst spurlos vorüber."
      ],
      [
        "Ich sage, ich betrachte das heute zunächst äußerlich, und es ist gut, wenn man sich einmal klarmacht, wie scheinbar spurlos alles vorbeigegangen"
      ],
      [
        "ist.",
        "Wichtige Dinge, wichtige Impulse hat es schon gegeben in dieser zweiten Hälfte des 19.Jahrhunderts, indem Menschen schon da waren, die bedeutungsvolle Gedanken gehabt, bedeutungsvolle Ge­danken dargelegt haben.",
        "Wenn Sie diese heute ansehen werden, so sehen diese Gedanken selbst wie abstrakte Gedanken aus, gewiß, aber sie sind keine abstrakten Gedanken.",
        "Auch sollten sie nicht so bleiben, wie sie dazumal waren.",
        "Ich wiederhole es noch einmal, äußerlich ist das jetzt betrachtet, morgen werden wir es innerlich betrachten."
      ],
      [
        "In allen Gebieten der heutigen Bildungswelt fast war das so.",
        "Wer betrachtet denn zum Beispiel, um ein Nächstes zu berühren, hier in diesem Lande, der Schweiz, dieses Leben so, daß er sich sagen würde:"
      ],
      [
        "Hier in der Schweiz hat im 19.",
        "Jahrhundert in den fünfziger Jahren ein Mensch gewirkt, der bedeutungsvolle Gedanken hegte, die dazumal allerdings philosophische Gedanken waren, die aber von zwei oder drei andern hätten aufgenommen, popularisiert zu werden gebraucht, und die in der fruchtbarsten Weise hätten eingreifen und die ganze Geschichte der Schweiz durchgeistigen können! - Wer denkt zum Bei­spiel, daß ein Geist ersten Ranges in Otto Heinrich Jäger geschaffen hat in der Mitte des 19.",
        "Jahrhunderts, einer der größten, die hier in der Schweiz geschaffen haben?",
        "Wo ist sein Name, wo wird er genannt?",
        "Wo ist das Bewußtsein dafür vorhanden, daß, obzwar die Gedanken abstrakt zutage getreten sind, scheinbar abstrakt, sie doch hätten kon­kret werden und blühen und Früchte tragen können, weil ein Größtes durch diesen Kopf gegangen ist, der an der Universität in Zürich ge­lehrt hat, der Bücher geschrieben hat über die wichtigsten Ideen - die hineingeweht werden müßten in das Leben der Gegenwart -, über die Idee der menschlichen Freiheit und ihres Zusammenhanges mit der ganzen geistigen Welt.",
        "Von einem andern Gesichtspunkte, als dann meine Freiheitsphilosophie in den neunziger Jahren entstanden ist, hat Otto Heinrich Jäger hier in der Schweiz eine Art Freiheitsphilosophie geschaffen."
      ],
      [
        "Und so wie dieses eine Beispiel könnte man überall unzählige an­führen.",
        "Es sprießten und sproßten die fruchtbarsten Ideen.",
        "Aber das, was man heute erzählt als Geistesgeschichte des 19.Jahrhunderts und bis in das 20.",
        "Jahrhundert herein, ist das Allerunbedeutendste von dem,"
      ],
      [
        "was sich wirklich zugetragen hat.",
        "Und das Allerbedeutendste, das Ein­drücklichste, ist nicht berücksichtigt worden.",
        "So sehen die Dinge, zu­nächst äußerlich betrachtet, aus.",
        "Die innerlichen Betrachtungen wer­den vielleicht trostreicher aussehen."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG Dornach, 11. Dezember 1917",
    "paragraphs": [
      "Das Thema, das wir jetzt besprechen, ist sehr umfassend, und es wird heute nicht so weit geführt werden können, als ich eigentlich gewollt habe, aber wir setzen ja diese Betrachtungen weiter fort. Denn ich möchte gerade in diesen Betrachtungen vor allem die Grundlage zum Verständnis von Freiheit und Notwendigkeit so legen, daß Sie ein Bild bekommen von dem, was vom okkultistischen Standpunkte in Betracht kommt, um den Verlauf des sozialen und des geschichtlichen, des ethisch-moralischen Menschenlebens zu verstehen.",
      "Wir haben betont, daß für das Leben zwischen der Geburt und dem Tode völlig wachend eigentlich nur das durchlebt wird, was wir in der Sinneswahrnehmung haben, was aus den Sinneseindrücken stammt und was in den Vorstellungen erlebt wird. Dagegen verträumt der Mensch alles das, was in den Gefühlen als Wirklichkeit lebt, und er verschläft alles, was in den Willensimpulsen eigentlich als die tiefere Notwendig­keit liegt, als die tiefere Wirklichkeit vorhanden ist. Wir leben in un­serem Gefühls- und Willensleben in denselben Sphären, in denen mit uns gemeinschaftlich die sogenannten Toten da sind.",
      "Nun ist es gut, wenn wir uns zunächst eine Vorstellung davon machen, was eigentlich hinter dem Sinnesleben nach außen hin liegt. Die Eindrücke der Sinne, man kann sie sich vorstellen, als ob sie sich wie ein Teppich vor uns ausbreiteten. Natürlich, diesen Teppich müs­sen wir uns besetzt denken auch mit den Gehörseindrücken, mit allen Eindrücken der zwölf Sinne, wie wir sie ja aus anthroposophischen Betrachtungen kennen. Sie wissen, daß die wirkliche Zahl der Sinne zwölf ist. Dieser Sinnesteppich deckt gewissermaßen eine hinter ihm liegende Wirklichkeit zu. Diese hinter den Sinneswahrnehmungen lie­gende Wirklichkeit dürfen wir uns nicht so vorstellen, wie etwa der Naturforscher sich die Atomwelt vorstellt, oder wie eine gewisse philo­sophische Richtung vom Ding an sich spricht. Denn ich habe sogar in den öffentlichen Vorträgen betont: Suchen nach einem Ding an sich, wie es die heutige Philosophie tut, wie es der Kantianismus tut, das",
      "hieße ungefähr dasselbe als, die Wesen, die man in einem Spiegel sieht, ihrer Wirklichkeit nach dadurch suchen zu wollen, daß man den Spiegel zerbricht, um zu sehen, was dahinter ist. - In diesem Sinne rede ich nicht von etwas, was hinter den Sinneswahrnehmungen liegt, sondern ich rede von etwas, was hinter den Sinneswahrnehmungen liegt als einem Geistigen, in dem wir selber eingebettet sind, an das aber des Menschen gewöhnliches Bewußtsein, das er zwischen der Geburt und dem Tode trägt, nicht reicht. In dem Augenblicke, wo wir den Sinnes-teppich gewissermaßen enträtseln würden auf einer ersten Stufe, so daß wir nach außen hin mehr sehen würden als die Mannigfaltigkeit der Sinnesimpulse - was würden wir da auf dieser ersten Stufe der spirituellen Enträtselung des Sinnesteppichs sehen? Diese Frage wollen wir uns einmal vorlegen.",
      "Es kann zunächst überraschen, was als dasjenige genannt werden muß, das man zunächst sieht. Was man da zunächst sieht, ist eine Summe von Kräften, die alle darauf ausgehen, unser gesamtes Leben zu impulsieren von der Geburt, oder sagen wir von der Empfängnis bis zum Tode. Nicht in den einzelnen Ereignissen würden wir unser Leben sehen, wenn wir den Sinnesteppich enträtseln, aber in seiner ganzen Artung. Nicht irgend etwas ganz Fremdartiges würden wir zunächst finden, uns selbst würden wir finden auf der ersten Stufe der Enträtselung der Sinneswahrnehmungen - aber uns selbst nicht, wie wir in diesem Augenblicke sind, sondern uns selbst so, wie wir geartet sind dieses ganze Leben zwischen der Geburt und dem Tode. Dieses Leben, das nicht in unseren physischen Leib hereinspielt, daher auch nicht mit physischen Sinnen wahrgenommen werden kann, dieses Le­ben spielt in unseren Ätherleib, in unseren Bildekräfteleib herein. Und unser Bildekräfteleib ist im wesentlichen ein Ausdruck dieses Lebens, das wir überblicken würden, wenn wir die Sinne, die Sinneswahrneh­mungen ausschalten würden. Würde gewissermaßen der Sinnesteppich zerreißen - und er zerreißt, wenn der Mensch zum Schauen aufsteigt -, so findet sich der Mensch selbst, so wie er geartet ist für diese Erden­inkarnation, in der er die betreffende Beobachtung macht. Aber wie gesagt, die Sinne sind nicht geeignet, dies wahrzunehmen.",
      "Was ist geeignet, dies wahrzunehmen? Der Mensch hat es schon,",
      "was geeignet ist, dies wahrzunehmen; aber er hat es in einer solchen Entwickelungsstufe, daß von einem wirklichen Wahrnehmen gegen­wärtig noch nicht die Rede sein kann. Was da wahrgenommen würde, das dringt in kein Auge, kein Ohr, dringt nicht in Sinnesorgane, son­dern wird - ich bitte Sie, das wohl zu verstehen - eingeatmet, mit dem Atem eingesogen.",
      "Und das, was unserer Lunge ätherisch zugrunde liegt - von der physischen Lunge kann ja dabei gar nicht die Rede sein, denn die Lunge ist, so wie sie ist, kein unmittelbares Wahrnehmungs­organ-, was ätherisch unserer Lunge zugrunde liegt, das ist eigentlich Wahrnehmungsorgan, aber für den Menschen zwischen Geburt und Tod nicht brauchbares Wahrnehmungsorgan desjenigen, was da ein­geatmet wird. In der Atemluft, die wir einsaugen, liegt eigentlich in bezug auf jeden Atemzug, wie er sich einfügt in den Gesamtrhythmus des Lebens von der Geburt bis zum Tode, unsere tiefere Wirklichkeit.",
      "Es ist nur so eingerichtet, daß das, was dem ganzen Lungensystem zu­grunde liegt, beim Menschen auf dem physischen Plan unausgebildet ist, nicht vorgeschritten ist bis zu der Fähigkeit, wahrzunehmen. Würde das, was eigentlich unser Lungensystem aufbaut, was da ätherisch zu­grunde liegt, untersucht und richtig erkannt, dann stellte es sich im Grunde genommen als ganz dasselbe dar, was physisch, für die phy­sische Welt, unser Gehirn mit den Sinnesorganen ist.",
      "In dem, was un­serem Lungensystem zugrunde liegt, haben wir ein Gehirn auf einer früheren Entwickelungsstufe, auf einer, man möchte sagen, noch kind­lichen Entwickelungsstufe. Auch in dieser Beziehung tragen wir ge­wissermaßen - ich sage ausdrücklich: gewissermaßen - einen zweiten Menschen in uns.",
      "Und Sie stellen nicht falsch vor, wenn Sie sich denken, daß außer dem physischen Kopf, den der Mensch trägt, noch ein äthe­rischer Kopf vorhanden ist, der nur noch nicht als Wahrnehmungs­organ im gewöhnlichen Leben brauchbar ist, der aber in der Anlage Wahrnehmungsvermögen hat für das, was hinter dem Bildekräfteleib, als diesen Bildekräfteleib schaffend, liegt. Dies aber, was da hinter dem Bildekräfteleib schaffend liegt, das ist dasjenige, in das wir eintreten, wenn wir durch die Pforte des Todes gehen.",
      "Den Bildekräfteleib selbst legen wir dann ab, aber was ihn schafft, was ihn produziert, in das treten wir ein. Es ist vielleicht eine schwierige Vorstellung; allein es ist",
      "gut, wenn Sie versuchen, diese Vorstellung wirklich zu Ende zu denken. Schematisch könnten wir uns die Sache doch noch verdeutlichen.",
      "# Bild s. 74",
      "Wir stellen uns das physische System des Kopfes vor, und wir stellen uns das physische System der Lunge vor (siehe Zeichnung, rot), herein­wirkend aus dem Kosmos die Impulse des Kosmos (blaue Pfeile), die sich rhythmisch ausdrücken in den Lungenbewegungen (rot schraffiert). Durch unsere Lunge stehen wir mit dem ganzen Kosmos in Beziehung, und der ganze Kosmos schafft an unserem Ätherleib. Den Ätherleib selbst legen wir ab, wenn wir durch die Pforte des Todes treten, aber wir treten ein in dasjenige, was hineinspielt in unser Lungensystem; das steht mit dem ganzen Kosmos in Verbindung. Daher jene merkwürdige Übereinstimmung im Rhythmus des Menschenlebens und im Rhythmus der Atmung. Sie wissen ja - ich habe das schon einmal hier ausgeführt-, wenn Sie die 18 Atemzüge, die der Mensch in der Minute hat, ausrech­nen, so daß Sie die Zahl der Atemzüge in einem Tage bekommen, so sind es also 18 mal 60 in der Stunde, für den Tag mal 24 sind 25 920 Atemzüge in einem Tage. Der Mensch atmet ein und atmet aus; das gibt seinen Rhythmus, seinen kleinsten Rhythmus zunächst. Dann aber ist ein anderer Rhythmus in unserem Leben da, wie ich Ihnen schon",
      "einmal angedeutet habe: der besteht darinnen, daß wir unser Seelisches, das Ich und den astralischen Leib, an jedem Morgen beim Aufwachen in unser physisches System gewissermaßen einatmen, beim Einschlafen wiederum ausatmen. Das machen wir durch unser ganzes physisches Leben hindurch.",
      "Nehmen wir ein Durchschnittsmaß des menschlichen Lebens an, so haben wir das so zu berechnen, daß wir sagen: 365mal während eines Jahres atmen wir uns selbst aus und uns selbst ein. Das gibt, wenn wir das menschliche Leben, sagen wir durchschnittsmäßig auf 71 Jahre annehmen, 25 915.",
      "Sie sehen, im wesentlichen dieselbe Zahl - das Leben ist ja nicht gleich bei den einzelnen Menschen -, wiederum 25920mal während eines Lebens zwischen Geburt und Tod wird aus- und eingeatmet dasjenige, was wir unser eigentliches Selbst nennen. So daß wir sagen können: Wie wir uns mit einem Atemzug verhalten zu den Elementen ringsherum, so verhalten wir uns zu der Welt, der wir selbst angehören.",
      "In demselben Rhythmus zum Kosmos leben wir während des Lebens, in welchem wir durch unser Atmen während des Tages stehen. Und wiederum, wenn wir unser Leben nehmen, sagen wir also ungefähr 71 Jahre, und wir betrachten dieses Leben des Menschen als einen kosmischen Tag - nennen wir einmal ein Menschenleben einen kosmischen Tag -, so würde ein kosmisches Jahr 365mal soviel sein, 25 920, also annähernd wiederum ein Jahr.",
      "Das aber ist die Zeit, in welcher die Sonne wiederum zurückkehrt zu dem­selben Sternbilde: 25 920 Jahre. Wenn in einem bestimmten Jahre die Sonne im Widder erscheint, nach 25 920 Jahren erscheint sie wiederum im Widder im Aufgang, denn die Sonne bewegt sich durch den ganzen Tierkreis im Laufe von 25920 Jahren.",
      "So also ist ein ganzes Menschen­leben herausgeatmet aus dem Kosmos, ein Atemzug des Kosmos, der sich genau zum kosmischen Werden, zum kosmischen Umschwung der Sonne im Tierkreis verhält, wie ein Atemzug zum Tagesleben. Eine tiefe innerliche Gesetzmäßigkeit!",
      "Sie sehen, alles ist auf Rhythmus auf­gebaut. Wir atmen dreifach oder wenigstens stehen dreifach in einem Atmungsprozeß drinnen. Wir atmen zunächst durch unsere Lunge in den Elementen - in einem Rhythmus, der durch die Zahl 25920 an­gegeben wird.",
      "Wir atmen im ganzen Sonnensystem, wenn wir Auf- und Untergang der Sonne als parallellaufend zählen unserem Einschlafen",
      "und Aufwachen. Wir atmen durch unser ganzes Leben hindurch in einem Rhythmus, der wiederum durch die Zahl 25920 bestimmt ist. Und endlich, das Weltenall atmet uns aus, atmet uns wieder ein in einem Rhythmus, der wiederum durch die Zahl 25920 bestimmt ist, bestimmt durch den Umlauf der Sonne um den Tierkreis.",
      "So sind wir hineingestellt in den ganzen sichtbaren Kosmos, dem nun der unsichtbare Kosmos zugrunde liegt. In diesen unsichtbaren Kosmos treten wir ein, wenn wir durch die Pforte des Todes treten. Rhythmisches Leben ist dasjenige Leben, das unserem Gefühlsleben zu­grunde liegt. In das rhythmische Leben des Kosmos treten wir ein in der Zeit, die wir durchleben zwischen dem Tod und einer neuen Geburt. Dieses rhythmische Leben liegt als unser ätherisches Leben bestimmend hinter dem Sinnesteppich ausgebreitet. Sehen würde man in dem Au­genblicke, wo man zum schauenden Bewußtsein kommt, diesenWelten­rhythmus, der gewissermaßen ein rhythmisch wogendes Weltenmeer ist, jetzt astralisch geartet. Und in diesem rhythmisch wogenden astra­lischen Meere sind auch die sogenannten Toten vorhanden, sind die Wesenheiten der höheren Hierarchien vorhanden, ist dasjenige vorhan­den, was zu uns gehört, was aber unter der Schwelle liegt, aus der nur die Gefühle heraufwogen, die verträumt werden, die Willensimpulse heraufwogen, die in ihrer eigenen Wirklichkeit verschlafen werden.",
      "Die Frage kann aufgeworfen werden - wir dürfen die Sache ver­gleichsweise, ohne in Teleologie zu verfallen, so sagen: Warum hat es die weisheitsvolle Weltenlenkung eingerichtet, daß der Mensch, so wie er nun einmal ist zwischen Geburt und Tod, nicht wahrnimmt, was da als rhythmisches Leben hinter dem Sinnesteppich liegt? Warum ist der Kopf des Menschen, der verborgene Kopf des Menschen, dem das Lungensystem entspricht, nicht geeignet zu einem entsprechenden Wahrnehmen? Ja, das führt auf eine Wahrheit, welche, man kann sagen, bis in unser Zeitalter von den entsprechenden okkulten Schulen als ein Geheimnis bewahrt worden ist, weil allerdings mit diesem Ge­heimnis andere Geheimnisse in Verbindung stehen, die nicht enthüllt werden sollen, sollten, bisher. Allein in unserer Zeit ist eben auch die Epoche gekommen, in der solche Dinge zum Bewußtsein der Mensch­heit gebracht werden müssen.",
      "Die okkulten Schulen, die da oder dort eingerichtet sind, bewahren solche Dinge aus Gründen, die jetzt nicht erörtert werden sollen, viel­fach heute noch, obwohl die Dinge heute notwendigerweise an das Menschenbewußtsein herangebracht werden sollen. Aber seit dem letz­ten Drittel des 19. Jahrhunderts sind Mittel und Wege gegeben, durch die dasjenige überholt werden kann, was die okkulten Schulen eigent­lich vielfach unrechtmäßigerweise zurückhalten. Das hängt zusammen mit dem Ereignis, von dem ich Ihnen gesprochen habe als fallend in den Herbst des Jahres 1879. Wir können nur den äußersten Saum dieses Geheimnisses für diesmal berühren. Allein schon dieser äußerste Saum dieses Geheimnisses gehört zu den bedeutsamsten Erkenntnissen des menschlichen Wesens. Ein Kopf ist es allerdings, den wir da in uns tragen als den Kopf eines zweiten Menschen, ein Kopf ist es - aber was zu diesem Kopf gehört, ist auch ein Leib, und der Leib, der dazugehört, der ist zunächst ein Tierleib. Der Mensch trägt also einen zweiten Men­schen in sich: dieser zweite Mensch hat einen richtig ausgebildeten Kopf, aber einen Tierleib daran, einen richtigen Kentaur. Der Kentaur ist schon eine Wahrheit. Er ist eben eine ätherische Wahrheit.",
      "Das Bedeutsame ist das, daß in dieser Wesenheit eine verhältnis­mäßig große Weisheit spielt, eine Weisheit, die sich auf den ganzen kos­mischen Rhythmus bezieht. Was der Kopf sieht, der diesem Kentaur angehört, das ist der kosmische Rhythmus, in dem auch der Mensch als Wesen, das zwischen Tod und neuer Geburt lebt, eingebettet ist. Es ist jener Weltenrhythmus, der hier in dreifacher Weise selbst zahlenmäßig gezeigt worden ist, jener Rhythmus, auf dem viele Geheimnisse des Kosmos beruhen. Dieser Kopf ist viel weiser als unser physischer Kopf. Alle Menschen tragen einen sehr weisen andern Menschen, eben den Kentaur, in sich. Aber zugleich ist dieser Kentaur, trotz seiner Weisheit, ausgerüstet mit allen wilden Instinkten der Tierheit.",
      "Jetzt werden Sie die weise Weltenlenkung verstehen. Sie konnte nicht dem Menschen ein Bewußtsein geben, das auf der einen Seite mächtig ist und den Weltenrhythmus durchschaut, aber auf der andern Seite ungebändigt ist, in wilden Trieben lebend. Aber was in der einen Inkarnation tierisch ist an diesem Kentaur, das wird - halten Sie das, was ich jetzt sage, mit andern Vorträgen zusammen, in denen ich das",
      "Thema von einem andern Gesichtspunkte aus beleuchtet habe -, das wird in der nächsten Inkarnation gebändigt, indem er durch die Welt des Weltenrhythmus durchgeht zwischen Tod und neuer Geburt. Was unserem Lungensystem in der gegenwärtigen Inkarnation zugrunde liegt, was da verborgen wird, das erscheint als Ihr physischer Kopf, der dann allerdings herabgedämpft ist zu seinem beschränkten sinnlichen Wissen, und es erscheint in der nächsten Inkarnation als der ganze Mensch nun auch den wilden Trieben nach gebändigt. Was Kentaur in dieser Inkarnation ist, ist der sinnlich wahrnehmende Mensch in der nächsten Inkarnation.",
      "Und jetzt werden Sie ein anderes begreifen. Jetzt werden Sie be­greifen, warum ich gesagt habe, daß der Mensch zwischen dem Tod und einer neuen Geburt als unterstes Reich das tierische Reich hat, in dessen Kräften er Meister werden muß. Was muß er denn tun? Woran muß er denn teilnehmen zwischen zwei Inkarnationen? Er muß daran teilnehmen, den Kentauren, das Tierische in ihm für die nächste Inkar­nation ins Menschliche umzuwandeln. Dazu sind wirklich Kenntnisse notwendig, welche über die Impulse des ganzen tierischen Reiches sich erstrecken müssen, welche in ihrer Abschwächung atavistisch eigen gewesen sind den Menschen jenes Zeitalters, in dem der Chiron gelebt hat. Wenn auch die Erkenntnisse, von denen der Chiron spricht, Ab­schwächungen sind dieser Inkarnation, von dieser Art sind sie. Aber Sie sehen den Zusammenhang. Sie sehen, wozu der Mensch zwischen dem Tod und einer neuen Geburt dieses untere Reich braucht, in dem er Meister werden muß: er braucht es, weil er den Kentauren in einen Menschen umwandeln muß.",
      "Was die anthroposophisch orientierte Geisteswissenschaft darbietet, war bis jetzt eigentlich nur in einzelnen Lichtblitzen außerhalb der okkulten Schulen erlangt worden. Aber einzelne Menschen hat es immer gegeben, die auf solche Dinge wie durch Lichtblitze des Lebens ge­kommen sind. Besonders im 19.Jahrhundert kamen, ich möchte sagen vorahnend, einzelne Geister darauf, daß im Menschen drinnen so etwas mit wildgebändigten Trieben steckt. Es gibt Schriftsteller, die davon sprechen. Und aus der Art, wie sie davon sprechen, sieht man, wie sie erschrocken sind über diese Erkenntnis. Ja, so bequem geistig zu verdauen",
      "wie die heutigen naturwissenschaftlichen Erkenntnisse, so bequem sind die hohen Wahrheiten nicht. Diese hohen Wahrheiten haben schon zuweilen die Eigenschaft, daß man vor ihrer Wirklichkeit erschrecken kann. Und es hat Geister im 19. Jahrhundert gegeben, die erschrocken sind, die furchtbar berührt gewesen sind, als sie wahrnahmen, was eigentlich aus dem manchmal verwirrt blickenden Auge des Menschen oder aus sonstigem am Menschen spricht. Einer der Schriftsteller des 19. Jahrhunderts hat sich drastisch ausgedrückt, indem er sagte: Jeder Mensch trägt eigentlich einen Mörder in sich. - Er meinte diesen Ken­tauren, der ihm unklar zum Bewußtsein gekommen ist.",
      "Daß auf dem Grunde der Menschennatur Rätselhaftes ist, über das der Mensch sich nach und nach aufklären muß, das ist etwas,was immer wieder und wieder betont werden muß. Mit Mut und Gelassenheit müssen diese Dinge ins Auge gefaßt werden. Aber sie dürfen nicht ver­trivialisiert werden, denn sie rücken das Menschheitsbewußtsein an den großen Ernst des Lebens heran. Und den Ernst des Lebens zu durch­schauen, das ist dasjenige, was den Menschen vorgesetzt ist für diese Zeit, die da kommt, die jetzt durch so furchtbare Zeichen eingetreten ist.",
      "Dies ist die eine Seite, durch die ich eine gewisse Betrachtung vor­bereiten will, die wir dann demnächst fortsetzen werden. Die andere Seite ist die folgende: Der Mensch tritt durch die Todespforte; ich habe ja das letzte Mal davon gesprochen, wie verschieden das ganze Erleben dann wird, indem ich Ihnen angedeutet habe, wie der Verkehr mit einem Toten eigentlich so vor sich geht, daß dasjenige, was man selber ihm mitteilt, wie aus ihm spricht, und dasjenige, was er einem mitteilt, wie aus den Tiefen des eigenen Wesens heraus spricht. Es kehrt sich geradezu das gegenseitige Verhältnis um im Verkehr mit dem Toten. Wenn Sie hier mit einem Menschen verkehren, da sprechen Sie. Sie hören sich dasjenige sprechen, was Sie dem andern mitteilen. Von ihm hören Sie dasjenige, was er Ihnen mitteilt. Wenn Sie mit dem Toten sich verständigen, dann dringt aus Ihrer eigenen Seele herauf dasjenige, was er sagt, und wie durch ein Echo tönt von ihm zurück Ihnen ent­gegen, was Sie ihm mitgeteilt haben. An sich nehmen Sie es gar nicht wahr, was Sie ihm mitgeteilt haben: an ihm nehmen Sie es wahr. Das wollte ich nur als ein Beispiel angeben für den radikalen Unterschied,",
      "der da besteht zwischen der physischen Welt hier, in der wir zwischen Geburt und Tod leben, und der Welt, in der wir leben zwischen dem Tod und einer neuen Geburt.",
      "Hinein schauen wir, indem wir diese Welt von der einen Seite an­schauen: indem wir den Sinnesteppich durchschauen, schauen wir in den Rhythmus der Welt. Aber dieser Rhythmus hat zwei Seiten. Ich will Ihnen diese zwei Seiten des Rhythmus schematisch dadurch dar­stellen, daß ich vielleicht eine Anzahl von Sternen, sagen wir Planeten",
      "# Bild s. 80",
      "zunächst, hier aufzeichne (rot). Das sei eine Anzahl von Sternen, Pla­neten. Meinetwillen sei das das Planetensystem, das zu unserer Erde gehört. Der Mensch geht durch dieses Planetensystem durch in der Zeit, die zwischen dem Tod und einer neuen Geburt liegt. Es gibt einen Zyklus von Vorträgen, der gedruckt ist, in dem Sie sich über diese Dinge unterrichten können. Der Mensch geht durch das System durch. Aber indem er durch das, was noch sichtbare Welt ist, durchgeht, kommt er in der Zeit zwischen dem Tod und einer neuen Geburt auch in die Welt, die nicht mehr sichtbar ist, die nicht einmal räumlich ist. Da redet man allerdings von schwierigen Dingen, weil der Mensch gewohnt ist, nach den Erfahrungen hier in der physischen Welt, wo er sich überhaupt",
      "etwas vorstellt, sich Räumliches vorzustellen. Aber es liegt eine Welt jenseits des Sinnlich-Wahrnehmbaren, die allerdings nicht mehr räum­lich ist. Ich kann sie schematisch nur räumlich ausdrücken.",
      "Die Alten haben gesagt: Jenseits der Planeten liegt der Fixstern­himmel - das ist zwar verkehrt gesagt, darauf kommt es aber jetzt nicht an - und jenseits davon liegt nun die übersinnliche Welt. - Die Alten stellten sie räumlich dar, aber das ist nur eine bildliche Vorstellung davon (siehe Zeichnung, blau).",
      "Ist der Mensch eingetreten in diese übersinnliche Welt in der Zeit, die zwischen dem Tod und einer neuen Geburt liegt, dann kann man sagen, trotzdem das auch wieder bildlich gesprochen ist, der Mensch befindet sich dann jenseits der Sterne, und die Sterne selbst dienen ihm zu einer Art von Lesen. Also die Sterne dienen dem Menschen zwischen dem Tod und einer neuen Geburt zu einer Art von Lesen.",
      "Machen wir uns das ganz klar, wie das ist. Wie lesen wir, wenn wir hier auf der Erde lesen? Wenn wir hier auf der Erde lesen, haben wir ungefähr zwölf Konsonanten und sieben Vokale mit verschiedenen Nuancen.",
      "Diese Buchstaben setzen wir in der mannigfaltigsten Weise zu Worten zu­sammen. Wir werfen sie durcheinander, die Buchstaben. Stellen Sie sich vor, wie der Setzer im Setzkasten die Dinge durcheinander wirft, damit Worte daraus werden.",
      "Aus den bestimmten Buchstaben, die wir haben, werden ja alle Worte. Was für den Menschen, der hier auf dem phy­sischen Plane ist, diese Buchstaben sind, diese ungefähr zwölf Konso­nanten und sieben Vokale mit den verschiedenen Nuancen, das sind für den Toten die Fixsterne des Tierkreises und die Planeten.",
      "Die Fix­sterne des Tierkreises sind die Konsonanten und die Planeten sind die Vokale. Ist man jenseits des Sternenhimmels, dann sieht man peri­pherisch. Der Mensch sieht zentral, wenn er zwischen der Geburt und dem Tode ist; er hat hier sein Auge, und dann sieht er so ausstrahlend nach verschiedenen Punkten hin.",
      "Es ist am schwersten vorzustellen, daß das umgekehrt ist nach dem Tode: da sieht man peripherisch. Man ist eigentlich im Umkreise und man sieht von außen die Sterne des Tier-kreises, die Konsonanten, und die Planeten, die Vokale.",
      "Und so sieht man von außen herein auf das, was auf der Erde vorgeht. Und je nach­dem man irgendeinen Teil seines Wesens belebt, sieht man - Sie müssen",
      "sich jetzt das nicht von der Erde aus denken, sondern umgekehrt, auf die Erde herunterschauend - durch den Stier und Mars auf die Erde nieder, oder Sie sehen durch den Stier durch zwischen Mars und Jupiter. Sie lesen, indem Sie als Toter die Erde umkreisen, Sie lesen mit Hilfe des Sternensystems.",
      "Nur müssen Sie sich dieses Lesen jetzt etwas anders vorstellen. Nicht wahr, wir könnten auch anders lesen, nur wäre es nicht technisch so bequem eingerichtet wie unser gegenwärtiges Lese-system. Man könnte auch anders lesen.",
      "Man könnte so lesen, daß wir die Buchstaben hintereinander haben: a, b, c, d, e, f, g und so weiter -oder nach einem andern System - und statt daß wir sie im Setzkasten um und um werfen, könnten wir so lesen, daß, wenn zum Beispiel «der» gelesen werden soll, ein Lichtstrahl fällt auf das «der»; soll «geht» ge­lesen werden, fällt ein Lichtstrahl auf «geht». Es könnte also die Rei­henfolge der Buchstaben erst da sein, und sie könnten so hintereinander beleuchtet sein.",
      "Es wäre technisch nicht so bequem, aber Sie könnten sich immerhin ein Erdenleben vorstellen, in dem das Lesen so bewerk­stelligt würde, daß man vor sich nimmt ein Alphabet, und dann gäbe es irgendeine Vorrichtung, durch die immer beleuchtet wird ein Buch­stabe; dann liest man hintereinander die Aufeinanderfolge der beleuch­teten Buchstaben - und es hat den Goetheschen «Faust» ergeben. Das ist natürlich nicht so ohne weiteres vorzustellen, doch eine Möglichkeit gibt es, sich so es vorzustellen, nicht wahr?",
      "# Bild s. 82",
      "Aber so liest der Tote mit Hilfe des Sternensystems: Die Fixsterne stehen fest, und er bewegt sich, denn er ist in der Bewegung drinnen. Die Fixsterne stehen fest, er bewegt sich. Soll er den Löwen über dem",
      "Jupiter lesen, so bewegt er sein Wesen so, daß ihm der Löwe über dem Jupiter steht, wie wir «der» lesen, indem wir das d mit dem e zusam­menbringen und so weiter. Dieses Lesen der Erdenverhältnisse aus dem Kosmos - wozu der unsichtbare Kosmos gehört - besteht also darinnen, daß das, was geistig den Sternen zugrunde liegt, von den Toten gelesen werden kann. Nur ist das ganze System auf Ruhe eingerichtet; dieses ganze göttliche System des Lesens vom Kosmos herein ist auf Ruhe ein­gerichtet. Was heißt das? Das heißt: Eigentlich sollten nach den Inten­tionen gewisser Wesen der höheren Hierarchien die Planeten ruhig sein, sollten eine ruhige Form abgeben. Dann würde bloß das Wesen, das sich draußen lesend verhält, in Bewegung sein. Es würde vom Welten-all aus auf der Erde unbedingt richtig gelesen werden können, wenn die Planeten in Ruhe wären, eine ruhende Lage hätten.",
      "Das sind sie nicht! Warum sind sie es nicht? Sie wären es, wenn die Weltenschöpfung so gegangen wäre, daß die Geister der Form, die Exusiai nach unserer Benennung, die Welt allein zustande gebracht hätten. Doch es beteiligten sich, hereingreifend in die Welt, luziferische Geister, wie Sie wissen. Luziferische Geister brachten das, was Gesetz war während der Mondengestalt der Erde - wo gewisse Dinge, die dann übergingen in die Macht der Geister der Form, den Geistern der Bewegung unterstanden -, dieses System der Bewegung herüber aus der Mondenzeit der Erde: sie brachten die Planeten in Bewegung. Daß die Planeten in bestimmter Bewegung sind, ist ein Luziferisches im Welten-raum. Das bringt in einer gewissen Beziehung in die elohimistische Ord­nung Unruhe hinein; das bringt in das Weltenall, in den Kosmos ein luziferisches Element hinein. Es ist das jenes luziferische Element, das der Mensch zwischen dem Tod und einer neuen Geburt kennenlernen muß; gerade dadurch kennenlernen muß, daß er lernt abzuziehen ge­wissermaßen von dem, was er liest, das, was aus der Bewegung der Planeten, der Irr- oder Wandelsterne kommt. Das muß er abziehen, das muß er abrechnen; dann bekommt er das Richtige zustande.",
      "Man lernt in der Tat zwischen dem Tod und einer neuen Geburt viel kennen über das Walten und Weben des Luziferischen im Kosmos. Und solche Dinge, wie der Gang der Wandelsterne, der Gang der Planeten, hängen mit Luziferischem zusammen.",
      "Das ist die andere Seite, auf die ich habe aufmerksam machen wol­len. Sie sehen aber daraus, wie jenes andere Leben, das wir durchleben zwischen dem Tod und einer neuen Geburt, mit unserem hiesigen Leben zusammenhängt. Man möchte sagen, die Welt hat zwei Seiten. Hier zwischen der Geburt und dem Tode sieht man die eine Seite durch die Sinne. Von der abgewendeten Seite aus schaut man sie mit dem Seelen-auge an in der Zeit zwischen dem Tod und einer neuen Geburt. Und zwischen dem Tod und einer neuen Geburt lernt man die Verhältnisse hier im Irdischen mit denen der geistigen Welt zusammenhängend lesen.",
      "Man mache sich so etwas nur ganz klar, man versuche, sich hinein­zuversetzen in diese Verhältnisse. Man wird sich gestehen müssen, daß es allerdings eine tiefe Bedeutung hat, wenn man davon spricht, daß die Welt, die der Mensch zunächst durch seine Sinne und durch seinen Verstand kennenlernt, eine Maja ist. Sobald man an die wirkliche Welt herantritt, verhält sich allerdings die Welt, die man kennt, zu dieser wirklichen Welt so, wie das, was im Spiegel drinnen erscheint, zu dem sich verhält, was vor dem Spiegel ist als Lebendiges und sich im Spiegel bloß spiegelt.",
      "Nun, wenn Sie hier einen Spiegel haben und dadrinnen sind ver­schiedene Gestalten, so weist das darauf hin, daß außerhalb des Spiegels Gestalten da sind, die sich spiegeln. Nehmen Sie an, Sie schauen in den Spiegel hinein als unbeteiligter Zuschauer. (Es wird gezeichnet.) Die zwei Gestalten, die ich da aufgezeichnet habe, die prügeln sich, das sehen Sie, die prügeln sich. Das weist zwar darauf hin, daß diejenigen Gestalten, die sich spiegeln, irgend etwas tun, aber Sie werden nicht behaupten dürfen, daß die Gestalt A im Spiegel dadrinnen die Gestalt B im Spiegel dadrinnen durchprügelt. Was da im Spiegel drinnen er­scheint, das gibt das Bild des Prügelns, weil die Gestalten außer dem Spiegel irgend etwas tun. Sind Sie der Meinung, daß die Gestalt A, die da im Spiegel drinnen ist als Spiegelbild, der Gestalt B, die im Spiegel drinnen ist, etwas antut, dann sind Sie in einer ganz irrtümlichen Mei­nung befangen. Sie können nicht Beziehungen, Verhältnisse aufstellen zwischen den Spiegelbildern, sondern Sie können nur sagen: Das, was sich in den Spiegelbildern ausdrückt, das weist hin auf irgend etwas in der Welt der Wirklichkeit, die sich spiegelt. - Aber die Welt, die der",
      "Mensch als gegebene hat, ist ein Spiegel, ist eine Maja, und in dieser Welt redet der Mensch von Ursachen und Wirkungen. Wenn Sie in dieser Welt von Ursachen und Wirkungen reden, so ist das gerade so, wie wenn Sie glauben würden, daß das Spiegelbild A dadrinnen das Spiegelbild B durchprügelt. In den wirklichen Wesen, die sich spiegeln, geschieht etwas; aber in dem Spiegelbild A, in dem Spiegelbild B liegen nicht die Impulse des Sich-Prügelns.",
      "Gehen Sie die ganze Naturordnung durch: sie ist zunächst, so wie sie den Sinnen erscheint, eine Maja, ein Spiegelndes, ein Gespiegeltes. Die Wirklichkeit liegt unter der Grenze, die ich angegeben habe, die zwischen dem Vorstellungsleben und dem Gefühlsleben liegt. Selbst Ihre eigene Wirklichkeit ist in dem, was das wache Bewußtsein enthält, gar nicht einmal drinnen. Aber diese eigene Wirklichkeit ist in der Geistwirklichkeit drinnen, in welche die träumende und schlafende Gefühls- und Willenskraft hinuntertaucht. Also von ursächlicher Not­wendigkeit in der Maja zu sprechen, ist, wie Sie sehen, ein Unding; ein Unding auch, in der historischen Folge der Ereignisse von Ursache und Wirkung zu sprechen. Ein Unding! Zu dem, was ich gesagt habe, füge ich hinzu, daß es ein Unding ist, zu sagen, die Ereignisse von 1914 sind eine Folge der Ereignisse von 1913,1912 und so weiter. Das ist geradeso gescheit, wie wenn man sagen würde: Ach, dieser A im Spiegel, der ist ein schlechter Kerl, der haut den B dadrinnen durch! - Auf die wahre Wirklichkeit zu gehen, das ist das, worauf es ankommt. Und die wahre Wirklichkeit liegt unter der Schwelle, die überschritten wird nach unten von unserer Gefühls- und Willenswelt, die aber nicht in das gewöhn­liche wachende Bewußtsein tritt. Und da lebt auch der Kentaur, von dem ich gesprochen habe.",
      "Sie sehen, daß man den Begriff: Irgend etwas mußte geschehen -Irgend etwas war notwendig - anders fassen muß, als man ihn in der gewöhnlichen Geschichte oder gar in der Naturwissenschaft faßt; daß man die Frage aufwerfen muß: Welches sind die wirklichen Wesen, die dasjenige, was in einem späteren Zeitpunkte auf einen früheren folgt, hervorgebracht haben? - Die sogenannten historischen Ereignisse von vorher sind nur Spiegelbilder, die können das nicht bewirken, was nachher geschieht.",
      "Das ist aber wiederum die eine Seite der Sache. Die andere wird Ihnen klar, wenn Sie bedenken, daß eigentlich im Vorstellungs- und Sinnesleben der wachen Wirklichkeit nur ein Spiegel des wahren Le­bens, eine Maja gegeben ist. Diese Maja kann aber nichts bewirken. Diese Maja kann nicht im Stande einer Causa sein, irgendeine wirkliche Ursache sein. Der Mensch ist aber in der Lage, sich von seinen reinen Vorstellungen zu Handlungen bestimmen zu lassen. Das ist eine Er­fahrungstatsache des Lebens, wenn der Mensch nicht durch Leiden­schaften, Triebe, Begierden, sondern durch reine Vorstellungen getrie­ben wird. Das kann sein, und das ist möglich; der Mensch kann sich von reinen Idealen, von reinen Ideen impulsieren lassen. Aber die können selbst nichts bewirken. Ich kann also eine Handlung ausführen unter dem Einfluß einer reinen Idee; aber die Idee kann nichts bewirken.",
      "Vergleichen Sie noch einmal, um das einzusehen, die Idee mit einem Spiegelbild. Ja, das Bild im Spiegel, das kann nicht bewirken, daß Sie davonlaufen. Es muß Ihnen nicht gefallen, oder es muß etwas sein, was gar nicht mit dem Spiegelbild in irgendeiner Beziehung steht, wenn Sie davonlaufen.",
      "Das Spiegelbild selbst kann nicht eine Peitsche nehmen und bewirken, daß Sie davonlaufen. Das kann keine Causa sein. Wenn aber der Mensch unter dem Einfluß seiner Spiegelbilder, also seiner Ideen handelt, dann handelt er aus der Maja heraus, handelt er eben aus dem Weltenspiegel heraus: Er muß es sein, der handelt, deshalb handelt er dann frei.",
      "Wenn er seinen Leidenschaften folgt, handelt er nicht frei; nicht einmal, wenn er seinen Gefühlen folgt, handelt er frei. Wenn er seinen Vorstellungen, die bloß Spiegelbilder sind, folgt, han­delt er frei.",
      "Aus diesem Grunde ist es, warum ich in der «Philosophie der Freiheit» ausgeführt habe, daß der Mensch, wenn er reinen Ideen folgt, dem reinen Denken folgt, ein frei handelndes Wesen ist, weil reine Ideen eben nichts bewirken können, also das Bewirken von an­derswoher kommen muß. Ich habe diese Sache mit diesem Bilde noch einmal durchgeführt in meinem Buche «Vom Menschenrätsel».",
      "Gerade weil dasjenige, was uns zunächst umgibt, eine Maja ist, die nichts be­wirken kann, wir aber unter dem Einflusse dieser Maja handeln, sind wir freie Menschenwesen. Unsere Freiheit beruht darauf, daß unsere Wahrnehmungswelt Maja ist.",
      "Unser Wesen vermählt sich mit der Maja",
      "und ist dadurch ein freies Wesen. Wäre die Welt, die wir wahrnehmen, Wirklichkeit, dann würde diese Wirklichkeit uns zwingen, dann wären wir nicht freie Wesen. Wir sind freie Wesen gerade deshalb, weil die Welt, die wir wahrnehmen, nicht eine Wirklichkeit ist, daher uns auch nicht zwingen kann, ebensowenig wie uns ein Spiegelbild zwingen kann davonzulaufen. Darinnen beruht das Geheimnis des freien Men­schen, daß man den Zusammenhang einsieht zwischen der Wahrneh­mungswelt als einer Maja, der bloßen Spiegelung einer Wirklichkeit, und dem Impulsieren des Menschen durch sich selbst. Der Mensch muß sich selber impulsieren, wenn dasjenige, unter dessen Eindruck er han­delt, ihn eben nicht bestimmt.",
      "Die Freiheit läßt sich streng beweisen, wenn man diesen Beweis auf der Grundlage sucht, daß die Welt, so wie sie als Wahrnehmung ge­geben ist, ein Spiegelbild ist und nicht eine Wirklichkeit.",
      "Das sind die vorbereitenden Ideen, die ich Ihnen mitteilen wollte über dasjenige, was auf dem Grunde der Menschennatur liegt. Was Wirklichkeiten wahrnehmen würde, aber zur Wahrnehmung in einer Inkarnation noch nicht reif ist, sondern abgeschwächt erst in der näch­sten Inkarnation Mensch wird, der Kentaur würde Wahrheit, würde Wirklichkeit wahrnehmen; aber der Kentaur nimmt eben noch nicht wahr. Dasjenige, was heute wahrgenommen wird, ist noch keine Wirk­lichkeit. Aber der Mensch kann sich bestimmen lassen durch dasjenige in seinem Wesen, was nicht mehr - oder noch nicht - ein Kentaur ist:",
      "dann handelt er als ein freies Wesen. Das Geheimnis unserer Freiheit hängt innig zusammen mit der Bändigung unserer Kentaurennatur. Unsere Kentaurennatur verhält sich so zu uns, daß sie angekettet, ge­fesselt ist, damit wir nicht die Wirklichkeit des Kentauren, sondern eine bloße Maja wahrnehmen. Wenn wir uns durch die Maja impul­sieren, sind wir frei.",
      "Das ist von dieser Seite aus gesehen. Von der andern Seite lernen wir erkennen die Welt zwischen dem Tod und einer neuen Geburt, indem dasjenige, was uns sonst als Kosmos umgibt, zusammenschrumpft zu einem Lesemittel im Kosmos, dessen Abglanz hier die physischen Buch­staben sind. Daß mehr Buchstaben heute vorhanden sind in den Spra­chen - die finnische Sprache hat heute noch immer bloß zwölf Konsonanten -,",
      "das ist nur, weil Nuancen geschaffen werden; aber im wesent­lichen gibt es zwölf Konsonanten und sieben mit verschiedenen Nuan­cen behaftete Vokale. Die verschiedenen Nuancen der Vokale sind dasjenige, was als Luziferisches dazugekommen ist. Was die Vokale in Bewegung bringt, das entspricht der Planetenbewegung.",
      "Sie sehen den Zusammenhang desjenigen, was im Kleinen im Men­schenleben spielt: das Lesen, der Zusammenhang zwischen dem Lesen der Buchstaben, die wir hier auf dem Papiere haben, und demjenigen, was im Kosmos draußen lebt. Der Mensch ist aus dem Kosmos heraus geboren, nicht bloß wiederum eine Wirkung desjenigen, was ihm in der Vererbung vorangegangen ist.",
      "Das sind so einige Grundlagen, um allmählich zu dem wirklichen Begreifen von Freiheit und Notwendigkeit von historischem, sozialem und ethisch-moralischem Geschehen zu kommen."
    ],
    "sentences": [
      [
        "Das Thema, das wir jetzt besprechen, ist sehr umfassend, und es wird heute nicht so weit geführt werden können, als ich eigentlich gewollt habe, aber wir setzen ja diese Betrachtungen weiter fort.",
        "Denn ich möchte gerade in diesen Betrachtungen vor allem die Grundlage zum Verständnis von Freiheit und Notwendigkeit so legen, daß Sie ein Bild bekommen von dem, was vom okkultistischen Standpunkte in Betracht kommt, um den Verlauf des sozialen und des geschichtlichen, des ethisch-moralischen Menschenlebens zu verstehen."
      ],
      [
        "Wir haben betont, daß für das Leben zwischen der Geburt und dem Tode völlig wachend eigentlich nur das durchlebt wird, was wir in der Sinneswahrnehmung haben, was aus den Sinneseindrücken stammt und was in den Vorstellungen erlebt wird.",
        "Dagegen verträumt der Mensch alles das, was in den Gefühlen als Wirklichkeit lebt, und er verschläft alles, was in den Willensimpulsen eigentlich als die tiefere Notwendig­keit liegt, als die tiefere Wirklichkeit vorhanden ist.",
        "Wir leben in un­serem Gefühls- und Willensleben in denselben Sphären, in denen mit uns gemeinschaftlich die sogenannten Toten da sind."
      ],
      [
        "Nun ist es gut, wenn wir uns zunächst eine Vorstellung davon machen, was eigentlich hinter dem Sinnesleben nach außen hin liegt.",
        "Die Eindrücke der Sinne, man kann sie sich vorstellen, als ob sie sich wie ein Teppich vor uns ausbreiteten.",
        "Natürlich, diesen Teppich müs­sen wir uns besetzt denken auch mit den Gehörseindrücken, mit allen Eindrücken der zwölf Sinne, wie wir sie ja aus anthroposophischen Betrachtungen kennen.",
        "Sie wissen, daß die wirkliche Zahl der Sinne zwölf ist.",
        "Dieser Sinnesteppich deckt gewissermaßen eine hinter ihm liegende Wirklichkeit zu.",
        "Diese hinter den Sinneswahrnehmungen lie­gende Wirklichkeit dürfen wir uns nicht so vorstellen, wie etwa der Naturforscher sich die Atomwelt vorstellt, oder wie eine gewisse philo­sophische Richtung vom Ding an sich spricht.",
        "Denn ich habe sogar in den öffentlichen Vorträgen betont: Suchen nach einem Ding an sich, wie es die heutige Philosophie tut, wie es der Kantianismus tut, das"
      ],
      [
        "hieße ungefähr dasselbe als, die Wesen, die man in einem Spiegel sieht, ihrer Wirklichkeit nach dadurch suchen zu wollen, daß man den Spiegel zerbricht, um zu sehen, was dahinter ist. - In diesem Sinne rede ich nicht von etwas, was hinter den Sinneswahrnehmungen liegt, sondern ich rede von etwas, was hinter den Sinneswahrnehmungen liegt als einem Geistigen, in dem wir selber eingebettet sind, an das aber des Menschen gewöhnliches Bewußtsein, das er zwischen der Geburt und dem Tode trägt, nicht reicht.",
        "In dem Augenblicke, wo wir den Sinnes-teppich gewissermaßen enträtseln würden auf einer ersten Stufe, so daß wir nach außen hin mehr sehen würden als die Mannigfaltigkeit der Sinnesimpulse - was würden wir da auf dieser ersten Stufe der spirituellen Enträtselung des Sinnesteppichs sehen?",
        "Diese Frage wollen wir uns einmal vorlegen."
      ],
      [
        "Es kann zunächst überraschen, was als dasjenige genannt werden muß, das man zunächst sieht.",
        "Was man da zunächst sieht, ist eine Summe von Kräften, die alle darauf ausgehen, unser gesamtes Leben zu impulsieren von der Geburt, oder sagen wir von der Empfängnis bis zum Tode.",
        "Nicht in den einzelnen Ereignissen würden wir unser Leben sehen, wenn wir den Sinnesteppich enträtseln, aber in seiner ganzen Artung.",
        "Nicht irgend etwas ganz Fremdartiges würden wir zunächst finden, uns selbst würden wir finden auf der ersten Stufe der Enträtselung der Sinneswahrnehmungen - aber uns selbst nicht, wie wir in diesem Augenblicke sind, sondern uns selbst so, wie wir geartet sind dieses ganze Leben zwischen der Geburt und dem Tode.",
        "Dieses Leben, das nicht in unseren physischen Leib hereinspielt, daher auch nicht mit physischen Sinnen wahrgenommen werden kann, dieses Le­ben spielt in unseren Ätherleib, in unseren Bildekräfteleib herein.",
        "Und unser Bildekräfteleib ist im wesentlichen ein Ausdruck dieses Lebens, das wir überblicken würden, wenn wir die Sinne, die Sinneswahrneh­mungen ausschalten würden.",
        "Würde gewissermaßen der Sinnesteppich zerreißen - und er zerreißt, wenn der Mensch zum Schauen aufsteigt -, so findet sich der Mensch selbst, so wie er geartet ist für diese Erden­inkarnation, in der er die betreffende Beobachtung macht.",
        "Aber wie gesagt, die Sinne sind nicht geeignet, dies wahrzunehmen."
      ],
      [
        "Was ist geeignet, dies wahrzunehmen?",
        "Der Mensch hat es schon,"
      ],
      [
        "was geeignet ist, dies wahrzunehmen; aber er hat es in einer solchen Entwickelungsstufe, daß von einem wirklichen Wahrnehmen gegen­wärtig noch nicht die Rede sein kann.",
        "Was da wahrgenommen würde, das dringt in kein Auge, kein Ohr, dringt nicht in Sinnesorgane, son­dern wird - ich bitte Sie, das wohl zu verstehen - eingeatmet, mit dem Atem eingesogen."
      ],
      [
        "Und das, was unserer Lunge ätherisch zugrunde liegt - von der physischen Lunge kann ja dabei gar nicht die Rede sein, denn die Lunge ist, so wie sie ist, kein unmittelbares Wahrnehmungs­organ-, was ätherisch unserer Lunge zugrunde liegt, das ist eigentlich Wahrnehmungsorgan, aber für den Menschen zwischen Geburt und Tod nicht brauchbares Wahrnehmungsorgan desjenigen, was da ein­geatmet wird.",
        "In der Atemluft, die wir einsaugen, liegt eigentlich in bezug auf jeden Atemzug, wie er sich einfügt in den Gesamtrhythmus des Lebens von der Geburt bis zum Tode, unsere tiefere Wirklichkeit."
      ],
      [
        "Es ist nur so eingerichtet, daß das, was dem ganzen Lungensystem zu­grunde liegt, beim Menschen auf dem physischen Plan unausgebildet ist, nicht vorgeschritten ist bis zu der Fähigkeit, wahrzunehmen.",
        "Würde das, was eigentlich unser Lungensystem aufbaut, was da ätherisch zu­grunde liegt, untersucht und richtig erkannt, dann stellte es sich im Grunde genommen als ganz dasselbe dar, was physisch, für die phy­sische Welt, unser Gehirn mit den Sinnesorganen ist."
      ],
      [
        "In dem, was un­serem Lungensystem zugrunde liegt, haben wir ein Gehirn auf einer früheren Entwickelungsstufe, auf einer, man möchte sagen, noch kind­lichen Entwickelungsstufe.",
        "Auch in dieser Beziehung tragen wir ge­wissermaßen - ich sage ausdrücklich: gewissermaßen - einen zweiten Menschen in uns."
      ],
      [
        "Und Sie stellen nicht falsch vor, wenn Sie sich denken, daß außer dem physischen Kopf, den der Mensch trägt, noch ein äthe­rischer Kopf vorhanden ist, der nur noch nicht als Wahrnehmungs­organ im gewöhnlichen Leben brauchbar ist, der aber in der Anlage Wahrnehmungsvermögen hat für das, was hinter dem Bildekräfteleib, als diesen Bildekräfteleib schaffend, liegt.",
        "Dies aber, was da hinter dem Bildekräfteleib schaffend liegt, das ist dasjenige, in das wir eintreten, wenn wir durch die Pforte des Todes gehen."
      ],
      [
        "Den Bildekräfteleib selbst legen wir dann ab, aber was ihn schafft, was ihn produziert, in das treten wir ein.",
        "Es ist vielleicht eine schwierige Vorstellung; allein es ist"
      ],
      [
        "gut, wenn Sie versuchen, diese Vorstellung wirklich zu Ende zu denken.",
        "Schematisch könnten wir uns die Sache doch noch verdeutlichen."
      ],
      [
        "# Bild s. 74"
      ],
      [
        "Wir stellen uns das physische System des Kopfes vor, und wir stellen uns das physische System der Lunge vor (siehe Zeichnung, rot), herein­wirkend aus dem Kosmos die Impulse des Kosmos (blaue Pfeile), die sich rhythmisch ausdrücken in den Lungenbewegungen (rot schraffiert).",
        "Durch unsere Lunge stehen wir mit dem ganzen Kosmos in Beziehung, und der ganze Kosmos schafft an unserem Ätherleib.",
        "Den Ätherleib selbst legen wir ab, wenn wir durch die Pforte des Todes treten, aber wir treten ein in dasjenige, was hineinspielt in unser Lungensystem; das steht mit dem ganzen Kosmos in Verbindung.",
        "Daher jene merkwürdige Übereinstimmung im Rhythmus des Menschenlebens und im Rhythmus der Atmung.",
        "Sie wissen ja - ich habe das schon einmal hier ausgeführt-, wenn Sie die 18 Atemzüge, die der Mensch in der Minute hat, ausrech­nen, so daß Sie die Zahl der Atemzüge in einem Tage bekommen, so sind es also 18 mal 60 in der Stunde, für den Tag mal 24 sind 25 920 Atemzüge in einem Tage.",
        "Der Mensch atmet ein und atmet aus; das gibt seinen Rhythmus, seinen kleinsten Rhythmus zunächst.",
        "Dann aber ist ein anderer Rhythmus in unserem Leben da, wie ich Ihnen schon"
      ],
      [
        "einmal angedeutet habe: der besteht darinnen, daß wir unser Seelisches, das Ich und den astralischen Leib, an jedem Morgen beim Aufwachen in unser physisches System gewissermaßen einatmen, beim Einschlafen wiederum ausatmen.",
        "Das machen wir durch unser ganzes physisches Leben hindurch."
      ],
      [
        "Nehmen wir ein Durchschnittsmaß des menschlichen Lebens an, so haben wir das so zu berechnen, daß wir sagen: 365mal während eines Jahres atmen wir uns selbst aus und uns selbst ein.",
        "Das gibt, wenn wir das menschliche Leben, sagen wir durchschnittsmäßig auf 71 Jahre annehmen, 25 915."
      ],
      [
        "Sie sehen, im wesentlichen dieselbe Zahl - das Leben ist ja nicht gleich bei den einzelnen Menschen -, wiederum 25920mal während eines Lebens zwischen Geburt und Tod wird aus- und eingeatmet dasjenige, was wir unser eigentliches Selbst nennen.",
        "So daß wir sagen können: Wie wir uns mit einem Atemzug verhalten zu den Elementen ringsherum, so verhalten wir uns zu der Welt, der wir selbst angehören."
      ],
      [
        "In demselben Rhythmus zum Kosmos leben wir während des Lebens, in welchem wir durch unser Atmen während des Tages stehen.",
        "Und wiederum, wenn wir unser Leben nehmen, sagen wir also ungefähr 71 Jahre, und wir betrachten dieses Leben des Menschen als einen kosmischen Tag - nennen wir einmal ein Menschenleben einen kosmischen Tag -, so würde ein kosmisches Jahr 365mal soviel sein, 25 920, also annähernd wiederum ein Jahr."
      ],
      [
        "Das aber ist die Zeit, in welcher die Sonne wiederum zurückkehrt zu dem­selben Sternbilde: 25 920 Jahre.",
        "Wenn in einem bestimmten Jahre die Sonne im Widder erscheint, nach 25 920 Jahren erscheint sie wiederum im Widder im Aufgang, denn die Sonne bewegt sich durch den ganzen Tierkreis im Laufe von 25920 Jahren."
      ],
      [
        "So also ist ein ganzes Menschen­leben herausgeatmet aus dem Kosmos, ein Atemzug des Kosmos, der sich genau zum kosmischen Werden, zum kosmischen Umschwung der Sonne im Tierkreis verhält, wie ein Atemzug zum Tagesleben.",
        "Eine tiefe innerliche Gesetzmäßigkeit!"
      ],
      [
        "Sie sehen, alles ist auf Rhythmus auf­gebaut.",
        "Wir atmen dreifach oder wenigstens stehen dreifach in einem Atmungsprozeß drinnen.",
        "Wir atmen zunächst durch unsere Lunge in den Elementen - in einem Rhythmus, der durch die Zahl 25920 an­gegeben wird."
      ],
      [
        "Wir atmen im ganzen Sonnensystem, wenn wir Auf- und Untergang der Sonne als parallellaufend zählen unserem Einschlafen"
      ],
      [
        "und Aufwachen.",
        "Wir atmen durch unser ganzes Leben hindurch in einem Rhythmus, der wiederum durch die Zahl 25920 bestimmt ist.",
        "Und endlich, das Weltenall atmet uns aus, atmet uns wieder ein in einem Rhythmus, der wiederum durch die Zahl 25920 bestimmt ist, bestimmt durch den Umlauf der Sonne um den Tierkreis."
      ],
      [
        "So sind wir hineingestellt in den ganzen sichtbaren Kosmos, dem nun der unsichtbare Kosmos zugrunde liegt.",
        "In diesen unsichtbaren Kosmos treten wir ein, wenn wir durch die Pforte des Todes treten.",
        "Rhythmisches Leben ist dasjenige Leben, das unserem Gefühlsleben zu­grunde liegt.",
        "In das rhythmische Leben des Kosmos treten wir ein in der Zeit, die wir durchleben zwischen dem Tod und einer neuen Geburt.",
        "Dieses rhythmische Leben liegt als unser ätherisches Leben bestimmend hinter dem Sinnesteppich ausgebreitet.",
        "Sehen würde man in dem Au­genblicke, wo man zum schauenden Bewußtsein kommt, diesenWelten­rhythmus, der gewissermaßen ein rhythmisch wogendes Weltenmeer ist, jetzt astralisch geartet.",
        "Und in diesem rhythmisch wogenden astra­lischen Meere sind auch die sogenannten Toten vorhanden, sind die Wesenheiten der höheren Hierarchien vorhanden, ist dasjenige vorhan­den, was zu uns gehört, was aber unter der Schwelle liegt, aus der nur die Gefühle heraufwogen, die verträumt werden, die Willensimpulse heraufwogen, die in ihrer eigenen Wirklichkeit verschlafen werden."
      ],
      [
        "Die Frage kann aufgeworfen werden - wir dürfen die Sache ver­gleichsweise, ohne in Teleologie zu verfallen, so sagen: Warum hat es die weisheitsvolle Weltenlenkung eingerichtet, daß der Mensch, so wie er nun einmal ist zwischen Geburt und Tod, nicht wahrnimmt, was da als rhythmisches Leben hinter dem Sinnesteppich liegt?",
        "Warum ist der Kopf des Menschen, der verborgene Kopf des Menschen, dem das Lungensystem entspricht, nicht geeignet zu einem entsprechenden Wahrnehmen?",
        "Ja, das führt auf eine Wahrheit, welche, man kann sagen, bis in unser Zeitalter von den entsprechenden okkulten Schulen als ein Geheimnis bewahrt worden ist, weil allerdings mit diesem Ge­heimnis andere Geheimnisse in Verbindung stehen, die nicht enthüllt werden sollen, sollten, bisher.",
        "Allein in unserer Zeit ist eben auch die Epoche gekommen, in der solche Dinge zum Bewußtsein der Mensch­heit gebracht werden müssen."
      ],
      [
        "Die okkulten Schulen, die da oder dort eingerichtet sind, bewahren solche Dinge aus Gründen, die jetzt nicht erörtert werden sollen, viel­fach heute noch, obwohl die Dinge heute notwendigerweise an das Menschenbewußtsein herangebracht werden sollen.",
        "Aber seit dem letz­ten Drittel des 19.",
        "Jahrhunderts sind Mittel und Wege gegeben, durch die dasjenige überholt werden kann, was die okkulten Schulen eigent­lich vielfach unrechtmäßigerweise zurückhalten.",
        "Das hängt zusammen mit dem Ereignis, von dem ich Ihnen gesprochen habe als fallend in den Herbst des Jahres 1879.",
        "Wir können nur den äußersten Saum dieses Geheimnisses für diesmal berühren.",
        "Allein schon dieser äußerste Saum dieses Geheimnisses gehört zu den bedeutsamsten Erkenntnissen des menschlichen Wesens.",
        "Ein Kopf ist es allerdings, den wir da in uns tragen als den Kopf eines zweiten Menschen, ein Kopf ist es - aber was zu diesem Kopf gehört, ist auch ein Leib, und der Leib, der dazugehört, der ist zunächst ein Tierleib.",
        "Der Mensch trägt also einen zweiten Men­schen in sich: dieser zweite Mensch hat einen richtig ausgebildeten Kopf, aber einen Tierleib daran, einen richtigen Kentaur.",
        "Der Kentaur ist schon eine Wahrheit.",
        "Er ist eben eine ätherische Wahrheit."
      ],
      [
        "Das Bedeutsame ist das, daß in dieser Wesenheit eine verhältnis­mäßig große Weisheit spielt, eine Weisheit, die sich auf den ganzen kos­mischen Rhythmus bezieht.",
        "Was der Kopf sieht, der diesem Kentaur angehört, das ist der kosmische Rhythmus, in dem auch der Mensch als Wesen, das zwischen Tod und neuer Geburt lebt, eingebettet ist.",
        "Es ist jener Weltenrhythmus, der hier in dreifacher Weise selbst zahlenmäßig gezeigt worden ist, jener Rhythmus, auf dem viele Geheimnisse des Kosmos beruhen.",
        "Dieser Kopf ist viel weiser als unser physischer Kopf.",
        "Alle Menschen tragen einen sehr weisen andern Menschen, eben den Kentaur, in sich.",
        "Aber zugleich ist dieser Kentaur, trotz seiner Weisheit, ausgerüstet mit allen wilden Instinkten der Tierheit."
      ],
      [
        "Jetzt werden Sie die weise Weltenlenkung verstehen.",
        "Sie konnte nicht dem Menschen ein Bewußtsein geben, das auf der einen Seite mächtig ist und den Weltenrhythmus durchschaut, aber auf der andern Seite ungebändigt ist, in wilden Trieben lebend.",
        "Aber was in der einen Inkarnation tierisch ist an diesem Kentaur, das wird - halten Sie das, was ich jetzt sage, mit andern Vorträgen zusammen, in denen ich das"
      ],
      [
        "Thema von einem andern Gesichtspunkte aus beleuchtet habe -, das wird in der nächsten Inkarnation gebändigt, indem er durch die Welt des Weltenrhythmus durchgeht zwischen Tod und neuer Geburt.",
        "Was unserem Lungensystem in der gegenwärtigen Inkarnation zugrunde liegt, was da verborgen wird, das erscheint als Ihr physischer Kopf, der dann allerdings herabgedämpft ist zu seinem beschränkten sinnlichen Wissen, und es erscheint in der nächsten Inkarnation als der ganze Mensch nun auch den wilden Trieben nach gebändigt.",
        "Was Kentaur in dieser Inkarnation ist, ist der sinnlich wahrnehmende Mensch in der nächsten Inkarnation."
      ],
      [
        "Und jetzt werden Sie ein anderes begreifen.",
        "Jetzt werden Sie be­greifen, warum ich gesagt habe, daß der Mensch zwischen dem Tod und einer neuen Geburt als unterstes Reich das tierische Reich hat, in dessen Kräften er Meister werden muß.",
        "Was muß er denn tun?",
        "Woran muß er denn teilnehmen zwischen zwei Inkarnationen?",
        "Er muß daran teilnehmen, den Kentauren, das Tierische in ihm für die nächste Inkar­nation ins Menschliche umzuwandeln.",
        "Dazu sind wirklich Kenntnisse notwendig, welche über die Impulse des ganzen tierischen Reiches sich erstrecken müssen, welche in ihrer Abschwächung atavistisch eigen gewesen sind den Menschen jenes Zeitalters, in dem der Chiron gelebt hat.",
        "Wenn auch die Erkenntnisse, von denen der Chiron spricht, Ab­schwächungen sind dieser Inkarnation, von dieser Art sind sie.",
        "Aber Sie sehen den Zusammenhang.",
        "Sie sehen, wozu der Mensch zwischen dem Tod und einer neuen Geburt dieses untere Reich braucht, in dem er Meister werden muß: er braucht es, weil er den Kentauren in einen Menschen umwandeln muß."
      ],
      [
        "Was die anthroposophisch orientierte Geisteswissenschaft darbietet, war bis jetzt eigentlich nur in einzelnen Lichtblitzen außerhalb der okkulten Schulen erlangt worden.",
        "Aber einzelne Menschen hat es immer gegeben, die auf solche Dinge wie durch Lichtblitze des Lebens ge­kommen sind.",
        "Besonders im 19.Jahrhundert kamen, ich möchte sagen vorahnend, einzelne Geister darauf, daß im Menschen drinnen so etwas mit wildgebändigten Trieben steckt.",
        "Es gibt Schriftsteller, die davon sprechen.",
        "Und aus der Art, wie sie davon sprechen, sieht man, wie sie erschrocken sind über diese Erkenntnis.",
        "Ja, so bequem geistig zu verdauen"
      ],
      [
        "wie die heutigen naturwissenschaftlichen Erkenntnisse, so bequem sind die hohen Wahrheiten nicht.",
        "Diese hohen Wahrheiten haben schon zuweilen die Eigenschaft, daß man vor ihrer Wirklichkeit erschrecken kann.",
        "Und es hat Geister im 19.",
        "Jahrhundert gegeben, die erschrocken sind, die furchtbar berührt gewesen sind, als sie wahrnahmen, was eigentlich aus dem manchmal verwirrt blickenden Auge des Menschen oder aus sonstigem am Menschen spricht.",
        "Einer der Schriftsteller des 19.",
        "Jahrhunderts hat sich drastisch ausgedrückt, indem er sagte: Jeder Mensch trägt eigentlich einen Mörder in sich. - Er meinte diesen Ken­tauren, der ihm unklar zum Bewußtsein gekommen ist."
      ],
      [
        "Daß auf dem Grunde der Menschennatur Rätselhaftes ist, über das der Mensch sich nach und nach aufklären muß, das ist etwas,was immer wieder und wieder betont werden muß.",
        "Mit Mut und Gelassenheit müssen diese Dinge ins Auge gefaßt werden.",
        "Aber sie dürfen nicht ver­trivialisiert werden, denn sie rücken das Menschheitsbewußtsein an den großen Ernst des Lebens heran.",
        "Und den Ernst des Lebens zu durch­schauen, das ist dasjenige, was den Menschen vorgesetzt ist für diese Zeit, die da kommt, die jetzt durch so furchtbare Zeichen eingetreten ist."
      ],
      [
        "Dies ist die eine Seite, durch die ich eine gewisse Betrachtung vor­bereiten will, die wir dann demnächst fortsetzen werden.",
        "Die andere Seite ist die folgende: Der Mensch tritt durch die Todespforte; ich habe ja das letzte Mal davon gesprochen, wie verschieden das ganze Erleben dann wird, indem ich Ihnen angedeutet habe, wie der Verkehr mit einem Toten eigentlich so vor sich geht, daß dasjenige, was man selber ihm mitteilt, wie aus ihm spricht, und dasjenige, was er einem mitteilt, wie aus den Tiefen des eigenen Wesens heraus spricht.",
        "Es kehrt sich geradezu das gegenseitige Verhältnis um im Verkehr mit dem Toten.",
        "Wenn Sie hier mit einem Menschen verkehren, da sprechen Sie.",
        "Sie hören sich dasjenige sprechen, was Sie dem andern mitteilen.",
        "Von ihm hören Sie dasjenige, was er Ihnen mitteilt.",
        "Wenn Sie mit dem Toten sich verständigen, dann dringt aus Ihrer eigenen Seele herauf dasjenige, was er sagt, und wie durch ein Echo tönt von ihm zurück Ihnen ent­gegen, was Sie ihm mitgeteilt haben.",
        "An sich nehmen Sie es gar nicht wahr, was Sie ihm mitgeteilt haben: an ihm nehmen Sie es wahr.",
        "Das wollte ich nur als ein Beispiel angeben für den radikalen Unterschied,"
      ],
      [
        "der da besteht zwischen der physischen Welt hier, in der wir zwischen Geburt und Tod leben, und der Welt, in der wir leben zwischen dem Tod und einer neuen Geburt."
      ],
      [
        "Hinein schauen wir, indem wir diese Welt von der einen Seite an­schauen: indem wir den Sinnesteppich durchschauen, schauen wir in den Rhythmus der Welt.",
        "Aber dieser Rhythmus hat zwei Seiten.",
        "Ich will Ihnen diese zwei Seiten des Rhythmus schematisch dadurch dar­stellen, daß ich vielleicht eine Anzahl von Sternen, sagen wir Planeten"
      ],
      [
        "# Bild s. 80"
      ],
      [
        "zunächst, hier aufzeichne (rot).",
        "Das sei eine Anzahl von Sternen, Pla­neten.",
        "Meinetwillen sei das das Planetensystem, das zu unserer Erde gehört.",
        "Der Mensch geht durch dieses Planetensystem durch in der Zeit, die zwischen dem Tod und einer neuen Geburt liegt.",
        "Es gibt einen Zyklus von Vorträgen, der gedruckt ist, in dem Sie sich über diese Dinge unterrichten können.",
        "Der Mensch geht durch das System durch.",
        "Aber indem er durch das, was noch sichtbare Welt ist, durchgeht, kommt er in der Zeit zwischen dem Tod und einer neuen Geburt auch in die Welt, die nicht mehr sichtbar ist, die nicht einmal räumlich ist.",
        "Da redet man allerdings von schwierigen Dingen, weil der Mensch gewohnt ist, nach den Erfahrungen hier in der physischen Welt, wo er sich überhaupt"
      ],
      [
        "etwas vorstellt, sich Räumliches vorzustellen.",
        "Aber es liegt eine Welt jenseits des Sinnlich-Wahrnehmbaren, die allerdings nicht mehr räum­lich ist.",
        "Ich kann sie schematisch nur räumlich ausdrücken."
      ],
      [
        "Die Alten haben gesagt: Jenseits der Planeten liegt der Fixstern­himmel - das ist zwar verkehrt gesagt, darauf kommt es aber jetzt nicht an - und jenseits davon liegt nun die übersinnliche Welt. - Die Alten stellten sie räumlich dar, aber das ist nur eine bildliche Vorstellung davon (siehe Zeichnung, blau)."
      ],
      [
        "Ist der Mensch eingetreten in diese übersinnliche Welt in der Zeit, die zwischen dem Tod und einer neuen Geburt liegt, dann kann man sagen, trotzdem das auch wieder bildlich gesprochen ist, der Mensch befindet sich dann jenseits der Sterne, und die Sterne selbst dienen ihm zu einer Art von Lesen.",
        "Also die Sterne dienen dem Menschen zwischen dem Tod und einer neuen Geburt zu einer Art von Lesen."
      ],
      [
        "Machen wir uns das ganz klar, wie das ist.",
        "Wie lesen wir, wenn wir hier auf der Erde lesen?",
        "Wenn wir hier auf der Erde lesen, haben wir ungefähr zwölf Konsonanten und sieben Vokale mit verschiedenen Nuancen."
      ],
      [
        "Diese Buchstaben setzen wir in der mannigfaltigsten Weise zu Worten zu­sammen.",
        "Wir werfen sie durcheinander, die Buchstaben.",
        "Stellen Sie sich vor, wie der Setzer im Setzkasten die Dinge durcheinander wirft, damit Worte daraus werden."
      ],
      [
        "Aus den bestimmten Buchstaben, die wir haben, werden ja alle Worte.",
        "Was für den Menschen, der hier auf dem phy­sischen Plane ist, diese Buchstaben sind, diese ungefähr zwölf Konso­nanten und sieben Vokale mit den verschiedenen Nuancen, das sind für den Toten die Fixsterne des Tierkreises und die Planeten."
      ],
      [
        "Die Fix­sterne des Tierkreises sind die Konsonanten und die Planeten sind die Vokale.",
        "Ist man jenseits des Sternenhimmels, dann sieht man peri­pherisch.",
        "Der Mensch sieht zentral, wenn er zwischen der Geburt und dem Tode ist; er hat hier sein Auge, und dann sieht er so ausstrahlend nach verschiedenen Punkten hin."
      ],
      [
        "Es ist am schwersten vorzustellen, daß das umgekehrt ist nach dem Tode: da sieht man peripherisch.",
        "Man ist eigentlich im Umkreise und man sieht von außen die Sterne des Tier-kreises, die Konsonanten, und die Planeten, die Vokale."
      ],
      [
        "Und so sieht man von außen herein auf das, was auf der Erde vorgeht.",
        "Und je nach­dem man irgendeinen Teil seines Wesens belebt, sieht man - Sie müssen"
      ],
      [
        "sich jetzt das nicht von der Erde aus denken, sondern umgekehrt, auf die Erde herunterschauend - durch den Stier und Mars auf die Erde nieder, oder Sie sehen durch den Stier durch zwischen Mars und Jupiter.",
        "Sie lesen, indem Sie als Toter die Erde umkreisen, Sie lesen mit Hilfe des Sternensystems."
      ],
      [
        "Nur müssen Sie sich dieses Lesen jetzt etwas anders vorstellen.",
        "Nicht wahr, wir könnten auch anders lesen, nur wäre es nicht technisch so bequem eingerichtet wie unser gegenwärtiges Lese-system.",
        "Man könnte auch anders lesen."
      ],
      [
        "Man könnte so lesen, daß wir die Buchstaben hintereinander haben: a, b, c, d, e, f, g und so weiter -oder nach einem andern System - und statt daß wir sie im Setzkasten um und um werfen, könnten wir so lesen, daß, wenn zum Beispiel «der» gelesen werden soll, ein Lichtstrahl fällt auf das «der»; soll «geht» ge­lesen werden, fällt ein Lichtstrahl auf «geht».",
        "Es könnte also die Rei­henfolge der Buchstaben erst da sein, und sie könnten so hintereinander beleuchtet sein."
      ],
      [
        "Es wäre technisch nicht so bequem, aber Sie könnten sich immerhin ein Erdenleben vorstellen, in dem das Lesen so bewerk­stelligt würde, daß man vor sich nimmt ein Alphabet, und dann gäbe es irgendeine Vorrichtung, durch die immer beleuchtet wird ein Buch­stabe; dann liest man hintereinander die Aufeinanderfolge der beleuch­teten Buchstaben - und es hat den Goetheschen «Faust» ergeben.",
        "Das ist natürlich nicht so ohne weiteres vorzustellen, doch eine Möglichkeit gibt es, sich so es vorzustellen, nicht wahr?"
      ],
      [
        "# Bild s. 82"
      ],
      [
        "Aber so liest der Tote mit Hilfe des Sternensystems: Die Fixsterne stehen fest, und er bewegt sich, denn er ist in der Bewegung drinnen.",
        "Die Fixsterne stehen fest, er bewegt sich.",
        "Soll er den Löwen über dem"
      ],
      [
        "Jupiter lesen, so bewegt er sein Wesen so, daß ihm der Löwe über dem Jupiter steht, wie wir «der» lesen, indem wir das d mit dem e zusam­menbringen und so weiter.",
        "Dieses Lesen der Erdenverhältnisse aus dem Kosmos - wozu der unsichtbare Kosmos gehört - besteht also darinnen, daß das, was geistig den Sternen zugrunde liegt, von den Toten gelesen werden kann.",
        "Nur ist das ganze System auf Ruhe eingerichtet; dieses ganze göttliche System des Lesens vom Kosmos herein ist auf Ruhe ein­gerichtet.",
        "Was heißt das?",
        "Das heißt: Eigentlich sollten nach den Inten­tionen gewisser Wesen der höheren Hierarchien die Planeten ruhig sein, sollten eine ruhige Form abgeben.",
        "Dann würde bloß das Wesen, das sich draußen lesend verhält, in Bewegung sein.",
        "Es würde vom Welten-all aus auf der Erde unbedingt richtig gelesen werden können, wenn die Planeten in Ruhe wären, eine ruhende Lage hätten."
      ],
      [
        "Das sind sie nicht!",
        "Warum sind sie es nicht?",
        "Sie wären es, wenn die Weltenschöpfung so gegangen wäre, daß die Geister der Form, die Exusiai nach unserer Benennung, die Welt allein zustande gebracht hätten.",
        "Doch es beteiligten sich, hereingreifend in die Welt, luziferische Geister, wie Sie wissen.",
        "Luziferische Geister brachten das, was Gesetz war während der Mondengestalt der Erde - wo gewisse Dinge, die dann übergingen in die Macht der Geister der Form, den Geistern der Bewegung unterstanden -, dieses System der Bewegung herüber aus der Mondenzeit der Erde: sie brachten die Planeten in Bewegung.",
        "Daß die Planeten in bestimmter Bewegung sind, ist ein Luziferisches im Welten-raum.",
        "Das bringt in einer gewissen Beziehung in die elohimistische Ord­nung Unruhe hinein; das bringt in das Weltenall, in den Kosmos ein luziferisches Element hinein.",
        "Es ist das jenes luziferische Element, das der Mensch zwischen dem Tod und einer neuen Geburt kennenlernen muß; gerade dadurch kennenlernen muß, daß er lernt abzuziehen ge­wissermaßen von dem, was er liest, das, was aus der Bewegung der Planeten, der Irr- oder Wandelsterne kommt.",
        "Das muß er abziehen, das muß er abrechnen; dann bekommt er das Richtige zustande."
      ],
      [
        "Man lernt in der Tat zwischen dem Tod und einer neuen Geburt viel kennen über das Walten und Weben des Luziferischen im Kosmos.",
        "Und solche Dinge, wie der Gang der Wandelsterne, der Gang der Planeten, hängen mit Luziferischem zusammen."
      ],
      [
        "Das ist die andere Seite, auf die ich habe aufmerksam machen wol­len.",
        "Sie sehen aber daraus, wie jenes andere Leben, das wir durchleben zwischen dem Tod und einer neuen Geburt, mit unserem hiesigen Leben zusammenhängt.",
        "Man möchte sagen, die Welt hat zwei Seiten.",
        "Hier zwischen der Geburt und dem Tode sieht man die eine Seite durch die Sinne.",
        "Von der abgewendeten Seite aus schaut man sie mit dem Seelen-auge an in der Zeit zwischen dem Tod und einer neuen Geburt.",
        "Und zwischen dem Tod und einer neuen Geburt lernt man die Verhältnisse hier im Irdischen mit denen der geistigen Welt zusammenhängend lesen."
      ],
      [
        "Man mache sich so etwas nur ganz klar, man versuche, sich hinein­zuversetzen in diese Verhältnisse.",
        "Man wird sich gestehen müssen, daß es allerdings eine tiefe Bedeutung hat, wenn man davon spricht, daß die Welt, die der Mensch zunächst durch seine Sinne und durch seinen Verstand kennenlernt, eine Maja ist.",
        "Sobald man an die wirkliche Welt herantritt, verhält sich allerdings die Welt, die man kennt, zu dieser wirklichen Welt so, wie das, was im Spiegel drinnen erscheint, zu dem sich verhält, was vor dem Spiegel ist als Lebendiges und sich im Spiegel bloß spiegelt."
      ],
      [
        "Nun, wenn Sie hier einen Spiegel haben und dadrinnen sind ver­schiedene Gestalten, so weist das darauf hin, daß außerhalb des Spiegels Gestalten da sind, die sich spiegeln.",
        "Nehmen Sie an, Sie schauen in den Spiegel hinein als unbeteiligter Zuschauer. (Es wird gezeichnet.) Die zwei Gestalten, die ich da aufgezeichnet habe, die prügeln sich, das sehen Sie, die prügeln sich.",
        "Das weist zwar darauf hin, daß diejenigen Gestalten, die sich spiegeln, irgend etwas tun, aber Sie werden nicht behaupten dürfen, daß die Gestalt A im Spiegel dadrinnen die Gestalt B im Spiegel dadrinnen durchprügelt.",
        "Was da im Spiegel drinnen er­scheint, das gibt das Bild des Prügelns, weil die Gestalten außer dem Spiegel irgend etwas tun.",
        "Sind Sie der Meinung, daß die Gestalt A, die da im Spiegel drinnen ist als Spiegelbild, der Gestalt B, die im Spiegel drinnen ist, etwas antut, dann sind Sie in einer ganz irrtümlichen Mei­nung befangen.",
        "Sie können nicht Beziehungen, Verhältnisse aufstellen zwischen den Spiegelbildern, sondern Sie können nur sagen: Das, was sich in den Spiegelbildern ausdrückt, das weist hin auf irgend etwas in der Welt der Wirklichkeit, die sich spiegelt. - Aber die Welt, die der"
      ],
      [
        "Mensch als gegebene hat, ist ein Spiegel, ist eine Maja, und in dieser Welt redet der Mensch von Ursachen und Wirkungen.",
        "Wenn Sie in dieser Welt von Ursachen und Wirkungen reden, so ist das gerade so, wie wenn Sie glauben würden, daß das Spiegelbild A dadrinnen das Spiegelbild B durchprügelt.",
        "In den wirklichen Wesen, die sich spiegeln, geschieht etwas; aber in dem Spiegelbild A, in dem Spiegelbild B liegen nicht die Impulse des Sich-Prügelns."
      ],
      [
        "Gehen Sie die ganze Naturordnung durch: sie ist zunächst, so wie sie den Sinnen erscheint, eine Maja, ein Spiegelndes, ein Gespiegeltes.",
        "Die Wirklichkeit liegt unter der Grenze, die ich angegeben habe, die zwischen dem Vorstellungsleben und dem Gefühlsleben liegt.",
        "Selbst Ihre eigene Wirklichkeit ist in dem, was das wache Bewußtsein enthält, gar nicht einmal drinnen.",
        "Aber diese eigene Wirklichkeit ist in der Geistwirklichkeit drinnen, in welche die träumende und schlafende Gefühls- und Willenskraft hinuntertaucht.",
        "Also von ursächlicher Not­wendigkeit in der Maja zu sprechen, ist, wie Sie sehen, ein Unding; ein Unding auch, in der historischen Folge der Ereignisse von Ursache und Wirkung zu sprechen.",
        "Ein Unding!",
        "Zu dem, was ich gesagt habe, füge ich hinzu, daß es ein Unding ist, zu sagen, die Ereignisse von 1914 sind eine Folge der Ereignisse von 1913,1912 und so weiter.",
        "Das ist geradeso gescheit, wie wenn man sagen würde: Ach, dieser A im Spiegel, der ist ein schlechter Kerl, der haut den B dadrinnen durch! - Auf die wahre Wirklichkeit zu gehen, das ist das, worauf es ankommt.",
        "Und die wahre Wirklichkeit liegt unter der Schwelle, die überschritten wird nach unten von unserer Gefühls- und Willenswelt, die aber nicht in das gewöhn­liche wachende Bewußtsein tritt.",
        "Und da lebt auch der Kentaur, von dem ich gesprochen habe."
      ],
      [
        "Sie sehen, daß man den Begriff: Irgend etwas mußte geschehen -Irgend etwas war notwendig - anders fassen muß, als man ihn in der gewöhnlichen Geschichte oder gar in der Naturwissenschaft faßt; daß man die Frage aufwerfen muß: Welches sind die wirklichen Wesen, die dasjenige, was in einem späteren Zeitpunkte auf einen früheren folgt, hervorgebracht haben? - Die sogenannten historischen Ereignisse von vorher sind nur Spiegelbilder, die können das nicht bewirken, was nachher geschieht."
      ],
      [
        "Das ist aber wiederum die eine Seite der Sache.",
        "Die andere wird Ihnen klar, wenn Sie bedenken, daß eigentlich im Vorstellungs- und Sinnesleben der wachen Wirklichkeit nur ein Spiegel des wahren Le­bens, eine Maja gegeben ist.",
        "Diese Maja kann aber nichts bewirken.",
        "Diese Maja kann nicht im Stande einer Causa sein, irgendeine wirkliche Ursache sein.",
        "Der Mensch ist aber in der Lage, sich von seinen reinen Vorstellungen zu Handlungen bestimmen zu lassen.",
        "Das ist eine Er­fahrungstatsache des Lebens, wenn der Mensch nicht durch Leiden­schaften, Triebe, Begierden, sondern durch reine Vorstellungen getrie­ben wird.",
        "Das kann sein, und das ist möglich; der Mensch kann sich von reinen Idealen, von reinen Ideen impulsieren lassen.",
        "Aber die können selbst nichts bewirken.",
        "Ich kann also eine Handlung ausführen unter dem Einfluß einer reinen Idee; aber die Idee kann nichts bewirken."
      ],
      [
        "Vergleichen Sie noch einmal, um das einzusehen, die Idee mit einem Spiegelbild.",
        "Ja, das Bild im Spiegel, das kann nicht bewirken, daß Sie davonlaufen.",
        "Es muß Ihnen nicht gefallen, oder es muß etwas sein, was gar nicht mit dem Spiegelbild in irgendeiner Beziehung steht, wenn Sie davonlaufen."
      ],
      [
        "Das Spiegelbild selbst kann nicht eine Peitsche nehmen und bewirken, daß Sie davonlaufen.",
        "Das kann keine Causa sein.",
        "Wenn aber der Mensch unter dem Einfluß seiner Spiegelbilder, also seiner Ideen handelt, dann handelt er aus der Maja heraus, handelt er eben aus dem Weltenspiegel heraus: Er muß es sein, der handelt, deshalb handelt er dann frei."
      ],
      [
        "Wenn er seinen Leidenschaften folgt, handelt er nicht frei; nicht einmal, wenn er seinen Gefühlen folgt, handelt er frei.",
        "Wenn er seinen Vorstellungen, die bloß Spiegelbilder sind, folgt, han­delt er frei."
      ],
      [
        "Aus diesem Grunde ist es, warum ich in der «Philosophie der Freiheit» ausgeführt habe, daß der Mensch, wenn er reinen Ideen folgt, dem reinen Denken folgt, ein frei handelndes Wesen ist, weil reine Ideen eben nichts bewirken können, also das Bewirken von an­derswoher kommen muß.",
        "Ich habe diese Sache mit diesem Bilde noch einmal durchgeführt in meinem Buche «Vom Menschenrätsel»."
      ],
      [
        "Gerade weil dasjenige, was uns zunächst umgibt, eine Maja ist, die nichts be­wirken kann, wir aber unter dem Einflusse dieser Maja handeln, sind wir freie Menschenwesen.",
        "Unsere Freiheit beruht darauf, daß unsere Wahrnehmungswelt Maja ist."
      ],
      [
        "Unser Wesen vermählt sich mit der Maja"
      ],
      [
        "und ist dadurch ein freies Wesen.",
        "Wäre die Welt, die wir wahrnehmen, Wirklichkeit, dann würde diese Wirklichkeit uns zwingen, dann wären wir nicht freie Wesen.",
        "Wir sind freie Wesen gerade deshalb, weil die Welt, die wir wahrnehmen, nicht eine Wirklichkeit ist, daher uns auch nicht zwingen kann, ebensowenig wie uns ein Spiegelbild zwingen kann davonzulaufen.",
        "Darinnen beruht das Geheimnis des freien Men­schen, daß man den Zusammenhang einsieht zwischen der Wahrneh­mungswelt als einer Maja, der bloßen Spiegelung einer Wirklichkeit, und dem Impulsieren des Menschen durch sich selbst.",
        "Der Mensch muß sich selber impulsieren, wenn dasjenige, unter dessen Eindruck er han­delt, ihn eben nicht bestimmt."
      ],
      [
        "Die Freiheit läßt sich streng beweisen, wenn man diesen Beweis auf der Grundlage sucht, daß die Welt, so wie sie als Wahrnehmung ge­geben ist, ein Spiegelbild ist und nicht eine Wirklichkeit."
      ],
      [
        "Das sind die vorbereitenden Ideen, die ich Ihnen mitteilen wollte über dasjenige, was auf dem Grunde der Menschennatur liegt.",
        "Was Wirklichkeiten wahrnehmen würde, aber zur Wahrnehmung in einer Inkarnation noch nicht reif ist, sondern abgeschwächt erst in der näch­sten Inkarnation Mensch wird, der Kentaur würde Wahrheit, würde Wirklichkeit wahrnehmen; aber der Kentaur nimmt eben noch nicht wahr.",
        "Dasjenige, was heute wahrgenommen wird, ist noch keine Wirk­lichkeit.",
        "Aber der Mensch kann sich bestimmen lassen durch dasjenige in seinem Wesen, was nicht mehr - oder noch nicht - ein Kentaur ist:"
      ],
      [
        "dann handelt er als ein freies Wesen.",
        "Das Geheimnis unserer Freiheit hängt innig zusammen mit der Bändigung unserer Kentaurennatur.",
        "Unsere Kentaurennatur verhält sich so zu uns, daß sie angekettet, ge­fesselt ist, damit wir nicht die Wirklichkeit des Kentauren, sondern eine bloße Maja wahrnehmen.",
        "Wenn wir uns durch die Maja impul­sieren, sind wir frei."
      ],
      [
        "Das ist von dieser Seite aus gesehen.",
        "Von der andern Seite lernen wir erkennen die Welt zwischen dem Tod und einer neuen Geburt, indem dasjenige, was uns sonst als Kosmos umgibt, zusammenschrumpft zu einem Lesemittel im Kosmos, dessen Abglanz hier die physischen Buch­staben sind.",
        "Daß mehr Buchstaben heute vorhanden sind in den Spra­chen - die finnische Sprache hat heute noch immer bloß zwölf Konsonanten -,"
      ],
      [
        "das ist nur, weil Nuancen geschaffen werden; aber im wesent­lichen gibt es zwölf Konsonanten und sieben mit verschiedenen Nuan­cen behaftete Vokale.",
        "Die verschiedenen Nuancen der Vokale sind dasjenige, was als Luziferisches dazugekommen ist.",
        "Was die Vokale in Bewegung bringt, das entspricht der Planetenbewegung."
      ],
      [
        "Sie sehen den Zusammenhang desjenigen, was im Kleinen im Men­schenleben spielt: das Lesen, der Zusammenhang zwischen dem Lesen der Buchstaben, die wir hier auf dem Papiere haben, und demjenigen, was im Kosmos draußen lebt.",
        "Der Mensch ist aus dem Kosmos heraus geboren, nicht bloß wiederum eine Wirkung desjenigen, was ihm in der Vererbung vorangegangen ist."
      ],
      [
        "Das sind so einige Grundlagen, um allmählich zu dem wirklichen Begreifen von Freiheit und Notwendigkeit von historischem, sozialem und ethisch-moralischem Geschehen zu kommen."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG Dornach. 15. Dezember 1917",
    "paragraphs": [
      "Wenn wir dasjenige durchdringen wollen, was den beiden in das Men­schenleben eingreifenden Impulsen, der sogenannten Freiheit und der sogenannten Notwendigkeit, zugrunde liegt, dann müssen wir zu den mancherlei Voraussetzungen, die wir schon geschaffen haben, einige andere noch hinzufügen. Und das will ich heute tun, damit wir dann morgen in der Lage sind, gewissermaßen die Konklusion, den Schluß in bezug auf den Freiheits- und Notwendigkeitsbegriff im mensch­lichen, sozialen, sittlichen und geschichtlichen Wirken zu ziehen.",
      "Wenn man solche Dinge bespricht, dann kommt eigentlich immer mehr in Betracht, daß die Menschen, und namentlich die Menschen der Gegen­wart danach streben, die höchsten, die wichtigsten, die bedeutsamsten Dinge mit den allereinfachsten Begriffen und Vorstellungen zu um­fassen. Um eine Uhr zu begreifen - ich habe das öfters schon erwähnt -, dazu hält man mancherlei Kenntnisse für notwendig, und man wird nicht ohne einen Schimmer davon zu haben, wie Räder zusammen­wirken oder dergleichen, aus dem Stegreif heraus den Gang einer Uhr im einzelnen erklären wollen.",
      "Ein Sachverständiger über Freiheit und Notwendigkeit will man eigentlich in jeder Lage des Lebens sein, ohne über diese Dinge etwas zugrunde Liegendes gelernt zu haben. Über die allerwichtigsten, allerwesentlichsten Dinge, die nur eingesehen werden können im ganzen Zusammenhange mit der Menschennatur, möchte man sich am liebsten nicht unterrichten und alles mögliche wie von selbst wissen und beurteilen.",
      "Das ist insbesondere so die Sehnsucht un­serer Zeit. Wenn geltend gemacht wird, daß der Mensch eine kompli­zierte, eine mannigfaltigst zusammengesetzte Wesenheit ist, eine Wesen­heit, die auf der einen Seite tief eintaucht in alles das, was mit dem physischen Plane zusammenhängt, auf der andern Seite wiederum see­lisch tief eintaucht in all das, was mit den geistigen Welten zusammen­hängt, dann wird gar leicht erwidert, daß solche Dinge trocken, ver­standesmäßig seien, daß man die allerwichtigsten und wesentlichsten Dinge in einer ganz andern Weise auffassen müsse.",
      "Die Welt wird kennenlernen müssen - sie lernt es vielleicht doch gerade durch die gegenwärtigen katastrophalen Ereignisse schon ein wenig -, was alles im Menschen und in seinem Zusammenhange mit dem Gang der Weltenentwickelung Verborgenes liegt. Wir haben seit Jahren betont, daß wir dasjenige im Rohen unterscheiden können im Menschen, was man seine physische Natur nennt, seinen physischen Leib, seinen Ätherleib, den Bildekräfteleib, wie ich ihn nenne, seinen astralischen Leib, der schon Seelisches ist, und das eigentliche Ich.",
      "Wir haben nun in den letzten Zeiten von den verschiedensten Ge­sichtspunkten her betont, daß der Mensch, so wie er lebt vom Auf­wachen bis zum Einschlafen, also im gewöhnlichen wachen Tages-bewußtsein, eigentlich in Wirklichkeit nur etwas weiß von den Ein­drücken seiner Sinneswahrnehmungen und noch von seinen Vorstellun­gen, daß er aber den eigentlichen Inhalt seines Gefühlslebens verträumt, und den eigentlichen Inhalt seines Willenslebens verschläft. Traum und Schlaf dehnen sich herein in die gewöhnliche Welt des Wachens, und mehr bewußt als eines Traumes sind wir uns auch unseres Gefühlslebens nicht im gewöhnlichen Wachbewußtsein. Mehr bewußt als im traum-losen Schlafe ist sich der Mensch seines wirklichen Willensinhaltes nicht. Denn durch unsere Gefühle, durch unseren Willensinhalt tauchen wir in dieselbe Welt hinein - das haben wir in diesen Betrachtungen betont - in welcher wir gemeinschaftlich mit den Toten unter den Wesenheiten der höheren Hierarchien, der Angeloi, Archangeloi, Archai und so weiter leben. Sobald wir in einem Gefühle leben - und wir leben ja fortwährend in Gefühlen -, lebt in der Sphäre, in dem Gebiete dieses Fühlens alles dasjenige mit, was im Reiche der Toten ist.",
      "Nun kommt ein anderes dazu. Wir sprechen im gewöhnlichen wa­chen Bewußtseinsleben von unserem Ich. Aber von diesem Ich können wir eigentlich mit dem gewöhnlichen Wachbewußtsein nur in recht uneigentlichem Sinne sprechen. Denn welche Natur und Wesenheit hat eigentlich dieses Ich? Es kann nicht erkannt werden im gewöhnlichen Wachbewußtsein. Taucht das schauende Bewußtsein in das wahre We­sen des Ich ein, dann ist das wahre Ich des Menschen willensartiger Natur. Das, was der Mensch im gewöhnlichen Bewußtsein hat, ist nur die Vorstellung des Ich. Daher wird es dem naturforscherischen Psy­chologen",
      "leicht, dieses Ich überhaupt wegzuleugnen, obwohl anderer­seits dieses Wegleugnen ein wirklicher Unsinn ist. Solche Naturforscher und Psychologen sprechen davon, daß das Ich sich eigentlich nach und nach heranbilde, daß der Mensch im Verlauf seiner individuellen Ent­wickelung zu diesem Ich komme. Er kommt nicht zu dem Ich, sondern zu der Ich-Vorstellung auf diese Art. Und es ist leicht hinwegzuleug­nen, weil es eben im gewöhnlichen Bewußtsein nur eine Vorstellung, ein Spiegelbild des wirklichen, wahren, echten Ich ist. Das echte Ich lebt in derselben Weltensphäre, in der die wahre Wirklichkeit unseres Willens lebt. Und das, was wir den astralischen Leib nennen, was wir als das eigentliche Seelenleben bezeichnen können, das wiederum lebt in derselben Sphäre, in der da lebt unser Gefühlsleben. Wenn Sie die beiden Dinge zusammennehmen, die wir so betrachtet haben, können Sie daraus wiederum ersehen, daß wir mit unserem Ich und mit un­serem astralischen Leib untertauchen in dasselbe Gebiet, das wir mit den Toten gemeinschaftlich haben. In dem Augenblicke, wo wir hell­seherisch in unser wahres Ich hinuntersteigen, sind wir ebenso unter den Ichen der Toten wie unter den Ichen der sogenannten Lebendigen.",
      "So etwas muß man sich nur ganz klarmachen, um voll einzusehen, wie sehr der Mensch mit seinem gewöhnlichen Bewußtsein in der soge­nannten Scheinwelt, oder wie man es mit einem orientalischen Aus­drucke nennt, in der Maja lebt. Wir leben wachbewußt in unserer Sinnes- und in unserer Vorstellungswelt. Aber die Sinnesimpulse, die geben uns nur den Teil der Welt, der als Natur sich ausbreitet. Und unsere Vorstellungswelt gibt uns auch nichts anderes als dasjenige in uns, was unserer Natur angemessen ist, aber zwischen der Geburt und dem Tode. Dasjenige, was unsere ewige Natur ist, das tritt im Grunde gar nicht aus der Welt heraus, die wir mit den Toten gemeinschaftlich haben. Das verbleibt im Grunde genommen in der Welt, in der die Toten auch sind, wenn wir durch die Verkörperung in das Leben des physischen Planes eintreten.",
      "Um aber diese Dinge voll zu verstehen, haben wir nötig, gewisse Begriffe aufzunehmen, die - man kann schon nichts dafür, das sagen zu müssen, weil die Dinge eben so sind - nicht ganz leicht zu durch­denken sind, bei denen man sich, um sie zu durchdenken, Mühe geben",
      "muß. Solche Begriffe hat zunächst der Mensch im Verlaufe seines ge­wöhnlichen wachen Bewußtseins nicht. Der Mensch kennt im gewöhn­lichen wachen Bewußtsein das, was räumlich ausgedehnt ist, was in der Zeit verläuft. Und er möchte eigentlich mit dem zufrieden sein, was räumlich ausgedehnt ist und was in der Zeit verläuft. Krankt ja sogar der Mensch vielfach daran, sich auch dasjenige, was in der geistigen Welt enthalten ist, möglichst räumlich zu denken, wenn auch nebulos, wenn auch dünn und nebelhaft, aber er möchte es doch irgendwie sich räumlich denken: räumlich herumfliegende Seelen und dergleichen möchte er sich denken. Man muß über die Begriffe von Raum und Zeit hinausgehen zu komplizierteren Begriffen, wenn man in diese Dinge wirklich eindringen will. Und da möchte ich Ihnen denn heute etwas andeuten, was wichtig ist zur Erfassung des menschlichen Gesamtlebens.",
      "Fassen wir noch einmal ins Auge - wie gesagt, im Rohen -, daß wir diese vierfache Natur zunächst haben: den physischen Leib, den Bilde-kräfte- oder Ätherleib, den astralischen Leib und das Ich. Wenn man so vom Standpunkte des gewöhnlichen wachen Bewußtseins aus redet und frägt: Wie alt ist eigentlich ein Mensch, dieser bestimmte Mensch A, wie alt ist er? - Nun, da wird irgend jemand sein Alter angeben, sagen wir fünfunddreißig Jahre, und er glaubt, damit etwas Ernst­haftes gesagt zu haben. Er hat auch für den physischen Plan und das gewöhnliche Wachbewußtsein etwas Ernsthaftes damit gesagt, daß er fünfunddreißig Jahre alt sei. Aber für die geistige Welt, also für die Gesamtwesenheit des Menschen, ist damit nur teilweise etwas gesagt. Denn Sie können eigentlich, wenn Sie sagen, ich bin fünfunddreißig Jahre alt, dies nur für Ihren physischen Leib sagen. Sie müßten sagen: Mein physischer Leib ist fünfunddreißig Jahre alt - dann würde die Sache stimmen. Für den ätherischen oder Bildekräfteleib, für die andern Glieder der menschlichen Wesenheit haben Sie aber damit noch gar nichts gesagt. Denn daß Ihr Ich zum Beispiel auch fünfunddreißig Jahre alt sein soll, wenn Ihr physischer Leib fünfunddreißig Jahre alt ist, das ist eine bloße Illusion, das ist sogar eine reine Phantasterei. Denn sehen Sie, hier tritt auf der Begriff verschieden geschwinder, ver­schieden schneller Entwickelung der verschiedenen Glieder der mensch­lichen Natur.",
      "Das können Sie sich durch folgende Zahlen klarmachen. Der Mensch wird, sagen wir sieben Jahre alt; das heißt aber nichts anderes als: sein physischer Leib ist sieben Jahre alt geworden. Dann ist deshalb sein Ätherleib, sein Bildekräfteleib noch nicht sieben Jahre alt, sondern sein Bildekräfteleib macht nicht so schnell mit; der ist noch nicht so alt ge­worden.",
      "Man kommt auf diese Dinge nur deshalb nicht, weil man die Zeit sich eben so als einen einheitlich dahinlaufenden Strom vorstellt und man sich gar nicht denken kann, daß innerhalb der Zeit verschie­denes mit verschiedener Geschwindigkeit vorwärtsgeht. Dieser phy­sische Leib, der sieben Jahre ist, der hat sich mit einer gewissen Ge­schwindigkeit entwickelt.",
      "Langsamer hat sich entwickelt der Ätherleib, noch langsamer der astralische Leib, und am langsamsten das Ich. Dieser Ätherl eib ist erst fünf Jahre drei Monate alt, wenn der physische Leib sieben Jahre alt ist, weil er ein langsameres Tempo durchmacht.",
      "Der astralische Leib ist drei Jahre sechs Monate alt. Und das Ich ist ein Jahr neun Monate alt. So daß Sie sich sagen müssen, wenn ein Kind sieben Jahre alt ist, so ist sein Ich erst ein Jahr neun Monate alt.",
      "Es macht dieses Ich eine langsamere Entwickelung durch auf dem phy­sischen Plane. Es geht dieses Ich auf dem physischen Plane ein lang­sameres Tempo, jenes langsamere Tempo, welches auch das Tempo ist, das man gemeinschaftlich mit den Toten durchleben kann.",
      "Warum faßt denn der Mensch dasjenige, was im Strom des Erlebens der Toten statt­findet, nicht auf? Weil er sich nicht angewöhnt, das langsamere Tempo einzuschlagen im Halten von Gedanken, im Halten von Gefühlen namentlich, in dem die Toten verharren.",
      "Ist also ein Mensch achtundzwanzig Jahre alt seinem physischen Leibe nach, so ist sein Ich erst sieben Jahre alt. Sie können also nur den Anspruch darauf machen, daß Sie in bezug auf Ihr Ich, was das Eigent­liche Ihrer Wesenheit ist, ein viel langsameres Tempo einhalten in der Entwickelung als in bezug auf den physischen Leib. Die Schwierigkeit besteht darinnen, daß man sonst Geschwindigkeiten nur als äußere Geschwindigkeiten auffaßt. Wenn die Dinge nebeneinander hinlaufen, so sagt man: Eines geht schneller und das andere geht langsamer - weil man die Zeit zum Vergleich hat. Aber hier ist die Geschwindigkeit in der Zeit verschieden. Ohne diese Einsicht aber, daß die verschiedenen",
      "Glieder der menschlichen Natur verschiedenes Tempo haben zu ihrer Entwickelung, ist es unmöglich, dasjenige einzusehen, was mit der eigentlichen tieferen Wesenheit des Menschen zusammenhängt.",
      "Sie sehen aber daraus, wie man im gewöhnlichen Bewußtsein eigent­lich ganz verschiedene Dinge, die in der menschlichen Natur sind, ein­fach zusammenwirft. Der Mensch hat diese viergliederige Wesenheit, und die vier Glieder dieser Wesenheit sind so voneinander verschieden, daß sie sogar verschiedenes Alter haben. Der Mensch aber gibt sich dadurch einer beträchtlichen Illusion hin, daß er alles auf seinen phy­sischen Leib bezieht. Er sagt etwas, was schlechterdings vor der geisti­gen Welt gar keinen Sinn hat, wenn er behauptet, sein Ich sei achtund­zwanzig Jahre alt, wenn er seinem physischen Leibe nach achtundzwan­zig Jahre alt ist. Es hätte nur einen Sinn, wenn er dann sagen würde:",
      "Mein Ich ist sieben Jahre alt - wobei aber dann ein Jahr selbstverständ­lich viermal so lang ist.",
      "Man könnte die Sache auch so ausdrücken: die vier verschiedenen Glieder der menschlichen Wesenheit rechnen nach ganz verschiedenen Zeitmaßen. Das Ich rechnet einfach ein Jahr viermal so lang als der physische Leib. Und bildhaft könnten Sie sich das so vorstellen, wenn Sie es sich projizieren wollten auf den physischen Plan heraus. Während zum Beispiel ein Mensch normal wächst, achtundzwanzig Jahre alt wird, wachse ein Kind langsamer und sei nach achtundzwanzig Jahren ein siebenjähriges Kind. So zunächst erscheint die ganze Sache wie eine abstrakte Wahrheit, aber es ist im Menschen eine gründliche Wirklich­keit. Denn denken Sie doch, daß wir in unserem Ich dasjenige tragen, was wir unseren Verstand, unser selbstbewußtes Denken nennen. Wenn wir in unserem Ich unseren Verstand, unser selbstbewußtes Denken haben, dann sind unser Verstand und unser selbstbewußtes Denken eigentlich wesentlich jünger, als wir scheinbar unserem physischen Leibe nach sind. Das sind sie auch, das sind sie wirklich!",
      "Ja, da kommen Sie aber darauf, einzusehen: wenn ein solcher Mensch achtundzwanzig Jahre alt ist und den Eindruck eines achtundzwanzig­jährig entwickelten Verstandes macht, so ist das, was sein Eigen ist von diesem Verstand, den er hat, nur ein Viertel. Es hilft nichts: wenn wir mit achtundzwanzig Jahren eine gewisse Summe von Verstand haben -",
      "uns eigen ist nur ein Viertel davon, das andere gehört der allgemeinen Welt an; das andere gehört der Welt an, in die wir eingetaucht sind durch unseren astralischen Leib, durch unseren Ätherleib, durch unseren physischen Leib. Aber von denen wissen wir ja unmittelbar nur durch Vorstellungen, durch Sinneswahrnehmungen etwas, also auch wieder­um im Ich. Das heißt, wenn wir als Menschen uns entwickeln zwischen der Geburt und dem Tode, so sind wir eigentlich rechte Scheinwesen der Wirklichkeit. Wir machen den Eindruck von viermal so gescheiten Wesen, als wir in Wirklichkeit sind. Das ist wahr! Alles, was wir außer jenem Viertel haben, das verdanken wir dem, was da waltet im histo­rischen, im sozialen, im moralischen Wirken jener Welt, die wir ver­träumen, die wir verschlafen. Träume, Schlafimpulse, die wir mit der Allgemeinheit gemein haben, brodeln herauf über den Horizont un­seres Daseins und befruchten unser Verstandes- und Seelenviertel und machen es viermal so stark, als es in Wirklichkeit ist.",
      "Hier ist der Punkt, wo die Täuschung entsteht in bezug auf die Frei­heit des Menschen. Der Mensch ist ein freies Wesen; das ist er schon. Aber nur der wahre Mensch ist ein freies Wesen - jenes Viertel, von dem ich eben gesprochen habe, das ist ein freies Wesen. Die andern drei Viertel, in die spielen andere Wesenheiten herein; die können nicht frei sein. Und dadurch entsteht die Täuschung in bezug auf die Freiheit, daß man immer frägt: Ist der Mensch frei oder ist er nicht frei? Frei ist der Mensch, wenn er diesen Begriff der Freiheit bezieht auf das eine Viertel seines Wesens in dem Sinne, wie ich das jetzt auseinandergesetzt habe. Will der Mensch diese Freiheit als einen eigenen Impuls haben, dann muß er allerdings dieses Viertel in entsprechend selbständiger Weise entwickeln. Im gewöhnlichen Leben kann dieses Viertel nicht zu seinem Rechte kommen, aus dem einfachen Grunde, weil es von den übrigen drei Vierteln überwältigt wird. In den übrigen drei Vierteln wirkt alles dasjenige, was der Mensch in sich trägt als seine Triebe, seine Begierden, seine Affekte, seine Leidenschaften. Die ertöten seine Freiheit, denn durch die Triebe, durch die Affekte, durch die Leiden­schaften wirkt dasjenige hindurch, was an Impulsen in der Allgemein­heit ist.",
      "Nun entsteht die Frage: Was wollen wir tun, um das eineViertel von",
      "Seelenleben, das in uns Realität ist, wirklich zur Freiheit zu bringen? Wir müssen es in Beziehung setzen, dieses Viertel, zu dem, was unab­hängig ist von dem übrigen Dreiviertel.",
      "Philosophisch habe ich eben versucht, diese Frage zu beantwor­ten in meiner «Philosophie der Freiheit», indem ich damals zu zeigen bestrebt war, wie der Mensch nur dadurch in sich den Impuls der Frei­heit realisieren kann, wenn er sein Handeln, sein Tun ganz unter den Einfluß des reinen Denkens stellt, wenn er dazu kommt, reine Gedan­kenimpulse zu seinen Handlungsimpulsen machen zu können, Impulse, die gar nicht herausentwickelt sind aus der äußeren Welt. Denn alles das, was aus der äußeren Welt entwickelt ist, läßt uns nicht Freiheit realisieren. Freiheit realisieren läßt uns nur dasjenige, was sich unab­hängig von der äußeren Welt in unserem Denken als Antrieb unseres Handelns entwickelt.",
      "Woher kommen solche Antriebe? Woher kommt das, was nicht aus der äußeren Welt kommt? Nun, es kommt aus der geistigen Welt. Der Mensch braucht sich nicht in jeder Lage seines Lebens hellseherisch bewußt zu sein, wie diese Impulse aus der geistigen Welt kommen, aber sie können in ihm doch da sein. Nur wird er sie notwendigerweise etwas anders auffassen müssen. Wenn wir uns im schauenden Bewußtsein zur ersten Stufe der geistigen Welt erheben, so ist das die imaginative Welt; die zweite Stufe ist die inspirierte Welt, wie Sie wissen; die dritte Stufe die intuitive Welt. Statt daß wir also die Impulse unseres Wollens, unseres Handelns aufsteigen lassen aus unserem physischen, aus un­serem astralischen, aus unserem ätherischen Leib, können wir, wenn wir von dieser Seite her keine Impulse empfangen, sondern sie aus der geistigen Welt empfangen, sie nur entgegennehmen als Imaginationen, hinter denen Inspirationen, hinter denen Intuitionen stehen. Aber das braucht nicht bewußt als hellseherisches Bewußtsein erlebt zu werden:",
      "Jetzt will ich dieses, dahinter stehen Intuitionen, Inspirationen, Imagi­nationen-, sondern das Resultat davon tritt auf als ein Begriff, als ein reines Denken, sieht so aus, wie ein in der Phantasie geschaffener Be­griff. Weil das so ist, weil ein solcher Begriff, der dem freien Handeln zugrunde liegt, für das gewöhnliche Bewußtsein wie ein aus der Phan­tasie heraus geschaffener Begriff erscheinen muß, nannte ich das, was",
      "dem freien Handeln zugrunde liegt, in meiner «Philosophie der Frei­heit» die moralische Phantasie. Was ist also diese moralische Phantasie? Diese moralische Phantasie ist, ich möchte sagen, das Gegenteil eines Spiegelbildes. Dasjenige, was wir um uns herum als die äußere phy­sische Wirklichkeit ausgebreitet haben, das ist ein Spiegelbild, da wer­den uns die Dinge zurückgespiegelt. Die moralische Phantasie ist das Tableau, durch das wir nicht durchsehen. Daher erscheinen uns die Dinge als Phantasie. Hinter ihnen stehen aber die eigentlichen Impulse: Imaginationen, Inspirationen, Intuitionen, die wirken (Siehe Zeich­nung S. 101). Wenn man nicht weiß, daß diese wirken, sondern nur das, was sie bewirken, ins Bewußtsein, ins gewöhnliche Bewußtsein herein-bekommt, so sieht es wie eine Phantasie aus. Und diese Ergebnisse der moralischen Phantasie, diese nicht aus Trieben, Leidenschaften, Affek­ten geholten Antriebe des Handelns, sie sind freie Antriebe.",
      "Wie soll man aber zu ihnen kommen? Würde man sich ohne weiteres zum hellseherischen Bewußtsein erheben, dann würde man durch das Hellsehen bewußt dazu kommen. Aber das braucht man gar nicht. Moralische Phantasie kann auch der Mensch entwickeln, der nicht hellseherisch ist. Alles dasjenige, was den wirklichen Fortschritt der Menschheit bedeutet hat, ist immer aus moralischer Phantasie hervor­gegangen, insoferne dieser Fortschritt auf ethischem Gebiete lag. Es handelt sich nur darum, daß der Mensch zuerst ein Gefühl entwickelt, und dann ein gesteigertes Gefühl - wir werden gleich deutlicher hören, was unter diesem gesteigerten Gefühl zu verstehen ist -, daß er hier auf dieser Erde da ist, um Dinge zu tun, welche nicht bloß seine Persönlich­keit, seine Individualität angehen, sondern um Dinge zu tun, durch die dasjenige verwirklicht wird, was die Zeitgeister wollen.",
      "Es scheint zunächst, als ob etwas ganz Besonderes dahinter stecke, wenn man sagt, der Mensch soll dasjenige realisieren, was die Zeitgeister wollen. Es wird eine Zeit kommen, wo man dies aber viel besser ver­stehen wird als in der Gegenwart. Und es wird eine Zeit kommen, wo man anderes zu Inhalten des menschlichen Lehrens machen wird, als es die Gegenwart macht, wo selbst den Allergebildetsten nur Begriffe beigebracht werden, die auf die Natur gehen. Denn was beigebracht wird den Leuten mit Bezug auf das ethische, mit Bezug auf das soziale",
      "Leben, das sind zumeist wesenlose, schemenhafte Abstraktionen, das sind äußerste Abstraktionen.",
      "In dieser Beziehung haben wir dasjenige noch nicht erreicht, was frühere Zeiten hatten. Nur kann sich der Mensch jetzt sehr schwer in frühere Zeiten hineindenken. Frühere Zeiten hatten Mythen - Mythen, die mit dem lebendigen Leben des Volkes zusammenhingen, Mythen, die in Dichtung, in Kunst, in alles mögliche hineinwirkten. Und womit beschäftigten sich diese Mythen? Man redete im Griechischen von Udipus, von Herkules, von andern Heroen, denen man nachstrebte, die etwas getan hatten, was die Einleitung von Taten war, in deren Fuß­stapfen man treten wollte. Jeder einzelne wollte in ihre Fußstapfen treten. Nach rückwärts leitete der Faden des Vorstellens, der Faden des Denkens, der Faden des Empfindens. Man fühlte sich eins mit längst Verstorbenen. Dasjenige, was von den Verstorbenen als ein Impuls aus­gegangen ist, das wurde erzählt im Mythus, und im Durchleben des Mythus, im Sich-Einswissen mit den Impulsen des Mythus lebten diese Menschen.",
      "Etwas Ähnliches muß wieder geschaffen werden, wird geschaffen werden, wenn die Impulse der Geisteswissenschaft richtig verstanden werden. Nur werden allerdings die Seelenblicke der Zukunft weniger nach rückwärts als nach vorwärts gerichtet sein. Aber was Inhalt des öffentlichen Unterrichts werden muß, das ist das, was den Menschen zusammenbindet mit dem Werden der Zeit, und damit mit den Im­pulsen vor allem des Zeitgeistes, des entsprechenden Wesens aus der Hierarchie der Archai, von dem ich in einer früheren Betrachtung ge­sagt habe, daß ihm ebenso die sogenannten Toten gegenüberstehen wie die Lebendigen. Lernen wird man im öffentlichen Unterricht in der Zukunft, was der Inhalt eines solchen Zeitalters ist wie desjenigen, das mit dem 15.Jahrhundert begonnen und zugleich das griechisch-latei­nische Zeitalter abgeschlossen hat; lernen wird man, was das allgemeine Weltenall in diesem fünften nachatlantischen Zeitraum eigentlich will. Die Impulse dieses fünften nachatlantischen Zeitraums wird man auf­nehmen. Man wird wissen: das muß sich realisieren zwischen dem 15.Jahrhundert und einem Jahrhundert in einem folgenden Jahrtau­send. Und man wird wissen: man gehört seinem Zeitalter so an, daß",
      "durch einen hindurchströmen die Impulse dieses bestehenden Zeitalters. Die Kinder schon werden es in der Zukunft lernen, wie sie Blumen be­nennen, wie sie Sterne benennen lernen - das tun sie ja heute wieder weniger, aber das ist wenigstens etwas Äußerlich-Reales -, so werden sie lernen, die wirklichen geistigen Impulse des Zeitalters aufzunehmen.",
      "Dazu müssen sie allerdings erst erzogen werden, dazu muß erst auf­hören, dasjenige Geschichte zu heißen, was jetzt als Geschichte erzählt wird. Statt all der Dinge, von denen heute die Geschichte erzählt, wird man in einer nicht zu fernen Zukunft von den geistigen Impulsen, die hinter dem geschichtlichen Werden stehen und die von den Menschen geträumt werden, sprechen.",
      "Denn diese geistigen Impulse sind das­jenige, was den Menschen aufruft zur Freiheit und ihn frei macht, weil es ihn erhebt zu der Welt, aus der die Intuitionen, Inspirationen, Ima­ginationen kommen. Denn dasjenige, was äußerlich auf dem physischen Plane geschieht, was äußerlich Geschichte ist - ich habe das selbst in öffentlichen Vorträgen auseinandergesetzt -, das hat schon seine Be­deutung verloren, wenn es vorüber ist; das hat in Wirklichkeit nicht die Bedeutung, daß man sagen kann: Das Vorhergehende ist immer die Ursache des Nachfolgenden. - Es gibt nichts Unsinnigeres, als Ge­schichte etwa so zu erzählen, daß man die Taten Napoleons im Beginn des 19.Jahrhunderts erzählt und dann glaubt, dasjenige, was später geschehen ist, nachdem Napoleon verbannt worden ist, sei die Folge desjenigen, was Napoleon zu seiner Zeit getan hat.",
      "Nichts Unsinnigeres gibt es als das! Denn das, was man von Napoleon erzählen kann, be­deutet für die Wirklichkeit genau dasselbe, was es für das Leben eines Menschen bedeutet, wenn ich drei Tage nach seinem Tode seinen Leich­nam beschreibe.",
      "Dasjenige, was jetzt Geschichte genannt wird, ist gegenüber der Wirklichkeit des geschichtlichen Werdens Kadaver-geschehen, wenn auch die Erzählung dieses Kadavergeschehens im Be­wußtsein mancher Menschen außerordentlich viel bedeutet.",
      "Was äußerlich geschehen ist, wird erst eine Wirklichkeit, wenn es aufgezeigt wird in seinem Hervorsprießen aus den geistigen Impulsen. Dann wird man vielfach sehen, daß das, was ein Mensch tut, sagen wir in irgendeinem bestimmten Jahrzehnt eines Jahrhunderts, die Folge von etwas ist, was er erfahren hat, bevor er zu seiner eigenen Erdeninkarnation",
      "gegangen ist, gar nicht die Folge von dem, was vor Jahr­zehnten im Verlauf des physischen Erlebens auf der Erde sich zugetra­gen hat und so weiter. Gerade mit Bezug auf das geschichtliche, mit Bezug auf das soziale und sittliche Leben wird die anthroposophisch orientierte Geisteswissenschaft vertiefend, befruchtend wirken mü ssen, namentlich auf dem Gebiete der Geschichte. Dieses Wissen der geistigen Impulse, das, zu den Forderungen unserer Zeit erhoben, etwas ähnliches sein wird, wie für die alten Zeiten das Drinnenstehen im lebendigen Mythus es war, das wird die Menschen erfüllen mit solchen Impulsen für ihr Tun und Handeln, die sie frei machen. Diese Dinge müssen zuerst verstanden werden, dann werden sie, wenn sich das Verständnis immer mehr und mehr ausbreitet, schon eingreifen in das wirkliche Leben.",
      "Aber noch ein anderes geht Ihnen ja gerade aus diesen Betrachtungen hervor. Es geht Ihnen daraus hervor, daß die Gefühlsimpulse, die Wil­lensimpulse, mit denen wir in derselben Lebenssphäre drinnenstehen, in der auch die sogenannten Toten drinnenstehen, dann eine höhere, eine intensivereWirklichkeit sind als dasjenige, was wir mit dem wachen Bewußtsein als Vorstellungen und als Sinnesempfindungen kennen. Daher kann das, was jetzt eben so gefordert worden ist, daß es auch ein Gegenstand der öffentlichen Belehrung werden muß, nur recht fruchtbar werden, wenn es nicht nur mit dem Verstande aufgefaßt wird, sondern wenn es übergeht in die Impulse des Fühlens, in die Im­pulse des Wollens.",
      "Das kann nur geschehen, wenn in Geisteswissenschaft eine reale Wirklichkeit gesehen wird, und nicht eine bloße Lehre. Es wird leicht in Geisteswissenschaft eine bloße Lehre gesehen, eine Theorie. Aber Geisteswissenschaft ist nicht eine bloße Lehre, ist nicht eine bloße Theo­rie, Geisteswissenschaft ist ein lebendiges Wort. Denn was als Geistes­wissenschaft verkündet wird, ist die Offenbarung aus den Welten, die wir gemeinschaftlich haben mit den höheren Hierarchien und mit der Welt der sogenannten Toten. Diese Welt selbst spricht zu uns durch Geisteswissenschaft. Und der, welcher wirklich Geisteswissenschaft versteht, der weiß, daß in der Geisteswissenschaft forttönt das, was Seelenmusik der geistigen Welt ist. Dasjenige, was herausgelesen wird -",
      "aber jetzt nicht aus toten Buchstaben, sondern aus wirklichem Ge­schehen der geistigen Welt -, es kann schon unser Gefühl durchdringen mit lebendigem Leben, wenn wir Geisteswissenschaft in diesem Sinne als etwas auffassen, was aus der geistigen Welt zu uns hereinspricht.",
      "Ich habe betont, wie das der Fall ist, als ich besprach, wie seit dem Jahre 1879 auf der einen Seite die Gelegenheit gegeben ist, daß in der Art, wie es früher nicht vorhanden war, Geistesleben herunterfließe auf den physischen Plan, auf der andern Seite allerdings es seine Geg­ner findet in den Geistern der Finsternis, von denen wir gesprochen haben. Und gerade mit Bezug auf dieses Einleben des geisteswissen­schaftlichen Inhaltes in Gefühl und Wille muß gewissermaßen noch alles, alles geschehen. Und dieses kann nur geschehen, wenn gewisse Dinge, mit Bezug auf welche die Menschen gegenwärtig geradezu in einer Kultursackgasse angelangt sind, sich gründlich ändern.",
      "Und durchdringen muß man sich damit: Auf der einen Seite schrei­tet die Entwickelung so fort, daß allerdings die Ereignisse der Ge­schichte sich vergleichen lassen mit einem Baum, der wächst; aber wenn sich die Blätter bis zu seiner äußeren Peripherie entwickelt haben, wächst er nicht weiter, da beginnt das Absterben. So ist es mit den ge­schichtlichen Ereignissen. Bleiben wir bei dem Bilde, das ich in diesen Betrachtungen schon früher gebraucht habe: Es gibt eine ganz be­stimmte Summe von geschichtlichen Ereignissen, die haben ihre Wur­zeln im letzten Drittel des 18.Jahrhunderts - davon werde ich dann morgen deutlicher sprechen -, dazu kommen andere Einflüsse im Lauf des 19.Jahrhunderts und so weiter. Und sehen Sie, diese historischen Ereignisse, die breiten sich aus und erreichen äußerste Grenzen (Siehe Zeichnung). Aber jene Grenzen sind nicht so wie bei einem Baum oder bei einer Pflanze, wo es an der Peripherie einfach nicht weiterwächst, sondern es muß eine neue Wurzel geschichtlicher Ereignisse beginnen. Wir leben im eminentesten Sinne seit Jahrzehnten schon in einer Zeit, in der solche neuen geschichtlichen Ereignisse aus unmittelbaren Intui­tionen heraus beginnen müssen (rechte Hälfte der Zeichnung). Nur ist es im geschichtlichen Leben der Menschen so, daß auch über diese Dinge leicht Illusionen sich ausbreiten. Sie können ja eine Pflanze, die durch ihr inneres Gesetz bis zu einer gewissen Peripherie wächst, naturgemäß",
      "# Bild s. 102",
      "wachsend ansehen nur bis zu dieser Peripherie. Jetzt aber könnten Sie eine Illusion hervorrufen: Sie könnten Drähte anbringen, Papierblätter an die Drähte anhängen und könnten sich der Illusion hingeben, daß dann die Pflanze bis dahin gehe.",
      "# Bild s. 103",
      "Solche Drähte gibt es allerdings bei geschichtlichen Ereignissen! Während längst ein anderer Duktus des geschichtlichen Ereignisses da sein sollte, gibt es solche Drähte. Nur sind im geschichtlichen Werden diese Drähte die menschlichen Vorurteile, die menschlichen Bequem­lichkeiten, die das, was längst abgestorben ist, eben in toten Drähten fortsetzen. Dann setzen sich gewisse Leute an das Ende dieser toten Drähte, und die Menschen, die sich dann an das Ende dieser toten Drähte setzen, das heißt, an die äußersten Ranken der menschlichen Vorurteile, die werden oftmals auch als historische Persönlichkeiten aufgefaßt, ja oftmals als die richtigen historischen Persönlichkeiten. Und man ahnt gar nicht, inwiefern diese Persönlichkeiten an solchen Drähten menschlicher Vorurteile sitzen! Ein wenig sich ein Urteil zu bilden, wieviel Persönlichkeiten, die in der Gegenwart als «große» an­gesehen werden, an solchen Drähten menschlicher Vorurteile pendeln, das gehört schon zu den wichtigen Aufgaben der Gegenwart."
    ],
    "sentences": [
      [
        "Wenn wir dasjenige durchdringen wollen, was den beiden in das Men­schenleben eingreifenden Impulsen, der sogenannten Freiheit und der sogenannten Notwendigkeit, zugrunde liegt, dann müssen wir zu den mancherlei Voraussetzungen, die wir schon geschaffen haben, einige andere noch hinzufügen.",
        "Und das will ich heute tun, damit wir dann morgen in der Lage sind, gewissermaßen die Konklusion, den Schluß in bezug auf den Freiheits- und Notwendigkeitsbegriff im mensch­lichen, sozialen, sittlichen und geschichtlichen Wirken zu ziehen."
      ],
      [
        "Wenn man solche Dinge bespricht, dann kommt eigentlich immer mehr in Betracht, daß die Menschen, und namentlich die Menschen der Gegen­wart danach streben, die höchsten, die wichtigsten, die bedeutsamsten Dinge mit den allereinfachsten Begriffen und Vorstellungen zu um­fassen.",
        "Um eine Uhr zu begreifen - ich habe das öfters schon erwähnt -, dazu hält man mancherlei Kenntnisse für notwendig, und man wird nicht ohne einen Schimmer davon zu haben, wie Räder zusammen­wirken oder dergleichen, aus dem Stegreif heraus den Gang einer Uhr im einzelnen erklären wollen."
      ],
      [
        "Ein Sachverständiger über Freiheit und Notwendigkeit will man eigentlich in jeder Lage des Lebens sein, ohne über diese Dinge etwas zugrunde Liegendes gelernt zu haben.",
        "Über die allerwichtigsten, allerwesentlichsten Dinge, die nur eingesehen werden können im ganzen Zusammenhange mit der Menschennatur, möchte man sich am liebsten nicht unterrichten und alles mögliche wie von selbst wissen und beurteilen."
      ],
      [
        "Das ist insbesondere so die Sehnsucht un­serer Zeit.",
        "Wenn geltend gemacht wird, daß der Mensch eine kompli­zierte, eine mannigfaltigst zusammengesetzte Wesenheit ist, eine Wesen­heit, die auf der einen Seite tief eintaucht in alles das, was mit dem physischen Plane zusammenhängt, auf der andern Seite wiederum see­lisch tief eintaucht in all das, was mit den geistigen Welten zusammen­hängt, dann wird gar leicht erwidert, daß solche Dinge trocken, ver­standesmäßig seien, daß man die allerwichtigsten und wesentlichsten Dinge in einer ganz andern Weise auffassen müsse."
      ],
      [
        "Die Welt wird kennenlernen müssen - sie lernt es vielleicht doch gerade durch die gegenwärtigen katastrophalen Ereignisse schon ein wenig -, was alles im Menschen und in seinem Zusammenhange mit dem Gang der Weltenentwickelung Verborgenes liegt.",
        "Wir haben seit Jahren betont, daß wir dasjenige im Rohen unterscheiden können im Menschen, was man seine physische Natur nennt, seinen physischen Leib, seinen Ätherleib, den Bildekräfteleib, wie ich ihn nenne, seinen astralischen Leib, der schon Seelisches ist, und das eigentliche Ich."
      ],
      [
        "Wir haben nun in den letzten Zeiten von den verschiedensten Ge­sichtspunkten her betont, daß der Mensch, so wie er lebt vom Auf­wachen bis zum Einschlafen, also im gewöhnlichen wachen Tages-bewußtsein, eigentlich in Wirklichkeit nur etwas weiß von den Ein­drücken seiner Sinneswahrnehmungen und noch von seinen Vorstellun­gen, daß er aber den eigentlichen Inhalt seines Gefühlslebens verträumt, und den eigentlichen Inhalt seines Willenslebens verschläft.",
        "Traum und Schlaf dehnen sich herein in die gewöhnliche Welt des Wachens, und mehr bewußt als eines Traumes sind wir uns auch unseres Gefühlslebens nicht im gewöhnlichen Wachbewußtsein.",
        "Mehr bewußt als im traum-losen Schlafe ist sich der Mensch seines wirklichen Willensinhaltes nicht.",
        "Denn durch unsere Gefühle, durch unseren Willensinhalt tauchen wir in dieselbe Welt hinein - das haben wir in diesen Betrachtungen betont - in welcher wir gemeinschaftlich mit den Toten unter den Wesenheiten der höheren Hierarchien, der Angeloi, Archangeloi, Archai und so weiter leben.",
        "Sobald wir in einem Gefühle leben - und wir leben ja fortwährend in Gefühlen -, lebt in der Sphäre, in dem Gebiete dieses Fühlens alles dasjenige mit, was im Reiche der Toten ist."
      ],
      [
        "Nun kommt ein anderes dazu.",
        "Wir sprechen im gewöhnlichen wa­chen Bewußtseinsleben von unserem Ich.",
        "Aber von diesem Ich können wir eigentlich mit dem gewöhnlichen Wachbewußtsein nur in recht uneigentlichem Sinne sprechen.",
        "Denn welche Natur und Wesenheit hat eigentlich dieses Ich?",
        "Es kann nicht erkannt werden im gewöhnlichen Wachbewußtsein.",
        "Taucht das schauende Bewußtsein in das wahre We­sen des Ich ein, dann ist das wahre Ich des Menschen willensartiger Natur.",
        "Das, was der Mensch im gewöhnlichen Bewußtsein hat, ist nur die Vorstellung des Ich.",
        "Daher wird es dem naturforscherischen Psy­chologen"
      ],
      [
        "leicht, dieses Ich überhaupt wegzuleugnen, obwohl anderer­seits dieses Wegleugnen ein wirklicher Unsinn ist.",
        "Solche Naturforscher und Psychologen sprechen davon, daß das Ich sich eigentlich nach und nach heranbilde, daß der Mensch im Verlauf seiner individuellen Ent­wickelung zu diesem Ich komme.",
        "Er kommt nicht zu dem Ich, sondern zu der Ich-Vorstellung auf diese Art.",
        "Und es ist leicht hinwegzuleug­nen, weil es eben im gewöhnlichen Bewußtsein nur eine Vorstellung, ein Spiegelbild des wirklichen, wahren, echten Ich ist.",
        "Das echte Ich lebt in derselben Weltensphäre, in der die wahre Wirklichkeit unseres Willens lebt.",
        "Und das, was wir den astralischen Leib nennen, was wir als das eigentliche Seelenleben bezeichnen können, das wiederum lebt in derselben Sphäre, in der da lebt unser Gefühlsleben.",
        "Wenn Sie die beiden Dinge zusammennehmen, die wir so betrachtet haben, können Sie daraus wiederum ersehen, daß wir mit unserem Ich und mit un­serem astralischen Leib untertauchen in dasselbe Gebiet, das wir mit den Toten gemeinschaftlich haben.",
        "In dem Augenblicke, wo wir hell­seherisch in unser wahres Ich hinuntersteigen, sind wir ebenso unter den Ichen der Toten wie unter den Ichen der sogenannten Lebendigen."
      ],
      [
        "So etwas muß man sich nur ganz klarmachen, um voll einzusehen, wie sehr der Mensch mit seinem gewöhnlichen Bewußtsein in der soge­nannten Scheinwelt, oder wie man es mit einem orientalischen Aus­drucke nennt, in der Maja lebt.",
        "Wir leben wachbewußt in unserer Sinnes- und in unserer Vorstellungswelt.",
        "Aber die Sinnesimpulse, die geben uns nur den Teil der Welt, der als Natur sich ausbreitet.",
        "Und unsere Vorstellungswelt gibt uns auch nichts anderes als dasjenige in uns, was unserer Natur angemessen ist, aber zwischen der Geburt und dem Tode.",
        "Dasjenige, was unsere ewige Natur ist, das tritt im Grunde gar nicht aus der Welt heraus, die wir mit den Toten gemeinschaftlich haben.",
        "Das verbleibt im Grunde genommen in der Welt, in der die Toten auch sind, wenn wir durch die Verkörperung in das Leben des physischen Planes eintreten."
      ],
      [
        "Um aber diese Dinge voll zu verstehen, haben wir nötig, gewisse Begriffe aufzunehmen, die - man kann schon nichts dafür, das sagen zu müssen, weil die Dinge eben so sind - nicht ganz leicht zu durch­denken sind, bei denen man sich, um sie zu durchdenken, Mühe geben"
      ],
      [
        "muß.",
        "Solche Begriffe hat zunächst der Mensch im Verlaufe seines ge­wöhnlichen wachen Bewußtseins nicht.",
        "Der Mensch kennt im gewöhn­lichen wachen Bewußtsein das, was räumlich ausgedehnt ist, was in der Zeit verläuft.",
        "Und er möchte eigentlich mit dem zufrieden sein, was räumlich ausgedehnt ist und was in der Zeit verläuft.",
        "Krankt ja sogar der Mensch vielfach daran, sich auch dasjenige, was in der geistigen Welt enthalten ist, möglichst räumlich zu denken, wenn auch nebulos, wenn auch dünn und nebelhaft, aber er möchte es doch irgendwie sich räumlich denken: räumlich herumfliegende Seelen und dergleichen möchte er sich denken.",
        "Man muß über die Begriffe von Raum und Zeit hinausgehen zu komplizierteren Begriffen, wenn man in diese Dinge wirklich eindringen will.",
        "Und da möchte ich Ihnen denn heute etwas andeuten, was wichtig ist zur Erfassung des menschlichen Gesamtlebens."
      ],
      [
        "Fassen wir noch einmal ins Auge - wie gesagt, im Rohen -, daß wir diese vierfache Natur zunächst haben: den physischen Leib, den Bilde-kräfte- oder Ätherleib, den astralischen Leib und das Ich.",
        "Wenn man so vom Standpunkte des gewöhnlichen wachen Bewußtseins aus redet und frägt: Wie alt ist eigentlich ein Mensch, dieser bestimmte Mensch A, wie alt ist er? - Nun, da wird irgend jemand sein Alter angeben, sagen wir fünfunddreißig Jahre, und er glaubt, damit etwas Ernst­haftes gesagt zu haben.",
        "Er hat auch für den physischen Plan und das gewöhnliche Wachbewußtsein etwas Ernsthaftes damit gesagt, daß er fünfunddreißig Jahre alt sei.",
        "Aber für die geistige Welt, also für die Gesamtwesenheit des Menschen, ist damit nur teilweise etwas gesagt.",
        "Denn Sie können eigentlich, wenn Sie sagen, ich bin fünfunddreißig Jahre alt, dies nur für Ihren physischen Leib sagen.",
        "Sie müßten sagen: Mein physischer Leib ist fünfunddreißig Jahre alt - dann würde die Sache stimmen.",
        "Für den ätherischen oder Bildekräfteleib, für die andern Glieder der menschlichen Wesenheit haben Sie aber damit noch gar nichts gesagt.",
        "Denn daß Ihr Ich zum Beispiel auch fünfunddreißig Jahre alt sein soll, wenn Ihr physischer Leib fünfunddreißig Jahre alt ist, das ist eine bloße Illusion, das ist sogar eine reine Phantasterei.",
        "Denn sehen Sie, hier tritt auf der Begriff verschieden geschwinder, ver­schieden schneller Entwickelung der verschiedenen Glieder der mensch­lichen Natur."
      ],
      [
        "Das können Sie sich durch folgende Zahlen klarmachen.",
        "Der Mensch wird, sagen wir sieben Jahre alt; das heißt aber nichts anderes als: sein physischer Leib ist sieben Jahre alt geworden.",
        "Dann ist deshalb sein Ätherleib, sein Bildekräfteleib noch nicht sieben Jahre alt, sondern sein Bildekräfteleib macht nicht so schnell mit; der ist noch nicht so alt ge­worden."
      ],
      [
        "Man kommt auf diese Dinge nur deshalb nicht, weil man die Zeit sich eben so als einen einheitlich dahinlaufenden Strom vorstellt und man sich gar nicht denken kann, daß innerhalb der Zeit verschie­denes mit verschiedener Geschwindigkeit vorwärtsgeht.",
        "Dieser phy­sische Leib, der sieben Jahre ist, der hat sich mit einer gewissen Ge­schwindigkeit entwickelt."
      ],
      [
        "Langsamer hat sich entwickelt der Ätherleib, noch langsamer der astralische Leib, und am langsamsten das Ich.",
        "Dieser Ätherl eib ist erst fünf Jahre drei Monate alt, wenn der physische Leib sieben Jahre alt ist, weil er ein langsameres Tempo durchmacht."
      ],
      [
        "Der astralische Leib ist drei Jahre sechs Monate alt.",
        "Und das Ich ist ein Jahr neun Monate alt.",
        "So daß Sie sich sagen müssen, wenn ein Kind sieben Jahre alt ist, so ist sein Ich erst ein Jahr neun Monate alt."
      ],
      [
        "Es macht dieses Ich eine langsamere Entwickelung durch auf dem phy­sischen Plane.",
        "Es geht dieses Ich auf dem physischen Plane ein lang­sameres Tempo, jenes langsamere Tempo, welches auch das Tempo ist, das man gemeinschaftlich mit den Toten durchleben kann."
      ],
      [
        "Warum faßt denn der Mensch dasjenige, was im Strom des Erlebens der Toten statt­findet, nicht auf?",
        "Weil er sich nicht angewöhnt, das langsamere Tempo einzuschlagen im Halten von Gedanken, im Halten von Gefühlen namentlich, in dem die Toten verharren."
      ],
      [
        "Ist also ein Mensch achtundzwanzig Jahre alt seinem physischen Leibe nach, so ist sein Ich erst sieben Jahre alt.",
        "Sie können also nur den Anspruch darauf machen, daß Sie in bezug auf Ihr Ich, was das Eigent­liche Ihrer Wesenheit ist, ein viel langsameres Tempo einhalten in der Entwickelung als in bezug auf den physischen Leib.",
        "Die Schwierigkeit besteht darinnen, daß man sonst Geschwindigkeiten nur als äußere Geschwindigkeiten auffaßt.",
        "Wenn die Dinge nebeneinander hinlaufen, so sagt man: Eines geht schneller und das andere geht langsamer - weil man die Zeit zum Vergleich hat.",
        "Aber hier ist die Geschwindigkeit in der Zeit verschieden.",
        "Ohne diese Einsicht aber, daß die verschiedenen"
      ],
      [
        "Glieder der menschlichen Natur verschiedenes Tempo haben zu ihrer Entwickelung, ist es unmöglich, dasjenige einzusehen, was mit der eigentlichen tieferen Wesenheit des Menschen zusammenhängt."
      ],
      [
        "Sie sehen aber daraus, wie man im gewöhnlichen Bewußtsein eigent­lich ganz verschiedene Dinge, die in der menschlichen Natur sind, ein­fach zusammenwirft.",
        "Der Mensch hat diese viergliederige Wesenheit, und die vier Glieder dieser Wesenheit sind so voneinander verschieden, daß sie sogar verschiedenes Alter haben.",
        "Der Mensch aber gibt sich dadurch einer beträchtlichen Illusion hin, daß er alles auf seinen phy­sischen Leib bezieht.",
        "Er sagt etwas, was schlechterdings vor der geisti­gen Welt gar keinen Sinn hat, wenn er behauptet, sein Ich sei achtund­zwanzig Jahre alt, wenn er seinem physischen Leibe nach achtundzwan­zig Jahre alt ist.",
        "Es hätte nur einen Sinn, wenn er dann sagen würde:"
      ],
      [
        "Mein Ich ist sieben Jahre alt - wobei aber dann ein Jahr selbstverständ­lich viermal so lang ist."
      ],
      [
        "Man könnte die Sache auch so ausdrücken: die vier verschiedenen Glieder der menschlichen Wesenheit rechnen nach ganz verschiedenen Zeitmaßen.",
        "Das Ich rechnet einfach ein Jahr viermal so lang als der physische Leib.",
        "Und bildhaft könnten Sie sich das so vorstellen, wenn Sie es sich projizieren wollten auf den physischen Plan heraus.",
        "Während zum Beispiel ein Mensch normal wächst, achtundzwanzig Jahre alt wird, wachse ein Kind langsamer und sei nach achtundzwanzig Jahren ein siebenjähriges Kind.",
        "So zunächst erscheint die ganze Sache wie eine abstrakte Wahrheit, aber es ist im Menschen eine gründliche Wirklich­keit.",
        "Denn denken Sie doch, daß wir in unserem Ich dasjenige tragen, was wir unseren Verstand, unser selbstbewußtes Denken nennen.",
        "Wenn wir in unserem Ich unseren Verstand, unser selbstbewußtes Denken haben, dann sind unser Verstand und unser selbstbewußtes Denken eigentlich wesentlich jünger, als wir scheinbar unserem physischen Leibe nach sind.",
        "Das sind sie auch, das sind sie wirklich!"
      ],
      [
        "Ja, da kommen Sie aber darauf, einzusehen: wenn ein solcher Mensch achtundzwanzig Jahre alt ist und den Eindruck eines achtundzwanzig­jährig entwickelten Verstandes macht, so ist das, was sein Eigen ist von diesem Verstand, den er hat, nur ein Viertel.",
        "Es hilft nichts: wenn wir mit achtundzwanzig Jahren eine gewisse Summe von Verstand haben -"
      ],
      [
        "uns eigen ist nur ein Viertel davon, das andere gehört der allgemeinen Welt an; das andere gehört der Welt an, in die wir eingetaucht sind durch unseren astralischen Leib, durch unseren Ätherleib, durch unseren physischen Leib.",
        "Aber von denen wissen wir ja unmittelbar nur durch Vorstellungen, durch Sinneswahrnehmungen etwas, also auch wieder­um im Ich.",
        "Das heißt, wenn wir als Menschen uns entwickeln zwischen der Geburt und dem Tode, so sind wir eigentlich rechte Scheinwesen der Wirklichkeit.",
        "Wir machen den Eindruck von viermal so gescheiten Wesen, als wir in Wirklichkeit sind.",
        "Das ist wahr!",
        "Alles, was wir außer jenem Viertel haben, das verdanken wir dem, was da waltet im histo­rischen, im sozialen, im moralischen Wirken jener Welt, die wir ver­träumen, die wir verschlafen.",
        "Träume, Schlafimpulse, die wir mit der Allgemeinheit gemein haben, brodeln herauf über den Horizont un­seres Daseins und befruchten unser Verstandes- und Seelenviertel und machen es viermal so stark, als es in Wirklichkeit ist."
      ],
      [
        "Hier ist der Punkt, wo die Täuschung entsteht in bezug auf die Frei­heit des Menschen.",
        "Der Mensch ist ein freies Wesen; das ist er schon.",
        "Aber nur der wahre Mensch ist ein freies Wesen - jenes Viertel, von dem ich eben gesprochen habe, das ist ein freies Wesen.",
        "Die andern drei Viertel, in die spielen andere Wesenheiten herein; die können nicht frei sein.",
        "Und dadurch entsteht die Täuschung in bezug auf die Freiheit, daß man immer frägt: Ist der Mensch frei oder ist er nicht frei?",
        "Frei ist der Mensch, wenn er diesen Begriff der Freiheit bezieht auf das eine Viertel seines Wesens in dem Sinne, wie ich das jetzt auseinandergesetzt habe.",
        "Will der Mensch diese Freiheit als einen eigenen Impuls haben, dann muß er allerdings dieses Viertel in entsprechend selbständiger Weise entwickeln.",
        "Im gewöhnlichen Leben kann dieses Viertel nicht zu seinem Rechte kommen, aus dem einfachen Grunde, weil es von den übrigen drei Vierteln überwältigt wird.",
        "In den übrigen drei Vierteln wirkt alles dasjenige, was der Mensch in sich trägt als seine Triebe, seine Begierden, seine Affekte, seine Leidenschaften.",
        "Die ertöten seine Freiheit, denn durch die Triebe, durch die Affekte, durch die Leiden­schaften wirkt dasjenige hindurch, was an Impulsen in der Allgemein­heit ist."
      ],
      [
        "Nun entsteht die Frage: Was wollen wir tun, um das eineViertel von"
      ],
      [
        "Seelenleben, das in uns Realität ist, wirklich zur Freiheit zu bringen?",
        "Wir müssen es in Beziehung setzen, dieses Viertel, zu dem, was unab­hängig ist von dem übrigen Dreiviertel."
      ],
      [
        "Philosophisch habe ich eben versucht, diese Frage zu beantwor­ten in meiner «Philosophie der Freiheit», indem ich damals zu zeigen bestrebt war, wie der Mensch nur dadurch in sich den Impuls der Frei­heit realisieren kann, wenn er sein Handeln, sein Tun ganz unter den Einfluß des reinen Denkens stellt, wenn er dazu kommt, reine Gedan­kenimpulse zu seinen Handlungsimpulsen machen zu können, Impulse, die gar nicht herausentwickelt sind aus der äußeren Welt.",
        "Denn alles das, was aus der äußeren Welt entwickelt ist, läßt uns nicht Freiheit realisieren.",
        "Freiheit realisieren läßt uns nur dasjenige, was sich unab­hängig von der äußeren Welt in unserem Denken als Antrieb unseres Handelns entwickelt."
      ],
      [
        "Woher kommen solche Antriebe?",
        "Woher kommt das, was nicht aus der äußeren Welt kommt?",
        "Nun, es kommt aus der geistigen Welt.",
        "Der Mensch braucht sich nicht in jeder Lage seines Lebens hellseherisch bewußt zu sein, wie diese Impulse aus der geistigen Welt kommen, aber sie können in ihm doch da sein.",
        "Nur wird er sie notwendigerweise etwas anders auffassen müssen.",
        "Wenn wir uns im schauenden Bewußtsein zur ersten Stufe der geistigen Welt erheben, so ist das die imaginative Welt; die zweite Stufe ist die inspirierte Welt, wie Sie wissen; die dritte Stufe die intuitive Welt.",
        "Statt daß wir also die Impulse unseres Wollens, unseres Handelns aufsteigen lassen aus unserem physischen, aus un­serem astralischen, aus unserem ätherischen Leib, können wir, wenn wir von dieser Seite her keine Impulse empfangen, sondern sie aus der geistigen Welt empfangen, sie nur entgegennehmen als Imaginationen, hinter denen Inspirationen, hinter denen Intuitionen stehen.",
        "Aber das braucht nicht bewußt als hellseherisches Bewußtsein erlebt zu werden:"
      ],
      [
        "Jetzt will ich dieses, dahinter stehen Intuitionen, Inspirationen, Imagi­nationen-, sondern das Resultat davon tritt auf als ein Begriff, als ein reines Denken, sieht so aus, wie ein in der Phantasie geschaffener Be­griff.",
        "Weil das so ist, weil ein solcher Begriff, der dem freien Handeln zugrunde liegt, für das gewöhnliche Bewußtsein wie ein aus der Phan­tasie heraus geschaffener Begriff erscheinen muß, nannte ich das, was"
      ],
      [
        "dem freien Handeln zugrunde liegt, in meiner «Philosophie der Frei­heit» die moralische Phantasie.",
        "Was ist also diese moralische Phantasie?",
        "Diese moralische Phantasie ist, ich möchte sagen, das Gegenteil eines Spiegelbildes.",
        "Dasjenige, was wir um uns herum als die äußere phy­sische Wirklichkeit ausgebreitet haben, das ist ein Spiegelbild, da wer­den uns die Dinge zurückgespiegelt.",
        "Die moralische Phantasie ist das Tableau, durch das wir nicht durchsehen.",
        "Daher erscheinen uns die Dinge als Phantasie.",
        "Hinter ihnen stehen aber die eigentlichen Impulse: Imaginationen, Inspirationen, Intuitionen, die wirken (Siehe Zeich­nung S. 101).",
        "Wenn man nicht weiß, daß diese wirken, sondern nur das, was sie bewirken, ins Bewußtsein, ins gewöhnliche Bewußtsein herein-bekommt, so sieht es wie eine Phantasie aus.",
        "Und diese Ergebnisse der moralischen Phantasie, diese nicht aus Trieben, Leidenschaften, Affek­ten geholten Antriebe des Handelns, sie sind freie Antriebe."
      ],
      [
        "Wie soll man aber zu ihnen kommen?",
        "Würde man sich ohne weiteres zum hellseherischen Bewußtsein erheben, dann würde man durch das Hellsehen bewußt dazu kommen.",
        "Aber das braucht man gar nicht.",
        "Moralische Phantasie kann auch der Mensch entwickeln, der nicht hellseherisch ist.",
        "Alles dasjenige, was den wirklichen Fortschritt der Menschheit bedeutet hat, ist immer aus moralischer Phantasie hervor­gegangen, insoferne dieser Fortschritt auf ethischem Gebiete lag.",
        "Es handelt sich nur darum, daß der Mensch zuerst ein Gefühl entwickelt, und dann ein gesteigertes Gefühl - wir werden gleich deutlicher hören, was unter diesem gesteigerten Gefühl zu verstehen ist -, daß er hier auf dieser Erde da ist, um Dinge zu tun, welche nicht bloß seine Persönlich­keit, seine Individualität angehen, sondern um Dinge zu tun, durch die dasjenige verwirklicht wird, was die Zeitgeister wollen."
      ],
      [
        "Es scheint zunächst, als ob etwas ganz Besonderes dahinter stecke, wenn man sagt, der Mensch soll dasjenige realisieren, was die Zeitgeister wollen.",
        "Es wird eine Zeit kommen, wo man dies aber viel besser ver­stehen wird als in der Gegenwart.",
        "Und es wird eine Zeit kommen, wo man anderes zu Inhalten des menschlichen Lehrens machen wird, als es die Gegenwart macht, wo selbst den Allergebildetsten nur Begriffe beigebracht werden, die auf die Natur gehen.",
        "Denn was beigebracht wird den Leuten mit Bezug auf das ethische, mit Bezug auf das soziale"
      ],
      [
        "Leben, das sind zumeist wesenlose, schemenhafte Abstraktionen, das sind äußerste Abstraktionen."
      ],
      [
        "In dieser Beziehung haben wir dasjenige noch nicht erreicht, was frühere Zeiten hatten.",
        "Nur kann sich der Mensch jetzt sehr schwer in frühere Zeiten hineindenken.",
        "Frühere Zeiten hatten Mythen - Mythen, die mit dem lebendigen Leben des Volkes zusammenhingen, Mythen, die in Dichtung, in Kunst, in alles mögliche hineinwirkten.",
        "Und womit beschäftigten sich diese Mythen?",
        "Man redete im Griechischen von Udipus, von Herkules, von andern Heroen, denen man nachstrebte, die etwas getan hatten, was die Einleitung von Taten war, in deren Fuß­stapfen man treten wollte.",
        "Jeder einzelne wollte in ihre Fußstapfen treten.",
        "Nach rückwärts leitete der Faden des Vorstellens, der Faden des Denkens, der Faden des Empfindens.",
        "Man fühlte sich eins mit längst Verstorbenen.",
        "Dasjenige, was von den Verstorbenen als ein Impuls aus­gegangen ist, das wurde erzählt im Mythus, und im Durchleben des Mythus, im Sich-Einswissen mit den Impulsen des Mythus lebten diese Menschen."
      ],
      [
        "Etwas Ähnliches muß wieder geschaffen werden, wird geschaffen werden, wenn die Impulse der Geisteswissenschaft richtig verstanden werden.",
        "Nur werden allerdings die Seelenblicke der Zukunft weniger nach rückwärts als nach vorwärts gerichtet sein.",
        "Aber was Inhalt des öffentlichen Unterrichts werden muß, das ist das, was den Menschen zusammenbindet mit dem Werden der Zeit, und damit mit den Im­pulsen vor allem des Zeitgeistes, des entsprechenden Wesens aus der Hierarchie der Archai, von dem ich in einer früheren Betrachtung ge­sagt habe, daß ihm ebenso die sogenannten Toten gegenüberstehen wie die Lebendigen.",
        "Lernen wird man im öffentlichen Unterricht in der Zukunft, was der Inhalt eines solchen Zeitalters ist wie desjenigen, das mit dem 15.Jahrhundert begonnen und zugleich das griechisch-latei­nische Zeitalter abgeschlossen hat; lernen wird man, was das allgemeine Weltenall in diesem fünften nachatlantischen Zeitraum eigentlich will.",
        "Die Impulse dieses fünften nachatlantischen Zeitraums wird man auf­nehmen.",
        "Man wird wissen: das muß sich realisieren zwischen dem 15.Jahrhundert und einem Jahrhundert in einem folgenden Jahrtau­send.",
        "Und man wird wissen: man gehört seinem Zeitalter so an, daß"
      ],
      [
        "durch einen hindurchströmen die Impulse dieses bestehenden Zeitalters.",
        "Die Kinder schon werden es in der Zukunft lernen, wie sie Blumen be­nennen, wie sie Sterne benennen lernen - das tun sie ja heute wieder weniger, aber das ist wenigstens etwas Äußerlich-Reales -, so werden sie lernen, die wirklichen geistigen Impulse des Zeitalters aufzunehmen."
      ],
      [
        "Dazu müssen sie allerdings erst erzogen werden, dazu muß erst auf­hören, dasjenige Geschichte zu heißen, was jetzt als Geschichte erzählt wird.",
        "Statt all der Dinge, von denen heute die Geschichte erzählt, wird man in einer nicht zu fernen Zukunft von den geistigen Impulsen, die hinter dem geschichtlichen Werden stehen und die von den Menschen geträumt werden, sprechen."
      ],
      [
        "Denn diese geistigen Impulse sind das­jenige, was den Menschen aufruft zur Freiheit und ihn frei macht, weil es ihn erhebt zu der Welt, aus der die Intuitionen, Inspirationen, Ima­ginationen kommen.",
        "Denn dasjenige, was äußerlich auf dem physischen Plane geschieht, was äußerlich Geschichte ist - ich habe das selbst in öffentlichen Vorträgen auseinandergesetzt -, das hat schon seine Be­deutung verloren, wenn es vorüber ist; das hat in Wirklichkeit nicht die Bedeutung, daß man sagen kann: Das Vorhergehende ist immer die Ursache des Nachfolgenden. - Es gibt nichts Unsinnigeres, als Ge­schichte etwa so zu erzählen, daß man die Taten Napoleons im Beginn des 19.Jahrhunderts erzählt und dann glaubt, dasjenige, was später geschehen ist, nachdem Napoleon verbannt worden ist, sei die Folge desjenigen, was Napoleon zu seiner Zeit getan hat."
      ],
      [
        "Nichts Unsinnigeres gibt es als das!",
        "Denn das, was man von Napoleon erzählen kann, be­deutet für die Wirklichkeit genau dasselbe, was es für das Leben eines Menschen bedeutet, wenn ich drei Tage nach seinem Tode seinen Leich­nam beschreibe."
      ],
      [
        "Dasjenige, was jetzt Geschichte genannt wird, ist gegenüber der Wirklichkeit des geschichtlichen Werdens Kadaver-geschehen, wenn auch die Erzählung dieses Kadavergeschehens im Be­wußtsein mancher Menschen außerordentlich viel bedeutet."
      ],
      [
        "Was äußerlich geschehen ist, wird erst eine Wirklichkeit, wenn es aufgezeigt wird in seinem Hervorsprießen aus den geistigen Impulsen.",
        "Dann wird man vielfach sehen, daß das, was ein Mensch tut, sagen wir in irgendeinem bestimmten Jahrzehnt eines Jahrhunderts, die Folge von etwas ist, was er erfahren hat, bevor er zu seiner eigenen Erdeninkarnation"
      ],
      [
        "gegangen ist, gar nicht die Folge von dem, was vor Jahr­zehnten im Verlauf des physischen Erlebens auf der Erde sich zugetra­gen hat und so weiter.",
        "Gerade mit Bezug auf das geschichtliche, mit Bezug auf das soziale und sittliche Leben wird die anthroposophisch orientierte Geisteswissenschaft vertiefend, befruchtend wirken mü ssen, namentlich auf dem Gebiete der Geschichte.",
        "Dieses Wissen der geistigen Impulse, das, zu den Forderungen unserer Zeit erhoben, etwas ähnliches sein wird, wie für die alten Zeiten das Drinnenstehen im lebendigen Mythus es war, das wird die Menschen erfüllen mit solchen Impulsen für ihr Tun und Handeln, die sie frei machen.",
        "Diese Dinge müssen zuerst verstanden werden, dann werden sie, wenn sich das Verständnis immer mehr und mehr ausbreitet, schon eingreifen in das wirkliche Leben."
      ],
      [
        "Aber noch ein anderes geht Ihnen ja gerade aus diesen Betrachtungen hervor.",
        "Es geht Ihnen daraus hervor, daß die Gefühlsimpulse, die Wil­lensimpulse, mit denen wir in derselben Lebenssphäre drinnenstehen, in der auch die sogenannten Toten drinnenstehen, dann eine höhere, eine intensivereWirklichkeit sind als dasjenige, was wir mit dem wachen Bewußtsein als Vorstellungen und als Sinnesempfindungen kennen.",
        "Daher kann das, was jetzt eben so gefordert worden ist, daß es auch ein Gegenstand der öffentlichen Belehrung werden muß, nur recht fruchtbar werden, wenn es nicht nur mit dem Verstande aufgefaßt wird, sondern wenn es übergeht in die Impulse des Fühlens, in die Im­pulse des Wollens."
      ],
      [
        "Das kann nur geschehen, wenn in Geisteswissenschaft eine reale Wirklichkeit gesehen wird, und nicht eine bloße Lehre.",
        "Es wird leicht in Geisteswissenschaft eine bloße Lehre gesehen, eine Theorie.",
        "Aber Geisteswissenschaft ist nicht eine bloße Lehre, ist nicht eine bloße Theo­rie, Geisteswissenschaft ist ein lebendiges Wort.",
        "Denn was als Geistes­wissenschaft verkündet wird, ist die Offenbarung aus den Welten, die wir gemeinschaftlich haben mit den höheren Hierarchien und mit der Welt der sogenannten Toten.",
        "Diese Welt selbst spricht zu uns durch Geisteswissenschaft.",
        "Und der, welcher wirklich Geisteswissenschaft versteht, der weiß, daß in der Geisteswissenschaft forttönt das, was Seelenmusik der geistigen Welt ist.",
        "Dasjenige, was herausgelesen wird -"
      ],
      [
        "aber jetzt nicht aus toten Buchstaben, sondern aus wirklichem Ge­schehen der geistigen Welt -, es kann schon unser Gefühl durchdringen mit lebendigem Leben, wenn wir Geisteswissenschaft in diesem Sinne als etwas auffassen, was aus der geistigen Welt zu uns hereinspricht."
      ],
      [
        "Ich habe betont, wie das der Fall ist, als ich besprach, wie seit dem Jahre 1879 auf der einen Seite die Gelegenheit gegeben ist, daß in der Art, wie es früher nicht vorhanden war, Geistesleben herunterfließe auf den physischen Plan, auf der andern Seite allerdings es seine Geg­ner findet in den Geistern der Finsternis, von denen wir gesprochen haben.",
        "Und gerade mit Bezug auf dieses Einleben des geisteswissen­schaftlichen Inhaltes in Gefühl und Wille muß gewissermaßen noch alles, alles geschehen.",
        "Und dieses kann nur geschehen, wenn gewisse Dinge, mit Bezug auf welche die Menschen gegenwärtig geradezu in einer Kultursackgasse angelangt sind, sich gründlich ändern."
      ],
      [
        "Und durchdringen muß man sich damit: Auf der einen Seite schrei­tet die Entwickelung so fort, daß allerdings die Ereignisse der Ge­schichte sich vergleichen lassen mit einem Baum, der wächst; aber wenn sich die Blätter bis zu seiner äußeren Peripherie entwickelt haben, wächst er nicht weiter, da beginnt das Absterben.",
        "So ist es mit den ge­schichtlichen Ereignissen.",
        "Bleiben wir bei dem Bilde, das ich in diesen Betrachtungen schon früher gebraucht habe: Es gibt eine ganz be­stimmte Summe von geschichtlichen Ereignissen, die haben ihre Wur­zeln im letzten Drittel des 18.Jahrhunderts - davon werde ich dann morgen deutlicher sprechen -, dazu kommen andere Einflüsse im Lauf des 19.Jahrhunderts und so weiter.",
        "Und sehen Sie, diese historischen Ereignisse, die breiten sich aus und erreichen äußerste Grenzen (Siehe Zeichnung).",
        "Aber jene Grenzen sind nicht so wie bei einem Baum oder bei einer Pflanze, wo es an der Peripherie einfach nicht weiterwächst, sondern es muß eine neue Wurzel geschichtlicher Ereignisse beginnen.",
        "Wir leben im eminentesten Sinne seit Jahrzehnten schon in einer Zeit, in der solche neuen geschichtlichen Ereignisse aus unmittelbaren Intui­tionen heraus beginnen müssen (rechte Hälfte der Zeichnung).",
        "Nur ist es im geschichtlichen Leben der Menschen so, daß auch über diese Dinge leicht Illusionen sich ausbreiten.",
        "Sie können ja eine Pflanze, die durch ihr inneres Gesetz bis zu einer gewissen Peripherie wächst, naturgemäß"
      ],
      [
        "# Bild s. 102"
      ],
      [
        "wachsend ansehen nur bis zu dieser Peripherie.",
        "Jetzt aber könnten Sie eine Illusion hervorrufen: Sie könnten Drähte anbringen, Papierblätter an die Drähte anhängen und könnten sich der Illusion hingeben, daß dann die Pflanze bis dahin gehe."
      ],
      [
        "# Bild s. 103"
      ],
      [
        "Solche Drähte gibt es allerdings bei geschichtlichen Ereignissen!",
        "Während längst ein anderer Duktus des geschichtlichen Ereignisses da sein sollte, gibt es solche Drähte.",
        "Nur sind im geschichtlichen Werden diese Drähte die menschlichen Vorurteile, die menschlichen Bequem­lichkeiten, die das, was längst abgestorben ist, eben in toten Drähten fortsetzen.",
        "Dann setzen sich gewisse Leute an das Ende dieser toten Drähte, und die Menschen, die sich dann an das Ende dieser toten Drähte setzen, das heißt, an die äußersten Ranken der menschlichen Vorurteile, die werden oftmals auch als historische Persönlichkeiten aufgefaßt, ja oftmals als die richtigen historischen Persönlichkeiten.",
        "Und man ahnt gar nicht, inwiefern diese Persönlichkeiten an solchen Drähten menschlicher Vorurteile sitzen!",
        "Ein wenig sich ein Urteil zu bilden, wieviel Persönlichkeiten, die in der Gegenwart als «große» an­gesehen werden, an solchen Drähten menschlicher Vorurteile pendeln, das gehört schon zu den wichtigen Aufgaben der Gegenwart."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "SECHSTER VORTRAG Dornach, 16. Dezember 1917",
    "paragraphs": [
      "Bei all diesen Betrachtungen, die wir jetzt gepflogen haben, stand im Hintergrunde eine Frage, welche von der Gegenwart, die doch in ihren Grundansichten viel materialistischer gefärbt ist, als sie denkt, eben im Lichte des Materialismus angesehen wird. Diese Frage bezieht sich auf das Hervorgehen gewisser geschichtlicher Ereignisse. Man spricht von geschichtlicher Notwendigkeit, man spricht davon, daß dasjenige, was also zum Beispiel in diesem Jahre geschieht, geschichtlich in einer ge­wissen Weise die Wirkung sei von dem, was in vorangehenden Jahren geschehen ist.",
      "Was ich hier als geschichtlich bezeichne, erstreckt sich selbstver­ständlich über alle Glieder des Geschehens, das aus dem menschlichen Handeln hervorgeht, also über das Soziale, das Moralische, das sonstige Kulturleben. Die materialistische Anschauung, die ja nicht bloß darin besteht, daß man auf dem Gebiete der Naturwissenschaft geistige Er­scheinungen aus materiellen Grundlagen herleitet, sondern die noch in mancherlei anderem besteht, diese materialistische Anschauung möchte den Begriff der Freiheit eigentlich am liebsten ganz ausschalten. Und so möchte sie denn dasjenige, was im Laufe der Geschichte sich voll­zieht, auch so auffassen, wie sie gewohnt worden ist, Naturwissen­schaftliches anzuschauen, daß immer mit einer gewissen Notwendigkeit das Folgende wie eine Wirkung hervorgeht aus einer voranliegenden Ursache. Dann sagt man, indem man vielleicht glaubt, recht sachgemäß zu denken: Nun, irgendein Ereignis - auch ein solches Ereignis wie das, was jetzt so furchtbar katastrophal in unser Weltgeschehen herein­gebrochen ist - sei eben eine Notwendigkeit.",
      "In diesem Sinne, das heißt mit dem Begriff «naturwissenschaftliche Notwendigkeit», ist die Anschauung eine völlig unsinnige, wenn auch derAusdruck: irgendein Ereignis sei eine Notwendigkeit-, nach anderer Richtung hin seinen guten Sinn hat. Wenn Sie bedenken, was gestern wiederum vor unsere Seele getreten ist, die Kompliziertheit der mensch­lichen Natur, dann werden Sie auch gefühlsmäßig, nicht nur verstandesmäßig,",
      "einen Einblick gewinnen in die Tiefe der Weltenordnung überhaupt und werden allmählich sich abgewöhnen zu glauben, daß mit den abstrakten naturwissenschaftlichen Gesetzesvorstellungen ir­gendwie diese Wirklichkeit zu umfassen ist.",
      "Ihr Blick wird sich dann auch auf gewisse Naturerscheinungen lenken, die, wenn man sie nur im rechten Lichte betrachten würde, den Menschen mancherlei lehren könnten, auf Naturerscheinungen, wie etwa die folgende. Im Meere entwickelt sich alljährlich eine große An­zahl von Lebenskeimen, die nicht zu Lebewesen werden.",
      "Lebenskeime werden abgelegt und gehen zugrunde. Nur ein kleiner Teil davon wird zu wirklichen Lebewesen. Das geschieht nun natürlich nicht bloß im weiten Meere, das geschieht in der ganzen Natur überhaupt.",
      "Lenken Sie nur den Blick darauf, wieviel eigentlich, wenn Sie nur ein Jahr betrachten, zum Leben vorbestimmt ist, indem die Lebenskeime, die Eier, in ihrer ersten Anlage abgelegt werden und nicht zur Entwicke­lung kommen. Wieviel zum Leben vorbestimmt ist, das nicht Leben wird!",
      "Müssen wir da nicht sagen: Alle diese Lebenskeime enthalten Ur­sachen, aus denen nicht Wirkungen werden? - In der Tat, wer die Natur nicht nach vorgefaßten theoretischen Meinungen betrachtet, namentlich nicht nach der allerbestimmtesten theoretischen Meinung: Alle Ursache hat ihre Wirkung und alle Wirkung hat ihre Ursache -wer die Natur unbefangen betrachtet, der wird finden, daß es Zahl­loses in der Natur gibt, was bezeichnet werden muß in vollem Sinne des Wortes als Ursache, ohne daß daraus eine Wirkung wird in dem Sinne, wie sie es werden müßte, wenn die Ursache sich völlig ausleben würde. Wir sehen gleichsam an unzähligen Punkten immer wieder und wiederum das Leben gewissermaßen aufgehalten, nicht zu seinem Ziele gelangt.",
      "Das ist etwas, was wir draußen in der materiellen Natur sehen kön­nen. Wenn nun der Geistesforscher sich frägt: Wie ist es entsprechend in der geistigen Welt? - da kommt er auf sehr Merkwürdiges. Er kommt auf etwas, was in einem gewissen Sinne genau entspricht dem Stehenbleiben des Lebens in der Natur, aber eben so, wie Geistiges Natürlichem entspricht. Und wir wissen aus zahllosen Betrachtungen, daß in sehr vielen Fragen, nicht in allen, das Geistige gerade dadurch",
      "zu charakterisieren ist, daß es in seinen Eigenschaften entgegengesetzt dem Natürlichen ist, gerade entgegengesetzt. So wie wir in den Fällen, von denen ich gesprochen habe, Naturursachen haben, die nicht zu ihren Wirkungen kommen, wo wir also gleichsam sehen: hier bricht der Prozeß ab und bricht dasjenige ab, was in ihm, wie man sagt, ver­anlagt ist und nicht zur Ausbildung gelangt - obwohl das Wort «ver­anlagt» wiederum zu den schlechtesten Worten gehört, die da sind, um die Wirklichkeit zu verstehen -, so sehen wir umgekehrt als Geistes-forscher in der geistigen Welt Wirkungen auftauchen, Wirkungen ent­stehen, von denen ebensowenig gesagt werden kann, da sind Ursachen, wie von den eben charakterisierten Ursachen gesagt werden kann, da sind Wirkungen.",
      "Fragen wir jetzt einmal im Konkreten: Was gibt sich denn den Blicken des Geistesforschers kund, wenn er das Seelenauge auf solche aufgehaltene Lebensvorgänge richtet wie die charakterisierten? Das physische Auge sieht, daß da einfach Keimanlagen zugrunde gehen; aber das geistige, das Seelenauge sieht, daß da, wo solche Keimanlagen -scheinbar nur - zugrunde gehen, Wesenhaftes entsteht auf einer frü­heren Stufe, auf einer noch nicht materiellen Stufe. Würde der Mensch verfolgen wollen, was in einem solchen Falle, wo gewissermaßen ma­terielle Ursachen keine Wirkungen haben, wirklich geschieht, dann müßte er, wenn ich den Ausdruck gebrauchen darf, kosmisch träumen. Der Mensch kann im gewöhnlichen Bewußtsein nur egoistisch träumen. Wenn er in der Nacht träumt, so träumt er in Gebundenheit an seinen eigenen Organismus; er ist im Traume nicht verbunden mit der Um­gebung. Kann er verbunden sein mit der Umgebung und dieselben Kräfte entwickeln, die er sonst im Traume entwickelt, so ist er eben im imaginativen Vorstellen.",
      "Was da aufgehalten wird im Naturprozeß, was nicht zu physischen Lebewesen wird, das wird zu etwas, was nun der imaginativen Vor­stellung sehr wohl zum Bewußtsein kommen kann. Wesen entstehen aus solchen aufgehaltenen Lebenskeimen, die nur den imaginativen Vorstellungen zugänglich sind, Wesen, von denen man träumen könnte, wenn man nicht als Mensch träumte, sondern als ein Wesen aus der Hierarchie der Angeloi träumte. Die Angeloi träumen in der Tat, wenn",
      "ich den Ausdruck gebrauchen darf, von jenen Wesen, die alljährlich zahlreich aufsteigen als elementarische Gestaltungen aus dem Meere, aus der Erde, die nichts anderes sind als Produkte der scheinbar zu­grunde gegangenen Lebenskeime.",
      "Wenn Sie sich den Gedanken recht lebendig machen, da sehen Sie aus der Erde aufsteigen wie einen geistigen Duft elementarisches Leben, in das wir eingebettet sind, in dem wir drinnenstehen mit unserer Seele. Aber wir stehen in einer viel intensiveren Weise noch in diesem elemen­tarischen Leben drinnen, denn wir sind beteiligt an dem Prozesse, von dem ich gesprochen habe.",
      "Wir sind gar sehr als Menschen daran be­teiligt. Und die Tiere sind auch daran beteiligt. Wieso? Nun, es ist gar keine Verschiedenheit zwischen dem, was da geschieht, wenn im Meere so und so viel Fischeier abgelegt werden, die nicht Fische werden, son­dern die nur zu einem elementarischen Dasein die Veranlassung geben, und dem, was dann geschieht, wenn wir auf einem Felde aus der Erde die Saat herauswachsen sehen, sagen wir die Weizensaat.",
      "Wie viele Weizenkörner wachsen da heraus, die alle als Ursachen vorbestimmt sind, selbst wiederum Weizenhalme zu bilden, und die es nicht werden, weil wir sie essen! Da sind wir es selbst in unserem in derWelt stehenden Prozesse, welche sich verbinden mit dem, was da als elementarisches Dasein sich entwickelt.",
      "Wir halten auch in den Weizenkörnern und in den andern Produkten, aus denen wir unser Leben nähren, den fort­laufenden, den fortgehenden Prozeß auf. Wir lassen nicht wirkliche Wesen daraus werden, sondern wir bewirken durch unser eigenes Da­sein die Verwandlung desjenigen, was zu ganz anderem bestimmt ist, in elementarischen Prozessen, die nur durch Imaginationen erreichbar sind.",
      "Aber diese Wirklichkeit, die diesem imaginativen Leben zugrunde liegt, spielt sich dadurch ab, daß wir selbst hineingestellt sind in den Prozeß, daß wir daran teilnehmen. Aus den Weizenkörnern, aus den Roggenkörnern, aus allem übrigen, was wir in dieser Weise aus der Natur genießen, aus alledem entwickelt sich elementarisches Leben, und dieses elementarische Leben zieht durch uns.",
      "Dieses elementarische Leben nehmen wir auf, in diesem elementarischen Leben stehen wir drinnen.",
      "Da sehen Sie auf den Grund eines elementarischen Lebens. Da sehen",
      "Sie, wie wir gewissermaßen nur dadurch in der Welt da sein können, daß wir einen andern fortgehenden Prozeß aufhalten und ihn zur Ver­geistigung bringen. Auch wenn wir essen, bringen wir einen Prozeß, der sonst rein materiell zu verlaufen bestimmt ist, zur Vergeistigung.",
      "Das Umgekehrte ist in der geistigen Welt vorhanden. Da ist die Sache so, daß nun Wirkungen da sind, welche nicht in demselben Sinne Ursachen haben wie die Bewegungen einer Billardkugel, die durch eine andere gestoßen wird, sondern welche gewissermaßen auftreten, ohne daß anzugeben ist: dies oder jenes ist ihre Ursache. Der Begriff von Ursache und Wirkung verliert eben, wenn wir den Blick auf solche Dinge wenden, seinen Sinn. In unser seelisch-geistiges Leben treten Wir­kungen herein, Wirkungen aus der geistigen Welt, von denen nicht ge­sagt werden kann, daß sie verursacht seien. So wie wir nun den elemen­tarischen Wirkungen, die gewissermaßen als Duft aufsteigen aus den geschilderten Prozessen, mit Begierde gegenüberstehen, mit jener Be­gierde, die aus unserer Lebensnotwendigkeit entspringt: wir wollen uns nähren, daher sind wir angewiesen, in jene elementarischen Prozesse, die geschildert worden sind, uns einzuspinnen -, so wie wir diesen Pro­zessen mit einer gewissen Begierde gegenüberstehen, so stehen wir, inso­fern wir Menschen des physischen Planes sind, eigentlich den geistigen Wirkungen, die in gewissem Sinne ursachenlos sind, mit Abneigung, mit Antipathie gegenüber. Wir haben das Bestreben, solche Wirkungen, die aus dem Geistigen kommen, insofern wir physische Menschen sind, nicht in uns hereinkommen zu lassen.",
      "Fassen Sie diesen etwas subtilen Gedanken, dann werden Sie sehen: Wir sind gewissermaßen von einem geistigen Wollen umgeben, das in uns herein will, das in uns herein strebt, und dem wir zunächst nicht mit Begierde gegenüberstehen, das wir zunächst gar nicht die Geneigt­heit haben, ohne weiteres in uns aufzunehmen. Es ist, wie wenn in der Luft um uns herum fortwährend Willensregungen schwebten, denen gegenüber wir uns abweisend verhalten. Das ist auch etwas, worauf das hellseherische Bewußtsein bald führt, wenn es zur Entwickelung ge­langt ist: die Einsicht, wie gewissermaßen Bildhaftes in unserer Um­gebung wandelt, wallt, und wie wir innere Widerstände haben, dieses Bildhafte in uns aufzunehmen.",
      "Betrachten wir dieses Bildhafte als eine Wirklichkeit. So wahr jedes Jahr auf der Erde so und so viele Lebenskeime zugrunde gehen, so wahr lebt in der Welt, die uns als geistige Welt immer umgibt, Geistig-Bild­haftes, durch Imagination auch zu Erreichendes, dem wir aber durch unsere Menschenanlage leicht Widerstand entgegensetzen.",
      "Die Widerstände sind nun nicht in Abstraktheit bloß allgemein zu fassen, sondern diese Widerstände sind konkret differenziert zu fassen. Was sich im physischen Leben wie aufsteigendes elementarisches Leben jedes Jahr entwickelt, das entwickelt sich in andern Zeitperioden, geistig herabsteigend, zu einem solchen, das wir ablehnen - in andern Zeiträumen eben, und zwar nicht in ganz regelmäßigen Zeiträumen. Es gibt Zeiten, in denen gewissermaßen das geistige Leben vehement uns umspielt und vieles an uns heran will. Andere Zeiten gibt es, in denen gewissermaßen die Geistesluft um uns herum ärmer ist. Der Mensch kann sich nun mehr oder weniger empfangend verhalten, ob­wohl er im allgemeinen Abneigung hat, diese durch Imaginationen erreichbare bildhafte Wesenheit in sich aufzunehmen. Er kann sich aber doch empfänglich durch irgendwelche Vorbedingungen verhalten, von denen wir noch zu sprechen haben werden, oder er kann sich ganz ablehnend verhalten.",
      "Nehmen wir an, es wäre in irgendeinem Zeitalter, ich möchte sagen, ein besonderer Andrang von solchen Wesenheiten, von Wesenheiten, die gewissermaßen geistig an den Menschen heran wollen, und der Mensch wäre abgeneigt, diese Wesenhaftigkeit in sich aufzunehmen. Was wird geschehen? Dann wird das geschehen, daß der Mensch, da-durch daß er ablehnt, solches ihm zukommendes Geistig-Wesenhaftes aufzunehmen, in sich selbst die Gelegenheit schafft - die Menschheit also in sich selbst die Gelegenheit schafft -, daß das Alte, das dürr ge­worden ist, trocken geworden ist, sich fortspinnt und, statt zu leben-diger Wirkung zu kommen, eine tote Wirkung hervorbringt: geradeso wie wenn eine Pflanze, die ihre Lebenszeit absolviert hat, nicht weg-geschafft würde, sondern als verholzte Pflanze trocken und ausgedörrt noch weiter zum Schaden der Umgebung bestehen würde.",
      "Im geschichtlichen Werden nimmt sich das in der folgenden Weise aus: Wenn ein Zeitalter kommt - und ein solches Zeitalter war im wesentlichen",
      "der Beginn des 20. Jahrhunderts -, wo Geistig-Wesenhaftes gewissermaßen wartet, um an den Menschen heranzukommen, wo für den Menschen alle Aufforderung dazu besteht, die Seele zu öffnen für neue Offenbarungen und der Mensch diese Offenbarungen nicht auf­nehmen will, abgeneigt ist für solche Offenbarungen, dann spinnt sich das Alte in ungehöriger Weise fort. Denn dieses Alte braucht Neu-befruchtung auf dem Umwege durch den Menschen. Die wird nicht vollzogen. Unbefruchtetes spinnt sich dürr, trocken fort, und dann entstehen solche Ereignisse, wie das gegenwärtige katastrophale Ereig­nis ist.",
      "Unter den mancherlei Ursachen, die man in der geistigen Welt fin­den kann, ist diese geradezu eine der hauptsächlichsten, daß die Ent­wickelung gegen das 20. Jahrhundert zu so gegangen ist, daß die Men­schen sich gesträubt haben - aus Ursachen, die wir noch besprechen werden - gegen neue Offenbarung. Man könnte sagen: Die geistige Welt war voll von dem, was sich der Menschheit anbot an neuen gei­stigen Erkenntnissen, an neuen geistigen Impulsen, und die Menschheit hat es zurückgewiesen. Aus welchem Grunde? Gewiß, solche Dinge hängen auch mit Entwickelungsbedingungen der Menschheit zusam­men. Wir wissen ja, es mußte die materialistische Zeit kommen, denn sie hat nach gewissen andern Seiten hin ihre guten Eigenschaften. Also diese materialistische Zeit kam, und eine Folge dieser materialistischen Zeit war die, daß die Mcnschen Begriffe ausbildeten, welche nur auf einen Teil der Menschennatur sich beziehen.",
      "Denken Sie an dasjenige, was wir gestern besprochen haben. Wir haben gestern besprochen, daß dieser viergliedrige Mensch, der, im groben Sinne genommen, aus dem physischen, dem Äther- oder Bilde­kräfteleib, dem astralischen Leib und dem Ich besteht, eigentlich mit Bezug auf alle diese Teile, diese Glieder verschiedenes Alter hat. Wenn ein Mensch achtundzwanzig Jahre alt ist, dann ist er nur in bezug auf seinen physischen Leib, sagte ich gestern, achtundzwanzig Jahre alt, mit Bezug auf den sogenannten Atherleib einundzwanzig Jahre, mit Bezug auf den astralischen Leib vierzehn Jahre, mit Bezug auf das Ich erst sieben Jahre. Sie können gut aus dem, was gestern besprochen wor­den ist, die Anschauung gewinnen: da steht ein Mensch mit achtundzwanzig",
      "Lebensjahren; aber das ist im uneigentlichen Sinne gesprochen: der Mensch mit diesen achtundzwanzig Lebensjahren ist nur als phy­sischer Mensch achtundzwanzig Jahre alt. In diesem Menschen lebt zum Beispiel das Ich - wenn wir von dem andern absehen -, das lang­samer lebt, das dann noch ein Kind von sieben Jahren ist, wenn der Mensch achtundzwanzig Jahre alt ist.",
      "Dieses Kind von sieben Jahren, wenn der Mensch seinem physischen Leibe nach achtundzwanzig Jahre alt ist, das steht in der Tat mit ganz andern Welten in Verbindung, als diejenige Welt ist, in der naturwissenschaftliche Notwendigkeit herrscht. Aber in dem materialistischen Zeitalter haben die Menschen sich gewöhnt, nur diejenigen Begriffe sich zu bilden, welche anwendbar sind auf das Verhältnis des physischen Leibes des Menschen zu der phy­sischen Umgebung, und nach diesem wird alles beurteilt.",
      "Der Mensch ist als wirklicher Mensch, wie er drinnensteht in der Welt, eine kompli­zierte Wesenheit, so kompliziert, wie wir das gestern wieder besprochen haben und von vielen Betrachtungen her kennen. Was der Mensch über sich zu wissen glaubt, was er von sich aussagt, das ist für unser materia­listisches Zeitalter eigentlich nur ein Viertel von dem, was sich auf den Menschen bezieht, nur dasjenige, was sich auf den physischen Leib be­zieht.",
      "Nur für dieses Verhältnis des physischen Leibes zur Umgebung kann man von naturwissenschaftlicher Notwendigkeit sprechen. Wo­von muß man sprechen, wenn wir von dem übrigen wieder absehen, in bezug auf das, was zum Beispiel in dem achtundzwanzigjährigen Menschen noch ein siebenjähriges Kind ist?",
      "Da muß man von etwas ganz anderem sprechen, von dem diese unendlich aufgeklärte Gegen-wart, diese unendlich gescheite Gegenwart sich ganz abgewendet hat. Da muß man sprechen, so sonderbar das den Menschen der Gegenwart klingt, von dem Wunder.",
      "Wunder in dem Sinne, wie vielfach Menschen sich Wunder vorstel­len, Wunder, wie sich auch diejenigen Menschen vorstellen, die gern in spiritistische Sitzungen gehen, das sind Dinge, von denen die wahre Geisteswissenschaft nicht sprechen kann. Wunder liegen auf ganz an­dern Gebieten. Wunder liegen im geistigen Geschehen. Denn wie im äußeren, natürlichen Geschehen Notwendigkeit liegt, so liegen die Wunder auf dem Felde des geistigen Geschehens. Kein Mensch, der hereintritt",
      "aus der geistigen Welt in die physische Welt, der zur physischen Verkörperung schreitet, ist eine physische Notwendigkeit. Eine Not­wendigkeit ist er, weil er diese Notwendigkeit sich selbst setzt, weil er aus der geistigen Welt heraus den überbewußten Beschluß faßt, sich mit irgendeiner Vererbungsströmung zu verbinden. Bei Vater und Mut­ter braucht nicht die Ursache zu liegen, liegt nur die Gelegenheit. Jedes Menschen Auftreten in der physischen Welt ist ein Wunder. Daß dies hereintritt in die physische Welt, was in unserem achtundzwanzigsten Jahre erst sieben Jahre alt ist, das ist immer ein wirkliches Wunder, gegenüber dem jedes Fragen in naturwissenschaftlicher Weise nach der Ursache ein ganz gewöhnlicher Unsinn ist. Dasjenige, was so langsam in uns lebt, daß es im achtundzwanzigsten Jahre erst sieben Jahre alt ist, aus der Vererbung herzuleiten, das ist ein Unding. Wollen wir wirk­lich eine Herleitung vornehmen, wollen wir fragen: Woraus stammt das, was da im achtundzwanzigsten Jahre erst sieben Jahre alt ist? - so kommen wir zurück in die geistige Welt, in jene Welt, die wir mit den sogenannten Toten gemeinschaftlich haben, in jene Welt, die wir mit­bevölkert haben, bevor wir herabgestiegen sind zu unserem Körper. Geister, welche unbefangen denken konnten, vermochten sich schon Begriffe von solchen Sachen zu verschaffen, wenn auch in unserem materialistischen Zeitalter nur auf schwierige Weise.",
      "Bedenken Sie, wieviel Goethe sich befaßt hat mit naturwissenschaft­lichen Vorstellungen, wie er es geradezu zu musterhaft naturwissen­schaftlichen Vorstellungen gebracht hat! In ihm lebte, wie Sie wissen, die fortdauernde Sehnsucht nach Italien, bevor er nach Italien ge­kommen ist. Und als er in Italien die großen Kunstwerke, die ihm eine Vorstellung von der griechischen künstlerischen Schöpfertätigkeit ge­geben haben, gesehen hat, schrieb er an seine Freunde in Weimar: «Da ist die Notwendigkeit, da ist Gott.» Er sprach von einer andern Not­wendigkeit, als die ist, von der die bloße Naturwissenschaft spricht. Von dieser Notwendigkeit hätte er gerade nach seinen naturwissen­schaftlichen Vorstellungen früher schon eine Empfindung haben kön­nen; die Notwendigkeit, die hereinleuchtete aus der geistigen Welt und die identisch ist mit dem Wunder, die empfand er, als er in Italien der griechischen Kunstwerke ansichtig wurde.",
      "Aber unsere Zeit ist aufgeklärt, die Menschen unserer Zeit sind sehr gescheit. Daher haben sie nicht nur den unberechtigten Wunderbegriff abgelehnt, sondern das Wunder überhaupt als solches auch aus der geistigen Welt verbannt. Aber das Wunder aus der geistigen Welt ver­bannen, das heißt nichts anderes, als alles das zu tun, um diese geistige Welt überhaupt nicht verstehen zu können. Denn aus der geistigen Welt treten die Dinge so heraus, daß wir nur Wirkungen sehen; wenn wir die Ursache suchen, so können wir sie nicht finden. Gerade dann, wenn man Geistesforscher ist, drängt sich einem das als eine unbedingte Wahrheit auf. Und weil die Gefühllosigkeit der Menschheit am Ende des 19.Jahrhunderts für die Verwunderung, für die Ehrfurcht des­jenigen, was sich aus der Welt heraus offenbaren will, bis zu einem ge­wissen hohen Grade gestiegen war, so war eine Abneigung gegen die Offenbarung vorhanden. Denn in demselben Sinne, in dem sich die Ehrfurcht entwickelt gegenüber allem, was Welttiefe ist, in demselben Maße kommen diese Offenbarungen auch an den Menschen heran.",
      "Dasjenige, was als Wunderwirkung eintreten kann in die Welten-ordnung, das kann auch ausbleiben, das kann auch weg sein. Mit dieser Abstumpfung der Menschheit für das Wunder hängt das zusammen, was in dem Zeitalter, das gegen das 20. Jahrhundert heranrückte, unter­lassen worden ist. Und wenn man von Ursachen sprechen will zu un­seren katastrophalen Ereignissen, dann sind diese Ursachen nicht solche, welche die Menschen geschaffen haben, sondern es sind diese Ursachen Unterlassungssünden. Das ist das Wesentliche, worauf es ankommt.",
      "Ich habe in früheren Jahren in einem Vortrage, den ich öfter gehal­ten habe, aufmerksam gemacht, wie in der Mitte des 19. Jahrhunderts ein ausgezeichneter Philosoph gelebt hat: Karl Christian Planck. Ich habe an vielen Orten Gelegenheit genommen, auf diesen Karl Christian Planck hinzuweisen, aus dem Grunde, weil er eine Schrift geschrieben hat, die er gewissermaßen als sein philosophisch-literarisches Testa­ment hinterlassen hat. Und in dieser Schrift ist bis in große Einzel­heiten, auch bis in geistige Einzelheiten die gegenwärtige Weltkata­strophe, man kann nicht einmal sagen, angedeutet, sondern im vor­hinein geschildert. Das Buch war 1880 geschrieben. Warum konnte er das? Weil Planck eben zu denjenigen Geistern gehörte, die zur richtigen",
      "Zeit sahen, was geschieht. Wenn Sie irgendein Haus haben, das bau­fällig ist, so muß es zur rechten Zeit ausgebessert werden. Warten Sie, bis es nicht mehr ausgebessert werden kann, so fällt es zusammen, und es kommt die Katastrophe.",
      "Und unsere jetzige Katastrophe ist nichts anderes als ein Zusammenfallen. In Wirklichkeit betrachtet, ist es ein Zusammenfallen. Für das, was hätte geschehen sollen, waren die sieb­ziger, achtziger Jahre des vorigen Jahrhunderts die richtige Zeit.",
      "Solche Geister wie Karl Christian Planck, die hingewiesen haben auf das, was da kommen muß, die sind ja bekanntlich niemals geeignet, im äußeren Leben führende Persönlichkeiten zu werden! Wenn es sich irgendwo darum handelt, zu einer führenden Persönlichkeit zu greifen, einen Staatsmann zu finden oder dergleichen, da greift man selbstverständ­lich nicht zu denjenigen, die im Sinne von Karl Christian Planck etwas wissen - die kann man doch nicht nehmen, nicht wahr -, sondern man greift zu andern, die sehr oft nicht die Möglichkeit finden, das bau­fällige Haus zu stützen.",
      "Aber man kann heute den historischen Nach­weis liefern, wenn man nur in die Hintergründe des Lebens sieht - und Karl Christian Planck ist nicht der einzige, es gibt manche andere -, daß zur rechten Zeit manchen Leuten aus der geistigen Welt die Offen­barung gekommen ist, welchem Ereignisse die Menschheit entgegengeht. Damals wäre auch noch die Zeit gewesen, diesem Ereignisse einen an­dern Lauf zu geben.",
      "Natürlich wurde Karl Christian Planck nicht gehört.",
      "Aber werden denn jetzt die Menschen gehört, die von dem reden, was eben, wenn es wirksam sein soll, Jahre vor dem ausgesprochen wer­den muß, bevor der Zusammenbruch eintritt? Man muß leider sagen:",
      "Die Art und Weise, wie die Menschheit dieses katastrophale Ereignis bis jetzt durchlebt, läßt deutlich erkennen, daß, wenn dieses katastro­phale Ereignis noch vier Jahre andauert, die Menschen sich daran ge­wöhnt haben werden und es hinnehmen werden - nun, wie eben das normale Leben; denn bis zu einem hohen Grade ist diese Gewöhnung schon fortgeschritten. Wer aber die Zeichen der Zeit versteht, der frägt heute: Was muß geschehen? - weil, wenn etwas nicht geschieht, nach Jahrzehnten dasjenige sich zeigt, was da kommen muß, weil etwas nicht zur rechten Zeit geschehen ist.",
      "Aber aus der umliegenden physischen Welt heraus kann das nicht gefunden werden, was nach den heutigen Zeitbedingungen geschehen soll. Heute muß man schon, wenn man das Richtige hören will, die­jenigen hören, die aus der geistigen Welt heraus sprechen können. Natürlich, für unbedeutendere Dinge vollziehen sich die Dinge rascher. Man kann sagen: In fünf Jahren werden vielleicht die Menschen ein­sehen, daß sie auf manches hätten hören sollen, was sie heute schon hätten wissen können, wenn sie hingehört hätten. Doch sie sind nicht geneigt, diese Dinge zu hören, weil sie nur geneigt sind, auf das zu hören, wofür sich schon die Anzeichen in der äußeren physischen Welt zeigen. Aber die physische Welt ist für das geschichtliche Werden un­bedeutend. Sie zeigt nicht dasjenige, was Anstoß, Impuls sein soll zum Geschehen. Was Anstoß, Impuls sein soll zum Geschehen im sozialen, im sittlichen Leben, das muß aus der geistigen Welt stammen.",
      "Nun, für ein größtes Ereignis im Verlaufe der Menschheitsentwicke­lung soll gerade die Menschheit in unserem Zeitalter erzogen werden: an Freiheit auch in der historischen Entwickelung zu glauben. An einem bestimmten Punkte des geistigen Lebens soll die Menschheit der Gegen­wart mit aller Gewalt darauf gestoßen werden, an Freiheit - und iden­tisch damit ist dann das Wunder - zu glauben. Und dieser Punkt ist in der Auffassung des Christus-Impulses, in der Auffassung des Myste­riums von Golgatha gelegen. Wie die Menschheit zum Mysterium von Golgatha stand, das war ganz anders in früheren Zeiten und war immer mehr anders, je weiter wir zurückgehen in der geschichtlichen Ent­wickelung. Wir haben öfters davon gesprochen. Heute gibt es nicht in den Menschen - gerade nicht in den im Sinne des Zeitgeistes fortge­schrittensten Menschen - die Möglichkeit, das Ereignis von Golgatha als historisches Ereignis wie andere historische Ereignisse hinzustellen. Ich brauche für Sie das, was hier als Voraussetzung in Betracht kommt, nur anzudeuten: Sie wissen, die Evangelien sind als historische Doku­mente in ihrer Bedeutung erschüttert. Nicht in demselben Sinne, wie wir die Dokumente über Sokrates oder Plato oder über Alkibiades oder Cäsar als historische Dokumente nehmen, können wir nach dem, wie heute geschichtlich geforscht wird, die Evangelien als Dokumente an­sehen, ebensowenig die andern Dokumente, die im Neuen Testament",
      "über das Ereignis von Golgatha vereinigt sind. So wie der Mensch heute über geschichtliches Forschen denkt, so entzieht sich diesem geschicht­lichen Forschen die Möglichkeit, die Evangelien als historische Doku­mente zu betrachten und aus den Evangelien das Ereignis von Golgatha als ein historisches anzusehen, als ein historisch beweisbares, meine ich, als ein in dem Sinne historisch beweisbares, wie man andere historische Geschehnisse und Tatsachen geschichtlich belegt und geschichtlich be­weist. Man kann nicht in demselben Sinne über den Christus Jesus als eine historische Persönlichkeit sprechen, wie man über Karl den Großen nach dem, was man heute historische Quellen nennt, als eine historische Persönlichkeit sprechen kann.",
      "Für den, der die Dinge durchschaut, ist heute der Zeitpunkt heran­gekommen, wo der aufrichtige, Wahrheit-durchdringende Menschen-sinn sich sagen muß: Was man für historische Quellen hielt in bezug auf das Mysterium von Golgatha, ist durch die Gestalt, welche die Ge­schichtsforschung angenommen hat, erschüttert. Und man muß schon so etwas wie ein Stumpfling sein, wie zum Beispiel Adoll Harnack, der berühmte Theologe, um sich immer wieder und wiederum hinzu­stellen und von dem, was man, wie er sagt, auf einer Quartseite zusam­menstellen kann über den Christus Jesus, zu behaupten: darinnen seien doch historische Dokumente im Sinne der heutigen Geschichte gegeben. Es sind natürlich in diesen Dingen, die auf dieser Quartseite stehen, ebensowenig historische Dokumente gegeben, wie in den Evangelien -nach Harnack selber - historische Dokumente gegeben sind. Aber sol­ches Unterfangen wie das Harnacksche, dem hunderte und hunderte von andern gegenüberstehen, hängt eben zusammen mit der ganzen Unwahrhaftigkeit unserer Zeit in solchen Dingen, die niemals bis zu den radikalen Folgerungen gehen will, welche aber eben einfach die richtigen Folgerungen sind.",
      "Die Folgerung, die ja gezogen werden muß, ist diese, daß der Mensch nach dem, was vorliegt, sich heute gestehen muß: sucht er auf äußerlich historischeWeise den ChristusJesus, so kann er ihn nicht finden. Finden muß er ihn auf dem Wege der Geisteserforschung. Da findet er ihn aber sicher. Da findet er das historische Ereignis von Golgatha. Warum? Weil das historische Ereignis von Golgatha ein solches war, das durch",
      "Freiheit in der Menschheitsentwickelung aufgetreten ist, durch eine Freiheit in noch viel höherem Sinne als andere historische Ereignisse, und weil dieses freie Ereignis gerade in unserem Zeitraum an den Men­schen so herantreten soll, daß nichts ihn zwingt, seine Geltung anzu­nehmen, sondern er diese Geltung aus innerer Freiheit annehmen muß. Wofür ein historischer Beweis schon da ist, für dessen Annahme ist man nicht frei. Wofür ein äußerer historischer Beweis nicht da ist, das nimmt man an aus geistigen Gründen, und auf dem geistigen Boden ist man frei. Christ wird man durch Freiheit. Und das ist gerade dasjenige, was notwendig ist dem heutigen Zeitalter zu verstehen, daß man Christ in Wirklichkeit nur sein kann aus voller Freiheit, nicht einmal ge­zwungen durch historische Dokumente. In unserem Zeitalter soll das Christentum jene Wahrheit gewinnen - das ist vorbestimmt dieser Zeit -, wodurch es zu dem großen Impuls des menschlichen Verständ­nisses für die Freiheit wird. Das gehört zu den Fundamentalwahrheiten in unserer Zeit, daß dies eingesehen wird, daß eingesehen wird, daß die Beweise für das Christentum in der geistigen Welt gesucht werden müssen.",
      "Wird diese Einsicht so intensiv in der menschlichen Natur, wie sie werden soll, so wird sie auch andere Einsichten erzeugen, wird manches andere noch hervorbringen. Was sie zunächst hervorbringen sollte, das ist, daß der Mensch überhaupt lerne, sich die Frage zu beantworten:",
      "Wie mache ich mich empfänglicher für das, was mich nicht aus der physischen Welt heraus zwingt, es anzuerkennen, sondern wogegen ich zunächst vielleicht sogar eine Abneigung, eine Antipathie habe? Was macht mich geneigter dazu?",
      "Wirklich nicht aus persönlicher Eitelkeit und Albernheit, sondern weil ich eben nur ein konkretes Exempel dabei statuieren will, muß ich bei einer solchen Gelegenheit immer wieder darauf aufmerksam machen, daß ich meine schriftstellerische Laufbahn damit begonnen habe, indem ich nicht meine Meinungen zunächst vertreten habe, son­dern alles dasjenige, was ich vertreten habe, in Anknüpfung an Goethe­schen Geist publizierte, im bewußten Zurückblicken zu einem Geiste, der schon 1832 in das geistige Reich der sogenannten Toten hinauf­gestiegen ist. Aber lesen Sie das, was ich so in Anknüpfung an Goethe",
      "in den Zeiten, die meiner «Philosophie der Freiheit» vorangegangen sind, geschrieben habe! Die sogenannten Goethe-Forscher sehen es zu­meist daraufhin an, ob es Goethesche Ansichten wiedergibt. Goethesche Ansichten sind diesen Leuten dann gegeben, wenn man ein literarischer Wiederkäuer ist, das heißt, wenn man das, was Goethe in seiner Inkar­nation gesagt hat bis 1832, wiederkaut. Ich war immer der Ansicht, daß dasjenige, was Goethe gesagt hat, wirklich nicht von dem oder jenem Schulmeister und auch nicht von mir wiedergesagt zu werden braucht, denn Goethe hat, was er hat sagen wollen, schon selber besser gesagt. Es ist immer besser, wenn die Goetheschen Werke gelesen wer­den, als die Ansichten der Schulmeister, und wären es selbst so aus­gezeichnete Schulmeister und Magister, wie zum Beispiel Lewes mit seiner berühmten Goethe-Biographie ist.Was ich versuchte zu schreiben, ist dasjenige, was auf der Inspiration des nicht mehr auf der Erde weilenden Goethe beruhte: die Fortbildung seiner Ansichten auf einem gewissen Gebiete nach seinem Tode, was geschrieben werden konnte aus einem gewissen Gefühl lebendiger Verbindung mit sogenannten verstorbenen Seelen.",
      "Ich erwähne dies als ein Exempel, wirklich nicht aus alberner Eitel­keit, sondern weil es zusammenhängt mit der Frage: Was sollen die Menschen tun, um sich empfänglicher zu machen für dasjenige, was aus der geistigen Welt heraus kommt? Verbinden müssen sich die Men­schen mit den Toten. Den Weg müssen sie finden in diejenigen Welten, worinnen die Toten leben, aber in einer vernünftigen, verständigen Weise, in einer wirklich entsprechenden Weise, nicht nach spiritistischer Weise. Die Toten reden weiter nach ihrem Tode. Und das, was sie reden, was sie impulsieren, es lebt, wie wir gesehen haben, zwar nicht in unseren Sinneserfahrungen, nicht in unserem Vorstellen, wohl aber in unserem Gefühl und in der Realität unserer Willensimpulse. Da lebt es drinnen.",
      "Dann müssen wir aber auch das in uns finden, was uns geneigt macht, an die geistige Welt überhaupt heranzutreten. Mit dem Un­glauben an ein Herantreten an die geistige Welt ist verbunden die Anti­pathie gegen die Imaginationen, die herein wollen aus der geistigen Welt, die unser Handeln auch im sozialen Menschengeschehen, im moralischen,",
      "im ethischen Menschengeschehen impulsieren wollen, und die doch einzig und allein den Menschen frei machen können.",
      "Zwei Dinge sind in unserer Zeit notwendig: einzusehen, daß das Bekenntnis zum Mysterium von Golgatha eine freie Tat der mensch­lichen Seele sein muß und dieses ganz zu durchdringen. Und auf der andern Seite: real, nicht bloß abstrakt, nicht bloß in einem abstrakten Glauben, sondern real die Brücke zu suchen zu den Toten. Auch gegen das letztere spricht viel in unserer Zeit. Die Menschen sehen nicht gleich ganz ein, was alles dagegen spricht. Was stellen sich die Menschen heute für das soziale Geschehen als ein Ideal vor? Sie stellen sich vor: Wir sind gescheit, denn wir sind geboren, wir sind in die Schule gegangen, wir sind also gescheite Wesen, gescheite Menschen, daher wissen wir ohne weiteres, was im sozialen Leben zu geschehen hat. Wir bilden Ver­sammlungen, Gemeinderäte, Staatsräte, Parlamente, wie man es nennt, da bespricht man selbstverständlich dasjenige, was zu geschehen hat im sozialen Leben, denn wir sind gescheit, und wenn sich so gescheite Leute, wie es die Menschen der Gegenwart sind, zusammensetzen, so wird immer das Richtige herauskommen.",
      "Das ist das Ideal. Aber das geht von einer Voraussetzung aus, die nicht richtig ist. Es geht von der Voraussetzung aus, daß man ohne weiteres wisse, was das Richtige ist. Wissen Sie, was das Richtige ist? Wissen Sie, wer es weiß, was das Richtige ist im Jahre 1917? Nicht die­jenigen, die jetzt in den Zwanzigerjahren sind und sich in den Parla­menten am liebsten so zum Reden bloß zusammensetzen und darüber urteilen, was das Richtige sei für 1917, sondern das wissen die am besten, die längst gestorben sind! Bei denen sollte man fragen, wie man sich zu verhalten hat! Hier liegt ein gut Teil von dem, was die Frage beantwortet: Wie kann unser soziales Leben aufgebessert werden? -Wenn wir lernen, die Toten zu befragen.",
      "Bis zu seinem Lebensende weiß man in der Regel hier als physischer Mensch alles doch nur so weit, als es einem selber persönlich frommt. Recht reif wird das Wissen erst, wenn man gestorben ist. Dann wird es erst so reif, daß es richtig anwendbar ist auf das soziale Leben. Aber man darf nicht glauben, daß nun die Toten wie mit physischen Hän­den unmittelbar eingreifen sollen, so ungefähr wie Menschen, die hier",
      "im physischen Leib leben. Die Toten können besser wissen als die Le­bendigen, was sozial zu geschehen hat, aber sie müssen gehört werden von den Menschen, und die ausführenden Organe müssen die hier im Physischen lebenden Menschen sein. Lernen müssen vor allen Dingen die Menschen in der Gegenwart, solche ausführenden Organe zu sein. Aber von solchen - wenn ich den Ausdruck gebrauchen darf, er ist so unangenehm - von solchen «Parlamenten», wo sich die Menschen be­streben werden, die Toten mitreden zu lassen, wird man noch lange nicht hören. Es wird jedoch auf gewissen Gebieten nicht Heil kommen, wenn man nicht die Toten wird mitreden lassen wollen, wenn nicht auch von dieser Seite her das soziale Leben spiritualisiert werden kann. Bevor man sich dem Glauben hingibt, daß die hier auf der Erde er­rungene, durch die Geburt, Welt und Schulung errungene Weisheit reif für soziale Impulse ist, sollte man sich vertiefen in das, was wirklich reif geworden ist für soziale Impulse: diejenige Weisheit, die schon den physischen Leib abgelegt hat, und die, wenn wir sie wirklich durch­forschen, uns erst bedeutsame Perspektiven eröffnet.",
      "Bedenken Sie, wie das Gefühlsleben vertieft wird, das ganze mensch­liche Gemüt eine Vertiefung erfährt, wenn das, was ich jetzt als Ideen ausgesprochen habe, eben Gefühl und Empfindung wird; wenn an die Stelle des alten Mythos, der den Gegenwartsmenschen verband mit den Vorfahren, dasjenige Band tritt, das ich angedeutet habe: ein konkretes geistiges Leben, das unsere geistige Atmosphäre wiederum anfüllen wird; und wenn, was so durch die Geisteswissenschaft als Ideen erfaßt werden kann, übergeht in Gemüt und Empfindung und die Menschen wahrhaftig drinnen leben wollen."
    ],
    "sentences": [
      [
        "Bei all diesen Betrachtungen, die wir jetzt gepflogen haben, stand im Hintergrunde eine Frage, welche von der Gegenwart, die doch in ihren Grundansichten viel materialistischer gefärbt ist, als sie denkt, eben im Lichte des Materialismus angesehen wird.",
        "Diese Frage bezieht sich auf das Hervorgehen gewisser geschichtlicher Ereignisse.",
        "Man spricht von geschichtlicher Notwendigkeit, man spricht davon, daß dasjenige, was also zum Beispiel in diesem Jahre geschieht, geschichtlich in einer ge­wissen Weise die Wirkung sei von dem, was in vorangehenden Jahren geschehen ist."
      ],
      [
        "Was ich hier als geschichtlich bezeichne, erstreckt sich selbstver­ständlich über alle Glieder des Geschehens, das aus dem menschlichen Handeln hervorgeht, also über das Soziale, das Moralische, das sonstige Kulturleben.",
        "Die materialistische Anschauung, die ja nicht bloß darin besteht, daß man auf dem Gebiete der Naturwissenschaft geistige Er­scheinungen aus materiellen Grundlagen herleitet, sondern die noch in mancherlei anderem besteht, diese materialistische Anschauung möchte den Begriff der Freiheit eigentlich am liebsten ganz ausschalten.",
        "Und so möchte sie denn dasjenige, was im Laufe der Geschichte sich voll­zieht, auch so auffassen, wie sie gewohnt worden ist, Naturwissen­schaftliches anzuschauen, daß immer mit einer gewissen Notwendigkeit das Folgende wie eine Wirkung hervorgeht aus einer voranliegenden Ursache.",
        "Dann sagt man, indem man vielleicht glaubt, recht sachgemäß zu denken: Nun, irgendein Ereignis - auch ein solches Ereignis wie das, was jetzt so furchtbar katastrophal in unser Weltgeschehen herein­gebrochen ist - sei eben eine Notwendigkeit."
      ],
      [
        "In diesem Sinne, das heißt mit dem Begriff «naturwissenschaftliche Notwendigkeit», ist die Anschauung eine völlig unsinnige, wenn auch derAusdruck: irgendein Ereignis sei eine Notwendigkeit-, nach anderer Richtung hin seinen guten Sinn hat.",
        "Wenn Sie bedenken, was gestern wiederum vor unsere Seele getreten ist, die Kompliziertheit der mensch­lichen Natur, dann werden Sie auch gefühlsmäßig, nicht nur verstandesmäßig,"
      ],
      [
        "einen Einblick gewinnen in die Tiefe der Weltenordnung überhaupt und werden allmählich sich abgewöhnen zu glauben, daß mit den abstrakten naturwissenschaftlichen Gesetzesvorstellungen ir­gendwie diese Wirklichkeit zu umfassen ist."
      ],
      [
        "Ihr Blick wird sich dann auch auf gewisse Naturerscheinungen lenken, die, wenn man sie nur im rechten Lichte betrachten würde, den Menschen mancherlei lehren könnten, auf Naturerscheinungen, wie etwa die folgende.",
        "Im Meere entwickelt sich alljährlich eine große An­zahl von Lebenskeimen, die nicht zu Lebewesen werden."
      ],
      [
        "Lebenskeime werden abgelegt und gehen zugrunde.",
        "Nur ein kleiner Teil davon wird zu wirklichen Lebewesen.",
        "Das geschieht nun natürlich nicht bloß im weiten Meere, das geschieht in der ganzen Natur überhaupt."
      ],
      [
        "Lenken Sie nur den Blick darauf, wieviel eigentlich, wenn Sie nur ein Jahr betrachten, zum Leben vorbestimmt ist, indem die Lebenskeime, die Eier, in ihrer ersten Anlage abgelegt werden und nicht zur Entwicke­lung kommen.",
        "Wieviel zum Leben vorbestimmt ist, das nicht Leben wird!"
      ],
      [
        "Müssen wir da nicht sagen: Alle diese Lebenskeime enthalten Ur­sachen, aus denen nicht Wirkungen werden? - In der Tat, wer die Natur nicht nach vorgefaßten theoretischen Meinungen betrachtet, namentlich nicht nach der allerbestimmtesten theoretischen Meinung: Alle Ursache hat ihre Wirkung und alle Wirkung hat ihre Ursache -wer die Natur unbefangen betrachtet, der wird finden, daß es Zahl­loses in der Natur gibt, was bezeichnet werden muß in vollem Sinne des Wortes als Ursache, ohne daß daraus eine Wirkung wird in dem Sinne, wie sie es werden müßte, wenn die Ursache sich völlig ausleben würde.",
        "Wir sehen gleichsam an unzähligen Punkten immer wieder und wiederum das Leben gewissermaßen aufgehalten, nicht zu seinem Ziele gelangt."
      ],
      [
        "Das ist etwas, was wir draußen in der materiellen Natur sehen kön­nen.",
        "Wenn nun der Geistesforscher sich frägt: Wie ist es entsprechend in der geistigen Welt? - da kommt er auf sehr Merkwürdiges.",
        "Er kommt auf etwas, was in einem gewissen Sinne genau entspricht dem Stehenbleiben des Lebens in der Natur, aber eben so, wie Geistiges Natürlichem entspricht.",
        "Und wir wissen aus zahllosen Betrachtungen, daß in sehr vielen Fragen, nicht in allen, das Geistige gerade dadurch"
      ],
      [
        "zu charakterisieren ist, daß es in seinen Eigenschaften entgegengesetzt dem Natürlichen ist, gerade entgegengesetzt.",
        "So wie wir in den Fällen, von denen ich gesprochen habe, Naturursachen haben, die nicht zu ihren Wirkungen kommen, wo wir also gleichsam sehen: hier bricht der Prozeß ab und bricht dasjenige ab, was in ihm, wie man sagt, ver­anlagt ist und nicht zur Ausbildung gelangt - obwohl das Wort «ver­anlagt» wiederum zu den schlechtesten Worten gehört, die da sind, um die Wirklichkeit zu verstehen -, so sehen wir umgekehrt als Geistes-forscher in der geistigen Welt Wirkungen auftauchen, Wirkungen ent­stehen, von denen ebensowenig gesagt werden kann, da sind Ursachen, wie von den eben charakterisierten Ursachen gesagt werden kann, da sind Wirkungen."
      ],
      [
        "Fragen wir jetzt einmal im Konkreten: Was gibt sich denn den Blicken des Geistesforschers kund, wenn er das Seelenauge auf solche aufgehaltene Lebensvorgänge richtet wie die charakterisierten?",
        "Das physische Auge sieht, daß da einfach Keimanlagen zugrunde gehen; aber das geistige, das Seelenauge sieht, daß da, wo solche Keimanlagen -scheinbar nur - zugrunde gehen, Wesenhaftes entsteht auf einer frü­heren Stufe, auf einer noch nicht materiellen Stufe.",
        "Würde der Mensch verfolgen wollen, was in einem solchen Falle, wo gewissermaßen ma­terielle Ursachen keine Wirkungen haben, wirklich geschieht, dann müßte er, wenn ich den Ausdruck gebrauchen darf, kosmisch träumen.",
        "Der Mensch kann im gewöhnlichen Bewußtsein nur egoistisch träumen.",
        "Wenn er in der Nacht träumt, so träumt er in Gebundenheit an seinen eigenen Organismus; er ist im Traume nicht verbunden mit der Um­gebung.",
        "Kann er verbunden sein mit der Umgebung und dieselben Kräfte entwickeln, die er sonst im Traume entwickelt, so ist er eben im imaginativen Vorstellen."
      ],
      [
        "Was da aufgehalten wird im Naturprozeß, was nicht zu physischen Lebewesen wird, das wird zu etwas, was nun der imaginativen Vor­stellung sehr wohl zum Bewußtsein kommen kann.",
        "Wesen entstehen aus solchen aufgehaltenen Lebenskeimen, die nur den imaginativen Vorstellungen zugänglich sind, Wesen, von denen man träumen könnte, wenn man nicht als Mensch träumte, sondern als ein Wesen aus der Hierarchie der Angeloi träumte.",
        "Die Angeloi träumen in der Tat, wenn"
      ],
      [
        "ich den Ausdruck gebrauchen darf, von jenen Wesen, die alljährlich zahlreich aufsteigen als elementarische Gestaltungen aus dem Meere, aus der Erde, die nichts anderes sind als Produkte der scheinbar zu­grunde gegangenen Lebenskeime."
      ],
      [
        "Wenn Sie sich den Gedanken recht lebendig machen, da sehen Sie aus der Erde aufsteigen wie einen geistigen Duft elementarisches Leben, in das wir eingebettet sind, in dem wir drinnenstehen mit unserer Seele.",
        "Aber wir stehen in einer viel intensiveren Weise noch in diesem elemen­tarischen Leben drinnen, denn wir sind beteiligt an dem Prozesse, von dem ich gesprochen habe."
      ],
      [
        "Wir sind gar sehr als Menschen daran be­teiligt.",
        "Und die Tiere sind auch daran beteiligt.",
        "Wieso?",
        "Nun, es ist gar keine Verschiedenheit zwischen dem, was da geschieht, wenn im Meere so und so viel Fischeier abgelegt werden, die nicht Fische werden, son­dern die nur zu einem elementarischen Dasein die Veranlassung geben, und dem, was dann geschieht, wenn wir auf einem Felde aus der Erde die Saat herauswachsen sehen, sagen wir die Weizensaat."
      ],
      [
        "Wie viele Weizenkörner wachsen da heraus, die alle als Ursachen vorbestimmt sind, selbst wiederum Weizenhalme zu bilden, und die es nicht werden, weil wir sie essen!",
        "Da sind wir es selbst in unserem in derWelt stehenden Prozesse, welche sich verbinden mit dem, was da als elementarisches Dasein sich entwickelt."
      ],
      [
        "Wir halten auch in den Weizenkörnern und in den andern Produkten, aus denen wir unser Leben nähren, den fort­laufenden, den fortgehenden Prozeß auf.",
        "Wir lassen nicht wirkliche Wesen daraus werden, sondern wir bewirken durch unser eigenes Da­sein die Verwandlung desjenigen, was zu ganz anderem bestimmt ist, in elementarischen Prozessen, die nur durch Imaginationen erreichbar sind."
      ],
      [
        "Aber diese Wirklichkeit, die diesem imaginativen Leben zugrunde liegt, spielt sich dadurch ab, daß wir selbst hineingestellt sind in den Prozeß, daß wir daran teilnehmen.",
        "Aus den Weizenkörnern, aus den Roggenkörnern, aus allem übrigen, was wir in dieser Weise aus der Natur genießen, aus alledem entwickelt sich elementarisches Leben, und dieses elementarische Leben zieht durch uns."
      ],
      [
        "Dieses elementarische Leben nehmen wir auf, in diesem elementarischen Leben stehen wir drinnen."
      ],
      [
        "Da sehen Sie auf den Grund eines elementarischen Lebens.",
        "Da sehen"
      ],
      [
        "Sie, wie wir gewissermaßen nur dadurch in der Welt da sein können, daß wir einen andern fortgehenden Prozeß aufhalten und ihn zur Ver­geistigung bringen.",
        "Auch wenn wir essen, bringen wir einen Prozeß, der sonst rein materiell zu verlaufen bestimmt ist, zur Vergeistigung."
      ],
      [
        "Das Umgekehrte ist in der geistigen Welt vorhanden.",
        "Da ist die Sache so, daß nun Wirkungen da sind, welche nicht in demselben Sinne Ursachen haben wie die Bewegungen einer Billardkugel, die durch eine andere gestoßen wird, sondern welche gewissermaßen auftreten, ohne daß anzugeben ist: dies oder jenes ist ihre Ursache.",
        "Der Begriff von Ursache und Wirkung verliert eben, wenn wir den Blick auf solche Dinge wenden, seinen Sinn.",
        "In unser seelisch-geistiges Leben treten Wir­kungen herein, Wirkungen aus der geistigen Welt, von denen nicht ge­sagt werden kann, daß sie verursacht seien.",
        "So wie wir nun den elemen­tarischen Wirkungen, die gewissermaßen als Duft aufsteigen aus den geschilderten Prozessen, mit Begierde gegenüberstehen, mit jener Be­gierde, die aus unserer Lebensnotwendigkeit entspringt: wir wollen uns nähren, daher sind wir angewiesen, in jene elementarischen Prozesse, die geschildert worden sind, uns einzuspinnen -, so wie wir diesen Pro­zessen mit einer gewissen Begierde gegenüberstehen, so stehen wir, inso­fern wir Menschen des physischen Planes sind, eigentlich den geistigen Wirkungen, die in gewissem Sinne ursachenlos sind, mit Abneigung, mit Antipathie gegenüber.",
        "Wir haben das Bestreben, solche Wirkungen, die aus dem Geistigen kommen, insofern wir physische Menschen sind, nicht in uns hereinkommen zu lassen."
      ],
      [
        "Fassen Sie diesen etwas subtilen Gedanken, dann werden Sie sehen: Wir sind gewissermaßen von einem geistigen Wollen umgeben, das in uns herein will, das in uns herein strebt, und dem wir zunächst nicht mit Begierde gegenüberstehen, das wir zunächst gar nicht die Geneigt­heit haben, ohne weiteres in uns aufzunehmen.",
        "Es ist, wie wenn in der Luft um uns herum fortwährend Willensregungen schwebten, denen gegenüber wir uns abweisend verhalten.",
        "Das ist auch etwas, worauf das hellseherische Bewußtsein bald führt, wenn es zur Entwickelung ge­langt ist: die Einsicht, wie gewissermaßen Bildhaftes in unserer Um­gebung wandelt, wallt, und wie wir innere Widerstände haben, dieses Bildhafte in uns aufzunehmen."
      ],
      [
        "Betrachten wir dieses Bildhafte als eine Wirklichkeit.",
        "So wahr jedes Jahr auf der Erde so und so viele Lebenskeime zugrunde gehen, so wahr lebt in der Welt, die uns als geistige Welt immer umgibt, Geistig-Bild­haftes, durch Imagination auch zu Erreichendes, dem wir aber durch unsere Menschenanlage leicht Widerstand entgegensetzen."
      ],
      [
        "Die Widerstände sind nun nicht in Abstraktheit bloß allgemein zu fassen, sondern diese Widerstände sind konkret differenziert zu fassen.",
        "Was sich im physischen Leben wie aufsteigendes elementarisches Leben jedes Jahr entwickelt, das entwickelt sich in andern Zeitperioden, geistig herabsteigend, zu einem solchen, das wir ablehnen - in andern Zeiträumen eben, und zwar nicht in ganz regelmäßigen Zeiträumen.",
        "Es gibt Zeiten, in denen gewissermaßen das geistige Leben vehement uns umspielt und vieles an uns heran will.",
        "Andere Zeiten gibt es, in denen gewissermaßen die Geistesluft um uns herum ärmer ist.",
        "Der Mensch kann sich nun mehr oder weniger empfangend verhalten, ob­wohl er im allgemeinen Abneigung hat, diese durch Imaginationen erreichbare bildhafte Wesenheit in sich aufzunehmen.",
        "Er kann sich aber doch empfänglich durch irgendwelche Vorbedingungen verhalten, von denen wir noch zu sprechen haben werden, oder er kann sich ganz ablehnend verhalten."
      ],
      [
        "Nehmen wir an, es wäre in irgendeinem Zeitalter, ich möchte sagen, ein besonderer Andrang von solchen Wesenheiten, von Wesenheiten, die gewissermaßen geistig an den Menschen heran wollen, und der Mensch wäre abgeneigt, diese Wesenhaftigkeit in sich aufzunehmen.",
        "Was wird geschehen?",
        "Dann wird das geschehen, daß der Mensch, da-durch daß er ablehnt, solches ihm zukommendes Geistig-Wesenhaftes aufzunehmen, in sich selbst die Gelegenheit schafft - die Menschheit also in sich selbst die Gelegenheit schafft -, daß das Alte, das dürr ge­worden ist, trocken geworden ist, sich fortspinnt und, statt zu leben-diger Wirkung zu kommen, eine tote Wirkung hervorbringt: geradeso wie wenn eine Pflanze, die ihre Lebenszeit absolviert hat, nicht weg-geschafft würde, sondern als verholzte Pflanze trocken und ausgedörrt noch weiter zum Schaden der Umgebung bestehen würde."
      ],
      [
        "Im geschichtlichen Werden nimmt sich das in der folgenden Weise aus: Wenn ein Zeitalter kommt - und ein solches Zeitalter war im wesentlichen"
      ],
      [
        "der Beginn des 20.",
        "Jahrhunderts -, wo Geistig-Wesenhaftes gewissermaßen wartet, um an den Menschen heranzukommen, wo für den Menschen alle Aufforderung dazu besteht, die Seele zu öffnen für neue Offenbarungen und der Mensch diese Offenbarungen nicht auf­nehmen will, abgeneigt ist für solche Offenbarungen, dann spinnt sich das Alte in ungehöriger Weise fort.",
        "Denn dieses Alte braucht Neu-befruchtung auf dem Umwege durch den Menschen.",
        "Die wird nicht vollzogen.",
        "Unbefruchtetes spinnt sich dürr, trocken fort, und dann entstehen solche Ereignisse, wie das gegenwärtige katastrophale Ereig­nis ist."
      ],
      [
        "Unter den mancherlei Ursachen, die man in der geistigen Welt fin­den kann, ist diese geradezu eine der hauptsächlichsten, daß die Ent­wickelung gegen das 20.",
        "Jahrhundert zu so gegangen ist, daß die Men­schen sich gesträubt haben - aus Ursachen, die wir noch besprechen werden - gegen neue Offenbarung.",
        "Man könnte sagen: Die geistige Welt war voll von dem, was sich der Menschheit anbot an neuen gei­stigen Erkenntnissen, an neuen geistigen Impulsen, und die Menschheit hat es zurückgewiesen.",
        "Aus welchem Grunde?",
        "Gewiß, solche Dinge hängen auch mit Entwickelungsbedingungen der Menschheit zusam­men.",
        "Wir wissen ja, es mußte die materialistische Zeit kommen, denn sie hat nach gewissen andern Seiten hin ihre guten Eigenschaften.",
        "Also diese materialistische Zeit kam, und eine Folge dieser materialistischen Zeit war die, daß die Mcnschen Begriffe ausbildeten, welche nur auf einen Teil der Menschennatur sich beziehen."
      ],
      [
        "Denken Sie an dasjenige, was wir gestern besprochen haben.",
        "Wir haben gestern besprochen, daß dieser viergliedrige Mensch, der, im groben Sinne genommen, aus dem physischen, dem Äther- oder Bilde­kräfteleib, dem astralischen Leib und dem Ich besteht, eigentlich mit Bezug auf alle diese Teile, diese Glieder verschiedenes Alter hat.",
        "Wenn ein Mensch achtundzwanzig Jahre alt ist, dann ist er nur in bezug auf seinen physischen Leib, sagte ich gestern, achtundzwanzig Jahre alt, mit Bezug auf den sogenannten Atherleib einundzwanzig Jahre, mit Bezug auf den astralischen Leib vierzehn Jahre, mit Bezug auf das Ich erst sieben Jahre.",
        "Sie können gut aus dem, was gestern besprochen wor­den ist, die Anschauung gewinnen: da steht ein Mensch mit achtundzwanzig"
      ],
      [
        "Lebensjahren; aber das ist im uneigentlichen Sinne gesprochen: der Mensch mit diesen achtundzwanzig Lebensjahren ist nur als phy­sischer Mensch achtundzwanzig Jahre alt.",
        "In diesem Menschen lebt zum Beispiel das Ich - wenn wir von dem andern absehen -, das lang­samer lebt, das dann noch ein Kind von sieben Jahren ist, wenn der Mensch achtundzwanzig Jahre alt ist."
      ],
      [
        "Dieses Kind von sieben Jahren, wenn der Mensch seinem physischen Leibe nach achtundzwanzig Jahre alt ist, das steht in der Tat mit ganz andern Welten in Verbindung, als diejenige Welt ist, in der naturwissenschaftliche Notwendigkeit herrscht.",
        "Aber in dem materialistischen Zeitalter haben die Menschen sich gewöhnt, nur diejenigen Begriffe sich zu bilden, welche anwendbar sind auf das Verhältnis des physischen Leibes des Menschen zu der phy­sischen Umgebung, und nach diesem wird alles beurteilt."
      ],
      [
        "Der Mensch ist als wirklicher Mensch, wie er drinnensteht in der Welt, eine kompli­zierte Wesenheit, so kompliziert, wie wir das gestern wieder besprochen haben und von vielen Betrachtungen her kennen.",
        "Was der Mensch über sich zu wissen glaubt, was er von sich aussagt, das ist für unser materia­listisches Zeitalter eigentlich nur ein Viertel von dem, was sich auf den Menschen bezieht, nur dasjenige, was sich auf den physischen Leib be­zieht."
      ],
      [
        "Nur für dieses Verhältnis des physischen Leibes zur Umgebung kann man von naturwissenschaftlicher Notwendigkeit sprechen.",
        "Wo­von muß man sprechen, wenn wir von dem übrigen wieder absehen, in bezug auf das, was zum Beispiel in dem achtundzwanzigjährigen Menschen noch ein siebenjähriges Kind ist?"
      ],
      [
        "Da muß man von etwas ganz anderem sprechen, von dem diese unendlich aufgeklärte Gegen-wart, diese unendlich gescheite Gegenwart sich ganz abgewendet hat.",
        "Da muß man sprechen, so sonderbar das den Menschen der Gegenwart klingt, von dem Wunder."
      ],
      [
        "Wunder in dem Sinne, wie vielfach Menschen sich Wunder vorstel­len, Wunder, wie sich auch diejenigen Menschen vorstellen, die gern in spiritistische Sitzungen gehen, das sind Dinge, von denen die wahre Geisteswissenschaft nicht sprechen kann.",
        "Wunder liegen auf ganz an­dern Gebieten.",
        "Wunder liegen im geistigen Geschehen.",
        "Denn wie im äußeren, natürlichen Geschehen Notwendigkeit liegt, so liegen die Wunder auf dem Felde des geistigen Geschehens.",
        "Kein Mensch, der hereintritt"
      ],
      [
        "aus der geistigen Welt in die physische Welt, der zur physischen Verkörperung schreitet, ist eine physische Notwendigkeit.",
        "Eine Not­wendigkeit ist er, weil er diese Notwendigkeit sich selbst setzt, weil er aus der geistigen Welt heraus den überbewußten Beschluß faßt, sich mit irgendeiner Vererbungsströmung zu verbinden.",
        "Bei Vater und Mut­ter braucht nicht die Ursache zu liegen, liegt nur die Gelegenheit.",
        "Jedes Menschen Auftreten in der physischen Welt ist ein Wunder.",
        "Daß dies hereintritt in die physische Welt, was in unserem achtundzwanzigsten Jahre erst sieben Jahre alt ist, das ist immer ein wirkliches Wunder, gegenüber dem jedes Fragen in naturwissenschaftlicher Weise nach der Ursache ein ganz gewöhnlicher Unsinn ist.",
        "Dasjenige, was so langsam in uns lebt, daß es im achtundzwanzigsten Jahre erst sieben Jahre alt ist, aus der Vererbung herzuleiten, das ist ein Unding.",
        "Wollen wir wirk­lich eine Herleitung vornehmen, wollen wir fragen: Woraus stammt das, was da im achtundzwanzigsten Jahre erst sieben Jahre alt ist? - so kommen wir zurück in die geistige Welt, in jene Welt, die wir mit den sogenannten Toten gemeinschaftlich haben, in jene Welt, die wir mit­bevölkert haben, bevor wir herabgestiegen sind zu unserem Körper.",
        "Geister, welche unbefangen denken konnten, vermochten sich schon Begriffe von solchen Sachen zu verschaffen, wenn auch in unserem materialistischen Zeitalter nur auf schwierige Weise."
      ],
      [
        "Bedenken Sie, wieviel Goethe sich befaßt hat mit naturwissenschaft­lichen Vorstellungen, wie er es geradezu zu musterhaft naturwissen­schaftlichen Vorstellungen gebracht hat!",
        "In ihm lebte, wie Sie wissen, die fortdauernde Sehnsucht nach Italien, bevor er nach Italien ge­kommen ist.",
        "Und als er in Italien die großen Kunstwerke, die ihm eine Vorstellung von der griechischen künstlerischen Schöpfertätigkeit ge­geben haben, gesehen hat, schrieb er an seine Freunde in Weimar: «Da ist die Notwendigkeit, da ist Gott.» Er sprach von einer andern Not­wendigkeit, als die ist, von der die bloße Naturwissenschaft spricht.",
        "Von dieser Notwendigkeit hätte er gerade nach seinen naturwissen­schaftlichen Vorstellungen früher schon eine Empfindung haben kön­nen; die Notwendigkeit, die hereinleuchtete aus der geistigen Welt und die identisch ist mit dem Wunder, die empfand er, als er in Italien der griechischen Kunstwerke ansichtig wurde."
      ],
      [
        "Aber unsere Zeit ist aufgeklärt, die Menschen unserer Zeit sind sehr gescheit.",
        "Daher haben sie nicht nur den unberechtigten Wunderbegriff abgelehnt, sondern das Wunder überhaupt als solches auch aus der geistigen Welt verbannt.",
        "Aber das Wunder aus der geistigen Welt ver­bannen, das heißt nichts anderes, als alles das zu tun, um diese geistige Welt überhaupt nicht verstehen zu können.",
        "Denn aus der geistigen Welt treten die Dinge so heraus, daß wir nur Wirkungen sehen; wenn wir die Ursache suchen, so können wir sie nicht finden.",
        "Gerade dann, wenn man Geistesforscher ist, drängt sich einem das als eine unbedingte Wahrheit auf.",
        "Und weil die Gefühllosigkeit der Menschheit am Ende des 19.Jahrhunderts für die Verwunderung, für die Ehrfurcht des­jenigen, was sich aus der Welt heraus offenbaren will, bis zu einem ge­wissen hohen Grade gestiegen war, so war eine Abneigung gegen die Offenbarung vorhanden.",
        "Denn in demselben Sinne, in dem sich die Ehrfurcht entwickelt gegenüber allem, was Welttiefe ist, in demselben Maße kommen diese Offenbarungen auch an den Menschen heran."
      ],
      [
        "Dasjenige, was als Wunderwirkung eintreten kann in die Welten-ordnung, das kann auch ausbleiben, das kann auch weg sein.",
        "Mit dieser Abstumpfung der Menschheit für das Wunder hängt das zusammen, was in dem Zeitalter, das gegen das 20.",
        "Jahrhundert heranrückte, unter­lassen worden ist.",
        "Und wenn man von Ursachen sprechen will zu un­seren katastrophalen Ereignissen, dann sind diese Ursachen nicht solche, welche die Menschen geschaffen haben, sondern es sind diese Ursachen Unterlassungssünden.",
        "Das ist das Wesentliche, worauf es ankommt."
      ],
      [
        "Ich habe in früheren Jahren in einem Vortrage, den ich öfter gehal­ten habe, aufmerksam gemacht, wie in der Mitte des 19.",
        "Jahrhunderts ein ausgezeichneter Philosoph gelebt hat: Karl Christian Planck.",
        "Ich habe an vielen Orten Gelegenheit genommen, auf diesen Karl Christian Planck hinzuweisen, aus dem Grunde, weil er eine Schrift geschrieben hat, die er gewissermaßen als sein philosophisch-literarisches Testa­ment hinterlassen hat.",
        "Und in dieser Schrift ist bis in große Einzel­heiten, auch bis in geistige Einzelheiten die gegenwärtige Weltkata­strophe, man kann nicht einmal sagen, angedeutet, sondern im vor­hinein geschildert.",
        "Das Buch war 1880 geschrieben.",
        "Warum konnte er das?",
        "Weil Planck eben zu denjenigen Geistern gehörte, die zur richtigen"
      ],
      [
        "Zeit sahen, was geschieht.",
        "Wenn Sie irgendein Haus haben, das bau­fällig ist, so muß es zur rechten Zeit ausgebessert werden.",
        "Warten Sie, bis es nicht mehr ausgebessert werden kann, so fällt es zusammen, und es kommt die Katastrophe."
      ],
      [
        "Und unsere jetzige Katastrophe ist nichts anderes als ein Zusammenfallen.",
        "In Wirklichkeit betrachtet, ist es ein Zusammenfallen.",
        "Für das, was hätte geschehen sollen, waren die sieb­ziger, achtziger Jahre des vorigen Jahrhunderts die richtige Zeit."
      ],
      [
        "Solche Geister wie Karl Christian Planck, die hingewiesen haben auf das, was da kommen muß, die sind ja bekanntlich niemals geeignet, im äußeren Leben führende Persönlichkeiten zu werden!",
        "Wenn es sich irgendwo darum handelt, zu einer führenden Persönlichkeit zu greifen, einen Staatsmann zu finden oder dergleichen, da greift man selbstverständ­lich nicht zu denjenigen, die im Sinne von Karl Christian Planck etwas wissen - die kann man doch nicht nehmen, nicht wahr -, sondern man greift zu andern, die sehr oft nicht die Möglichkeit finden, das bau­fällige Haus zu stützen."
      ],
      [
        "Aber man kann heute den historischen Nach­weis liefern, wenn man nur in die Hintergründe des Lebens sieht - und Karl Christian Planck ist nicht der einzige, es gibt manche andere -, daß zur rechten Zeit manchen Leuten aus der geistigen Welt die Offen­barung gekommen ist, welchem Ereignisse die Menschheit entgegengeht.",
        "Damals wäre auch noch die Zeit gewesen, diesem Ereignisse einen an­dern Lauf zu geben."
      ],
      [
        "Natürlich wurde Karl Christian Planck nicht gehört."
      ],
      [
        "Aber werden denn jetzt die Menschen gehört, die von dem reden, was eben, wenn es wirksam sein soll, Jahre vor dem ausgesprochen wer­den muß, bevor der Zusammenbruch eintritt?",
        "Man muß leider sagen:"
      ],
      [
        "Die Art und Weise, wie die Menschheit dieses katastrophale Ereignis bis jetzt durchlebt, läßt deutlich erkennen, daß, wenn dieses katastro­phale Ereignis noch vier Jahre andauert, die Menschen sich daran ge­wöhnt haben werden und es hinnehmen werden - nun, wie eben das normale Leben; denn bis zu einem hohen Grade ist diese Gewöhnung schon fortgeschritten.",
        "Wer aber die Zeichen der Zeit versteht, der frägt heute: Was muß geschehen? - weil, wenn etwas nicht geschieht, nach Jahrzehnten dasjenige sich zeigt, was da kommen muß, weil etwas nicht zur rechten Zeit geschehen ist."
      ],
      [
        "Aber aus der umliegenden physischen Welt heraus kann das nicht gefunden werden, was nach den heutigen Zeitbedingungen geschehen soll.",
        "Heute muß man schon, wenn man das Richtige hören will, die­jenigen hören, die aus der geistigen Welt heraus sprechen können.",
        "Natürlich, für unbedeutendere Dinge vollziehen sich die Dinge rascher.",
        "Man kann sagen: In fünf Jahren werden vielleicht die Menschen ein­sehen, daß sie auf manches hätten hören sollen, was sie heute schon hätten wissen können, wenn sie hingehört hätten.",
        "Doch sie sind nicht geneigt, diese Dinge zu hören, weil sie nur geneigt sind, auf das zu hören, wofür sich schon die Anzeichen in der äußeren physischen Welt zeigen.",
        "Aber die physische Welt ist für das geschichtliche Werden un­bedeutend.",
        "Sie zeigt nicht dasjenige, was Anstoß, Impuls sein soll zum Geschehen.",
        "Was Anstoß, Impuls sein soll zum Geschehen im sozialen, im sittlichen Leben, das muß aus der geistigen Welt stammen."
      ],
      [
        "Nun, für ein größtes Ereignis im Verlaufe der Menschheitsentwicke­lung soll gerade die Menschheit in unserem Zeitalter erzogen werden: an Freiheit auch in der historischen Entwickelung zu glauben.",
        "An einem bestimmten Punkte des geistigen Lebens soll die Menschheit der Gegen­wart mit aller Gewalt darauf gestoßen werden, an Freiheit - und iden­tisch damit ist dann das Wunder - zu glauben.",
        "Und dieser Punkt ist in der Auffassung des Christus-Impulses, in der Auffassung des Myste­riums von Golgatha gelegen.",
        "Wie die Menschheit zum Mysterium von Golgatha stand, das war ganz anders in früheren Zeiten und war immer mehr anders, je weiter wir zurückgehen in der geschichtlichen Ent­wickelung.",
        "Wir haben öfters davon gesprochen.",
        "Heute gibt es nicht in den Menschen - gerade nicht in den im Sinne des Zeitgeistes fortge­schrittensten Menschen - die Möglichkeit, das Ereignis von Golgatha als historisches Ereignis wie andere historische Ereignisse hinzustellen.",
        "Ich brauche für Sie das, was hier als Voraussetzung in Betracht kommt, nur anzudeuten: Sie wissen, die Evangelien sind als historische Doku­mente in ihrer Bedeutung erschüttert.",
        "Nicht in demselben Sinne, wie wir die Dokumente über Sokrates oder Plato oder über Alkibiades oder Cäsar als historische Dokumente nehmen, können wir nach dem, wie heute geschichtlich geforscht wird, die Evangelien als Dokumente an­sehen, ebensowenig die andern Dokumente, die im Neuen Testament"
      ],
      [
        "über das Ereignis von Golgatha vereinigt sind.",
        "So wie der Mensch heute über geschichtliches Forschen denkt, so entzieht sich diesem geschicht­lichen Forschen die Möglichkeit, die Evangelien als historische Doku­mente zu betrachten und aus den Evangelien das Ereignis von Golgatha als ein historisches anzusehen, als ein historisch beweisbares, meine ich, als ein in dem Sinne historisch beweisbares, wie man andere historische Geschehnisse und Tatsachen geschichtlich belegt und geschichtlich be­weist.",
        "Man kann nicht in demselben Sinne über den Christus Jesus als eine historische Persönlichkeit sprechen, wie man über Karl den Großen nach dem, was man heute historische Quellen nennt, als eine historische Persönlichkeit sprechen kann."
      ],
      [
        "Für den, der die Dinge durchschaut, ist heute der Zeitpunkt heran­gekommen, wo der aufrichtige, Wahrheit-durchdringende Menschen-sinn sich sagen muß: Was man für historische Quellen hielt in bezug auf das Mysterium von Golgatha, ist durch die Gestalt, welche die Ge­schichtsforschung angenommen hat, erschüttert.",
        "Und man muß schon so etwas wie ein Stumpfling sein, wie zum Beispiel Adoll Harnack, der berühmte Theologe, um sich immer wieder und wiederum hinzu­stellen und von dem, was man, wie er sagt, auf einer Quartseite zusam­menstellen kann über den Christus Jesus, zu behaupten: darinnen seien doch historische Dokumente im Sinne der heutigen Geschichte gegeben.",
        "Es sind natürlich in diesen Dingen, die auf dieser Quartseite stehen, ebensowenig historische Dokumente gegeben, wie in den Evangelien -nach Harnack selber - historische Dokumente gegeben sind.",
        "Aber sol­ches Unterfangen wie das Harnacksche, dem hunderte und hunderte von andern gegenüberstehen, hängt eben zusammen mit der ganzen Unwahrhaftigkeit unserer Zeit in solchen Dingen, die niemals bis zu den radikalen Folgerungen gehen will, welche aber eben einfach die richtigen Folgerungen sind."
      ],
      [
        "Die Folgerung, die ja gezogen werden muß, ist diese, daß der Mensch nach dem, was vorliegt, sich heute gestehen muß: sucht er auf äußerlich historischeWeise den ChristusJesus, so kann er ihn nicht finden.",
        "Finden muß er ihn auf dem Wege der Geisteserforschung.",
        "Da findet er ihn aber sicher.",
        "Da findet er das historische Ereignis von Golgatha.",
        "Warum?",
        "Weil das historische Ereignis von Golgatha ein solches war, das durch"
      ],
      [
        "Freiheit in der Menschheitsentwickelung aufgetreten ist, durch eine Freiheit in noch viel höherem Sinne als andere historische Ereignisse, und weil dieses freie Ereignis gerade in unserem Zeitraum an den Men­schen so herantreten soll, daß nichts ihn zwingt, seine Geltung anzu­nehmen, sondern er diese Geltung aus innerer Freiheit annehmen muß.",
        "Wofür ein historischer Beweis schon da ist, für dessen Annahme ist man nicht frei.",
        "Wofür ein äußerer historischer Beweis nicht da ist, das nimmt man an aus geistigen Gründen, und auf dem geistigen Boden ist man frei.",
        "Christ wird man durch Freiheit.",
        "Und das ist gerade dasjenige, was notwendig ist dem heutigen Zeitalter zu verstehen, daß man Christ in Wirklichkeit nur sein kann aus voller Freiheit, nicht einmal ge­zwungen durch historische Dokumente.",
        "In unserem Zeitalter soll das Christentum jene Wahrheit gewinnen - das ist vorbestimmt dieser Zeit -, wodurch es zu dem großen Impuls des menschlichen Verständ­nisses für die Freiheit wird.",
        "Das gehört zu den Fundamentalwahrheiten in unserer Zeit, daß dies eingesehen wird, daß eingesehen wird, daß die Beweise für das Christentum in der geistigen Welt gesucht werden müssen."
      ],
      [
        "Wird diese Einsicht so intensiv in der menschlichen Natur, wie sie werden soll, so wird sie auch andere Einsichten erzeugen, wird manches andere noch hervorbringen.",
        "Was sie zunächst hervorbringen sollte, das ist, daß der Mensch überhaupt lerne, sich die Frage zu beantworten:"
      ],
      [
        "Wie mache ich mich empfänglicher für das, was mich nicht aus der physischen Welt heraus zwingt, es anzuerkennen, sondern wogegen ich zunächst vielleicht sogar eine Abneigung, eine Antipathie habe?",
        "Was macht mich geneigter dazu?"
      ],
      [
        "Wirklich nicht aus persönlicher Eitelkeit und Albernheit, sondern weil ich eben nur ein konkretes Exempel dabei statuieren will, muß ich bei einer solchen Gelegenheit immer wieder darauf aufmerksam machen, daß ich meine schriftstellerische Laufbahn damit begonnen habe, indem ich nicht meine Meinungen zunächst vertreten habe, son­dern alles dasjenige, was ich vertreten habe, in Anknüpfung an Goethe­schen Geist publizierte, im bewußten Zurückblicken zu einem Geiste, der schon 1832 in das geistige Reich der sogenannten Toten hinauf­gestiegen ist.",
        "Aber lesen Sie das, was ich so in Anknüpfung an Goethe"
      ],
      [
        "in den Zeiten, die meiner «Philosophie der Freiheit» vorangegangen sind, geschrieben habe!",
        "Die sogenannten Goethe-Forscher sehen es zu­meist daraufhin an, ob es Goethesche Ansichten wiedergibt.",
        "Goethesche Ansichten sind diesen Leuten dann gegeben, wenn man ein literarischer Wiederkäuer ist, das heißt, wenn man das, was Goethe in seiner Inkar­nation gesagt hat bis 1832, wiederkaut.",
        "Ich war immer der Ansicht, daß dasjenige, was Goethe gesagt hat, wirklich nicht von dem oder jenem Schulmeister und auch nicht von mir wiedergesagt zu werden braucht, denn Goethe hat, was er hat sagen wollen, schon selber besser gesagt.",
        "Es ist immer besser, wenn die Goetheschen Werke gelesen wer­den, als die Ansichten der Schulmeister, und wären es selbst so aus­gezeichnete Schulmeister und Magister, wie zum Beispiel Lewes mit seiner berühmten Goethe-Biographie ist.Was ich versuchte zu schreiben, ist dasjenige, was auf der Inspiration des nicht mehr auf der Erde weilenden Goethe beruhte: die Fortbildung seiner Ansichten auf einem gewissen Gebiete nach seinem Tode, was geschrieben werden konnte aus einem gewissen Gefühl lebendiger Verbindung mit sogenannten verstorbenen Seelen."
      ],
      [
        "Ich erwähne dies als ein Exempel, wirklich nicht aus alberner Eitel­keit, sondern weil es zusammenhängt mit der Frage: Was sollen die Menschen tun, um sich empfänglicher zu machen für dasjenige, was aus der geistigen Welt heraus kommt?",
        "Verbinden müssen sich die Men­schen mit den Toten.",
        "Den Weg müssen sie finden in diejenigen Welten, worinnen die Toten leben, aber in einer vernünftigen, verständigen Weise, in einer wirklich entsprechenden Weise, nicht nach spiritistischer Weise.",
        "Die Toten reden weiter nach ihrem Tode.",
        "Und das, was sie reden, was sie impulsieren, es lebt, wie wir gesehen haben, zwar nicht in unseren Sinneserfahrungen, nicht in unserem Vorstellen, wohl aber in unserem Gefühl und in der Realität unserer Willensimpulse.",
        "Da lebt es drinnen."
      ],
      [
        "Dann müssen wir aber auch das in uns finden, was uns geneigt macht, an die geistige Welt überhaupt heranzutreten.",
        "Mit dem Un­glauben an ein Herantreten an die geistige Welt ist verbunden die Anti­pathie gegen die Imaginationen, die herein wollen aus der geistigen Welt, die unser Handeln auch im sozialen Menschengeschehen, im moralischen,"
      ],
      [
        "im ethischen Menschengeschehen impulsieren wollen, und die doch einzig und allein den Menschen frei machen können."
      ],
      [
        "Zwei Dinge sind in unserer Zeit notwendig: einzusehen, daß das Bekenntnis zum Mysterium von Golgatha eine freie Tat der mensch­lichen Seele sein muß und dieses ganz zu durchdringen.",
        "Und auf der andern Seite: real, nicht bloß abstrakt, nicht bloß in einem abstrakten Glauben, sondern real die Brücke zu suchen zu den Toten.",
        "Auch gegen das letztere spricht viel in unserer Zeit.",
        "Die Menschen sehen nicht gleich ganz ein, was alles dagegen spricht.",
        "Was stellen sich die Menschen heute für das soziale Geschehen als ein Ideal vor?",
        "Sie stellen sich vor: Wir sind gescheit, denn wir sind geboren, wir sind in die Schule gegangen, wir sind also gescheite Wesen, gescheite Menschen, daher wissen wir ohne weiteres, was im sozialen Leben zu geschehen hat.",
        "Wir bilden Ver­sammlungen, Gemeinderäte, Staatsräte, Parlamente, wie man es nennt, da bespricht man selbstverständlich dasjenige, was zu geschehen hat im sozialen Leben, denn wir sind gescheit, und wenn sich so gescheite Leute, wie es die Menschen der Gegenwart sind, zusammensetzen, so wird immer das Richtige herauskommen."
      ],
      [
        "Das ist das Ideal.",
        "Aber das geht von einer Voraussetzung aus, die nicht richtig ist.",
        "Es geht von der Voraussetzung aus, daß man ohne weiteres wisse, was das Richtige ist.",
        "Wissen Sie, was das Richtige ist?",
        "Wissen Sie, wer es weiß, was das Richtige ist im Jahre 1917?",
        "Nicht die­jenigen, die jetzt in den Zwanzigerjahren sind und sich in den Parla­menten am liebsten so zum Reden bloß zusammensetzen und darüber urteilen, was das Richtige sei für 1917, sondern das wissen die am besten, die längst gestorben sind!",
        "Bei denen sollte man fragen, wie man sich zu verhalten hat!",
        "Hier liegt ein gut Teil von dem, was die Frage beantwortet: Wie kann unser soziales Leben aufgebessert werden? -Wenn wir lernen, die Toten zu befragen."
      ],
      [
        "Bis zu seinem Lebensende weiß man in der Regel hier als physischer Mensch alles doch nur so weit, als es einem selber persönlich frommt.",
        "Recht reif wird das Wissen erst, wenn man gestorben ist.",
        "Dann wird es erst so reif, daß es richtig anwendbar ist auf das soziale Leben.",
        "Aber man darf nicht glauben, daß nun die Toten wie mit physischen Hän­den unmittelbar eingreifen sollen, so ungefähr wie Menschen, die hier"
      ],
      [
        "im physischen Leib leben.",
        "Die Toten können besser wissen als die Le­bendigen, was sozial zu geschehen hat, aber sie müssen gehört werden von den Menschen, und die ausführenden Organe müssen die hier im Physischen lebenden Menschen sein.",
        "Lernen müssen vor allen Dingen die Menschen in der Gegenwart, solche ausführenden Organe zu sein.",
        "Aber von solchen - wenn ich den Ausdruck gebrauchen darf, er ist so unangenehm - von solchen «Parlamenten», wo sich die Menschen be­streben werden, die Toten mitreden zu lassen, wird man noch lange nicht hören.",
        "Es wird jedoch auf gewissen Gebieten nicht Heil kommen, wenn man nicht die Toten wird mitreden lassen wollen, wenn nicht auch von dieser Seite her das soziale Leben spiritualisiert werden kann.",
        "Bevor man sich dem Glauben hingibt, daß die hier auf der Erde er­rungene, durch die Geburt, Welt und Schulung errungene Weisheit reif für soziale Impulse ist, sollte man sich vertiefen in das, was wirklich reif geworden ist für soziale Impulse: diejenige Weisheit, die schon den physischen Leib abgelegt hat, und die, wenn wir sie wirklich durch­forschen, uns erst bedeutsame Perspektiven eröffnet."
      ],
      [
        "Bedenken Sie, wie das Gefühlsleben vertieft wird, das ganze mensch­liche Gemüt eine Vertiefung erfährt, wenn das, was ich jetzt als Ideen ausgesprochen habe, eben Gefühl und Empfindung wird; wenn an die Stelle des alten Mythos, der den Gegenwartsmenschen verband mit den Vorfahren, dasjenige Band tritt, das ich angedeutet habe: ein konkretes geistiges Leben, das unsere geistige Atmosphäre wiederum anfüllen wird; und wenn, was so durch die Geisteswissenschaft als Ideen erfaßt werden kann, übergeht in Gemüt und Empfindung und die Menschen wahrhaftig drinnen leben wollen."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SIEBENTER VORTRAG Dornach, 17. Dezember1917",
    "paragraphs": [
      "Den Betrachtungen, die in diesen Wochen gehalten worden sind, lag verschiedenes zugrunde, das dazu führen kann, die menschliche Natur in ihrem Zusammenhang mit dem geschichtlichen Werden der Mensch­heit so zu verstehen, daß man sich allmählich eine Vorstellung bilden kann über Notwendigkeit und Freiheit. Weniger können solche Dinge entschieden werden durch Definitionen und Wortauseinandersetzungen als dadurch, daß man die entsprechenden Wahrheiten aus der geistigen Welt zusammenträgt.",
      "Die Menschheit wird sich in unserem Zeitalter immer mehr daran gewöhnen müssen, eine andere Art des Verständ­nisses der Wirklichkeit sich anzueignen, als es die heute so vielfach herr­schende und übliche ist, die sich im Grunde genommen an sehr Sekun­däres, an allerlei nebulose Vorstellungen in Anknüpfung an Wortdefi­nitionen und so weiter hält. Man hat heute, wenn man das vornimmt, was manche Leute schreiben oder sagen, die sich für ganz besonders gescheit halten, das Gefühl: sie reden in Begriffen und Vorstellungen, die nur scheinbar bestimmt, in Wirklichkeit aber so unbestimmt sind, wie wenn jemand über einen gewissen Gegenstand sprechen würde, der zum Beispiel aus einem Kürbis gemacht ist.",
      "Hat man einen Kürbis um­gestaltet zu einer Flasche und benützt ihn als Flasche, so kann man über diesen Gegenstand so reden, als ob man über einen Kürbis redet, denn ein Kürbis ist es in Wirklichkeit; aber man kann auch wie über eine Flasche reden, denn eine Flasche ist er ja auch, er wird richtig be­nützt als Flasche. Nicht wahr, die Dinge, über die man spricht, bekom­men erst ihre Valeurs in den Zusammenhängen, in denen man sich ergeht.",
      "Wenn man nicht in Anlehnung an Worte, sondern aus einer ge­wissen Anschauung heraus spricht, so wird jeder Mensch wissen, ob man eine Flasche meint oder einen Kürbis. Aber man darf sich dann nicht auf die Beschreibung des Gegenstandes oder die Definition des Gegenstandes beschränken.",
      "Denn solange man sich auf eine Beschrei­bung, auf eine Definition beschränkt, kann es ebensogut ein Kürbis oder eine Flasche sein. Und so kann heute dasjenige, worüber viele",
      "Philologen, Leute, die sich sehr gescheit dünken, reden, die Seele des Menschen sein, es kann aber auch der Leib des Menschen sein, es kann Kürbis und kann Flasche sein.",
      "Ich meine mit dieser Bemerkung sehr vieles von dem, was in der Ge­genwart sehr ernst genommen wird, zum Teil zum Unheil der Mensch­heit. Daher eben ist es notwendig, daß gerade von der anthroposophisch orientierten Geisteswissenschaft, zu der unter anderem auch klares, präzises Denken nötig ist, ausgehe ein Bestreben, nicht in einer solchen Weise, wie es heute üblich ist, die Welt anzuschauen, nicht den Kürbis mit der Flasche zu verwechseln, sondern überall auf das Reale zu sehen, sei es das äußere Physisch-Reale, sei es das Geistig-Reale.",
      "Man kann ohnedies nicht zu einer wirklichen Vorstellung über das­jenige gelangen, was für den Menschen in Betracht kommt, wenn man sich an Definitionen und dergleichen hält, sondern nur dann, wenn man die Lebenszusammenhänge in ihrer Wirklichkeit ins Auge faßt. Und gar über solch wichtige Begriffe wie Freiheit und Notwendigkeit im sozialen, im sittlichen Leben, kann man nur Klarheit gewinnen, wenn man zusammenhält solche spirituellen Tatsachen, wie sie in die­sen Betrachtungen vorgebracht worden sind und gewissermaßen ver­sucht, sie immer aneinander abzuwägen, um ein Urteil über die Wirk­lichkeit zu gewinnen.",
      "Bedenken Sie, daß ich schon in öffentlichen Vorträgen und auch hier wiederum in den verschiedensten Zusammenhängen mit einer ge­wissen Intensität immer wieder und wieder hervorgehoben habe, daß wir das, was wir Vorstellungen nennen, nur dann richtig begreifen können, wenn wir sie so in Beziehung bringen zu unserm leiblichen Organismus, daß wir den Vorstellungen im Leibe nicht etwas Wach­sendes, Gedeihendes zugrunde liegend sehen, sondern gerade umgekehrt, etwas Absterbendes, etwas partiell im Leibe Absterbendes. Ich habe das so ausgesprochen in einem öffentlichen Vortrage, daß ich gesagt habe:",
      "Der Mensch stirbt eigentlich immer in sein Nervensystem hinein ab. -Der Nervenprozeß ist ein solcher, daß er sich auf das Nervensystem beschränken muß. Denn würde er sich ausdehnen über den ganzen Or­ganismus, würde dasselbe vorgehen im ganzen Organismus, was in den Nerven vorgeht, so würde dies den Tod des Menschen in jedem Augenblick",
      "bedeuten. Man kann sagen: Vorstellungen entstehen da, wo der Organismus sich selber abbaut, wir sterben in unser Nervensystem fort­während hinein. - Dadurch ist Geisteswissenschaft in die Notwendig­keit versetzt, nicht nur diejenigen Prozesse zu verfolgen, welche die heutige Naturwissenschaft als die einzig maßgebenden betrachtet: die aufsteigenden Prozesse. Diese aufsteigenden Prozesse, sie sind Wachs­tumsprozesse, sie gipfeln noch im Unbewußten. Erst wenn der Orga­nismus mit den absteigenden Prozessen beginnt, tritt im Organismus jene Tätigkeit der Seele auf, die man als Vorstellungs-, ja auch als sinn­liche Wahrnehmungstätigkeit bezeichnen kann. Dieser Abbauprozeß, dieser Ersterbeprozeß, der muß da sein, wenn überhaupt vorgestellt werden soll.",
      "Nun habe ich gezeigt, daß das freie Handeln des Menschen geradezu darauf beruht, daß der Mensch in die Lage kommt, aus reinen Gedan­ken heraus die Impulse für sein Handeln zu suchen. Diese reinen Ge­danken werden am meisten von Einfluß sein auf die Abbauprozesse im menschlichen Organismus. Was geschieht denn eigentlich, wenn der Mensch so recht eine freie Handlung vollzieht? Machen wir uns das einmal klar, was da beim gewöhnlichen physischen Menschen geschieht, wenn der Mensch aus moralischer Phantasie heraus - Sie wissen jetzt, was ich damit meine -, aus moralischer Phantasie heraus, das heißt aus einem Denken, das von sinnlichen Impulsen, sinnlichen Trieben und Affekten nicht beherrscht ist, handelt, was geschieht da mit dem Men­schen eigentlich? Dann geschieht das, daß er sich reinen Gedanken hin­gibt; die bilden seine Impulse. Sie können ihn nicht impulsieren durch sich selbst; er muß sich impulsieren, denn sie sind bloße Spiegelbilder, das haben wir ja betont. Sie gehören der Maja an. Spiegelbilder können nicht zwingen, der Mensch muß sich selber zwingen unter dem Einfluß der reinen Vorstellungen.",
      "Worauf wirken reine Vorstellungen? Am stärksten wirken sie auf den Abbauprozeß im menschlichen Organismus. Auf der einen Seite kommt aus dem Organismus heraus der Abbauprozeß, und auf der andern Seite kommt aus dem geistigen Leben diesem Abbauprozeß ent­gegen der reine Tatgedanke. Ich meine damit den Gedanken, welcher der Tat zugrunde liegt. Durch die Vereinigung von beiden, durch das",
      "Aufeinanderwirken des Abbauprozesses und des Tatgedankens entsteht die freie Handlung.",
      "Ich sagte, der Abbauprozeß wird nicht durch das reine Denken be­wirkt; der ist sowieso da, er ist also eigentlich immer da. Wenn der Mensch diesem Abbauprozeß, gerade den bedeutsamsten Abbauprozes­sen in ihm, nichts aus dem reinen Denken heraus entgegenstellt, dann bleibt er Abbauprozeß, dann wird der Abbauprozeß nicht umgewandelt in einen Aufbauprozeß, dann bleibt ein ersterbender Teil im Menschen. Denken Sie das einmal durch, dann ersehen Sie daraus, daß die Mög­lichkeit besteht, daß der Mensch gerade durch Unterlassung von freien Handlungen einen Todesprozeß in sich nicht aufhebt. Darin liegt einer der subtilsten Gedanken, die der Mensch nötig hat, in sich aufzu­nehmen. Wer diesen Gedanken versteht, kann im Leben nicht mehr zweifeln an dem Vorhandensein der menschlichen Freiheit. Denn eine Handlung, die aus Freiheit geschieht, geschieht nicht durch etwas, was im Organismus verursacht wird, sondern wo die Ursachen aufhören, nämlich aus einem Abbauprozeß heraus. Dem Organismus muß etwas zugrunde liegen, wo die Ursachen aufhören, dann kann überhaupt erst die reine Vorstellung als Motiv des Handelns eingreifen. Aber solche Abbauprozesse sind immer da, sie bleiben nur gewissermaßen un­genützt, wenn der Mensch nicht freie Handlungen vollführt.",
      "Was hier zugrunde liegt, bezeugt aber auch, wie es mit einem Zeit­alter aussehen muß, welches sich nicht darauf einlassen will, die Idee der Freiheit im vollsten Umfange zu verstehen. Die zweite Hälfte des 19. Jahrhunderts, das 20. Jahrhundert bis in unsere Zeit, diese Epoche hat es sich geradezu zur Aufgabe gesetzt, auf allen Gebieten des Lebens die Idee der Freiheit immer mehr und mehr für die Erkenntnis zu trüben, für das praktische Leben in Wirklichkeit auszuschalten. Freiheit wollte man nicht verstehen, Freiheit wollte man nicht haben. Die Phi­losophen haben sich bemüht, zu beweisen, daß alles mit einer gewissen Notwendigkeit aus der menschlichen Natur hervorgeht. Gewiß, der menschlichen Natur liegt eine Notwendigkeit zugrunde, aber diese Notwendigkeit hört auf, indem Abbauprozesse beginnen, in welchen der Zusammenhang der Ursachen sein Ende findet. Wenn Freiheit da eingegriffen hat, wo die Notwendigkeit im Organismus aufhört, dann",
      "kann man nicht sagen, daß die Handlungen der Menschen aus der inneren Notwendigkeit hervorgehen; sie gehen dann erst aus ihm her­vor, wenn diese Notwendigkeit aufhört. Der ganze Fehler bestand darinnen, daß man sich nicht eingelassen hat darauf, im menschlichen Organismus nicht nur zu verstehen die aufbauenden Prozesse, sondern auch zu verstehen die abbauenden Prozesse. Es wäre aber allerdings nötig, daß man, um das zu erkennen, was eigentlich der menschlichen Natur zugrunde liegt, mehr Begabung entwickele, als die Gegenwart Neigung dazu hat. Wir haben gestern gesehen, daß es notwendig ist, dasjenige wirklich ins Seelenauge fassen zu können, was man als menschliches Ich bezeichnet. Aber es ist gerade in der Gegenwart wenig Talent vorhanden, diese Wirklichkeit des Ich irgendwie zu erfassen. Ich will Ihnen einen Beweis liefern.",
      "Ich habe öfter die ausgezeichnete wissenschaftliche Leistung von Theodor Ziehen erwähnt: «Die physiologische Psychologie.» Da ist auf Seite 205 auch die Rede von dem Ich. Nur kommt Ziehen niemals in die Lage, auch nur hinzudeuten auf das wirkliche Ich, sondern er redet nur von der Ich-Vorstellung. Wir wissen, die ist jedoch nur ein Spiegel­bild des wirklichen Ich. Aber interessant ist es gerade zu hören, wie ein ausgezeichneter Denker der Gegenwart, aber ein solcher, der da glaubt, mit naturwissenschaftlichen Vorstellungen alles erschöpfen zu können, über das Ich redet. Es sind Vorträge, die wiedergegeben werden, des­halb ist die Sache in Vortragsform vorgebracht. Ziehen sagt: «Es wird Ihnen vielleicht auffallen, daß die mit dem kurzen kleinen Wort Ich bezeichnete Ich-Vorstellung ein so komplexes dreigliedriges Gebilde sein soll, an welchem tausend und abertausend Teilvorstellungen be­teiligt sein sollen. Aber ich bitte Sie zu erwägen: dasWort ist zwar kurz, aber daß sein Vorstellungsinhalt dieser Komplex sein muß, geht schon daraus hervor, daß jeder von Ihnen in Verlegenheit geraten wird, wenn er den Denkinhalt seiner sogenannten Ich-Vorstellung angeben soll.»",
      "Und jetzt geht Ziehen daran, etwas zu sagen über den Denkinhalt der Ich-Vorstellungen. Nun wollen wir einmal sehen, was der ausge­zeichnete Gelehrte über dasjenige zu sagen weiß, woran man eigentlich denken soll, wenn man über sein Ich denkt: «Sie werden alsbald an Ihren Körper denken» - also an Ihren Körper denken! - «an Ihre Relationen",
      "zur Außenwelt, Ihre verwandtschaftlichen und Eigentums­beziehungen» - also man wird bald daran gehen, an seine Börse zu denken und sein Geld abzuzählen! - «Ihre Namen und Titel... »",
      "Nun, der ausgezeichnete Gelehrte weist ausdrücklich darauf hin, daß man auch an seinen Namen und an seinen Titel denken soll, wenn man sein Ich in der Vorstellung umfassen, umspannen soll.",
      "... . Ihre Hauptneigungen und dominierenden Vorstellungen und endlich an Ihre Vergangenheit, und damit selbst den Beweis führen, wie äußerst zusammengesetzt diese Ich-Vorstellung ist. Freilich redu­ziert der reflektierende Mensch diese Kompliziertheit der Ich-Vorstel­lung wieder auf eine relative Einfachheit, indem er den äußeren Objek­ten und anderen Ichs sein eigenes Ich als das Subjekt seiner Empfin­dungen, Vorstellungen und Bewegungen gegenüberstellt. Gewiß hat auch diese Gegenüberstellung und diese Vereinfachung der Ich-Vorstel­lung ihre tiefe erkenntnistheoretische Begründung, aber, rein psycho­logisch betrachtet, ist dieses einfache Ich nur eine theoretische Fiktion.»",
      "Also «dieses einfache Ich» ist nur eine «theoretische Fiktion», das heißt eine bloße Phantasievorstellung, die sich aufbaut, wenn man sei­nen Namen, seine Titel, vermutlich auch seine Orden und andere der­gleichen Dinge zusammenstellt, die einem Gewicht geben! An solchen Punkten kann man die ganze Schwäche des heutigen Denkens erkennen. Und diese Schwäche muß um so mehr ins Auge gefaßt werden, weil ja dasjenige, was sich als entscheidende Schwäche für die Erkenntnis des seelischen Lebens erweist, eine Stärke ist für die Erkenntnis der äußeren naturwissenschaftlichen Tatsachen. Gerade was untauglich ist für die Erkenntnis des seelischen Lebens, ist sehr tauglich, um die äußere sinnen-fällige Tatsache in ihrer unmittelbaren äußeren Notwendigkeit zu durchschauen.",
      "Man muß sich nicht hinwegtäuschen darüber, daß es ein Charakte­ristikon unserer Zeit ist, daß Leute, die auf einem Gebiete groß sein können, auf dem andern Gebiete Vertreter des äußersten Unsinns sind. Nur wenn man diese Tatsache, die so sehr geeignet ist, der Menschheit Sand in die Augen zu streuen, scharf ins Auge faßt, dann kann man irgendwie mitdenken bei dem, was in Betracht kommt für die Wieder-aufrichtung jener Kraft, die die Menschheit braucht, um solche Vorstellungen",
      "zu gewinnen, die fruchtbar und heilsam in das Leben ein­greifen können. Denn in dieses Leben, wie es heute ist, werden nur Vor­stellungen eingreifen, die tief aus der wahren Wirklichkeit heraus genommen sind, bei denen man sich nicht scheut, tief in die wahre Wirklichkeit hineinzugreifen. Davor aber scheuen sich gerade viele Menschen der Gegenwart.",
      "Die Menschen der Gegenwart finden sich sehr häufig geneigt, ohne erst hineingeschaut zu haben in die wahre Wirklichkeit, aus der sie ihre Impulse schöpfen sollten, die geistige Wirklichkeit zu reformieren. Wer reformiert heute nicht alles Mögliche in der Welt, das heißt, glaubt zu reformieren. Was holt man nicht alles aus dem reinen Nichts der Seele heraus! Aber in einer Zeit, wie diese ist, können nur diejenigen Dinge fruchtbar sein, welche aus der Tiefe der geistigen Wirklichkeit heraus selbst geholt sind. Dazu muß Wille vorhanden sein.",
      "Die Eitelkeit, die auf Grund des seelischen Nichts alle möglichen Reformgedanken fassen will, ist ebenso schädlich der Entwickelung in unserer heutigen Zeit wie der Materialismus selber. Ich habe gestern am Schluß darauf aufmerksam gemacht, wie das wahre Ich des Men­schen, dasjenige Ich, das allerdings der Willensnatur angehört, über das sich daher für das gewöhnliche Bewußtsein Schlaf breitet, befruchtet werden muß dadurch, daß schon durch den öffentlichen Unterricht die Menschen hingeführt werden zum konkreten Begreifen der großen Zeit-interessen. Das kann man nicht anders machen in unserer Zeit, als in­dem man klarmacht, welche geistigen Kräfte und Wirksamkeiten her-eingreifen in unser Geschehen. Nicht mit allgemeinen nebulosen Reden über den Geist ist es getan, sondern mit der Erkenntnis der konkreten geistigen Vorgänge, wie wir sie in diesen Betrachtungen geschildert haben, wo man per Jahrzahl darauf hinweist, wie da und dort diese gewissen Mächte und Kräfte aus der geistigen Welt hier in die physische hereingegriffen haben.",
      "Dadurch aber kommt das zustande, was ich bezeichnen konnte im Gesamtwerden der Menschheit als das Zusammenarbeiten der soge­nannten Toten mit den sogenannten Lebendigen. Denn im Wirklichen unseres Gefühls- und Willenslebens sind wir mit den Toten in einem Reich. Man kann ebensogut sagen, mit dem Wirklichen unseres Ich und",
      "unseres astralischen Leibes sind wir mit den Toten in einem Reich. Beides besagt dasselbe. Dadurch aber ist hingewiesen auf ein gemein­sames Gebiet, in das wir eingebettet sind, in dem die Toten und die Lebendigen zusammenarbeiten an demjenigen Gewebe, das man das soziale, das sittliche, das geschichtliche Menschenleben in seiner Ganz­heit nennen kann, wozu auch diejenigen Lebensläufe gehören, die zwischen dem Tod und einer neuen Geburt zugebracht werden.",
      "Wir haben darauf hingewiesen in diesen Betrachtungen, wie der so­genannte Tote zwischen dem Tod und einer neuen Geburt als unterstes Reich das tierische Reich hat, so wie wir das mineralische Reich als unterstes Reich haben. Wir haben auch in einer gewissen Weise darauf hingewiesen, wie der Tote zu arbeiten hat innerhalb des Wesens des tierischen Reiches, wie er aufzubauen hat aus den Gesetzen der Tierheit dasjenige, was wiederum der nächsten Inkarnation als Organisation zugrunde liegt. Wir haben darauf hingewiesen, wie als zweites Reich der Tote alle diejenigen Zusammenhänge erlebt, die hier in der physi­schen Welt karmisch begründet worden sind, und die sich in die geistige Welt hinein entsprechend verwandelt fortsetzen. Ein zweites Reich baut sich auf also für den Toten, das zusammengewoben ist aus all den karmischen Zusammenhängen, die er jemals in einer Inkarnation auf der Erde begründet hat. Dadurch dehnt sich aber allmählich alles, was der Mensch an Interesse entwickelt zwischen dem Tod und einer neuen Geburt, man kann sagen, in Konkretheit über die ganze Menschheit aus.",
      "Als drittes Reich, das der Mensch dann durchlebt, können wir auf­fassen das Reich der Angeloi. Und wir haben auch schon in einem ge­wissen Sinne darauf hingewiesen, welche Rolle die Angeloi spielen drüben in dem Leben zwischen dem Tod und einer neuen Geburt. Sie tragen gewissermaßen die Gedanken von der einen menschlichen Seele zur andern menschlichen Seele hin und bringen sie wieder zurück. Sie sind die Boten des gemeinschaftlichen Gedankenlebens. Die Angeloi sind im Grunde genommen von den Wesen der höheren Hierarchien diejenigen, über die der Tote das klarste Erleben hat; ein klares Erleben über die tierischen und ein klares Erleben über die menschlichen Zu­sammenhänge, das sein Karma begründet hat durch die Wesen der höheren Hierarchien. Die klarste Vorstellung hat er von jenen Wesen",
      "aus der Hierarchie der Angeloi, die eigentlich die Träger der Gedanken beziehungsweise überhaupt der Seeleninhalte von einem Wesen zu dem andern sind, die auch dem Toten helfen beim Bearbeiten der Tierheit. Man könnte sagen - wenn man von den Angelegenheiten der Toten als von persönlichen Angelegenheiten spricht -, die Wesen aus der Hierar­chie der Angeloi haben sich vorzugsweise zu bestreben, die persönlichen Angelegenheiten der Toten zu besorgen. Allgemeinere Angelegenheiten der Toten, die nicht persönliche sind, werden mehr besorgt von den Wesen aus dem Reich der Archangeloi und der Archai.",
      "Wenn Sie sich erinnern an den Vortragszyklus über «Inneres Wesen des Menschen und Leben zwischen Tod und neuer Geburt», dann wer­den Sie in Ihr Gedächtnis zurückrufen, daß es zum Leben des sogenann­ten Toten gehört, abwechselnd gewissermaßen sein Wesen auszudehnen über die Welt und es wieder zusammenzuziehen in sein Inneres. Ich habe das dort tiefer begründet und geschildert.",
      "Das Leben des Toten ver­läuft so, daß gewissermaßen eine Art Abwechselung stattfindet zwi­schen Tag und Nacht. Aber diese Art ist so, daß aus dem Innern auf-taucht reges Leben. Man weiß: Was da auftaucht, dieses rege Leben, das ist nur das Wiederauftauchen dessen, was man in dem andern Zu­stande, mit dem dieser abwechselt, durchlebt hat, indem man sein Wesen ausgedehnt hat über die Welt, indem man zusammengewachsen ist mit der Außenwelt.",
      "Wenn man daher mit einem Toten zusammen-kommt, trifft man abwechselnde Zustände: Solche Zustände, wo er sein Wesen über die Welt ausdehnt, wo er gewissermaßen mit seinem eigenen Wesen in die Wesenhaftigkeit seiner Umgebung, in die Vorgänge seiner Umgebung hineinwächst. Da weiß er am wenigsten, da ist für ihn eine Art von Schlafzustand vorhanden, wenn er mit seinem Wesen in die geistige Welt um ihn hineinwächst.",
      "Wenn das wieder auftaucht aus sei­nem Innern, dann ist für ihn eine Art Wachzustand vorhanden, dann weiß er alles das. Denn sein Leben verfließt in der Zeit, nicht im Raume. Wie wir als Besitzer des wachen Tagesbewußtseins draußen im Raume dasjenige haben, was wir hereinnehmen in unser Bewußtsein und dann wiederum uns von ihm zurückziehen im Schlafe, so ist es beim Toten so, daß er von einem gewissen Zeitraume, den er durchlebt hat, die Erlebnisse hereinnimmt in den nächsten Zeitraum und sie dann sein",
      "Bewußtsein ausfüllen. Vergangene Zeit füllt sein Bewußtsein aus, wie unser Wachbewußtsein der Raum ausfüllt. Es ist ein völliges Leben in der Zeit. Und damit muß man sich bekanntmachen.",
      "Durch dieses rhythmische Zeitleben, das der Tote führt, kommt er nun in eine ganz bestimmte Beziehung zu den Wesen aus der Hierarchie der Archangeloi und der Archai. Von diesen Wesenheiten, von den Archangeloi und den Archai, hat er nicht eine so klare Vorstellung wie von den Angeloi und von den Menschen und von der Tierheit, aber er hat vor allen Dingen immer die Vorstellung, daß diese Wesenheiten, die Archai und Archangeloi, diejenigen sind, welche mit ihm zusammen­arbeiten in diesem Aufwachen, Einschlafen, Aufwachen, Einschlafen -in diesem Rhythmus, der sich im Laufe der Zeit abspielt. Der Tote hat -wenn er dazu kommt, ein Bewußtsein von dem zu entwickeln, was er im vorhergehenden Zeitabschnitt erlebt, aber nicht gewußt hat -, er hat immer das Bewußtsein, daß ein Wesen aus der Hierarchie der Archai ihn aufgeweckt hat; er hat immer das Bewußtsein, daß er in bezug auf dieses rhythmische Leben zusammenarbeitet mit den Archai und Arch­angeloi.",
      "Halten wir recht gut fest, geradeso wie wir hier im Aufwachen ge­wahr werden: uns wird bewußt die äußere Welt, von der wir während des Schlafens nicht wissen, wie wir hier gewahr werden: diese äußere Welt geht in die Finsternis hinunter, wenn wir einschlafen - so lebt in der Seele des sogenannten Toten das Bewußtsein: Archai, Archangeloi, mit ihnen arbeite ich zusammen, auf daß ich durchgehen kann durch dieses Leben des Einschlafens, Aufwachens, Einschlafens, Aufwachens und so weiter. Man möchte sagen, der Tote verkehrt mit Archangeloi und Archai so, wie wir hier im Wachbewußtsein mit der physischen Umgebung, der Pflanzen- und mineralischen Welt verkehren. Der Mensch kann nicht zurückschauen in dieses Zusammenspielen, in das er hineinverwoben ist zwischen dem Tod und einer neuen Geburt. Warum nicht? Nun, man meint: Warum nicht? - aber gerade dieses Zurück­schauen ist etwas, was der Mensch wird lernen müssen, nur kann er es freilich aus den materialistischen Vorstellungen der Gegenwart heraus schwierig lernen. Ich möchte Ihnen graphisch darstellen, warum da der Mensch nicht zurücksieht (Siehe Zeichnung).",
      "# Bild s. 131",
      "Nehmen Sie einmal an: Sie stehen mit Ihrem gesamten Sinnes- und Vorstellungsapparat der Welt gegenüber. Dadurch haben Sie Vorstel­lungen, Wahrnehmungsinhalte verschiedenster Art. Ich bezeichne das, was in einem Momente Bewußtsein ist, so, daß ich da verschiedene Ringe, kleine Kreise aufzeichne.",
      "Das ist in einem Momente im Bewußt­sein. Jetzt wissen Sie, findet in anderer Art, als Psychologen heute meinen, aber es findet statt ein Erinnerungsprozeß, wenn Sie zurück­schauen; und die Zeit, in die Sie zurückschauen können, indem Sie sich erinnern, die bezeichne ich mit dieser Linie, mit der aber eigentlich die­ser Raum gemeint ist, der da blind ausläuft, hier wäre der Punkt im dritten, vierten oder fünften Jahre, bis zu dem man sich im Leben zurückerinnert.",
      "Da drinnen liegen also alle die Vorstellungen, die ent­stehen, wenn man sich an die Erlebnisse zurückerinnert, die man gehabt hat. Nehmen Sie an: Sie haben diese Vorstellungen, sagen wir mit drei­ßig Jahren, so erinnern Sie sich, indem diese Vorstellungen vor Ihnen auftauchen, an etwas, das Sie vor zehn Jahren gehabt haben.",
      "Wenn Sie sich so recht lebhaft, bildhaft vorstellen, wie das eigentlich ist mit der Seele, so können Sie folgendes denken. Sie können sich sagen: Wenn wir so zurückschauen bis dahin, wo in der Kindheit dasjenige auftaucht, bis wohin wir uns erinnern, so ist das ein seelischer Sack, der ein Ende hat; er hat dort seinen Bogen, wo der Punkt liegt, bis zu dem wir uns in der Kindheit zurückerinnern.",
      "Das ist ein solcher Seelensack; das ist die Zeit, die überschaut wird. Stellen Sie sich solch einen seelischen Sack",
      "vor, in den Sie so zurück hineinblicken: hier ist die Grenze dieses Sackes, diese Grenze fällt in Wirklichkeit zusammen mit der Grenze zwischen Ätherleib und physischem Leib. Diese Grenze muß da sein, Sie können sich das sehr grob vorstellen: sonst würden nämlich die Vorgänge, welche die Erinnerung herbeiführen, immerfort da durchfallen. Sie würden sich an nichts erinnern können, die Seele wäre ein Sack, der keinen Boden hat, es würde alles durchfallen. Es muß also eine Grenze da sein, es muß ein wirklicher seelischer Sack vorliegen. Dieser seelische Sack aber hindert zu gleicher Zeit, auch dasjenige wahrzunehmen, was man so durchlebt hat, daß es außerhalb liegt. Sie sind sich selbst in Ihrem Seelenleben undurchsichtig, weil Sie Erinnerungen haben. Weil Sie das Vermögen der Erinnerung haben, sind Sie undurchsichtig.",
      "Sie sehen, das, was macht, daß wir ein ordentliches Bewußtsein für den physischen Plan haben, ist zu gleicher Zeit der Grund, daß wir nicht hineinsehen mit dem gewöhnlichen Bewußtsein in dieses Gebiet, welches hinter der Erinnerung liegen müßte. Hinter der Erinnerung liegt es nämlich in Wirklichkeit.",
      "Man kann sich aber bemühen, die Er­innerung nach und nach etwas umzugestalten. Man muß nur vorsichtig dabei sein. Man kann damit beginnen, daß man versucht, dasjenige, an das man sich erinnert, immer genauer und genauer meditativ ins Auge zu fassen, bis man das Gefühl hat: Es ist nicht nur etwas, was man so in der Erinnerung ergreift, sondern etwas, was eigentlich da stehen bleibt.",
      "Ein Mensch, der ein intensives, reges Geistesleben entwickelt, bekommt schon allmählich dieses Gefühl, daß die Erinnerung nicht etwas ist, das kommt und geht, kommt und vergeht, sondern daß der Inhalt der Erinnerung etwas ist, was stehen bleibt. Nun allerdings, in dieser Weise arbeiten, kann nur dazu führen, die Cberzeugung hervor­zurufen, daß dasjenige, was in der Erinnerung sonst auftaucht, stehen bleibt, daß es wirklich als Akasha-Chronik vorhanden bleibt, daß es nicht weggeht.",
      "Dasjenige, was wir sonst in der Erinnerung überblicken: es steht da in der Welt, es ist in Wirklichkeit da. Aber weiter kommt man durch diese Methode eigentlich nicht, denn diese Methode, sich nur an seine persönlichen Erlebnisse zu erinnern, die gut hervorgerufen wird, die Erkenntnis, daß der Erinnerungsgehalt stehen bleibt - diese Methode ist in einem höheren Sinne zu egoistisch, um weiterzuführen",
      "als nur bis zu dieser Überzeugung. Im Gegenteil, wenn Sie über einen gewissen Punkt hin gerade diese Fähigkeit ausbilden würden, hinzu-schauen auf das Stehenbleibende Ihrer eigenen Erlebnisse, so werden Sie sich erst recht den Ausblick in die freie Geisteswelt verbauen. Denn statt daß der Sack der Erinnerungen da ist, steht dann nur Ihr eigenes Leben um so kompakter da und läßt Sie nicht durchblicken.",
      "Dagegen kann man eine andere Methode anwenden, die in ganz aus­gezeichneter Weise, wenn ich den Ausdruck gebrauchen darf, die Ein-schreibungen der Akasha-Chronik durchsichtig macht. Und sieht man einmal durch die stehengebliebenen Erinnerungen, dann sieht man sicher hinein in die geistige Welt, mit der man verbunden war zwischen dem Tod und einer neuen Geburt. Aber dazu muß man nicht nur das­jenige, was als erinnerungsgemäß stehen bleibt aus dem eigenen Leben, benützen - das wird immer kompakter und kompakter, da sieht man dann erst recht nicht durch. Es muß das durchsichtig werden. Und durchsichtig wäre es, wenn man immer stärker und stärker den Ver­such macht, nicht so sehr an das sich zu erinnern, was man von seinem Gesichtspunkte aus erlebt hat, sondern an das sich immer mehr zu er­innern, was von außen an einen herangetreten ist. Statt an das, was man gelernt hat, erinnert man sich an den Lehrer, an die Art, wie der Lehrer gesprochen, wie der Lehrer gewirkt hat, was der Lehrer mit einem gemacht hat. Man erinnert sich daran, wie das Buch entstanden ist, aus dem man dies oder jenes gelernt hat. Man erinnert sich vorzugs­weise an dasjenige, was von der Außenwelt herein an einem gearbeitet hat.",
      "Ein sehr schöner, wunderbarer Anfang, ja eine Anleitung zu solcher Erinnerung ist Goethes Schrift «Dichtung und Wahrheit», wo er schil­dert, wie er, Goethe, aus der Zeit heraus geformt wird; wie die ver­schiedenen Kräfte an ihm arbeiten. Daß Goethe so etwas gemacht hat in seinem Leben, daß er in einer solchen Weise eine Art Rückschau ge­halten hat, nicht von dem Gesichtspunkte der eigenen Erlebnisse, son­dern von dem Gesichtspunkte der andern und der Zeitereignisse, die an ihm gearbeitet haben, dem verdankt er, daß er solche tiefen Einblicke hat tun können in die geistige Welt, wie er getan hat. Das aber ist auch zu gleicher Zeit der Weg, um in weiterem Umfange mit der Zeit in",
      "Berührung zu kommen, die zwischen dem letzten Tode und dieser un­serer Geburt verflossen ist.",
      "Also Sie sehen, von einem andern Gesichtspunkt aus weise ich Sie heute auf dasselbe hin, worauf ich Sie schon hingewiesen habe: Erwei­terung der Interessen über das Persönliche hinaus, gerade Hinlenkung der Interessen und der Aufmerksamkeit auf dasjenige, was nicht wir sind, sondern was uns geformt hat, woraus wir entstanden sind. Ein Ideal ist es, hinzuschauen auf die Zeit und auf längere Vorzeit vor uns und all die Kräfte aufzusuchen, die diesen Kerl, der man geworden ist, aus sich heraus geformt haben.",
      "Das allerdings bietet wenig Schwierigkeiten, wenn man es so schil­dert, aber es ist keine ganz leichte Aufgabe. Es ist auch eine Aufgabe, die, weil sie starke Selbstlosigkeit erfordert, großen Erfolg hat. Gerade diese Methode erweckt die Kräfte, mit seinem Ich in dieselbe Sphäre hineinzukommen, die die Toten mit den Lebendigen gemeinschaftlich haben. Weniger sich kennenzulernen, mehr seine Zeit kennenzulernen, das wird die Aufgabe eines öffentlichen Unterrichts in einer gar nicht zu fernen Zukunft sein, aber seine Zeit im Konkreten kennenzulernen, nicht so kennenzulernen, wie es jetzt in den Geschichtsbüchern steht; so, wie diese Zeit selbstverständlich sich entwickelt aus geistigen Im­pulsen heraus.",
      "Also wieder werden wir auch auf diese Weise dazu geführt, die In­teressen zu erweitern über eine Charakteristik unseres Zeitalters und seines Hervorgehens aus dem allgemeinen Weltengang. Warum hat denn Goethe so intensiv danach gestrebt, griechische Kunst kennenzu­lernen, seine Zeit durch und durch zu verstehen, sie abzumessen an der vorhergehenden Zeit? Warum läßt er seinen Faust bis in die griechische Zeit, bis in die Helena-Zeit zurückgehen, den Chiron aufsuchen, die Sphinxe aufsuchen? Weil er seine eigene Zeit, wie sie an ihm gearbeitet hat, so kennenlernen will, wie er sie nur kennenlernen kann, wenn er diese eigene Zeit an der früheren Zeit mißt. Aber Goethe läßt seinen Faust nicht sich hinsetzen und Pergamente entfalten, Urkunden der Staatsarchive entfalten, sondern er führt ihn zurück auf Seelenwegen in die Impulse, welche ihn selber geformt haben. Es steckt in ihm man­ches von dem, was den Menschen hinweist auf ein Zusammenkommen",
      "auf der einen Seite mit den Toten, auf der andern Seite - Sie können es jetzt sehen aus dem Zusammenhang der Toten und Archangeloi - mit den Zeitgeistern und den Erzengeln. Dadurch, daß der Mensch mit den Toten zusammenkommt, kommt er auch in Berührung mit den Erz-engeln und den Zeitgeistern. Gerade in den Impulsen, auf die Goethe in seinem «Faust» hindeutet, liegt das, wodurch der Mensch seine Inter­essen erweitert über den Zeitgeist, liegt das, was im eminentesten Sinne unserer Zeit notwendig ist. Allerdings ist unserer Zeit notwendig, in anderer Art auf so etwas hinzuschauen, wie es zum Beispiel der «Faust» ist, als die Zeit bisher darauf hingeschaut hat. Die meisten derjenigen, die den «Faust» beurteilen, kommen kaum darauf, wo die Probleme liegen. Einige kommen darauf, die Fragen zu stellen. Die Antworten werden oft in der kuriosesten Weise gegeben.",
      "Nehmen Sie ein Beispiel, wo Goethe nun wirklich darauf hinweist:",
      "Denkt nach! Wird da immer nachgedacht? Goethe macht aber alles, um Deutlichkeit dafür hervorzurufen, daß über gewisse Dinge nachzu­denken ist. Zum Beispiel: Sie wissen, die Erichtho redet über dasjenige, was Schauplatz der klassischen Walpurgisnacht ist; sie entfernt sich, die Luftfahrer, Homunkulus mit Faust und Mephistopheles erscheinen. Sie erinnern sich an die ersten Reden des Homunkulus, des Mephisto, des Faust. Nachdem Faust den Boden berührt hat und die Frage auf­geworfen hat: Wo ist sie? - sagt Homunkulus:",
      "Wüßten's nicht zu sagen,",
      "Doch hier wahrscheinlich zu erfragen.",
      "In Eile magst du, eh' es tagt,",
      "Von Flamm' zu Flamme spürend gehen:",
      "Wer zu den Müttern sich gewagt,",
      "Hat weiter nichts zu überstehen.",
      "Homunkulus sagt: «Wer zu den Müttern sich gewagt, hat weiter nichts zu überstehen . . . » Woher weiß denn der, daß der Faust bei den Müttern war? Das ist eine Frage, die ganz notwendig sich ergibt, denn blättern Sie zurück, so werden Sie sehen, daß nirgends eine Andeutung darüber ist, daß Homunkulus erfahren haben könnte als ein Wesen außer dem Faust, daß der Faust bei den Müttern war. Jetzt auf einmal piepst der",
      "Homunkulus davon, daß «wer zu den Müttern sich gewagt, hat weiter nichts zu überstehen». Sie sehen, Goethe gibt schon Rätsel auf. Mit zwingender Notwendigkeit geht daraus hervor, daß Homunkulus, wenn er überhaupt irgend etwas ist, dieses innerhalb des Bewußtseins-bereiches des Faust selber ist; denn nur dann kann er dasjenige, was innerhalb des Bewußtseinsbereiches des Faust ist, wissen, wenn er zum Bewußtseinsbereiche des Faust selber gehört.",
      "Erinnern Sie sich an manche Auseinandersetzungen, die wir über den «Faust» gegeben haben, daß Homunkulus eigentlich nichts anderes ist als dasjenige, was als astralischer Leib bereitet werden muß, damit die Helena crscheinen kann. Aber dadurch ist er in einem andern Be­wußtsein, ist sein Bewußtsein erweitert über den Astralleib. Dann haben Sie eine Verständnismöglichkeit des Wissens des Homunkulus, wenn er in den Bewußtseinsbereich des Faust selber hineinkommt. Deshalb läßt Goethe den Homunkulus werden, weil durch das Werden des Homun­kulus das Bewußtsein des Faust gewissermaßen die Möglichkeit findet, aus sich herauszugehen, nicht nur in sich zu sein, sondern draußen zu sein. Und er ist auch da, wo der Homunkulus ist; der Homunkulus ist im Bewußtsein des Faust darinnen.",
      "Goethe nimmt in diesem Sinne Alchimie sehr ernst, wie Sie sehen. Solche Rätsel, die direkt mit Geheimnissen der geistigen Welt zusam­menhängen, sind im «Faust» sehr viele. Man muß den «Faust» so auf sich wirken lassen, daß man gewahr wird, welche Tiefen geistiger Wirklichkeit eigentlich diesem «Faust» zugrunde liegen. Nur dadurch versteht man so jemanden wie Goethe, daß jnan sich klarmacht: Er hat auf der einen Seite getrachtet, das, was ihn gemacht hat, wirklich wie von außen anzusehen, wofür ein Beweis seine Darstellung in «Dichtung und Wahrheit» ist, und hat auf der andern Seite auch gewußt, das führt zurück sogar in weite perspektivische Zusammenhänge mit den Toten. Und Faust tritt in das Leben sehr weit zurückliegender Menschen-entwickelung ein, tritt auch in das Leben weit zurückliegender geistiger Wesenheiten ein.",
      "Aber, wenn man ganz durchschauen will, was nötig ist in positivem Sinne für die Gegenwart, dann muß man in vieler Beziehung auch einen Blick und ein Gefühl für das Negative haben, muß das richtige",
      "Fühlen entwickeln für das Negative. Man muß einen Blick haben für alles das, was verhindert das als notwendig bezeichnete Zusammen­kommen der lebenden Menschen im gemeinsamen Plane mit dem Wir­ken der Toten. Überall können Sie heute die Hindernisse entdecken. Sie finden sie auf Schritt und Tritt. Sie finden sie gerade dort, wo Bil­dung - verzeihen Sie, daß ich dieses häßliche Wort gebrauche - heute verbreitet wird.",
      "Wie fühlt sich ein Mensch heute geradezu gescheit, tief gescheit, auf­geklärt, wenn er dergleichen hinschreiben kann: «Swedenborg, um dessen finster-rätselvolle Persönlichkeit auch Goethe mit ehrfürchtigem Tasten herumgewandert ist, hat mit den Engeln jenseits der Erde ver­kehrt. Erzählt hat er, daß diese überirdischen Geschöpfe, mit Gedanken streitend, sogar mit Gewändern bekleidet einhergehen.",
      "Das Ringen um Erkenntnis und Aufklärung sei ihnen nicht fremd, haben sie doch eine Druckerei eingerichtet, von der sie manchmal zu besonders glücklichen Menschen einige Blätter hinabschicken. Mit hebräischen Buchstaben sind die Zeitungen des Jenseits dann bedeckt.",
      "Ein Eigentümliches der ehrwürdigen biblischen Bilderzeichen wäre es, daß jeder Strich an ihnen, jede Kante, jede Biegung, einen geheimnisvollen Geisteswert verberge. Nur lernen müsse der Mensch, das Engelsgeschnörkel richtig zu lesen, damit er in die Wahrheit des Jenseits, in das abgekehrte, ewig besonnte Leben, in die beseligende Festlichkeit und das erheiternde Paradies des Jenseits eingeweiht werde.",
      "Swedenborg, dem es gelang, bei lebendigem Leibe manchmal für das irdische Leben abzusterben und vor dem körperlichen Tode schon den Aufschwung in das Jenseits zu vollführen, hat vieles von den Engeln erfragt und über sie berichtet. Jahrhunderte vor ihm haben Babylonier, Ägypter und Juden das gleiche Kundschafterhandwerk geübt.",
      "Menschenalter nach ihm, bis zum heu­tigen Tage noch, tun es die auf der Erde unzufriedenen Wesen, die sich über ihre Zukunft von Gott Rates holen wollen, die auf die Gesellschaft ihrer Toten nicht verzichten, und die endlich der Meinung sind, die Brücke, die von ihrem träumeumspielten Bett bis in die Bezirke des Unfaßbaren gebaut wird, sei ein fester, seraphisch zementierter, von Geistern durchaus gestählter und getragener Weg.»",
      "Und so setzt der betreffende, sich sehr gescheit haltende Mensch",
      "seine Betrachtungen fort, sich in einem billigen Spott über diejenigen ergehend, die da versuchen, die Brücke zu schlagen in das Jenseits; denn dieser sehr gescheite Mann hat das Buch eines andern sehr gescheit sich dünkenden Menschen gelesen und schreibt darüber: «Dieses Jenseits der Sinne, das von der Seele bewohnt wird, will das gewichtige Buch Max Dessoirs:  neu beschreiben, nachdem schon tausende von Grüblern diesen Weg ins Jenseits betreten haben. Diesmal redet also ein Philosoph, der sich um Menschenkenntnis mehr bemüht hat als um die Sonderung verwaister Gedankenrichtungen, ein Kunst-freund, der sich nicht gescheut hat, die Rätsel-umschattete Geburts­sekunde eines Künstlerplanes auszudeuten, ein Mann endlich, der ge­legentlich auch mit dem Messer in der Hand Knochen und Nerven des Menschen abgesucht hat, damit er sich in den zahlreichen irdischen Verstecken der Seele zurechtfindet.",
      "Weil Dessoir so vielfältig gegen die Übereilung der Schwarmgeister und gegen die Kälte der hochmütigen Vernünftler geschützt ist, ver­dient sein seit mehr als dreißig Jahren vorbereitetes Urteil über Dinge des Jenseits auch bei jenen Achtung und Gehör, die ihm nicht auf sei­nem Wege folgen können» und so weiter.",
      "Jenes besagte Individuum Max Dessoir mußte ich besprechen in dem zweiten Kapitel meines Buches: «Von Seelenrätseln», denn dieser Uni­versitätsprofessor hatte die Frechheit, die Anthroposophie als solche zu besprechen. Ich mußte mich der Aufgabe unterziehen, nachzuweisen, daß die ganze Art, wie Max Dessoir arbeitet, die gewissenloseste, ober­flächlichste Art ist, die sich nur denken läßt. Dieser Mann hat die Stirne, auf fast ausschließlich blödsinnig geformte Zitate hin, die er aus wenigen meiner Bücher ausschreibt und immer so ausschreibt, daß sie in der blödsinnigsten Weise entstellt sind, ein abfälliges Urteil zu fällen. Man muß schon die Tatsache in dieser Form hinstellen, wenn man jenen Skandal in Wirklichkeit sehen will, der möglich ist innerhalb des­jenigen, was sich heute vielfach Wissenschaft nennt. Ich habe das Indi­viduumDessoir in meinem Leben nur einmal gesehen; es war im Anfang der neunziger Jahre. Damals hat er mir eine sehr gescheite Bemerkung gemacht. Meine «Philosophie der Freiheit» war damals noch nicht ge­schrieben. Max Dessoir sagte dazumal - es war bei einem Goethe-Diner",
      "in Weimar: «Ja, Sie haben allerdings einen Fehler, Sie beschäftigen sich mit zu vielerlei Wissenschaften.» Das war der große Fehler, daß man versuchte, nicht einseitig zu sein!",
      "Unter den andern Blödsinnigkeiten, die Max Dessoir in seinem Buche begeht, ist zum Beispiel auch diese, daß er jetzt von meiner «Philosophie der Freiheit» als von meinem «Erstling» spricht. Der ist zehn Jahre ungefähr nach meinem wirklichen Erstling geschrieben; eine zehn-jährige Schriftstellerlaufbahn liegt vor der «Philosophie der Freiheit». Das alles und vieles andere ist ganz gleich erlogen in dem Dessoir-Buch. Wie viele Leute werden die notwendig gewordenen, sachlichen Aus­einandersetzungen, die zeigen, welche Windbeutelei Dessoirs Wissen­schaft ist, wie viele Leute werden diese sachlichen Auseinandersetzun­gen in meinem Buche «Von Seelenrätseln» lesen! Wie vielesJournalisten­geschmeiß von der Sorte von Max Hochdorf in Zürich findet sich aber zusammen, um das unsinnige Buch Max Dessoirs «Vom Jenseits der Seele» hinauszuposaunen in der Art, daß man sagt, «Dieses Jenseits der Sinne, das von der Seele bewohnt wird, will das gewichtige Buch Max Dessoirs:  neu beschreiben, nachdem schon tausende von Grüblern diesen Weg ins Jenseits betreten haben» und so weiter.",
      "Auf solche Dinge ist es notwendig den Blick zu richten. Es ist ja sattsam bekannt, daß dasjenige, was auf dem Boden der anthroposo­phisch orientierten Geisteswissenschaft versucht wird, in beispiellosester Weise da und dort entstellt wird; zuweilen von Leuten, die sehr gut wissen, daß das Gegenteil von dem wahr ist, was sie sagen. Allein das sind zum großen Teil arme Hascherln, die innerhalb der Gesellschaft ihre persönlichen Interessen nicht befriedigen konnten, die sie befrie­digen zu können glaubten, und mit denen man ja Mitleid haben kann, über die man nicht weiter zu reden braucht. Und die wissen selbst am besten, wie es mit der objektiven Wahrheit dessen steht, was sie sagen. Aber solches Gift, wie das von Max Dessoir verbreitete, das ist aller­dings ernster zu nehmen, und ich mußte schon das Meinige tun, um gewissermaßen Satz für Satz die ganze philosophische Nichtswürdig­keit der Dessoirschen Auseinandersetzungen klarzulegen. Ehe nicht in weitesten Kreisen ein gesundes Urteil über solche angebliche Wissenschaftelei",
      "herrscht wie die eines Max Dessoir - und solche Max Dessoirs gibt es sehr viele - und so lange nicht ein gesundes Urteil herrscht über solche Schleppenträger der Max Dessoirei, wie zum Beispiel dieser Artikelschreiber ist, der sich natürlich dann nicht entwehren kann, seinen Artikel zu schließen mit den Worten: «Weil eben der Weg in das Jenseits so vollkommen versperrt ist» - natürlich, für das verbaute Ge­hirn dieses Herrn Max Dessoir ist der Weg in das Jenseits versperrt! -«haben die Menschen in den Jahrtausenden immer wieder versucht, die Schranken zu sprengen.» «Magische Idealisten» nennt Dessoir diese Kämpfer um das verzweifelt feste und doch gar nicht greifbare Geister-reich. Er führt sie alle heran, diese Gesundbeter, Zahlenapostel, ägyp­tischen Zauberer, Negerheiligen, Anthroposophen, Neubuddhisten, Kabbalisten . . . Er ist ein höchst fesselnder Geschichtsschreiber all der dem Wunder unterworfenen, all der dem Wunder trotzdem aufsässigen Geschlechter. «Es verbrüdert sich eine eigentümliche Gesellschaft, wenn man alle Männer, die Weisen und die Narren, aufzählt, die sich um den reinen Geist versammeln wollten. Cagliostro und Kant, Hegel und auch der moderne Hexenmeister Svengali begegnen da einander, wenn sie sich lustwandelnd auf dem Wege ins Jenseits verlieren.»",
      "Zu verhindern, daß es Menschen gibt, die in dieser Weise schreiben, ist natürlich nicht möglich, aber in weitesten Kreisen muß ein gesundes Urteil Platz greifen, welches verhindert, daß dasjenige, was auf diesem Wege in die Öffentlichkeit kommt, autoritativ hingenommen wird. Denn selbstverständlich, Gedankenformen von dieser Art, herum­sprühend in unserem sozialen Organismus, verhindern jede Möglichkeit eines heilsamen Fortschrittes der Menschheit. Für sich selber kann man sich, wenn man wissenschaftlichen Unrat wie den Max Dessoirschen hat angreifen müssen, die Hände waschen und kann sich damit be­friedigt erklären. Aber dieser wissenschaftliche Unrat fließt und fließt, und es sind heute der Wege allzu viele, auf denen dieser Unrat fließen kann. Man muß schon manchmal ein Beispiel annageln. Es mußte in diesem Falle wiederum geschehen, weil Sie sich ja ausrechnen können, in wie viele Menschenköpfe nun wiederum einmal unter andern auch ein Urteil über die Anthroposophie hineingetrichtert wird, wenn ein solches Feuilleton wie das vom 14. Dezember 1917 in der «Neuen Zürcher",
      "Zeitung» erscheint, von einem Menschen, der als ein ganz gescheiter auf einem ebensolchen gescheiten, nämlich auf Max Dessoir, fußt!",
      "Diese Dinge muß man als kulturhistorische Fakta ins Auge fassen, muß ihre kulturhistorische Bedeutung ins Auge fassen. Gewiß, es ist nur eine geringfügige Möglichkeit leider heute noch vorhanden, so etwas wie dieses Kapitel, das ich geschrieben habe: «Max Dessoir über An­throposophie», unter die Menschen zu bringen.",
      "Denn auch in der An­throposophischen Gesellschaft ist ja nur ein kleiner Kreis, der seine Aufgabe wirklich versteht: die Aufgabe, die Menschheit aufzuklären über die Art und Weise, wie heute oftmals Wissenschaft gemacht wird, aufzuklären in der richtigen und rechtmäßigen Weise. Und das, was heute als Wissenschaft gemacht wird, das ist aber nur ein Symptom für allgemeines Denken.",
      "Denn so, wie es in der Wissenschaft bestellt ist -wofür Max Dessoir ein schreiendes Beispiel ist mit all seinen Traban­ten -, so ist es auch auf andern Gebieten bestellt. Und wenn Sie die Frage aufwerfen: Was hat in die heutige Katastrophe an tieferen Kräf­ten hineingeführt? - bleiben Sie immer an der Oberflächenansicht, wenn Sie nicht auf diese tieferen Gründe eingehen, auf dasjenige, was in der Verrenktheit, in der gesuchten Verrenktheit und in der gesuchten Oberflächlichkeit, Scharlatanerie liegt, eine Scharlatanerie, die sich da­durch zu erhalten sucht, daß sie ernste Geistigkeit gerade der Scharla­tanerie zuschreibt.",
      "Das muß in gesundem Sinne in seiner wahren Ge­stalt durchschaut werden. Ich führe das Beispiel von Max Dessoir nur aus dem Grunde an, weil es eben gerade naheliegt. Aber es ist ein Bei­spiel für vieles, was als Negatives in unserer Zeit existiert.",
      "Will einer in der Menschheit ein Herz haben für das Positive des Zusammen­wachsens mit der geistigen Welt, dann muß er auch ein Herz haben zum Abweis, zum starken, herzhaften Abweis, wo es nur sein kann, des Unechten, des Oberflächlichen, des Nichtsnutzigen.",
      "Erleben wir es ja geradezu in unseren Tagen, daß oftmals diejenigen, die auch im öffentlichen Leben am schlimmsten hingestellt werden, gerade die Anständigsten sind. Es gibt nicht die Notwendigkeit, mit Pessimismus nach diesen Dingen zu blicken, aber es gibt die Notwen­digkeit, in seiner eigenen Seele Kräfte aufzusuchen, die ein gesundes Urteil über diese Dinge in dieser Seele erzeugen und heranzüchten."
    ],
    "sentences": [
      [
        "Den Betrachtungen, die in diesen Wochen gehalten worden sind, lag verschiedenes zugrunde, das dazu führen kann, die menschliche Natur in ihrem Zusammenhang mit dem geschichtlichen Werden der Mensch­heit so zu verstehen, daß man sich allmählich eine Vorstellung bilden kann über Notwendigkeit und Freiheit.",
        "Weniger können solche Dinge entschieden werden durch Definitionen und Wortauseinandersetzungen als dadurch, daß man die entsprechenden Wahrheiten aus der geistigen Welt zusammenträgt."
      ],
      [
        "Die Menschheit wird sich in unserem Zeitalter immer mehr daran gewöhnen müssen, eine andere Art des Verständ­nisses der Wirklichkeit sich anzueignen, als es die heute so vielfach herr­schende und übliche ist, die sich im Grunde genommen an sehr Sekun­däres, an allerlei nebulose Vorstellungen in Anknüpfung an Wortdefi­nitionen und so weiter hält.",
        "Man hat heute, wenn man das vornimmt, was manche Leute schreiben oder sagen, die sich für ganz besonders gescheit halten, das Gefühl: sie reden in Begriffen und Vorstellungen, die nur scheinbar bestimmt, in Wirklichkeit aber so unbestimmt sind, wie wenn jemand über einen gewissen Gegenstand sprechen würde, der zum Beispiel aus einem Kürbis gemacht ist."
      ],
      [
        "Hat man einen Kürbis um­gestaltet zu einer Flasche und benützt ihn als Flasche, so kann man über diesen Gegenstand so reden, als ob man über einen Kürbis redet, denn ein Kürbis ist es in Wirklichkeit; aber man kann auch wie über eine Flasche reden, denn eine Flasche ist er ja auch, er wird richtig be­nützt als Flasche.",
        "Nicht wahr, die Dinge, über die man spricht, bekom­men erst ihre Valeurs in den Zusammenhängen, in denen man sich ergeht."
      ],
      [
        "Wenn man nicht in Anlehnung an Worte, sondern aus einer ge­wissen Anschauung heraus spricht, so wird jeder Mensch wissen, ob man eine Flasche meint oder einen Kürbis.",
        "Aber man darf sich dann nicht auf die Beschreibung des Gegenstandes oder die Definition des Gegenstandes beschränken."
      ],
      [
        "Denn solange man sich auf eine Beschrei­bung, auf eine Definition beschränkt, kann es ebensogut ein Kürbis oder eine Flasche sein.",
        "Und so kann heute dasjenige, worüber viele"
      ],
      [
        "Philologen, Leute, die sich sehr gescheit dünken, reden, die Seele des Menschen sein, es kann aber auch der Leib des Menschen sein, es kann Kürbis und kann Flasche sein."
      ],
      [
        "Ich meine mit dieser Bemerkung sehr vieles von dem, was in der Ge­genwart sehr ernst genommen wird, zum Teil zum Unheil der Mensch­heit.",
        "Daher eben ist es notwendig, daß gerade von der anthroposophisch orientierten Geisteswissenschaft, zu der unter anderem auch klares, präzises Denken nötig ist, ausgehe ein Bestreben, nicht in einer solchen Weise, wie es heute üblich ist, die Welt anzuschauen, nicht den Kürbis mit der Flasche zu verwechseln, sondern überall auf das Reale zu sehen, sei es das äußere Physisch-Reale, sei es das Geistig-Reale."
      ],
      [
        "Man kann ohnedies nicht zu einer wirklichen Vorstellung über das­jenige gelangen, was für den Menschen in Betracht kommt, wenn man sich an Definitionen und dergleichen hält, sondern nur dann, wenn man die Lebenszusammenhänge in ihrer Wirklichkeit ins Auge faßt.",
        "Und gar über solch wichtige Begriffe wie Freiheit und Notwendigkeit im sozialen, im sittlichen Leben, kann man nur Klarheit gewinnen, wenn man zusammenhält solche spirituellen Tatsachen, wie sie in die­sen Betrachtungen vorgebracht worden sind und gewissermaßen ver­sucht, sie immer aneinander abzuwägen, um ein Urteil über die Wirk­lichkeit zu gewinnen."
      ],
      [
        "Bedenken Sie, daß ich schon in öffentlichen Vorträgen und auch hier wiederum in den verschiedensten Zusammenhängen mit einer ge­wissen Intensität immer wieder und wieder hervorgehoben habe, daß wir das, was wir Vorstellungen nennen, nur dann richtig begreifen können, wenn wir sie so in Beziehung bringen zu unserm leiblichen Organismus, daß wir den Vorstellungen im Leibe nicht etwas Wach­sendes, Gedeihendes zugrunde liegend sehen, sondern gerade umgekehrt, etwas Absterbendes, etwas partiell im Leibe Absterbendes.",
        "Ich habe das so ausgesprochen in einem öffentlichen Vortrage, daß ich gesagt habe:"
      ],
      [
        "Der Mensch stirbt eigentlich immer in sein Nervensystem hinein ab. -Der Nervenprozeß ist ein solcher, daß er sich auf das Nervensystem beschränken muß.",
        "Denn würde er sich ausdehnen über den ganzen Or­ganismus, würde dasselbe vorgehen im ganzen Organismus, was in den Nerven vorgeht, so würde dies den Tod des Menschen in jedem Augenblick"
      ],
      [
        "bedeuten.",
        "Man kann sagen: Vorstellungen entstehen da, wo der Organismus sich selber abbaut, wir sterben in unser Nervensystem fort­während hinein. - Dadurch ist Geisteswissenschaft in die Notwendig­keit versetzt, nicht nur diejenigen Prozesse zu verfolgen, welche die heutige Naturwissenschaft als die einzig maßgebenden betrachtet: die aufsteigenden Prozesse.",
        "Diese aufsteigenden Prozesse, sie sind Wachs­tumsprozesse, sie gipfeln noch im Unbewußten.",
        "Erst wenn der Orga­nismus mit den absteigenden Prozessen beginnt, tritt im Organismus jene Tätigkeit der Seele auf, die man als Vorstellungs-, ja auch als sinn­liche Wahrnehmungstätigkeit bezeichnen kann.",
        "Dieser Abbauprozeß, dieser Ersterbeprozeß, der muß da sein, wenn überhaupt vorgestellt werden soll."
      ],
      [
        "Nun habe ich gezeigt, daß das freie Handeln des Menschen geradezu darauf beruht, daß der Mensch in die Lage kommt, aus reinen Gedan­ken heraus die Impulse für sein Handeln zu suchen.",
        "Diese reinen Ge­danken werden am meisten von Einfluß sein auf die Abbauprozesse im menschlichen Organismus.",
        "Was geschieht denn eigentlich, wenn der Mensch so recht eine freie Handlung vollzieht?",
        "Machen wir uns das einmal klar, was da beim gewöhnlichen physischen Menschen geschieht, wenn der Mensch aus moralischer Phantasie heraus - Sie wissen jetzt, was ich damit meine -, aus moralischer Phantasie heraus, das heißt aus einem Denken, das von sinnlichen Impulsen, sinnlichen Trieben und Affekten nicht beherrscht ist, handelt, was geschieht da mit dem Men­schen eigentlich?",
        "Dann geschieht das, daß er sich reinen Gedanken hin­gibt; die bilden seine Impulse.",
        "Sie können ihn nicht impulsieren durch sich selbst; er muß sich impulsieren, denn sie sind bloße Spiegelbilder, das haben wir ja betont.",
        "Sie gehören der Maja an.",
        "Spiegelbilder können nicht zwingen, der Mensch muß sich selber zwingen unter dem Einfluß der reinen Vorstellungen."
      ],
      [
        "Worauf wirken reine Vorstellungen?",
        "Am stärksten wirken sie auf den Abbauprozeß im menschlichen Organismus.",
        "Auf der einen Seite kommt aus dem Organismus heraus der Abbauprozeß, und auf der andern Seite kommt aus dem geistigen Leben diesem Abbauprozeß ent­gegen der reine Tatgedanke.",
        "Ich meine damit den Gedanken, welcher der Tat zugrunde liegt.",
        "Durch die Vereinigung von beiden, durch das"
      ],
      [
        "Aufeinanderwirken des Abbauprozesses und des Tatgedankens entsteht die freie Handlung."
      ],
      [
        "Ich sagte, der Abbauprozeß wird nicht durch das reine Denken be­wirkt; der ist sowieso da, er ist also eigentlich immer da.",
        "Wenn der Mensch diesem Abbauprozeß, gerade den bedeutsamsten Abbauprozes­sen in ihm, nichts aus dem reinen Denken heraus entgegenstellt, dann bleibt er Abbauprozeß, dann wird der Abbauprozeß nicht umgewandelt in einen Aufbauprozeß, dann bleibt ein ersterbender Teil im Menschen.",
        "Denken Sie das einmal durch, dann ersehen Sie daraus, daß die Mög­lichkeit besteht, daß der Mensch gerade durch Unterlassung von freien Handlungen einen Todesprozeß in sich nicht aufhebt.",
        "Darin liegt einer der subtilsten Gedanken, die der Mensch nötig hat, in sich aufzu­nehmen.",
        "Wer diesen Gedanken versteht, kann im Leben nicht mehr zweifeln an dem Vorhandensein der menschlichen Freiheit.",
        "Denn eine Handlung, die aus Freiheit geschieht, geschieht nicht durch etwas, was im Organismus verursacht wird, sondern wo die Ursachen aufhören, nämlich aus einem Abbauprozeß heraus.",
        "Dem Organismus muß etwas zugrunde liegen, wo die Ursachen aufhören, dann kann überhaupt erst die reine Vorstellung als Motiv des Handelns eingreifen.",
        "Aber solche Abbauprozesse sind immer da, sie bleiben nur gewissermaßen un­genützt, wenn der Mensch nicht freie Handlungen vollführt."
      ],
      [
        "Was hier zugrunde liegt, bezeugt aber auch, wie es mit einem Zeit­alter aussehen muß, welches sich nicht darauf einlassen will, die Idee der Freiheit im vollsten Umfange zu verstehen.",
        "Die zweite Hälfte des 19.",
        "Jahrhunderts, das 20.",
        "Jahrhundert bis in unsere Zeit, diese Epoche hat es sich geradezu zur Aufgabe gesetzt, auf allen Gebieten des Lebens die Idee der Freiheit immer mehr und mehr für die Erkenntnis zu trüben, für das praktische Leben in Wirklichkeit auszuschalten.",
        "Freiheit wollte man nicht verstehen, Freiheit wollte man nicht haben.",
        "Die Phi­losophen haben sich bemüht, zu beweisen, daß alles mit einer gewissen Notwendigkeit aus der menschlichen Natur hervorgeht.",
        "Gewiß, der menschlichen Natur liegt eine Notwendigkeit zugrunde, aber diese Notwendigkeit hört auf, indem Abbauprozesse beginnen, in welchen der Zusammenhang der Ursachen sein Ende findet.",
        "Wenn Freiheit da eingegriffen hat, wo die Notwendigkeit im Organismus aufhört, dann"
      ],
      [
        "kann man nicht sagen, daß die Handlungen der Menschen aus der inneren Notwendigkeit hervorgehen; sie gehen dann erst aus ihm her­vor, wenn diese Notwendigkeit aufhört.",
        "Der ganze Fehler bestand darinnen, daß man sich nicht eingelassen hat darauf, im menschlichen Organismus nicht nur zu verstehen die aufbauenden Prozesse, sondern auch zu verstehen die abbauenden Prozesse.",
        "Es wäre aber allerdings nötig, daß man, um das zu erkennen, was eigentlich der menschlichen Natur zugrunde liegt, mehr Begabung entwickele, als die Gegenwart Neigung dazu hat.",
        "Wir haben gestern gesehen, daß es notwendig ist, dasjenige wirklich ins Seelenauge fassen zu können, was man als menschliches Ich bezeichnet.",
        "Aber es ist gerade in der Gegenwart wenig Talent vorhanden, diese Wirklichkeit des Ich irgendwie zu erfassen.",
        "Ich will Ihnen einen Beweis liefern."
      ],
      [
        "Ich habe öfter die ausgezeichnete wissenschaftliche Leistung von Theodor Ziehen erwähnt: «Die physiologische Psychologie.» Da ist auf Seite 205 auch die Rede von dem Ich.",
        "Nur kommt Ziehen niemals in die Lage, auch nur hinzudeuten auf das wirkliche Ich, sondern er redet nur von der Ich-Vorstellung.",
        "Wir wissen, die ist jedoch nur ein Spiegel­bild des wirklichen Ich.",
        "Aber interessant ist es gerade zu hören, wie ein ausgezeichneter Denker der Gegenwart, aber ein solcher, der da glaubt, mit naturwissenschaftlichen Vorstellungen alles erschöpfen zu können, über das Ich redet.",
        "Es sind Vorträge, die wiedergegeben werden, des­halb ist die Sache in Vortragsform vorgebracht.",
        "Ziehen sagt: «Es wird Ihnen vielleicht auffallen, daß die mit dem kurzen kleinen Wort Ich bezeichnete Ich-Vorstellung ein so komplexes dreigliedriges Gebilde sein soll, an welchem tausend und abertausend Teilvorstellungen be­teiligt sein sollen.",
        "Aber ich bitte Sie zu erwägen: dasWort ist zwar kurz, aber daß sein Vorstellungsinhalt dieser Komplex sein muß, geht schon daraus hervor, daß jeder von Ihnen in Verlegenheit geraten wird, wenn er den Denkinhalt seiner sogenannten Ich-Vorstellung angeben soll.»"
      ],
      [
        "Und jetzt geht Ziehen daran, etwas zu sagen über den Denkinhalt der Ich-Vorstellungen.",
        "Nun wollen wir einmal sehen, was der ausge­zeichnete Gelehrte über dasjenige zu sagen weiß, woran man eigentlich denken soll, wenn man über sein Ich denkt: «Sie werden alsbald an Ihren Körper denken» - also an Ihren Körper denken! - «an Ihre Relationen"
      ],
      [
        "zur Außenwelt, Ihre verwandtschaftlichen und Eigentums­beziehungen» - also man wird bald daran gehen, an seine Börse zu denken und sein Geld abzuzählen! - «Ihre Namen und Titel... »"
      ],
      [
        "Nun, der ausgezeichnete Gelehrte weist ausdrücklich darauf hin, daß man auch an seinen Namen und an seinen Titel denken soll, wenn man sein Ich in der Vorstellung umfassen, umspannen soll."
      ],
      [
        "... .",
        "Ihre Hauptneigungen und dominierenden Vorstellungen und endlich an Ihre Vergangenheit, und damit selbst den Beweis führen, wie äußerst zusammengesetzt diese Ich-Vorstellung ist.",
        "Freilich redu­ziert der reflektierende Mensch diese Kompliziertheit der Ich-Vorstel­lung wieder auf eine relative Einfachheit, indem er den äußeren Objek­ten und anderen Ichs sein eigenes Ich als das Subjekt seiner Empfin­dungen, Vorstellungen und Bewegungen gegenüberstellt.",
        "Gewiß hat auch diese Gegenüberstellung und diese Vereinfachung der Ich-Vorstel­lung ihre tiefe erkenntnistheoretische Begründung, aber, rein psycho­logisch betrachtet, ist dieses einfache Ich nur eine theoretische Fiktion.»"
      ],
      [
        "Also «dieses einfache Ich» ist nur eine «theoretische Fiktion», das heißt eine bloße Phantasievorstellung, die sich aufbaut, wenn man sei­nen Namen, seine Titel, vermutlich auch seine Orden und andere der­gleichen Dinge zusammenstellt, die einem Gewicht geben!",
        "An solchen Punkten kann man die ganze Schwäche des heutigen Denkens erkennen.",
        "Und diese Schwäche muß um so mehr ins Auge gefaßt werden, weil ja dasjenige, was sich als entscheidende Schwäche für die Erkenntnis des seelischen Lebens erweist, eine Stärke ist für die Erkenntnis der äußeren naturwissenschaftlichen Tatsachen.",
        "Gerade was untauglich ist für die Erkenntnis des seelischen Lebens, ist sehr tauglich, um die äußere sinnen-fällige Tatsache in ihrer unmittelbaren äußeren Notwendigkeit zu durchschauen."
      ],
      [
        "Man muß sich nicht hinwegtäuschen darüber, daß es ein Charakte­ristikon unserer Zeit ist, daß Leute, die auf einem Gebiete groß sein können, auf dem andern Gebiete Vertreter des äußersten Unsinns sind.",
        "Nur wenn man diese Tatsache, die so sehr geeignet ist, der Menschheit Sand in die Augen zu streuen, scharf ins Auge faßt, dann kann man irgendwie mitdenken bei dem, was in Betracht kommt für die Wieder-aufrichtung jener Kraft, die die Menschheit braucht, um solche Vorstellungen"
      ],
      [
        "zu gewinnen, die fruchtbar und heilsam in das Leben ein­greifen können.",
        "Denn in dieses Leben, wie es heute ist, werden nur Vor­stellungen eingreifen, die tief aus der wahren Wirklichkeit heraus genommen sind, bei denen man sich nicht scheut, tief in die wahre Wirklichkeit hineinzugreifen.",
        "Davor aber scheuen sich gerade viele Menschen der Gegenwart."
      ],
      [
        "Die Menschen der Gegenwart finden sich sehr häufig geneigt, ohne erst hineingeschaut zu haben in die wahre Wirklichkeit, aus der sie ihre Impulse schöpfen sollten, die geistige Wirklichkeit zu reformieren.",
        "Wer reformiert heute nicht alles Mögliche in der Welt, das heißt, glaubt zu reformieren.",
        "Was holt man nicht alles aus dem reinen Nichts der Seele heraus!",
        "Aber in einer Zeit, wie diese ist, können nur diejenigen Dinge fruchtbar sein, welche aus der Tiefe der geistigen Wirklichkeit heraus selbst geholt sind.",
        "Dazu muß Wille vorhanden sein."
      ],
      [
        "Die Eitelkeit, die auf Grund des seelischen Nichts alle möglichen Reformgedanken fassen will, ist ebenso schädlich der Entwickelung in unserer heutigen Zeit wie der Materialismus selber.",
        "Ich habe gestern am Schluß darauf aufmerksam gemacht, wie das wahre Ich des Men­schen, dasjenige Ich, das allerdings der Willensnatur angehört, über das sich daher für das gewöhnliche Bewußtsein Schlaf breitet, befruchtet werden muß dadurch, daß schon durch den öffentlichen Unterricht die Menschen hingeführt werden zum konkreten Begreifen der großen Zeit-interessen.",
        "Das kann man nicht anders machen in unserer Zeit, als in­dem man klarmacht, welche geistigen Kräfte und Wirksamkeiten her-eingreifen in unser Geschehen.",
        "Nicht mit allgemeinen nebulosen Reden über den Geist ist es getan, sondern mit der Erkenntnis der konkreten geistigen Vorgänge, wie wir sie in diesen Betrachtungen geschildert haben, wo man per Jahrzahl darauf hinweist, wie da und dort diese gewissen Mächte und Kräfte aus der geistigen Welt hier in die physische hereingegriffen haben."
      ],
      [
        "Dadurch aber kommt das zustande, was ich bezeichnen konnte im Gesamtwerden der Menschheit als das Zusammenarbeiten der soge­nannten Toten mit den sogenannten Lebendigen.",
        "Denn im Wirklichen unseres Gefühls- und Willenslebens sind wir mit den Toten in einem Reich.",
        "Man kann ebensogut sagen, mit dem Wirklichen unseres Ich und"
      ],
      [
        "unseres astralischen Leibes sind wir mit den Toten in einem Reich.",
        "Beides besagt dasselbe.",
        "Dadurch aber ist hingewiesen auf ein gemein­sames Gebiet, in das wir eingebettet sind, in dem die Toten und die Lebendigen zusammenarbeiten an demjenigen Gewebe, das man das soziale, das sittliche, das geschichtliche Menschenleben in seiner Ganz­heit nennen kann, wozu auch diejenigen Lebensläufe gehören, die zwischen dem Tod und einer neuen Geburt zugebracht werden."
      ],
      [
        "Wir haben darauf hingewiesen in diesen Betrachtungen, wie der so­genannte Tote zwischen dem Tod und einer neuen Geburt als unterstes Reich das tierische Reich hat, so wie wir das mineralische Reich als unterstes Reich haben.",
        "Wir haben auch in einer gewissen Weise darauf hingewiesen, wie der Tote zu arbeiten hat innerhalb des Wesens des tierischen Reiches, wie er aufzubauen hat aus den Gesetzen der Tierheit dasjenige, was wiederum der nächsten Inkarnation als Organisation zugrunde liegt.",
        "Wir haben darauf hingewiesen, wie als zweites Reich der Tote alle diejenigen Zusammenhänge erlebt, die hier in der physi­schen Welt karmisch begründet worden sind, und die sich in die geistige Welt hinein entsprechend verwandelt fortsetzen.",
        "Ein zweites Reich baut sich auf also für den Toten, das zusammengewoben ist aus all den karmischen Zusammenhängen, die er jemals in einer Inkarnation auf der Erde begründet hat.",
        "Dadurch dehnt sich aber allmählich alles, was der Mensch an Interesse entwickelt zwischen dem Tod und einer neuen Geburt, man kann sagen, in Konkretheit über die ganze Menschheit aus."
      ],
      [
        "Als drittes Reich, das der Mensch dann durchlebt, können wir auf­fassen das Reich der Angeloi.",
        "Und wir haben auch schon in einem ge­wissen Sinne darauf hingewiesen, welche Rolle die Angeloi spielen drüben in dem Leben zwischen dem Tod und einer neuen Geburt.",
        "Sie tragen gewissermaßen die Gedanken von der einen menschlichen Seele zur andern menschlichen Seele hin und bringen sie wieder zurück.",
        "Sie sind die Boten des gemeinschaftlichen Gedankenlebens.",
        "Die Angeloi sind im Grunde genommen von den Wesen der höheren Hierarchien diejenigen, über die der Tote das klarste Erleben hat; ein klares Erleben über die tierischen und ein klares Erleben über die menschlichen Zu­sammenhänge, das sein Karma begründet hat durch die Wesen der höheren Hierarchien.",
        "Die klarste Vorstellung hat er von jenen Wesen"
      ],
      [
        "aus der Hierarchie der Angeloi, die eigentlich die Träger der Gedanken beziehungsweise überhaupt der Seeleninhalte von einem Wesen zu dem andern sind, die auch dem Toten helfen beim Bearbeiten der Tierheit.",
        "Man könnte sagen - wenn man von den Angelegenheiten der Toten als von persönlichen Angelegenheiten spricht -, die Wesen aus der Hierar­chie der Angeloi haben sich vorzugsweise zu bestreben, die persönlichen Angelegenheiten der Toten zu besorgen.",
        "Allgemeinere Angelegenheiten der Toten, die nicht persönliche sind, werden mehr besorgt von den Wesen aus dem Reich der Archangeloi und der Archai."
      ],
      [
        "Wenn Sie sich erinnern an den Vortragszyklus über «Inneres Wesen des Menschen und Leben zwischen Tod und neuer Geburt», dann wer­den Sie in Ihr Gedächtnis zurückrufen, daß es zum Leben des sogenann­ten Toten gehört, abwechselnd gewissermaßen sein Wesen auszudehnen über die Welt und es wieder zusammenzuziehen in sein Inneres.",
        "Ich habe das dort tiefer begründet und geschildert."
      ],
      [
        "Das Leben des Toten ver­läuft so, daß gewissermaßen eine Art Abwechselung stattfindet zwi­schen Tag und Nacht.",
        "Aber diese Art ist so, daß aus dem Innern auf-taucht reges Leben.",
        "Man weiß: Was da auftaucht, dieses rege Leben, das ist nur das Wiederauftauchen dessen, was man in dem andern Zu­stande, mit dem dieser abwechselt, durchlebt hat, indem man sein Wesen ausgedehnt hat über die Welt, indem man zusammengewachsen ist mit der Außenwelt."
      ],
      [
        "Wenn man daher mit einem Toten zusammen-kommt, trifft man abwechselnde Zustände: Solche Zustände, wo er sein Wesen über die Welt ausdehnt, wo er gewissermaßen mit seinem eigenen Wesen in die Wesenhaftigkeit seiner Umgebung, in die Vorgänge seiner Umgebung hineinwächst.",
        "Da weiß er am wenigsten, da ist für ihn eine Art von Schlafzustand vorhanden, wenn er mit seinem Wesen in die geistige Welt um ihn hineinwächst."
      ],
      [
        "Wenn das wieder auftaucht aus sei­nem Innern, dann ist für ihn eine Art Wachzustand vorhanden, dann weiß er alles das.",
        "Denn sein Leben verfließt in der Zeit, nicht im Raume.",
        "Wie wir als Besitzer des wachen Tagesbewußtseins draußen im Raume dasjenige haben, was wir hereinnehmen in unser Bewußtsein und dann wiederum uns von ihm zurückziehen im Schlafe, so ist es beim Toten so, daß er von einem gewissen Zeitraume, den er durchlebt hat, die Erlebnisse hereinnimmt in den nächsten Zeitraum und sie dann sein"
      ],
      [
        "Bewußtsein ausfüllen.",
        "Vergangene Zeit füllt sein Bewußtsein aus, wie unser Wachbewußtsein der Raum ausfüllt.",
        "Es ist ein völliges Leben in der Zeit.",
        "Und damit muß man sich bekanntmachen."
      ],
      [
        "Durch dieses rhythmische Zeitleben, das der Tote führt, kommt er nun in eine ganz bestimmte Beziehung zu den Wesen aus der Hierarchie der Archangeloi und der Archai.",
        "Von diesen Wesenheiten, von den Archangeloi und den Archai, hat er nicht eine so klare Vorstellung wie von den Angeloi und von den Menschen und von der Tierheit, aber er hat vor allen Dingen immer die Vorstellung, daß diese Wesenheiten, die Archai und Archangeloi, diejenigen sind, welche mit ihm zusammen­arbeiten in diesem Aufwachen, Einschlafen, Aufwachen, Einschlafen -in diesem Rhythmus, der sich im Laufe der Zeit abspielt.",
        "Der Tote hat -wenn er dazu kommt, ein Bewußtsein von dem zu entwickeln, was er im vorhergehenden Zeitabschnitt erlebt, aber nicht gewußt hat -, er hat immer das Bewußtsein, daß ein Wesen aus der Hierarchie der Archai ihn aufgeweckt hat; er hat immer das Bewußtsein, daß er in bezug auf dieses rhythmische Leben zusammenarbeitet mit den Archai und Arch­angeloi."
      ],
      [
        "Halten wir recht gut fest, geradeso wie wir hier im Aufwachen ge­wahr werden: uns wird bewußt die äußere Welt, von der wir während des Schlafens nicht wissen, wie wir hier gewahr werden: diese äußere Welt geht in die Finsternis hinunter, wenn wir einschlafen - so lebt in der Seele des sogenannten Toten das Bewußtsein: Archai, Archangeloi, mit ihnen arbeite ich zusammen, auf daß ich durchgehen kann durch dieses Leben des Einschlafens, Aufwachens, Einschlafens, Aufwachens und so weiter.",
        "Man möchte sagen, der Tote verkehrt mit Archangeloi und Archai so, wie wir hier im Wachbewußtsein mit der physischen Umgebung, der Pflanzen- und mineralischen Welt verkehren.",
        "Der Mensch kann nicht zurückschauen in dieses Zusammenspielen, in das er hineinverwoben ist zwischen dem Tod und einer neuen Geburt.",
        "Warum nicht?",
        "Nun, man meint: Warum nicht? - aber gerade dieses Zurück­schauen ist etwas, was der Mensch wird lernen müssen, nur kann er es freilich aus den materialistischen Vorstellungen der Gegenwart heraus schwierig lernen.",
        "Ich möchte Ihnen graphisch darstellen, warum da der Mensch nicht zurücksieht (Siehe Zeichnung)."
      ],
      [
        "# Bild s. 131"
      ],
      [
        "Nehmen Sie einmal an: Sie stehen mit Ihrem gesamten Sinnes- und Vorstellungsapparat der Welt gegenüber.",
        "Dadurch haben Sie Vorstel­lungen, Wahrnehmungsinhalte verschiedenster Art.",
        "Ich bezeichne das, was in einem Momente Bewußtsein ist, so, daß ich da verschiedene Ringe, kleine Kreise aufzeichne."
      ],
      [
        "Das ist in einem Momente im Bewußt­sein.",
        "Jetzt wissen Sie, findet in anderer Art, als Psychologen heute meinen, aber es findet statt ein Erinnerungsprozeß, wenn Sie zurück­schauen; und die Zeit, in die Sie zurückschauen können, indem Sie sich erinnern, die bezeichne ich mit dieser Linie, mit der aber eigentlich die­ser Raum gemeint ist, der da blind ausläuft, hier wäre der Punkt im dritten, vierten oder fünften Jahre, bis zu dem man sich im Leben zurückerinnert."
      ],
      [
        "Da drinnen liegen also alle die Vorstellungen, die ent­stehen, wenn man sich an die Erlebnisse zurückerinnert, die man gehabt hat.",
        "Nehmen Sie an: Sie haben diese Vorstellungen, sagen wir mit drei­ßig Jahren, so erinnern Sie sich, indem diese Vorstellungen vor Ihnen auftauchen, an etwas, das Sie vor zehn Jahren gehabt haben."
      ],
      [
        "Wenn Sie sich so recht lebhaft, bildhaft vorstellen, wie das eigentlich ist mit der Seele, so können Sie folgendes denken.",
        "Sie können sich sagen: Wenn wir so zurückschauen bis dahin, wo in der Kindheit dasjenige auftaucht, bis wohin wir uns erinnern, so ist das ein seelischer Sack, der ein Ende hat; er hat dort seinen Bogen, wo der Punkt liegt, bis zu dem wir uns in der Kindheit zurückerinnern."
      ],
      [
        "Das ist ein solcher Seelensack; das ist die Zeit, die überschaut wird.",
        "Stellen Sie sich solch einen seelischen Sack"
      ],
      [
        "vor, in den Sie so zurück hineinblicken: hier ist die Grenze dieses Sackes, diese Grenze fällt in Wirklichkeit zusammen mit der Grenze zwischen Ätherleib und physischem Leib.",
        "Diese Grenze muß da sein, Sie können sich das sehr grob vorstellen: sonst würden nämlich die Vorgänge, welche die Erinnerung herbeiführen, immerfort da durchfallen.",
        "Sie würden sich an nichts erinnern können, die Seele wäre ein Sack, der keinen Boden hat, es würde alles durchfallen.",
        "Es muß also eine Grenze da sein, es muß ein wirklicher seelischer Sack vorliegen.",
        "Dieser seelische Sack aber hindert zu gleicher Zeit, auch dasjenige wahrzunehmen, was man so durchlebt hat, daß es außerhalb liegt.",
        "Sie sind sich selbst in Ihrem Seelenleben undurchsichtig, weil Sie Erinnerungen haben.",
        "Weil Sie das Vermögen der Erinnerung haben, sind Sie undurchsichtig."
      ],
      [
        "Sie sehen, das, was macht, daß wir ein ordentliches Bewußtsein für den physischen Plan haben, ist zu gleicher Zeit der Grund, daß wir nicht hineinsehen mit dem gewöhnlichen Bewußtsein in dieses Gebiet, welches hinter der Erinnerung liegen müßte.",
        "Hinter der Erinnerung liegt es nämlich in Wirklichkeit."
      ],
      [
        "Man kann sich aber bemühen, die Er­innerung nach und nach etwas umzugestalten.",
        "Man muß nur vorsichtig dabei sein.",
        "Man kann damit beginnen, daß man versucht, dasjenige, an das man sich erinnert, immer genauer und genauer meditativ ins Auge zu fassen, bis man das Gefühl hat: Es ist nicht nur etwas, was man so in der Erinnerung ergreift, sondern etwas, was eigentlich da stehen bleibt."
      ],
      [
        "Ein Mensch, der ein intensives, reges Geistesleben entwickelt, bekommt schon allmählich dieses Gefühl, daß die Erinnerung nicht etwas ist, das kommt und geht, kommt und vergeht, sondern daß der Inhalt der Erinnerung etwas ist, was stehen bleibt.",
        "Nun allerdings, in dieser Weise arbeiten, kann nur dazu führen, die Cberzeugung hervor­zurufen, daß dasjenige, was in der Erinnerung sonst auftaucht, stehen bleibt, daß es wirklich als Akasha-Chronik vorhanden bleibt, daß es nicht weggeht."
      ],
      [
        "Dasjenige, was wir sonst in der Erinnerung überblicken: es steht da in der Welt, es ist in Wirklichkeit da.",
        "Aber weiter kommt man durch diese Methode eigentlich nicht, denn diese Methode, sich nur an seine persönlichen Erlebnisse zu erinnern, die gut hervorgerufen wird, die Erkenntnis, daß der Erinnerungsgehalt stehen bleibt - diese Methode ist in einem höheren Sinne zu egoistisch, um weiterzuführen"
      ],
      [
        "als nur bis zu dieser Überzeugung.",
        "Im Gegenteil, wenn Sie über einen gewissen Punkt hin gerade diese Fähigkeit ausbilden würden, hinzu-schauen auf das Stehenbleibende Ihrer eigenen Erlebnisse, so werden Sie sich erst recht den Ausblick in die freie Geisteswelt verbauen.",
        "Denn statt daß der Sack der Erinnerungen da ist, steht dann nur Ihr eigenes Leben um so kompakter da und läßt Sie nicht durchblicken."
      ],
      [
        "Dagegen kann man eine andere Methode anwenden, die in ganz aus­gezeichneter Weise, wenn ich den Ausdruck gebrauchen darf, die Ein-schreibungen der Akasha-Chronik durchsichtig macht.",
        "Und sieht man einmal durch die stehengebliebenen Erinnerungen, dann sieht man sicher hinein in die geistige Welt, mit der man verbunden war zwischen dem Tod und einer neuen Geburt.",
        "Aber dazu muß man nicht nur das­jenige, was als erinnerungsgemäß stehen bleibt aus dem eigenen Leben, benützen - das wird immer kompakter und kompakter, da sieht man dann erst recht nicht durch.",
        "Es muß das durchsichtig werden.",
        "Und durchsichtig wäre es, wenn man immer stärker und stärker den Ver­such macht, nicht so sehr an das sich zu erinnern, was man von seinem Gesichtspunkte aus erlebt hat, sondern an das sich immer mehr zu er­innern, was von außen an einen herangetreten ist.",
        "Statt an das, was man gelernt hat, erinnert man sich an den Lehrer, an die Art, wie der Lehrer gesprochen, wie der Lehrer gewirkt hat, was der Lehrer mit einem gemacht hat.",
        "Man erinnert sich daran, wie das Buch entstanden ist, aus dem man dies oder jenes gelernt hat.",
        "Man erinnert sich vorzugs­weise an dasjenige, was von der Außenwelt herein an einem gearbeitet hat."
      ],
      [
        "Ein sehr schöner, wunderbarer Anfang, ja eine Anleitung zu solcher Erinnerung ist Goethes Schrift «Dichtung und Wahrheit», wo er schil­dert, wie er, Goethe, aus der Zeit heraus geformt wird; wie die ver­schiedenen Kräfte an ihm arbeiten.",
        "Daß Goethe so etwas gemacht hat in seinem Leben, daß er in einer solchen Weise eine Art Rückschau ge­halten hat, nicht von dem Gesichtspunkte der eigenen Erlebnisse, son­dern von dem Gesichtspunkte der andern und der Zeitereignisse, die an ihm gearbeitet haben, dem verdankt er, daß er solche tiefen Einblicke hat tun können in die geistige Welt, wie er getan hat.",
        "Das aber ist auch zu gleicher Zeit der Weg, um in weiterem Umfange mit der Zeit in"
      ],
      [
        "Berührung zu kommen, die zwischen dem letzten Tode und dieser un­serer Geburt verflossen ist."
      ],
      [
        "Also Sie sehen, von einem andern Gesichtspunkt aus weise ich Sie heute auf dasselbe hin, worauf ich Sie schon hingewiesen habe: Erwei­terung der Interessen über das Persönliche hinaus, gerade Hinlenkung der Interessen und der Aufmerksamkeit auf dasjenige, was nicht wir sind, sondern was uns geformt hat, woraus wir entstanden sind.",
        "Ein Ideal ist es, hinzuschauen auf die Zeit und auf längere Vorzeit vor uns und all die Kräfte aufzusuchen, die diesen Kerl, der man geworden ist, aus sich heraus geformt haben."
      ],
      [
        "Das allerdings bietet wenig Schwierigkeiten, wenn man es so schil­dert, aber es ist keine ganz leichte Aufgabe.",
        "Es ist auch eine Aufgabe, die, weil sie starke Selbstlosigkeit erfordert, großen Erfolg hat.",
        "Gerade diese Methode erweckt die Kräfte, mit seinem Ich in dieselbe Sphäre hineinzukommen, die die Toten mit den Lebendigen gemeinschaftlich haben.",
        "Weniger sich kennenzulernen, mehr seine Zeit kennenzulernen, das wird die Aufgabe eines öffentlichen Unterrichts in einer gar nicht zu fernen Zukunft sein, aber seine Zeit im Konkreten kennenzulernen, nicht so kennenzulernen, wie es jetzt in den Geschichtsbüchern steht; so, wie diese Zeit selbstverständlich sich entwickelt aus geistigen Im­pulsen heraus."
      ],
      [
        "Also wieder werden wir auch auf diese Weise dazu geführt, die In­teressen zu erweitern über eine Charakteristik unseres Zeitalters und seines Hervorgehens aus dem allgemeinen Weltengang.",
        "Warum hat denn Goethe so intensiv danach gestrebt, griechische Kunst kennenzu­lernen, seine Zeit durch und durch zu verstehen, sie abzumessen an der vorhergehenden Zeit?",
        "Warum läßt er seinen Faust bis in die griechische Zeit, bis in die Helena-Zeit zurückgehen, den Chiron aufsuchen, die Sphinxe aufsuchen?",
        "Weil er seine eigene Zeit, wie sie an ihm gearbeitet hat, so kennenlernen will, wie er sie nur kennenlernen kann, wenn er diese eigene Zeit an der früheren Zeit mißt.",
        "Aber Goethe läßt seinen Faust nicht sich hinsetzen und Pergamente entfalten, Urkunden der Staatsarchive entfalten, sondern er führt ihn zurück auf Seelenwegen in die Impulse, welche ihn selber geformt haben.",
        "Es steckt in ihm man­ches von dem, was den Menschen hinweist auf ein Zusammenkommen"
      ],
      [
        "auf der einen Seite mit den Toten, auf der andern Seite - Sie können es jetzt sehen aus dem Zusammenhang der Toten und Archangeloi - mit den Zeitgeistern und den Erzengeln.",
        "Dadurch, daß der Mensch mit den Toten zusammenkommt, kommt er auch in Berührung mit den Erz-engeln und den Zeitgeistern.",
        "Gerade in den Impulsen, auf die Goethe in seinem «Faust» hindeutet, liegt das, wodurch der Mensch seine Inter­essen erweitert über den Zeitgeist, liegt das, was im eminentesten Sinne unserer Zeit notwendig ist.",
        "Allerdings ist unserer Zeit notwendig, in anderer Art auf so etwas hinzuschauen, wie es zum Beispiel der «Faust» ist, als die Zeit bisher darauf hingeschaut hat.",
        "Die meisten derjenigen, die den «Faust» beurteilen, kommen kaum darauf, wo die Probleme liegen.",
        "Einige kommen darauf, die Fragen zu stellen.",
        "Die Antworten werden oft in der kuriosesten Weise gegeben."
      ],
      [
        "Nehmen Sie ein Beispiel, wo Goethe nun wirklich darauf hinweist:"
      ],
      [
        "Denkt nach!",
        "Wird da immer nachgedacht?",
        "Goethe macht aber alles, um Deutlichkeit dafür hervorzurufen, daß über gewisse Dinge nachzu­denken ist.",
        "Zum Beispiel: Sie wissen, die Erichtho redet über dasjenige, was Schauplatz der klassischen Walpurgisnacht ist; sie entfernt sich, die Luftfahrer, Homunkulus mit Faust und Mephistopheles erscheinen.",
        "Sie erinnern sich an die ersten Reden des Homunkulus, des Mephisto, des Faust.",
        "Nachdem Faust den Boden berührt hat und die Frage auf­geworfen hat: Wo ist sie? - sagt Homunkulus:"
      ],
      [
        "Wüßten's nicht zu sagen,"
      ],
      [
        "Doch hier wahrscheinlich zu erfragen."
      ],
      [
        "In Eile magst du, eh' es tagt,"
      ],
      [
        "Von Flamm' zu Flamme spürend gehen:"
      ],
      [
        "Wer zu den Müttern sich gewagt,"
      ],
      [
        "Hat weiter nichts zu überstehen."
      ],
      [
        "Homunkulus sagt: «Wer zu den Müttern sich gewagt, hat weiter nichts zu überstehen . . . » Woher weiß denn der, daß der Faust bei den Müttern war?",
        "Das ist eine Frage, die ganz notwendig sich ergibt, denn blättern Sie zurück, so werden Sie sehen, daß nirgends eine Andeutung darüber ist, daß Homunkulus erfahren haben könnte als ein Wesen außer dem Faust, daß der Faust bei den Müttern war.",
        "Jetzt auf einmal piepst der"
      ],
      [
        "Homunkulus davon, daß «wer zu den Müttern sich gewagt, hat weiter nichts zu überstehen».",
        "Sie sehen, Goethe gibt schon Rätsel auf.",
        "Mit zwingender Notwendigkeit geht daraus hervor, daß Homunkulus, wenn er überhaupt irgend etwas ist, dieses innerhalb des Bewußtseins-bereiches des Faust selber ist; denn nur dann kann er dasjenige, was innerhalb des Bewußtseinsbereiches des Faust ist, wissen, wenn er zum Bewußtseinsbereiche des Faust selber gehört."
      ],
      [
        "Erinnern Sie sich an manche Auseinandersetzungen, die wir über den «Faust» gegeben haben, daß Homunkulus eigentlich nichts anderes ist als dasjenige, was als astralischer Leib bereitet werden muß, damit die Helena crscheinen kann.",
        "Aber dadurch ist er in einem andern Be­wußtsein, ist sein Bewußtsein erweitert über den Astralleib.",
        "Dann haben Sie eine Verständnismöglichkeit des Wissens des Homunkulus, wenn er in den Bewußtseinsbereich des Faust selber hineinkommt.",
        "Deshalb läßt Goethe den Homunkulus werden, weil durch das Werden des Homun­kulus das Bewußtsein des Faust gewissermaßen die Möglichkeit findet, aus sich herauszugehen, nicht nur in sich zu sein, sondern draußen zu sein.",
        "Und er ist auch da, wo der Homunkulus ist; der Homunkulus ist im Bewußtsein des Faust darinnen."
      ],
      [
        "Goethe nimmt in diesem Sinne Alchimie sehr ernst, wie Sie sehen.",
        "Solche Rätsel, die direkt mit Geheimnissen der geistigen Welt zusam­menhängen, sind im «Faust» sehr viele.",
        "Man muß den «Faust» so auf sich wirken lassen, daß man gewahr wird, welche Tiefen geistiger Wirklichkeit eigentlich diesem «Faust» zugrunde liegen.",
        "Nur dadurch versteht man so jemanden wie Goethe, daß jnan sich klarmacht: Er hat auf der einen Seite getrachtet, das, was ihn gemacht hat, wirklich wie von außen anzusehen, wofür ein Beweis seine Darstellung in «Dichtung und Wahrheit» ist, und hat auf der andern Seite auch gewußt, das führt zurück sogar in weite perspektivische Zusammenhänge mit den Toten.",
        "Und Faust tritt in das Leben sehr weit zurückliegender Menschen-entwickelung ein, tritt auch in das Leben weit zurückliegender geistiger Wesenheiten ein."
      ],
      [
        "Aber, wenn man ganz durchschauen will, was nötig ist in positivem Sinne für die Gegenwart, dann muß man in vieler Beziehung auch einen Blick und ein Gefühl für das Negative haben, muß das richtige"
      ],
      [
        "Fühlen entwickeln für das Negative.",
        "Man muß einen Blick haben für alles das, was verhindert das als notwendig bezeichnete Zusammen­kommen der lebenden Menschen im gemeinsamen Plane mit dem Wir­ken der Toten.",
        "Überall können Sie heute die Hindernisse entdecken.",
        "Sie finden sie auf Schritt und Tritt.",
        "Sie finden sie gerade dort, wo Bil­dung - verzeihen Sie, daß ich dieses häßliche Wort gebrauche - heute verbreitet wird."
      ],
      [
        "Wie fühlt sich ein Mensch heute geradezu gescheit, tief gescheit, auf­geklärt, wenn er dergleichen hinschreiben kann: «Swedenborg, um dessen finster-rätselvolle Persönlichkeit auch Goethe mit ehrfürchtigem Tasten herumgewandert ist, hat mit den Engeln jenseits der Erde ver­kehrt.",
        "Erzählt hat er, daß diese überirdischen Geschöpfe, mit Gedanken streitend, sogar mit Gewändern bekleidet einhergehen."
      ],
      [
        "Das Ringen um Erkenntnis und Aufklärung sei ihnen nicht fremd, haben sie doch eine Druckerei eingerichtet, von der sie manchmal zu besonders glücklichen Menschen einige Blätter hinabschicken.",
        "Mit hebräischen Buchstaben sind die Zeitungen des Jenseits dann bedeckt."
      ],
      [
        "Ein Eigentümliches der ehrwürdigen biblischen Bilderzeichen wäre es, daß jeder Strich an ihnen, jede Kante, jede Biegung, einen geheimnisvollen Geisteswert verberge.",
        "Nur lernen müsse der Mensch, das Engelsgeschnörkel richtig zu lesen, damit er in die Wahrheit des Jenseits, in das abgekehrte, ewig besonnte Leben, in die beseligende Festlichkeit und das erheiternde Paradies des Jenseits eingeweiht werde."
      ],
      [
        "Swedenborg, dem es gelang, bei lebendigem Leibe manchmal für das irdische Leben abzusterben und vor dem körperlichen Tode schon den Aufschwung in das Jenseits zu vollführen, hat vieles von den Engeln erfragt und über sie berichtet.",
        "Jahrhunderte vor ihm haben Babylonier, Ägypter und Juden das gleiche Kundschafterhandwerk geübt."
      ],
      [
        "Menschenalter nach ihm, bis zum heu­tigen Tage noch, tun es die auf der Erde unzufriedenen Wesen, die sich über ihre Zukunft von Gott Rates holen wollen, die auf die Gesellschaft ihrer Toten nicht verzichten, und die endlich der Meinung sind, die Brücke, die von ihrem träumeumspielten Bett bis in die Bezirke des Unfaßbaren gebaut wird, sei ein fester, seraphisch zementierter, von Geistern durchaus gestählter und getragener Weg.»"
      ],
      [
        "Und so setzt der betreffende, sich sehr gescheit haltende Mensch"
      ],
      [
        "seine Betrachtungen fort, sich in einem billigen Spott über diejenigen ergehend, die da versuchen, die Brücke zu schlagen in das Jenseits; denn dieser sehr gescheite Mann hat das Buch eines andern sehr gescheit sich dünkenden Menschen gelesen und schreibt darüber: «Dieses Jenseits der Sinne, das von der Seele bewohnt wird, will das gewichtige Buch Max Dessoirs: neu beschreiben, nachdem schon tausende von Grüblern diesen Weg ins Jenseits betreten haben.",
        "Diesmal redet also ein Philosoph, der sich um Menschenkenntnis mehr bemüht hat als um die Sonderung verwaister Gedankenrichtungen, ein Kunst-freund, der sich nicht gescheut hat, die Rätsel-umschattete Geburts­sekunde eines Künstlerplanes auszudeuten, ein Mann endlich, der ge­legentlich auch mit dem Messer in der Hand Knochen und Nerven des Menschen abgesucht hat, damit er sich in den zahlreichen irdischen Verstecken der Seele zurechtfindet."
      ],
      [
        "Weil Dessoir so vielfältig gegen die Übereilung der Schwarmgeister und gegen die Kälte der hochmütigen Vernünftler geschützt ist, ver­dient sein seit mehr als dreißig Jahren vorbereitetes Urteil über Dinge des Jenseits auch bei jenen Achtung und Gehör, die ihm nicht auf sei­nem Wege folgen können» und so weiter."
      ],
      [
        "Jenes besagte Individuum Max Dessoir mußte ich besprechen in dem zweiten Kapitel meines Buches: «Von Seelenrätseln», denn dieser Uni­versitätsprofessor hatte die Frechheit, die Anthroposophie als solche zu besprechen.",
        "Ich mußte mich der Aufgabe unterziehen, nachzuweisen, daß die ganze Art, wie Max Dessoir arbeitet, die gewissenloseste, ober­flächlichste Art ist, die sich nur denken läßt.",
        "Dieser Mann hat die Stirne, auf fast ausschließlich blödsinnig geformte Zitate hin, die er aus wenigen meiner Bücher ausschreibt und immer so ausschreibt, daß sie in der blödsinnigsten Weise entstellt sind, ein abfälliges Urteil zu fällen.",
        "Man muß schon die Tatsache in dieser Form hinstellen, wenn man jenen Skandal in Wirklichkeit sehen will, der möglich ist innerhalb des­jenigen, was sich heute vielfach Wissenschaft nennt.",
        "Ich habe das Indi­viduumDessoir in meinem Leben nur einmal gesehen; es war im Anfang der neunziger Jahre.",
        "Damals hat er mir eine sehr gescheite Bemerkung gemacht.",
        "Meine «Philosophie der Freiheit» war damals noch nicht ge­schrieben.",
        "Max Dessoir sagte dazumal - es war bei einem Goethe-Diner"
      ],
      [
        "in Weimar: «Ja, Sie haben allerdings einen Fehler, Sie beschäftigen sich mit zu vielerlei Wissenschaften.» Das war der große Fehler, daß man versuchte, nicht einseitig zu sein!"
      ],
      [
        "Unter den andern Blödsinnigkeiten, die Max Dessoir in seinem Buche begeht, ist zum Beispiel auch diese, daß er jetzt von meiner «Philosophie der Freiheit» als von meinem «Erstling» spricht.",
        "Der ist zehn Jahre ungefähr nach meinem wirklichen Erstling geschrieben; eine zehn-jährige Schriftstellerlaufbahn liegt vor der «Philosophie der Freiheit».",
        "Das alles und vieles andere ist ganz gleich erlogen in dem Dessoir-Buch.",
        "Wie viele Leute werden die notwendig gewordenen, sachlichen Aus­einandersetzungen, die zeigen, welche Windbeutelei Dessoirs Wissen­schaft ist, wie viele Leute werden diese sachlichen Auseinandersetzun­gen in meinem Buche «Von Seelenrätseln» lesen!",
        "Wie vielesJournalisten­geschmeiß von der Sorte von Max Hochdorf in Zürich findet sich aber zusammen, um das unsinnige Buch Max Dessoirs «Vom Jenseits der Seele» hinauszuposaunen in der Art, daß man sagt, «Dieses Jenseits der Sinne, das von der Seele bewohnt wird, will das gewichtige Buch Max Dessoirs: neu beschreiben, nachdem schon tausende von Grüblern diesen Weg ins Jenseits betreten haben» und so weiter."
      ],
      [
        "Auf solche Dinge ist es notwendig den Blick zu richten.",
        "Es ist ja sattsam bekannt, daß dasjenige, was auf dem Boden der anthroposo­phisch orientierten Geisteswissenschaft versucht wird, in beispiellosester Weise da und dort entstellt wird; zuweilen von Leuten, die sehr gut wissen, daß das Gegenteil von dem wahr ist, was sie sagen.",
        "Allein das sind zum großen Teil arme Hascherln, die innerhalb der Gesellschaft ihre persönlichen Interessen nicht befriedigen konnten, die sie befrie­digen zu können glaubten, und mit denen man ja Mitleid haben kann, über die man nicht weiter zu reden braucht.",
        "Und die wissen selbst am besten, wie es mit der objektiven Wahrheit dessen steht, was sie sagen.",
        "Aber solches Gift, wie das von Max Dessoir verbreitete, das ist aller­dings ernster zu nehmen, und ich mußte schon das Meinige tun, um gewissermaßen Satz für Satz die ganze philosophische Nichtswürdig­keit der Dessoirschen Auseinandersetzungen klarzulegen.",
        "Ehe nicht in weitesten Kreisen ein gesundes Urteil über solche angebliche Wissenschaftelei"
      ],
      [
        "herrscht wie die eines Max Dessoir - und solche Max Dessoirs gibt es sehr viele - und so lange nicht ein gesundes Urteil herrscht über solche Schleppenträger der Max Dessoirei, wie zum Beispiel dieser Artikelschreiber ist, der sich natürlich dann nicht entwehren kann, seinen Artikel zu schließen mit den Worten: «Weil eben der Weg in das Jenseits so vollkommen versperrt ist» - natürlich, für das verbaute Ge­hirn dieses Herrn Max Dessoir ist der Weg in das Jenseits versperrt! -«haben die Menschen in den Jahrtausenden immer wieder versucht, die Schranken zu sprengen.» «Magische Idealisten» nennt Dessoir diese Kämpfer um das verzweifelt feste und doch gar nicht greifbare Geister-reich.",
        "Er führt sie alle heran, diese Gesundbeter, Zahlenapostel, ägyp­tischen Zauberer, Negerheiligen, Anthroposophen, Neubuddhisten, Kabbalisten . . .",
        "Er ist ein höchst fesselnder Geschichtsschreiber all der dem Wunder unterworfenen, all der dem Wunder trotzdem aufsässigen Geschlechter.",
        "«Es verbrüdert sich eine eigentümliche Gesellschaft, wenn man alle Männer, die Weisen und die Narren, aufzählt, die sich um den reinen Geist versammeln wollten.",
        "Cagliostro und Kant, Hegel und auch der moderne Hexenmeister Svengali begegnen da einander, wenn sie sich lustwandelnd auf dem Wege ins Jenseits verlieren.»"
      ],
      [
        "Zu verhindern, daß es Menschen gibt, die in dieser Weise schreiben, ist natürlich nicht möglich, aber in weitesten Kreisen muß ein gesundes Urteil Platz greifen, welches verhindert, daß dasjenige, was auf diesem Wege in die Öffentlichkeit kommt, autoritativ hingenommen wird.",
        "Denn selbstverständlich, Gedankenformen von dieser Art, herum­sprühend in unserem sozialen Organismus, verhindern jede Möglichkeit eines heilsamen Fortschrittes der Menschheit.",
        "Für sich selber kann man sich, wenn man wissenschaftlichen Unrat wie den Max Dessoirschen hat angreifen müssen, die Hände waschen und kann sich damit be­friedigt erklären.",
        "Aber dieser wissenschaftliche Unrat fließt und fließt, und es sind heute der Wege allzu viele, auf denen dieser Unrat fließen kann.",
        "Man muß schon manchmal ein Beispiel annageln.",
        "Es mußte in diesem Falle wiederum geschehen, weil Sie sich ja ausrechnen können, in wie viele Menschenköpfe nun wiederum einmal unter andern auch ein Urteil über die Anthroposophie hineingetrichtert wird, wenn ein solches Feuilleton wie das vom 14.",
        "Dezember 1917 in der «Neuen Zürcher"
      ],
      [
        "Zeitung» erscheint, von einem Menschen, der als ein ganz gescheiter auf einem ebensolchen gescheiten, nämlich auf Max Dessoir, fußt!"
      ],
      [
        "Diese Dinge muß man als kulturhistorische Fakta ins Auge fassen, muß ihre kulturhistorische Bedeutung ins Auge fassen.",
        "Gewiß, es ist nur eine geringfügige Möglichkeit leider heute noch vorhanden, so etwas wie dieses Kapitel, das ich geschrieben habe: «Max Dessoir über An­throposophie», unter die Menschen zu bringen."
      ],
      [
        "Denn auch in der An­throposophischen Gesellschaft ist ja nur ein kleiner Kreis, der seine Aufgabe wirklich versteht: die Aufgabe, die Menschheit aufzuklären über die Art und Weise, wie heute oftmals Wissenschaft gemacht wird, aufzuklären in der richtigen und rechtmäßigen Weise.",
        "Und das, was heute als Wissenschaft gemacht wird, das ist aber nur ein Symptom für allgemeines Denken."
      ],
      [
        "Denn so, wie es in der Wissenschaft bestellt ist -wofür Max Dessoir ein schreiendes Beispiel ist mit all seinen Traban­ten -, so ist es auch auf andern Gebieten bestellt.",
        "Und wenn Sie die Frage aufwerfen: Was hat in die heutige Katastrophe an tieferen Kräf­ten hineingeführt? - bleiben Sie immer an der Oberflächenansicht, wenn Sie nicht auf diese tieferen Gründe eingehen, auf dasjenige, was in der Verrenktheit, in der gesuchten Verrenktheit und in der gesuchten Oberflächlichkeit, Scharlatanerie liegt, eine Scharlatanerie, die sich da­durch zu erhalten sucht, daß sie ernste Geistigkeit gerade der Scharla­tanerie zuschreibt."
      ],
      [
        "Das muß in gesundem Sinne in seiner wahren Ge­stalt durchschaut werden.",
        "Ich führe das Beispiel von Max Dessoir nur aus dem Grunde an, weil es eben gerade naheliegt.",
        "Aber es ist ein Bei­spiel für vieles, was als Negatives in unserer Zeit existiert."
      ],
      [
        "Will einer in der Menschheit ein Herz haben für das Positive des Zusammen­wachsens mit der geistigen Welt, dann muß er auch ein Herz haben zum Abweis, zum starken, herzhaften Abweis, wo es nur sein kann, des Unechten, des Oberflächlichen, des Nichtsnutzigen."
      ],
      [
        "Erleben wir es ja geradezu in unseren Tagen, daß oftmals diejenigen, die auch im öffentlichen Leben am schlimmsten hingestellt werden, gerade die Anständigsten sind.",
        "Es gibt nicht die Notwendigkeit, mit Pessimismus nach diesen Dingen zu blicken, aber es gibt die Notwen­digkeit, in seiner eigenen Seele Kräfte aufzusuchen, die ein gesundes Urteil über diese Dinge in dieser Seele erzeugen und heranzüchten."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "ACHTER VORTRAG Dornach, 22. Dezember 1917",
    "paragraphs": [
      "Es scheint, daß es gut sein könnte gerade in der Gegenwart, im gegen­wärtigen Zeitpunkt unserer Betrachtung etwas zurückzublicken auf Verschiedenes, das im Laufe dieser Auseinandersetzungen durch unsere Seelen gegangen ist, zurückzublicken allerdings nicht in wiederholen-der Weise, sondern in orientierender Weise, wiederum von einem ge­wissen Gesichtspunkt aus die Dinge beleuchtend. Denn die Betrach­tungen, die wir in dieser Zeit angestellt haben, und die sich in einer gewissen Art angeschlossen haben an das, was wir durch die Vorjahre vor unsere Seele haben treten lassen, sie sollen vor allen Dingen neben den positiven Mitteilungen, die sie enthalten, dazu geeignet sein, in dieser ernsten Zeit unsere Seele mit solchen Gedanken zu erfüllen, wie sie eben von der menschlichen Seele gebraucht werden in dieser Zeit, einer Zeit, von der man sagen muß, daß sie zu dem Ernstesten der welt-geschichtlichen Entwickelung gehört. Wir stehen, trotzdem wir man­cherlei im Laufe der letzten Jahre mitgemacht haben, vor wahrhaftig ernsten Dingen. Und den Ernst der Zeit sollte eigentlich niemand ver­kennen, der nicht durch dieses Verkennen seine Seele ablenken will von vielem, das im eminentesten Sinne eben notwendig, der Menschenseele dringend notwendig ist, wenn sie einigermaßen würdig miterleben will diese gegenwärtige Zeit.",
      "Wir haben das 19. Jahrhundert und den Beginn des 20. Jahrhunderts mit den Mitteln zu charakterisieren versucht, die sich ergeben, wenn man die wichtigen, einschneidenden Ereignisse betrachtet, mit denen die Entwickelung der Menschen in diesem 19. und 20. Jahrhundert zu­sammenhängt. Sie werden erkannt haben, daß man vor allen Dingen, wenn man verstehen will, was das bedeutsamste Charakteristikon die­ser neuesten Zeit ist, den Blick zu richten hat darauf, daß diese unsere Zeit an einer Überfülle von Intellektualität geradezu leidet. Nicht als ob damit gesagt sein sollte, daß die Menschheit in unserer Gegenwart, verglichen mit früheren Zeitaltern, ganz besonders gescheit wäre. Das ist damit nicht gemeint, sondern gemeint ist, daß die verschiedenen",
      "Seelenkräfte des Menschen in unserer Zeit alle nach der Intellektualität hinneigen. Und da wir im materialistischen Zeitalter leben, so wird die Intellektualität ausschließlich dazu verwendet, das materielle Dasein mit der Menschenseele zu durchspinnen, und umgekehrt die Menschen-seele zu durchspinnen mit dem materiellen Dasein.",
      "Hoch ist unsere Intellektualität im gegenwärtigen Zeitalter nicht, weil sie sich fast ausschließlich richtet auf die Zusammenstellung und Zusammenfassung, wenn ich mich pedantisch ausdrücken will, auf die Systematisierung der materiellen Dinge und materiellen Erscheinungen. Aber in einem gewissen Sinne ist diese Intellektualität alleinherrschend innerhalb der menschlichen Seele.",
      "Was ist das Notwendige an Seelenkraft, das in dem nächsten Zeit­alter, an dessen Beginn wir stehen, zu der Intellektualität dazukommen muß? Mit Intellektuellem ist heute alles durchdrungen, wenn auch mit Intellektuellem, das ausschließlich auf den physischen Plan sich bezieht.",
      "Mit Intellektuellem ist die Wissenschaft, mit Intellektuellem ist die Kunst, mit Intellektuellem ist das menschliche soziale Denken durch­drungen. Was dazukommen muß, das ist etwas, was, wirklich ver­standen, gar nicht intellektuell sein kann.",
      "Und was gar nicht intellek­tuell sein kann, wenn es wirklich verstanden wird, wenn es in das menschliche Bewußtsein aufgenommen wird, das ist der menschliche Wille, der so von der Liebe durchdrungene menschliche Wille, wie ich versucht habe, den menschlichen Willen im Zusammenhange mit dem Impuls der Liebe zu charakterisieren in meiner «Philosophie der Frei­heit». Der menschliche Wille äußert sich entweder in den unterbewuß­ten Realitäten der Triebe, der Begierden, seien sie egoistische einzelne Begierden, seien sie soziale Begierden, seien sie politische Aspirationen, all dieses bleibt unbewußt oder unterbewußt.",
      "Wird aber der Wille wirklich heraufgehoben in das Bewußtsein, wird dasjenige, was sonst von den Willensimpulsen verschlafen wird, oder höchstens verträumt wird, wie die letzten Betrachtungen gezeigt haben, wird das herauf-gehoben in die Sphäre des Bewußtseins, dann kann diese Anschauung des Willens nicht mehr materialistisch sein. Wir finden in unserer Zeit für jeden wirklich spirituell die Welt durchschauenden Menschen ein beweisendes Symptom dafür, daß, was Wille ist, in unserer Zeit nicht",
      "erfaßt wird. Und dieses Symptom ist, daß überhaupt in einer solchen Weise, wie es der Fall ist, die Frage aufgeworfen werden kann von denjenigen Geistern, die sich selber als die bedeutendsten in unserer Zeit gelten: ob es überhaupt eine menschliche Freiheit gäbe oder nicht.",
      "Diese Frage, ob es überhaupt eine menschliche Freiheit gibt oder nicht, beweist, wenn sie aufgeworfen wird, eine unspirituelle Denkungs­art. Vom spirituellen Gesichtspunkt aus muß man sich zu der Frage der Freiheit in ganz anderer Weise verhalten. Da muß man sich so dazu verhalten, daß man weiß: Derjenige, der überhaupt zweifeln kann an der Tatsache der menschlichen Freiheit, versteht den menschlichen Willen nicht. Wo immer Zweifel auftreten an der menschlichen Frei­heit, da ist dieses Vorhandensein des Zweifels ein Beweis dafür, daß der Betreffende keine Ahnung hat von der wirklichen Realität des menschlichen Willens. Denn sobald man den Willen erkennt, erkennt man auch das selbstverständliche Korrelat des Willens, erkennt man den Impuls der menschlichen Freiheit.",
      "Allerdings, in unserer Zeit wird über Freiheit und Notwendigkeit so gesprochen, daß in dem Sprechen deutlich erkennbar ist dasjenige, was ich Ihnen das letzte Mal dargelegt habe in dem trivialen Vergleich mit dem Kürbis und der Flasche. Ich sagte, wenn man aus einem Kür­bis eine Flasche macht, so kann einer sagen: Das ist ein Kürbis - und der andere kann sagen: Das ist eine Flasche. - So streiten sich die Men­schen heute über Freiheit und Notwendigkeit des menschlichen Han­delns, und das, was sie vorzubringen wissen, ist in der Regel so viel wert, als wenn der eine steif und fest behauptet, das sei ein Kürbis, und der andere steif und fest behauptet, das sei eine Flasche. Es ist eben ein Kürbis, der eine Flasche geworden ist!",
      "Dies ist das Wichtige und Wesentliche, daß die Menschen in ihr Be­wußtsein wiederum aufnehmen die Kraft des Willens. Sobald man von Weltenwille redet, redet man auch von dem, was real waltet in dem Weltenwillen: von der Weltenliebe. Von ihr allerdings braucht wenig geredet zu werden, denn sie waltet dann, wenn der Wille wirklich vor­handen ist. Und viel bedeutungsvoller ist es, von den einzelnen kon­kreten Impulsen des Willens, die notwendig sind in unserer Zeit, zu",
      "reden, als sich in sentimentalen Allgemeinheiten zu ergehen über Liebe und Liebe und Liebe.",
      "Aber die Dinge müssen so angeschaut werden, daß im Anschauen wirklicher Mut zur Erkenntnis liegt und auch wirkliche Tatkraft zur Erkenntnis. Denn Erkenntnis der völligen, ganzen Menschennatur ist unserer Zeit notwendig. Und unsere Zeit muß beginnen, die Frage auf­zuwerfen als eine Menschenschicksalsfrage: Wie muß sich die Anschau­ung gegenüber dem Menschenwesen gestalten, wenn man in Frage zieht, daß so, wie wir es in diesen Betrachtungen vor unsere Seele hingeführt haben, die Sphäre der sogenannten Lebendigen und die Sphäre der so­genannten Toten eine ist, daß wir im Grunde genommen unter Leben­digen nur leben mit unserer Sinneswahrnehmung und unserem Intellekt, daß wir aber, insoferne wir fühlende und wollende Wesen sind, in der­selben Welt leben, in der die Toten auch leben. Und anschließen muß sich an das, was an inneren Seelenimpulsen bei dieser Erkenntnisfrage mitwirkt, ein wirklicher Wille, das Leben des Menschen konkret zu verstehen, auch wie es verläuft zwischen dem Tod und einer neuen Ge­burt. Denn ohne das Verständnis für dieses leiblose Leben des Men­schen ist auch ein wirkliches Verständnis nicht möglich für das Dasein des Menschen innerhalb des physischen Leibes, namentlich nicht mög­lich ein Verständnis für die Aufgabe des Menschen innerhalb des phy­sischen Leibes.",
      "Gewissermaßen abstrakt gesprochen: Es ist der gegenwärtigen Menschheit notwendig, die inneren Impulse des Zeitgeistes, jenes Zeit-geistes, der im engeren Sinne seit dem Jahre 1879 waltet, im weiteren Sinne schon waltet seit der Mitte des 15. Jahrhunderts, wirklich in sich aufzunehmen, mit den Impulsen dieses Zeitgeistes sich bekanntzu­machen. Davon haben viele Menschen - wenigstens von dem, was eigentlich mit dem eben ausgesprochenen Worte gemeint ist -, haben die meisten Menschen der Gegenwart kaum die allerspärlichste Ahnung. Ich habe es oft in diesen Betrachtungen gesagt: Das, was unserer Ju­gend - unserer jüngeren Jugend und unserer älteren Jugend - als soge­nannte Geschichte mitgeteilt wird, ist zumeist auf der einen Seite Fable convenue, auf der andern Seite vielfach wertloses Zeug. Soll wirkliche Geschichte entstehen, dann muß erst durchschaut werden das, was die",
      "Impulse der letzten Jahrhunderte waren und was in diesen Impulsen sich gerade in unserem Zeitalter ändern muß. Man hat heute kaum eine Ahnung davon, welcher gewaltige Umschwung im menschlichen Denken und Fühlen eingetreten ist mit dem Beginne des fünften nach-atlantischen Zeitraums, mit der Mitte des 15. Jahrhunderts. Das un­sinnigste Wort in bezug auf die Entwickelung gilt ja vielen Leuten heute als ein Geleitwort. Dieses unsinnige Wort ist: Die Natur macht keine Sprünge. - So wie die Natur ihren gewaltigen Sprung macht von dem grünen Laubblatt zu dem farbigen Blumenblatt, so macht die Natur ihre Sprünge überall. Und es ist nicht ein allgemeiner t)ber­gang gewesen aus dem vierten nachatlantischen Zeitraum zu der ersten Hälfte des 15.Jahrhunderts, zu dem fünften nachatlantischen Zeit­raum, angefangen von der zweiten Hälfte des 15.Jahrhunderts, son­dern es ist ein gewaltiger Umschwung dagewesen. Orientieren kann man sich nur, wenn man wenigstens einigermaßen vergleichen kann das, was die paar Jahrhunderte des fünften nachatlantischen Zeit­raums bisher gebracht haben, mit dem, was vorangegangen ist; denn beide Dinge sind voneinander grundverschieden. Von einem gewissen Gesichtspunkte aus möchte ich Ihren Geistesblick heute auf diese An­gelegenheit lenken.",
      "Hat man sich bekanntgemacht mit dem, was man lernen kann aus dem heutigen Inhalt der Wissenschaft, dem heutigen Inhalt der Men­schenbildung - falls man das törichte Wort «Bildung» gebrauchen darf -, hat man sich aus dem heraus heute vorbereitet und nimmt dann Schriften noch aus dem 15. Jahrhundert in die Hand, so versteht man sie gerade dann nicht, wenn man ein besonders gelehrter Kopf der heutigen Zeit ist.",
      "Nun müssen Sie mich nicht mißverstehen. Ich kann nach allen Vor­aussetzungen unserer anthroposophisch orientierten Geisteswissenschaft keineswegs dafür sein, daß alte Dinge aufgewärmt werden. Jenes Ge­rede, das so vielfach durch die Welt heute geht von der Notwendigkeit der Aufwärmung aller möglichen alten Schmöker und aller möglichen alten Anschauungen, das kann nicht etwa auch auf dem Felde unserer anthroposophisch orientierten Geisteswissenschaft getrieben werden, weil diese anthroposophisch orientierte Geisteswissenschaft aus dem",
      "unmittelbaren Geistesleben selbst heraus dasjenige zu schöpfen hat, was sich gerade für die Gegenwart zu offenbaren hat und weil sich in un­serer Zeit für den Empfangenden Bedeutsames offenbart. Aber klar­machen kann man sich manches, wenn man den Blick hinrichtet auf die Art, wie heute gerade ein recht gelehrter Kopf sich verhalten kann zu den Dingen, die als Weisheitsgut erhalten sind - wir brauchen gar nicht weiter zurückzugehen, sagen wir als ins 14., 15. Jahrhundert. Wenn heute ein recht gelehrter Kopf zum Beispiel in die Hand nimmt die Werke des sogenannten Basilius Valentinus, des berühmten Adepten aus dem 15. Jahrhundert, so weiß er gar nichts mit ihnen anzufangen. Was man heute gewöhnlich erfährt, wenn Leute so etwas wie den Basilius Valentinus in die Hand nehmen - es könnten auch andere sein, aber ich führe ihn an, weil er der berühmteste Adept des 15. Jahrhun-derts ist -, das ist so, daß sie entweder Unsinn reden, dilettantisches Zeug, indem sie sich vollpfropfen mit dem, was doch nicht verstanden werden kann, aber an das Unverstandene glauben, oder aber daß sie als gelehrte Knöpfe allerlei Unsinn reden, impotentes Zeug reden über das, was ihnen aus Basilius Valentinus entgegenströmt.",
      "Liest man mit Kennerblick, mit wirklichem spirituellem Kenner­blick so etwas wie den Basilius Valentinus, dann kommt man sehr bald darauf, daß in diesem Basilius Valentinus eine Weisheit enthalten ist, die allerdings unbrauchbar ist für die Menschen der Gegenwart, welche eben die landläufigen Interessen der Gegenwart haben, daß aber in diesem Basilius Valentinus um so mehr Weisheit von der Art ist, wie sie auftritt, wenn man sich in Verbindung bringen kann mit den Seelen, welche ihr Dasein haben zwischen dem Tod und einer neuen Geburt. Man kann sagen, was den Menschen gegenwärtig unnötig erscheint, diese Weisheit, wie sie in Basilius Valentinus steht, die haben um so mehr diejenigen Menschen nötig, welche zwischen dem Tod und einer neuen Geburt leben. Auch diese brauchen nicht den Basilius Valentinus zu studieren, denn wir haben in der anthroposophisch orientierten Gei­steswissenschaft etwas, was die Sprache spricht, die gemeinsam für die sogenannten Lebenden und für die sogenannten Toten ist. Es genügt das, was die anthroposophisch orientierte Geisteswissenschaft gibt, um in der uns bekannten Weise auch mit den Toten zu reden. Aber gewissermaßen",
      "als eine historische Tatsache führe ich es an, daß die Art, wie der Tote aufnimmt das, was Weltenwissen ist, eine gewisse Verwandt­schaft hat mit dem, was solche Schriften wie die des Basilius Valentinus bringen. Denn Basilius Valentinus redet von allerlei chemischen Ver­richtungen, redet scheinbar von demjenigen, was man mit Metall und andern Stoffen in Retorten und Schmelztiegeln unternimmt. In Wirk­lichkeit redet er von demjenigen Wissen, das sich die Toten aneignen müssen, wenn sie ihre Verrichtungen pflegen wollen in jenem untersten Reiche, von dem ich gesprochen habe, das also das unterste Reich eben für sie ist, in dem tierischen Reiche. Er redet von dem, was man zu kennen hat von jenen Impulsen, die aus der geistigen Welt heraus kommen, um den Mikrokosmos selbst aus dem Makrokosmos heraus zu begreifen. Dies ist ja die Erkenntnistätigkeit der Seele zwischen dem Tod und einer neuen Geburt, die aber heute nur richtig verrichtet wer-den kann,wenn sie vorbereitet wird zwischen der Geburt und dem Tode. Das war als ein atavistisches Erbgut, als ein uraltes Weisheitserbe noch bis ins 15. Jahrhundert vorhanden. Und Basilius Valentinus redet von diesem uralten Weisheitserbe, redet von den Geheimnissen, wie der Mensch zusammenhängt mit dem Makrokosmos, redet wirkliche, gött­liche Weisheit - in Imaginationen, wie wir heute sagen würden.",
      "Diese Art sich zu dem Kosmos zu verhalten im Erkennen, ist im Laufe der letzten Jahrhunderte verschwunden. Sie muß wieder er­worben werden - auf eine geistigere Weise, als sie vor dem 15. Jahr-hundert vorhanden war, muß sie wiederum erworben werden. Denn sie muß geübt werden sowohl in der Wissenschaft wie auch in dem sozialpolitischen Leben. Ein Heil ist der Menschheit nur möglich, wenn solche Ziele verfolgt werden. Und das muß erkannt werden, daß der Menschheit ein Heil nur unter dem Einfluß solcher Ziele mög­lich ist.",
      "Ein gewissermaßen Uroffenbarung zu nennendes, uraltes Erbgut ging durch die Jahrhunderte herunter. Im materialistischen fünften nachatlantischen Zeitalter verlor sie sich. Erworben muß sie wiederum in neuer Weise werden. Erworben kann sie nur werden, wenn der Mensch sie erwirbt, wie wir oft und oft auseinandergesetzt haben, indem er sich durchdringt, aber tätig, willentlich durchdringt mit dem",
      "Paulinischen Aber wie gesagt, gerade der gelehrte Kopf der Gegenwart, wie steht er vor dieser alten Weisheit? So etwa, wie jener Gelehrte, der die Worte gesprochen hat: «Die letzte und wichtigste Operation von Basilius Valentinus ist die zehn Monate hindurch allmählich gesteigerte Erhit­zung des philosophischen Quecksilbers und Goldes im Philosophen-Ofen, wodurch der  den  und dieser den  gebärt, der wieder den  er­zeugt. Dieser aber (eine rote Substanz) ist der Stein der Weisen, der sich bis zur Unendlichkeit vermehren kann. Man vermag leider nicht» -sagt der moderne wissenschaftliche Kopf -, «man vermag leider nicht zu begreifen, wie jemand, und wäre es der geschickteste und begeistert­ste Adept (so wurden die Männer genannt, die das Geheimnis des Stei­nes der Weisen besaßen) solchen Vorschriften folgen könnte.»",
      "So Theodor Svedberg in Uppsala, der ein Buch über diese Dinge von dem wissenschaftlichen Standpunkt der Gegenwart geschrieben hat und der in dieser Beziehung nur der Repräsentant all der gelehrten Köpfe ist, die eben sagen müssen: Man vermag leider nicht zu begrei­fen. - Es ist noch das beste, wenn sie das sagen: Man vermag leider nicht zu begreifen. - Für sie alle hat Basilius Valentinus schon die nötigen abfertigenden Worte selbst hingeschrieben, indem er in seinen «Zwölf Schlüsseln zum Weltenall und dessen Verständnis» schreibt:",
      "«Verstehest du jetzo, was ich rede, so hast du mit dem Schlüssel das erste Schloß eröffnet und den Riegel des Anlaufs zurückgetrieben. Kannst du aber noch kein Licht drinnen ergründen, so wird dich auch kein gläsern Gesichte befördern, noch natürliche Augen vermögen zu helfen, das Letzte zu finden, das du im Anfange gemangelt hast. Dann",
      "will ich nicht ferner reden von diesem Schlüssel, wie mich Lucius Papirius gelehret hat.»",
      "So spricht Basilius Valentinus schon zu all den Nachfahren, die dem alten Weisheitsgut gegenüber höchstens die Worte haben: Man vermag leider nicht zu begreifen. - Aber diese Menschen der Gegenwart haben ja auch etwas anderes zu tun, als das Geistige zu begreifen! Diese Men­schen der Gegenwart müssen sich mit allerlei andern Dingen befassen; und wenn vom Geiste irgendwie die Rede ist, so müssen sie sich vor allen Dingen damit befassen, dieses Reden vom Geiste zu verleumden. Und ungeheuer viel Zeit wird heute aufgebraucht dazu, das Reden vom Geiste zu verleumden.",
      "Zu dem Berliner Unsinn des Max Dessoir kann noch hinzugefügt werden - ich habe das Geschreibsel noch nicht selbst lesen können, aber es ist mir einiges erzählt worden - das holländische Konterfei des Phi­losophen Bolland, der sich ja einige Verdienste für die philosophische Entwickelung dadurch erworben hat, daß er durch sein Nachreden Hartmannscher und Hegelscher Brocken die philosophische Jugend Hollands in Begeisterung versetzt hat, aber auch, wie es scheint, nicht umhin konnte, in der letzten Zeit seine philosophische Unproduktivi­tät dazu zu verwenden, unsere Geisteswissenschaft durch allerlei un­wahres Zeug zu verleumden.",
      "Das muß immer wieder und wiederum hervorgehoben werden, denn es gehört schon zum wirklichen Aufnehmen der Geisteswissenschaft in unsere Seele auch die Aufmerksamkeit auf die Art und Weise, wie die Gegenwart in ihrer geisteswissenschaftlichen Impotenz sich verhält zu dem, was der Menschheit notwendig ist.",
      "Diese gegenwärtige Wissenschaft - ich spreche da nicht von der äußeren Wissenschaft, die ich, wie Sie wissen, voll anerkenne, wenn ich auch nicht jedem Naturforscher nachlaufe -, aber das, was vielfach sich Philosophie und dergleichen nennt, ist in der Gegenwart nicht viel mehr als abstraktes Gerede, welches in der völligen Verwirrung über die Begriffe von Kürbis und Flasche geführt wird. Leider geschieht es bei uns auch noch viel zu häufig, daß wir immer wieder und wieder auf das unsinnige Gerede namentlich der gegenwärtigen Philosophen hin­einfallen und sogar zuweilen froh sind, wenn da oder dort irgendein",
      "philosophischer Knopf dies oder jenes, sagen wir, nicht zu tadeln fin­det an dem, was anthroposophisch orientierte Geisteswissenschaft will. Als ob das nicht, wenn er es nicht zu tadeln findet, mindestens seine Pflicht und Schuldigkeit wäre! Wir brauchen uns gar nicht zu freuen, so wie es viele unter uns tun, wenn von dieser oder jener Seite einmal auch ein lobendes Wörtchen abfällt. Auch diese lobenden Wörtchen sind ja zumeist nicht gerade von einem großen Verständnisse getragen. Aber wir müssen uns gefaßt machen darauf, daß solche Verleumder von der Sorte Dessoirs oder Bollands immer wieder und wieder auf­treten werden, und daß sie sich in der nächsten Zeit gar sich vermehren werden. Denn sie müssen sich doch mit etwas beschäftigen, diese Leute! Und da sie viel zu bequem sind, einzugehen auf das, was aus der geisti­gen Welt zum Heile der Menschheit im gegenwärtigen Zeitalter geholt werden muß, so müssen sie sich damit beschäftigen, das, was geholt wird, zu verleumden.",
      "Basilius Valentinus, sagte ich, bot noch ein uraltes, atavistisch über­kommenes Erbgut, eine Wissenschaft von der Art, wie der Mensch her­ausgeschaffen wird aus dem kosmischen All, wie sie vor allen Dingen die Wissenschaft der vom Leibe befreiten Seele ist, wie aber auch sein muß die Wissenschaft, die mitwirken will bei allem, was nicht bloß äußere Natur ist. Gefördert kann diese Wissenschaft nur werden, wenn zu dem reinen, und zwar materialistisch orientierten intellektuellen Elemente der Neuzeit die Erkenntnis des Willens aufgenommen wird, des Willens, der, wenn er als Wille wirklich erkannt wird, nur in seiner spirituellen Natur erkannt werden kann, weil er nur spirituell sich äußert in dem gegenwärtigen Entwickelungsstadium der Menschheit. Ein nicht feiges Heraufholen der Lebensimpulse aus der Sphäre des Willens, das ist das, was der Gegenwart so sehr mangelt. Die Gegen­wart will vor allen Dingen reden, reden! Das ist gut, aber nur auf Grundlage eines wirklichen Erkennens. Nicht das letztere will die Ge­genwart - reden will jeder, reden will jeder, auch auf nichtige Voraus­setzungen hin. Und wir haben ja gesehen, daß in diesem Unberücksich­tigtlassen des spirituellen Elementes in der Welt gerade das Unglück unseres Zeitalters liegt. Man meint es in der Gegenwart nur dann ehr­lich mit der Entwickelung der Menschheit, wenn man sich wirklich einlassen",
      "will auf die Ergründung derjenigen Willensimpulse, die notwen­dig sind, um die Wogen der Menschheitsentwickelung weiterzutreiben.",
      "Selbstverständlich müssen diese Dinge nicht persönlich genommen werden. An diesem oder jenem Platz des Lebens kann selbstverständ­lich jeder sagen: Ja, was soll ich tun? - Ganz gewiß, das kann auch niemals die Anforderung sein, daß wir heute begreifen, was wir tun sollen, um morgen irgendwie die ersten Schritte zu tun, um irgend etwas Weltepochemachendes zu unternehmen.",
      "Was wir zu unternehmen haben, wird uns das Karma schon bringen. Was wir aber zu tun haben, das ist: die Augen - ich meine die Augen der Seele - aufzumachen, um wirklich zu erkennen, um wirklich die Zeit zu durchschauen.",
      "Das, was wir zu tun haben, ist: diese Zeit nicht zu verschlafen, sondern hinein-zuschauen in das, was geschieht! Was der Materialismus des fünften nachatlantischen Zeitraumes den Menschen genommen hat, notwendig nehmen mußte, weil sich die Menschen zunächst rein persönlich orien­tieren mußten, das sind umfassende Ideen, wie sie gerade die Ausflüsse des Zeitgeistes sind, das sind umfassende Ideen, die wir gemeinsam haben können mit den sogenannten Toten.",
      "Das intellektualistische Zeug, das in unserer Zeit so groß geworden ist, hat nicht nur die Men­schenseelen ergriffen, das hat deshalb auch ergriffen die soziale und geschichtliche Entwickelung des Zeitalters selbst. Der Mensch hat vor der Notwendigkeit der Geschichte - mit einem gewissen Recht, denn an diesen Dingen soll nicht Kritik geübt werden, sondern sie sollen charakterisiert werden -, der Mensch hat mit einem gewissen Recht manches von dem, was er früher aus seiner Menschheitsinitiative her­aus, ich meine auch aus der organischen Menschheitsinitiative heraus verrichtet hat, an die Maschine abgegeben.",
      "Das materialistische Zeit­alter ist ja zu gleicher Zeit das Maschinenzeitalter. Und dieses Ma­schinenzeitalter formt mit den Maschinen nicht nur dasjenige, was es zum gewöhnlichen Leben braucht, sondern der Krieg selbst ist zur Pflege einer großen Maschinerie geworden.",
      "Es konnte nicht anders kommen, denn die Menschheit hat im Laufe der letzten Jahrhunderte nicht nur eine gewisse Menschheitsschicht ausgebildet, sondern inner­halb dieser Menschheitsschicht auch Anschauungen kultiviert, die vor allen Dingen darauf bedacht sind, nur das als wissenschaftlich gelten",
      "zu lassen, was sich realisieren kann innerhalb der äußeren sozialen Ordnung im Werden von Maschinen: entweder im Werden von mecha­nischen Maschinen - wenn ich diese Tautologie, den Pleonasmus ge­brauchen darf - oder aber im Werden von sozialen Maschinen. Denn eine große Maschinerie ist zum Beispiel bis vor dem Kriege die Finanz­gebarung gewesen, die internationale Finanzgebarung der Welt. Alles ist maschinenmäßig gewesen. An das Maschinenmäßige hat der Mensch viel abgegeben. Zurückbehalten wollte eine gewisse Schicht der Mensch­heit von diesem Maschinenmäßigen im Grunde genommen nur das, was die triviale Lebensnotwendigkeit vergnüglich macht. Man könnte sagen: Im Winter schuften, im Sommer ins Bad gehen und nur so viel denken, als notwendig ist, damit die Weltenmaschinerie für einen schuftet, das wurde Signatur des Zeitalters.",
      "Nicht als ob das hätte unterbleiben können. DieseWeltenmaschinerje mußte heraufkommen, das ist ganz selbstverständlich. An dem Ge­schehenen Kritik zu üben, ist ein Dilettantismus, an dem sich Geistes­wissenschaft nicht beteiligen kann. Aber durchschaut, und in der Eigen­art, die es hat, erkannt werden muß die Sache, denn nur dann wird man demgegenüber die richtigen Willensimpulse entwickeln können.",
      "Immer wiederum sind die Menschen gekommen, welche die ange­messenen Ideen schon ausgesprochen haben für dieses Zeitalter. Aber diese Aussprecher der angemessenen Ideen wurden gerade in der zwei­ten Hälfte des 19. Jahrhunderts und im Beginne des 20. Jahrhunderts eigentlich als unmögliche menschliche Persönlichkeiten betrachtet. Über solche Köpfe, die klar sahen, wie die soziale Struktur der Mensch­heit über die Erde hin sein muß unter dem Einfluß des Maschinenzeit-alters, über solche Köpfe wie Bright oder Cobden ist die nachfolgende Menschheit zur Tagesordnung übergegangen - diese nachfolgende Menschheit, die allerdings etwas Geisteskraft hätte aufwenden müssen, um gerade das Angemessene der Brightschen und Cobdenschen Ideen für das Maschinenzeitalter herauszufinden! Aber den Willen in den Intellekt hineinzudrängen, um die Wirklichkeit zu durchschauen, das ist eben eine Kraftanstrengung, vor der die Menschen der Gegenwart zurückschrecken. Sie wollen nicht ihre Gedanken von Willen durch­tränken. Sie wollen ihre Gedanken sentimental hinzielen lassen über",
      "dasjenige, was ihnen, wie sie sagen, wohlig ums Herz macht, wenn sie sich erheben wollen. Und unter dem Einflusse eines solchen willens­entblößten Denkens, dem es aber so warm und wohl wird beim Schwätzen in Sentimentalitäten, gewöhnt man sich daran, auch die wichtigsten Fragen mit einem willenlosen, feigen Denken zu ergreifen. Man gewöhnt sich vor allen Dingen daran, von der weltgeschichtlichen Entwickelung nichts zu lernen. Ist denn die Menschheit gegenwärtig bereit zu lernen? Auch das soll nicht als eine Kritik ausgesprochen wer­den, sondern nur als eine Charakteristik.",
      "All dasjenige, was ich sage, ist nicht eingegeben von dem Gesichts­punkt der Kritik, sondern ist eingegeben von dem Gesichtspunkt der Anregung des Willens. Klarstellen muß man, wie man in seine Ge­danken den Willensimpuis hineinleitet, der zum Heile der Menschheit dienen kann.",
      "Leider sind die Menschen der Gegenwart zu wenig ge­neigt, zu lernen. Sie lassen die Dinge an sich vorübergehen und bereden sie und glauben, mit dem Bereden auch das Willenselement zu meistern. Wieviel ist geschwätzt, wesenlos geschwätzt worden in der Zeit, in der sich die unheilvollen Ursachen dieser Weltenkatastrophe vorbereitet haben!",
      "Wieviel ist geschwätzt worden auf die Anregung der Friedens­manifest-Firlefanzereien des Zaren hin! Das konnte geschehen, denn man kann sagen, daß eben erst gelernt werden mußte, daß es sich um Friedensmanifest-Firlefanzereien handelte, und daß all dieses Ge­schwätz, das daran geknüpft worden ist, Millionen und Millionen Meilen weit entfernt war von der Möglichkeit, Willensimpulse anzu­regen in der Menschheit.",
      "Aber gelernt sollte werden. Wird gelernt? Nein, es wird vorläufig nicht gelernt - und nicht darum handelt es sich, das Nichtlernen zu bemängeln, sondern darum handelt es sich, dieses Nichtlernen zu durchschauen, damit man lerne.",
      "Was ist an die Stelle getreten, an die Stelle des Schwätzens über allerlei Weltenziele in Anknüpfung an die Friedensmanifest-Firlefanzereien des nunmehr abgetanen Zaren? Der andere Unsinn von den Friedensmanifest-Firle­fanzereien des Schwätzers Woodrow Wilson!",
      "Genau dieselbe Sache anstelle derselben Sache! Das ist zu lernen, daß die Menschheit nicht lernen will. Und in der Erkenntnis von diesem Nichtlernenwollen wird sich anfachen in unserer Seele der heilige Wille zum rechten Wollen,",
      "das hervorgehen muß aus dem rechten Durchschauen desjenigen, was wirkt und webt in unserer Zeit.",
      "Ich habe in den öffentlichen Vorträgen gesagt, daß im Grunde ge­nommen das, was sich im Lauf der letzten vier Jahrhunderte im ge­schichtlichen Traum der Menschheit heraufentwickelt hat, wie ein Weltenprogramm ausgesprochen worden ist im Lauf des 19.Jahrhun-derts von solchen Leuten wie Karl Marx und ähnlichen Leuten. Die Impulse sind schon vergangen gewesen, als es ausgesprochen worden ist; aber es war damit das ausgesprochen, was im Grunde genommen die Unterlage war für das geschichtliche Werden der letzten vier Jahr­hunderte.",
      "Wie liegt die Sache? Die Sache liegt heute so, daß die breiteren menschlichen Schichten alles Denken über soziale Zusammenhänge aufgegeben haben. Man überläßt es den Professoren der National­ökonomie, die ja im Verlauf der letzten Jahrhunderte, namentlich Jahr­zehnte genug Unsinn geschwätzt haben.",
      "Wirkliches soziales Denken, das hervorzugehen hat aus der Erkenntnis der aus der Geisteswelt kommenden Impulse, ist in den sogenannten führenden Schichten ab­handen gekommen. Einzig und allein eine Schicht hat weltgeschicht­liche Ideen in der letzten Zeit in die Welt gesetzt: diejenige Schicht, die in okkulter Auffassung Brüder des Schattens sind gegenüber den Brü­dern der bürgerlichen Parteien der letzten Jahrhunderte.",
      "Weltgeschicht­liche Ideen, wenn auch Schattenideen, hat die Sozialdemokratie ge­bracht, graue Schattenideen von besonders gefährlicher Art, da sie ganz imprägniert sind von dem Geiste der letzten Jahrhunderte. Aber weit-geschichtliche Ideen sind es, die den andern Schichten der Menschheit völlig gemangelt haben.",
      "Denn die andern Schichten der Menschheit, sie hätten sie entlehnen müssen aus der geistigen Welt; sie hätten nötig gehabt, nicht im allgemeinen in salbungsvoller Weise ihre religiösen, ihre sozialen, ihre geschichtlichen Ideen zu entwickeln, sondern auf fester Erkenntnisgrundlage das soziale Werden zu durchschauen. Nie­mand wird das soziale Werden in Wirklichkeit durchschauen, der sich nicht in die Lage versetzen will, dies von Ausgangspunkten zu tun, die diesen unseren Betrachtungen in den letzten Wochen hier zugrunde gelegen haben.",
      "Dafür spricht das Beste, was die sogenannten Lebenden heute aus der geistigen Welt empfangen können, dafür spricht das Beste, was die Toten uns offenbaren aus ihrem Leben zwischen dem Tod und einer neuen Geburt. Dafür spricht jene neue Auffassung des Mysteriums von Golgatha, der wir durch die Vertiefung der anthroposophisch orientier­ten Geisteswissenschaft entgegengehen müssen. Dafür spricht alles das, was wir in dieser ernsten Zeit als ernste Weihnachtsgedanken uns durch die Seele ziehen lassen sollen. Denn zum Heil der Menschheit ist das Wesen in die Erdenentwickelung eingetreten, dessen Geburt im Weih­nachtsfeste gefeiert wird, nicht zum behaglichen Zur-Seele-Reden bloß, sondern dazu, daß diese Menschenseele sich durchdringt mit - wenn ich das paradoxe Wort gebrauchen darf - dem Willen zum Willen, dem Willen zum Wollen. Durchdringt dieser Wille zum Wollen die Menschenseelen, dann wird dies den Impuls bedeuten zu einer Sehn­sucht nach wirklich neuen Ideen, denn die alten sind abgebraucht. Manchmal können wir nicht einmal die Worte mehr gebrauchen.",
      "Wir leben in einer katastrophalen Zeit. Das, was geschieht, Krieg zu nennen, ist fast schon anachronistisch, ist nur aus der alten Gewohn­heit entstanden, die Flasche noch Kürbis zu nennen. Ebensowenig aber, wie das, was geschieht, Krieg zu nennen ist, ebensowenig sollte in leicht­fertiger Weise die wohlbehäbige Hoffnung in der alten Weise von Frieden sprechen! Gewaltige Zeichen kündigen sich in unserer Zeit an, und der Menschheit obliegt es, zu versuchen, diese Zeichen zu verstehen. In den Ereignissen selber wandeln sich die Ereignisse um. 1914 hat ein Weltenereignis begonnen, das man vielleicht im Anfange nennen konnte einen Krieg zwischen der Entente und den europäischen Mittelmächten. Unter dem aber, was so genannt wird, waltet etwas wesentlich anderes, stehen einander ganz andere Feinde gegenüber! Und in unseren Tagen kündigt sich uns an ein ernstes Symptom von dem, was glimmend wal­tet unter dem, was wir recht uneigentlich noch einen Krieg zwischen der Entente und den Mittelmächten nennen, kündigt sich uns an ein Symptom, das da besteht in dem traurigen Aufeinanderprallen der Bevölkerung Nord- und Südrußlands, ein bedeutungsvolles Symptom, wenn es auch vielleicht noch verlöschen kann zunächst, ein bedeutungs­volles Symptom für das, was unter den Ereignissen glimmt. Die Menschen",
      "lieben es nicht, daß die Dinge heute beim rechten Namen genannt werden, weil sie das Wollen nicht wollen, weil sie sich lieber über den Ernst der Zeit hinwegsetzen, solange es nur irgend geht, solange der Magen nicht allzustark knurrt. Dasjenige, um was es sich handelt, das ist, daß wir wirklich den Willen entwickeln, die tieferen Grundlagen der Ereignisse zu schauen, daß wir endlich einmal den Willen ent­wickeln, alle Oberflächlichkeit abzutun, um mit den Seelenaugen den Dingen ins Antlitz zu schauen.",
      "Wir werden, indem wir das, was wir jetzt in einer Art von Über­schau durch unsere Seele haben ziehen lassen, in den nächsten Vorträgen ergänzend auf mancherlei noch hinzuweisen haben, was zusammen­hängt mit den tieferen Impulsen, denen wir uns in diesen Betrachtungen hingegeben haben. Aber ich glaube, in dieser Zeit ehrt man die geheim­nisvolle dreifache Notwendigkeit, welche durch das Weltenwerden geht und die der Bruder ist von der Menschenfreiheit und der Freiheit der andern Geschöpfe, am meisten, wenn man sich keinen Schleier vor das Auge weben will. Hier auf dieser Erde müssen wir Freiheit begrei­fen. Auch in dieser Beziehung lernt der Blick des Gegenwartsmenschen sehr viel, wenn er sich zu den Toten hinrichtet; denn der Tote weiß, daß ihm Freiheit in dem Leben zwischen dem Tod und einer neuen Ge­burt durch das wird, was er sich mitbringt aus dem Leben zwischen der Geburt und dem Tode. Eingebettet sein in die Intelligenzen der höheren Hierarchien, das ist etwas, was uns wie eine Naturnotwendigkeit wird, wenn wir durch die Pforte des Todes gehen, wenn wir drüben leben -eingebettet sein in den Intelligenzen der höheren Hierarchien und deren Impulsen folgen, wie hier ein Naturereignis mit Notwendigkeit den Naturimpulsen folgt. Dann sind wir noch, nachdem wir durch die Pforte des Todes geschritten sind, frei, wenn wir in unserer Seele mit hinübertragen in die geistige Welt dasjenige, was wir uns hier als Wis­sen vom geistigen Werden und geistigen Wesen erwerben können.",
      "Dies ist etwas, was nun auch im tiefsten Sinne mit dem Mysterium von Golgatha zusammenhängt. Und weil dies so ist, glaube ich, daß auch Weihnachtsbetrachtungen in dieser Zeit nicht sentimentale sein dürfen, sondern solche sein müssen, welche an den Willen zum Wollen appellieren.",
      "Denn man nehme die Evangelien: wieviel ist in den Evangelien ge­rade an Appell zum Willen zum Wollen! Die Evangelien sind keine sentimentalen Schriften, die Evangelien sind Schriften, die allerdings zu dem Allerbescheidensten der Menschennatur sprechen, aber sie sind auch Schriften, welche das, was der Mensch an Stärke des Willens auf­bringen kann, in den Menschen erwecken wollen. Nicht nur dazu sollen die Weihnachtskerzen brennen, daß wir uns in einer gewissen Weise wollüstigen Betrachtungen hingeben, sondern auch dazu sollen sie bren­nen, daß sie Symbole seien für die Anfachung des der Welt zum Heile dienenden Willenslichtes.",
      "Die Menschheit hat viel nachzuholen; und es ist nachzuholen! Denn indem sie die Kraft entwickeln wird, welche in diesem Nachholen liegt, wird sie rechte heilsame Kräfte entwickeln, um aus der gegenwärtigen katastrophalen Zeit herauszukommen. Das ist der Menschheit nicht zur Aufgabe gesetzt worden, bloß hineinzukommen in diese Zeiten; viel wichtiger ist die Aufgabe, aus ihnen herauszukommen. Diese Auf­gabe steht als ein heiliges Zeichen, wie ich glaube, mit Flammenschrift geschrieben hinter all den Weihnachtskerzen, die nun schon seit vier Jahren in anderer Weise vor unserer Seele brennen als manches frühere Jahr!",
      "Morgen treffen wir uns um vier Uhr im Basler Zweig zu einer Weih-nachtsfeier. Montag um viereinhalb werden wir uns hier versammeln zur ersten Aufführung des «Paradeis-Spieles», und ich werde dann daranschließen eine Weihnachtsbetrachtung für diejenigen unserer Freunde, die nicht durch irgend etwas zu Hause abgehalten sind, son­dern die gerade jetzt da sind, sich den Arbeiten und dergleichen wid­mend, und die an diesem Tage vielleicht ihr Weihnachten am liebsten hier verbringen mögen."
    ],
    "sentences": [
      [
        "Es scheint, daß es gut sein könnte gerade in der Gegenwart, im gegen­wärtigen Zeitpunkt unserer Betrachtung etwas zurückzublicken auf Verschiedenes, das im Laufe dieser Auseinandersetzungen durch unsere Seelen gegangen ist, zurückzublicken allerdings nicht in wiederholen-der Weise, sondern in orientierender Weise, wiederum von einem ge­wissen Gesichtspunkt aus die Dinge beleuchtend.",
        "Denn die Betrach­tungen, die wir in dieser Zeit angestellt haben, und die sich in einer gewissen Art angeschlossen haben an das, was wir durch die Vorjahre vor unsere Seele haben treten lassen, sie sollen vor allen Dingen neben den positiven Mitteilungen, die sie enthalten, dazu geeignet sein, in dieser ernsten Zeit unsere Seele mit solchen Gedanken zu erfüllen, wie sie eben von der menschlichen Seele gebraucht werden in dieser Zeit, einer Zeit, von der man sagen muß, daß sie zu dem Ernstesten der welt-geschichtlichen Entwickelung gehört.",
        "Wir stehen, trotzdem wir man­cherlei im Laufe der letzten Jahre mitgemacht haben, vor wahrhaftig ernsten Dingen.",
        "Und den Ernst der Zeit sollte eigentlich niemand ver­kennen, der nicht durch dieses Verkennen seine Seele ablenken will von vielem, das im eminentesten Sinne eben notwendig, der Menschenseele dringend notwendig ist, wenn sie einigermaßen würdig miterleben will diese gegenwärtige Zeit."
      ],
      [
        "Wir haben das 19.",
        "Jahrhundert und den Beginn des 20.",
        "Jahrhunderts mit den Mitteln zu charakterisieren versucht, die sich ergeben, wenn man die wichtigen, einschneidenden Ereignisse betrachtet, mit denen die Entwickelung der Menschen in diesem 19. und 20.",
        "Jahrhundert zu­sammenhängt.",
        "Sie werden erkannt haben, daß man vor allen Dingen, wenn man verstehen will, was das bedeutsamste Charakteristikon die­ser neuesten Zeit ist, den Blick zu richten hat darauf, daß diese unsere Zeit an einer Überfülle von Intellektualität geradezu leidet.",
        "Nicht als ob damit gesagt sein sollte, daß die Menschheit in unserer Gegenwart, verglichen mit früheren Zeitaltern, ganz besonders gescheit wäre.",
        "Das ist damit nicht gemeint, sondern gemeint ist, daß die verschiedenen"
      ],
      [
        "Seelenkräfte des Menschen in unserer Zeit alle nach der Intellektualität hinneigen.",
        "Und da wir im materialistischen Zeitalter leben, so wird die Intellektualität ausschließlich dazu verwendet, das materielle Dasein mit der Menschenseele zu durchspinnen, und umgekehrt die Menschen-seele zu durchspinnen mit dem materiellen Dasein."
      ],
      [
        "Hoch ist unsere Intellektualität im gegenwärtigen Zeitalter nicht, weil sie sich fast ausschließlich richtet auf die Zusammenstellung und Zusammenfassung, wenn ich mich pedantisch ausdrücken will, auf die Systematisierung der materiellen Dinge und materiellen Erscheinungen.",
        "Aber in einem gewissen Sinne ist diese Intellektualität alleinherrschend innerhalb der menschlichen Seele."
      ],
      [
        "Was ist das Notwendige an Seelenkraft, das in dem nächsten Zeit­alter, an dessen Beginn wir stehen, zu der Intellektualität dazukommen muß?",
        "Mit Intellektuellem ist heute alles durchdrungen, wenn auch mit Intellektuellem, das ausschließlich auf den physischen Plan sich bezieht."
      ],
      [
        "Mit Intellektuellem ist die Wissenschaft, mit Intellektuellem ist die Kunst, mit Intellektuellem ist das menschliche soziale Denken durch­drungen.",
        "Was dazukommen muß, das ist etwas, was, wirklich ver­standen, gar nicht intellektuell sein kann."
      ],
      [
        "Und was gar nicht intellek­tuell sein kann, wenn es wirklich verstanden wird, wenn es in das menschliche Bewußtsein aufgenommen wird, das ist der menschliche Wille, der so von der Liebe durchdrungene menschliche Wille, wie ich versucht habe, den menschlichen Willen im Zusammenhange mit dem Impuls der Liebe zu charakterisieren in meiner «Philosophie der Frei­heit».",
        "Der menschliche Wille äußert sich entweder in den unterbewuß­ten Realitäten der Triebe, der Begierden, seien sie egoistische einzelne Begierden, seien sie soziale Begierden, seien sie politische Aspirationen, all dieses bleibt unbewußt oder unterbewußt."
      ],
      [
        "Wird aber der Wille wirklich heraufgehoben in das Bewußtsein, wird dasjenige, was sonst von den Willensimpulsen verschlafen wird, oder höchstens verträumt wird, wie die letzten Betrachtungen gezeigt haben, wird das herauf-gehoben in die Sphäre des Bewußtseins, dann kann diese Anschauung des Willens nicht mehr materialistisch sein.",
        "Wir finden in unserer Zeit für jeden wirklich spirituell die Welt durchschauenden Menschen ein beweisendes Symptom dafür, daß, was Wille ist, in unserer Zeit nicht"
      ],
      [
        "erfaßt wird.",
        "Und dieses Symptom ist, daß überhaupt in einer solchen Weise, wie es der Fall ist, die Frage aufgeworfen werden kann von denjenigen Geistern, die sich selber als die bedeutendsten in unserer Zeit gelten: ob es überhaupt eine menschliche Freiheit gäbe oder nicht."
      ],
      [
        "Diese Frage, ob es überhaupt eine menschliche Freiheit gibt oder nicht, beweist, wenn sie aufgeworfen wird, eine unspirituelle Denkungs­art.",
        "Vom spirituellen Gesichtspunkt aus muß man sich zu der Frage der Freiheit in ganz anderer Weise verhalten.",
        "Da muß man sich so dazu verhalten, daß man weiß: Derjenige, der überhaupt zweifeln kann an der Tatsache der menschlichen Freiheit, versteht den menschlichen Willen nicht.",
        "Wo immer Zweifel auftreten an der menschlichen Frei­heit, da ist dieses Vorhandensein des Zweifels ein Beweis dafür, daß der Betreffende keine Ahnung hat von der wirklichen Realität des menschlichen Willens.",
        "Denn sobald man den Willen erkennt, erkennt man auch das selbstverständliche Korrelat des Willens, erkennt man den Impuls der menschlichen Freiheit."
      ],
      [
        "Allerdings, in unserer Zeit wird über Freiheit und Notwendigkeit so gesprochen, daß in dem Sprechen deutlich erkennbar ist dasjenige, was ich Ihnen das letzte Mal dargelegt habe in dem trivialen Vergleich mit dem Kürbis und der Flasche.",
        "Ich sagte, wenn man aus einem Kür­bis eine Flasche macht, so kann einer sagen: Das ist ein Kürbis - und der andere kann sagen: Das ist eine Flasche. - So streiten sich die Men­schen heute über Freiheit und Notwendigkeit des menschlichen Han­delns, und das, was sie vorzubringen wissen, ist in der Regel so viel wert, als wenn der eine steif und fest behauptet, das sei ein Kürbis, und der andere steif und fest behauptet, das sei eine Flasche.",
        "Es ist eben ein Kürbis, der eine Flasche geworden ist!"
      ],
      [
        "Dies ist das Wichtige und Wesentliche, daß die Menschen in ihr Be­wußtsein wiederum aufnehmen die Kraft des Willens.",
        "Sobald man von Weltenwille redet, redet man auch von dem, was real waltet in dem Weltenwillen: von der Weltenliebe.",
        "Von ihr allerdings braucht wenig geredet zu werden, denn sie waltet dann, wenn der Wille wirklich vor­handen ist.",
        "Und viel bedeutungsvoller ist es, von den einzelnen kon­kreten Impulsen des Willens, die notwendig sind in unserer Zeit, zu"
      ],
      [
        "reden, als sich in sentimentalen Allgemeinheiten zu ergehen über Liebe und Liebe und Liebe."
      ],
      [
        "Aber die Dinge müssen so angeschaut werden, daß im Anschauen wirklicher Mut zur Erkenntnis liegt und auch wirkliche Tatkraft zur Erkenntnis.",
        "Denn Erkenntnis der völligen, ganzen Menschennatur ist unserer Zeit notwendig.",
        "Und unsere Zeit muß beginnen, die Frage auf­zuwerfen als eine Menschenschicksalsfrage: Wie muß sich die Anschau­ung gegenüber dem Menschenwesen gestalten, wenn man in Frage zieht, daß so, wie wir es in diesen Betrachtungen vor unsere Seele hingeführt haben, die Sphäre der sogenannten Lebendigen und die Sphäre der so­genannten Toten eine ist, daß wir im Grunde genommen unter Leben­digen nur leben mit unserer Sinneswahrnehmung und unserem Intellekt, daß wir aber, insoferne wir fühlende und wollende Wesen sind, in der­selben Welt leben, in der die Toten auch leben.",
        "Und anschließen muß sich an das, was an inneren Seelenimpulsen bei dieser Erkenntnisfrage mitwirkt, ein wirklicher Wille, das Leben des Menschen konkret zu verstehen, auch wie es verläuft zwischen dem Tod und einer neuen Ge­burt.",
        "Denn ohne das Verständnis für dieses leiblose Leben des Men­schen ist auch ein wirkliches Verständnis nicht möglich für das Dasein des Menschen innerhalb des physischen Leibes, namentlich nicht mög­lich ein Verständnis für die Aufgabe des Menschen innerhalb des phy­sischen Leibes."
      ],
      [
        "Gewissermaßen abstrakt gesprochen: Es ist der gegenwärtigen Menschheit notwendig, die inneren Impulse des Zeitgeistes, jenes Zeit-geistes, der im engeren Sinne seit dem Jahre 1879 waltet, im weiteren Sinne schon waltet seit der Mitte des 15.",
        "Jahrhunderts, wirklich in sich aufzunehmen, mit den Impulsen dieses Zeitgeistes sich bekanntzu­machen.",
        "Davon haben viele Menschen - wenigstens von dem, was eigentlich mit dem eben ausgesprochenen Worte gemeint ist -, haben die meisten Menschen der Gegenwart kaum die allerspärlichste Ahnung.",
        "Ich habe es oft in diesen Betrachtungen gesagt: Das, was unserer Ju­gend - unserer jüngeren Jugend und unserer älteren Jugend - als soge­nannte Geschichte mitgeteilt wird, ist zumeist auf der einen Seite Fable convenue, auf der andern Seite vielfach wertloses Zeug.",
        "Soll wirkliche Geschichte entstehen, dann muß erst durchschaut werden das, was die"
      ],
      [
        "Impulse der letzten Jahrhunderte waren und was in diesen Impulsen sich gerade in unserem Zeitalter ändern muß.",
        "Man hat heute kaum eine Ahnung davon, welcher gewaltige Umschwung im menschlichen Denken und Fühlen eingetreten ist mit dem Beginne des fünften nach-atlantischen Zeitraums, mit der Mitte des 15.",
        "Jahrhunderts.",
        "Das un­sinnigste Wort in bezug auf die Entwickelung gilt ja vielen Leuten heute als ein Geleitwort.",
        "Dieses unsinnige Wort ist: Die Natur macht keine Sprünge. - So wie die Natur ihren gewaltigen Sprung macht von dem grünen Laubblatt zu dem farbigen Blumenblatt, so macht die Natur ihre Sprünge überall.",
        "Und es ist nicht ein allgemeiner t)ber­gang gewesen aus dem vierten nachatlantischen Zeitraum zu der ersten Hälfte des 15.Jahrhunderts, zu dem fünften nachatlantischen Zeit­raum, angefangen von der zweiten Hälfte des 15.Jahrhunderts, son­dern es ist ein gewaltiger Umschwung dagewesen.",
        "Orientieren kann man sich nur, wenn man wenigstens einigermaßen vergleichen kann das, was die paar Jahrhunderte des fünften nachatlantischen Zeit­raums bisher gebracht haben, mit dem, was vorangegangen ist; denn beide Dinge sind voneinander grundverschieden.",
        "Von einem gewissen Gesichtspunkte aus möchte ich Ihren Geistesblick heute auf diese An­gelegenheit lenken."
      ],
      [
        "Hat man sich bekanntgemacht mit dem, was man lernen kann aus dem heutigen Inhalt der Wissenschaft, dem heutigen Inhalt der Men­schenbildung - falls man das törichte Wort «Bildung» gebrauchen darf -, hat man sich aus dem heraus heute vorbereitet und nimmt dann Schriften noch aus dem 15.",
        "Jahrhundert in die Hand, so versteht man sie gerade dann nicht, wenn man ein besonders gelehrter Kopf der heutigen Zeit ist."
      ],
      [
        "Nun müssen Sie mich nicht mißverstehen.",
        "Ich kann nach allen Vor­aussetzungen unserer anthroposophisch orientierten Geisteswissenschaft keineswegs dafür sein, daß alte Dinge aufgewärmt werden.",
        "Jenes Ge­rede, das so vielfach durch die Welt heute geht von der Notwendigkeit der Aufwärmung aller möglichen alten Schmöker und aller möglichen alten Anschauungen, das kann nicht etwa auch auf dem Felde unserer anthroposophisch orientierten Geisteswissenschaft getrieben werden, weil diese anthroposophisch orientierte Geisteswissenschaft aus dem"
      ],
      [
        "unmittelbaren Geistesleben selbst heraus dasjenige zu schöpfen hat, was sich gerade für die Gegenwart zu offenbaren hat und weil sich in un­serer Zeit für den Empfangenden Bedeutsames offenbart.",
        "Aber klar­machen kann man sich manches, wenn man den Blick hinrichtet auf die Art, wie heute gerade ein recht gelehrter Kopf sich verhalten kann zu den Dingen, die als Weisheitsgut erhalten sind - wir brauchen gar nicht weiter zurückzugehen, sagen wir als ins 14., 15.",
        "Jahrhundert.",
        "Wenn heute ein recht gelehrter Kopf zum Beispiel in die Hand nimmt die Werke des sogenannten Basilius Valentinus, des berühmten Adepten aus dem 15.",
        "Jahrhundert, so weiß er gar nichts mit ihnen anzufangen.",
        "Was man heute gewöhnlich erfährt, wenn Leute so etwas wie den Basilius Valentinus in die Hand nehmen - es könnten auch andere sein, aber ich führe ihn an, weil er der berühmteste Adept des 15.",
        "Jahrhun-derts ist -, das ist so, daß sie entweder Unsinn reden, dilettantisches Zeug, indem sie sich vollpfropfen mit dem, was doch nicht verstanden werden kann, aber an das Unverstandene glauben, oder aber daß sie als gelehrte Knöpfe allerlei Unsinn reden, impotentes Zeug reden über das, was ihnen aus Basilius Valentinus entgegenströmt."
      ],
      [
        "Liest man mit Kennerblick, mit wirklichem spirituellem Kenner­blick so etwas wie den Basilius Valentinus, dann kommt man sehr bald darauf, daß in diesem Basilius Valentinus eine Weisheit enthalten ist, die allerdings unbrauchbar ist für die Menschen der Gegenwart, welche eben die landläufigen Interessen der Gegenwart haben, daß aber in diesem Basilius Valentinus um so mehr Weisheit von der Art ist, wie sie auftritt, wenn man sich in Verbindung bringen kann mit den Seelen, welche ihr Dasein haben zwischen dem Tod und einer neuen Geburt.",
        "Man kann sagen, was den Menschen gegenwärtig unnötig erscheint, diese Weisheit, wie sie in Basilius Valentinus steht, die haben um so mehr diejenigen Menschen nötig, welche zwischen dem Tod und einer neuen Geburt leben.",
        "Auch diese brauchen nicht den Basilius Valentinus zu studieren, denn wir haben in der anthroposophisch orientierten Gei­steswissenschaft etwas, was die Sprache spricht, die gemeinsam für die sogenannten Lebenden und für die sogenannten Toten ist.",
        "Es genügt das, was die anthroposophisch orientierte Geisteswissenschaft gibt, um in der uns bekannten Weise auch mit den Toten zu reden.",
        "Aber gewissermaßen"
      ],
      [
        "als eine historische Tatsache führe ich es an, daß die Art, wie der Tote aufnimmt das, was Weltenwissen ist, eine gewisse Verwandt­schaft hat mit dem, was solche Schriften wie die des Basilius Valentinus bringen.",
        "Denn Basilius Valentinus redet von allerlei chemischen Ver­richtungen, redet scheinbar von demjenigen, was man mit Metall und andern Stoffen in Retorten und Schmelztiegeln unternimmt.",
        "In Wirk­lichkeit redet er von demjenigen Wissen, das sich die Toten aneignen müssen, wenn sie ihre Verrichtungen pflegen wollen in jenem untersten Reiche, von dem ich gesprochen habe, das also das unterste Reich eben für sie ist, in dem tierischen Reiche.",
        "Er redet von dem, was man zu kennen hat von jenen Impulsen, die aus der geistigen Welt heraus kommen, um den Mikrokosmos selbst aus dem Makrokosmos heraus zu begreifen.",
        "Dies ist ja die Erkenntnistätigkeit der Seele zwischen dem Tod und einer neuen Geburt, die aber heute nur richtig verrichtet wer-den kann,wenn sie vorbereitet wird zwischen der Geburt und dem Tode.",
        "Das war als ein atavistisches Erbgut, als ein uraltes Weisheitserbe noch bis ins 15.",
        "Jahrhundert vorhanden.",
        "Und Basilius Valentinus redet von diesem uralten Weisheitserbe, redet von den Geheimnissen, wie der Mensch zusammenhängt mit dem Makrokosmos, redet wirkliche, gött­liche Weisheit - in Imaginationen, wie wir heute sagen würden."
      ],
      [
        "Diese Art sich zu dem Kosmos zu verhalten im Erkennen, ist im Laufe der letzten Jahrhunderte verschwunden.",
        "Sie muß wieder er­worben werden - auf eine geistigere Weise, als sie vor dem 15.",
        "Jahr-hundert vorhanden war, muß sie wiederum erworben werden.",
        "Denn sie muß geübt werden sowohl in der Wissenschaft wie auch in dem sozialpolitischen Leben.",
        "Ein Heil ist der Menschheit nur möglich, wenn solche Ziele verfolgt werden.",
        "Und das muß erkannt werden, daß der Menschheit ein Heil nur unter dem Einfluß solcher Ziele mög­lich ist."
      ],
      [
        "Ein gewissermaßen Uroffenbarung zu nennendes, uraltes Erbgut ging durch die Jahrhunderte herunter.",
        "Im materialistischen fünften nachatlantischen Zeitalter verlor sie sich.",
        "Erworben muß sie wiederum in neuer Weise werden.",
        "Erworben kann sie nur werden, wenn der Mensch sie erwirbt, wie wir oft und oft auseinandergesetzt haben, indem er sich durchdringt, aber tätig, willentlich durchdringt mit dem"
      ],
      [
        "Paulinischen Aber wie gesagt, gerade der gelehrte Kopf der Gegenwart, wie steht er vor dieser alten Weisheit?",
        "So etwa, wie jener Gelehrte, der die Worte gesprochen hat: «Die letzte und wichtigste Operation von Basilius Valentinus ist die zehn Monate hindurch allmählich gesteigerte Erhit­zung des philosophischen Quecksilbers und Goldes im Philosophen-Ofen, wodurch der den und dieser den gebärt, der wieder den er­zeugt.",
        "Dieser aber (eine rote Substanz) ist der Stein der Weisen, der sich bis zur Unendlichkeit vermehren kann.",
        "Man vermag leider nicht» -sagt der moderne wissenschaftliche Kopf -, «man vermag leider nicht zu begreifen, wie jemand, und wäre es der geschickteste und begeistert­ste Adept (so wurden die Männer genannt, die das Geheimnis des Stei­nes der Weisen besaßen) solchen Vorschriften folgen könnte.»"
      ],
      [
        "So Theodor Svedberg in Uppsala, der ein Buch über diese Dinge von dem wissenschaftlichen Standpunkt der Gegenwart geschrieben hat und der in dieser Beziehung nur der Repräsentant all der gelehrten Köpfe ist, die eben sagen müssen: Man vermag leider nicht zu begrei­fen. - Es ist noch das beste, wenn sie das sagen: Man vermag leider nicht zu begreifen. - Für sie alle hat Basilius Valentinus schon die nötigen abfertigenden Worte selbst hingeschrieben, indem er in seinen «Zwölf Schlüsseln zum Weltenall und dessen Verständnis» schreibt:"
      ],
      [
        "«Verstehest du jetzo, was ich rede, so hast du mit dem Schlüssel das erste Schloß eröffnet und den Riegel des Anlaufs zurückgetrieben.",
        "Kannst du aber noch kein Licht drinnen ergründen, so wird dich auch kein gläsern Gesichte befördern, noch natürliche Augen vermögen zu helfen, das Letzte zu finden, das du im Anfange gemangelt hast.",
        "Dann"
      ],
      [
        "will ich nicht ferner reden von diesem Schlüssel, wie mich Lucius Papirius gelehret hat.»"
      ],
      [
        "So spricht Basilius Valentinus schon zu all den Nachfahren, die dem alten Weisheitsgut gegenüber höchstens die Worte haben: Man vermag leider nicht zu begreifen. - Aber diese Menschen der Gegenwart haben ja auch etwas anderes zu tun, als das Geistige zu begreifen!",
        "Diese Men­schen der Gegenwart müssen sich mit allerlei andern Dingen befassen; und wenn vom Geiste irgendwie die Rede ist, so müssen sie sich vor allen Dingen damit befassen, dieses Reden vom Geiste zu verleumden.",
        "Und ungeheuer viel Zeit wird heute aufgebraucht dazu, das Reden vom Geiste zu verleumden."
      ],
      [
        "Zu dem Berliner Unsinn des Max Dessoir kann noch hinzugefügt werden - ich habe das Geschreibsel noch nicht selbst lesen können, aber es ist mir einiges erzählt worden - das holländische Konterfei des Phi­losophen Bolland, der sich ja einige Verdienste für die philosophische Entwickelung dadurch erworben hat, daß er durch sein Nachreden Hartmannscher und Hegelscher Brocken die philosophische Jugend Hollands in Begeisterung versetzt hat, aber auch, wie es scheint, nicht umhin konnte, in der letzten Zeit seine philosophische Unproduktivi­tät dazu zu verwenden, unsere Geisteswissenschaft durch allerlei un­wahres Zeug zu verleumden."
      ],
      [
        "Das muß immer wieder und wiederum hervorgehoben werden, denn es gehört schon zum wirklichen Aufnehmen der Geisteswissenschaft in unsere Seele auch die Aufmerksamkeit auf die Art und Weise, wie die Gegenwart in ihrer geisteswissenschaftlichen Impotenz sich verhält zu dem, was der Menschheit notwendig ist."
      ],
      [
        "Diese gegenwärtige Wissenschaft - ich spreche da nicht von der äußeren Wissenschaft, die ich, wie Sie wissen, voll anerkenne, wenn ich auch nicht jedem Naturforscher nachlaufe -, aber das, was vielfach sich Philosophie und dergleichen nennt, ist in der Gegenwart nicht viel mehr als abstraktes Gerede, welches in der völligen Verwirrung über die Begriffe von Kürbis und Flasche geführt wird.",
        "Leider geschieht es bei uns auch noch viel zu häufig, daß wir immer wieder und wieder auf das unsinnige Gerede namentlich der gegenwärtigen Philosophen hin­einfallen und sogar zuweilen froh sind, wenn da oder dort irgendein"
      ],
      [
        "philosophischer Knopf dies oder jenes, sagen wir, nicht zu tadeln fin­det an dem, was anthroposophisch orientierte Geisteswissenschaft will.",
        "Als ob das nicht, wenn er es nicht zu tadeln findet, mindestens seine Pflicht und Schuldigkeit wäre!",
        "Wir brauchen uns gar nicht zu freuen, so wie es viele unter uns tun, wenn von dieser oder jener Seite einmal auch ein lobendes Wörtchen abfällt.",
        "Auch diese lobenden Wörtchen sind ja zumeist nicht gerade von einem großen Verständnisse getragen.",
        "Aber wir müssen uns gefaßt machen darauf, daß solche Verleumder von der Sorte Dessoirs oder Bollands immer wieder und wieder auf­treten werden, und daß sie sich in der nächsten Zeit gar sich vermehren werden.",
        "Denn sie müssen sich doch mit etwas beschäftigen, diese Leute!",
        "Und da sie viel zu bequem sind, einzugehen auf das, was aus der geisti­gen Welt zum Heile der Menschheit im gegenwärtigen Zeitalter geholt werden muß, so müssen sie sich damit beschäftigen, das, was geholt wird, zu verleumden."
      ],
      [
        "Basilius Valentinus, sagte ich, bot noch ein uraltes, atavistisch über­kommenes Erbgut, eine Wissenschaft von der Art, wie der Mensch her­ausgeschaffen wird aus dem kosmischen All, wie sie vor allen Dingen die Wissenschaft der vom Leibe befreiten Seele ist, wie aber auch sein muß die Wissenschaft, die mitwirken will bei allem, was nicht bloß äußere Natur ist.",
        "Gefördert kann diese Wissenschaft nur werden, wenn zu dem reinen, und zwar materialistisch orientierten intellektuellen Elemente der Neuzeit die Erkenntnis des Willens aufgenommen wird, des Willens, der, wenn er als Wille wirklich erkannt wird, nur in seiner spirituellen Natur erkannt werden kann, weil er nur spirituell sich äußert in dem gegenwärtigen Entwickelungsstadium der Menschheit.",
        "Ein nicht feiges Heraufholen der Lebensimpulse aus der Sphäre des Willens, das ist das, was der Gegenwart so sehr mangelt.",
        "Die Gegen­wart will vor allen Dingen reden, reden!",
        "Das ist gut, aber nur auf Grundlage eines wirklichen Erkennens.",
        "Nicht das letztere will die Ge­genwart - reden will jeder, reden will jeder, auch auf nichtige Voraus­setzungen hin.",
        "Und wir haben ja gesehen, daß in diesem Unberücksich­tigtlassen des spirituellen Elementes in der Welt gerade das Unglück unseres Zeitalters liegt.",
        "Man meint es in der Gegenwart nur dann ehr­lich mit der Entwickelung der Menschheit, wenn man sich wirklich einlassen"
      ],
      [
        "will auf die Ergründung derjenigen Willensimpulse, die notwen­dig sind, um die Wogen der Menschheitsentwickelung weiterzutreiben."
      ],
      [
        "Selbstverständlich müssen diese Dinge nicht persönlich genommen werden.",
        "An diesem oder jenem Platz des Lebens kann selbstverständ­lich jeder sagen: Ja, was soll ich tun? - Ganz gewiß, das kann auch niemals die Anforderung sein, daß wir heute begreifen, was wir tun sollen, um morgen irgendwie die ersten Schritte zu tun, um irgend etwas Weltepochemachendes zu unternehmen."
      ],
      [
        "Was wir zu unternehmen haben, wird uns das Karma schon bringen.",
        "Was wir aber zu tun haben, das ist: die Augen - ich meine die Augen der Seele - aufzumachen, um wirklich zu erkennen, um wirklich die Zeit zu durchschauen."
      ],
      [
        "Das, was wir zu tun haben, ist: diese Zeit nicht zu verschlafen, sondern hinein-zuschauen in das, was geschieht!",
        "Was der Materialismus des fünften nachatlantischen Zeitraumes den Menschen genommen hat, notwendig nehmen mußte, weil sich die Menschen zunächst rein persönlich orien­tieren mußten, das sind umfassende Ideen, wie sie gerade die Ausflüsse des Zeitgeistes sind, das sind umfassende Ideen, die wir gemeinsam haben können mit den sogenannten Toten."
      ],
      [
        "Das intellektualistische Zeug, das in unserer Zeit so groß geworden ist, hat nicht nur die Men­schenseelen ergriffen, das hat deshalb auch ergriffen die soziale und geschichtliche Entwickelung des Zeitalters selbst.",
        "Der Mensch hat vor der Notwendigkeit der Geschichte - mit einem gewissen Recht, denn an diesen Dingen soll nicht Kritik geübt werden, sondern sie sollen charakterisiert werden -, der Mensch hat mit einem gewissen Recht manches von dem, was er früher aus seiner Menschheitsinitiative her­aus, ich meine auch aus der organischen Menschheitsinitiative heraus verrichtet hat, an die Maschine abgegeben."
      ],
      [
        "Das materialistische Zeit­alter ist ja zu gleicher Zeit das Maschinenzeitalter.",
        "Und dieses Ma­schinenzeitalter formt mit den Maschinen nicht nur dasjenige, was es zum gewöhnlichen Leben braucht, sondern der Krieg selbst ist zur Pflege einer großen Maschinerie geworden."
      ],
      [
        "Es konnte nicht anders kommen, denn die Menschheit hat im Laufe der letzten Jahrhunderte nicht nur eine gewisse Menschheitsschicht ausgebildet, sondern inner­halb dieser Menschheitsschicht auch Anschauungen kultiviert, die vor allen Dingen darauf bedacht sind, nur das als wissenschaftlich gelten"
      ],
      [
        "zu lassen, was sich realisieren kann innerhalb der äußeren sozialen Ordnung im Werden von Maschinen: entweder im Werden von mecha­nischen Maschinen - wenn ich diese Tautologie, den Pleonasmus ge­brauchen darf - oder aber im Werden von sozialen Maschinen.",
        "Denn eine große Maschinerie ist zum Beispiel bis vor dem Kriege die Finanz­gebarung gewesen, die internationale Finanzgebarung der Welt.",
        "Alles ist maschinenmäßig gewesen.",
        "An das Maschinenmäßige hat der Mensch viel abgegeben.",
        "Zurückbehalten wollte eine gewisse Schicht der Mensch­heit von diesem Maschinenmäßigen im Grunde genommen nur das, was die triviale Lebensnotwendigkeit vergnüglich macht.",
        "Man könnte sagen: Im Winter schuften, im Sommer ins Bad gehen und nur so viel denken, als notwendig ist, damit die Weltenmaschinerie für einen schuftet, das wurde Signatur des Zeitalters."
      ],
      [
        "Nicht als ob das hätte unterbleiben können.",
        "DieseWeltenmaschinerje mußte heraufkommen, das ist ganz selbstverständlich.",
        "An dem Ge­schehenen Kritik zu üben, ist ein Dilettantismus, an dem sich Geistes­wissenschaft nicht beteiligen kann.",
        "Aber durchschaut, und in der Eigen­art, die es hat, erkannt werden muß die Sache, denn nur dann wird man demgegenüber die richtigen Willensimpulse entwickeln können."
      ],
      [
        "Immer wiederum sind die Menschen gekommen, welche die ange­messenen Ideen schon ausgesprochen haben für dieses Zeitalter.",
        "Aber diese Aussprecher der angemessenen Ideen wurden gerade in der zwei­ten Hälfte des 19.",
        "Jahrhunderts und im Beginne des 20.",
        "Jahrhunderts eigentlich als unmögliche menschliche Persönlichkeiten betrachtet.",
        "Über solche Köpfe, die klar sahen, wie die soziale Struktur der Mensch­heit über die Erde hin sein muß unter dem Einfluß des Maschinenzeit-alters, über solche Köpfe wie Bright oder Cobden ist die nachfolgende Menschheit zur Tagesordnung übergegangen - diese nachfolgende Menschheit, die allerdings etwas Geisteskraft hätte aufwenden müssen, um gerade das Angemessene der Brightschen und Cobdenschen Ideen für das Maschinenzeitalter herauszufinden!",
        "Aber den Willen in den Intellekt hineinzudrängen, um die Wirklichkeit zu durchschauen, das ist eben eine Kraftanstrengung, vor der die Menschen der Gegenwart zurückschrecken.",
        "Sie wollen nicht ihre Gedanken von Willen durch­tränken.",
        "Sie wollen ihre Gedanken sentimental hinzielen lassen über"
      ],
      [
        "dasjenige, was ihnen, wie sie sagen, wohlig ums Herz macht, wenn sie sich erheben wollen.",
        "Und unter dem Einflusse eines solchen willens­entblößten Denkens, dem es aber so warm und wohl wird beim Schwätzen in Sentimentalitäten, gewöhnt man sich daran, auch die wichtigsten Fragen mit einem willenlosen, feigen Denken zu ergreifen.",
        "Man gewöhnt sich vor allen Dingen daran, von der weltgeschichtlichen Entwickelung nichts zu lernen.",
        "Ist denn die Menschheit gegenwärtig bereit zu lernen?",
        "Auch das soll nicht als eine Kritik ausgesprochen wer­den, sondern nur als eine Charakteristik."
      ],
      [
        "All dasjenige, was ich sage, ist nicht eingegeben von dem Gesichts­punkt der Kritik, sondern ist eingegeben von dem Gesichtspunkt der Anregung des Willens.",
        "Klarstellen muß man, wie man in seine Ge­danken den Willensimpuis hineinleitet, der zum Heile der Menschheit dienen kann."
      ],
      [
        "Leider sind die Menschen der Gegenwart zu wenig ge­neigt, zu lernen.",
        "Sie lassen die Dinge an sich vorübergehen und bereden sie und glauben, mit dem Bereden auch das Willenselement zu meistern.",
        "Wieviel ist geschwätzt, wesenlos geschwätzt worden in der Zeit, in der sich die unheilvollen Ursachen dieser Weltenkatastrophe vorbereitet haben!"
      ],
      [
        "Wieviel ist geschwätzt worden auf die Anregung der Friedens­manifest-Firlefanzereien des Zaren hin!",
        "Das konnte geschehen, denn man kann sagen, daß eben erst gelernt werden mußte, daß es sich um Friedensmanifest-Firlefanzereien handelte, und daß all dieses Ge­schwätz, das daran geknüpft worden ist, Millionen und Millionen Meilen weit entfernt war von der Möglichkeit, Willensimpulse anzu­regen in der Menschheit."
      ],
      [
        "Aber gelernt sollte werden.",
        "Wird gelernt?",
        "Nein, es wird vorläufig nicht gelernt - und nicht darum handelt es sich, das Nichtlernen zu bemängeln, sondern darum handelt es sich, dieses Nichtlernen zu durchschauen, damit man lerne."
      ],
      [
        "Was ist an die Stelle getreten, an die Stelle des Schwätzens über allerlei Weltenziele in Anknüpfung an die Friedensmanifest-Firlefanzereien des nunmehr abgetanen Zaren?",
        "Der andere Unsinn von den Friedensmanifest-Firle­fanzereien des Schwätzers Woodrow Wilson!"
      ],
      [
        "Genau dieselbe Sache anstelle derselben Sache!",
        "Das ist zu lernen, daß die Menschheit nicht lernen will.",
        "Und in der Erkenntnis von diesem Nichtlernenwollen wird sich anfachen in unserer Seele der heilige Wille zum rechten Wollen,"
      ],
      [
        "das hervorgehen muß aus dem rechten Durchschauen desjenigen, was wirkt und webt in unserer Zeit."
      ],
      [
        "Ich habe in den öffentlichen Vorträgen gesagt, daß im Grunde ge­nommen das, was sich im Lauf der letzten vier Jahrhunderte im ge­schichtlichen Traum der Menschheit heraufentwickelt hat, wie ein Weltenprogramm ausgesprochen worden ist im Lauf des 19.Jahrhun-derts von solchen Leuten wie Karl Marx und ähnlichen Leuten.",
        "Die Impulse sind schon vergangen gewesen, als es ausgesprochen worden ist; aber es war damit das ausgesprochen, was im Grunde genommen die Unterlage war für das geschichtliche Werden der letzten vier Jahr­hunderte."
      ],
      [
        "Wie liegt die Sache?",
        "Die Sache liegt heute so, daß die breiteren menschlichen Schichten alles Denken über soziale Zusammenhänge aufgegeben haben.",
        "Man überläßt es den Professoren der National­ökonomie, die ja im Verlauf der letzten Jahrhunderte, namentlich Jahr­zehnte genug Unsinn geschwätzt haben."
      ],
      [
        "Wirkliches soziales Denken, das hervorzugehen hat aus der Erkenntnis der aus der Geisteswelt kommenden Impulse, ist in den sogenannten führenden Schichten ab­handen gekommen.",
        "Einzig und allein eine Schicht hat weltgeschicht­liche Ideen in der letzten Zeit in die Welt gesetzt: diejenige Schicht, die in okkulter Auffassung Brüder des Schattens sind gegenüber den Brü­dern der bürgerlichen Parteien der letzten Jahrhunderte."
      ],
      [
        "Weltgeschicht­liche Ideen, wenn auch Schattenideen, hat die Sozialdemokratie ge­bracht, graue Schattenideen von besonders gefährlicher Art, da sie ganz imprägniert sind von dem Geiste der letzten Jahrhunderte.",
        "Aber weit-geschichtliche Ideen sind es, die den andern Schichten der Menschheit völlig gemangelt haben."
      ],
      [
        "Denn die andern Schichten der Menschheit, sie hätten sie entlehnen müssen aus der geistigen Welt; sie hätten nötig gehabt, nicht im allgemeinen in salbungsvoller Weise ihre religiösen, ihre sozialen, ihre geschichtlichen Ideen zu entwickeln, sondern auf fester Erkenntnisgrundlage das soziale Werden zu durchschauen.",
        "Nie­mand wird das soziale Werden in Wirklichkeit durchschauen, der sich nicht in die Lage versetzen will, dies von Ausgangspunkten zu tun, die diesen unseren Betrachtungen in den letzten Wochen hier zugrunde gelegen haben."
      ],
      [
        "Dafür spricht das Beste, was die sogenannten Lebenden heute aus der geistigen Welt empfangen können, dafür spricht das Beste, was die Toten uns offenbaren aus ihrem Leben zwischen dem Tod und einer neuen Geburt.",
        "Dafür spricht jene neue Auffassung des Mysteriums von Golgatha, der wir durch die Vertiefung der anthroposophisch orientier­ten Geisteswissenschaft entgegengehen müssen.",
        "Dafür spricht alles das, was wir in dieser ernsten Zeit als ernste Weihnachtsgedanken uns durch die Seele ziehen lassen sollen.",
        "Denn zum Heil der Menschheit ist das Wesen in die Erdenentwickelung eingetreten, dessen Geburt im Weih­nachtsfeste gefeiert wird, nicht zum behaglichen Zur-Seele-Reden bloß, sondern dazu, daß diese Menschenseele sich durchdringt mit - wenn ich das paradoxe Wort gebrauchen darf - dem Willen zum Willen, dem Willen zum Wollen.",
        "Durchdringt dieser Wille zum Wollen die Menschenseelen, dann wird dies den Impuls bedeuten zu einer Sehn­sucht nach wirklich neuen Ideen, denn die alten sind abgebraucht.",
        "Manchmal können wir nicht einmal die Worte mehr gebrauchen."
      ],
      [
        "Wir leben in einer katastrophalen Zeit.",
        "Das, was geschieht, Krieg zu nennen, ist fast schon anachronistisch, ist nur aus der alten Gewohn­heit entstanden, die Flasche noch Kürbis zu nennen.",
        "Ebensowenig aber, wie das, was geschieht, Krieg zu nennen ist, ebensowenig sollte in leicht­fertiger Weise die wohlbehäbige Hoffnung in der alten Weise von Frieden sprechen!",
        "Gewaltige Zeichen kündigen sich in unserer Zeit an, und der Menschheit obliegt es, zu versuchen, diese Zeichen zu verstehen.",
        "In den Ereignissen selber wandeln sich die Ereignisse um. 1914 hat ein Weltenereignis begonnen, das man vielleicht im Anfange nennen konnte einen Krieg zwischen der Entente und den europäischen Mittelmächten.",
        "Unter dem aber, was so genannt wird, waltet etwas wesentlich anderes, stehen einander ganz andere Feinde gegenüber!",
        "Und in unseren Tagen kündigt sich uns an ein ernstes Symptom von dem, was glimmend wal­tet unter dem, was wir recht uneigentlich noch einen Krieg zwischen der Entente und den Mittelmächten nennen, kündigt sich uns an ein Symptom, das da besteht in dem traurigen Aufeinanderprallen der Bevölkerung Nord- und Südrußlands, ein bedeutungsvolles Symptom, wenn es auch vielleicht noch verlöschen kann zunächst, ein bedeutungs­volles Symptom für das, was unter den Ereignissen glimmt.",
        "Die Menschen"
      ],
      [
        "lieben es nicht, daß die Dinge heute beim rechten Namen genannt werden, weil sie das Wollen nicht wollen, weil sie sich lieber über den Ernst der Zeit hinwegsetzen, solange es nur irgend geht, solange der Magen nicht allzustark knurrt.",
        "Dasjenige, um was es sich handelt, das ist, daß wir wirklich den Willen entwickeln, die tieferen Grundlagen der Ereignisse zu schauen, daß wir endlich einmal den Willen ent­wickeln, alle Oberflächlichkeit abzutun, um mit den Seelenaugen den Dingen ins Antlitz zu schauen."
      ],
      [
        "Wir werden, indem wir das, was wir jetzt in einer Art von Über­schau durch unsere Seele haben ziehen lassen, in den nächsten Vorträgen ergänzend auf mancherlei noch hinzuweisen haben, was zusammen­hängt mit den tieferen Impulsen, denen wir uns in diesen Betrachtungen hingegeben haben.",
        "Aber ich glaube, in dieser Zeit ehrt man die geheim­nisvolle dreifache Notwendigkeit, welche durch das Weltenwerden geht und die der Bruder ist von der Menschenfreiheit und der Freiheit der andern Geschöpfe, am meisten, wenn man sich keinen Schleier vor das Auge weben will.",
        "Hier auf dieser Erde müssen wir Freiheit begrei­fen.",
        "Auch in dieser Beziehung lernt der Blick des Gegenwartsmenschen sehr viel, wenn er sich zu den Toten hinrichtet; denn der Tote weiß, daß ihm Freiheit in dem Leben zwischen dem Tod und einer neuen Ge­burt durch das wird, was er sich mitbringt aus dem Leben zwischen der Geburt und dem Tode.",
        "Eingebettet sein in die Intelligenzen der höheren Hierarchien, das ist etwas, was uns wie eine Naturnotwendigkeit wird, wenn wir durch die Pforte des Todes gehen, wenn wir drüben leben -eingebettet sein in den Intelligenzen der höheren Hierarchien und deren Impulsen folgen, wie hier ein Naturereignis mit Notwendigkeit den Naturimpulsen folgt.",
        "Dann sind wir noch, nachdem wir durch die Pforte des Todes geschritten sind, frei, wenn wir in unserer Seele mit hinübertragen in die geistige Welt dasjenige, was wir uns hier als Wis­sen vom geistigen Werden und geistigen Wesen erwerben können."
      ],
      [
        "Dies ist etwas, was nun auch im tiefsten Sinne mit dem Mysterium von Golgatha zusammenhängt.",
        "Und weil dies so ist, glaube ich, daß auch Weihnachtsbetrachtungen in dieser Zeit nicht sentimentale sein dürfen, sondern solche sein müssen, welche an den Willen zum Wollen appellieren."
      ],
      [
        "Denn man nehme die Evangelien: wieviel ist in den Evangelien ge­rade an Appell zum Willen zum Wollen!",
        "Die Evangelien sind keine sentimentalen Schriften, die Evangelien sind Schriften, die allerdings zu dem Allerbescheidensten der Menschennatur sprechen, aber sie sind auch Schriften, welche das, was der Mensch an Stärke des Willens auf­bringen kann, in den Menschen erwecken wollen.",
        "Nicht nur dazu sollen die Weihnachtskerzen brennen, daß wir uns in einer gewissen Weise wollüstigen Betrachtungen hingeben, sondern auch dazu sollen sie bren­nen, daß sie Symbole seien für die Anfachung des der Welt zum Heile dienenden Willenslichtes."
      ],
      [
        "Die Menschheit hat viel nachzuholen; und es ist nachzuholen!",
        "Denn indem sie die Kraft entwickeln wird, welche in diesem Nachholen liegt, wird sie rechte heilsame Kräfte entwickeln, um aus der gegenwärtigen katastrophalen Zeit herauszukommen.",
        "Das ist der Menschheit nicht zur Aufgabe gesetzt worden, bloß hineinzukommen in diese Zeiten; viel wichtiger ist die Aufgabe, aus ihnen herauszukommen.",
        "Diese Auf­gabe steht als ein heiliges Zeichen, wie ich glaube, mit Flammenschrift geschrieben hinter all den Weihnachtskerzen, die nun schon seit vier Jahren in anderer Weise vor unserer Seele brennen als manches frühere Jahr!"
      ],
      [
        "Morgen treffen wir uns um vier Uhr im Basler Zweig zu einer Weih-nachtsfeier.",
        "Montag um viereinhalb werden wir uns hier versammeln zur ersten Aufführung des «Paradeis-Spieles», und ich werde dann daranschließen eine Weihnachtsbetrachtung für diejenigen unserer Freunde, die nicht durch irgend etwas zu Hause abgehalten sind, son­dern die gerade jetzt da sind, sich den Arbeiten und dergleichen wid­mend, und die an diesem Tage vielleicht ihr Weihnachten am liebsten hier verbringen mögen."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "HINWEISE",
    "paragraphs": [
      "9    Zu den Betrachtungen, die wir angestellt haben: Rudolf Steiner: «Die Spiri­tuellen Hintergründe der äußeren Welt - Der Sturz der Geister der Finsternis«, 14 Vorträge Dornach 1917. Bibl.-Nr. 177, Gesamtausgabe Dornach 1965.",
      "11    Rudolf Steiner: «Von Seelenrätseln« (Berlin 1917), Bibl.-Nr. 21, Gesamtausgabe Dornach 1976.",
      "21    eine Broschüre: Adolf von Strümpell, 1853-1925, zuletzt Professor der Medizin in Leipzig. «Die Schädigung der Nerven und des geistigen Lebens durch den Krieg«, Leipzig 1917, S. 22ff.",
      "31    Jch will Ihnen ein richtiges Beispiel anführen: Siehe Vortrag vom 7. November",
      "1917 «Anthroposophie und Geschichtswissenschaft« in Rudolf Steiner «Die Er­gänzung heutiger Wissenschaften durch Anthroposophie«, 8 Vorträge Zürich 1917/18. Bibl.-Nr. 73, Gesamtausgabe Dornach 1973.",
      "49    Zyklus über das Leben zwischen dem Tod und einer neuen Geburt: Rudolf Steiner: «Inneres Wesen des Menschen und Leben zwischen Tod und neuer Ge­burt«, 8 Vorträge Wien 1914. Bibl.-Nr. 153, Gesamtausgabe Dornach 1959.",
      "Mitternachtsstunde des Daseins: Sechstes Bild in «Der Seelen Erwachen», in Rudolf Steiner: «Vier Mysteriendramen», Bibl.-Nr. 14, Gesamtausgabe Dorn-ach 1962.",
      "69    Otto Heinrich Jäger, 1828-1912. Schrieb als Student in Tübingen die preis-gekrönte Arbeit «Die Gymnastik der Hellenen«. 1856 wurde er Professor der Philosophie in Zürich. 1859 erschien seine Schrift «Die Freiheitslehre als System der Philosophie«.",
      "meine Freiheitsphilosophie: Rudolf Steiner: «Die Philosophie der Freiheit» (Berlin 1894). Bibl.-Nr. 4, Gesamtausgabe Dornach 1973.",
      "76    von den entsprechenden okkulten Schulen: Siehe Rudolf Steiner: «Die okkulre Bewegung im neunzehnten Jahrhundert und ihre Beziehung zur Weltkultur», 19 Vorträge Dornach 1915. Bibl.-Nr. 254, Gesamtausgabe Dornach 1969.",
      "78    von einem andern Gesichtspunkte aus: Rudolf Steiner: «Welche Bedeutung hat die okkulte Entwickelung des Menschen für seine Hüllen - physischen Leib, Atherleib, Astralleib - und sein Selbst?», 10 Vorträge Den Haag 1913. Bibl.­Nr.145, Gesamtausgabe Dornach 1976; «Weltwesen und Ichheit«, 7 Vorträge Berlin 1915. Bibl.-Nr. 169, Gesamtausgabe Dornach 1963.",
      "Chiron, der weise Kentaur der griechischen Mythologie, Lehrer des Askulap, Jason und Achilles.",
      "80    Es gibt einen Zyklus: Rudolf Steiner: «Das Leben zwischen dem Tode und der neuen Geburt im Verhältnis zu den kosmischen Tatsachen«, 10 Vorträge Berlin 1912/13. Bibl.-Nr. 141, Gesamtausgabe Dornach 1964.",
      "112    Da ist die Notwendigkeit, da ist Gott: Goethe «Italienische Reise». Teil III, Korrespondenz, 6. September 1787.",
      "[13    Karl Christian Planck, 1819-1880. «Testament eines Deutschen. Philosophie der Natur und der Menschheit.» Aus dem NacMaß herausgegeben von K. Köstlin, Tübingen 1881, Neuausgabe Jena 1915, S. XIV.",
      "116    Adolf von Harnack, 1851-1930, Professor der Theologie in Berlin. »Das Wesen des Christentums«, Leipzig 1900.",
      "118    George Henry Lewes, 1817-1878. «Life of Goethe», 2 Bde., 1855, deutsch",
      "125    Theodor Ziehen, 1863-1950, Professor der Psychiatrie in Jena, zuletzt Professor der Philosophie in Berlin. «Leitfaden der physiologischen Psychologie», 15 Vor­lesungen. 2. Aufl. Jena 1893, S. 172.",
      "135    sagt Homunkulus: «Faust» II, 7056-7061.",
      "136    manche Auseinandersetzungen: Vortrag vom 26. März 1914, in Rudolf Steiner:",
      "«Geisteswissenschaft als Lebensgut», 12 Vorträge, Berlin 1913/14. Bibl.-Nr. 63, Gesamtausgabe Dornach 1959; ferner Rudolf Steiner: «Geisteswissenschaftliche Erläuterungen zu Goethes Faust», Band II »Das Faustproblem. Die romantische und die klassische Walpurgisnacht», 12 Vorträge Dornach 1916-18. Bibl.-Nr. 273, Gesamtausgabe Dornach 1967.",
      "137    wenn er dergleichen hinschreiben kann: Max Hochdorf in «Neue Zürcher Zei­tung« vom 14. Dezember 1917 über das Buch von Max Dessoir «Vom Jenseins der Seele», Stuttgart 1917. Rudolf Steiner: «Von Seelenrätseln«, siehe Hinweis zu S. 11.",
      "147    Basilius Valentinus lebte seit 1415 als Benediktinermönch in Erfurt. Seine alchi­mistischen Schriften wurden um 1600 von dem Ratskämmerer Joh. Thölde in Frankenhausen (Thüringen) erstmals herausgegeben. Rudolf Steiner: «Die Mystik im Aufgange des neuzeitlichen Geisteslebens und ihr Verhältnis zur modernen Weltanschauung», Bibl.-Nr. 7, Gesamtausgabe Dornach 1960.",
      "149    «Nicht ich, sondern der Christus in mir»: Galater 2, 20.",
      "Theodor Svedberg, geb. 1884, schwedischer Chemiker, 1926 Nobelpreis für Che­mie. Vermutlich handelt es sich um das Buch «Die Materie» (1912), 1914 in deutsch erschienen.",
      "153    John Bright, 1811-1889, englischer liberaler Politiker. Neben seinem Freunde Cobden Führer der freihändlerischen Manchesterpartei, kämpfte für eine fort­schrittliche Sozialpolitik.",
      "Richard Cobden, 1804-1865, englischer Wirtschaftspolitiker. Setzte sich für eine internationale Verständigungspolitik und für Demokratie im Inneren ein.",
      "154    Friedensmanifest-Firlefanzereien des Zaren: Nikolaus II., 1868-1918, etwog im Herbst 1916 vorübergehend den von dem damaligen Ministerpräsidenten Stürmer vertretenen Gedanken eines Sonderfriedens mit den Mittelmächten;",
      "Stürmer mußte jedoch im November 1916 zurücktreten, und in einem Tages­befehl an Heer und Marine zum Jahresende 1916 erklärte der Zar, der Zeit­punkt für Friedensverhandlungen sei noch nicht gekommen.",
      "154    Woodrow Wilson, 1856-1924, Präsident der USA 1913-1921. Propagierte die Beseitigung autokratischer Regierungssysteme, die Einführung demokratischer Verfassungen und die Errichtung eines Völkerbundes, dessen ursprüngliche Idee aber nicht von ihm stammte.",
      "155  in den öffentlichen Vorträgen: Siehe Hinweis zu S. 31.",
      "158    im Basler Zweig: «Et incarnatus est. Die Umlaufzeit geschichtlicher Ereignisse«, Vortrag Basel, 23. Dezember 1917. In Rudolf Steiner: «Mysterienwahrheiten und Weihnachtsimpulse. Alte Mythen und ihre Bedeutung«, 16 Vorträge Basel und Dornach 1917/18. Bibl.-Nr. 180, Gesamtausgabe Dornach 1966.",
      "eine Weihnachtshetrachtung: Zweiter Vortrag in «Mysterienwahrheiten und Weihnachtsimpulse. Alte Mythen und ihre Bedeutung«, siehe vorigen Hinweis."
    ],
    "sentences": [
      [
        "9 Zu den Betrachtungen, die wir angestellt haben: Rudolf Steiner: «Die Spiri­tuellen Hintergründe der äußeren Welt - Der Sturz der Geister der Finsternis«, 14 Vorträge Dornach 1917.",
        "Bibl.-Nr. 177, Gesamtausgabe Dornach 1965."
      ],
      [
        "11 Rudolf Steiner: «Von Seelenrätseln« (Berlin 1917), Bibl.-Nr. 21, Gesamtausgabe Dornach 1976."
      ],
      [
        "21 eine Broschüre: Adolf von Strümpell, 1853-1925, zuletzt Professor der Medizin in Leipzig.",
        "«Die Schädigung der Nerven und des geistigen Lebens durch den Krieg«, Leipzig 1917, S. 22ff."
      ],
      [
        "31 Jch will Ihnen ein richtiges Beispiel anführen: Siehe Vortrag vom 7.",
        "November"
      ],
      [
        "1917 «Anthroposophie und Geschichtswissenschaft« in Rudolf Steiner «Die Er­gänzung heutiger Wissenschaften durch Anthroposophie«, 8 Vorträge Zürich 1917/18.",
        "Bibl.-Nr. 73, Gesamtausgabe Dornach 1973."
      ],
      [
        "49 Zyklus über das Leben zwischen dem Tod und einer neuen Geburt: Rudolf Steiner: «Inneres Wesen des Menschen und Leben zwischen Tod und neuer Ge­burt«, 8 Vorträge Wien 1914.",
        "Bibl.-Nr. 153, Gesamtausgabe Dornach 1959."
      ],
      [
        "Mitternachtsstunde des Daseins: Sechstes Bild in «Der Seelen Erwachen», in Rudolf Steiner: «Vier Mysteriendramen», Bibl.-Nr. 14, Gesamtausgabe Dorn-ach 1962."
      ],
      [
        "69 Otto Heinrich Jäger, 1828-1912.",
        "Schrieb als Student in Tübingen die preis-gekrönte Arbeit «Die Gymnastik der Hellenen«. 1856 wurde er Professor der Philosophie in Zürich. 1859 erschien seine Schrift «Die Freiheitslehre als System der Philosophie«."
      ],
      [
        "meine Freiheitsphilosophie: Rudolf Steiner: «Die Philosophie der Freiheit» (Berlin 1894).",
        "Bibl.-Nr. 4, Gesamtausgabe Dornach 1973."
      ],
      [
        "76 von den entsprechenden okkulten Schulen: Siehe Rudolf Steiner: «Die okkulre Bewegung im neunzehnten Jahrhundert und ihre Beziehung zur Weltkultur», 19 Vorträge Dornach 1915.",
        "Bibl.-Nr. 254, Gesamtausgabe Dornach 1969."
      ],
      [
        "78 von einem andern Gesichtspunkte aus: Rudolf Steiner: «Welche Bedeutung hat die okkulte Entwickelung des Menschen für seine Hüllen - physischen Leib, Atherleib, Astralleib - und sein Selbst?», 10 Vorträge Den Haag 1913.",
        "Bibl.­Nr.145, Gesamtausgabe Dornach 1976; «Weltwesen und Ichheit«, 7 Vorträge Berlin 1915.",
        "Bibl.-Nr. 169, Gesamtausgabe Dornach 1963."
      ],
      [
        "Chiron, der weise Kentaur der griechischen Mythologie, Lehrer des Askulap, Jason und Achilles."
      ],
      [
        "80 Es gibt einen Zyklus: Rudolf Steiner: «Das Leben zwischen dem Tode und der neuen Geburt im Verhältnis zu den kosmischen Tatsachen«, 10 Vorträge Berlin 1912/13.",
        "Bibl.-Nr. 141, Gesamtausgabe Dornach 1964."
      ],
      [
        "112 Da ist die Notwendigkeit, da ist Gott: Goethe «Italienische Reise».",
        "Teil III, Korrespondenz, 6.",
        "September 1787."
      ],
      [
        "[13 Karl Christian Planck, 1819-1880.",
        "«Testament eines Deutschen.",
        "Philosophie der Natur und der Menschheit.» Aus dem NacMaß herausgegeben von K.",
        "Köstlin, Tübingen 1881, Neuausgabe Jena 1915, S.",
        "XIV."
      ],
      [
        "116 Adolf von Harnack, 1851-1930, Professor der Theologie in Berlin. »Das Wesen des Christentums«, Leipzig 1900."
      ],
      [
        "118 George Henry Lewes, 1817-1878.",
        "«Life of Goethe», 2 Bde., 1855, deutsch"
      ],
      [
        "125 Theodor Ziehen, 1863-1950, Professor der Psychiatrie in Jena, zuletzt Professor der Philosophie in Berlin.",
        "«Leitfaden der physiologischen Psychologie», 15 Vor­lesungen. 2.",
        "Aufl.",
        "Jena 1893, S. 172."
      ],
      [
        "135 sagt Homunkulus: «Faust» II, 7056-7061."
      ],
      [
        "136 manche Auseinandersetzungen: Vortrag vom 26.",
        "März 1914, in Rudolf Steiner:"
      ],
      [
        "«Geisteswissenschaft als Lebensgut», 12 Vorträge, Berlin 1913/14.",
        "Bibl.-Nr. 63, Gesamtausgabe Dornach 1959; ferner Rudolf Steiner: «Geisteswissenschaftliche Erläuterungen zu Goethes Faust», Band II »Das Faustproblem.",
        "Die romantische und die klassische Walpurgisnacht», 12 Vorträge Dornach 1916-18.",
        "Bibl.-Nr. 273, Gesamtausgabe Dornach 1967."
      ],
      [
        "137 wenn er dergleichen hinschreiben kann: Max Hochdorf in «Neue Zürcher Zei­tung« vom 14.",
        "Dezember 1917 über das Buch von Max Dessoir «Vom Jenseins der Seele», Stuttgart 1917.",
        "Rudolf Steiner: «Von Seelenrätseln«, siehe Hinweis zu S. 11."
      ],
      [
        "147 Basilius Valentinus lebte seit 1415 als Benediktinermönch in Erfurt.",
        "Seine alchi­mistischen Schriften wurden um 1600 von dem Ratskämmerer Joh.",
        "Thölde in Frankenhausen (Thüringen) erstmals herausgegeben.",
        "Rudolf Steiner: «Die Mystik im Aufgange des neuzeitlichen Geisteslebens und ihr Verhältnis zur modernen Weltanschauung», Bibl.-Nr. 7, Gesamtausgabe Dornach 1960."
      ],
      [
        "149 «Nicht ich, sondern der Christus in mir»: Galater 2, 20."
      ],
      [
        "Theodor Svedberg, geb. 1884, schwedischer Chemiker, 1926 Nobelpreis für Che­mie.",
        "Vermutlich handelt es sich um das Buch «Die Materie» (1912), 1914 in deutsch erschienen."
      ],
      [
        "153 John Bright, 1811-1889, englischer liberaler Politiker.",
        "Neben seinem Freunde Cobden Führer der freihändlerischen Manchesterpartei, kämpfte für eine fort­schrittliche Sozialpolitik."
      ],
      [
        "Richard Cobden, 1804-1865, englischer Wirtschaftspolitiker.",
        "Setzte sich für eine internationale Verständigungspolitik und für Demokratie im Inneren ein."
      ],
      [
        "154 Friedensmanifest-Firlefanzereien des Zaren: Nikolaus II., 1868-1918, etwog im Herbst 1916 vorübergehend den von dem damaligen Ministerpräsidenten Stürmer vertretenen Gedanken eines Sonderfriedens mit den Mittelmächten;"
      ],
      [
        "Stürmer mußte jedoch im November 1916 zurücktreten, und in einem Tages­befehl an Heer und Marine zum Jahresende 1916 erklärte der Zar, der Zeit­punkt für Friedensverhandlungen sei noch nicht gekommen."
      ],
      [
        "154 Woodrow Wilson, 1856-1924, Präsident der USA 1913-1921.",
        "Propagierte die Beseitigung autokratischer Regierungssysteme, die Einführung demokratischer Verfassungen und die Errichtung eines Völkerbundes, dessen ursprüngliche Idee aber nicht von ihm stammte."
      ],
      [
        "155 in den öffentlichen Vorträgen: Siehe Hinweis zu S. 31."
      ],
      [
        "158 im Basler Zweig: «Et incarnatus est.",
        "Die Umlaufzeit geschichtlicher Ereignisse«, Vortrag Basel, 23.",
        "Dezember 1917.",
        "In Rudolf Steiner: «Mysterienwahrheiten und Weihnachtsimpulse.",
        "Alte Mythen und ihre Bedeutung«, 16 Vorträge Basel und Dornach 1917/18.",
        "Bibl.-Nr. 180, Gesamtausgabe Dornach 1966."
      ],
      [
        "eine Weihnachtshetrachtung: Zweiter Vortrag in «Mysterienwahrheiten und Weihnachtsimpulse.",
        "Alte Mythen und ihre Bedeutung«, siehe vorigen Hinweis."
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

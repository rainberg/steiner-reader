#!/usr/bin/env python3
"""Standalone import script for GA158 — GA158 - Der Zusammenhang des Menschen mit der elementarischen Welt"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA158 - Der Zusammenhang des Menschen mit der elementarischen Welt"""
GA_NUMBER = "GA158"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "KALEWALA DAS WESEN NATIONALER EPEN MIT SPEZIELLEM HINWEIS AUF KALEWALA Öffentlicher Vortrag, Helsingfors, 9. April 1912",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Vor allen Dingen darf ich Sie um Entschuldigung bitten, wenn ich den Vortrag, den ich zu halten habe, nicht in einer der hier landesüblichen Sprachen halten kann. Es entspricht die Tatsache, daß dieser Vortrag gehalten wird, dem Wunsche der Freunde unserer Theosophischen Ge­sellschaft, für welche ich hierher gerufen worden bin, eine Reihe von Vorträgen vierzehn Tage hindurch zu halten, und welche die Meinung hatten, daß die Möglichkeit bestehe, innerhalb dieser Zeit auch die zwei angekündigten öffentlichen Vorträge einzufügen. Damit hängt es natür­lich zusammen, daß ich weiter werde um Entschuldigung bitten müssen, wenn mancher der Namen und manche der Bezeichnungen, die gerade aus dem Volksepos der Finnen entlehnt sind, vielleicht von mir, als der Sprache unkundig, nicht ganz richtig ausgesprochen werden. In die Geisteswissenschaft selber wird uns allerdings erst der Vortrag am nächsten Freitag hineinführen können. Die Betrachtung des heutigen Abends wird vielmehr eine Art Nachbargebiet betreffen, welches in eine geisteswissenschaftliche Beleuchtung gerückt werden kann. Aller­dings von einem Gebiet soll die Rede sein, das im allertiefsten Sinn des Wortes zu den interessantesten der menschlichen geschichtlichen Be­trachtung, des menschlichen geschichtlichen Nachdenkens gehört.",
      "Volksepen! Wir brauchen nur an einige der bekannteren Volksepen zu denken, an die Epen Homers, welche griechische Volksepen gewor­den sind, an die mitteleuropäische Nibelungensage und endlich an Ka­lewala, und sogleich wird uns aufleuchten, daß wir durch diese Volks­epen tiefer in Menschenseelen und in Menschenstreben hineingeführt werden als durch irgendeine geschichtliche Forschung, so hineingeführt werden, daß uns wichtige alte Zeiten lebendig, wie gegenwärtig vor die Seele hingerückt werden, aber in einer Weise, daß sie in unmittel­barer Gegenwart uns wie die Schicksale und das Leben gegenwärtiger, um uns herum lebender Menschen berühren. Wie ungewiß und dämmerhaft",
      "sind uns geschichtlich diejenigen Zeiten des alten griechischen Vol­kes, von dem uns die Homerischen Epen erzählen, und wie schauen wir hinein, wenn wir den Inhalt der Ilias, der Odyssee auf uns wirken lassen, in die Seelen jener Menschen, die für die gewöhnliche Geschichts­betrachtung eigentlich vollständig entrückt sind. Kein Wunder, daß die Betrachtung der Volksepen für diejenigen, die sich wissenschaftlich oder literarisch damit beschäftigen, etwas Rätselhaftes hat.",
      "Wir brau­chen nur auf eine Tatsache in bezug auf die alten griechischen Epen hin­zuweisen, die ein geistvoller Betrachter der Ilias in einem sehr schönen, erst vor wenigen Jahren erschienenen Buch über Homers Ilias wiederholt geäußert hat. Ich meine Herman Grimm, den Neffen des großen ger­manischen Mythen-, Sagen- und Sprachforschers Jakob Grimm.",
      "Indem Herman Grimm die Gestalten und Tatsachen der Ilias auf sich wirken ließ, fühlte er sich immer wieder und wieder veranlaßt zu sagen: Oh, dieser Homer - wir brauchen heute nicht einzugehen auf die Frage nach der Persönlichkeit des Homer - scheint, wenn er irgend etwas schildert, das einem Handwerk, einer Kunst entlehnt ist, wie wenn er Fachmann in diesem Handwerk, in dieser Kunst wäre. Schildert er eine Schlacht, einen Kampf, so scheint er völlig bekannt zu sein mit all den strategischen und militärischen Grundsätzen, die innerhalb der Kriegsführung in Betracht kommen. - Mit Recht weist Herman Grimm darauf hin, daß ein strenger Richter in solchen Dingen ein Bewunderer der sachlichen Schlachtenschilderung Homers war, nämlich Napoleon, ein Mann, der zweifellos berechtigt war, ein Urteil darüber zu fällen, ob aus dem Geist Homers heraus das Militärische unmittelbar sachge­mäß und lebendig vor unsere Seele hingestellt wird oder nicht.",
      "Vom allgemein menschlichen Standpunkt aus wissen wir, wie die Gestalten plastisch, wie wenn wir sie unmittelbar vor dem physischen Auge hät­ten, durch Homer vor unsere Seele hingestellt werden.",
      "Wie ist es mit einem solchen Volksepos, wie erweist es sich dauernd durch die verschiedenen Zeiten? Denn wahrhaftig, derjenige, der die Verhältnisse unbefangen beobachtet, wird nicht den Eindruck erhalten, daß künstliche Veranstaltungen der Menschheit, etwa eine künstliche pädagogische Zucht, das Interesse der Jahrhunderte bis in unsere Tage herein an der Ilias und Odyssee immer wieder festgehalten haben. Dieses",
      "Interesse ist ein selbstverständliches, ist ein allgemein menschliches. Nur geben uns diese Volksepen in einem gewissen Sinne eine Aufgabe an die Hand, stellen uns sogleich, wenn wir sie betrachten wollen, eine ganz bestimmte, man möchte sagen interessante Aufgabe.",
      "Sie wollen nämlich in allen ihren Einzelheiten ganz genau genommen werden. Wir fühlen es sogleich, daß uns etwas unverständlich wird in den Inhalten solcher Volksepen, wenn wir sie etwa so lesen wollen, wie wir irgendein modernes Kunstwerk, einen modernen Roman oder dergleichen lesen.",
      "Wir fühlen gleich bei den ersten Zeilen der Ilias, daß Homer genau spricht. Was schildert er uns? Er sagt es uns im Beginn. Mancherlei weiß man aus andern Darstellungen, die nicht in der Ilias enthalten sind, über Ereignisse, die sich nach rückwärts an­schließen an die Tatsachen der Iliade.",
      "Homer will uns nur schildern, was er in der ersten Zeile prägnant sagt: den Zorn des Achill. Und wenn wir nun die ganze Iliade durchgehen und unbefangen betrach­ten, so müssen wir sagen: Nichts ist in Wahrheit darin, was nicht so bezeichnet werden kann, daß es auftritt als Tatsache, die da folgt aus dem Zorn des Achill. - Und weiter eine eigentümliche Tatsache wiederum gleich im Beginn der Iliade.",
      "Homer beginnt nicht etwa einfach mit den Tatsachen, er beginnt auch nicht mit irgendeiner per­sönlichen Meinung, sondern er beginnt mit etwas, was gerade eine mo­derne Zeit vielleicht als Phrase nehmen möchte, beginnt damit, daß er sagt: Singe mir, 0 Muse, von dem Zorne des Achill! - Und je tiefer wir eindringen in dieses Volksepos, desto klarer wird es uns, daß wir gar nicht Sinn und Geist und Bedeutung desselben verstehen können, wenn wir dieses Wort im Beginne nicht ernst nehmen. Dann aber müssen wir uns fragen: Was bedeutet es eigentlich?",
      "Und nun die Art der Darstellung, die ganze Art, wie die Ereignisse vor unsere Seele hingebracht werden! Es waren für viele, nicht nur fachmännische, wissenschaftliche Betrachter, sondern auch für künstle­risch umfassende Geister wie Herman Grimm, eine Frage diese Worte:",
      "0 singe mir, Muse, von dem Zorne des Achill. - Eine Frage, die ihnen tief zu Herzen ging. Wie spielen in dieser Ilias, geradeso wie im Nibe­lungenlied oder in Kalewala, die Taten geistig-göttlicher Wesenheiten zusammen - in Homers Dichtungen zunächst die Taten und Absichten",
      "und Leidenschaften der olympischen Götter - mit den Taten und Ab­sichten und Leidenschaften von Menschen, die, wie Achill, in einem gewissen Sinne dem gewöhnlichen Menschlichen fernstehen, und wie­derum mit den Leidenschaften und Absichten und Taten von Men­schen, die dem gewöhnlichen Menschlichen schon naheliegen wie Odys­seus oder wie Agamemnon? Wenn dieser Achill vor unsere Seele hintritt, so erscheint er uns gegenüber den Menschen, mit denen er zusam­menlebt, einsam.",
      "Wir fühlen sehr bald im Fortgang der Ilias, daß wir in Achill eine Persönlichkeit vor uns haben, die eigentlich über ihre innersten Angelegenheiten mit all den andern Helden nicht rechtspre­chen kann. Homer führt uns auch vor, wie Achill seine eigentlichen Herzensangelegenheiten mit göttlich-geistigen Wesenheiten auszuma­chen hat, die nicht dem Menschenreiche angehören, wie er einsam dem Menschenreiche gegenübersteht durch den ganzen Fortgang der Iliade und wiederum nahesteht übersinnlichen, überirdischen Mächten.",
      "Und dabei wiederum das Sonderbare, daß, wenn wir all unser menschliches Fühlen in die Art und Weise von Denken und Empfinden, wie wir sie uns im Kulturprozeß erobert haben, zusammennehmen und den Blick hinlenken nach diesem Achill, er uns dann so erscheint, daß wir oft­mals sagen müssen: Wie egoistisch, wie persönlich! - Eine Wesenheit, in deren Seele göttlich-geistige Impulse hereinspielen, sie handelt ganz aus dem unmittelbar Persönlichen heraus. Eine lange Zeit hindurch nimmt ein für die Griechen so wichtiger Krieg, wie der trojanische Sagenkrieg, nur dadurch seinen Fortgang, gewinnt die besonderen Epi­soden, welche die Iliade schildert, daß Achill für sich dasjenige aus­macht, was er persönlich auszumachen hat mit Agamemnon.",
      "Und immer sehen wir, daß überirdische Mächte hereinspielen. Wir sehen Zeus, Apollo, Athene die Impulse austeilen, sozusagen die Menschen an ihre Plätze hinstellen. Es war immer sonderbar, bevor die Aufgabe an mich kam, vom Standpunkt der Geisteswissenschaft an diese Dinge heranzutreten, wie ein sehr geistvoller Mann, mit dem ich das Glück hatte, oftmals persönlich auch über diese Dinge zu verhandeln, wie Herman Grimm mit diesen Dingen sich zurechtfand.",
      "Er hat es nicht nur in seinen Schriften, sondern oftmals im persönlichen Gespräche, und da noch viel genauer, ausgesprochen. Er sagte: Wenn wir nur das",
      "zusammennehmen, was an historischen Mächten und Impulsen in der Menschheitsentwickelung spielt, dann kommen wir nicht zurecht mit dem, was da lebt und schafft namentlich in den großen Volksepen. -Daher wurde für Herman Grimm, den geistvollen Betrachter der Iliade und der Volksdichtungen überhaupt, etwas, was über die gewöhn­lichen Bewußtseinskräfte des Menschen, über Verstand, Vernunft, Sin­nesanschauung, über das gewöhnliche Gefühl hinausgeht, zu einer rea­len Macht, zu einer Macht, die schöpferisch ist ebenso wie die andern historischen Impulse. Herman Grimm sprach von einer durch die Menschheitsentwickelung durchgehenden realen schöpferischen Phan­tasie, sprach von einer Phantasie so, wie man von einer Wesenheit, von einer Realität spricht, von etwas, was für die Menschen waltete und was ihnen im Anfang der Zeiten, die wir beobachten können, im Wer­den der einzelnen Völker mehr sagen konnte als das, was die gewöhn­lichen Seelenkräfte dem Menschen sagen. Wie das Hereinleuchten einer Welt, die sich nicht in den gewöhnlichen menschlichen Seelenkräften erschöpft, so sprach Herman Grimm immer die schöpferische Phan­tasie an, die damit für ihn etwa die Rolle einer Mitschöpferin beim Menschenwerdeprozeß bekam.",
      "Aber nun ist es eigentümlich, wenn wir diesen Kampfplatz der Iliade, diese Darstellung des Zornes des Achill betrachten mit all dem Hereinspielen übersinnlicher göttlich-geistiger Mächte, dann kommt man doch nicht zurecht mit einer solchen Betrachtung, wie sie Herman Grimm angestellt hat, und gerade in seinem Buche über die Iliade fin­den wir manches Wort der Resignation, das uns zeigt, wie der gewöhn­liche Standpunkt, den man heute literarisch oder wissenschaftlich ein­nehmen kann, nicht mit diesen Dingen zurechtkommt. Wozu kommt Herman Grimm gegenüber der Ilias, auch gegenüber der Nibelungensage? Er kommt dazu, anzunehmen, daß den historischen Dynastien, Herrschergeschlechtern, andere vorangegangen sind. So denkt Herman Grimm tatsächlich, man möchte sagen, buchstäblich. So denkt er daran, daß etwa Zeus mit seinem ganzen Umkreis eine Art Herrschergeschlecht darstellt, das dem Herrschergeschlecht, dem Agamemnon angehört, vorangegangen sei. Er denkt also sozusagen die Menschheitsgeschichte in einer gewissen Einförmigkeit, denkt sich in den in der Ilias oder der",
      "Nibelungensage dargestellten Göttem oder Heroen uralte Menschen, welche die späteren Menschen nur dadurch darzustellen wagten, daß sie ihre Taten, ihre Charaktere in das Kleid des übermenschlichen My­thos kleideten. Es gibt vieles, mit dem man sich nicht zurechtfinden kann, wenn man eine solche Voraussetzung zugrunde legt, so vor allen Dingen die besondere Art des Eingreifens der Götter gerade bei Homer. Ich bitte Sie, meine sehr verehrten Anwesenden, nur das eine zu neh­men: Thetis, die Mutter des Achill, Athene, andere Göttergestalten, wie greifen sie ein in die Ereignisse von Troja? So greifen sie ein, daß sie die Gestalt von sterblichen Menschen annehmen, diese gleichsam begeistern, diese hinführen zu ihren Taten. Sie erscheinen also nicht selber, sondern durchdringen lebendige Menschen. Lebendige Men­schen figurieren nicht nur wie ihre Stellvertreter, sondern wie die Hül­len, die von unsichtbaren Mächten durchdrungen werden, die nicht in eigener Gestalt, nicht in eigener Wesenheit auf dem Kampfplatz er­scheinen können. Es wäre doch sonderbar, anzunehmen, daß uralte Menschen der gewöhnlichen Art so dargestellt werden sollten, daß sie die stellvertretenden Menschen aus dem sterblichen Geschlecht wie zu ihrer Hülle nehmen müßten. Das ist nur eine der Hindeutungen, die uns alle beweisen können, daß wir in dieser Art nicht zurechtkommen mit den alten Volksepen.",
      "Ebensowenig aber kommen wir zurecht, wenn wir etwa die Ge­stalten des Nibelungenliedes nehmen, jenen Siegfried aus Xanten am Niederrhein, der nach Worms an den Burgunderhof hinversetzt wird, dort wirbt um Kriemhilde, die Schwester des Gunther, und wiederum für Gunther wirbt, durch seine besonderen Eigenschaften aber nur um Brunhilde werben kann. Und wie merkwürdig werden uns solche Ge­stalten wie Brunhilde aus Isenland, wie Siegfried, geschildert. Siegfried wird so geschildert, daß er das sogenannte Nibelungengeschlecht über­wunden hat, daß er da den Nibelungenschatz erworben, erobert hat. Durch das, was er sich durch den Sieg über die Nibelungen erworben hat, bekommt er ganz besondere Eigenschaften, die im Epos dadurch ausge­drückt werden, daß gesagt wird, er könne sich unsichtbar machen, er sei unverwundbar in gewisser Beziehung, er habe außerdem Kräfte, die der gewöhnliche Gunther nicht hat, denn dieser kann Brunhilde,",
      "die sich nicht von einem gewöhnlichen Sterblichen besiegen läßt, nicht erwerben. Durch seine besonderen Kräfte, die er als der Besitzer des Nibelungenhortes hat, besiegt Siegfried Brunhilde, und wiederum da­durch, daß er die Kräfte verbergen kann, die er entfaltet, ist er in der Lage, Brunhilde dem Gunther, seinem Schwager, zuzuführen.",
      "Und da finden wir, wie Kriemhilde und Brunhilde, die wir dann gleichzeitig am Burgunderhof erleben, zwei ganz verschiedene Charaktere sind, Charaktere, in die offenbar Dinge hereinspielen, die mit den gewöhn­lichen menschlichen Seelenkräften nicht zu erklären sind. Dadurch kommen sie in Streit, dadurch kommt es auch, daß Brunhilde den ge­treuen Dienstmann Hagen verleiten kann, Siegfried zu töten.",
      "Das wie­der weist uns auf einen Zug hin, der so merkwürdig gerade in der mit­teleuropäischen Sage auftritt. Siegfried hat höhere, übermenschliche Kräfte. Diese übermenschlichen Kräfte hat er durch den Besitz des Ni­belungenhortes.",
      "Sie machen ihn zuletzt nicht zu einer unbedingt sieg­haften Gestalt, sondern zu einer Gestalt, die tragisch vor uns steht. Ein Verhängnis sind zugleich für den Menschen die Kräfte, die Siegfried durch den Nibelungenhort hat.",
      "Noch sonderbarer werden die Dinge, wenn wir die damit verwandte nordische Sage von Sigurd, dem Dra­chentöter, dazunehmen, aber aufklärend wirkt dies. Da tritt uns Si­gurd, der nichts anderes ist als Siegfried, gleich entgegen als der Besieger des Drachens, der gerade dadurch den Nibelungenhort von einem alten Zwergengeschlecht erwirbt.",
      "Und Brunhilde tritt uns entgegen als eine Gestalt von übermenschlicher Natur, als eine Walkürengestalt.",
      "Wir sehen also, daß zwei Arten, in Europa diese Dinge darzustellen, existieren. Die eine Art, welche unmittelbar alles an das Göttlich-Über­sinnliche anknüpft, welche uns noch zeigt, wie in Brunhilde etwas ge­meint ist, was unmittelbar der übersinnlichen Welt angehört, und die andere Art, welche die Sage vermenschlicht hat. Aber wir können den­noch erkennen, wie auch in dieser Art überall das Durchklingen des Göttlichen zu finden ist.",
      "Und nun werfen wir von diesen Sagen, von diesen Volksepen den Blick in jenes Gebiet herüber, von dem ich wahrhaftig nur als ein sol­cher sprechen darf, der die Dinge von außen ansehen kann, nur so, wie man sie erkennen kann, wenn man die betreffende Sprache nicht",
      "spricht. Das bitte ich in Erwägung zu ziehen, daß ich über alles das, was dem Westeuropäer in Kalewala entgegentritt, nur so sprechen kann wie derjenige, welcher den geistigen Gehalt, die großen, gewaltigen Gestalten ins Auge faßt, und dem selbstverständlich äußerlich die zwei­fellos vorhandenen Feinheiten des Epos entgehen müssen, die dann erst herauskommen, wenn man die Sprache wirklich beherrscht, in der das­selbe abgefaßt ist.",
      "Aber auch bei einer solchen Betrachtung, wie eigen­tümlich tritt uns da entgegen die Dreiheit in den drei, ja, man ist eigent­lich in Verlegenheit, einen Namen zu gebrauchen, man kann nicht sagen Götter, man kann nicht sagen Heroen, sagen wir also in den drei Wesenheiten: Wäinämöinen, Ilmarinen und Lemminkäinen. Eine merk­würdige Sprache sprechen diese Gestalten, wenn wir sie in ihren Cha­rakteren miteinander vergleichen, eine Sprache, aus der wir deutlich erkennen, die Dinge, die uns gesagt werden sollen, gehen über das hin­aus, was mit den gewöhnlichen menschlichen Seelenkräften ausgerich­tet werden kann.",
      "Wachsen doch, wenn wir sie nur äußerlich betrachten, diese drei Gestalten ins Ungeheuerliche. Und doch wieder, was das Eigentümliche ist, indem sie ins Ungeheuerliche wachsen, steht uns jeder einzelne Zug plastisch vor Augen, so daß wir nirgends irgendwie das Gefühl haben, das Ungeheuerliche sei ein Groteskes, ein Paradoxes, überall haben wir das Gefühl, selbstverständlich muß das, was gesagt werden soll, in übermenschlicher Größe, in übermenschlicher Bedeu­tung auftreten.",
      "Und dann: welch Rätselhaftes im Inhalt. Etwas, was unsere Seele anspornt, an das Allermenschlichste zu denken, das aber doch wiederum über all das hinausgeht, was gewöhnliche Seelenkräfte fassen können.",
      "Ilmarinen, den man oftmals den Schmied, den über alles kunstvollen Schmied nennt, schmiedet für ein Gebiet, in dem sozusagen ältere Brüder der Menschheit oder wenigstens primitivere Menschen wohnen als die Finnen, für irgendein fremdes Gebiet auf Anstiften des Wäinämöinen den Sampo. Und wir sehen diese merkwürdige Sache zu­nächst, daß sich fern von dem Schauplatz, auf dem sich die Tatsachen abspielen, von denen die Rede ist, mancherlei zuträgt, daß da Zeit ver­geht, und wir sehen, wie nach einer bestimmten Zeit Wäinämöinen und Ilmarinen wiederum veranlaßt werden, das zurückzuholen, was ihnen in der Fremde geblieben ist, den Sampo.",
      "Wer die eigentümliche Geistessprache,",
      "die aus diesem Schmieden des Sampo, aus diesem Entfernthal­ten und Wiedergewinnen desselben spricht, auf sich wirken läßt, hat unmittelbar den Eindruck - wie gesagt, ich bitte zu berücksichtigen, daß ich sozusagen als Fremder spreche und daher nur von dem Ein­druck eines solchen sprechen kann -, daß das Wesentlichste, das Be­deutungsvollste in dieser grandiosen Dichtung doch das Schmieden, das Fernhalten und das spätere Wiedererringen des Sämpo ist.",
      "Was mich ganz besonders merkwürdig berührt an Kalewala, ist der Schluß. Ich habe gehört, daß es Menschen gibt, welche glauben, daß dieser Schluß vielleicht eine spätere Hinzufügung sei. Für mein Gefühl gehört gerade dieser Schluß von Mariata und ihrem Sohn, dieses Hereinspielen eines ganz merkwürdigen Christentums - ich sage ausdrück­lich eines ganz merkwürdigen Christentums - zu dem Ganzen.",
      "Es be­kommt Kalewala dadurch, daß dieser Schluß da ist, eine ganz beson­dere Nuance, eine Färbung, die uns die Sache sozusagen erst recht ver­ständlich machen kann. Ich darf sagen, daß für mein Gefühl eine so zarte, wunderbar unpersönliche Darstellung des Christentums über­haupt sich nirgends findet als am Schluß von Kalewala.",
      "Losgelöst ist das christliche Prinzip von allem Örtlichen. Das Hinkommen von Märiata zu Herodes, der uns in Kalewala als Rotus entgegentritt, ist so unpersönlich gefaßt, daß man kaum an irgendeine Örtlichkeit oder Persönlichkeit in Palästina erinnert wird.",
      "Ja, man wird, darf man sagen, nicht einmal im allergeringsten an den historischen Christus Jesus erinnert. Als eine intimste Herzenssache der Menschheit finden wir am Schlusse von Kalewala das Eindringen der edelsten Kulturperle der Menschheit in die finnische Kultur zart angedeutet.",
      "Und da­mit verknüpft ist der tragische Zug, der so unendlich tief wiederum auf unsere Seele wirken kann, daß Wäinämöinen in dem Augenblick, da das Christentum einzieht, wo der Sohn der Mariata getauft wird, Abschied nimmt von seinem Volk, um in eine unbestimmte Örtlich­keit zu gehen, zurücklassend seinem Volk nur den Inhalt und die Macht dessen, was er aus seiner Sangeskunst heraus zu erzählen wußte über die uralten Geschehnisse, welche das Historische dieses Volkes ein­schließt. Dieses Zurückziehen des Wäinämöinen gegenüber dem Sohn von Mariata erscheint mir so bedeutsam, daß man darin das lebendige",
      "Zusammenspiel von alldem sehen möchte, was auf dem Grund des fin­nischen Volkes, der finnischen Volksseele waltete, waltete von uralten Zeiten her in dem Moment, als das Christentum in Finnland Einlaß fand. Wie dieses uralt Waltende sich verhielt zu dem Christentum, ist so, daß man alles, was da in den Seelen spielte, mit einer wunderbaren Intimität fühlen kann. Das sage ich als etwas, von dessen Objektivität ich mir bewußt bin, das ich niemand zur Freude, niemand zur Schmei­chelei sagen möchte. Wir Westeuropäer haben durch dieses Volksepos gerade eines der wunderbarsten Beispiele, wie in unmittelbarer Gegen­wart die Glieder eines Volkes mit ihrer ganzen Seele leibhaftig vor uns stehen, so daß man durch Kalewala die finnische Seele in Westeuropa in einer Weise kennenlernt, daß man mit ihr völlig vertraut werden kann.",
      "Dies alles - warum habe ich es gesagt? Gesagt habe ich es, um zu charakterisieren, wie in den Volksepen etwas spricht, was durch ge­wöhnliche menschliche Seelenkräfte, selbst wenn man von der Phan­tasie als einer realen Macht spricht, nicht erklärt werden kann. Und wenn auch manchem das, was gesägt wird, nur wie eine Hypothese klingt, so darf da vielleicht das, was Geisteswissenschaft über das Wesen dieser Volksepen zu sagen hat, an diese Betrachtung über die Volksepen angeführt werden. Gewiß, ich bin mir bewußt, daß mit dem, was ich zu sägen habe, heute in unserer Gegenwart noch etwas getroffen ist, wozu die wenigsten Menschen ihre Zustimmung geben können. Von vielen wird es vielleicht wie eine Träumerei, wie eine Phantasterei an­gesehen werden; einige aber werden es wenigstens neben andern Hypo­thesen, die über das Werden der Menschheit aufgestellt werden, an­nehmen. Für denjenigen aber, der so in die Geisteswissenschaft ein­dringt, wie ich mir das im nächsten Vortrag zu schildern gestatten werde, wird nicht von einer Hypothese, sondern von einem wirk­lichen Forschungsergebnis, das sich neben andere wissenschaftliche For­schungsergebnisse hinstellen kann, gesprochen. Fremd klingen die Dinge, über die gesprochen werden muß, aus dem Grunde, weil gerade jene Wissenschaftlichkeit, welche heute glaubt, ganz fest auf dem Boden des Tatsächlichen, des Währen zu stehen, des einzig Erreichbaren, sich nur auf das beschränkt, was äußere Sinne wahrnehmen, was der an die",
      "Sinne und das Gehirn gebundene Verstand von den Dingen erkunden kann. Und es gilt deshalb heute vielfach für unwissenschaftlich, wenn von einer Forschungsmethode gesprochen wird, welche zu andern Kräf­ten der Seele greift, denen es möglich ist, in das Übersinnliche und in das Hereinspielen des Übersinnlichen in das Sinnliche zu schauen. Durch diese Forschungsmethode, durch Geisteswissenschaft, wird man nicht bloß zu der abstrakten Phantasie geführt, zu welcher Herman Grimm den Volksepen gegenüber geführt worden ist, sondern man wird zu etwas geführt, das weit über die Phantasie hinausgeht, was einen ganz andern Seelen- oder Bewußtseinszustand darstellt, als ihn der Mensch in dem gegenwärtigen Zeitpunkt seiner Entwickelung haben kann. Und so werden wir durch Geisteswissenschaft in einer ganz an­dern Weise zur menschlichen Vorzeit zurückgeführt als etwa durch die gewöhnliche Wissenschaft.",
      "Die gewöhnliche Wissenschaft ist es heute gewöhnt, rückblickend das Werden der Menschheit so zu betrachten, daß das, was wir heute Menschen nennen, sich nach und nach aus niedrigeren, tierähnlichen Geschöpfen heraus entwickelt hat. Geisteswissenschaft stellt sich nicht etwa dieser modernen Forschung kampfgerüstet gegenüber, sondern er­kennt völlig das Große und Gewaltige der Errungenschaften dieser Naturwissenschaft des 19. Jahrhunderts an, das Bedeutungsvolle des Gedankens einer Umwandlung der tierischen Formen von dem Un­vollkommensten zum Vollkommenen und einen Anschluß der äußeren Menschenform an die vollkommenste tierische Form. Aber sie kann bei einer solchen Betrachtung des Menschenwerdens, des Werdens der Organismen überhaupt, nicht stehenbleiben, die sich etwa darstellen würde, wenn man mit einem äußeren sinnlichen Blick dasjenige über­schauen könnte, was sich im Laufe des Erdengeschehens in der organi­schen Welt bis zum Menschen herauf vollzogen hat. Für die Geistes­wissenschaft steht heute der Mensch neben der tierischen Welt da. Wir erblicken in der Welt, die uns umgibt, die verschieden geformten tie­rischen Gestalten. Wir erblicken über die Erde hin ausgebreitet das in einer gewissen Weise einheitliche Menschengeschlecht. Wir haben auch in der Geisteswissenschaft einen unbefangenen Blick dafür, wie in der äußeren Form alles für die Verwandtschaft des Menschen mit den",
      "übrigen Organismen spricht, aber wir können in der Geisteswissen­schaft, wenn wir das Werden der Menschheit rückwärts verfolgen, nicht so zurückgehen, daß wir in einer grauen Vorzeit etwa unmittelbar hin­einlaufen lassen den Strom der Menschheit in die tierische Entwicke­lungsreihe. Wir finden nämlich, wenn wir von der Gegenwart in die Vergangenheit zurückgehen, daß wir nirgends unmittelbar die gegen­wärtige Menschengestalt, den gegenwärtigen Menschen aus irgend­einer Tierform, die wir wiederum aus der Gegenwart kennen, anreihen dürfen.",
      "Wenn wir in der Menschheitsentwickelung zurückgehen, dann fin­den wir zunächst, man möchte sagen, bis zu immer primitiveren For­men beim Menschen die Seelenkräfte ausgebildet, die Verstandes- und Gemüts- und Willenskräfte, die wir auch in der Gegenwart haben. Dann kommen wir zurück bis in graue Vorzeiten, von denen uns alte Dokumente nur spärlich erzählen.",
      "Selbst da, wo wir so weit zurück­gehen können wie bei den Ägyptern oder den vorderasiatischen Völ­kern, werden wir überall in ein uraltes Menschentum zurückgeführt, welches zwar in einer gewissen Beziehung primitiver, aber auch groß­artiger dieselben Kräfte, Gemüts-, Verstandes- und Willenskräfte hat, die allerdings erst gegen die Gegenwart herein ihre jetzige Ausbildung gefunden haben, die wir aber als wichtigste Menschheitsimpulse, als wichtigste geschichtliche Impulse erblicken, soweit wir eben die Mensch­heit zunächst, indem wir diese ihre gegenwärtige Seele in Betracht zie­hen, zurückverfolgen können. Da finden wir nirgends die Möglichkeit, auch den am weitesten zurückliegenden Menschenschlag etwa in eine besondere Verwandtschaft mit den heutigen tierischen Formen zu stel­len.",
      "Dies, was so Geisteswissenschaft für sich behaupten muß, erkennen heute selbst schön denkende Naturforscher an. Aber indem wir weiter zurückgehen und betrachten, wie doch die menschliche Seele sich än­dert, wenn wir vergleichen, wie gegenwärtig ein Mensch, sagen wir, wissenschaftlich oder sonst denkt, wie er seinen Verstand anwendet und seine Gemütskräfte wirken, wenn wir das zurückverfolgen - oh, wir können es ziemlich genau verfolgen -: in einer bestimmten Zeit leuchtete es zuerst in der Menschheit auf.",
      "Wir möchten sagen: In dem 6., 7. vorchristlichen Jahrhundert leuchtete es auf. Die gesamte Konfiguration",
      "des gegenwärtigen Fühlens und Denkens reicht eigentlich nicht weiter zurück als in jene Zeiten, von denen uns als den Zeiten der ersten griechischen Naturphilosophie erzählt wird.",
      "Wenn wir weiter zurückkommen und unbefangenen Blick genug haben, finden wir, ohne noch die Geisteswissenschaft zu berühren, daß nicht nur alles gegenwärtige wissenschaftliche Denken aufhört nach rückwärts hin, sondern daß die menschliche Seele überhaupt in einer ganz andern Verfassung ist, in einer viel unpersönlicheren Verfassung, aber auch in einer solchen Verfassung, daß wir ihre Kräfte viel mehr als instinktiv ansprechen müssen. Nicht etwa so, wie wenn wir sagen wollten, daß von dieser Zeit die Menschen aus solchen Instinkten her­aus gehandelt hätten wie die heutigen Tiere, aber jene Leitung durch Vernunft und Verstand, wie sie heute vorhanden ist, war nicht da.",
      "Dafür aber war eine gewisse instinktive, unmittelbare Sicherheit bei den Menschen da. Sie handelten aus unmittelbaren, elementaren Im­pulsen heraus, sie kontrollierten nicht durch den an das Gehirn ge­bundenen Verstand.",
      "Da finden wir allerdings, daß in der menschlichen Seele diejenigen Kräfte ungemischt noch walten, die wir heute abge­sondert als Verstandeskräfte haben, und jene Kräfte, die wir heute sorgfältig von den Verstandes- und zur Wissenschaft führenden Kräf­ten absondern, die Phantasiekräfte. Phantasie, Verstand und Vernunft, sie wirken in jenen alten Zeiten durcheinander.",
      "Je weiter wir zurück­gehen, desto mehr finden wir, daß wir gar nicht mehr das, was da in der Seele der Menschen waltete, was da ungetrennt als Phantasie und Verstand wirkte, so ansprechen dürfen, wie wir heute eine Seelenkraft bezeichnen, wenn wir sie Phantasie nennen. Wir wissen heute ganz genau, wenn wir von der Phantasie sprechen, so sprechen wir von einer Seelenkraft, deren Ausdrücke wir nicht wiederum wirklich anwenden dürfen, denen wir nicht Realität zuschreiben dürfen.",
      "Der moderne Mensch ist sorgsam in dieser Sache, er hütet sich wohl, dasjenige, was ihm die Phantasie gibt, zusammenzumischen mit dem, was die Logik der Vernunft ihm sagt. Sehen wir auf das, was der Geist der Menschen in jenen vorhistorischen Zeiten äußert, bevor Phantasie und Verstand abgesondert auftreten, dann fühlen wir in den Seelen eine ursprüng­liche, elementare, instinktive Kraft walten.",
      "Wir können in ihr Merkmale",
      "der heutigen Phantasie finden, aber das, was - wenn wir den Aus­druck gebrauchen - Phantasie damals der menschlichen Seele gab, hatte etwas mit einer Wirklichkeit, mit einer Realität zu tun. Die Phantasie war noch nicht Phantasie, sie war noch - ich darf mich nicht scheuen, den Ausdruck unmittelbar zu gebrauchen - hellsichtige Kraft, war noch ein besonderes Seelenvermögen, war die Gabe der Seele, durch die der Mensch Dinge sah, Tatsachen sah, die ihm heute in seiner Entwicke­lungsepoche, wo Verstand und Vernunft sich besonders ausbilden sol­len, verborgen sind. Tiefer hinunter drangen jene Kräfte, die nicht Phantasie, sondern hellsichtige Kraft waren, in verborgene Kräfte und verborgene Daseinsformen, die hinter der sinnlichen Welt liegen. Das ist das, wozu uns eine unbefangene Betrachtung führen muß, daß, wenn wir rückläufig die Menschheitsentwickelung betrachten, wir uns sägen müssen: Wahrhaftig, wir müssen das Wort Evolution, Entwicke­lung, ernst nehmen.",
      "Daß die Menschheit in der Gegenwart, in den letzten Jahrhunder­ten und Jahrtausenden sozusagen zu ihren sie heute so hochbringenden Vernunft- und Verstandeskräften gekommen ist, das ist ein Entwicke­lungsergebnis. Diese Seelenkräfte haben sich aus andern heraus ent­wickelt. Und während diese unsere gegenwärtigen Seelenkräfte auf das beschränkt sind, was sich in der äußeren Sinneswelt darbietet, sah eine ursprüngliche Menschheit, die allerdings auf Wissenschaft im heu­tigen Sinn, auf Verstandesgebrauch im heutigen Sinn verzichten mußte, sah eine ursprüngliche menschliche Seelenkraft auf dem Grund aller einzelnen Völker in Untergründe des Daseins hinein, in ein Gebiet, das als ein übersinnliches hinter dem Sinnlichen liegt. Hellseherische Kräfte waren bei allen Völkern einstmals den menschlichen Seelen eigen, und aus diesen hellseherischen Kräften heraus haben sich erst die gegenwärtigen menschlichen Verstandes- und Vernunftkräfte, hat sich die gegenwärtige Art, zu denken und zu fühlen, gebildet. Jene See­lenkräfte, die wir in einer gewissen Weise als hellseherische Kräfte an­sprechen dürfen, wären nun so, daß der Mensch zugleich fühlte: Ich bin es nicht selbst, der da in mir denkt, in mir fühlt. - Der Mensch fühlte sich wie hingegeben mit seiner ganzen Körperlichkeit und auch mit seinem Seelenwesen an höhere, übersinnliche Kräfte, die in ihm",
      "wirkten und lebten. So fühlte sich der Mensch wie ein Gefäß, durch das übersinnliche Kräfte selbst sprachen. Wenn man das bedenkt, dann begreift man auch den Sinn der Fortentwickelung der Mensch­heit. Die Menschen wären unselbständige Wesen geblieben, die sich nur als Gefäße, als Hüllen von Mächten und Wesenheiten hätten füh­len können, wenn sie nicht zum eigentlichen Verstandes- und Ver­nunftgebrauch vorgeschritten wären.",
      "Selbständiger ist der Mensch ge­worden durch Verstandes- und Vernunftgebrauch, zugleich aber auch für eine Weile der Entwickelung von der geistigen Welt in gewisser Beziehung abgeschnitten, abgeschnitten von den übersinnlichen Un­tergründen des Daseins. In der Zukunft wird das wieder anders wer­den.",
      "Je weiter wir zurückgehen, desto tiefer sieht durch die hellsehe­rischen Kräfte die menschliche Seele in die Untergründe des Daseins hinein, sieht hinein, wie aus diesen Untergründen des Daseins auch diejenigen Kräfte hervorgegangen sind, die am Menschen selber in vorhistorischer Zeit gearbeitet haben, bis in einen Zeitpunkt hinein, in dem alle Verhältnisse der Erde noch ganz anders waren als heute, wo sie so waren, daß die Formen der Lebewesen viel beweglicher, viel mehr einer Art von Metamorphose unterworfen waren als heute. So müssen wir weit von dem, was man gegenwärtige menschliche Kulturzeit nennt, zurückgehen, müssen nebeneinander Menschenwerden und tierisches Werden verfolgen.",
      "Und viel weiter zurückliegend, als man heute gewöhnlich glaubt, ist die Abtrennung der tierischen Form von der menschlichen. Die tierischen Formen sind dann erstarrt, sind un­beweglicher geworden in einer Zeit, in der die menschliche Form noch durchaus weich und biegsam war und geformt und geprägt werden konnte von dem, was innerlich seelisch erlebt wurde.",
      "Da kommen wir allerdings im Menschenwerden in eine Zeit zurück, bis zu der das heu­tige Bewußtsein nicht reicht, aber für die noch ein anderes Bewußtsein in der Seele vorhanden war, das im Zusammenhang mit den hellseheri­schen Kräften steht, die eben charakterisiert worden sind. Ein solches Bewußtsein, das auf die Vergangenheit hinblicken konnte und die Menschheitsentwickelung im Herkommen aus der Vergangenheit schon in völliger Abtrennung von allem tierischen Leben sah, sah auch, wie die menschlichen Kräfte walteten, aber noch in lebendigem Zusammenhang",
      "mit den übersinnlichen Kräften, die da hereinspielten. Es sah das­jenige, was in den Zeiten, in denen zum Beispiel die Homerischen Epen entstanden sind, nur noch als ein alter Nachklang vorhanden war, und was in noch früheren Zeiten in einem viel erhöhteren Maße vorhanden war.",
      "Wenn wir hinter Homer zurückgingen, so fänden wir, daß die Menschen hellseherisches Bewußtsein hatten, das sich an menschliche vorgeschichtliche Ereignisse gleichsam erinnerte und in der Erinnerung den Hergang bei der Menschwerdung zu erzählen vermochte. Zu Ho­mers Zeiten war dann die Sache schon so, daß man fühlte, das alte hellseherische Bewußtsein war im Schwinden, aber man fühlte noch, daß es da war.",
      "Das war eine Zeit, in der nicht der Mensch als selbstän­diges egoistisches Wesen von sich aus sprach, sondern in der aus ihm heraussprachen Götter, übersinnlich geistige Kräfte. So müssen wir es ernst nehmen, wenn Homer nicht von sich spricht, sondern wenn er sagt: Singe mir, o Muse, von dem Zorn des Achill!",
      "Singe in mir, höheres Wesen, Wesen, das durch mich spricht, das von mir Besitz ergreift, indem ich singe und sage. - Eine Realität ist diese erste Zeile bei Homer. Hingewiesen werden wir also nicht auf alte Herrscherdyna­stien, die im gewöhnlichen Sinne unserer jetzigen Menschheit ähnlich sind, sondern hingewiesen werden wir durch Homer selber darauf, daß es in der Urzeit andere Menschen gegeben hat, Menschen, in denen das Übersinnliche lebte.",
      "Und Achill ist durchaus noch eine Persönlich­keit aus der Übergangszeit vom alten Hellsehen zu der modernen An­schauungsweise, die wir schon bei Agamemnon, die wir bei Nestor und Odysseus finden, die aber dann weitergeführt wird zu einer höheren Anschauung. Nur dadurch begreifen wir Achill, wenn wir wissen, daß Homer in ihm einen Angehörigen der alten Menschheit hinstellen will, der in einer Zeit lebte, die zwischen jener Zeit liegt, wo die Menschen noch unmittelbar zu den alten Göttern hinaufreichten und der gegen­wärtigen Menschheitszeit, die etwa mit Agamemnon beginnt.",
      "Ebenso werden wir auf eine menschliche Vorzeit in der mitteleuro­päischen Nibelungensage hingewiesen. Das zeigt uns die ganze Dar­stellung dieses Epos. Wir haben es da zwar schon zu tun mit Menschen unserer Gegenwart in gewisser Beziehung, aber mit solchen Menschen unserer Gegenwart, die sich noch etwas herüberbewahrt haben aus der",
      "Zeit des alten Hellsehens. All die Eigenschaften, die von Siegfried an­geführt werden, daß er sich unsichtbar machen kann, daß er Kräfte hat, durch die er Brunhilde überwindet, welche ein gewöhnlicher Sterb­licher nicht überwinden kann, all das zeigt uns neben dem andern, was uns von ihm mitgeteilt wird, daß wir in ihm einen Menschen haben, der wie in einer inneren menschlichen Erinnerung die Errungenschaften der alten Seelenkräfte, die mit Hellsichtigkeit und dem Verbundensein mit der Natur verknüpft waren, in das gegenwärtige Menschentum herübergetragen hat.",
      "An welchem Übergang steht Siegfried? Das zeigt uns Brunhildes Verhältnis zu Kriemhilde, der Frau des Siegfried. Es kann hier nicht näher ausgeführt werden, was die beiden Gestalten bedeuten. Aber wir kommen zurecht mit all diesen Sagen, wenn wir mit den Gestalten, die uns vorgeführt werden, bildliche Darstellungen für innere hellseherische oder erinnerte hellseherische Verhältnisse sehen.",
      "So dürfen wir in Siegfrieds Verhältnis zu Kriemhilde sein Ver­hältnis zu seinen eigenen Seelenkräften sehen, die in ihm walten. Seine Seele ist gewissermaßen eine Übergangsseele, und zwar dadurch, daß Siegfried sich mit dem Nibelungenschatz, das heißt, mit den hellseheri­schen Geheimnissen der alten Zeit noch etwas in die neue Zeit her-überbringt, was ihn aber zugleich für seine Gegenwart ungeeignet macht.",
      "So konnten leben mit diesem Nibelungenhort, das heißt mit den alten hellseherischen Kräften, die Menschen der alten Zeit. Die Erde hat ihre Bedingungen geändert. Dadurch ist Siegfried, der in seiner Seele noch einen Nachklang der alten Zeit trägt, nicht mehr hinein-passend in die Gegenwart, dadurch wird er zu einer tragischen Ge­stalt.",
      "Wie kann sich die Gegenwart zu dem verhalten, was für Sieg­fried noch lebendig ist? Für ihn ist noch etwas von den alten hellsehe­rischen Kräften lebendig, denn als er überwunden wird, bleibt Kriem­hilde zurück.",
      "Ihr wird der Nibelungenhort gebracht, sie kann ihn an­wenden. Wir erfahren, daß ihr später durch Hagen der Nibelungenhort genommen wird. Wir können sehen, daß auch Brunhilde in ge­wisser Weise in der Lage ist, mit den alten hellseherischen Kräften zu arbeiten.",
      "Dadurch steht sie denjenigen Menschen entgegen, die in die damalige Gegenwart hineingepaßt sind: Gunther und seinen Brüdern, Gunther vor allem, für den Brunhilde nichts übrig hat. Warum das?",
      "Nun, wir wissen aus der Sage, daß Brunhilde eine Art Walkürengestalt ist: also wiederum etwas in der menschlichen Seele, und zwar dasjenige, mit dem sich in alten Zeiten durch die hellseherischen Kräfte der Mensch noch vereinigen konnte, das sich aber zurückgezogen hat vom Menschen, unbewußt geworden ist und mit dem sich der Mensch so, wie er gegenwärtig im Verstandeszeitalter lebt, erst nach dem Tod vereinigen kann. Daher die Vereinigung mit der Walküre im Moment des Todes. Die Walküre ist die Personifikation der lebendigen Seelen-kräfte, die im gegenwärtigen Menschen sind, jener Seelenkräfte, bis zu denen das alte hellseherische Bewußtsein hinkäm, die aber der gegen­wärtige Mensch erst erlebt, wenn er durch die Pforte des Todes tritt. Da wird er erst mit dieser Seele, die in Brunhilde dargestellt wird, vereint. Weil Kriemhilde noch etwas weiß von der alten Hellseher-zeit und den Kräften, welche die Seele durch das alte Hellsehen emp­fängt, wird sie zu einer Gestalt, deren Zorn geschildert wird, wie in der Ilias der Zorn des Achilles. Das wird uns hinlänglich angedeutet, daß die Menschen, die in alten Zeiten noch mit hellseherischen Kräften be­gabt waren, nicht kontrollierten mit dem Verstand, nicht den Verstand walten ließen, sondern unmittelbar aus ihren elementarsten, intensiv­sten Impulsen heraus wirkten. Daher das Persönliche, das unmittelbar Egoistische, sowohl bei Kriemhilde wie bei Achill.",
      "Insbesondere interessant wird die ganze Sache in der Betrachtung der Volksepen, wenn wir zu den angeführten Volksepen Kalewala hin­zunehmen. Wir werden zeigen können, heute kann das wegen der Kürze der Zeit bloß angedeutet werden, daß Geisteswissenschaft in unserer Gegenwart nur deshalb auf die alten hellseherischen Zustände der Menschheit hinweisen kann, weil es möglich wird, heute wiederum",
      "- allerdings in einer erhöhteren Weise, vom Verstand durchdrungen, nicht traumhaft - die hellseherischen Zustände durch geistige Schulung hervorzurufen. Der Mensch der Gegenwart wächst allmählich wieder in ein Zeitalter hinein, in dem aus den Tiefen der menschlichen Seele verborgene Kräfte, die wiederum ins Übersinnliche hineinweisen - allerdings nunmehr geführt von Vernunft, nicht unkontrolliert von dieser -, heräuswachsen werden, wo diese Menschen ins übersinnliche Gebiet hinaufweisen werden, so daß wir die Gebiete wieder kennenlernen",
      "werden, von denen uns die alten Volksepen aus dem dumpfen Bewußtsein der alten Zeiten heraus sprechen. Daher können wir sägen:",
      "Man lernt erkennen, daß es möglich ist, eine Offenbarung der Welt zu gewinnen, nicht bloß durch die äußeren Sinne, sondern durch etwas Übersinnliches, das dem äußeren physischen Menschenleib zugrunde liegt.",
      "Es gibt Methoden - von denen soll dann im nächsten Vortrag ge­sprochen werden -, durch die der Mensch das geistige übersinnliche Innere, was heute so oftmals abgeleugnet wird, von dem sinnlichen äußeren Leib unabhängig machen kann, so daß der Mensch nicht in einem bewußtlosen Zustand lebt wie etwa im Schlaf, wenn er von sei­nem Leibe unabhängig wird, sondern daß er Geistiges um sich herum wahrnimmt. Dadurch zeigt das moderne Hellsehen dem Menschen die Möglichkeit, erkennend in einem höheren, übersinnlichen Leib zu leben, der wie ein Gefäß den gewöhnlichen Sinnenleib ausfüllt.",
      "Man nennt ihn in der Geisteswissenschaft den ätherischen oder Ätherleib. Dieser Ätherleib ruht in unserem Sinnenleib drinnen. Durch ihn kommen wir, wenn wir ihn innerlich von dem physisch-sinnlichen Leib loslösen, auch heute in jenen Zustand des Wahrnehmens, durch den wir über­sinnliche Tatsachen gewahr werden.",
      "Zweierlei übersinnlicher Tatsachen werden wir gewahr. Erstens werden wir dessen gewahr im Beginn die­ses hellseherischen Zustandes, wenn wir anfangen zu wissen, wir sehen nicht mehr durch unseren physischen Leib, wir hören nicht mehr durch unseren physischen Leib, denken auch nicht mehr durch das an den physischen Leib gebundene Gehirn.",
      "Da wissen wir zunächst von aller äußeren Welt noch nichts. - Ich erzähle Ihnen Tatsachen, deren genauere Begründung erst im nächsten Vortrage möglich ist. - Dafür führt uns aber die erste Stufe des Hellsehens um so mehr zu einer An­schauung unseres eigenen Ätherleibes. Wir sehen ein übersinnliches Leibliches der menschlichen Natur, das dieser zugrunde liegt, und das wir nicht anders ansprechen können als etwas, das wirkt und schafft wie eine Art von innerem Baumeister, innerem Werkmeister, das unse­ren physischen Leib lebendig durchdringt.",
      "Und dann werden wir des Folgenden gewahr.",
      "Wir werden gewahr, daß das, was wir da an uns selber wahrnehmen,",
      "was wir als das eigentliche Lebendige unseres Ätherleibes an uns selber wahrnehmen, auf der einen Seite beschränkt, modifiziert wird durch unseren physischen Leib, daß es gleichsam nach der physischen Seite hin eingekleidet wird. Indem der Ätherleib auskleidet Augen und Ohren, auskleidet das physische Gehirn, gehören wir gewissermaßen dem irdischen Element an.",
      "Dadurch nehmen wir wahr, wie unser äthe­rischer Leib zum speziellen einzelnen, egoistischen Menschen wird, der in die Hülle seines physischen Leibes eingegliedert ist. Auf der andern Seite aber nehmen wir wahr, wie unser ätherischer Leib uns gerade wiederum in jene Regionen hineinführt, wo wir unpersönlich einem Höheren, Übersinnlichen gegenüberstehen, etwas, was nicht wir sind, was aber in uns mit voller Gegenwart vorhanden ist, was als geistige übersinnliche Macht und Kraft durch uns hindurch wirkt.",
      "Dadurch zerfällt für uns dann in der geisteswissenschaftlichen Betrachtung das innere Seelenleben in drei Glieder, die in drei äußere Leibeshüllen wie eingeschlossen sind, diese ausfüllend. Wir leben zunächst mit unserer Seele so, daß wir in ihr dasjenige erleben, was unsere Augen sehen, unsere Ohren hören, unsere Sinne überhaupt ergreifen können, was unser Verstand begreifen kann.",
      "Wir leben mit unserer Seele in unserem physischen Leibe. Insofern unsere Seele im physischen Leibe lebt, nen­nen wir sie in der Geisteswissenschaft die Bewußtseinsseele, weil erst durch das vollständige Einleben in den physischen Leib im Laufe des Menschenwerdens es möglich geworden ist, daß der Mensch zum Ich-Bewußtsein aufgerückt ist.",
      "Dann lernt insbesondere der moderne Hell­seher auch kennen das Leben der Seele in demjenigen, was wir Äther­leib genannt haben. Da lebt die Seele so im Ätherleib, daß sie zwar ihre Kräfte hat, daß da aber die Seelenkräfte so wirken, daß wir nicht sagen können, unsere persönlichen Kräfte sind es.",
      "Es sind allgemeine Menschheitskräfte, Kräfte, durch die wir den gesamten verborgenen Tatsachen der Natur viel näherstehen. Insofern die Seele diese Kräfte in einer äußeren Hülle, eben in dem Ätherleib wahrnimmt, sprechen wir von der Verstandes- oder Gemütsseele als einem zweiten Seelen-glied.",
      "So daß, ebenso wie wir die Bewußtseinsseele in der Hülle des physischen Leibes eingeschlossen finden, wir die Verstandes- oder Ge­mütsseele in dem ätherischen Leib eingeschlossen haben. Und dann haben",
      "wir einen noch feineren Leib, durch den wir hinaufragen in die übersinnliche Welt. Alles das, was wir innerlich erleben als unsere ur­eigensten Geheimnisse, zugleich als das, was heute dem Bewußtsein ver­borgen ist und was in der Zeit des alten Hellsehens als die Werdekräfte empfunden wurde im menschlichen Entwickelungsprozeß, was so emp­funden wurde, als ob man zurückschauen könnte in die Ereignisse grauer Vorzeiten, alles das schreiben wir der Empfindungsseele zu, schreiben es dieser so zu, daß sie in dem feinsten menschlichen Leib eingeschlossen ist, in dem, was wir - bitte, stoßen Sie sich nicht an dem Ausdruck, nehmen Sie ihn als Terminus technicus - den astralischen Leib nennen. Es ist der Wesensteil des Menschen, der gleichsam dem Menschen dasjenige an das äußere Irdische anknüpft, was inspirierend hereinwirkt in sein Inneres, was er nicht durch die äußeren Sinne wahr­nehmen kann, auch nicht wahrnehmen kann, wenn er durch sein eige­nes Inneres in den Ätherleib hineinsieht, sondern was er wahrnimmt, wenn er von sich selber, von dem Ätherleib unabhängig wird und ver­bunden ist mit den Kräften seines Ursprungs.",
      "So haben wir die Empfindungsseele im astralischen Leib, die Ver­standes- oder Gemütsseele im ätherischen Leib und die Bewußtseinsseele im physischen Leib. In den Zeiten des alten Hellsehens waren diese Dinge mehr oder weniger instinktiv bewußt den Menschen, denn sie sahen in sich hinein, sie sahen dieses dreigliedrige Seelenwesen. Nicht daß sie sich verstandesmäßig die Seele zergliedert hätten, aber indem sie ein hellseherisches Bewußtsein hatten, stand vor ihnen die dreiglied­rige Menschenseele: die Empfindungsseele im astralischen, die Verstan­des- oder Gemütsseele im ätherischen und die Bewußtseinsseele im phy­sischen Leibe. Indem sie zurückblickten, sahen sie, wie das Äußere des Menschen, die äußere Gestalt, als das Tierische längst verhärtet war, sich aus dem herausentwickelte, was uns heute in seinem Ergebnis als dreifache Seelenkräfte entgegentritt. Da empfanden sie, daß diese drei­fache Gliederung aus übersinnlichen schöpferischen Mächten herausgeboren ist. Sie empfanden, daß die Empfindungsseele aus übersinn­lichen schöpferischen Mächten herausgeboren ist, die dem Menschen den astralischen Leib gaben, jenen Leib, den er nicht nur hat wie seinen ätherischen und physischen Leib zwischen Geburt und Tod, sondern",
      "den er mitnimmt, wenn er durch die Pforte des Todes schreitet, und den er schon hatte, bevor er durch die Geburt ins Dasein trat. So sahen die alten Hellseher die Empfindungsseele verbunden mit dem astra­lischen Leibe und das, was sozusagen aus den geistigen Welten inspi­rierend auf den Menschen wirkt und seinen astralischen Leib schafft, als die eine schöpferische Kraft, die den Menschen aus dem Weltgan­zen heraus bildet.",
      "Und als eine zweite schöpferische Kraft sahen sie das, was wir heute im Ergebnis der Verstandes- oder Gemütsseele haben und was den ätherischen Leib schafft so, daß dieser ätherische Leib alle äußeren Substanzen, alle äußeren Materien umwandelt, so daß sie die physische Menschengestalt im menschlichen, nicht im tie­rischen Sinn durchdringen können. Den schöpferischen Geist für den ätherischen Leib, der in seinen Ergebnissen in unserer Verständesseele auftritt, sahen die alten Hellseher als eine übermenschliche kosmische Macht hereinwirken, etwa wie im Magnetismus in die physische Ma­terie herein, so in den Menschen herein.",
      "Sie sahen hinauf in die geisti­gen Welten, sahen eine göttlich-geistige Macht, welche den ätherischen Leib des Menschen zimmert, schmiedet, so daß dieser ätherische Leib der Werkmeister, der Baumeister wird, der die äußere Materie um­gestaltet, sie gleichsam durcheinanderbringt, sie pulverisiert, mahlt, so daß das, was sonst als Materie vorhanden ist, im Menschen sich gliedert und der Mensch die menschlichen Fähigkeiten bekommt. Die alten Hellseher sahen, wie diese schöpferische Kraft alle Materie in kunst­voller Weise umschafft, so daß sie menschliche Materie werden konnte.",
      "Dann wiederum sahen sie auf das Dritte, auf die Bewußtseinsseele, die den egoistischen Menschen eigentlich macht, welche die Umwandlung von dem physischen Leib ist, und sie schrieben diejenigen Kräfte, welche in diesem physischen Leibe walten, einzig und allein der Ver­erbungslinie zu, dem, was von Vater und Mutter, von Großvater und Urgroßvater abstammt, kurz, was Ergebnis der menschlichen Liebes­kräfte, der menschlichen Fortpflanzungskräfte ist. Darin sahen sie die dritte schöpferische Macht.",
      "Die Macht der Liebe wirkt von Generation zu Generation.",
      "Zu drei Mächten sahen die alten Hellseher hinauf, zu einem schöp­ferischen Wesen, das unsere Empfindungsseele zuletzt hervorruft, indem",
      "es im Menschen den astralischen Leib gestaltet, der von den über­sinnlichen Mächten inspiriert werden kann, weil er der Leib ist, den der Mensch hatte, bevor er ein physisches Wesen durch die Empfäng­nis wurde, der Leib, welchen der Mensch haben wird, wenn er durch die Pforte des Todes geschritten ist. Dieses Kräftegebilde, können wir besser sagen, dieses gleichsam himmlische Gebilde im Menschen, das dauert, während Ätherleib und physischer Leib vorübergehen, das ist zugleich für die alten Hellseher dasjenige gewesen - das ergab ihnen ihre unmittelbare Erfahrung -, was ins menschliche Leben alle Kultur hereinbringen konnte.",
      "Deshalb sahen sie im Bringer des astralischen Leibes jene Macht, die das Göttliche hereinträgt, die selber nur aus dem Dauernden besteht, durch welches das Ewige der Welt hereinsingt und hereintönt. Und die alten Hellseher, denen - ich sage es ungescheut - die Gestalten von Kalewala entsprungen sind, haben die lebendige pla­stische Ausgestaltung derjenigen Schöpfungsmacht, die uns im Resultat der Empfindungsseele entgegendringt, die das Göttliche in das Mensch­liche hereininspiriert, hingestellt in Wäinämöinen.",
      "Wäinämöinen ist der Schöpfer jenes menschlichen Leibesgliedes, das über Geburt und Tod hinausdauert und das das Himmlische ins Irdische hereinbringt. Und wir sehen die zweite Gestalt in Kalewala: Ilmarinen.",
      "Wenn wir zurückgehen auf das alte hellseherische Bewußtsein, dann finden wir, daß Ilmarinen alles das herausschafft, was Abbild ist in seiner leben­digen Gestaltung vom ätherischen Leib aus den Kräften der Erde und aus dem, was nicht der sinnlichen Erde, sondern was den tieferen Kräf­ten der Erde angehört. Wir sehen in Ilmarinen den Bringer desjenigen, was alle Materie umgestaltet, ummahlt.",
      "Wir sehen in ihm den Schmied der menschlichen Gestalt. Und wir sehen in dem Sampo den mensch­lichen Ätherleib, geschmiedet von Ilmarinen aus der übersinnlichen Welt heraus, damit die sinnliche Materie pulverisiert und dann fort-geleitet werden kann von Generation zu Generation, so daß in den Kräften, welche die dritte göttliche übersinnliche Wesenheit gibt, von Generation zu Generation durch die Liebeskräfte die menschliche Be­wußtseinsseele im physischen Menschenleib fortwirkt.",
      "Diese dritte gött­lich-übersinnliche Macht sehen wir in Lemminkäinen. So sehen wir tiefe Geheimnisse der Menschheitsentstehung in dem Schmieden des",
      "Sampo, sehen tiefe Geheimnisse aus dem alten hellseherischen Bewußt­sein heraus auf dem Grund von Kalewala und blicken 50 in mensch­liche Vorzeiten zurück, von denen wir uns sagen dürfen: Nicht war damals das Zeitalter, wo man hätte mit Verstand die Naturerscheinun­gen zergliedern können. Primitiv war alles, aber im Primitiven lebte die Anschauung dessen, was hinter dem Sinnlichen steht.",
      "Nun war es so, daß, wenn diese Leiber des Menschen geschmiedet waren, wenn namentlich der ätherische Leib des Menschen, der Sampo, geschmiedet war, daß das erst eine Weile verarbeitet werden mußte, daß der Mensch nicht sogleich die Kräfte hatte, die ihm dadurch von den übersinnlichen Mächten bereitet waren. Indem der Ätherleib geschmiedet war, muß er erst innerlich sich einleben, wie wenn wir eine Maschine zubereiten, die erst fertig sein muß, gleichsam dann erst völlig ausreifen muß, um in Gebrauch zu treten.",
      "In dem Menschenwerden mußten immer - das zeigt sich bei aller Evolution - Zwischenzeiten zwischen dem Schaffen der entsprechenden Glieder und dem Gebrauch derselben sein. So hatte der Mensch seinen ätherischen Leib in ferner Urzeit geschmiedet.",
      "Dann kam eine Episode, wo dieser Ätherleib hinunter in die menschliche Na­tur gesandt ward. Erst später leuchtete er auf als Verstandesseele. Der Mensch lernte seine Kräfte gebrauchen als äußere Naturkräfte, er holte aus seiner eigenen Natur den verborgen gebliebenen Sampo hervor.",
      "Wir sehen in einer wunderbaren Weise bildlich dieses Geheimnis des Men­schenwerdens in dem Schmieden des Sampo, in dem Verborgensein, in dem Unwirksamsein des Sampo, in der Episode, die zwischen dem Schmieden und Wiederauffinden desselben liegt. Wir sehen den Sampo erst in die menschliche Natur versenkt, dann herausgeholt zu den äuße­ren Kulturkräften, die erst als primitive Kräfte auftreten, wie sie im zweiten Teil von Kälewäla geschildert werden.",
      "So gewinnt alles dann eine tiefe Bedeutung in diesem großen Volksepos, wenn wir in ihm Schilderungen hellseherisch erworbener alter Vorgänge des Menschenwerdens sehen, des Zustandekommens der Men­schennatur aus ihren verschiedenen Gliedern. Es war mir, der ich wahr­haftig - ich kann es Ihnen versichern - Kalewala erst lange, lange nachher kennenlernte, nachdem diese Tatsachen vom Werden der menschlichen Natur mir klar vor der Seele standen, eine wunderbare,",
      "überraschende Tatsache, gerade in diesem Epos das wiederzufinden, was ich mehr oder weniger theoretisch in meiner «Theosophie» dar­stellen konnte, die in einer Zeit geschrieben ist, als ich noch keine Zeile von Kalewala kannte. So sehen wir, wie der Menschheit Geheimnisse gerade in dem aufgehen, was Wäinämöinen gibt, er, der Schöpfer der übersinnlichen Inspirationen: die Geschichte von dem Schmieden des Ätherleibes.",
      "Aber da ist noch ein anderes Geheimnis verborgen. Ich verstehe, wohlgemerkt, nichts vom Finnischen, ich kann nur aus der Geisteswissenschaft heraus sprechen. Ich würde das Wort Sampo einzig und allein nur dadurch ausdrücken können, daß ich versuchte, ein Wort zu bilden, das auf folgende Weise entstehen könnte: In den Tieren sehen wir den ätherischen Leib so wirksam, daß er der Baumeister für die verschiedensten Gestalten wird, von den unvollkommensten zu den vollkommensten.",
      "Im menschlichen Ätherleib wurde etwas geschmiedet, was alle diese tierischen Gestalten wie in einer Einheit zusammenfaßt, nur mit der einzigen Ausnahme, daß über die Erde hin der Ätherleib, das heißt der Sampo, geschmiedet wird je nach den klimatischen und ändern Verhältnissen, so daß dieser Ätherleib die besonderen Volkscharaktere, die besonderen Volkseigentümlichkeiten in seinen Kräften hat, daß er das eine Volk so und das ändere anders gestaltet. Der Sampo ist dasjenige für jedes Volk, was die besondere Gestalt des Ätherleibes ausmacht, der gerade diese besondere Volksheit ins Leben setzt, so daß die Glieder dieser Volksheit von demselben Aussehen sind in bezug auf das, was hindurchleuchtet durch ihr Lebendiges und durch ihr Physi­sches.",
      "Insofern das gleiche Aussehen in der menschlichen Gestalt aus dem Ätherischen gezimmert ist, insofern liegen die Kräfte des Äther-leibes in dem Sampo. In dem Sampo haben wir also das Symbolum des Zusammenhaltens des finnischen Volkes, dasjenige, was in den Tiefen der Menschlichkeit macht, daß das finnische Volkstum sich gerade in einer bestimmten Gestalt ausgelebt hat.",
      "So ist es aber bei jedem Volksepos. Volksepen können nur da ent­stehen, wo die Kultur noch in die Kräfte des Sampo eingeschlossen ist, in die Kräfte des ätherischen Leibes. Solange die Kultur von den Kräf­ten des Sampo abhängt, so lange trägt das Volk den Stempel dieses Sampo. Dieser Ätherleib trägt daher in der ganzen Kultur den Charakter",
      "des Volkstümlichen, des Volksheitlichen. Wann konnte im Laufe des Kulturprozesses ein Bruch in dieses Volkstümliche, in dieses Volksheit­liche hineinkommen? Dann konnte er hineinkommen, als etwas in dem menschlichen Kulturprozeß eintrat, das nicht für einen Menschen, für einen Stamm, für ein Volk, sondern für die ganze Menschheit ist, was aus solchen Tiefen der Menschennatur, aus solchen Feinheiten und Inti­mitäten herausgenommen und dem Kulturprozeß einverleibt ist, daß es für alle Menschen gilt ohne Unterschied der Nationalität, der Rasse und so weiter.",
      "Das aber wär gegeben, als jene Mächte zu den Menschen sprachen, die nicht zu einem Volk sprachen, sondern zur ganzen Mensch­heit, jene Mächte, die nur so unpersönlich auch im Sinn der Volksheit, so fein und zart am Ende von Kalewala angedeutet werden, indem der Christus aus Mariäta geboren ist. Als Er getauft wird, da verläßt Wäi­nämöinen das Land, da ist etwas eingetreten, was die besondere Volks­heit mit dem Allgemein-Menschlichen zusammenbringt.",
      "Und hier an diesem Punkte, wo eines der bedeutendsten, prägnäntesten, grandiose­sten Volksepen in die Schilderung, in die ganz unpersönliche - erlauben Sie den paradoxen Ausdruck- unpalästinische Schilderung des Christus-Impulses einmündet, wird Kalewala ganz besonders bedeutsam. Da führt sie uns ganz besonders in das hinein, was empfunden werden kann da, wo die Wohltaten, das Glück des Sämpo lebendig empfunden werden als fortwirkend durch alles Menschenwerden und im Zusam­menwirken zugleich mit der christlichen Idee, mit dem christlichen Im­puls.",
      "Das ist das unendlich Zarte am Ende von Kalewala. Das ist es auch, was uns so klar erläutert, daß dasjenige, was vor diesem Schluß in Kalewala liegt, der vörchristlichen Zeit angehört. Aber so wahr alles Allgemein-Menschliche nur immerfort bestehen wird, indem es das In­dividuelle bewahren wird, so wahr werden die einzelnen Volkskulturen, die ihr Wesen aus alten hellseherischen Zuständen der Völker herleiten, fortleben in dem Allgemein-Menschlichen.",
      "So wahr wird alles, was Kalewalä am Schluß als Christliches andeutet, immerdar sich ver­binden, seine besondere Folge behalten durch das ohne Ende Fort-wirkende, das angedeutet ist in den Inspirationen von Wäinämöinen. Denn mit Wäinämöinen ist etwas gemeint, das jenem menschlichen Wesensteil angehört, der über Geburt und Tod erhaben ist, der mit dem",
      "Menschen durch alles Menschenwerden hindurchschreitet. So stellen uns solche Epen wie Kalewala etwas dar, was unvergänglich ist, was durchdrungen werden kann von dem, was christliche Idee ist, das sich aber geltend machen wird als Individuelles, das immer den Beweis liefern wird, daß das Allgemein-Menschliche, so wie das weiße Sonnen­licht in vielen Farben sich zerteilt, in den vielen Volkskulturen fort­leben wird. Und weil dieses Allgemein-Menschliche in dem Wesen der Volksepen das Individuelle durchdringt, das aber in jeden Menschen hineinleuchtet, zu jedem Menschen spricht, deshalb leben die Indivi­dualitäten der Völker so sehr in dem Wesen ihrer Volksepen. Deshalb stehen so lebendig vor unseren Augen die Menschen älter Zeiten, die in ihrem Hellsehen das Wesen ihres eigenen Volkstums geschaut haben, wie es uns in allen Volksepen geschildert wird, wie wir es aber doch ganz wunderbar kennenlernen können da, wo die Menschheit in ihren Intimitäten umfaßt wird durch Umstände, wie sie im finnischen Volks­tum leben, wo dieses, auf den Tiefen der Seele liegend, so dargestellt wird, daß es gleichsam unmittelbar zusammengestellt werden kann mit dem, was uns wiederum die modernste Geisteswissenschaft über die menschlichen Geheimnisse enthüllen kann.",
      "So aber sind, meine sehr verehrten Anwesenden, zugleich solche Volksepen in ihrem Wesen der lebendige Protest gegen allen Materia­lismus, gegen alles Herleiten des Menschen aus bloß äußeren materiellen Kräften, materiellen Zuständen, materiellen Wesenheiten. Es berichten uns solche Volksepen, wie insbesondere Kalewala, davon, daß der Mensch seinen Ursprung und Urstand im Geistig-Seelischen hat. Des­halb kann auch eine Erneuerung, eine Wiederbefruchtung alter Volks­epen im lebendigsten Sinn der spirituellen, der geistigen Kultur uner­meßlich große Dienste leisten. Denn wie Geisteswissenschaft heute über­haupt eine Erneuerung des menschlichen Bewußtseins sein will in der Richtung, daß das Menschentum nicht in der Materie, sondern im Geiste wurzelt, so zeigt uns eine genaue Betrachtung eines solchen Epos wie Kälewala, daß das Beste, was der Mensch hat, auch das Beste, was der Mensch ist, aus dem Geistig-Seelischen stammt. In diesem Sinne war es mir interessant, daß eine der Runen, der Kantelen unmittelbar, ich möchte sägen, Protest erhebt gegen eine Ausdeutung dessen, was in",
      "Kalewala vorkommt, in einem materialistischen Sinn. Jenes Instru­ment, jenes harfenartige, mit dem die alten Sänger von den alten Zeiten sangen, im Bild wird es angedeutet so, wie wenn es aus Materialien der physischen Welt gebildet wäre. Die alten Runen aber protestierten da­gegen, protestierten im geisteswissenschaftlichen Sinne, möchte man sagen, dagegen, daß aus Naturprodukten, welche die Sinne schauen können, das Saiteninstrument für Wäinämöinen zusammengefügt war. In Wahrheit, so sagt die alte Rune, stammt aus Geistig-Seelischem das Instrument, worauf der Mensch die Weisen spielt, die ihm unmittelbar aus der geistigen Welt hereinkommen. In diesem Sinn ist die alte Rune ganz im geisteswissenschaftlichen Sinn zu deuten, ein lebendiger Pro­test gegen die Ausdeutung dessen, wozu der Mensch imstande ist im materialistischen Sinn, eine Hindeutung darauf, daß das, was der Mensch besitzt, was sein Wesen ist und was nur symbolisch ausgedrückt wird in einem solchen Instrument, wie jenes, welches dem Wäinämöinen zugeschrieben wird, daß ein solches Instrument aus dem Geist heraus und damit überhaupt das ganze Wesen des Menschen aus dem Geist heraus stammt. Wie ein Motto für die Gesinnung der Geisteswissen­schaft kann sie gelten, die alte finnische Volksrune, die uns in die deut­sche Sprache in folgender Weise übersetzt ist, und in welcher ich den Grundton, die Grundnuance dessen, was der Vortrag erläutern wollte an dem Wesen der Volksepen, zusammenfassen kann:",
      "Falsches sagen die gewißlich",
      "Und befinden sich im Irrtum,",
      "Die da glauben, Wäinämöinen",
      "Hab gezimmert die Kantele,",
      "Unsere schönen Saitenspiele,",
      "Aus den Kinnbacken des Hechtes,",
      "Und daß Saiten er gesponnen",
      "Aus dem Schweif des Hiisi-Rosses.",
      "Sie ist aus der Not gezimmert,",
      "Kummer band dann ihre Teile,",
      "Bittere Sehnsuchtstränen spannen",
      "Und die Leiden ihre Saiten.",
      "So ist alles Wesen nicht aus Materiellem, sondern aus Geistig-Seelischem herausgeboren, so diese alte Volksrune, so wiederum die Geisteswissen­schaft, welche sich hineinstellen will in den lebendigen Kulturprozeß unserer Zeit."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Vor allen Dingen darf ich Sie um Entschuldigung bitten, wenn ich den Vortrag, den ich zu halten habe, nicht in einer der hier landesüblichen Sprachen halten kann.",
        "Es entspricht die Tatsache, daß dieser Vortrag gehalten wird, dem Wunsche der Freunde unserer Theosophischen Ge­sellschaft, für welche ich hierher gerufen worden bin, eine Reihe von Vorträgen vierzehn Tage hindurch zu halten, und welche die Meinung hatten, daß die Möglichkeit bestehe, innerhalb dieser Zeit auch die zwei angekündigten öffentlichen Vorträge einzufügen.",
        "Damit hängt es natür­lich zusammen, daß ich weiter werde um Entschuldigung bitten müssen, wenn mancher der Namen und manche der Bezeichnungen, die gerade aus dem Volksepos der Finnen entlehnt sind, vielleicht von mir, als der Sprache unkundig, nicht ganz richtig ausgesprochen werden.",
        "In die Geisteswissenschaft selber wird uns allerdings erst der Vortrag am nächsten Freitag hineinführen können.",
        "Die Betrachtung des heutigen Abends wird vielmehr eine Art Nachbargebiet betreffen, welches in eine geisteswissenschaftliche Beleuchtung gerückt werden kann.",
        "Aller­dings von einem Gebiet soll die Rede sein, das im allertiefsten Sinn des Wortes zu den interessantesten der menschlichen geschichtlichen Be­trachtung, des menschlichen geschichtlichen Nachdenkens gehört."
      ],
      [
        "Volksepen!",
        "Wir brauchen nur an einige der bekannteren Volksepen zu denken, an die Epen Homers, welche griechische Volksepen gewor­den sind, an die mitteleuropäische Nibelungensage und endlich an Ka­lewala, und sogleich wird uns aufleuchten, daß wir durch diese Volks­epen tiefer in Menschenseelen und in Menschenstreben hineingeführt werden als durch irgendeine geschichtliche Forschung, so hineingeführt werden, daß uns wichtige alte Zeiten lebendig, wie gegenwärtig vor die Seele hingerückt werden, aber in einer Weise, daß sie in unmittel­barer Gegenwart uns wie die Schicksale und das Leben gegenwärtiger, um uns herum lebender Menschen berühren.",
        "Wie ungewiß und dämmerhaft"
      ],
      [
        "sind uns geschichtlich diejenigen Zeiten des alten griechischen Vol­kes, von dem uns die Homerischen Epen erzählen, und wie schauen wir hinein, wenn wir den Inhalt der Ilias, der Odyssee auf uns wirken lassen, in die Seelen jener Menschen, die für die gewöhnliche Geschichts­betrachtung eigentlich vollständig entrückt sind.",
        "Kein Wunder, daß die Betrachtung der Volksepen für diejenigen, die sich wissenschaftlich oder literarisch damit beschäftigen, etwas Rätselhaftes hat."
      ],
      [
        "Wir brau­chen nur auf eine Tatsache in bezug auf die alten griechischen Epen hin­zuweisen, die ein geistvoller Betrachter der Ilias in einem sehr schönen, erst vor wenigen Jahren erschienenen Buch über Homers Ilias wiederholt geäußert hat.",
        "Ich meine Herman Grimm, den Neffen des großen ger­manischen Mythen-, Sagen- und Sprachforschers Jakob Grimm."
      ],
      [
        "Indem Herman Grimm die Gestalten und Tatsachen der Ilias auf sich wirken ließ, fühlte er sich immer wieder und wieder veranlaßt zu sagen: Oh, dieser Homer - wir brauchen heute nicht einzugehen auf die Frage nach der Persönlichkeit des Homer - scheint, wenn er irgend etwas schildert, das einem Handwerk, einer Kunst entlehnt ist, wie wenn er Fachmann in diesem Handwerk, in dieser Kunst wäre.",
        "Schildert er eine Schlacht, einen Kampf, so scheint er völlig bekannt zu sein mit all den strategischen und militärischen Grundsätzen, die innerhalb der Kriegsführung in Betracht kommen. - Mit Recht weist Herman Grimm darauf hin, daß ein strenger Richter in solchen Dingen ein Bewunderer der sachlichen Schlachtenschilderung Homers war, nämlich Napoleon, ein Mann, der zweifellos berechtigt war, ein Urteil darüber zu fällen, ob aus dem Geist Homers heraus das Militärische unmittelbar sachge­mäß und lebendig vor unsere Seele hingestellt wird oder nicht."
      ],
      [
        "Vom allgemein menschlichen Standpunkt aus wissen wir, wie die Gestalten plastisch, wie wenn wir sie unmittelbar vor dem physischen Auge hät­ten, durch Homer vor unsere Seele hingestellt werden."
      ],
      [
        "Wie ist es mit einem solchen Volksepos, wie erweist es sich dauernd durch die verschiedenen Zeiten?",
        "Denn wahrhaftig, derjenige, der die Verhältnisse unbefangen beobachtet, wird nicht den Eindruck erhalten, daß künstliche Veranstaltungen der Menschheit, etwa eine künstliche pädagogische Zucht, das Interesse der Jahrhunderte bis in unsere Tage herein an der Ilias und Odyssee immer wieder festgehalten haben.",
        "Dieses"
      ],
      [
        "Interesse ist ein selbstverständliches, ist ein allgemein menschliches.",
        "Nur geben uns diese Volksepen in einem gewissen Sinne eine Aufgabe an die Hand, stellen uns sogleich, wenn wir sie betrachten wollen, eine ganz bestimmte, man möchte sagen interessante Aufgabe."
      ],
      [
        "Sie wollen nämlich in allen ihren Einzelheiten ganz genau genommen werden.",
        "Wir fühlen es sogleich, daß uns etwas unverständlich wird in den Inhalten solcher Volksepen, wenn wir sie etwa so lesen wollen, wie wir irgendein modernes Kunstwerk, einen modernen Roman oder dergleichen lesen."
      ],
      [
        "Wir fühlen gleich bei den ersten Zeilen der Ilias, daß Homer genau spricht.",
        "Was schildert er uns?",
        "Er sagt es uns im Beginn.",
        "Mancherlei weiß man aus andern Darstellungen, die nicht in der Ilias enthalten sind, über Ereignisse, die sich nach rückwärts an­schließen an die Tatsachen der Iliade."
      ],
      [
        "Homer will uns nur schildern, was er in der ersten Zeile prägnant sagt: den Zorn des Achill.",
        "Und wenn wir nun die ganze Iliade durchgehen und unbefangen betrach­ten, so müssen wir sagen: Nichts ist in Wahrheit darin, was nicht so bezeichnet werden kann, daß es auftritt als Tatsache, die da folgt aus dem Zorn des Achill. - Und weiter eine eigentümliche Tatsache wiederum gleich im Beginn der Iliade."
      ],
      [
        "Homer beginnt nicht etwa einfach mit den Tatsachen, er beginnt auch nicht mit irgendeiner per­sönlichen Meinung, sondern er beginnt mit etwas, was gerade eine mo­derne Zeit vielleicht als Phrase nehmen möchte, beginnt damit, daß er sagt: Singe mir, 0 Muse, von dem Zorne des Achill! - Und je tiefer wir eindringen in dieses Volksepos, desto klarer wird es uns, daß wir gar nicht Sinn und Geist und Bedeutung desselben verstehen können, wenn wir dieses Wort im Beginne nicht ernst nehmen.",
        "Dann aber müssen wir uns fragen: Was bedeutet es eigentlich?"
      ],
      [
        "Und nun die Art der Darstellung, die ganze Art, wie die Ereignisse vor unsere Seele hingebracht werden!",
        "Es waren für viele, nicht nur fachmännische, wissenschaftliche Betrachter, sondern auch für künstle­risch umfassende Geister wie Herman Grimm, eine Frage diese Worte:"
      ],
      [
        "0 singe mir, Muse, von dem Zorne des Achill. - Eine Frage, die ihnen tief zu Herzen ging.",
        "Wie spielen in dieser Ilias, geradeso wie im Nibe­lungenlied oder in Kalewala, die Taten geistig-göttlicher Wesenheiten zusammen - in Homers Dichtungen zunächst die Taten und Absichten"
      ],
      [
        "und Leidenschaften der olympischen Götter - mit den Taten und Ab­sichten und Leidenschaften von Menschen, die, wie Achill, in einem gewissen Sinne dem gewöhnlichen Menschlichen fernstehen, und wie­derum mit den Leidenschaften und Absichten und Taten von Men­schen, die dem gewöhnlichen Menschlichen schon naheliegen wie Odys­seus oder wie Agamemnon?",
        "Wenn dieser Achill vor unsere Seele hintritt, so erscheint er uns gegenüber den Menschen, mit denen er zusam­menlebt, einsam."
      ],
      [
        "Wir fühlen sehr bald im Fortgang der Ilias, daß wir in Achill eine Persönlichkeit vor uns haben, die eigentlich über ihre innersten Angelegenheiten mit all den andern Helden nicht rechtspre­chen kann.",
        "Homer führt uns auch vor, wie Achill seine eigentlichen Herzensangelegenheiten mit göttlich-geistigen Wesenheiten auszuma­chen hat, die nicht dem Menschenreiche angehören, wie er einsam dem Menschenreiche gegenübersteht durch den ganzen Fortgang der Iliade und wiederum nahesteht übersinnlichen, überirdischen Mächten."
      ],
      [
        "Und dabei wiederum das Sonderbare, daß, wenn wir all unser menschliches Fühlen in die Art und Weise von Denken und Empfinden, wie wir sie uns im Kulturprozeß erobert haben, zusammennehmen und den Blick hinlenken nach diesem Achill, er uns dann so erscheint, daß wir oft­mals sagen müssen: Wie egoistisch, wie persönlich! - Eine Wesenheit, in deren Seele göttlich-geistige Impulse hereinspielen, sie handelt ganz aus dem unmittelbar Persönlichen heraus.",
        "Eine lange Zeit hindurch nimmt ein für die Griechen so wichtiger Krieg, wie der trojanische Sagenkrieg, nur dadurch seinen Fortgang, gewinnt die besonderen Epi­soden, welche die Iliade schildert, daß Achill für sich dasjenige aus­macht, was er persönlich auszumachen hat mit Agamemnon."
      ],
      [
        "Und immer sehen wir, daß überirdische Mächte hereinspielen.",
        "Wir sehen Zeus, Apollo, Athene die Impulse austeilen, sozusagen die Menschen an ihre Plätze hinstellen.",
        "Es war immer sonderbar, bevor die Aufgabe an mich kam, vom Standpunkt der Geisteswissenschaft an diese Dinge heranzutreten, wie ein sehr geistvoller Mann, mit dem ich das Glück hatte, oftmals persönlich auch über diese Dinge zu verhandeln, wie Herman Grimm mit diesen Dingen sich zurechtfand."
      ],
      [
        "Er hat es nicht nur in seinen Schriften, sondern oftmals im persönlichen Gespräche, und da noch viel genauer, ausgesprochen.",
        "Er sagte: Wenn wir nur das"
      ],
      [
        "zusammennehmen, was an historischen Mächten und Impulsen in der Menschheitsentwickelung spielt, dann kommen wir nicht zurecht mit dem, was da lebt und schafft namentlich in den großen Volksepen. -Daher wurde für Herman Grimm, den geistvollen Betrachter der Iliade und der Volksdichtungen überhaupt, etwas, was über die gewöhn­lichen Bewußtseinskräfte des Menschen, über Verstand, Vernunft, Sin­nesanschauung, über das gewöhnliche Gefühl hinausgeht, zu einer rea­len Macht, zu einer Macht, die schöpferisch ist ebenso wie die andern historischen Impulse.",
        "Herman Grimm sprach von einer durch die Menschheitsentwickelung durchgehenden realen schöpferischen Phan­tasie, sprach von einer Phantasie so, wie man von einer Wesenheit, von einer Realität spricht, von etwas, was für die Menschen waltete und was ihnen im Anfang der Zeiten, die wir beobachten können, im Wer­den der einzelnen Völker mehr sagen konnte als das, was die gewöhn­lichen Seelenkräfte dem Menschen sagen.",
        "Wie das Hereinleuchten einer Welt, die sich nicht in den gewöhnlichen menschlichen Seelenkräften erschöpft, so sprach Herman Grimm immer die schöpferische Phan­tasie an, die damit für ihn etwa die Rolle einer Mitschöpferin beim Menschenwerdeprozeß bekam."
      ],
      [
        "Aber nun ist es eigentümlich, wenn wir diesen Kampfplatz der Iliade, diese Darstellung des Zornes des Achill betrachten mit all dem Hereinspielen übersinnlicher göttlich-geistiger Mächte, dann kommt man doch nicht zurecht mit einer solchen Betrachtung, wie sie Herman Grimm angestellt hat, und gerade in seinem Buche über die Iliade fin­den wir manches Wort der Resignation, das uns zeigt, wie der gewöhn­liche Standpunkt, den man heute literarisch oder wissenschaftlich ein­nehmen kann, nicht mit diesen Dingen zurechtkommt.",
        "Wozu kommt Herman Grimm gegenüber der Ilias, auch gegenüber der Nibelungensage?",
        "Er kommt dazu, anzunehmen, daß den historischen Dynastien, Herrschergeschlechtern, andere vorangegangen sind.",
        "So denkt Herman Grimm tatsächlich, man möchte sagen, buchstäblich.",
        "So denkt er daran, daß etwa Zeus mit seinem ganzen Umkreis eine Art Herrschergeschlecht darstellt, das dem Herrschergeschlecht, dem Agamemnon angehört, vorangegangen sei.",
        "Er denkt also sozusagen die Menschheitsgeschichte in einer gewissen Einförmigkeit, denkt sich in den in der Ilias oder der"
      ],
      [
        "Nibelungensage dargestellten Göttem oder Heroen uralte Menschen, welche die späteren Menschen nur dadurch darzustellen wagten, daß sie ihre Taten, ihre Charaktere in das Kleid des übermenschlichen My­thos kleideten.",
        "Es gibt vieles, mit dem man sich nicht zurechtfinden kann, wenn man eine solche Voraussetzung zugrunde legt, so vor allen Dingen die besondere Art des Eingreifens der Götter gerade bei Homer.",
        "Ich bitte Sie, meine sehr verehrten Anwesenden, nur das eine zu neh­men: Thetis, die Mutter des Achill, Athene, andere Göttergestalten, wie greifen sie ein in die Ereignisse von Troja?",
        "So greifen sie ein, daß sie die Gestalt von sterblichen Menschen annehmen, diese gleichsam begeistern, diese hinführen zu ihren Taten.",
        "Sie erscheinen also nicht selber, sondern durchdringen lebendige Menschen.",
        "Lebendige Men­schen figurieren nicht nur wie ihre Stellvertreter, sondern wie die Hül­len, die von unsichtbaren Mächten durchdrungen werden, die nicht in eigener Gestalt, nicht in eigener Wesenheit auf dem Kampfplatz er­scheinen können.",
        "Es wäre doch sonderbar, anzunehmen, daß uralte Menschen der gewöhnlichen Art so dargestellt werden sollten, daß sie die stellvertretenden Menschen aus dem sterblichen Geschlecht wie zu ihrer Hülle nehmen müßten.",
        "Das ist nur eine der Hindeutungen, die uns alle beweisen können, daß wir in dieser Art nicht zurechtkommen mit den alten Volksepen."
      ],
      [
        "Ebensowenig aber kommen wir zurecht, wenn wir etwa die Ge­stalten des Nibelungenliedes nehmen, jenen Siegfried aus Xanten am Niederrhein, der nach Worms an den Burgunderhof hinversetzt wird, dort wirbt um Kriemhilde, die Schwester des Gunther, und wiederum für Gunther wirbt, durch seine besonderen Eigenschaften aber nur um Brunhilde werben kann.",
        "Und wie merkwürdig werden uns solche Ge­stalten wie Brunhilde aus Isenland, wie Siegfried, geschildert.",
        "Siegfried wird so geschildert, daß er das sogenannte Nibelungengeschlecht über­wunden hat, daß er da den Nibelungenschatz erworben, erobert hat.",
        "Durch das, was er sich durch den Sieg über die Nibelungen erworben hat, bekommt er ganz besondere Eigenschaften, die im Epos dadurch ausge­drückt werden, daß gesagt wird, er könne sich unsichtbar machen, er sei unverwundbar in gewisser Beziehung, er habe außerdem Kräfte, die der gewöhnliche Gunther nicht hat, denn dieser kann Brunhilde,"
      ],
      [
        "die sich nicht von einem gewöhnlichen Sterblichen besiegen läßt, nicht erwerben.",
        "Durch seine besonderen Kräfte, die er als der Besitzer des Nibelungenhortes hat, besiegt Siegfried Brunhilde, und wiederum da­durch, daß er die Kräfte verbergen kann, die er entfaltet, ist er in der Lage, Brunhilde dem Gunther, seinem Schwager, zuzuführen."
      ],
      [
        "Und da finden wir, wie Kriemhilde und Brunhilde, die wir dann gleichzeitig am Burgunderhof erleben, zwei ganz verschiedene Charaktere sind, Charaktere, in die offenbar Dinge hereinspielen, die mit den gewöhn­lichen menschlichen Seelenkräften nicht zu erklären sind.",
        "Dadurch kommen sie in Streit, dadurch kommt es auch, daß Brunhilde den ge­treuen Dienstmann Hagen verleiten kann, Siegfried zu töten."
      ],
      [
        "Das wie­der weist uns auf einen Zug hin, der so merkwürdig gerade in der mit­teleuropäischen Sage auftritt.",
        "Siegfried hat höhere, übermenschliche Kräfte.",
        "Diese übermenschlichen Kräfte hat er durch den Besitz des Ni­belungenhortes."
      ],
      [
        "Sie machen ihn zuletzt nicht zu einer unbedingt sieg­haften Gestalt, sondern zu einer Gestalt, die tragisch vor uns steht.",
        "Ein Verhängnis sind zugleich für den Menschen die Kräfte, die Siegfried durch den Nibelungenhort hat."
      ],
      [
        "Noch sonderbarer werden die Dinge, wenn wir die damit verwandte nordische Sage von Sigurd, dem Dra­chentöter, dazunehmen, aber aufklärend wirkt dies.",
        "Da tritt uns Si­gurd, der nichts anderes ist als Siegfried, gleich entgegen als der Besieger des Drachens, der gerade dadurch den Nibelungenhort von einem alten Zwergengeschlecht erwirbt."
      ],
      [
        "Und Brunhilde tritt uns entgegen als eine Gestalt von übermenschlicher Natur, als eine Walkürengestalt."
      ],
      [
        "Wir sehen also, daß zwei Arten, in Europa diese Dinge darzustellen, existieren.",
        "Die eine Art, welche unmittelbar alles an das Göttlich-Über­sinnliche anknüpft, welche uns noch zeigt, wie in Brunhilde etwas ge­meint ist, was unmittelbar der übersinnlichen Welt angehört, und die andere Art, welche die Sage vermenschlicht hat.",
        "Aber wir können den­noch erkennen, wie auch in dieser Art überall das Durchklingen des Göttlichen zu finden ist."
      ],
      [
        "Und nun werfen wir von diesen Sagen, von diesen Volksepen den Blick in jenes Gebiet herüber, von dem ich wahrhaftig nur als ein sol­cher sprechen darf, der die Dinge von außen ansehen kann, nur so, wie man sie erkennen kann, wenn man die betreffende Sprache nicht"
      ],
      [
        "spricht.",
        "Das bitte ich in Erwägung zu ziehen, daß ich über alles das, was dem Westeuropäer in Kalewala entgegentritt, nur so sprechen kann wie derjenige, welcher den geistigen Gehalt, die großen, gewaltigen Gestalten ins Auge faßt, und dem selbstverständlich äußerlich die zwei­fellos vorhandenen Feinheiten des Epos entgehen müssen, die dann erst herauskommen, wenn man die Sprache wirklich beherrscht, in der das­selbe abgefaßt ist."
      ],
      [
        "Aber auch bei einer solchen Betrachtung, wie eigen­tümlich tritt uns da entgegen die Dreiheit in den drei, ja, man ist eigent­lich in Verlegenheit, einen Namen zu gebrauchen, man kann nicht sagen Götter, man kann nicht sagen Heroen, sagen wir also in den drei Wesenheiten: Wäinämöinen, Ilmarinen und Lemminkäinen.",
        "Eine merk­würdige Sprache sprechen diese Gestalten, wenn wir sie in ihren Cha­rakteren miteinander vergleichen, eine Sprache, aus der wir deutlich erkennen, die Dinge, die uns gesagt werden sollen, gehen über das hin­aus, was mit den gewöhnlichen menschlichen Seelenkräften ausgerich­tet werden kann."
      ],
      [
        "Wachsen doch, wenn wir sie nur äußerlich betrachten, diese drei Gestalten ins Ungeheuerliche.",
        "Und doch wieder, was das Eigentümliche ist, indem sie ins Ungeheuerliche wachsen, steht uns jeder einzelne Zug plastisch vor Augen, so daß wir nirgends irgendwie das Gefühl haben, das Ungeheuerliche sei ein Groteskes, ein Paradoxes, überall haben wir das Gefühl, selbstverständlich muß das, was gesagt werden soll, in übermenschlicher Größe, in übermenschlicher Bedeu­tung auftreten."
      ],
      [
        "Und dann: welch Rätselhaftes im Inhalt.",
        "Etwas, was unsere Seele anspornt, an das Allermenschlichste zu denken, das aber doch wiederum über all das hinausgeht, was gewöhnliche Seelenkräfte fassen können."
      ],
      [
        "Ilmarinen, den man oftmals den Schmied, den über alles kunstvollen Schmied nennt, schmiedet für ein Gebiet, in dem sozusagen ältere Brüder der Menschheit oder wenigstens primitivere Menschen wohnen als die Finnen, für irgendein fremdes Gebiet auf Anstiften des Wäinämöinen den Sampo.",
        "Und wir sehen diese merkwürdige Sache zu­nächst, daß sich fern von dem Schauplatz, auf dem sich die Tatsachen abspielen, von denen die Rede ist, mancherlei zuträgt, daß da Zeit ver­geht, und wir sehen, wie nach einer bestimmten Zeit Wäinämöinen und Ilmarinen wiederum veranlaßt werden, das zurückzuholen, was ihnen in der Fremde geblieben ist, den Sampo."
      ],
      [
        "Wer die eigentümliche Geistessprache,"
      ],
      [
        "die aus diesem Schmieden des Sampo, aus diesem Entfernthal­ten und Wiedergewinnen desselben spricht, auf sich wirken läßt, hat unmittelbar den Eindruck - wie gesagt, ich bitte zu berücksichtigen, daß ich sozusagen als Fremder spreche und daher nur von dem Ein­druck eines solchen sprechen kann -, daß das Wesentlichste, das Be­deutungsvollste in dieser grandiosen Dichtung doch das Schmieden, das Fernhalten und das spätere Wiedererringen des Sämpo ist."
      ],
      [
        "Was mich ganz besonders merkwürdig berührt an Kalewala, ist der Schluß.",
        "Ich habe gehört, daß es Menschen gibt, welche glauben, daß dieser Schluß vielleicht eine spätere Hinzufügung sei.",
        "Für mein Gefühl gehört gerade dieser Schluß von Mariata und ihrem Sohn, dieses Hereinspielen eines ganz merkwürdigen Christentums - ich sage ausdrück­lich eines ganz merkwürdigen Christentums - zu dem Ganzen."
      ],
      [
        "Es be­kommt Kalewala dadurch, daß dieser Schluß da ist, eine ganz beson­dere Nuance, eine Färbung, die uns die Sache sozusagen erst recht ver­ständlich machen kann.",
        "Ich darf sagen, daß für mein Gefühl eine so zarte, wunderbar unpersönliche Darstellung des Christentums über­haupt sich nirgends findet als am Schluß von Kalewala."
      ],
      [
        "Losgelöst ist das christliche Prinzip von allem Örtlichen.",
        "Das Hinkommen von Märiata zu Herodes, der uns in Kalewala als Rotus entgegentritt, ist so unpersönlich gefaßt, daß man kaum an irgendeine Örtlichkeit oder Persönlichkeit in Palästina erinnert wird."
      ],
      [
        "Ja, man wird, darf man sagen, nicht einmal im allergeringsten an den historischen Christus Jesus erinnert.",
        "Als eine intimste Herzenssache der Menschheit finden wir am Schlusse von Kalewala das Eindringen der edelsten Kulturperle der Menschheit in die finnische Kultur zart angedeutet."
      ],
      [
        "Und da­mit verknüpft ist der tragische Zug, der so unendlich tief wiederum auf unsere Seele wirken kann, daß Wäinämöinen in dem Augenblick, da das Christentum einzieht, wo der Sohn der Mariata getauft wird, Abschied nimmt von seinem Volk, um in eine unbestimmte Örtlich­keit zu gehen, zurücklassend seinem Volk nur den Inhalt und die Macht dessen, was er aus seiner Sangeskunst heraus zu erzählen wußte über die uralten Geschehnisse, welche das Historische dieses Volkes ein­schließt.",
        "Dieses Zurückziehen des Wäinämöinen gegenüber dem Sohn von Mariata erscheint mir so bedeutsam, daß man darin das lebendige"
      ],
      [
        "Zusammenspiel von alldem sehen möchte, was auf dem Grund des fin­nischen Volkes, der finnischen Volksseele waltete, waltete von uralten Zeiten her in dem Moment, als das Christentum in Finnland Einlaß fand.",
        "Wie dieses uralt Waltende sich verhielt zu dem Christentum, ist so, daß man alles, was da in den Seelen spielte, mit einer wunderbaren Intimität fühlen kann.",
        "Das sage ich als etwas, von dessen Objektivität ich mir bewußt bin, das ich niemand zur Freude, niemand zur Schmei­chelei sagen möchte.",
        "Wir Westeuropäer haben durch dieses Volksepos gerade eines der wunderbarsten Beispiele, wie in unmittelbarer Gegen­wart die Glieder eines Volkes mit ihrer ganzen Seele leibhaftig vor uns stehen, so daß man durch Kalewala die finnische Seele in Westeuropa in einer Weise kennenlernt, daß man mit ihr völlig vertraut werden kann."
      ],
      [
        "Dies alles - warum habe ich es gesagt?",
        "Gesagt habe ich es, um zu charakterisieren, wie in den Volksepen etwas spricht, was durch ge­wöhnliche menschliche Seelenkräfte, selbst wenn man von der Phan­tasie als einer realen Macht spricht, nicht erklärt werden kann.",
        "Und wenn auch manchem das, was gesägt wird, nur wie eine Hypothese klingt, so darf da vielleicht das, was Geisteswissenschaft über das Wesen dieser Volksepen zu sagen hat, an diese Betrachtung über die Volksepen angeführt werden.",
        "Gewiß, ich bin mir bewußt, daß mit dem, was ich zu sägen habe, heute in unserer Gegenwart noch etwas getroffen ist, wozu die wenigsten Menschen ihre Zustimmung geben können.",
        "Von vielen wird es vielleicht wie eine Träumerei, wie eine Phantasterei an­gesehen werden; einige aber werden es wenigstens neben andern Hypo­thesen, die über das Werden der Menschheit aufgestellt werden, an­nehmen.",
        "Für denjenigen aber, der so in die Geisteswissenschaft ein­dringt, wie ich mir das im nächsten Vortrag zu schildern gestatten werde, wird nicht von einer Hypothese, sondern von einem wirk­lichen Forschungsergebnis, das sich neben andere wissenschaftliche For­schungsergebnisse hinstellen kann, gesprochen.",
        "Fremd klingen die Dinge, über die gesprochen werden muß, aus dem Grunde, weil gerade jene Wissenschaftlichkeit, welche heute glaubt, ganz fest auf dem Boden des Tatsächlichen, des Währen zu stehen, des einzig Erreichbaren, sich nur auf das beschränkt, was äußere Sinne wahrnehmen, was der an die"
      ],
      [
        "Sinne und das Gehirn gebundene Verstand von den Dingen erkunden kann.",
        "Und es gilt deshalb heute vielfach für unwissenschaftlich, wenn von einer Forschungsmethode gesprochen wird, welche zu andern Kräf­ten der Seele greift, denen es möglich ist, in das Übersinnliche und in das Hereinspielen des Übersinnlichen in das Sinnliche zu schauen.",
        "Durch diese Forschungsmethode, durch Geisteswissenschaft, wird man nicht bloß zu der abstrakten Phantasie geführt, zu welcher Herman Grimm den Volksepen gegenüber geführt worden ist, sondern man wird zu etwas geführt, das weit über die Phantasie hinausgeht, was einen ganz andern Seelen- oder Bewußtseinszustand darstellt, als ihn der Mensch in dem gegenwärtigen Zeitpunkt seiner Entwickelung haben kann.",
        "Und so werden wir durch Geisteswissenschaft in einer ganz an­dern Weise zur menschlichen Vorzeit zurückgeführt als etwa durch die gewöhnliche Wissenschaft."
      ],
      [
        "Die gewöhnliche Wissenschaft ist es heute gewöhnt, rückblickend das Werden der Menschheit so zu betrachten, daß das, was wir heute Menschen nennen, sich nach und nach aus niedrigeren, tierähnlichen Geschöpfen heraus entwickelt hat.",
        "Geisteswissenschaft stellt sich nicht etwa dieser modernen Forschung kampfgerüstet gegenüber, sondern er­kennt völlig das Große und Gewaltige der Errungenschaften dieser Naturwissenschaft des 19.",
        "Jahrhunderts an, das Bedeutungsvolle des Gedankens einer Umwandlung der tierischen Formen von dem Un­vollkommensten zum Vollkommenen und einen Anschluß der äußeren Menschenform an die vollkommenste tierische Form.",
        "Aber sie kann bei einer solchen Betrachtung des Menschenwerdens, des Werdens der Organismen überhaupt, nicht stehenbleiben, die sich etwa darstellen würde, wenn man mit einem äußeren sinnlichen Blick dasjenige über­schauen könnte, was sich im Laufe des Erdengeschehens in der organi­schen Welt bis zum Menschen herauf vollzogen hat.",
        "Für die Geistes­wissenschaft steht heute der Mensch neben der tierischen Welt da.",
        "Wir erblicken in der Welt, die uns umgibt, die verschieden geformten tie­rischen Gestalten.",
        "Wir erblicken über die Erde hin ausgebreitet das in einer gewissen Weise einheitliche Menschengeschlecht.",
        "Wir haben auch in der Geisteswissenschaft einen unbefangenen Blick dafür, wie in der äußeren Form alles für die Verwandtschaft des Menschen mit den"
      ],
      [
        "übrigen Organismen spricht, aber wir können in der Geisteswissen­schaft, wenn wir das Werden der Menschheit rückwärts verfolgen, nicht so zurückgehen, daß wir in einer grauen Vorzeit etwa unmittelbar hin­einlaufen lassen den Strom der Menschheit in die tierische Entwicke­lungsreihe.",
        "Wir finden nämlich, wenn wir von der Gegenwart in die Vergangenheit zurückgehen, daß wir nirgends unmittelbar die gegen­wärtige Menschengestalt, den gegenwärtigen Menschen aus irgend­einer Tierform, die wir wiederum aus der Gegenwart kennen, anreihen dürfen."
      ],
      [
        "Wenn wir in der Menschheitsentwickelung zurückgehen, dann fin­den wir zunächst, man möchte sagen, bis zu immer primitiveren For­men beim Menschen die Seelenkräfte ausgebildet, die Verstandes- und Gemüts- und Willenskräfte, die wir auch in der Gegenwart haben.",
        "Dann kommen wir zurück bis in graue Vorzeiten, von denen uns alte Dokumente nur spärlich erzählen."
      ],
      [
        "Selbst da, wo wir so weit zurück­gehen können wie bei den Ägyptern oder den vorderasiatischen Völ­kern, werden wir überall in ein uraltes Menschentum zurückgeführt, welches zwar in einer gewissen Beziehung primitiver, aber auch groß­artiger dieselben Kräfte, Gemüts-, Verstandes- und Willenskräfte hat, die allerdings erst gegen die Gegenwart herein ihre jetzige Ausbildung gefunden haben, die wir aber als wichtigste Menschheitsimpulse, als wichtigste geschichtliche Impulse erblicken, soweit wir eben die Mensch­heit zunächst, indem wir diese ihre gegenwärtige Seele in Betracht zie­hen, zurückverfolgen können.",
        "Da finden wir nirgends die Möglichkeit, auch den am weitesten zurückliegenden Menschenschlag etwa in eine besondere Verwandtschaft mit den heutigen tierischen Formen zu stel­len."
      ],
      [
        "Dies, was so Geisteswissenschaft für sich behaupten muß, erkennen heute selbst schön denkende Naturforscher an.",
        "Aber indem wir weiter zurückgehen und betrachten, wie doch die menschliche Seele sich än­dert, wenn wir vergleichen, wie gegenwärtig ein Mensch, sagen wir, wissenschaftlich oder sonst denkt, wie er seinen Verstand anwendet und seine Gemütskräfte wirken, wenn wir das zurückverfolgen - oh, wir können es ziemlich genau verfolgen -: in einer bestimmten Zeit leuchtete es zuerst in der Menschheit auf."
      ],
      [
        "Wir möchten sagen: In dem 6., 7. vorchristlichen Jahrhundert leuchtete es auf.",
        "Die gesamte Konfiguration"
      ],
      [
        "des gegenwärtigen Fühlens und Denkens reicht eigentlich nicht weiter zurück als in jene Zeiten, von denen uns als den Zeiten der ersten griechischen Naturphilosophie erzählt wird."
      ],
      [
        "Wenn wir weiter zurückkommen und unbefangenen Blick genug haben, finden wir, ohne noch die Geisteswissenschaft zu berühren, daß nicht nur alles gegenwärtige wissenschaftliche Denken aufhört nach rückwärts hin, sondern daß die menschliche Seele überhaupt in einer ganz andern Verfassung ist, in einer viel unpersönlicheren Verfassung, aber auch in einer solchen Verfassung, daß wir ihre Kräfte viel mehr als instinktiv ansprechen müssen.",
        "Nicht etwa so, wie wenn wir sagen wollten, daß von dieser Zeit die Menschen aus solchen Instinkten her­aus gehandelt hätten wie die heutigen Tiere, aber jene Leitung durch Vernunft und Verstand, wie sie heute vorhanden ist, war nicht da."
      ],
      [
        "Dafür aber war eine gewisse instinktive, unmittelbare Sicherheit bei den Menschen da.",
        "Sie handelten aus unmittelbaren, elementaren Im­pulsen heraus, sie kontrollierten nicht durch den an das Gehirn ge­bundenen Verstand."
      ],
      [
        "Da finden wir allerdings, daß in der menschlichen Seele diejenigen Kräfte ungemischt noch walten, die wir heute abge­sondert als Verstandeskräfte haben, und jene Kräfte, die wir heute sorgfältig von den Verstandes- und zur Wissenschaft führenden Kräf­ten absondern, die Phantasiekräfte.",
        "Phantasie, Verstand und Vernunft, sie wirken in jenen alten Zeiten durcheinander."
      ],
      [
        "Je weiter wir zurück­gehen, desto mehr finden wir, daß wir gar nicht mehr das, was da in der Seele der Menschen waltete, was da ungetrennt als Phantasie und Verstand wirkte, so ansprechen dürfen, wie wir heute eine Seelenkraft bezeichnen, wenn wir sie Phantasie nennen.",
        "Wir wissen heute ganz genau, wenn wir von der Phantasie sprechen, so sprechen wir von einer Seelenkraft, deren Ausdrücke wir nicht wiederum wirklich anwenden dürfen, denen wir nicht Realität zuschreiben dürfen."
      ],
      [
        "Der moderne Mensch ist sorgsam in dieser Sache, er hütet sich wohl, dasjenige, was ihm die Phantasie gibt, zusammenzumischen mit dem, was die Logik der Vernunft ihm sagt.",
        "Sehen wir auf das, was der Geist der Menschen in jenen vorhistorischen Zeiten äußert, bevor Phantasie und Verstand abgesondert auftreten, dann fühlen wir in den Seelen eine ursprüng­liche, elementare, instinktive Kraft walten."
      ],
      [
        "Wir können in ihr Merkmale"
      ],
      [
        "der heutigen Phantasie finden, aber das, was - wenn wir den Aus­druck gebrauchen - Phantasie damals der menschlichen Seele gab, hatte etwas mit einer Wirklichkeit, mit einer Realität zu tun.",
        "Die Phantasie war noch nicht Phantasie, sie war noch - ich darf mich nicht scheuen, den Ausdruck unmittelbar zu gebrauchen - hellsichtige Kraft, war noch ein besonderes Seelenvermögen, war die Gabe der Seele, durch die der Mensch Dinge sah, Tatsachen sah, die ihm heute in seiner Entwicke­lungsepoche, wo Verstand und Vernunft sich besonders ausbilden sol­len, verborgen sind.",
        "Tiefer hinunter drangen jene Kräfte, die nicht Phantasie, sondern hellsichtige Kraft waren, in verborgene Kräfte und verborgene Daseinsformen, die hinter der sinnlichen Welt liegen.",
        "Das ist das, wozu uns eine unbefangene Betrachtung führen muß, daß, wenn wir rückläufig die Menschheitsentwickelung betrachten, wir uns sägen müssen: Wahrhaftig, wir müssen das Wort Evolution, Entwicke­lung, ernst nehmen."
      ],
      [
        "Daß die Menschheit in der Gegenwart, in den letzten Jahrhunder­ten und Jahrtausenden sozusagen zu ihren sie heute so hochbringenden Vernunft- und Verstandeskräften gekommen ist, das ist ein Entwicke­lungsergebnis.",
        "Diese Seelenkräfte haben sich aus andern heraus ent­wickelt.",
        "Und während diese unsere gegenwärtigen Seelenkräfte auf das beschränkt sind, was sich in der äußeren Sinneswelt darbietet, sah eine ursprüngliche Menschheit, die allerdings auf Wissenschaft im heu­tigen Sinn, auf Verstandesgebrauch im heutigen Sinn verzichten mußte, sah eine ursprüngliche menschliche Seelenkraft auf dem Grund aller einzelnen Völker in Untergründe des Daseins hinein, in ein Gebiet, das als ein übersinnliches hinter dem Sinnlichen liegt.",
        "Hellseherische Kräfte waren bei allen Völkern einstmals den menschlichen Seelen eigen, und aus diesen hellseherischen Kräften heraus haben sich erst die gegenwärtigen menschlichen Verstandes- und Vernunftkräfte, hat sich die gegenwärtige Art, zu denken und zu fühlen, gebildet.",
        "Jene See­lenkräfte, die wir in einer gewissen Weise als hellseherische Kräfte an­sprechen dürfen, wären nun so, daß der Mensch zugleich fühlte: Ich bin es nicht selbst, der da in mir denkt, in mir fühlt. - Der Mensch fühlte sich wie hingegeben mit seiner ganzen Körperlichkeit und auch mit seinem Seelenwesen an höhere, übersinnliche Kräfte, die in ihm"
      ],
      [
        "wirkten und lebten.",
        "So fühlte sich der Mensch wie ein Gefäß, durch das übersinnliche Kräfte selbst sprachen.",
        "Wenn man das bedenkt, dann begreift man auch den Sinn der Fortentwickelung der Mensch­heit.",
        "Die Menschen wären unselbständige Wesen geblieben, die sich nur als Gefäße, als Hüllen von Mächten und Wesenheiten hätten füh­len können, wenn sie nicht zum eigentlichen Verstandes- und Ver­nunftgebrauch vorgeschritten wären."
      ],
      [
        "Selbständiger ist der Mensch ge­worden durch Verstandes- und Vernunftgebrauch, zugleich aber auch für eine Weile der Entwickelung von der geistigen Welt in gewisser Beziehung abgeschnitten, abgeschnitten von den übersinnlichen Un­tergründen des Daseins.",
        "In der Zukunft wird das wieder anders wer­den."
      ],
      [
        "Je weiter wir zurückgehen, desto tiefer sieht durch die hellsehe­rischen Kräfte die menschliche Seele in die Untergründe des Daseins hinein, sieht hinein, wie aus diesen Untergründen des Daseins auch diejenigen Kräfte hervorgegangen sind, die am Menschen selber in vorhistorischer Zeit gearbeitet haben, bis in einen Zeitpunkt hinein, in dem alle Verhältnisse der Erde noch ganz anders waren als heute, wo sie so waren, daß die Formen der Lebewesen viel beweglicher, viel mehr einer Art von Metamorphose unterworfen waren als heute.",
        "So müssen wir weit von dem, was man gegenwärtige menschliche Kulturzeit nennt, zurückgehen, müssen nebeneinander Menschenwerden und tierisches Werden verfolgen."
      ],
      [
        "Und viel weiter zurückliegend, als man heute gewöhnlich glaubt, ist die Abtrennung der tierischen Form von der menschlichen.",
        "Die tierischen Formen sind dann erstarrt, sind un­beweglicher geworden in einer Zeit, in der die menschliche Form noch durchaus weich und biegsam war und geformt und geprägt werden konnte von dem, was innerlich seelisch erlebt wurde."
      ],
      [
        "Da kommen wir allerdings im Menschenwerden in eine Zeit zurück, bis zu der das heu­tige Bewußtsein nicht reicht, aber für die noch ein anderes Bewußtsein in der Seele vorhanden war, das im Zusammenhang mit den hellseheri­schen Kräften steht, die eben charakterisiert worden sind.",
        "Ein solches Bewußtsein, das auf die Vergangenheit hinblicken konnte und die Menschheitsentwickelung im Herkommen aus der Vergangenheit schon in völliger Abtrennung von allem tierischen Leben sah, sah auch, wie die menschlichen Kräfte walteten, aber noch in lebendigem Zusammenhang"
      ],
      [
        "mit den übersinnlichen Kräften, die da hereinspielten.",
        "Es sah das­jenige, was in den Zeiten, in denen zum Beispiel die Homerischen Epen entstanden sind, nur noch als ein alter Nachklang vorhanden war, und was in noch früheren Zeiten in einem viel erhöhteren Maße vorhanden war."
      ],
      [
        "Wenn wir hinter Homer zurückgingen, so fänden wir, daß die Menschen hellseherisches Bewußtsein hatten, das sich an menschliche vorgeschichtliche Ereignisse gleichsam erinnerte und in der Erinnerung den Hergang bei der Menschwerdung zu erzählen vermochte.",
        "Zu Ho­mers Zeiten war dann die Sache schon so, daß man fühlte, das alte hellseherische Bewußtsein war im Schwinden, aber man fühlte noch, daß es da war."
      ],
      [
        "Das war eine Zeit, in der nicht der Mensch als selbstän­diges egoistisches Wesen von sich aus sprach, sondern in der aus ihm heraussprachen Götter, übersinnlich geistige Kräfte.",
        "So müssen wir es ernst nehmen, wenn Homer nicht von sich spricht, sondern wenn er sagt: Singe mir, o Muse, von dem Zorn des Achill!"
      ],
      [
        "Singe in mir, höheres Wesen, Wesen, das durch mich spricht, das von mir Besitz ergreift, indem ich singe und sage. - Eine Realität ist diese erste Zeile bei Homer.",
        "Hingewiesen werden wir also nicht auf alte Herrscherdyna­stien, die im gewöhnlichen Sinne unserer jetzigen Menschheit ähnlich sind, sondern hingewiesen werden wir durch Homer selber darauf, daß es in der Urzeit andere Menschen gegeben hat, Menschen, in denen das Übersinnliche lebte."
      ],
      [
        "Und Achill ist durchaus noch eine Persönlich­keit aus der Übergangszeit vom alten Hellsehen zu der modernen An­schauungsweise, die wir schon bei Agamemnon, die wir bei Nestor und Odysseus finden, die aber dann weitergeführt wird zu einer höheren Anschauung.",
        "Nur dadurch begreifen wir Achill, wenn wir wissen, daß Homer in ihm einen Angehörigen der alten Menschheit hinstellen will, der in einer Zeit lebte, die zwischen jener Zeit liegt, wo die Menschen noch unmittelbar zu den alten Göttern hinaufreichten und der gegen­wärtigen Menschheitszeit, die etwa mit Agamemnon beginnt."
      ],
      [
        "Ebenso werden wir auf eine menschliche Vorzeit in der mitteleuro­päischen Nibelungensage hingewiesen.",
        "Das zeigt uns die ganze Dar­stellung dieses Epos.",
        "Wir haben es da zwar schon zu tun mit Menschen unserer Gegenwart in gewisser Beziehung, aber mit solchen Menschen unserer Gegenwart, die sich noch etwas herüberbewahrt haben aus der"
      ],
      [
        "Zeit des alten Hellsehens.",
        "All die Eigenschaften, die von Siegfried an­geführt werden, daß er sich unsichtbar machen kann, daß er Kräfte hat, durch die er Brunhilde überwindet, welche ein gewöhnlicher Sterb­licher nicht überwinden kann, all das zeigt uns neben dem andern, was uns von ihm mitgeteilt wird, daß wir in ihm einen Menschen haben, der wie in einer inneren menschlichen Erinnerung die Errungenschaften der alten Seelenkräfte, die mit Hellsichtigkeit und dem Verbundensein mit der Natur verknüpft waren, in das gegenwärtige Menschentum herübergetragen hat."
      ],
      [
        "An welchem Übergang steht Siegfried?",
        "Das zeigt uns Brunhildes Verhältnis zu Kriemhilde, der Frau des Siegfried.",
        "Es kann hier nicht näher ausgeführt werden, was die beiden Gestalten bedeuten.",
        "Aber wir kommen zurecht mit all diesen Sagen, wenn wir mit den Gestalten, die uns vorgeführt werden, bildliche Darstellungen für innere hellseherische oder erinnerte hellseherische Verhältnisse sehen."
      ],
      [
        "So dürfen wir in Siegfrieds Verhältnis zu Kriemhilde sein Ver­hältnis zu seinen eigenen Seelenkräften sehen, die in ihm walten.",
        "Seine Seele ist gewissermaßen eine Übergangsseele, und zwar dadurch, daß Siegfried sich mit dem Nibelungenschatz, das heißt, mit den hellseheri­schen Geheimnissen der alten Zeit noch etwas in die neue Zeit her-überbringt, was ihn aber zugleich für seine Gegenwart ungeeignet macht."
      ],
      [
        "So konnten leben mit diesem Nibelungenhort, das heißt mit den alten hellseherischen Kräften, die Menschen der alten Zeit.",
        "Die Erde hat ihre Bedingungen geändert.",
        "Dadurch ist Siegfried, der in seiner Seele noch einen Nachklang der alten Zeit trägt, nicht mehr hinein-passend in die Gegenwart, dadurch wird er zu einer tragischen Ge­stalt."
      ],
      [
        "Wie kann sich die Gegenwart zu dem verhalten, was für Sieg­fried noch lebendig ist?",
        "Für ihn ist noch etwas von den alten hellsehe­rischen Kräften lebendig, denn als er überwunden wird, bleibt Kriem­hilde zurück."
      ],
      [
        "Ihr wird der Nibelungenhort gebracht, sie kann ihn an­wenden.",
        "Wir erfahren, daß ihr später durch Hagen der Nibelungenhort genommen wird.",
        "Wir können sehen, daß auch Brunhilde in ge­wisser Weise in der Lage ist, mit den alten hellseherischen Kräften zu arbeiten."
      ],
      [
        "Dadurch steht sie denjenigen Menschen entgegen, die in die damalige Gegenwart hineingepaßt sind: Gunther und seinen Brüdern, Gunther vor allem, für den Brunhilde nichts übrig hat.",
        "Warum das?"
      ],
      [
        "Nun, wir wissen aus der Sage, daß Brunhilde eine Art Walkürengestalt ist: also wiederum etwas in der menschlichen Seele, und zwar dasjenige, mit dem sich in alten Zeiten durch die hellseherischen Kräfte der Mensch noch vereinigen konnte, das sich aber zurückgezogen hat vom Menschen, unbewußt geworden ist und mit dem sich der Mensch so, wie er gegenwärtig im Verstandeszeitalter lebt, erst nach dem Tod vereinigen kann.",
        "Daher die Vereinigung mit der Walküre im Moment des Todes.",
        "Die Walküre ist die Personifikation der lebendigen Seelen-kräfte, die im gegenwärtigen Menschen sind, jener Seelenkräfte, bis zu denen das alte hellseherische Bewußtsein hinkäm, die aber der gegen­wärtige Mensch erst erlebt, wenn er durch die Pforte des Todes tritt.",
        "Da wird er erst mit dieser Seele, die in Brunhilde dargestellt wird, vereint.",
        "Weil Kriemhilde noch etwas weiß von der alten Hellseher-zeit und den Kräften, welche die Seele durch das alte Hellsehen emp­fängt, wird sie zu einer Gestalt, deren Zorn geschildert wird, wie in der Ilias der Zorn des Achilles.",
        "Das wird uns hinlänglich angedeutet, daß die Menschen, die in alten Zeiten noch mit hellseherischen Kräften be­gabt waren, nicht kontrollierten mit dem Verstand, nicht den Verstand walten ließen, sondern unmittelbar aus ihren elementarsten, intensiv­sten Impulsen heraus wirkten.",
        "Daher das Persönliche, das unmittelbar Egoistische, sowohl bei Kriemhilde wie bei Achill."
      ],
      [
        "Insbesondere interessant wird die ganze Sache in der Betrachtung der Volksepen, wenn wir zu den angeführten Volksepen Kalewala hin­zunehmen.",
        "Wir werden zeigen können, heute kann das wegen der Kürze der Zeit bloß angedeutet werden, daß Geisteswissenschaft in unserer Gegenwart nur deshalb auf die alten hellseherischen Zustände der Menschheit hinweisen kann, weil es möglich wird, heute wiederum"
      ],
      [
        "- allerdings in einer erhöhteren Weise, vom Verstand durchdrungen, nicht traumhaft - die hellseherischen Zustände durch geistige Schulung hervorzurufen.",
        "Der Mensch der Gegenwart wächst allmählich wieder in ein Zeitalter hinein, in dem aus den Tiefen der menschlichen Seele verborgene Kräfte, die wiederum ins Übersinnliche hineinweisen - allerdings nunmehr geführt von Vernunft, nicht unkontrolliert von dieser -, heräuswachsen werden, wo diese Menschen ins übersinnliche Gebiet hinaufweisen werden, so daß wir die Gebiete wieder kennenlernen"
      ],
      [
        "werden, von denen uns die alten Volksepen aus dem dumpfen Bewußtsein der alten Zeiten heraus sprechen.",
        "Daher können wir sägen:"
      ],
      [
        "Man lernt erkennen, daß es möglich ist, eine Offenbarung der Welt zu gewinnen, nicht bloß durch die äußeren Sinne, sondern durch etwas Übersinnliches, das dem äußeren physischen Menschenleib zugrunde liegt."
      ],
      [
        "Es gibt Methoden - von denen soll dann im nächsten Vortrag ge­sprochen werden -, durch die der Mensch das geistige übersinnliche Innere, was heute so oftmals abgeleugnet wird, von dem sinnlichen äußeren Leib unabhängig machen kann, so daß der Mensch nicht in einem bewußtlosen Zustand lebt wie etwa im Schlaf, wenn er von sei­nem Leibe unabhängig wird, sondern daß er Geistiges um sich herum wahrnimmt.",
        "Dadurch zeigt das moderne Hellsehen dem Menschen die Möglichkeit, erkennend in einem höheren, übersinnlichen Leib zu leben, der wie ein Gefäß den gewöhnlichen Sinnenleib ausfüllt."
      ],
      [
        "Man nennt ihn in der Geisteswissenschaft den ätherischen oder Ätherleib.",
        "Dieser Ätherleib ruht in unserem Sinnenleib drinnen.",
        "Durch ihn kommen wir, wenn wir ihn innerlich von dem physisch-sinnlichen Leib loslösen, auch heute in jenen Zustand des Wahrnehmens, durch den wir über­sinnliche Tatsachen gewahr werden."
      ],
      [
        "Zweierlei übersinnlicher Tatsachen werden wir gewahr.",
        "Erstens werden wir dessen gewahr im Beginn die­ses hellseherischen Zustandes, wenn wir anfangen zu wissen, wir sehen nicht mehr durch unseren physischen Leib, wir hören nicht mehr durch unseren physischen Leib, denken auch nicht mehr durch das an den physischen Leib gebundene Gehirn."
      ],
      [
        "Da wissen wir zunächst von aller äußeren Welt noch nichts. - Ich erzähle Ihnen Tatsachen, deren genauere Begründung erst im nächsten Vortrage möglich ist. - Dafür führt uns aber die erste Stufe des Hellsehens um so mehr zu einer An­schauung unseres eigenen Ätherleibes.",
        "Wir sehen ein übersinnliches Leibliches der menschlichen Natur, das dieser zugrunde liegt, und das wir nicht anders ansprechen können als etwas, das wirkt und schafft wie eine Art von innerem Baumeister, innerem Werkmeister, das unse­ren physischen Leib lebendig durchdringt."
      ],
      [
        "Und dann werden wir des Folgenden gewahr."
      ],
      [
        "Wir werden gewahr, daß das, was wir da an uns selber wahrnehmen,"
      ],
      [
        "was wir als das eigentliche Lebendige unseres Ätherleibes an uns selber wahrnehmen, auf der einen Seite beschränkt, modifiziert wird durch unseren physischen Leib, daß es gleichsam nach der physischen Seite hin eingekleidet wird.",
        "Indem der Ätherleib auskleidet Augen und Ohren, auskleidet das physische Gehirn, gehören wir gewissermaßen dem irdischen Element an."
      ],
      [
        "Dadurch nehmen wir wahr, wie unser äthe­rischer Leib zum speziellen einzelnen, egoistischen Menschen wird, der in die Hülle seines physischen Leibes eingegliedert ist.",
        "Auf der andern Seite aber nehmen wir wahr, wie unser ätherischer Leib uns gerade wiederum in jene Regionen hineinführt, wo wir unpersönlich einem Höheren, Übersinnlichen gegenüberstehen, etwas, was nicht wir sind, was aber in uns mit voller Gegenwart vorhanden ist, was als geistige übersinnliche Macht und Kraft durch uns hindurch wirkt."
      ],
      [
        "Dadurch zerfällt für uns dann in der geisteswissenschaftlichen Betrachtung das innere Seelenleben in drei Glieder, die in drei äußere Leibeshüllen wie eingeschlossen sind, diese ausfüllend.",
        "Wir leben zunächst mit unserer Seele so, daß wir in ihr dasjenige erleben, was unsere Augen sehen, unsere Ohren hören, unsere Sinne überhaupt ergreifen können, was unser Verstand begreifen kann."
      ],
      [
        "Wir leben mit unserer Seele in unserem physischen Leibe.",
        "Insofern unsere Seele im physischen Leibe lebt, nen­nen wir sie in der Geisteswissenschaft die Bewußtseinsseele, weil erst durch das vollständige Einleben in den physischen Leib im Laufe des Menschenwerdens es möglich geworden ist, daß der Mensch zum Ich-Bewußtsein aufgerückt ist."
      ],
      [
        "Dann lernt insbesondere der moderne Hell­seher auch kennen das Leben der Seele in demjenigen, was wir Äther­leib genannt haben.",
        "Da lebt die Seele so im Ätherleib, daß sie zwar ihre Kräfte hat, daß da aber die Seelenkräfte so wirken, daß wir nicht sagen können, unsere persönlichen Kräfte sind es."
      ],
      [
        "Es sind allgemeine Menschheitskräfte, Kräfte, durch die wir den gesamten verborgenen Tatsachen der Natur viel näherstehen.",
        "Insofern die Seele diese Kräfte in einer äußeren Hülle, eben in dem Ätherleib wahrnimmt, sprechen wir von der Verstandes- oder Gemütsseele als einem zweiten Seelen-glied."
      ],
      [
        "So daß, ebenso wie wir die Bewußtseinsseele in der Hülle des physischen Leibes eingeschlossen finden, wir die Verstandes- oder Ge­mütsseele in dem ätherischen Leib eingeschlossen haben.",
        "Und dann haben"
      ],
      [
        "wir einen noch feineren Leib, durch den wir hinaufragen in die übersinnliche Welt.",
        "Alles das, was wir innerlich erleben als unsere ur­eigensten Geheimnisse, zugleich als das, was heute dem Bewußtsein ver­borgen ist und was in der Zeit des alten Hellsehens als die Werdekräfte empfunden wurde im menschlichen Entwickelungsprozeß, was so emp­funden wurde, als ob man zurückschauen könnte in die Ereignisse grauer Vorzeiten, alles das schreiben wir der Empfindungsseele zu, schreiben es dieser so zu, daß sie in dem feinsten menschlichen Leib eingeschlossen ist, in dem, was wir - bitte, stoßen Sie sich nicht an dem Ausdruck, nehmen Sie ihn als Terminus technicus - den astralischen Leib nennen.",
        "Es ist der Wesensteil des Menschen, der gleichsam dem Menschen dasjenige an das äußere Irdische anknüpft, was inspirierend hereinwirkt in sein Inneres, was er nicht durch die äußeren Sinne wahr­nehmen kann, auch nicht wahrnehmen kann, wenn er durch sein eige­nes Inneres in den Ätherleib hineinsieht, sondern was er wahrnimmt, wenn er von sich selber, von dem Ätherleib unabhängig wird und ver­bunden ist mit den Kräften seines Ursprungs."
      ],
      [
        "So haben wir die Empfindungsseele im astralischen Leib, die Ver­standes- oder Gemütsseele im ätherischen Leib und die Bewußtseinsseele im physischen Leib.",
        "In den Zeiten des alten Hellsehens waren diese Dinge mehr oder weniger instinktiv bewußt den Menschen, denn sie sahen in sich hinein, sie sahen dieses dreigliedrige Seelenwesen.",
        "Nicht daß sie sich verstandesmäßig die Seele zergliedert hätten, aber indem sie ein hellseherisches Bewußtsein hatten, stand vor ihnen die dreiglied­rige Menschenseele: die Empfindungsseele im astralischen, die Verstan­des- oder Gemütsseele im ätherischen und die Bewußtseinsseele im phy­sischen Leibe.",
        "Indem sie zurückblickten, sahen sie, wie das Äußere des Menschen, die äußere Gestalt, als das Tierische längst verhärtet war, sich aus dem herausentwickelte, was uns heute in seinem Ergebnis als dreifache Seelenkräfte entgegentritt.",
        "Da empfanden sie, daß diese drei­fache Gliederung aus übersinnlichen schöpferischen Mächten herausgeboren ist.",
        "Sie empfanden, daß die Empfindungsseele aus übersinn­lichen schöpferischen Mächten herausgeboren ist, die dem Menschen den astralischen Leib gaben, jenen Leib, den er nicht nur hat wie seinen ätherischen und physischen Leib zwischen Geburt und Tod, sondern"
      ],
      [
        "den er mitnimmt, wenn er durch die Pforte des Todes schreitet, und den er schon hatte, bevor er durch die Geburt ins Dasein trat.",
        "So sahen die alten Hellseher die Empfindungsseele verbunden mit dem astra­lischen Leibe und das, was sozusagen aus den geistigen Welten inspi­rierend auf den Menschen wirkt und seinen astralischen Leib schafft, als die eine schöpferische Kraft, die den Menschen aus dem Weltgan­zen heraus bildet."
      ],
      [
        "Und als eine zweite schöpferische Kraft sahen sie das, was wir heute im Ergebnis der Verstandes- oder Gemütsseele haben und was den ätherischen Leib schafft so, daß dieser ätherische Leib alle äußeren Substanzen, alle äußeren Materien umwandelt, so daß sie die physische Menschengestalt im menschlichen, nicht im tie­rischen Sinn durchdringen können.",
        "Den schöpferischen Geist für den ätherischen Leib, der in seinen Ergebnissen in unserer Verständesseele auftritt, sahen die alten Hellseher als eine übermenschliche kosmische Macht hereinwirken, etwa wie im Magnetismus in die physische Ma­terie herein, so in den Menschen herein."
      ],
      [
        "Sie sahen hinauf in die geisti­gen Welten, sahen eine göttlich-geistige Macht, welche den ätherischen Leib des Menschen zimmert, schmiedet, so daß dieser ätherische Leib der Werkmeister, der Baumeister wird, der die äußere Materie um­gestaltet, sie gleichsam durcheinanderbringt, sie pulverisiert, mahlt, so daß das, was sonst als Materie vorhanden ist, im Menschen sich gliedert und der Mensch die menschlichen Fähigkeiten bekommt.",
        "Die alten Hellseher sahen, wie diese schöpferische Kraft alle Materie in kunst­voller Weise umschafft, so daß sie menschliche Materie werden konnte."
      ],
      [
        "Dann wiederum sahen sie auf das Dritte, auf die Bewußtseinsseele, die den egoistischen Menschen eigentlich macht, welche die Umwandlung von dem physischen Leib ist, und sie schrieben diejenigen Kräfte, welche in diesem physischen Leibe walten, einzig und allein der Ver­erbungslinie zu, dem, was von Vater und Mutter, von Großvater und Urgroßvater abstammt, kurz, was Ergebnis der menschlichen Liebes­kräfte, der menschlichen Fortpflanzungskräfte ist.",
        "Darin sahen sie die dritte schöpferische Macht."
      ],
      [
        "Die Macht der Liebe wirkt von Generation zu Generation."
      ],
      [
        "Zu drei Mächten sahen die alten Hellseher hinauf, zu einem schöp­ferischen Wesen, das unsere Empfindungsseele zuletzt hervorruft, indem"
      ],
      [
        "es im Menschen den astralischen Leib gestaltet, der von den über­sinnlichen Mächten inspiriert werden kann, weil er der Leib ist, den der Mensch hatte, bevor er ein physisches Wesen durch die Empfäng­nis wurde, der Leib, welchen der Mensch haben wird, wenn er durch die Pforte des Todes geschritten ist.",
        "Dieses Kräftegebilde, können wir besser sagen, dieses gleichsam himmlische Gebilde im Menschen, das dauert, während Ätherleib und physischer Leib vorübergehen, das ist zugleich für die alten Hellseher dasjenige gewesen - das ergab ihnen ihre unmittelbare Erfahrung -, was ins menschliche Leben alle Kultur hereinbringen konnte."
      ],
      [
        "Deshalb sahen sie im Bringer des astralischen Leibes jene Macht, die das Göttliche hereinträgt, die selber nur aus dem Dauernden besteht, durch welches das Ewige der Welt hereinsingt und hereintönt.",
        "Und die alten Hellseher, denen - ich sage es ungescheut - die Gestalten von Kalewala entsprungen sind, haben die lebendige pla­stische Ausgestaltung derjenigen Schöpfungsmacht, die uns im Resultat der Empfindungsseele entgegendringt, die das Göttliche in das Mensch­liche hereininspiriert, hingestellt in Wäinämöinen."
      ],
      [
        "Wäinämöinen ist der Schöpfer jenes menschlichen Leibesgliedes, das über Geburt und Tod hinausdauert und das das Himmlische ins Irdische hereinbringt.",
        "Und wir sehen die zweite Gestalt in Kalewala: Ilmarinen."
      ],
      [
        "Wenn wir zurückgehen auf das alte hellseherische Bewußtsein, dann finden wir, daß Ilmarinen alles das herausschafft, was Abbild ist in seiner leben­digen Gestaltung vom ätherischen Leib aus den Kräften der Erde und aus dem, was nicht der sinnlichen Erde, sondern was den tieferen Kräf­ten der Erde angehört.",
        "Wir sehen in Ilmarinen den Bringer desjenigen, was alle Materie umgestaltet, ummahlt."
      ],
      [
        "Wir sehen in ihm den Schmied der menschlichen Gestalt.",
        "Und wir sehen in dem Sampo den mensch­lichen Ätherleib, geschmiedet von Ilmarinen aus der übersinnlichen Welt heraus, damit die sinnliche Materie pulverisiert und dann fort-geleitet werden kann von Generation zu Generation, so daß in den Kräften, welche die dritte göttliche übersinnliche Wesenheit gibt, von Generation zu Generation durch die Liebeskräfte die menschliche Be­wußtseinsseele im physischen Menschenleib fortwirkt."
      ],
      [
        "Diese dritte gött­lich-übersinnliche Macht sehen wir in Lemminkäinen.",
        "So sehen wir tiefe Geheimnisse der Menschheitsentstehung in dem Schmieden des"
      ],
      [
        "Sampo, sehen tiefe Geheimnisse aus dem alten hellseherischen Bewußt­sein heraus auf dem Grund von Kalewala und blicken 50 in mensch­liche Vorzeiten zurück, von denen wir uns sagen dürfen: Nicht war damals das Zeitalter, wo man hätte mit Verstand die Naturerscheinun­gen zergliedern können.",
        "Primitiv war alles, aber im Primitiven lebte die Anschauung dessen, was hinter dem Sinnlichen steht."
      ],
      [
        "Nun war es so, daß, wenn diese Leiber des Menschen geschmiedet waren, wenn namentlich der ätherische Leib des Menschen, der Sampo, geschmiedet war, daß das erst eine Weile verarbeitet werden mußte, daß der Mensch nicht sogleich die Kräfte hatte, die ihm dadurch von den übersinnlichen Mächten bereitet waren.",
        "Indem der Ätherleib geschmiedet war, muß er erst innerlich sich einleben, wie wenn wir eine Maschine zubereiten, die erst fertig sein muß, gleichsam dann erst völlig ausreifen muß, um in Gebrauch zu treten."
      ],
      [
        "In dem Menschenwerden mußten immer - das zeigt sich bei aller Evolution - Zwischenzeiten zwischen dem Schaffen der entsprechenden Glieder und dem Gebrauch derselben sein.",
        "So hatte der Mensch seinen ätherischen Leib in ferner Urzeit geschmiedet."
      ],
      [
        "Dann kam eine Episode, wo dieser Ätherleib hinunter in die menschliche Na­tur gesandt ward.",
        "Erst später leuchtete er auf als Verstandesseele.",
        "Der Mensch lernte seine Kräfte gebrauchen als äußere Naturkräfte, er holte aus seiner eigenen Natur den verborgen gebliebenen Sampo hervor."
      ],
      [
        "Wir sehen in einer wunderbaren Weise bildlich dieses Geheimnis des Men­schenwerdens in dem Schmieden des Sampo, in dem Verborgensein, in dem Unwirksamsein des Sampo, in der Episode, die zwischen dem Schmieden und Wiederauffinden desselben liegt.",
        "Wir sehen den Sampo erst in die menschliche Natur versenkt, dann herausgeholt zu den äuße­ren Kulturkräften, die erst als primitive Kräfte auftreten, wie sie im zweiten Teil von Kälewäla geschildert werden."
      ],
      [
        "So gewinnt alles dann eine tiefe Bedeutung in diesem großen Volksepos, wenn wir in ihm Schilderungen hellseherisch erworbener alter Vorgänge des Menschenwerdens sehen, des Zustandekommens der Men­schennatur aus ihren verschiedenen Gliedern.",
        "Es war mir, der ich wahr­haftig - ich kann es Ihnen versichern - Kalewala erst lange, lange nachher kennenlernte, nachdem diese Tatsachen vom Werden der menschlichen Natur mir klar vor der Seele standen, eine wunderbare,"
      ],
      [
        "überraschende Tatsache, gerade in diesem Epos das wiederzufinden, was ich mehr oder weniger theoretisch in meiner «Theosophie» dar­stellen konnte, die in einer Zeit geschrieben ist, als ich noch keine Zeile von Kalewala kannte.",
        "So sehen wir, wie der Menschheit Geheimnisse gerade in dem aufgehen, was Wäinämöinen gibt, er, der Schöpfer der übersinnlichen Inspirationen: die Geschichte von dem Schmieden des Ätherleibes."
      ],
      [
        "Aber da ist noch ein anderes Geheimnis verborgen.",
        "Ich verstehe, wohlgemerkt, nichts vom Finnischen, ich kann nur aus der Geisteswissenschaft heraus sprechen.",
        "Ich würde das Wort Sampo einzig und allein nur dadurch ausdrücken können, daß ich versuchte, ein Wort zu bilden, das auf folgende Weise entstehen könnte: In den Tieren sehen wir den ätherischen Leib so wirksam, daß er der Baumeister für die verschiedensten Gestalten wird, von den unvollkommensten zu den vollkommensten."
      ],
      [
        "Im menschlichen Ätherleib wurde etwas geschmiedet, was alle diese tierischen Gestalten wie in einer Einheit zusammenfaßt, nur mit der einzigen Ausnahme, daß über die Erde hin der Ätherleib, das heißt der Sampo, geschmiedet wird je nach den klimatischen und ändern Verhältnissen, so daß dieser Ätherleib die besonderen Volkscharaktere, die besonderen Volkseigentümlichkeiten in seinen Kräften hat, daß er das eine Volk so und das ändere anders gestaltet.",
        "Der Sampo ist dasjenige für jedes Volk, was die besondere Gestalt des Ätherleibes ausmacht, der gerade diese besondere Volksheit ins Leben setzt, so daß die Glieder dieser Volksheit von demselben Aussehen sind in bezug auf das, was hindurchleuchtet durch ihr Lebendiges und durch ihr Physi­sches."
      ],
      [
        "Insofern das gleiche Aussehen in der menschlichen Gestalt aus dem Ätherischen gezimmert ist, insofern liegen die Kräfte des Äther-leibes in dem Sampo.",
        "In dem Sampo haben wir also das Symbolum des Zusammenhaltens des finnischen Volkes, dasjenige, was in den Tiefen der Menschlichkeit macht, daß das finnische Volkstum sich gerade in einer bestimmten Gestalt ausgelebt hat."
      ],
      [
        "So ist es aber bei jedem Volksepos.",
        "Volksepen können nur da ent­stehen, wo die Kultur noch in die Kräfte des Sampo eingeschlossen ist, in die Kräfte des ätherischen Leibes.",
        "Solange die Kultur von den Kräf­ten des Sampo abhängt, so lange trägt das Volk den Stempel dieses Sampo.",
        "Dieser Ätherleib trägt daher in der ganzen Kultur den Charakter"
      ],
      [
        "des Volkstümlichen, des Volksheitlichen.",
        "Wann konnte im Laufe des Kulturprozesses ein Bruch in dieses Volkstümliche, in dieses Volksheit­liche hineinkommen?",
        "Dann konnte er hineinkommen, als etwas in dem menschlichen Kulturprozeß eintrat, das nicht für einen Menschen, für einen Stamm, für ein Volk, sondern für die ganze Menschheit ist, was aus solchen Tiefen der Menschennatur, aus solchen Feinheiten und Inti­mitäten herausgenommen und dem Kulturprozeß einverleibt ist, daß es für alle Menschen gilt ohne Unterschied der Nationalität, der Rasse und so weiter."
      ],
      [
        "Das aber wär gegeben, als jene Mächte zu den Menschen sprachen, die nicht zu einem Volk sprachen, sondern zur ganzen Mensch­heit, jene Mächte, die nur so unpersönlich auch im Sinn der Volksheit, so fein und zart am Ende von Kalewala angedeutet werden, indem der Christus aus Mariäta geboren ist.",
        "Als Er getauft wird, da verläßt Wäi­nämöinen das Land, da ist etwas eingetreten, was die besondere Volks­heit mit dem Allgemein-Menschlichen zusammenbringt."
      ],
      [
        "Und hier an diesem Punkte, wo eines der bedeutendsten, prägnäntesten, grandiose­sten Volksepen in die Schilderung, in die ganz unpersönliche - erlauben Sie den paradoxen Ausdruck- unpalästinische Schilderung des Christus-Impulses einmündet, wird Kalewala ganz besonders bedeutsam.",
        "Da führt sie uns ganz besonders in das hinein, was empfunden werden kann da, wo die Wohltaten, das Glück des Sämpo lebendig empfunden werden als fortwirkend durch alles Menschenwerden und im Zusam­menwirken zugleich mit der christlichen Idee, mit dem christlichen Im­puls."
      ],
      [
        "Das ist das unendlich Zarte am Ende von Kalewala.",
        "Das ist es auch, was uns so klar erläutert, daß dasjenige, was vor diesem Schluß in Kalewala liegt, der vörchristlichen Zeit angehört.",
        "Aber so wahr alles Allgemein-Menschliche nur immerfort bestehen wird, indem es das In­dividuelle bewahren wird, so wahr werden die einzelnen Volkskulturen, die ihr Wesen aus alten hellseherischen Zuständen der Völker herleiten, fortleben in dem Allgemein-Menschlichen."
      ],
      [
        "So wahr wird alles, was Kalewalä am Schluß als Christliches andeutet, immerdar sich ver­binden, seine besondere Folge behalten durch das ohne Ende Fort-wirkende, das angedeutet ist in den Inspirationen von Wäinämöinen.",
        "Denn mit Wäinämöinen ist etwas gemeint, das jenem menschlichen Wesensteil angehört, der über Geburt und Tod erhaben ist, der mit dem"
      ],
      [
        "Menschen durch alles Menschenwerden hindurchschreitet.",
        "So stellen uns solche Epen wie Kalewala etwas dar, was unvergänglich ist, was durchdrungen werden kann von dem, was christliche Idee ist, das sich aber geltend machen wird als Individuelles, das immer den Beweis liefern wird, daß das Allgemein-Menschliche, so wie das weiße Sonnen­licht in vielen Farben sich zerteilt, in den vielen Volkskulturen fort­leben wird.",
        "Und weil dieses Allgemein-Menschliche in dem Wesen der Volksepen das Individuelle durchdringt, das aber in jeden Menschen hineinleuchtet, zu jedem Menschen spricht, deshalb leben die Indivi­dualitäten der Völker so sehr in dem Wesen ihrer Volksepen.",
        "Deshalb stehen so lebendig vor unseren Augen die Menschen älter Zeiten, die in ihrem Hellsehen das Wesen ihres eigenen Volkstums geschaut haben, wie es uns in allen Volksepen geschildert wird, wie wir es aber doch ganz wunderbar kennenlernen können da, wo die Menschheit in ihren Intimitäten umfaßt wird durch Umstände, wie sie im finnischen Volks­tum leben, wo dieses, auf den Tiefen der Seele liegend, so dargestellt wird, daß es gleichsam unmittelbar zusammengestellt werden kann mit dem, was uns wiederum die modernste Geisteswissenschaft über die menschlichen Geheimnisse enthüllen kann."
      ],
      [
        "So aber sind, meine sehr verehrten Anwesenden, zugleich solche Volksepen in ihrem Wesen der lebendige Protest gegen allen Materia­lismus, gegen alles Herleiten des Menschen aus bloß äußeren materiellen Kräften, materiellen Zuständen, materiellen Wesenheiten.",
        "Es berichten uns solche Volksepen, wie insbesondere Kalewala, davon, daß der Mensch seinen Ursprung und Urstand im Geistig-Seelischen hat.",
        "Des­halb kann auch eine Erneuerung, eine Wiederbefruchtung alter Volks­epen im lebendigsten Sinn der spirituellen, der geistigen Kultur uner­meßlich große Dienste leisten.",
        "Denn wie Geisteswissenschaft heute über­haupt eine Erneuerung des menschlichen Bewußtseins sein will in der Richtung, daß das Menschentum nicht in der Materie, sondern im Geiste wurzelt, so zeigt uns eine genaue Betrachtung eines solchen Epos wie Kälewala, daß das Beste, was der Mensch hat, auch das Beste, was der Mensch ist, aus dem Geistig-Seelischen stammt.",
        "In diesem Sinne war es mir interessant, daß eine der Runen, der Kantelen unmittelbar, ich möchte sägen, Protest erhebt gegen eine Ausdeutung dessen, was in"
      ],
      [
        "Kalewala vorkommt, in einem materialistischen Sinn.",
        "Jenes Instru­ment, jenes harfenartige, mit dem die alten Sänger von den alten Zeiten sangen, im Bild wird es angedeutet so, wie wenn es aus Materialien der physischen Welt gebildet wäre.",
        "Die alten Runen aber protestierten da­gegen, protestierten im geisteswissenschaftlichen Sinne, möchte man sagen, dagegen, daß aus Naturprodukten, welche die Sinne schauen können, das Saiteninstrument für Wäinämöinen zusammengefügt war.",
        "In Wahrheit, so sagt die alte Rune, stammt aus Geistig-Seelischem das Instrument, worauf der Mensch die Weisen spielt, die ihm unmittelbar aus der geistigen Welt hereinkommen.",
        "In diesem Sinn ist die alte Rune ganz im geisteswissenschaftlichen Sinn zu deuten, ein lebendiger Pro­test gegen die Ausdeutung dessen, wozu der Mensch imstande ist im materialistischen Sinn, eine Hindeutung darauf, daß das, was der Mensch besitzt, was sein Wesen ist und was nur symbolisch ausgedrückt wird in einem solchen Instrument, wie jenes, welches dem Wäinämöinen zugeschrieben wird, daß ein solches Instrument aus dem Geist heraus und damit überhaupt das ganze Wesen des Menschen aus dem Geist heraus stammt.",
        "Wie ein Motto für die Gesinnung der Geisteswissen­schaft kann sie gelten, die alte finnische Volksrune, die uns in die deut­sche Sprache in folgender Weise übersetzt ist, und in welcher ich den Grundton, die Grundnuance dessen, was der Vortrag erläutern wollte an dem Wesen der Volksepen, zusammenfassen kann:"
      ],
      [
        "Falsches sagen die gewißlich"
      ],
      [
        "Und befinden sich im Irrtum,"
      ],
      [
        "Die da glauben, Wäinämöinen"
      ],
      [
        "Hab gezimmert die Kantele,"
      ],
      [
        "Unsere schönen Saitenspiele,"
      ],
      [
        "Aus den Kinnbacken des Hechtes,"
      ],
      [
        "Und daß Saiten er gesponnen"
      ],
      [
        "Aus dem Schweif des Hiisi-Rosses."
      ],
      [
        "Sie ist aus der Not gezimmert,"
      ],
      [
        "Kummer band dann ihre Teile,"
      ],
      [
        "Bittere Sehnsuchtstränen spannen"
      ],
      [
        "Und die Leiden ihre Saiten."
      ],
      [
        "So ist alles Wesen nicht aus Materiellem, sondern aus Geistig-Seelischem herausgeboren, so diese alte Volksrune, so wiederum die Geisteswissen­schaft, welche sich hineinstellen will in den lebendigen Kulturprozeß unserer Zeit."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ERSTER VORTRAG Dornach, 9. November 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Ich möchte durch eine in unsere Vorträge eingeschobene Betrachtung dazu beitragen, daß wir das schon Gesagte, mehr oder weniger mit der Ausgestaltung unseres Baues zusammenhängend Gesagte, noch tiefer verstehen lernen und manches noch in Zukunft hinzufügen können, was besser wird verstanden werden können durch eine solche episo­dische Betrachtung, wie es die heutige sein soll.",
      "Wir wissen, daß des Menschen Seelenwesen gegliedert uns erscheint in die Empfindungsseele, die Verstandes- oder Gemütsseele und die Be­wußtseinsseele. Wir wissen, daß in diesen drei Seelengliedern arbeitet, so wie es in der «Theosophie» beschrieben ist, das Ich des Menschen.",
      "Nun geht in der menschlichen Natur wirklich viel vor sich, das nicht so, wie es vor sich geht, ins Bewußtsein hereindringt. Gerade die geistes­wissenschaftliche Erkenntnis kann allmählich dazu führen, daß vieles, was in den Tiefen der menschlichen Seele liegt, beleuchtet wird von dem Lichte des Bewußtseins.",
      "Aber wenn so die Menschenseele hinlebt, so beleuchtet sie gleichsam nur einen kleinen Teil des gesamten Seelen­horizontes, und unter diesem Horizont liegt vieles, was tiefe, tiefe Be­deutung für die Seele hat, aber nicht für das gewöhnliche Leben bewußt wird, was gewissermaßen viel bedeutsamer ist für die menschliche See­lengestaltung als das, was bewußt ist. Vor allen Dingen wollen wir jetzt unseren Blick werfen auf etwas, was gewöhnlich nicht zum Bewußtsein kommt.",
      "Für den heutigen Menschen ist es sogar recht heilsam, daß das nicht zum Bewußtsein kommt. Wir werden aber später sehen, daß das nicht immer für alle Menschen so war. Wenn nur ein wenig sich das gewöhnliche Alltägsbewußtsein des Menschen vertiefen würde und würde heräufhölen können, was, ich möchte sagen, nur um einen Grad unbewußter ist als das gewöhnliche Bewußtsein, dann würde die Men­schenseele sehr bald dahinterkömmen, daß sie die Dreiheit ist, von der gesprochen worden ist, daß sie wirklich nicht so ohne weiteres eine Ein­heit ist, söndern eine Dreiheit.",
      "Ich habe angedeutet in der Schrift «Wie erlangt män Erkenntnisse höherer Welten?», daß, wenn der Mensch anfängt",
      "vorzurücken gegen die geistigen Welten zu, er gleichsam ausein­anderfällt in eine Dreiheit. Und sobald man nur, wie gesagt, ein wenig hereinblickt in den gleichsam zugedeckten Teil des Bewußtseins, so merkt man sehr bald, daß diese Dreiheit von Empfindungsseele, Ver­standes- oder Gemütsseele und Bewußtseinsseele da ist. Unter der Schwelle des Bewußtseins - und zwar gar nicht besonders tief für den gegenwärtigen Menschen - ist wirklich eine Art von Seelenreich, das durchsetzt wird nicht von einer Einheit, sondern von einer Art Drei­heit, von dem Hereinstrahlen dieser Dreiheit, so daß in dem Augen­blick, wo der Mensch zurückdrängt das, was er im Grunde genommen erst so völlig seit der zweiten Hälfte der vierten nachatlantischen Pe­riode erlangt hat und so ganz klar erst nach dem Beginn des fünften nachatlantischen Zeitraums, sobald also der Mensch das zurückdrängt, kann er genau zwischen drei Welten oder Gebieten in seiner Seele unter­scheiden. Das eine Gebiet ist ein solches, das mehr inspiriert wird, in welches traumhafte, träumerische Inspirationen hineinkommen. Das zweite Gebiet ist das, durch welches der Mensch gleichsam sich selbst durchseelt, auferbaut in den physischen Teilen. Und das dritte Gebiet ist das, wo er das Bewußtsein von der Welt erhält.",
      "Das erste Gebiet also ist das, in welches die Inspirationen herein-dringen, traumhafte Inspirationen, welche die Seele ausfüllen, was an die Empfindungsseele gebunden ist. Ein zweites Gebiet, wo die Seele gleichsam durch ihre eigenen inneren Gestaltungen und Bildungen ihren Leib auferbaut, ist gebunden an die Verstandes- oder Gemütsseele. Das ist der innere Werkmeister, der Baumeister, wir könnten auch sagen der Schmied des physischen Leibes. Und das dritte, die Vermittlung des äu­ßeren Erkennens, das in Zusammenhang tritt mit der Welt, die an die Sinne gebunden ist, überhaupt mit der physischen Welt zusammen­hängt, ist an die Bewußtseinsseele gebunden. Wir können also sagen:",
      "zusammenhängend mit physischen Gewalten.",
      "Gleichsam eine Seelentrinität waltet auf dem Grunde der Seele des Menschen, und dieser Trinität steht gegenüber das Walten und Wirken desjenigen, was zur Einheit strebt. Ich will es dadurch andeuten, daß ich gleichsam ein besonderes Seelenreich dem andern hier gegenüber­stelle (siehe folgende Zeichnung).",
      "Dieses Seehenreich wirkt in gewisser Beziehung ganz in sich einheitlich. Es wirkt aber naturhaft einheitlich gleichsam dasjenige, was die Seele ihrem Temperamente, ihrem Charakter nach ist, was tief unten in der Seele ruht, aber als einheitliche Seele. Das möchte ich mit diesem be­zeichnen: Einheitsseele, im Gegensatz zu der Dreiheit.",
      "# Bild s. 42",
      "So, wie einmal unsere Seele jetzt ist, kann diese Einheitsseele aus einem gewissen dumpfen Leben nicht herauskommen, wenn sie nicht gleichsam überhellt, überheuchtet wird. Und in unserer Zeit geht das Überleuchten immer aus in irgendwelcher Form von dem Mysterium von Golgätha, so daß ich das, was in irgendwelcher Weise hereinstrahlt",
      "in die Einheitsseele, symbolisch Ihnen hinzeichne: irgendeine Form, in der das Mysterium von Golgatha hereinstrahlt in die Einheitsseele.",
      "Nun haben wir wirklich schon im Laufe der Jahre vieles, vieles auf­gewendet, um nach und nach uns eine Vorstellung davon zu verschaf­fen, wie unendlich weit all das ist, was mit dem Mysterium von Gol­gatha zusammenhängt. Sie können sich daher denken, daß, wenn so das Mysterium von Golgatha in irgendeiner Form in die Menschenseele",
      "# Bild s. 43",
      "hereinstrählt, das immer nur eine gewisse Stufe, ein gewisser Grad des Mysteriums von Golgatha ist. Aber wir stellen uns vor, daß, weil die Einheitsseele etwas gleichsam dumpf Brütendes ist, aber das für unsere Zeit besonders Wertvolle enthält, so muß dieses Einheitliche in irgend­einer Form von dem Mysterium von Golgatha durchstrahlt werden.",
      "Nun ragt in jede Seele dasjenige hinein, was von den verschiedenen Inspirations- und Initiationszentren der Welt ausgeht, und das gehört auch zu den unterbewußten Einflüssen in der Menschenseele. Sehen Sie, die Wirkung des Mysteriums von Golgätha ist eine umfassende, eine universelle, aber der Mensch, die Menschenseele kann dieses Mysterium von Golgatha nur in einer bestimmten Weise aufnehmen. Das Initia­tionszentrum, welches ganz besonders in das Innere der Seele herein-wirkt, damit das Innere der Seele richtig vorbereitet wird, sich von dem Mysterium von Golgatha ganz besonders durchstrahlen zu lassen, habe ich früher öfter so besprochen, daß ich gesagt habe: Es steht immer vor diesem Initlationszentrum der Eingeweihte Skythianos. - Nehmen wir also an, die Seele wäre vorbereitet worden in der Einheitsseele für das, was vom Mysterium von Golgathä kommt, bereit, es aufzunehmen durch das, was in jeder Seele unbewußt, von Skythianos her, hinein wirkt.",
      "Da haben wir gleichsam die Seele des Menschen gespalten in zwei Reiche: in das eine Reich, das eine Dreigliedrigkeit ist, und in ein an­deres Reich, welches eine Einheit ist: in ein mehr seelisches Reich und in ein mehr näturhaftes, temperamentmäßig brütendes Reich, möchte ich sagen, in ein Reich, das mehr aufnimmt in seine Naturgrundlage die Kräfte des Mysteriums von Golgatha auf der einen Seite und auf der ändern Seite die Einflüsse des Skythianos.",
      "Nun kann diese Einheit mit der Dreiheit nicht ohne weiteres sich verbinden, das ginge nicht, und deshalb ist es auch so, daß diese Drei­heit bei den gegenwärtigen Menschen unter der Schwelle des Bewußt­seins bleibt. Es wird diese Dreiheit gleichsam übertäubt; es muß das Bewußtsein davon ausgelöscht werden. Wenn die Seele wirklich her-unterkommen könnte zu der Dreiheit, würde sie sich sogleich als Drei­heit, nicht als eins, fühlen. Sie würde sägen: Da ist etwas in mir, das inspiriert mich, etwas, das baut mich auf, das schmiedet mich zusam­men, und etwas, das steht mit der Außenwelt im Zusammenhang. -Aber diese Dreiheit muß gleichsam durch etwas ausgelöscht, über­schattet werden, was seelisch den Menschen dahin bringt, daß er sägt:",
      "Ich unterscheide nicht die Drei. - Es muß also etwas hereinstrahlen in die Drei, das macht, daß die Seele die Drei nicht in sich empfindet,",
      "diese Drei auslöscht, gleichsam wie Nebelgebilde zueinander sein läßt.",
      "Sehen Sie, dann kann die Verbindung bestehen zwischen dem, was in der Seele als Einheit leben soll, und dem, was als Dreiheit in der Seele ist, wenn eine Kommunikation, eine Art Austausch da ist, gleichsam eine Art Seelenstamm, der zur ausgelöschten Dreiheit hinführt und der",
      "# Bild s. 45",
      "ausgeht von dem, was Einheit ist, aber von zwei Seiten her durchstrahlt wird, gleichsam durchleuchtet wird dazu, daß es nicht nur eine dumpfe, gleichmäßige charakter- und temperamentgemäße Natureinheit ist, sondern daß es einheitlich durchleuchtet wird von dem, was der Mensch sein soll: von dem Bewußtsein der Menschenseele in ihrem Zusammen­hang mit dem göttlich-geistigen Sein. Eigentlich habe ich da etwas aufgezeichnet,",
      "was auf dem Grunde jeder Menschenseele ruht. Keine ein­zige Menschenseele kann in unserer Zeit ohne das sein, daß alle diese Dinge in ihr vorhanden sind.",
      "Aber nun stellen Sie sich das Folgende vor. Ich habe wiederholt gerade hier betont, um zu zeigen, was unser Bau sein soll, daß dasjenige, was in der Menschenseele lebt, äußerlich auch zur Darstellung kommt, sich auslebt sozusagen in der äußeren Evolution der Erde.",
      "Wenn es ein solches Gebiet in der Menschenseele gibt, das wirklich eine Art von Dreiheit darstellt, das bei den heutigen Menschen gleichsam schon überzogen ist von dem gewöhnlichen Bewußtsein, so müssen wir ein­mal ein Evolutionsstadium finden, wo uns das äußerlich entgegentritt, daß die Seele wirklich sich als eine Dreiheit empfindet, gleichsam aus­einandergelegt in drei Seelenglieder. Mit andern Worten, es muß ein Volk einmal dagewesen sein, das diese drei Seelenglieder auseinander-gelegt empfand und so empfand, daß im Grunde genommen die Einheit viel geringer empfunden wurde in der Seele als die Dreiheit, da die Dreiheit noch in Verbindung gedacht wurde mit dem Kosmos.",
      "Dieses Volk war da in Europa und hat ein bedeutendes Kulturdenkmäl hinter­lassen, von dem ich schon einmal gesprochen habe. Dieses Volk, das einmal, und zwar an der Stelle in Europa, wo es sein mußte, diese Drei­heit empfand in der Seele, ist das finnische Volk.",
      "Und der Ausdruck dieser Kulturstufe ist niedergelegt in Kalewala. In dem, was in Kale­wala dargestellt ist, ist das deutliche Bewußtsein von der Dreiheit der Seele vorhanden, so daß von den alten Sehern, deren Sehertum Käle­wala zugrunde liegt, empfunden wurde: Da ist etwas Inspirierendes in der Welt, mit dem steht ein Glied meiner Seele in Verbindung, meine Empfindungsseele.",
      "Sie tendiert dahin, deren Kräfte gehen dahin, sie bekommt von da die Impulse. - Gleichsam ein Menschlich-Göttliches oder Menschlich-Heroisches empfand dieses Volk oder empfanden diese alten Seher als das Inspirierende der Empfindungsseele. Und sie nann­ten das Wäinämöinen.",
      "Das ist nichts anderes als das im Kosmos Inspi­rierende der Empfindungsseele. Alle die Schicksale, die in Kalewäla als die Schicksale von Wäinämöinen geschildert werden, drücken aus, daß dieses Bewußtsein einmal vorhanden war bei einem Volke, welches eine große Ausbreitung in dem Nordosten des europäischen Gebietes hätte,",
      "und das die drei Seelenglieder getrennt empfand und die Empfindungs­seele inspiriert von Wäinämöinen.",
      "Ebenso hat dieses Volk, haben diese alten Seher empfunden, daß die Verstandes- oder Gemütsseele gleichsam ein Glied extra in der Seele ist, das seine Impulse empfängt zum Schmieden, haben empfunden das, was schmiedet in der menschlichen Seele, was sie aufbaut, von einer andern elementärischen, heroischen Wesenheit empfängt, von Ilma­rinen. Wie also Wäinämöinen entspricht der Empfindungsseele, so ent­spricht in Kalewala Ilmarinen der Verständes- oder Gemütsseele. Wenn Sie den Vortrag über Kalewala nachlesen, so können Sie das alles darin finden.",
      "Und ebenso empfand dieses Volk - das muß festgehalten werden -, daß dazumal die Bewußtseinsseele empfunden wurde wie das, was den Menschen erst zu einem Eroberer auf dem physischen Plan macht, empfanden diese alten Seher in Lemminkäinen ein Wesen, das mit den Gewalten des physischen Planes zusammenhängt, ein elementares, hero­isches Wesen in dem Inspirator der Bewußtseinsseele. So stammen diese drei, man möchte sagen, Heldenfiguren, wenn man in Analogie mit andern Epen spricht, von dem alten finnischen Volk her, inspirierend die Dreigliedrigkeit der Seele.",
      "Das Wunderbare ist der Zusammenhang zwischen Ilmarinen und demjenigen, was da geschmiedet wird. Ich deutete es schon an. Es wird geschmiedet aus den Naturelementen heraus der Mensch selber. Dieses Wesen, das aus allen Naturatomen zusammengeschmiedet wird, pul­verisiert und zusammengeschmiedet wird, ist in einem großartigen Tableau in dem Schmieden des Sampo in Kalewäla dargestellt. Und daß dieses Bilden des Menschen aus diesen drei Seelengliedern heraus einmal geschehen ist, dann gleichsam wie in ein Prälaya gehen muß und dann wiederum hervorkommt, ist auch dargestellt in Kalewala: wie der Sampo verlorengeht und wiedergefunden wird, gleichsam wie wieder­gefunden wird das, über das sich zunächst Bewußtseinsdunkelheit ver­breitet.",
      "Und nun stellen wir uns vor, daß gegen den Süden zu, gegen den Südosten, können wir sägen, ein anderes Volk gegenübersteht, das die­jenigen Seeleneigenschaften zunächst in älter Zeit ausgebildet hat, von",
      "denen ich gesprochen habe, das Einheitsmäßige in der Seele, das, was das Einheitsmäßige zum Ausdruck bringt in den Charakter-, den Ge­mutseigenschaften, in den Temperamentseigenschaften. Dieses Volk ist ein slawisches Volk, während das Volk, das ihm gegenübersteht, das finnische Volk ist. Dieses slawische Volk bekommt seine Einflüsse von Skythianos, der auch eine Zeitlang in alten Zeiten gelebt hat vom alten Skythenvolk umgeben. Es ist durchaus nicht notwendig, daß um ein Initiationszentrum herum auch ein hochentwickeltes Volk lebe, son­dern es muß im Verlaufe der Entwickelung das geschehen, was not­wendig ist. Und das Hereindringen einer bestimmten Form des Myste­riums von Golgätha ist das Hereindringen der griechisch-byzantinischen Kultur in das Slawentum. Was ich Ihnen hier als ein Zentrum der grie­chisch-byzantinischen Kultur aufgezeichnet habe, das können Sie ruhig, wenn Sie wollen, als Konstantinopel auffassen auf der Karte von Eu­ropa, denn das ist im Grunde genommen Konstantinopel.",
      "So haben wir also jetzt Seelen, die sich mit einem slawischen Grund-typ imprägniert finden. Es sind Seelen, die auf der einen Seite ver­bunden sind mit dem, was zu einem Einheitswesen durch das Myste­rium von Golgatha führen kann, was in Einheitsseelen zum Christen­tum vorbereiten kann, die auf der andern Seite das Mysterium von Gölgatha in einer ganz bestimmten Form empfangen, etwas wie die Inspiration, die Influenzierung durch das Mysterium von Golgatha, wie sie von der byzantinisch-griechischen Kultur ausgegangen ist.",
      "Nun muß aber noch etwas anderes, von einem gewissen Punkte her gleichsam, kommen. Was im finnischen Volke da war als die Scheidung, die Trennung in die drei Glieder, deren Bodensatz so großartig in Kale­wälä enthalten ist, das muß ausgelöscht werden. Das kann nur ausge­löscht werden, wenn ein Einfluß von außen kommt, kann nur aus­gelöscht werden dadurch, daß gleichsam ein Volk oder ein Völksteil da vördrängt, der von vornherein dazu veranlagt ist, nicht die Dreiheit, sondern die Einheit in der Seele zu empfinden, nicht die Einheit, die man bekommt von dem Mysterium von Golgatha aus, sondern die Ein­heit, die man gleichsam von Natur aus hat. Wenn man das finnische Volk betrachtet, so findet man es besonders veranlagt, das Bewußtsein der Dreiheit auszubilden. Und man kann nicht bedeutsamer diese Dreiheit",
      "# Bild s. 49",
      "in ihrem Verhältnis zum Kosmos ausdrücken, als das in Kalewala geschehen ist. Aber dann mußte das im Norden übertüncht, übernebelt werden von dem, was gleichsam auslöscht das Bewußtsein von dieser Dreiheit. Es drängte da ein Stamm herunter, der in einer naturhaften Weise das in seiner Seele trug, was damals als das Einheitsstreben da war, was in einer ganz andern Weise, auf einer ganz andern Stufe im Goetheschen «Faust», aber auch überhaupt in Faust zum Ausdruck ge­kommen ist, etwas, das nicht weiß von der Dreigliedrigkeit, das nach der Einheit des Ich strebt. Hier noch auf einer primitiven Stufe wirkt das auslöschend auf die drei Seelenglieder.",
      "Nun ist aber das finnische Volk ein solches gewesen, welches noch naturhaft empfand, sonst hätte es nicht die drei Seelenglieder empfun­den. Das, was dahinflutet, auslöschend die Dreiheit, dieses Hin flutende, Hineindrängende empfand man als ein r r r, und weil man es empfand als etwas, was, man möchte sägen, in okkulter Spräche am besten aus­gedrückt ist in den Buchstaben, in dem Laute u u o, so daß man sägen möchte: Es kommt heran, man muß eigentlich Scheu davor haben, so haucht es hin in dem rruuo und setzt sich fest, was immer durch das Tau, t, empfunden wird, wenn das in die menschliche Seele hinein­dringt. Geradeso wie das Hineindringen in die menschliche Seele beim alten Jehova durch das s, durch das hebräische «Shin», ausgedrückt ist, so wird überhaupt dieses Eindringen in die Seele, das Durchdringende durch den s-Laut ausgedrückt. All das hängt zusammen mit dem, was in die Seele eindringt und festhält in der Seele, all das drängt zum i hin, dessen Bedeutung ja bekannt ist, im finnischen Volk das, was mit dem rruu zusammenhängt. Daher empfand es dieses rutsi, ruotsi, und daher nannte es die Völker, die herunterdrängen da, die Rutsi, Ruotsi. Und diesen Namen haben allmählich die Slawen aufgenommen, und weil sie sich verbunden haben mit dem von oben nach unten Dringenden, was die Finnen so nannten, nannten sie sich selbst Rutsi, was später zu dem Namen Russen wurde.",
      "Sie sehen also, das alles mußte sein, was in der Geschichte äußer­lich erzählt wird, daß diese hier unten sitzenden Völker gerufen haben die Warägerstämme, die eigentlich normannisch-germanische Stämme waren, die sich verbinden mußten mit den slawischen Stämmen. Dem liegt etwas zugrunde, was sein mußte, durch die Einrichtung der Men­schenseele notwendig sein mußte. Und so kam denn das zustande, was dann später im Osten von Europa als das Element des Russischen in das europäische Volkstum eintrat. In dem Element des Russischen lebt also all das wirklich drinnen, von dem ich gesprochen habe. Es lebt vor allen Dingen darinnen jenes normannisch-germanische Element, lebt sogar in dem Namen drinnen, von dem der Name Russe gekommen ist, denn der ist auf dem Wege gekommen, den ich angedeutet habe.",
      "In tiefsinniger Weise wird in Kalewala ausgedrückt, daß die Größe des finnischen Volkes darauf beruht, daß es eigentlich vorbereitet in",
      "der Dreiheit die Einheit, vorbereitet durch Auslöschung der Dreiheit das Entgegennehmen derjenigen Einheit, die nun nicht mehr nur menschliche Einheit ist, sondern die göttliche Einheit ist. in welcher lebt der göttliche Held des Mysteriums von Golgatha.",
      "Damit eine Gruppe von Menschen aufnehmen kann dasjenige, was an sie herankommt, muß sie erst vorbereitet werden. Wir bekommen auf diese Weise einen Eindruck davon, was alles innerlich geschehen muß, damit das in der Entwickelung sich vollziehen kann, was einem äußerlich entgegentritt. Ich sagte, in Kalewala wird in großartiger Weise ausgedrückt, daß das finnische Volk diese Vorbereitung zu lie­fern hatte, dadurch, daß am Schlusse in eigentümlicher Weise das Mysterium von Golgätha in Kalewala eingeführt wird. Christus tritt am Schlusse von Kalewala auf, aber indem er seinen Impuls in das finnische Leben wirft, geht Wäinämöinen aus dem Lande fort, was aus­drückt, daß das ursprünglich Große, das Bedeutungsvolle, das durch das finnische Element in Europa hereingekommen ist, ein Vorberei­tungsstadium für das Christentum ist und das Christentum wie eine Kunde, wie eine Botschaft von außen empfängt.",
      "Wie wir beim einzelnen Menschen sehen, daß er in außerordentlich komplizierter Weise gleichsam zubereitet werden muß, damit dann seine Seele das finde von den verschiedensten Seiten her, was sie braucht, um in einer bestimmten Inkarnation zu leben, so ist es auch mit den Völ­kern. Ein Volk ist nicht etwas ganz so Einheitliches, Homogenes, son­dern ein Volk ist etwas, worin viel zusammenfließt. Das Volk, das da im Osten drüben lebt, in ihm ist all das zusammengeflossen. Und all dasjenige, könnte man sagen, was innerlich spirituell ist, ist äußerlich wenn auch äußerlich in leichter Weise nur - angedeutet. Ich habe ge­sagt, bei diesem Volk muß ein Seelenstamm sein, der von unten nach oben, respektive auch von oben nach unten führt, wenn es ein verbin­dender Seelenstamm ist. Das war vorhanden in einer mächtigen Straße, welche vom Schwarzen Meer zum Finnischen Meerbusen ging, und auf der ein Austausch stattfand zwischen dem griechisch-byzantinischen Element und dem, was ein Näturelement war der Rutsi.",
      "Der Mensch muß im Laufe seiner verschiedenen Inkarnationen ver­schiedenes durchmachen. Eine Inkarnation muß sich immer auf die",
      "andere aufbauen. Das kann der Mensch nur dadurch, daß gleichsam in die Substanz, in das Material, aus dem die einzelnen Völker und ihre Angehörigen gebildet werden, wirklich die Kräfte zusammenfließen, durch welche später die Menschenevolution sich vollziehen kann.",
      "Es muß eine Menschenseele einmal in ihren Inkarnationen solch eine Leib­lichkeit finden, die zusammengeflossen ist aus den Kräften, die ich hier dargestellt habe. Und was man so einfach sagt, ein Mensch wird als Russe geboren, das hat seine tiefe, seine kolossal tiefe Bedeutung.",
      "Ein Mensch wird als Russe geboren, heißt: er ist auf dem Wege durch die verschiedenen Inkarnationen dabei angelangt, innerhalb seiner Erden-laufbahn das zu erleben, was man nur dadurch erleben kann, daß man in einer Körperlichkeit durchläuft ein Leben zwischen Geburt und Tod, die auf solche Weise zusammengetragen ist. Würde man nicht in einem solchen Körper das durchleben, so würde einem etwas fehlen in dem, was man von Inkarnation zu Inkarnation sich erwirbt.",
      "Törichte Men­schen - ich sage das, ohne daß damit irgendeine Empfindungsnuance verbunden ist, sondern ich sage das als Terminus technicus - haben immer wieder und wiederum von dem Sprichwort gesprochen: Die Welt begreift man in ihrer Wahrheit am besten, wenn sie einem in ihrer Einfachheit erscheint. - Das ist nicht wahr, das ist nur bequem. Tiefe Geister haben es immer ausgesprochen, zum letzten Mal am eindring­lichsten wohl Ralph Waldo Emerson, daß man zur Wahrheit der Tat­sachen erst eindringt, wenn man sie in ihrer ganzen Kompliziertheit erkennt.",
      "Es ist nicht so einfach, das, was in der Welt lebt und was mit der ganzen Weltenevolution zusammenhängt.",
      "Und so wie es auf der östlichen Hälfte der europäischen Halbinsel ist, daß die Seelen zubereitet werden, um etwas Besonderes zu erleben, so ist es für alle andern Fälle der Erdenoberfläche, so sind die einzelnen Volkscharaktere in einer komplizierten Weise zubereitet. Nun erinnern Sie sich vor allen Dingen an eines, das wir genügend im Verlaufe un­serer geisteswissenschäftlichen Betrachtungen kennengelernt haben.",
      "Der Mensch ist gewissermaßen, wenn er durch die Pforte des Todes gegangen ist, dadurch, daß er zurückblickt auf sein letztes Erdenleben, abhängig von dem, was er in seinem letzten Erdenleben erlebt hat. Wir wissen, daß jahrelang hineinspielen in das Leben nach dem Tode die",
      "Zusammenhänge mit dem früheren Erdenleben. Das muß aber so sein. Der Mensch muß durch eine physische Inkarnation hindurchgehen, damit er in dieser Zeit zwischen dem Tode und einer neuen Geburt bestimmte Erinnerungen an diese vorhergehende Inkarnation hat, be­stimmte Impulse aus dieser vorhergehenden Inkarnation hereinreichen.",
      "Dadurch, daß er ein ganz bestimmtes Menschenwesen mit einem be­stimmten Organismus war, der durch die Erdenverhältnisse bestimm­ten Einflüssen unterworfen wär, wirken auch noch gewissermaßen die Eindrücke nach dem Tode, die erinnerungsmäßig zurückgehen. Diese werden dadurch influenziert, beeinflußt, sie bekommen eine gewisse Schattierung.",
      "Das ist die Schattierung, welche eine Seele dadurch emp­fängt, daß sie durch eine bestimmte Nationalität hindurchgegangen ist, die sie aus einer gewissen Nationalität heraus bekommt. Das wird immer mehr und mehr abgestreift, je mehr das Nationale in das Inter­nationale übergeht.",
      "Aber heute ist das noch in hohem Maße vorhanden, sonst hätten die heutigen Ereignisse nicht eintreten können. Die Men­schen blicken in gewissem Maße noch zurück auf dasjenige, was sie durch ihren Organismus - insofern dieser national bestimmt ist - im vorhergehenden Leben zwischen Geburt und Tod erlebt haben.",
      "Nun werden die Seelen, die auf die heute beschriebene Weise durch Leiber hindurchgehen, die gerade auf diese bestimmte Art zubereitet worden sind, in einer ganz bestimmten Art präpariert auf das Leben, welches sie antreten, nachdem sie durch die Todespforte gegangen sind. Die Individualität wird natürlich nicht beeinflußt, nur das, was gleichsam wie die Kleider, die Hüllen der eigentlichen Individualität ist.",
      "Aber diese Kleider oder Hüllen, mit denen die Nationalität zusammenhängt, geben da noch etwas, was die Seele auch nach dem Tode hat, von dem sie weiß, das hat zu deinem Durchgänge durch das Erdenleben gehört.",
      "Wenn nun die Seele durch einen Leib durchgegangen ist, der so zu­bereitet worden ist - exoterisch würde man sagen, die durch einen russischen Leib in einer Inkarnation durchgegangen ist -, so hat sie selbstverständlich die Nuancierung des äußeren Hüllenhäften, das nach dem Tode zu einer Vorstellung wird, die man von sich hat, wie man sonst Vorstellungen von sich hat. In das hat sie aufgenommen alles das, was hier (siehe Zeichnung S.49) auf diese Weise ausgedrückt ist, und",
      "wenn man aussprechen will, was die Seele innerlich dadurch durch­macht, daß sie einen so zusammengesetzten Leib hat, so kann man fol­gendes sagen. Nicht wahr, wir wissen aus den bisherigen Betrachtungen, daß sich das Bewußtsein in einer gewissen Weise verändert nach dem Tode, es erlangt einen höheren Grad, wird deutlicher, intensiver nach dem Tode, als es in einem physischen Leib ist. Das durchgemacht zu haben, was vorher gemeint ist, bereitet die Seele vor, in besonders in­time Beziehung nach dem Tode zu denjenigen Wesen zu kommen, die wie besondere Schutzgeister über den eigentlichen menschlichen Indi­vidualitäten leben und in die nächst höhere Hierarchie gehören, in die Hierarchie der Angeloi. In dem Leben nach dem Tode, das bei einer Seele auf eine russische Inkarnation folgt, ist sie gleichsam veranlagt, sich zu identifizieren im Bewußtsein mit ihrem Angelos, die geistige Welt gleichsam anzusehen, um einen groben Ausdruck zu gebrauchen, mit den Augen des Angelos.",
      "Der Mensch strebt zum höheren Selbst hinauf. Dieses höhere Selbst lebt sich in der verschiedensten Weise aus. Lesen Sie den letzten Münch­ner Zyklus über «Die Geheimnisse der Schwelle». Da haben Sie aus­einandergesetzt, wie das Bewußtsein etwas anderes wird, gleichsam sich die Seele mit dem Angelos durchdringt. Sie muß sich damit durch­dringen und bereitet sich zu dem Durchdringen mit dem Angelos da­durch vor, indem sie sich hineinlebt durch die Pforte des Todes in die geistige Welt nach dem Leben in einem russischen Leibe, der so zu­bereitet worden ist, wie wir es beschrieben haben. So daß wir sagen können: Derjenige, der durch einen russischen Leib gegangen ist, fühlt eigentlich alles nuänciert nach dem Tode dadurch, daß er besonders durchsetzt ist in seinem ganzen Wesen von einem Angelos, von dem alle Menschen beschützenden Genius der nächst höheren Hierarchie.",
      "Aber bei den Völkern der westlichen Kultur ist es so, daß man weniger stark sich imprägniert, weniger stark sich durchdringt nach dem Tode mit dem Wesen des Angelos. Geht man durch eine westliche Inkarnation, so erfährt man nach dem Tode eher das Folgende: Ich empfinde noch so, wie ich sonst auch empfunden habe, ich schaue die Welt noch an, wie ich sie sonst angeschaut habe. - Man empfindet es wie eine besondere Kunst, mit seinem Angelos zusammenzuwachsen.",
      "Für den Angehörigen des russischen Volkes ist es etwas Naturgemäßes, immer mit seinem Angelos zusammen zu sein. Die Seele geht auf dem Wege durch die Inkarnationen durch alle möglichen Nationalitäten hindurch und muß auch durch diese Inkarnation gehen, wo sie den Im­puls erhält, mehr in dem Angelos aufzugehen, mit dem Angelos zu­sammenzuwächsen, mit seinem Geistesauge zu schauen in die geistige Welt.",
      "Natürlich bezieht sich das mehr als auf andere Zeiten zwischen dem Tode und der neuen Geburt auf die Zeit unmittelbar nach dem Tode, die nächsten Jahre oder einundeinhalb bis zwei Jahrzehnte, denn in der Hauptzeit vor und nach der «Mitternacht», von der ich schon ge­sprochen habe, streift die Seele solche Dinge ab. Es bezieht sich das also auf die Zeit, in welcher der Mensch noch influenziert ist von dem, was er im physischen Leibe erlebt hat, wo das noch nachwirkt.",
      "Und nun wenden wir, nachdem wir dies auseinandergesetzt haben, einmal unseren Blick hin auf die geistige Welt, gleichsam auf das Innere der Welt, in der wir drinnen leben, indem wir zu unserer Betrachtung hinzunehmen, daß es nur dem beschränkten Menschensinne entspricht, wenn er glaubt, er ist nur von physischen Menschen umgeben. Er ist immer auch von den Verstorbenen umgeben, von denjenigen, die in der geistigen Welt leben. So haben wir in unserer Umgebung gestorbene Seelen, die durch physische, russische Leiber gegangen sind, die eine große Neigung haben, mehr als Angelos, möchte ich sagen, in ihrer jetzigen Seelenverfassung zu leben denn als Mensch.",
      "Nach einer solchen Inkärnation tritt noch das besonders Eigentüm­liche auf, daß der Ätherleib ganz besonders schnell sich in der um-liegenden Ätherwelt auflöst, während bei den westlichen Völkern der Ätherleib mehr kompakt ist, sich mehr zusammenhält, schwerer sich auflöst in der umgebenden Ätherwelt. Nun lehen wir aber bereits in einem Zeitpunkt, namentlich seit dem letzten Drittel des 19.Jahrhun-derts, wie ich schon oft angedeutet habe, wo in der geistigen Welt die Herrschaft durch Michael angetreten ist, nachdem vorher Gabriel re­gierte.Wir leben jetzt in einer Zeit,wo diese Verhältnisse ganz besonders stark in der geistigen Welt hervortreten, ganz besonders das Geschilderte wirkt in der geistigen Welt. Denn es obliegt unserer Zeit, das große Ereignis",
      "vorzubereiten, das ich schön in dem ersten Mysteriendräma «Die Pforte der Einweihung» angedeutet habe, das Erscheinen des Christus in einer geistigen Gestalt vor dem Menschen. Dieses Ereignis der Er­scheinung des Christus, so wie es die Theödora angedeutet hat, kann nur herbeigeführt werden, wenn sich die Herrschaft des Michael immer mehr und mehr ausbreitet.",
      "Noch ist das ein Prozeß in der geistigen Welt Gleichsam kämpft auf dem Plane, der angrenzt an unsere Welt, Michael für das Herannahen des Christus. Er braucht seine Scharen, seine Kämpfer dazu. Nun werden wichtige Kämpfer ihm geliefert, wichtige Scharen aus denjenigen Seelen, die in der jetzigen Inkarnation durch einen russischen Leib gegangen sind.",
      "So daß wir geradezu in der geistigen Welt auf eine Art von Eroberungszug des Michael für das Herannahen des Christus blicken können. Dazu rekrutiert er sich eine Schar, eine Reihe von wichtigen Kämpfern aus den Seelen, die durch russische Leiber gegangen sind, weil sie in sich veranlagt sind, sich zu identifizieren mit ihrem Angelos.",
      "Dadurch werden sie ganz besonders geeignet, die Kräfte herbeizuführen, um in Reinheit das Bild zu geben, durch das der Christus erscheinen soll. Damit er nicht erscheint in fal­scher Gestalt, in subjektiver Menschheitsimaginätion, damit er erscheint im richtigen Bilde, muß Michael den Kampf kämpfen, den ich ange­deutet habe.",
      "Er kann ihn ganz besonders durch diejenigen Seelen kämp­fen, die naturhaft in sich dieses Angelosbewußtsein tragen. Dadurch sind sie besonders präpariert. Auch dadurch, daß ihr Ätherleib sich besonders leicht auflöst, haben sie nichts in ihrem Ätherleib, was den Christus in falscher Gestalt, in fälschen Imaginätionen erscheinen ließe.",
      "Damit all das, was in der Welt geschehen soll, richtig geschehen könne, müssen verschiedene Glieder in der Weltenordnung zusammen­wirken. Es muß nun, damit das geschehen könne, was ich dargestellt habe - nehmen Sie das ganz objektiv - eine Eigentümlichkeit bekämpft werden, die mehr im Westen ist, besonders bei den Seelen, die durch eine französische Inkarnation durchgegangen sind. Diese Seelen be­kommen von ihrer Nationalität das Eigentümliche, stark ihren Äther­leib festzuhalten, eine ganz bestimmte Imaginationsgestalt im Ätherleib lange festzuhalten. Das kann nicht durch die westlichen Seelen allein",
      "bekämpft werden, sondern es muß dabei diesen westlichen Seelen, man möchte sägen, geholfen werden, es muß gearbeitet werden an der Zer­streuung dieser Ätherleiber in dem allgemeinen Weltenäther, damit nicht ein falsches Bild von der Christus-Erscheinung hervorgerufen werde. Es müssen also die Scharen zusammenwirken, die unter Michael kämpfen, müssen diejenigen Seelen bekämpfen, die durch französische Leiber hindurchgegangen sind.",
      "Das ist dasjenige, was hellseherisches Bewußtsein gerade in dem letz­ten Drittel des 19. Jahrhunderts und bis in unsere Zeit hinein als die Grundlage unserer jetzigen Evolution schauen konnte. Immer mehr und mehr entwickelte sich in der geistigen Welt, in der astralischen Welt, ein Kampf, geistig, zwischen Rußland und Frankreich - selbst­verständlich in demjenigen, was geistig zugrunde liegt -, und dieser Kampf wurde immer stärker und stärker. Kampf in der geistigen Welt bedeutet eigentlich Zusammenwirken in der physischen Welt, aber es ist das schon ein Bild des Kampfes, des Gegeneinanderwirkens, und der­jenige, der in die geistige Welt hineinschaut, hatte seit dem letzten Drittel des 19. Jahrhunderts bis in unsere Zeit hinein immer mehr und mehr ein Intensivwerden eines geistigen Kampfes zwischen Westen und Osten vor sich, über Mitteleuropa hindurch, den Kampf im Himmel, man könnte ihn schon so nennen, der darin besteht, daß immer mehr und mehr unter der Herrschaft des Michael Scharen im Osten gesam­melt worden sind, um all das, was verhindern könnte im Westen - in dem immer mehr und mehr in den Materialismus hineinwachsenden Westen - die Erscheinung des Christus, zu bekämpfen.",
      "Ja, meine lieben Freunde, wo eine hohe Kultur ist, eine so ganz aus­geprägte, zum Gipfel gekommene Kultur ist wie in Frankreich, hat die Seele bestimmte Imaginationen angenommen. Diese Imaginationen bleiben nach dem Tode, sie hindern aber, daß etwas ganz Neues kom­men kann, was durch den Christus kommen muß. Daher muß vor allem in der geistigen Welt das bekämpft werden, was aus einer vollreifen Kultur in die Seelen übergeht. Michael kann sich nicht seine Scharen aus einer vollreifen Kultur wählen, die eignen sich zu einer bestimmten Imagination; die Imaginationen müssen erst ausgelöscht werden. Daher das grandiose Bild hinter der Szene der geistigen Welt: des Kampfes",
      "des Ostens gegen den Westen, der Schar des Michael gegen die selb­ständig gewordenen Seelen des Westens.",
      "Und sehen Sie, der äußere physische Ausdruck für einen geistigen Kampf ist ein physisches Bündnis. Was sich auf dem physischen Plane verbündet, drückt damit aus, daß es sich auf dem geistigen Plane in einem Kampf befindet. Man wird zu Verbündeten auf dem physischen Plan, wenn man auf dem geistigen Plan notwendig hat, sich zu be­kämpfen. Daraus sehen Sie wiederum einmal, wie ernst wir das Wort von der Mäja und der Wahrheit nehmen müssen. Oft und oft spricht man es aus, das Wort von der Maja und der Wahrheit, aber es bleibt Theorie, denn wer in die geistige Welt hereinschaut und dort schaut, was der physischen Welt zugrunde liegt, den überkommt schon das Gefühl ungeheuerlichster Erschütterung, wenn er im Ernste von der Mäja zur Wahrheit vordringt und hinter dem, was in der Maja lebt, die Wahrheit findet. Die Wahrheit muß oftmals mit ganz andern Worten ausgedrückt werden als auf dem physischen Plan.",
      "Was auf dem physischen Plan Bündnis heißt, heißt auf dem geistigen Plan oftmals Krieg. Natürlich darf man nun keine falschen Konstruk­tionen machen, indem man das, was man auf dem physischen Plan fin­det, in seinem Gegenteil im Geiste sucht, denn es ist nicht für alle Sachen so. Man muß die Dinge in ihrer Wirklichkeit im Geistigen suchen. Es ist in manchen Fällen durchaus so, daß das, was auf dem physischen Plane geschieht, direkt ein Abbild sein kann von dem, was in der gei­stigen Welt geschieht. In andern Fällen ist ein so kolossaler Gegensatz vorhanden wie hier zwischen dem Osten und dem Westen, wo man auf dem physischen Plan in der Maja ein Bündnis hat und in der geistigen Welt einen an Bedeutung unendlich überragenden Kampf. Denn durch diesen Kampf soll allmählich herbeigeführt werden, daß ein richtiges Bild aus der Ätherwelt heraustritt, ein Bild von dem Wesen, das in unserer Zeit im Laufe des 20. Jahrhunderts herankommen soll an die Menschheit, in dem Christus.",
      "Mit solchen Betrachtungen wollen wir bei der nächsten Gelegenheit fortfahren. Aber ich bitte Sie, solche Dinge wie die heutigen im vollen Ernste zu nehmen, denn ich versichere Sie, wenn man sie zum ersten Male findet, wirken sie genugsam erschütternd."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Ich möchte durch eine in unsere Vorträge eingeschobene Betrachtung dazu beitragen, daß wir das schon Gesagte, mehr oder weniger mit der Ausgestaltung unseres Baues zusammenhängend Gesagte, noch tiefer verstehen lernen und manches noch in Zukunft hinzufügen können, was besser wird verstanden werden können durch eine solche episo­dische Betrachtung, wie es die heutige sein soll."
      ],
      [
        "Wir wissen, daß des Menschen Seelenwesen gegliedert uns erscheint in die Empfindungsseele, die Verstandes- oder Gemütsseele und die Be­wußtseinsseele.",
        "Wir wissen, daß in diesen drei Seelengliedern arbeitet, so wie es in der «Theosophie» beschrieben ist, das Ich des Menschen."
      ],
      [
        "Nun geht in der menschlichen Natur wirklich viel vor sich, das nicht so, wie es vor sich geht, ins Bewußtsein hereindringt.",
        "Gerade die geistes­wissenschaftliche Erkenntnis kann allmählich dazu führen, daß vieles, was in den Tiefen der menschlichen Seele liegt, beleuchtet wird von dem Lichte des Bewußtseins."
      ],
      [
        "Aber wenn so die Menschenseele hinlebt, so beleuchtet sie gleichsam nur einen kleinen Teil des gesamten Seelen­horizontes, und unter diesem Horizont liegt vieles, was tiefe, tiefe Be­deutung für die Seele hat, aber nicht für das gewöhnliche Leben bewußt wird, was gewissermaßen viel bedeutsamer ist für die menschliche See­lengestaltung als das, was bewußt ist.",
        "Vor allen Dingen wollen wir jetzt unseren Blick werfen auf etwas, was gewöhnlich nicht zum Bewußtsein kommt."
      ],
      [
        "Für den heutigen Menschen ist es sogar recht heilsam, daß das nicht zum Bewußtsein kommt.",
        "Wir werden aber später sehen, daß das nicht immer für alle Menschen so war.",
        "Wenn nur ein wenig sich das gewöhnliche Alltägsbewußtsein des Menschen vertiefen würde und würde heräufhölen können, was, ich möchte sagen, nur um einen Grad unbewußter ist als das gewöhnliche Bewußtsein, dann würde die Men­schenseele sehr bald dahinterkömmen, daß sie die Dreiheit ist, von der gesprochen worden ist, daß sie wirklich nicht so ohne weiteres eine Ein­heit ist, söndern eine Dreiheit."
      ],
      [
        "Ich habe angedeutet in der Schrift «Wie erlangt män Erkenntnisse höherer Welten?», daß, wenn der Mensch anfängt"
      ],
      [
        "vorzurücken gegen die geistigen Welten zu, er gleichsam ausein­anderfällt in eine Dreiheit.",
        "Und sobald man nur, wie gesagt, ein wenig hereinblickt in den gleichsam zugedeckten Teil des Bewußtseins, so merkt man sehr bald, daß diese Dreiheit von Empfindungsseele, Ver­standes- oder Gemütsseele und Bewußtseinsseele da ist.",
        "Unter der Schwelle des Bewußtseins - und zwar gar nicht besonders tief für den gegenwärtigen Menschen - ist wirklich eine Art von Seelenreich, das durchsetzt wird nicht von einer Einheit, sondern von einer Art Drei­heit, von dem Hereinstrahlen dieser Dreiheit, so daß in dem Augen­blick, wo der Mensch zurückdrängt das, was er im Grunde genommen erst so völlig seit der zweiten Hälfte der vierten nachatlantischen Pe­riode erlangt hat und so ganz klar erst nach dem Beginn des fünften nachatlantischen Zeitraums, sobald also der Mensch das zurückdrängt, kann er genau zwischen drei Welten oder Gebieten in seiner Seele unter­scheiden.",
        "Das eine Gebiet ist ein solches, das mehr inspiriert wird, in welches traumhafte, träumerische Inspirationen hineinkommen.",
        "Das zweite Gebiet ist das, durch welches der Mensch gleichsam sich selbst durchseelt, auferbaut in den physischen Teilen.",
        "Und das dritte Gebiet ist das, wo er das Bewußtsein von der Welt erhält."
      ],
      [
        "Das erste Gebiet also ist das, in welches die Inspirationen herein-dringen, traumhafte Inspirationen, welche die Seele ausfüllen, was an die Empfindungsseele gebunden ist.",
        "Ein zweites Gebiet, wo die Seele gleichsam durch ihre eigenen inneren Gestaltungen und Bildungen ihren Leib auferbaut, ist gebunden an die Verstandes- oder Gemütsseele.",
        "Das ist der innere Werkmeister, der Baumeister, wir könnten auch sagen der Schmied des physischen Leibes.",
        "Und das dritte, die Vermittlung des äu­ßeren Erkennens, das in Zusammenhang tritt mit der Welt, die an die Sinne gebunden ist, überhaupt mit der physischen Welt zusammen­hängt, ist an die Bewußtseinsseele gebunden.",
        "Wir können also sagen:"
      ],
      [
        "zusammenhängend mit physischen Gewalten."
      ],
      [
        "Gleichsam eine Seelentrinität waltet auf dem Grunde der Seele des Menschen, und dieser Trinität steht gegenüber das Walten und Wirken desjenigen, was zur Einheit strebt.",
        "Ich will es dadurch andeuten, daß ich gleichsam ein besonderes Seelenreich dem andern hier gegenüber­stelle (siehe folgende Zeichnung)."
      ],
      [
        "Dieses Seehenreich wirkt in gewisser Beziehung ganz in sich einheitlich.",
        "Es wirkt aber naturhaft einheitlich gleichsam dasjenige, was die Seele ihrem Temperamente, ihrem Charakter nach ist, was tief unten in der Seele ruht, aber als einheitliche Seele.",
        "Das möchte ich mit diesem be­zeichnen: Einheitsseele, im Gegensatz zu der Dreiheit."
      ],
      [
        "# Bild s. 42"
      ],
      [
        "So, wie einmal unsere Seele jetzt ist, kann diese Einheitsseele aus einem gewissen dumpfen Leben nicht herauskommen, wenn sie nicht gleichsam überhellt, überheuchtet wird.",
        "Und in unserer Zeit geht das Überleuchten immer aus in irgendwelcher Form von dem Mysterium von Golgätha, so daß ich das, was in irgendwelcher Weise hereinstrahlt"
      ],
      [
        "in die Einheitsseele, symbolisch Ihnen hinzeichne: irgendeine Form, in der das Mysterium von Golgatha hereinstrahlt in die Einheitsseele."
      ],
      [
        "Nun haben wir wirklich schon im Laufe der Jahre vieles, vieles auf­gewendet, um nach und nach uns eine Vorstellung davon zu verschaf­fen, wie unendlich weit all das ist, was mit dem Mysterium von Gol­gatha zusammenhängt.",
        "Sie können sich daher denken, daß, wenn so das Mysterium von Golgatha in irgendeiner Form in die Menschenseele"
      ],
      [
        "# Bild s. 43"
      ],
      [
        "hereinstrählt, das immer nur eine gewisse Stufe, ein gewisser Grad des Mysteriums von Golgatha ist.",
        "Aber wir stellen uns vor, daß, weil die Einheitsseele etwas gleichsam dumpf Brütendes ist, aber das für unsere Zeit besonders Wertvolle enthält, so muß dieses Einheitliche in irgend­einer Form von dem Mysterium von Golgatha durchstrahlt werden."
      ],
      [
        "Nun ragt in jede Seele dasjenige hinein, was von den verschiedenen Inspirations- und Initiationszentren der Welt ausgeht, und das gehört auch zu den unterbewußten Einflüssen in der Menschenseele.",
        "Sehen Sie, die Wirkung des Mysteriums von Golgätha ist eine umfassende, eine universelle, aber der Mensch, die Menschenseele kann dieses Mysterium von Golgatha nur in einer bestimmten Weise aufnehmen.",
        "Das Initia­tionszentrum, welches ganz besonders in das Innere der Seele herein-wirkt, damit das Innere der Seele richtig vorbereitet wird, sich von dem Mysterium von Golgatha ganz besonders durchstrahlen zu lassen, habe ich früher öfter so besprochen, daß ich gesagt habe: Es steht immer vor diesem Initlationszentrum der Eingeweihte Skythianos. - Nehmen wir also an, die Seele wäre vorbereitet worden in der Einheitsseele für das, was vom Mysterium von Golgathä kommt, bereit, es aufzunehmen durch das, was in jeder Seele unbewußt, von Skythianos her, hinein wirkt."
      ],
      [
        "Da haben wir gleichsam die Seele des Menschen gespalten in zwei Reiche: in das eine Reich, das eine Dreigliedrigkeit ist, und in ein an­deres Reich, welches eine Einheit ist: in ein mehr seelisches Reich und in ein mehr näturhaftes, temperamentmäßig brütendes Reich, möchte ich sagen, in ein Reich, das mehr aufnimmt in seine Naturgrundlage die Kräfte des Mysteriums von Golgatha auf der einen Seite und auf der ändern Seite die Einflüsse des Skythianos."
      ],
      [
        "Nun kann diese Einheit mit der Dreiheit nicht ohne weiteres sich verbinden, das ginge nicht, und deshalb ist es auch so, daß diese Drei­heit bei den gegenwärtigen Menschen unter der Schwelle des Bewußt­seins bleibt.",
        "Es wird diese Dreiheit gleichsam übertäubt; es muß das Bewußtsein davon ausgelöscht werden.",
        "Wenn die Seele wirklich her-unterkommen könnte zu der Dreiheit, würde sie sich sogleich als Drei­heit, nicht als eins, fühlen.",
        "Sie würde sägen: Da ist etwas in mir, das inspiriert mich, etwas, das baut mich auf, das schmiedet mich zusam­men, und etwas, das steht mit der Außenwelt im Zusammenhang. -Aber diese Dreiheit muß gleichsam durch etwas ausgelöscht, über­schattet werden, was seelisch den Menschen dahin bringt, daß er sägt:"
      ],
      [
        "Ich unterscheide nicht die Drei. - Es muß also etwas hereinstrahlen in die Drei, das macht, daß die Seele die Drei nicht in sich empfindet,"
      ],
      [
        "diese Drei auslöscht, gleichsam wie Nebelgebilde zueinander sein läßt."
      ],
      [
        "Sehen Sie, dann kann die Verbindung bestehen zwischen dem, was in der Seele als Einheit leben soll, und dem, was als Dreiheit in der Seele ist, wenn eine Kommunikation, eine Art Austausch da ist, gleichsam eine Art Seelenstamm, der zur ausgelöschten Dreiheit hinführt und der"
      ],
      [
        "# Bild s. 45"
      ],
      [
        "ausgeht von dem, was Einheit ist, aber von zwei Seiten her durchstrahlt wird, gleichsam durchleuchtet wird dazu, daß es nicht nur eine dumpfe, gleichmäßige charakter- und temperamentgemäße Natureinheit ist, sondern daß es einheitlich durchleuchtet wird von dem, was der Mensch sein soll: von dem Bewußtsein der Menschenseele in ihrem Zusammen­hang mit dem göttlich-geistigen Sein.",
        "Eigentlich habe ich da etwas aufgezeichnet,"
      ],
      [
        "was auf dem Grunde jeder Menschenseele ruht.",
        "Keine ein­zige Menschenseele kann in unserer Zeit ohne das sein, daß alle diese Dinge in ihr vorhanden sind."
      ],
      [
        "Aber nun stellen Sie sich das Folgende vor.",
        "Ich habe wiederholt gerade hier betont, um zu zeigen, was unser Bau sein soll, daß dasjenige, was in der Menschenseele lebt, äußerlich auch zur Darstellung kommt, sich auslebt sozusagen in der äußeren Evolution der Erde."
      ],
      [
        "Wenn es ein solches Gebiet in der Menschenseele gibt, das wirklich eine Art von Dreiheit darstellt, das bei den heutigen Menschen gleichsam schon überzogen ist von dem gewöhnlichen Bewußtsein, so müssen wir ein­mal ein Evolutionsstadium finden, wo uns das äußerlich entgegentritt, daß die Seele wirklich sich als eine Dreiheit empfindet, gleichsam aus­einandergelegt in drei Seelenglieder.",
        "Mit andern Worten, es muß ein Volk einmal dagewesen sein, das diese drei Seelenglieder auseinander-gelegt empfand und so empfand, daß im Grunde genommen die Einheit viel geringer empfunden wurde in der Seele als die Dreiheit, da die Dreiheit noch in Verbindung gedacht wurde mit dem Kosmos."
      ],
      [
        "Dieses Volk war da in Europa und hat ein bedeutendes Kulturdenkmäl hinter­lassen, von dem ich schon einmal gesprochen habe.",
        "Dieses Volk, das einmal, und zwar an der Stelle in Europa, wo es sein mußte, diese Drei­heit empfand in der Seele, ist das finnische Volk."
      ],
      [
        "Und der Ausdruck dieser Kulturstufe ist niedergelegt in Kalewala.",
        "In dem, was in Kale­wala dargestellt ist, ist das deutliche Bewußtsein von der Dreiheit der Seele vorhanden, so daß von den alten Sehern, deren Sehertum Käle­wala zugrunde liegt, empfunden wurde: Da ist etwas Inspirierendes in der Welt, mit dem steht ein Glied meiner Seele in Verbindung, meine Empfindungsseele."
      ],
      [
        "Sie tendiert dahin, deren Kräfte gehen dahin, sie bekommt von da die Impulse. - Gleichsam ein Menschlich-Göttliches oder Menschlich-Heroisches empfand dieses Volk oder empfanden diese alten Seher als das Inspirierende der Empfindungsseele.",
        "Und sie nann­ten das Wäinämöinen."
      ],
      [
        "Das ist nichts anderes als das im Kosmos Inspi­rierende der Empfindungsseele.",
        "Alle die Schicksale, die in Kalewäla als die Schicksale von Wäinämöinen geschildert werden, drücken aus, daß dieses Bewußtsein einmal vorhanden war bei einem Volke, welches eine große Ausbreitung in dem Nordosten des europäischen Gebietes hätte,"
      ],
      [
        "und das die drei Seelenglieder getrennt empfand und die Empfindungs­seele inspiriert von Wäinämöinen."
      ],
      [
        "Ebenso hat dieses Volk, haben diese alten Seher empfunden, daß die Verstandes- oder Gemütsseele gleichsam ein Glied extra in der Seele ist, das seine Impulse empfängt zum Schmieden, haben empfunden das, was schmiedet in der menschlichen Seele, was sie aufbaut, von einer andern elementärischen, heroischen Wesenheit empfängt, von Ilma­rinen.",
        "Wie also Wäinämöinen entspricht der Empfindungsseele, so ent­spricht in Kalewala Ilmarinen der Verständes- oder Gemütsseele.",
        "Wenn Sie den Vortrag über Kalewala nachlesen, so können Sie das alles darin finden."
      ],
      [
        "Und ebenso empfand dieses Volk - das muß festgehalten werden -, daß dazumal die Bewußtseinsseele empfunden wurde wie das, was den Menschen erst zu einem Eroberer auf dem physischen Plan macht, empfanden diese alten Seher in Lemminkäinen ein Wesen, das mit den Gewalten des physischen Planes zusammenhängt, ein elementares, hero­isches Wesen in dem Inspirator der Bewußtseinsseele.",
        "So stammen diese drei, man möchte sagen, Heldenfiguren, wenn man in Analogie mit andern Epen spricht, von dem alten finnischen Volk her, inspirierend die Dreigliedrigkeit der Seele."
      ],
      [
        "Das Wunderbare ist der Zusammenhang zwischen Ilmarinen und demjenigen, was da geschmiedet wird.",
        "Ich deutete es schon an.",
        "Es wird geschmiedet aus den Naturelementen heraus der Mensch selber.",
        "Dieses Wesen, das aus allen Naturatomen zusammengeschmiedet wird, pul­verisiert und zusammengeschmiedet wird, ist in einem großartigen Tableau in dem Schmieden des Sampo in Kalewäla dargestellt.",
        "Und daß dieses Bilden des Menschen aus diesen drei Seelengliedern heraus einmal geschehen ist, dann gleichsam wie in ein Prälaya gehen muß und dann wiederum hervorkommt, ist auch dargestellt in Kalewala: wie der Sampo verlorengeht und wiedergefunden wird, gleichsam wie wieder­gefunden wird das, über das sich zunächst Bewußtseinsdunkelheit ver­breitet."
      ],
      [
        "Und nun stellen wir uns vor, daß gegen den Süden zu, gegen den Südosten, können wir sägen, ein anderes Volk gegenübersteht, das die­jenigen Seeleneigenschaften zunächst in älter Zeit ausgebildet hat, von"
      ],
      [
        "denen ich gesprochen habe, das Einheitsmäßige in der Seele, das, was das Einheitsmäßige zum Ausdruck bringt in den Charakter-, den Ge­mutseigenschaften, in den Temperamentseigenschaften.",
        "Dieses Volk ist ein slawisches Volk, während das Volk, das ihm gegenübersteht, das finnische Volk ist.",
        "Dieses slawische Volk bekommt seine Einflüsse von Skythianos, der auch eine Zeitlang in alten Zeiten gelebt hat vom alten Skythenvolk umgeben.",
        "Es ist durchaus nicht notwendig, daß um ein Initiationszentrum herum auch ein hochentwickeltes Volk lebe, son­dern es muß im Verlaufe der Entwickelung das geschehen, was not­wendig ist.",
        "Und das Hereindringen einer bestimmten Form des Myste­riums von Golgätha ist das Hereindringen der griechisch-byzantinischen Kultur in das Slawentum.",
        "Was ich Ihnen hier als ein Zentrum der grie­chisch-byzantinischen Kultur aufgezeichnet habe, das können Sie ruhig, wenn Sie wollen, als Konstantinopel auffassen auf der Karte von Eu­ropa, denn das ist im Grunde genommen Konstantinopel."
      ],
      [
        "So haben wir also jetzt Seelen, die sich mit einem slawischen Grund-typ imprägniert finden.",
        "Es sind Seelen, die auf der einen Seite ver­bunden sind mit dem, was zu einem Einheitswesen durch das Myste­rium von Golgatha führen kann, was in Einheitsseelen zum Christen­tum vorbereiten kann, die auf der andern Seite das Mysterium von Gölgatha in einer ganz bestimmten Form empfangen, etwas wie die Inspiration, die Influenzierung durch das Mysterium von Golgatha, wie sie von der byzantinisch-griechischen Kultur ausgegangen ist."
      ],
      [
        "Nun muß aber noch etwas anderes, von einem gewissen Punkte her gleichsam, kommen.",
        "Was im finnischen Volke da war als die Scheidung, die Trennung in die drei Glieder, deren Bodensatz so großartig in Kale­wälä enthalten ist, das muß ausgelöscht werden.",
        "Das kann nur ausge­löscht werden, wenn ein Einfluß von außen kommt, kann nur aus­gelöscht werden dadurch, daß gleichsam ein Volk oder ein Völksteil da vördrängt, der von vornherein dazu veranlagt ist, nicht die Dreiheit, sondern die Einheit in der Seele zu empfinden, nicht die Einheit, die man bekommt von dem Mysterium von Golgatha aus, sondern die Ein­heit, die man gleichsam von Natur aus hat.",
        "Wenn man das finnische Volk betrachtet, so findet man es besonders veranlagt, das Bewußtsein der Dreiheit auszubilden.",
        "Und man kann nicht bedeutsamer diese Dreiheit"
      ],
      [
        "# Bild s. 49"
      ],
      [
        "in ihrem Verhältnis zum Kosmos ausdrücken, als das in Kalewala geschehen ist.",
        "Aber dann mußte das im Norden übertüncht, übernebelt werden von dem, was gleichsam auslöscht das Bewußtsein von dieser Dreiheit.",
        "Es drängte da ein Stamm herunter, der in einer naturhaften Weise das in seiner Seele trug, was damals als das Einheitsstreben da war, was in einer ganz andern Weise, auf einer ganz andern Stufe im Goetheschen «Faust», aber auch überhaupt in Faust zum Ausdruck ge­kommen ist, etwas, das nicht weiß von der Dreigliedrigkeit, das nach der Einheit des Ich strebt.",
        "Hier noch auf einer primitiven Stufe wirkt das auslöschend auf die drei Seelenglieder."
      ],
      [
        "Nun ist aber das finnische Volk ein solches gewesen, welches noch naturhaft empfand, sonst hätte es nicht die drei Seelenglieder empfun­den.",
        "Das, was dahinflutet, auslöschend die Dreiheit, dieses Hin flutende, Hineindrängende empfand man als ein r r r, und weil man es empfand als etwas, was, man möchte sägen, in okkulter Spräche am besten aus­gedrückt ist in den Buchstaben, in dem Laute u u o, so daß man sägen möchte: Es kommt heran, man muß eigentlich Scheu davor haben, so haucht es hin in dem rruuo und setzt sich fest, was immer durch das Tau, t, empfunden wird, wenn das in die menschliche Seele hinein­dringt.",
        "Geradeso wie das Hineindringen in die menschliche Seele beim alten Jehova durch das s, durch das hebräische «Shin», ausgedrückt ist, so wird überhaupt dieses Eindringen in die Seele, das Durchdringende durch den s-Laut ausgedrückt.",
        "All das hängt zusammen mit dem, was in die Seele eindringt und festhält in der Seele, all das drängt zum i hin, dessen Bedeutung ja bekannt ist, im finnischen Volk das, was mit dem rruu zusammenhängt.",
        "Daher empfand es dieses rutsi, ruotsi, und daher nannte es die Völker, die herunterdrängen da, die Rutsi, Ruotsi.",
        "Und diesen Namen haben allmählich die Slawen aufgenommen, und weil sie sich verbunden haben mit dem von oben nach unten Dringenden, was die Finnen so nannten, nannten sie sich selbst Rutsi, was später zu dem Namen Russen wurde."
      ],
      [
        "Sie sehen also, das alles mußte sein, was in der Geschichte äußer­lich erzählt wird, daß diese hier unten sitzenden Völker gerufen haben die Warägerstämme, die eigentlich normannisch-germanische Stämme waren, die sich verbinden mußten mit den slawischen Stämmen.",
        "Dem liegt etwas zugrunde, was sein mußte, durch die Einrichtung der Men­schenseele notwendig sein mußte.",
        "Und so kam denn das zustande, was dann später im Osten von Europa als das Element des Russischen in das europäische Volkstum eintrat.",
        "In dem Element des Russischen lebt also all das wirklich drinnen, von dem ich gesprochen habe.",
        "Es lebt vor allen Dingen darinnen jenes normannisch-germanische Element, lebt sogar in dem Namen drinnen, von dem der Name Russe gekommen ist, denn der ist auf dem Wege gekommen, den ich angedeutet habe."
      ],
      [
        "In tiefsinniger Weise wird in Kalewala ausgedrückt, daß die Größe des finnischen Volkes darauf beruht, daß es eigentlich vorbereitet in"
      ],
      [
        "der Dreiheit die Einheit, vorbereitet durch Auslöschung der Dreiheit das Entgegennehmen derjenigen Einheit, die nun nicht mehr nur menschliche Einheit ist, sondern die göttliche Einheit ist. in welcher lebt der göttliche Held des Mysteriums von Golgatha."
      ],
      [
        "Damit eine Gruppe von Menschen aufnehmen kann dasjenige, was an sie herankommt, muß sie erst vorbereitet werden.",
        "Wir bekommen auf diese Weise einen Eindruck davon, was alles innerlich geschehen muß, damit das in der Entwickelung sich vollziehen kann, was einem äußerlich entgegentritt.",
        "Ich sagte, in Kalewala wird in großartiger Weise ausgedrückt, daß das finnische Volk diese Vorbereitung zu lie­fern hatte, dadurch, daß am Schlusse in eigentümlicher Weise das Mysterium von Golgätha in Kalewala eingeführt wird.",
        "Christus tritt am Schlusse von Kalewala auf, aber indem er seinen Impuls in das finnische Leben wirft, geht Wäinämöinen aus dem Lande fort, was aus­drückt, daß das ursprünglich Große, das Bedeutungsvolle, das durch das finnische Element in Europa hereingekommen ist, ein Vorberei­tungsstadium für das Christentum ist und das Christentum wie eine Kunde, wie eine Botschaft von außen empfängt."
      ],
      [
        "Wie wir beim einzelnen Menschen sehen, daß er in außerordentlich komplizierter Weise gleichsam zubereitet werden muß, damit dann seine Seele das finde von den verschiedensten Seiten her, was sie braucht, um in einer bestimmten Inkarnation zu leben, so ist es auch mit den Völ­kern.",
        "Ein Volk ist nicht etwas ganz so Einheitliches, Homogenes, son­dern ein Volk ist etwas, worin viel zusammenfließt.",
        "Das Volk, das da im Osten drüben lebt, in ihm ist all das zusammengeflossen.",
        "Und all dasjenige, könnte man sagen, was innerlich spirituell ist, ist äußerlich wenn auch äußerlich in leichter Weise nur - angedeutet.",
        "Ich habe ge­sagt, bei diesem Volk muß ein Seelenstamm sein, der von unten nach oben, respektive auch von oben nach unten führt, wenn es ein verbin­dender Seelenstamm ist.",
        "Das war vorhanden in einer mächtigen Straße, welche vom Schwarzen Meer zum Finnischen Meerbusen ging, und auf der ein Austausch stattfand zwischen dem griechisch-byzantinischen Element und dem, was ein Näturelement war der Rutsi."
      ],
      [
        "Der Mensch muß im Laufe seiner verschiedenen Inkarnationen ver­schiedenes durchmachen.",
        "Eine Inkarnation muß sich immer auf die"
      ],
      [
        "andere aufbauen.",
        "Das kann der Mensch nur dadurch, daß gleichsam in die Substanz, in das Material, aus dem die einzelnen Völker und ihre Angehörigen gebildet werden, wirklich die Kräfte zusammenfließen, durch welche später die Menschenevolution sich vollziehen kann."
      ],
      [
        "Es muß eine Menschenseele einmal in ihren Inkarnationen solch eine Leib­lichkeit finden, die zusammengeflossen ist aus den Kräften, die ich hier dargestellt habe.",
        "Und was man so einfach sagt, ein Mensch wird als Russe geboren, das hat seine tiefe, seine kolossal tiefe Bedeutung."
      ],
      [
        "Ein Mensch wird als Russe geboren, heißt: er ist auf dem Wege durch die verschiedenen Inkarnationen dabei angelangt, innerhalb seiner Erden-laufbahn das zu erleben, was man nur dadurch erleben kann, daß man in einer Körperlichkeit durchläuft ein Leben zwischen Geburt und Tod, die auf solche Weise zusammengetragen ist.",
        "Würde man nicht in einem solchen Körper das durchleben, so würde einem etwas fehlen in dem, was man von Inkarnation zu Inkarnation sich erwirbt."
      ],
      [
        "Törichte Men­schen - ich sage das, ohne daß damit irgendeine Empfindungsnuance verbunden ist, sondern ich sage das als Terminus technicus - haben immer wieder und wiederum von dem Sprichwort gesprochen: Die Welt begreift man in ihrer Wahrheit am besten, wenn sie einem in ihrer Einfachheit erscheint. - Das ist nicht wahr, das ist nur bequem.",
        "Tiefe Geister haben es immer ausgesprochen, zum letzten Mal am eindring­lichsten wohl Ralph Waldo Emerson, daß man zur Wahrheit der Tat­sachen erst eindringt, wenn man sie in ihrer ganzen Kompliziertheit erkennt."
      ],
      [
        "Es ist nicht so einfach, das, was in der Welt lebt und was mit der ganzen Weltenevolution zusammenhängt."
      ],
      [
        "Und so wie es auf der östlichen Hälfte der europäischen Halbinsel ist, daß die Seelen zubereitet werden, um etwas Besonderes zu erleben, so ist es für alle andern Fälle der Erdenoberfläche, so sind die einzelnen Volkscharaktere in einer komplizierten Weise zubereitet.",
        "Nun erinnern Sie sich vor allen Dingen an eines, das wir genügend im Verlaufe un­serer geisteswissenschäftlichen Betrachtungen kennengelernt haben."
      ],
      [
        "Der Mensch ist gewissermaßen, wenn er durch die Pforte des Todes gegangen ist, dadurch, daß er zurückblickt auf sein letztes Erdenleben, abhängig von dem, was er in seinem letzten Erdenleben erlebt hat.",
        "Wir wissen, daß jahrelang hineinspielen in das Leben nach dem Tode die"
      ],
      [
        "Zusammenhänge mit dem früheren Erdenleben.",
        "Das muß aber so sein.",
        "Der Mensch muß durch eine physische Inkarnation hindurchgehen, damit er in dieser Zeit zwischen dem Tode und einer neuen Geburt bestimmte Erinnerungen an diese vorhergehende Inkarnation hat, be­stimmte Impulse aus dieser vorhergehenden Inkarnation hereinreichen."
      ],
      [
        "Dadurch, daß er ein ganz bestimmtes Menschenwesen mit einem be­stimmten Organismus war, der durch die Erdenverhältnisse bestimm­ten Einflüssen unterworfen wär, wirken auch noch gewissermaßen die Eindrücke nach dem Tode, die erinnerungsmäßig zurückgehen.",
        "Diese werden dadurch influenziert, beeinflußt, sie bekommen eine gewisse Schattierung."
      ],
      [
        "Das ist die Schattierung, welche eine Seele dadurch emp­fängt, daß sie durch eine bestimmte Nationalität hindurchgegangen ist, die sie aus einer gewissen Nationalität heraus bekommt.",
        "Das wird immer mehr und mehr abgestreift, je mehr das Nationale in das Inter­nationale übergeht."
      ],
      [
        "Aber heute ist das noch in hohem Maße vorhanden, sonst hätten die heutigen Ereignisse nicht eintreten können.",
        "Die Men­schen blicken in gewissem Maße noch zurück auf dasjenige, was sie durch ihren Organismus - insofern dieser national bestimmt ist - im vorhergehenden Leben zwischen Geburt und Tod erlebt haben."
      ],
      [
        "Nun werden die Seelen, die auf die heute beschriebene Weise durch Leiber hindurchgehen, die gerade auf diese bestimmte Art zubereitet worden sind, in einer ganz bestimmten Art präpariert auf das Leben, welches sie antreten, nachdem sie durch die Todespforte gegangen sind.",
        "Die Individualität wird natürlich nicht beeinflußt, nur das, was gleichsam wie die Kleider, die Hüllen der eigentlichen Individualität ist."
      ],
      [
        "Aber diese Kleider oder Hüllen, mit denen die Nationalität zusammenhängt, geben da noch etwas, was die Seele auch nach dem Tode hat, von dem sie weiß, das hat zu deinem Durchgänge durch das Erdenleben gehört."
      ],
      [
        "Wenn nun die Seele durch einen Leib durchgegangen ist, der so zu­bereitet worden ist - exoterisch würde man sagen, die durch einen russischen Leib in einer Inkarnation durchgegangen ist -, so hat sie selbstverständlich die Nuancierung des äußeren Hüllenhäften, das nach dem Tode zu einer Vorstellung wird, die man von sich hat, wie man sonst Vorstellungen von sich hat.",
        "In das hat sie aufgenommen alles das, was hier (siehe Zeichnung S.49) auf diese Weise ausgedrückt ist, und"
      ],
      [
        "wenn man aussprechen will, was die Seele innerlich dadurch durch­macht, daß sie einen so zusammengesetzten Leib hat, so kann man fol­gendes sagen.",
        "Nicht wahr, wir wissen aus den bisherigen Betrachtungen, daß sich das Bewußtsein in einer gewissen Weise verändert nach dem Tode, es erlangt einen höheren Grad, wird deutlicher, intensiver nach dem Tode, als es in einem physischen Leib ist.",
        "Das durchgemacht zu haben, was vorher gemeint ist, bereitet die Seele vor, in besonders in­time Beziehung nach dem Tode zu denjenigen Wesen zu kommen, die wie besondere Schutzgeister über den eigentlichen menschlichen Indi­vidualitäten leben und in die nächst höhere Hierarchie gehören, in die Hierarchie der Angeloi.",
        "In dem Leben nach dem Tode, das bei einer Seele auf eine russische Inkarnation folgt, ist sie gleichsam veranlagt, sich zu identifizieren im Bewußtsein mit ihrem Angelos, die geistige Welt gleichsam anzusehen, um einen groben Ausdruck zu gebrauchen, mit den Augen des Angelos."
      ],
      [
        "Der Mensch strebt zum höheren Selbst hinauf.",
        "Dieses höhere Selbst lebt sich in der verschiedensten Weise aus.",
        "Lesen Sie den letzten Münch­ner Zyklus über «Die Geheimnisse der Schwelle».",
        "Da haben Sie aus­einandergesetzt, wie das Bewußtsein etwas anderes wird, gleichsam sich die Seele mit dem Angelos durchdringt.",
        "Sie muß sich damit durch­dringen und bereitet sich zu dem Durchdringen mit dem Angelos da­durch vor, indem sie sich hineinlebt durch die Pforte des Todes in die geistige Welt nach dem Leben in einem russischen Leibe, der so zu­bereitet worden ist, wie wir es beschrieben haben.",
        "So daß wir sagen können: Derjenige, der durch einen russischen Leib gegangen ist, fühlt eigentlich alles nuänciert nach dem Tode dadurch, daß er besonders durchsetzt ist in seinem ganzen Wesen von einem Angelos, von dem alle Menschen beschützenden Genius der nächst höheren Hierarchie."
      ],
      [
        "Aber bei den Völkern der westlichen Kultur ist es so, daß man weniger stark sich imprägniert, weniger stark sich durchdringt nach dem Tode mit dem Wesen des Angelos.",
        "Geht man durch eine westliche Inkarnation, so erfährt man nach dem Tode eher das Folgende: Ich empfinde noch so, wie ich sonst auch empfunden habe, ich schaue die Welt noch an, wie ich sie sonst angeschaut habe. - Man empfindet es wie eine besondere Kunst, mit seinem Angelos zusammenzuwachsen."
      ],
      [
        "Für den Angehörigen des russischen Volkes ist es etwas Naturgemäßes, immer mit seinem Angelos zusammen zu sein.",
        "Die Seele geht auf dem Wege durch die Inkarnationen durch alle möglichen Nationalitäten hindurch und muß auch durch diese Inkarnation gehen, wo sie den Im­puls erhält, mehr in dem Angelos aufzugehen, mit dem Angelos zu­sammenzuwächsen, mit seinem Geistesauge zu schauen in die geistige Welt."
      ],
      [
        "Natürlich bezieht sich das mehr als auf andere Zeiten zwischen dem Tode und der neuen Geburt auf die Zeit unmittelbar nach dem Tode, die nächsten Jahre oder einundeinhalb bis zwei Jahrzehnte, denn in der Hauptzeit vor und nach der «Mitternacht», von der ich schon ge­sprochen habe, streift die Seele solche Dinge ab.",
        "Es bezieht sich das also auf die Zeit, in welcher der Mensch noch influenziert ist von dem, was er im physischen Leibe erlebt hat, wo das noch nachwirkt."
      ],
      [
        "Und nun wenden wir, nachdem wir dies auseinandergesetzt haben, einmal unseren Blick hin auf die geistige Welt, gleichsam auf das Innere der Welt, in der wir drinnen leben, indem wir zu unserer Betrachtung hinzunehmen, daß es nur dem beschränkten Menschensinne entspricht, wenn er glaubt, er ist nur von physischen Menschen umgeben.",
        "Er ist immer auch von den Verstorbenen umgeben, von denjenigen, die in der geistigen Welt leben.",
        "So haben wir in unserer Umgebung gestorbene Seelen, die durch physische, russische Leiber gegangen sind, die eine große Neigung haben, mehr als Angelos, möchte ich sagen, in ihrer jetzigen Seelenverfassung zu leben denn als Mensch."
      ],
      [
        "Nach einer solchen Inkärnation tritt noch das besonders Eigentüm­liche auf, daß der Ätherleib ganz besonders schnell sich in der um-liegenden Ätherwelt auflöst, während bei den westlichen Völkern der Ätherleib mehr kompakt ist, sich mehr zusammenhält, schwerer sich auflöst in der umgebenden Ätherwelt.",
        "Nun lehen wir aber bereits in einem Zeitpunkt, namentlich seit dem letzten Drittel des 19.Jahrhun-derts, wie ich schon oft angedeutet habe, wo in der geistigen Welt die Herrschaft durch Michael angetreten ist, nachdem vorher Gabriel re­gierte.Wir leben jetzt in einer Zeit,wo diese Verhältnisse ganz besonders stark in der geistigen Welt hervortreten, ganz besonders das Geschilderte wirkt in der geistigen Welt.",
        "Denn es obliegt unserer Zeit, das große Ereignis"
      ],
      [
        "vorzubereiten, das ich schön in dem ersten Mysteriendräma «Die Pforte der Einweihung» angedeutet habe, das Erscheinen des Christus in einer geistigen Gestalt vor dem Menschen.",
        "Dieses Ereignis der Er­scheinung des Christus, so wie es die Theödora angedeutet hat, kann nur herbeigeführt werden, wenn sich die Herrschaft des Michael immer mehr und mehr ausbreitet."
      ],
      [
        "Noch ist das ein Prozeß in der geistigen Welt Gleichsam kämpft auf dem Plane, der angrenzt an unsere Welt, Michael für das Herannahen des Christus.",
        "Er braucht seine Scharen, seine Kämpfer dazu.",
        "Nun werden wichtige Kämpfer ihm geliefert, wichtige Scharen aus denjenigen Seelen, die in der jetzigen Inkarnation durch einen russischen Leib gegangen sind."
      ],
      [
        "So daß wir geradezu in der geistigen Welt auf eine Art von Eroberungszug des Michael für das Herannahen des Christus blicken können.",
        "Dazu rekrutiert er sich eine Schar, eine Reihe von wichtigen Kämpfern aus den Seelen, die durch russische Leiber gegangen sind, weil sie in sich veranlagt sind, sich zu identifizieren mit ihrem Angelos."
      ],
      [
        "Dadurch werden sie ganz besonders geeignet, die Kräfte herbeizuführen, um in Reinheit das Bild zu geben, durch das der Christus erscheinen soll.",
        "Damit er nicht erscheint in fal­scher Gestalt, in subjektiver Menschheitsimaginätion, damit er erscheint im richtigen Bilde, muß Michael den Kampf kämpfen, den ich ange­deutet habe."
      ],
      [
        "Er kann ihn ganz besonders durch diejenigen Seelen kämp­fen, die naturhaft in sich dieses Angelosbewußtsein tragen.",
        "Dadurch sind sie besonders präpariert.",
        "Auch dadurch, daß ihr Ätherleib sich besonders leicht auflöst, haben sie nichts in ihrem Ätherleib, was den Christus in falscher Gestalt, in fälschen Imaginätionen erscheinen ließe."
      ],
      [
        "Damit all das, was in der Welt geschehen soll, richtig geschehen könne, müssen verschiedene Glieder in der Weltenordnung zusammen­wirken.",
        "Es muß nun, damit das geschehen könne, was ich dargestellt habe - nehmen Sie das ganz objektiv - eine Eigentümlichkeit bekämpft werden, die mehr im Westen ist, besonders bei den Seelen, die durch eine französische Inkarnation durchgegangen sind.",
        "Diese Seelen be­kommen von ihrer Nationalität das Eigentümliche, stark ihren Äther­leib festzuhalten, eine ganz bestimmte Imaginationsgestalt im Ätherleib lange festzuhalten.",
        "Das kann nicht durch die westlichen Seelen allein"
      ],
      [
        "bekämpft werden, sondern es muß dabei diesen westlichen Seelen, man möchte sägen, geholfen werden, es muß gearbeitet werden an der Zer­streuung dieser Ätherleiber in dem allgemeinen Weltenäther, damit nicht ein falsches Bild von der Christus-Erscheinung hervorgerufen werde.",
        "Es müssen also die Scharen zusammenwirken, die unter Michael kämpfen, müssen diejenigen Seelen bekämpfen, die durch französische Leiber hindurchgegangen sind."
      ],
      [
        "Das ist dasjenige, was hellseherisches Bewußtsein gerade in dem letz­ten Drittel des 19.",
        "Jahrhunderts und bis in unsere Zeit hinein als die Grundlage unserer jetzigen Evolution schauen konnte.",
        "Immer mehr und mehr entwickelte sich in der geistigen Welt, in der astralischen Welt, ein Kampf, geistig, zwischen Rußland und Frankreich - selbst­verständlich in demjenigen, was geistig zugrunde liegt -, und dieser Kampf wurde immer stärker und stärker.",
        "Kampf in der geistigen Welt bedeutet eigentlich Zusammenwirken in der physischen Welt, aber es ist das schon ein Bild des Kampfes, des Gegeneinanderwirkens, und der­jenige, der in die geistige Welt hineinschaut, hatte seit dem letzten Drittel des 19.",
        "Jahrhunderts bis in unsere Zeit hinein immer mehr und mehr ein Intensivwerden eines geistigen Kampfes zwischen Westen und Osten vor sich, über Mitteleuropa hindurch, den Kampf im Himmel, man könnte ihn schon so nennen, der darin besteht, daß immer mehr und mehr unter der Herrschaft des Michael Scharen im Osten gesam­melt worden sind, um all das, was verhindern könnte im Westen - in dem immer mehr und mehr in den Materialismus hineinwachsenden Westen - die Erscheinung des Christus, zu bekämpfen."
      ],
      [
        "Ja, meine lieben Freunde, wo eine hohe Kultur ist, eine so ganz aus­geprägte, zum Gipfel gekommene Kultur ist wie in Frankreich, hat die Seele bestimmte Imaginationen angenommen.",
        "Diese Imaginationen bleiben nach dem Tode, sie hindern aber, daß etwas ganz Neues kom­men kann, was durch den Christus kommen muß.",
        "Daher muß vor allem in der geistigen Welt das bekämpft werden, was aus einer vollreifen Kultur in die Seelen übergeht.",
        "Michael kann sich nicht seine Scharen aus einer vollreifen Kultur wählen, die eignen sich zu einer bestimmten Imagination; die Imaginationen müssen erst ausgelöscht werden.",
        "Daher das grandiose Bild hinter der Szene der geistigen Welt: des Kampfes"
      ],
      [
        "des Ostens gegen den Westen, der Schar des Michael gegen die selb­ständig gewordenen Seelen des Westens."
      ],
      [
        "Und sehen Sie, der äußere physische Ausdruck für einen geistigen Kampf ist ein physisches Bündnis.",
        "Was sich auf dem physischen Plane verbündet, drückt damit aus, daß es sich auf dem geistigen Plane in einem Kampf befindet.",
        "Man wird zu Verbündeten auf dem physischen Plan, wenn man auf dem geistigen Plan notwendig hat, sich zu be­kämpfen.",
        "Daraus sehen Sie wiederum einmal, wie ernst wir das Wort von der Mäja und der Wahrheit nehmen müssen.",
        "Oft und oft spricht man es aus, das Wort von der Maja und der Wahrheit, aber es bleibt Theorie, denn wer in die geistige Welt hereinschaut und dort schaut, was der physischen Welt zugrunde liegt, den überkommt schon das Gefühl ungeheuerlichster Erschütterung, wenn er im Ernste von der Mäja zur Wahrheit vordringt und hinter dem, was in der Maja lebt, die Wahrheit findet.",
        "Die Wahrheit muß oftmals mit ganz andern Worten ausgedrückt werden als auf dem physischen Plan."
      ],
      [
        "Was auf dem physischen Plan Bündnis heißt, heißt auf dem geistigen Plan oftmals Krieg.",
        "Natürlich darf man nun keine falschen Konstruk­tionen machen, indem man das, was man auf dem physischen Plan fin­det, in seinem Gegenteil im Geiste sucht, denn es ist nicht für alle Sachen so.",
        "Man muß die Dinge in ihrer Wirklichkeit im Geistigen suchen.",
        "Es ist in manchen Fällen durchaus so, daß das, was auf dem physischen Plane geschieht, direkt ein Abbild sein kann von dem, was in der gei­stigen Welt geschieht.",
        "In andern Fällen ist ein so kolossaler Gegensatz vorhanden wie hier zwischen dem Osten und dem Westen, wo man auf dem physischen Plan in der Maja ein Bündnis hat und in der geistigen Welt einen an Bedeutung unendlich überragenden Kampf.",
        "Denn durch diesen Kampf soll allmählich herbeigeführt werden, daß ein richtiges Bild aus der Ätherwelt heraustritt, ein Bild von dem Wesen, das in unserer Zeit im Laufe des 20.",
        "Jahrhunderts herankommen soll an die Menschheit, in dem Christus."
      ],
      [
        "Mit solchen Betrachtungen wollen wir bei der nächsten Gelegenheit fortfahren.",
        "Aber ich bitte Sie, solche Dinge wie die heutigen im vollen Ernste zu nehmen, denn ich versichere Sie, wenn man sie zum ersten Male findet, wirken sie genugsam erschütternd."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "ZWEITER VORTRAG Dornach, 14. November 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Wenn wir nur des Menschen physischen Leib betrachten, kommen wir sehr schwer zu solchen Erkenntnissen, wie diejenigen sind, von denen wir das letzte Mal gesprochen haben. Insbesondere gilt dieses für die­jenigen Völker, welche die Völker der neuen Welt, Europas und Ame­rikas, sind.",
      "Der physische Menschenleib in diesen Gebieten ist in weit geringe­rem Maße, als dies zum Beispiel in Asien und Afrika der Fall ist, von innen heraus gebildet. Bei den Völkerschaften Asiens und Afrikas ist der physische Leib mehr von innen heraus, von den im Ätherleibe lie­genden Kräften gebildet, formiert. Bei den Völkern Europas und Ame­rikas rührt der größere Einfluß in den Bildungs- und Formierungskräf­ten des physischen Leibes von den Einflüssen von außen her.",
      "Wir können etwa so sagen: Sobald wir nach den Kräften suchen, welche des Menschen physischen Leib bilden, formieren, müssen wir ätherische Kräfte finden. Diese ätherischen Kräfte liegen für die Be­wohner Afrikas und Asiens mehr im Inneren des eigenen Ätherleibes. Für die Bewohner Europas und Amerikas liegen sie mehr in der Äther­welt, die den Menschen von außen umgibt.",
      "Der Mensch Afrikas und Asiens steht also mehr mit den inneren Ätherkräften, der Mensch Europas und Amerikas mehr mit den äußeren Ätherkräften in Beziehung und dadurch mehr mit den Naturgeistern.",
      "Wenn ich mich primitiv ausdrücken, weniger auf das Rücksicht nehmen will, was uns klargeworden ist gerade durch die geisteswissen­schaftliche Betrachtung, so müßte ich sagen: Der physische Leib der afrikanischen und asiatischen Völker ist mehr von innen heraus, mehr durch innere Bildungskräfte geprägt. Der Leib der europäischen und amerikanischen Völker wird mehr durch die Hinwendung zu den Ver­hältnissen der Außenwelt geprägt. Die äußeren Kräfte drücken sich mehr in die plastischen Formen ein und bilden daher mehr die Formen des physischen Leibes.",
      "Ich habe in der Schrift «Die Schwelle der geistigen Welt» aufmerk­sam darauf gemacht, wie wir beim Menschen, sobald wir auf seinen Ätherleib Rücksicht nehmen, finden, daß er in einem größeren Maße, als man glauben könnte, wenn man das Auge bloß auf den physischen Leib richtet, mit dem ganzen Organismus der Erde in Beziehung steht. Die Erde selbst ist eine Art lebendiges Wesen. Aber, während uns der Mensch als lebendiges Wesen gewissermaßen wie eine abgeschlossene Einheit erscheint, so daß wir ihn auch als Einheit empfinden müssen, müssen wir die Erde als einen lebendigen Organismus so betrachten, daß wir in ihr ein Vielfaches von Naturwesen, die durcheinander-wirken, sehen.",
      "Zur Erde gehört zunächst die feste Erde selber, welche die Konti­nente bildet. Das, was wir aber als dieses Materielle, Feste der Erde an­sprechen, ist nichts anderes als Maja. Die Wirklichkeit ist eine große Summe von Naturgeistern, die wieder geführt werden von Geistern höherer Hierarchien. Daß sich das gleichsam zusammenballt und als feste Erde wirkt, ist Maja. Die Erde ist durch und durch Geist. Das ist oftmals betont worden.",
      "Nun gehört zur Erde nicht nur die feste Erde, sondern auch das, was als Gewässer die Erde durchsetzt, und insofern sich die Materie der Erde im Flüssigen auslebt, haben wir es wieder zu tun mit dem Wasser als der Maja. In Wirklichkeit aber haben wir es zu tun mit einer großen Anzahl von Naturgeistern. Ebenso ist es bei der Luft und ebenso bei der die Erde durchsetzenden und umspülenden Wärme. Das alles ist eine Summe von Naturgeistern, und das Materielle ist nur die äußere Maja.",
      "Mehr als das in Asien und Afrika der Fall ist, ist beim europäischen Menschen - beschränken wir uns darauf zunächst - gleichsam ein fort­währender Austausch der Impulse zwischen den inneren Ätherkräften und den Elementarwesen, welche in Feuer, Wasser, Luft und Erde ent­halten sind. Diese Elementarwesen wirken von außen herein auf die menschlichen Ätherleiber, und dadurch erhalten sie die formenden und bildenden Kräfte, die dann in dem Aussehen und den Verrichtungen des physischen Leibes bis in die Sprache hinein zum Vorschein kommen. Denn die Sprache ist durchaus auch eine Verrichtung des physischen Leibes. Aber selbstverständlich liegen die Impulse dazu im Ätherleibe.",
      "Nun, sehen Sie, muß man, wenn man den Menschen, so wie er auf der Erde lebt, wie er also auf dem Umwege über den Ätherleib ein Erdenwesen ist, der Erde angehört, darauf Rücksicht nehmen, in welch verschiedener Weise die einzelnen Wesenheiten der Erde, des Wassers, der Luft und so weiter auf den menschlichen Ätherleib wirken. Denn von ganz anderer Natur sind die elementarischen und ätherischen We­senheiten der Erde, von ganz anderer Natur die ätherischen und ele­mentarischen Wesenheiten des Wassers, so daß wir sagen können: Ein­fach dadurch, daß irgendein Mensch als physisches Wesen im Gebirge lebt oder am Meeresstrande, haben andere Wesenheiten auf seinen äthe­rischen Leib einen größeren Einfluß. Bei dem, der am Meeresstrande lebt, haben die elementarischen Wesenheiten, die ihren Majaausdruck im Wasser haben, einen viel größeren Einfluß als bei dem Menschen, der im Gebirge lebt. Bei einem Menschen, der im Gebirge lebt, haben die Wesen, die in der Erde leben, einen größeren Einfluß als die Wesen­heiten, die ihren Majaausdruck im Wasser haben.",
      "Nun wird dasjenige, was aus dem Menschen formiert, gemacht wird, durch dieses Zusammenwirken - ich rede jetzt immer hauptsächlich vom europäischen Menschen - der elementarischen Geister mitgewirkt, ich sage mitgewirkt, und in der Art, wie diese elementarischen Geister der Natur wirken, liegt etwas von dem, was aus der geistigen Welt her­aus den Menschen bildet, insofern dieser Mensch ein Erdenwesen ist.",
      "Ich habe Ihnen das letzte Mal davon gesprochen, daß der östlichen Kultur Europas voranging, sagen wir, eine Kulturschicht, deren Men-schen so beschaffen waren, daß sie in ihren Seelen noch etwas hatten von dem, was bei den heutigen Menschen mehr in das Unterbewußtsein zurückgedrängt ist, daß sie etwas im gewöhnlichen Leben hatten von einer Spaltung der Seele in Empfindungs-, Verstandes- oder Gemüts-und Bewußtseinsseele. Ich habe Sie darauf hingewiesen, daß das finni­sche Volk, das in alten Zeiten große finnische Volk - das heutige ist nur ein Rest eines einstmals ausgebreiteten finnischen Volkes -, eine solche Seele hatte, daß die Seelen dieser Menschen bei einem gewissen alten Hellsehen, das bei ihnen ausgebildet war, bei ihrem unmittelbaren Er-leben des Tages, etwas hatten von einer Spaltung der Seele in Empfin­dungs-, Verstandes- oder Gemüts- und Bewußtseinsseele.",
      "Ich habe Ihnen gesagt, daß in dem großartigen Epos Kalewala in den drei Figuren: Wäinämöinen, Ilmarinen und Lemminkäinen zum Ausdruck kommt die Darstellung, wie aus dem Kosmos herein diese dreigespaltene Seele bedingt wird, gleichsam gerichtet wird.",
      "Nun, wie konnte denn so etwas überhaupt zustande kommen? Wie konnte an einem bestimmten Punkte Europas - so stellen wir uns die Frage - ein großes Volk sich entwickeln, welches eine so geartete Seele hatte, wie ich es beschrieben habe?",
      "Nun, sehen Sie, wie der Mensch sein eigentliches Ich, die Gabe der Erde, entwickelt, das rührt davon her, daß die Geister der Erde von unten herauf, durch die Maja der irdischen Materie auf ihn wirken. Von unten herauf, gleichsam durch die feste Erde hindurch, wirken die Geister der Erde, und in unserem Zyklus ist es so, daß diese Geister der Erde im wesentlichen dazu benutzt werden, um in dem Menschen die Ich-Natur hervorzurufen.",
      "Sollte nun in einem Volksstamme, wie es das alte finnische Volk war, in die Seele hereinleuchten etwas von dem, was gleichsam unter der Ich-Natur liegt, was geistiger ist als die Ich-Natur, was mehr zusam­menhängt mit den göttlichen Kräften - denn wenn die Seele sich drei-gespalten empfindet, hängt sie mehr zusammen mit den göttlichen Kräften, als wenn sie das nicht tut -, sollte so etwas entstehen, so durfte in einer gewissen Weise nicht bloß das Irdische mit seinen elementari­schen Geistern von unten herauf in das Irdische des Menschen strahlen, sondern es mußte etwas anderes in dieses Irdische hereinstrahlen, ein anderer elementarischer Einfluß.",
      "Ebenso nun wie des Menschen physisches Dasein innig zusammen­hängt mit den Geistern der Erde - physisches Dasein, insofern es ein irdisches Dasein ist, und es in ihm sein Ich entwickelt -, zusammen­hängt mit den Geistern, die von der Erde selber, von unten nach oben, wirken, so hängt zusammen das Seelische des Menschen, das sich wie natürliches, temperamenthaftes, charakterhaftes seelisches Dasein des Menschen bekundet, mit alledem, was als wässeriges Element, als flüs­siges Element auf der Erde lebt. Es müssen also Geister des wässerigen, des flüssigen Elementes hereinwirken in diese Seelen, die also drei-gespalten sind.",
      "Nun ist einmal für unseren Zeitenzyklus das irdische Element das Ich-bildende Element, also dasjenige, worauf es ankommt. Wenn ein anderes Element hereinragt, wie zum Beispiel das wässerige Element, so ragt dieses mehr aus der geistigen Welt herein. Es ist nicht in dem Menschen selber enthalten. Es muß sich gleichsam als ein geistiges We­sen in den Menschen hineinsenken, damit er hereinbekommt in seine irdische Natur etwas, was ihn in die geistige Welt hineinführt.",
      "Nehmen Sie an, die Fläche der Tafel wäre das, wo die elementari­schen Kräfte der Erde herauskommen, so muß, wenn ein geistiges Ele­ment sich da hineinsenken will, dies von dem Organismus der Erde selber ausgehen, von etwas, was an sich geistig ist. Ein Wesen muß da sein, ein wirkliches Wesen, das nicht der Mensch selber ist, das den Menschen gleichsam inspiriert zu der Dreigespaltenheit der Seele. Ein Wesen also muß da sein, das gleichsam so auf die Seele wirkt, aus der Naturgeistigkeit heraus wirkt, daß die Empfindungsseele, die Verstan­des- oder Gemütsseele und die Bewußtseinsseele sich auseinanderlegen, so daß die Seelen wirklich sagen können: Für meine Empfindungsseele wirkt da aus der Natur herein etwas, wie Wäinämöinen, das mir ent­gegenströmt wie ein Naturwesen, das mir die Kräfte der Empfindungs­seele gibt.",
      "Aber es wirkt auch etwas herein wie Ilmarinen, etwas, was mir die Kräfte der Verstandes- oder Gemütsseele gibt, und es wirkt ferner etwas herein wie Lemminkäinen, etwas, was mir die Kräfte der Be­wußtseinsseele gibt. Wenn da ein Wesen ist, das gleichsam seine Fühler in die Natur vorstreckt wie durch eine Art von Hals, wenn ein Wesen, das hier gleichsam seinen Hauptgruppenleib hat und hier seine Fühler ausstreckt, so daß wir den einen der Fühler mit der Empfindungsseele hier haben, und sich hier hereinstreckt das zweite Fühlhorn und hier das dritte Fühlhorn, so hat das Naturwesen einen Leib und streckt sein Seelisches gleichsam wie seelische Fühler da hinein, um zu inspirieren, und da können die Ätherleiber sich bilden, welche der Seele die Fähig­keit geben, sich dreigeteilt zu fühlen.",
      "Die alten Finnen, die Bevölkerung des alten Finnland, sagten: Wir leben hier, aber wir fühlen etwas wie drei gewaltige Wesen, die nicht Wesen des physischen Planes sind, die Naturwesen sind. Sie enthüllen",
      "sich von Westen her, sie sind drei Teile, gleichsam Organe eines großen Wesens, das seinen Leib hat da drüben, aber es streckt uns seine Fühl­hörner hier entgegen: Wäinämöinen, Ilmarinen, Lemminkäinen. Ein mächtiges Meereswesen breitet sich von Westen nach Osten hin aus, das seine Fühlhörner ausstreckt und diesen Stamm mit demjenigen begabt, was die dreigeteilte Seele ist.",
      "# Bild s. 64",
      "Die Völker, die das noch empfunden haben, haben so gefühlt und auch gesprochen, auch in Kalewala, wie ich es auseinandergesetzt habe. Der moderne Mensch, der heute nur noch auf dem physischen Plane lebt, sagt, das westliche Meer erstreckt sich hier hinein; das ist der Bottnische, das ist der Finnische und das ist der Rigaische Meerbusen. Wir nehmen zusammen aber, indem wir das Geistige des äußeren Phy­sischen durchschauen wollen, dasjenige, was uns wie in einem Quer­schnitt von der Natur heraus erscheint, wir nehmen zusammen das Folgende. Da drunten ist noch viel Wasser, da drüben ist die Luft, der",
      "Mensch atmet Luft, und die Meereswelt da ist ein großes, mächtiges Wesen, das nur anders formiert ist, als wir es gewohnt sind. Das ist ein mächtiges Wesen, das sich darüber ausbreitet, und mit diesem Wesen stand der Mensch der früheren Rasse in einem ganz ausgesprochenen, bestimmt konfigurierten Zusammenhang. Und wenn wir jetzt sprechen von Volksgeistern, so haben diese Volksgeister in den Elementarwesen, die in zahlreichen solchen Seelenäußerungen leben, die Werkzeuge, um zu wirken. Sie organisieren sich gleichsam ein Heer, um zu wirken, um hineinzuwirken bis in den Ätherleib und vom Ätherleib aus den Men­schen so zu machen, daß sein physischer Leib ein Werkzeug ist für das­jenige, was er gerade für seine spezielle Mission auf der Erde sein soll.",
      "Nur dann, wenn wir die Formen, die uns in der Natur entgegen­treten, als Ausdruck von Geistigem ansehen können, verstehen wir die Natur selbst in ihrem Zusammenhange mit dem Menschen, wenn wir nicht so einfach gedankenlos hinblicken auf die Meeres- und Landes-grenzen, sondern verstehen, was sich in diesen Formen ausdrückt. Es könnte ja auch jemandem beim Gesicht des Menschen einfallen, zu",
      "# Bild s. 65",
      "sagen: Ja, es sind da solche Formen. Da grenzen Fleisch und Luft zu­sammen. - Wenn dieses jemand sagt, so wird man aber wenig verstan­den haben davon. Man hat das doch erst verstanden, wenn man es als",
      "Ausdruck des Menschen, als Gesicht auffaßt. So hat man das hier auch erst verstanden, wenn man es als eine gewisse Physiognomie eines mächtigen Wesens betrachtet, das aus dem Ozean heraus gewisse Teile seines Hauptkörpers vorstreckt, das diesen Teil seiner Physiognomie vorstreckt.",
      "Vieles geht eben wirklich unterhalb der Schwelle des Bewußtseins vor, und die Geister der Form haben die Formen in die Natur nicht umsonst hineingestellt. Diese Formen können verstanden werden. Sie sind der Ausdruck innerer Wesenheit. Und wenn wir die Schüler der Geister der Form werden, dann bilden wir selber Formen, welche aus­drücken, was in der inneren Wesenheit des Natürlichen und des Gei­stigen lebt.",
      "So sollten auch zum Beispiel in unseren Architraven, in dem, was über den Säulen ist, Formen gebildet werden, die wirklich der Aus­druck sind für diejenige Geistigkeit, die in Zusammenhang gebracht werden soll mit dem, was innerhalb des Baues geschehen soll. Der Mensch ist durchaus ein Wesen, welches gleichsam wie aus einem Meer heraustaucht mit seiner Oberfläche, aus einem Meer von Realität, von verborgener Realität, in das er eingetaucht ist.",
      "Sehen Sie, das ist wiederum ein Beispiel, wie wir eigentlich hinter die Maja dringen müssen, wenn wir das, was uns vorliegt in der Welt, wirklich verstehen wollen, namentlich wenn wir den Menschen ver­stehen wollen mit all seinen Äußerungen. Da müssen wir oft hinunter-gehen in das, was im Menschen lebt, ohne daß er es weiß, oder das er erst nach und nach lernt durch Vermittelung des Wissens.",
      "Wir können nämlich gar nicht anders, wenn wir irgendwohin den Blick wenden, ak daß wir zunächst auf die äußere Maja schauen, und dann müssen wir uns klar sein darüber, daß hinter dieser äußeren Maja etwas außerordentlich Kompliziertes liegt.",
      "Würden wir die Neigung haben, überall einzugehen auf dasjenige, was hinter der Maja liegt, dann würde es eine unendliche Harmonie, einen Zusammenklang geben können in der ganzen Menschenwesen­heit, denn gewissermaßen steht diese Menschenwesenheit durch un­endliche unterirdische Impulse mit einer harmonischen Einheitswesen­heit in Beziehung, und alles, was in der Welt vorhanden ist, kann nur",
      "verstanden werden, wenn man es in bezug auf das, was unter der Ober­fläche des Daseins liegt, prüft.",
      "Es bleibt immer eine Einseitigkeit, wenn man irgend etwas nur be­trachtet in bezug auf die Maja. Ich will hier etwas einschalten. Nicht wahr, solche Dinge, wie wir sie jetzt besprochen haben, kann man nur nach und nach ganz verstehen. Ich will zeigen, wie schon iin gewöhn­lichen Leben es schwer ist, auf alles das, was in den Dingen liegt, die an uns herantreten,wirklich einzugehen. So zum Beispiel werden vielleicht die wenigsten unserer lieben Freunde bemerkt haben, daß ich in einem Vortrage der letzten Zeit einmal intensiv über die Schweiz gesprochen habe, über etwas, was intensiv mit der schweizerischen Natur zusam­menhängt. Ich weiß nicht, in wieviel Gemütern jetzt eigentlich ein Be­wußtsein davon lebt, wovon ich spreche. Sie erinnern sich aber viel­leicht, daß ich an die vier Vorträge, die ich gehalten habe über okkultes Lesen und Hören, einen Vortrag angeschlossen habe, in dem ich rein äußerlich, geschichtlich, viel von Herman Grimm gesprochen habe. Das war ein Vortrag, in dem tatsächlich außerordentlich viel über die Schweiz gesprochen worden ist, aber man muß zurückgehen auf das Innere der Sache, auf das, was unter der Oberfläche liegt. Wieso denn?",
      "Sehen Sie, der Mensch - ich wiederhole etwas ganz Elementares -besteht, wie wir wissen, aus seinem physischen Leibe, seinem Äther-leibe, seinem Astralleibe und seiner Ich-Natur. Wir wissen, daß die Ich-Natur und der astralische Leib beim schlafenden Menschen den physischen und den Ätherleib verlassen und gleichsam sich außen, mehr in der geistigen Welt aufhalten, in einer Welt, von der wir sagen kön­nen also: In der Nacht sind wir darinnen in dieser Welt, wo auch die elementarischen, ätherischen Wesenheiten sind. - Da sind aber auch diejenigen geistigen elementarischen Wesenheiten darinnen, welche zu­sammenhängen mit dem ganzen Aufbau unseres physischen Seins. Die sind und wirken alle darinnen. Mit dem ganzen Aufbau unseres phy­sischen Seins hängt eine Anzahl von elementarischen Wesenheiten zu­sammen. Ich habe einmal aufmerksam gemacht in einem Vortrags-zyklus, den ich in Kassel gehalten habe über den Zusammenhang des Johannes-Evangeliums mit den andern Evangelien, wie der Mensch durch seine Vorfahren zusammenhängt mit den Wesenheiten der elementarischen",
      "Natur. Ich habe aufmerksam gemacht - Sie können es in diesem Vortragszyklus nachlesen -, daß der Mensch, wenn wir in dieser Weise seine vier Glieder anordnen, hier den physischen Leib, hier das Ich, hier den Ätherleib, hier den astralischen Leib hat, daß er dann ererbt hat dasjenige, was mehr in seinem physischen Leibe und seinem Ich lebt, von der väterlichen Seite her.",
      "# Bild s. 68",
      "Derjenige, welcher den Vortragszyklus aufmerksam gelesen hat, wird sich erinnern, daß das, was mehr im Ätherleibe und im astrali­schen Leibe lebt, von der mütterlichen Seite her vererbt wird. Wenn wir nun schlafen, so haben wir den physischen und den ätherischen Leib im Bette liegen, also etwas Väterliches und etwas Mütterliches. Wir haben aber das Ich und den astralischen Leib draußen. Der astra­lische Leib enthält dasjenige, was unseren Empfindungen, unserer gan­zen Temperamentsanlage sich einprägt, dasjenige, was uns den Seelen-charakter gibt. Und in dieses, was uns da den Seelencharakter gibt, wirken wiederum herein in der Zeitenfolge elementarische Wesen­heiten, Wesenheiten, die von den Vorfahren zu den Nachkommen hin­tragen die Kräfte, so daß diese Nachkommen in einer gewissen Weise werden.",
      "Bei einer solchen Persönlichkeit, wie Herman Grimm war, wirkt etwas ganz Eigentümliches. Man hat eine Nachwirkung bei Herman Grimm von dem, was seine unmittelbaren Vorfahren waren. Seine un­mittelbaren Vorfahren, sein Vater und sein Onkel, waren die Sammler der Kinder- und Hausmärchen, und diese Kinder- und Hausmärchen",
      "haben sie erzählen hören. Sie haben einfach hingehört, wenn man sie ihnen erzählt hat, und haben sie dann aufgeschrieben. Aber man tut so etwas nicht, wenn man nicht einen besonders zugerichteten astralischen Leib hat, der dazu veranlagt ist. Solche Dinge müssen tief begründet sein in dem ganzen Hergang der Sache.",
      "Ilerman Grimm hat eine gewisse Art, sich fein geistig auszudrücken, eine Art, die schon fast herankommt an das Geisteswissenschaftliche. Das ist dadurch in ihm enthalten, daß schon in seiner Vorfahrenschaft eine Hinneigung zum Märchenhaften war und zu demjenigen, worin Naturgeistigkeit lebt. Da sehen wir, wie die Naturgeister etwas in ihn hineinget?agen haben, was sie noch nachklingen ließen, wenn Herman Grimm mit seinem Ich und seinem Astralleibe außerhalb des physischen und Ätherleibes war. Wer hat denn dem Vater und dem Oheim zu­nächst in besonderer Anschaulichkeit - wie in einem Elementarwesen darinnen stehend - die Märchen erzählt? Die Frau des Vaters Herman Grimms, also die Mutter Herman Grimms. Die Mutter Herman Grimms war das belebende Element bei dieser Märchenübertragung. Sie hat eine besondere Freude gehabt, hinzuhorchen auf diese Märchen, wo sie im Volke lebten, und sie hat sie so aufgenommen, daß sie die beiden Brüder Grimm, Herman Grimms Vater und Oheim, aufschreiben konnten.",
      "Wer war diese Mutter? Dorothea Grimm, geborene Wild, war aus einem alten Berner Geschlecht. Sie selbst war noch Bürgerin dieser Stadt. Die Vorfahren hatten noch mitgekämpft in der Schlacht von Murten. Das ganze Gefühl, das sie da gewonnen hatte, mit all den Ele­mentargeistern, wurde dann ins Hessische hinaufgetragen, weil der Vater, der ausgewandert war von Bern, oder der Großvater von Her-man Grimm, das Apothekerhandwerk gelernt hatte, dann nach Kassel gezogen war und dort die Sonnenapotheke gegründet hatte. Wenn wir also suchen nach dem, was die Elementargeister wirkten gerade in Her-man Grimm, was sozusagen gerade die besondere Konfiguration dieses Geistes machte, weil sozusagen diese Geister, während er schlief, in ihm wirkten, dann müssen wir an die Schweiz denken, und wir reden eigent­lich, indem wir von dem Charakteristischen bei Herman Grimm spre­chen, von charakteristisch Bernerisch-Schweizerischem.",
      "So tritt uns manchmal, äußerlich ganz und gar von Maja überstrahlt,",
      "dasjenige entgegen, was das Wesentliche ist. Man horcht hin auf das, was das Wesen im Gemüte der Mutter Herman Grimms ist, wenn man das eigentümliche Gefüge seines Geistes in Betracht zieht, so daß ich eigentlich in dem Geistigen, in dem, was ich als unter der Schwelle des Bewußtseins liegend hervorgehoben habe, etwas unmittelbar Schwei­zerisches sagte und von dem Schweizerischen, speziell Bernerischen ge­sprochen habe, als ich von Herman Grimm sprach. Daher war voraus­zusetzen, daß gerade diese Art, von der da Andeutungen gemacht wor­den sind, unter manchen unserer Freunde recht vertraute, heimische Gefühle hervorgerufen haben wird.",
      "Es kommt also nicht bloß darauf an, was sozusagen äußerlich uns entgegentritt, sondern, was in dem lebt, was uns äußerlich entgegen­tritt. Die Erde mit allem, was auf ihr ist, ist tatsächlich im innigen Zu­sammenhange, die Erde als Einheitswesen ist tatsächlich im innigen Zusammenhange mit dem, was der Mensch auf ihr sein kann, mit dem, was auf dem Umwege durch den Ätherleib um den Menschen sich ge­staltet, figuriert.",
      "Nun gehen wir, nachdem ich durch das vorliegende Beispiel klar­gemacht habe, wie wir durch die Maja hindurchgehen müssen, wenn wir verstehen wollen, was da ist, nochmals zu dem Meeresdrachen zu­rück, der gleichsam der Inspirator der europäischen Menschheit ist, der sich vom Atlantischen Ozean herüberdrängte, um der Inspirator der europäischen Menschheit zu sein. Er enthält, wenn wir die Gesamtheit seiner elementarisch-ätherischen Wesenheiten ins Auge fassen, alles das­jenige, was geistig ist in der europäischen Menschheit. Würden wir ihn vollständig verstehen, diesen Drachen, würden wir uns ihm ganz hin­geben können, dann würden wir alle Hellseher sein. Aber die europä­ische Menschheit hat nicht die Aufgabe, etwa bloß hellsehend zu sein, sondern sie hat die Aufgabe, gerade denjenigen Teil des Seelenhaften zu entwickeln, der über das Hellsehen hinausragt, wie die Inseln aus dem Meere herausragen. Dasjenige, was nun ganz besonders sich ent­wickeln mußte als, ich möchte sagen, die Grundtypen der fünften nach-atlantischen Kulturperiode, mußte das Grundgepräge haben, sich her­auszuheben als Bewußtseinsnatur, sich herauszuheben aus dem bloß Seelenhaften. Das mußte inspiriert werden von den durch die Erde",
      "wirkenden Naturgeistern. Es mußte die Möglichkeit haben, überall zu­sammenzuhängen, gleichsam durch unzählige fließende Impulse zu­sammenzuhängen mit diesem inspirierenden Wesen. Aber es mußte sich herausheben, es mußte hineinschicken in das Wässerige das Erdenhafte. Und das ist dadurch geschehen, daß die britischen Inseln sich heraushoben mit der Summe aller ihrer Naturgeister aus dem sie ganz um­gebenden inspirierenden Meere.",
      "# Bild s. 71",
      "Wenn es einmal eine wirkliche Geisteswissenschaft geben wird, dann wird man wissen, daß auf einem solchen kontinentalen Gebiet des Men­schen Seelenträger, sein physischer und sein Ätherleib, sich so bilden müssen, wie das Verhältnis von Meer und Land das bedingt. Genauso wie die Hebung über das Meer, die Hebung des Landes über das Meer das bedingt, genau ebenso ist es, wie der Mensch in seiner Natur be­stimmte Räume dadurch ausfüllen muß, daß er sie nicht Muskeln sein läßt, sondern zu Knochen werden läßt, also so, daß das weiche Wesen und das harte Wesen ein bestimmtes Verhältnis zueinander haben.",
      "So gestaltet sich auch draußen in der großen Erdenmutter die Sache, und zwar so, daß aus dem flüssigen Elemente das feste Element auf­taucht. Man kann sagen: Die Erde schickt aus ihren Tiefen die elementarischen",
      "Geister herauf, welche die Erde bilden in bestimmter Kon­figuration, an einer bestimmten Stelle der geistigen Inspiration, damit ein solcher Boden entsteht, auf welchem solche Leiber wohnen können, in denen die Bewußtseinsseele sich entwickelt.",
      "Das feste Land im Meere ist wirklich wie ein Knochengerüst in der elementarischen Wesenheit. Geradeso wie unser Knochensystem im weichen Muskelsystem darinnen sitzt, so sitzt konfiguriert das Feste der Erde im Meere darinnen. Und die Länder entstehen nicht so regellos, wie es die Geologie darstellt, sondern entstehen in ihren Formen ebenso regelmäßig, wie in uns das Knochensystem regelmäßig entsteht, allerdings nicht durch Zellen gerade, wie sich die Knochen bilden. Wir müssen nur verstehen lernen, warum die einzelnen Kontinente in dieser oder jener Form gebildet sind. Ich möchte noch einen Vergleich ge­brauchen, der Sie nur nicht zu einem Mißverständnisse verführen soll. Ich möchte sagen: Damit hier bei diesem alten finnischen Volke jene Anschauung entstehen konnte, von der wir gesprochen haben, war es notwendig, daß eine solche Landkonfiguration entstand in den Meer-busen.",
      "Wie die menschliche Lunge hereinläßt die Luft, so sind in dieser Landkonfiguration vorgezeichnet - wie hineingenommen - Fangarme jenes großen Wesens, das zusammenhängt mit aller Konfiguration Eu­ropas.",
      "Wir haben nun das letzte Mal gesprochen von den Leibern, die der russischen Seele verliehen werden, wenn sich diese Seele in einem rus­sischen Leibe inkarniert. Wir haben gezeigt, das letzte Mal und auch im Verlaufe anderer Betrachtungen, daß in einem russischen Leibe die russische Seele sich erwartungsvoll bildet, daß sie dasjenige vorbildet in sich, was einmal ein Zukünftiges empfangen kann. Dazu ist not­wendig, daß diese Seele in einer gewissen Weise mit dem Geistigen in Beziehung bleibt. Sonst würde nicht das Geistselbst einmal gebildet werden können. Aber auf der andern Seite muß diese Seele verhindert werden, allzu früh sich in diejenigen Regionen zu entwickeln, die ihr eigentlich vorgebildet sind.",
      "Nehmen wir einmal an, es wäre hier - wo die Ostsee jetzt ist - Land und das hier - wo Rußland ist - wäre alles Meer. Es würden sich nur",
      "halbinselförmige Gebilde vorstrecken wie Italien und so weiter. Der Bottnische, Finnische, Rigaische Meerbusen würden bis zum Kaspischen Meer sich ausdehnen, statt daß wir russisches Land hier haben würden. Dann würden wir hier ein Seefahrervolk haben, daß diese Seezungen hier befahren würden. Dadurch würden sich aber die Leiber hier nicht bilden können, wie sie sich bilden sollen. Da würde jenes Wesen, wel­ches die Fangarme hier herüberstreckt, dasjenige ausatmen, was emp­fangen würden diese Seefahrer, und sie würden vorzeitig - also in zu früher Zeit - ihre Anlagen entfalten. Sie würden dasjenige, was auf eine spätere Zeit warten müßte, zu früh entfalten. Das Geistselbst muß eine gewisse Zeit warten, darf nicht zu früh entfaltet werden. Daher muß hier nicht Meer sein, sondern das Land muß so weit auftauchen, daß nicht zu früh das Geistselbst entwickelt werde, daß aber noch die Mög­lichkeit bleibt, die Inspirationen dieses großen Wesens zu empfangen. Es dürfen also nicht hohe Gebirge wie die Alpen vorhanden sein und auch nicht flache Länder, nur solche Erhebungen, daß nicht zu früh das Geistselbst empfangen wird. Gerade soviel Land muß es sein, um das Geistselbst zu erzeugen: also ausgedehnte, mehr flache Landgebiete. Wäre hier ein seefahrendes Volk, so würde dieses seefahrende Volk längst das Geistselbst entwickelt haben. Aber das wäre unreif, da würde zur Unzeit die Entwickelung eintreten.",
      "Und jetzt kommen wir auf den kosmischen Verstand der Erde. Die Erde hat kosmischen Verstand, der ihre Form bedingt, ihre Form so bedingt, daß sie überall aufwirft das Land so weit, als es nötig ist, da­mit die richtigen Elementargeister mit den auf der Erde befindlichen Wesen in Zusammenhang kommen, und andererseits das Wasser be­stehen läßt, so weit es nötig ist, damit die inspirierenden Genien wirken können.",
      "Wir bekommen den Eindruck, daß wir förmlich auf unsere Erde hinschauen und in einem solchen Aufwerfen von Land etwas Ähn­liches sehen können, wie wenn wir diese oder jene Miene im Gesichte bilden, wo auch das Seelische in der Miene in dieser oder jener Kon­figuration des Ausdruckes zum Vorschein kommt. Das Seelische der Erde tritt uns in der Konfiguration der Erde entgegen. Tatsächlich:",
      "sobald wir auf den menschlichen Ätherleib kommen, dehnt sich gleichsam",
      "diese Wesenheit des menschlichen Ätherleibes über die ganze Or­ganisation der Erde aus, und es steht überall im Zusammenhang der menschliche Ätherleib mit dem Organismus der Erde. Überall finden wir, daß das eigentlich Irdische - die Maja also für die Erdgeister - für den jetzigen Menschen zusammenhängt mit seiner Ich-Natur, mit der äußeren physischen Natur. Alles dasjenige, was Wasser und Luft -geistig betrachtet - ist, hängt zusammen mit dem, was er im Wider­spruch mit der Ich-Natur entwickelt. Denn die ganze Erde ist dazu da, um eben den irdischen Menschen zu bilden. Das andere besteht dar­innen, diesen irdischen Menschen zu nuancieren. Dieses Nuancieren wird eben durch das gegenseitige Verhältnis von Land und Wasser und Luft durch die Erde bewirkt.",
      "Wenn wir Europa im Süden anschauen und insbesondere die grie­chische und die italienische Halbinsel betrachten, so finden wir durch die Art, in der hier Land und Wasser verteilt sind, die Erde vorbereitet für solche Leiber, die gerade die vierte nachatlantische Kultur tragen konnten, in welcher die Verstandes- oder Gemütsseele so ganz beson­ders zum Ausdruck kommt.",
      "Wären die Länder im Süden Europas größer und die Meereinschnitte kleiner gewesen, so hätte in Griechenland und Italien etwas entstehen müssen, was erst später entstehen sollte, das heißt, es würde für die Evolution etwas in unbrauchbarer Weise entstanden sein. Damit in sol­cher Weise, wie ich es dargestellt habe, das griechische Wesen in dem romanischen Wesen seine Wiederholung hat finden können, mußte gegen die Meere hin eine breitere Landmasse vorgestreckt werden, als es bei Griechenland der Fall ist. Das ist aber in Frankreich der Fall. Und in dem Verhältnisse, von dem ich gesagt habe, wie es besteht zwi­schen Frankreich und Griechenland, können Sie genau ausgedrückt finden in der Physiognomie Griechenlands, wie es überall eingeschnit­ten ist von dem Meere, und in der Physiognomie Frankreichs, wie es mehr im großen seine Vorsprünge gegen das Meer vorstreckt.",
      "Ich wollte Ihnen heute einige Anhaltspunkte geben für allerlei Dinge, die noch weiter in unserem Zusammensein ausgeführt werden müssen. Zunächst werden wir auf diesen Anhaltspunkten dann morgen weiterbauen."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Wenn wir nur des Menschen physischen Leib betrachten, kommen wir sehr schwer zu solchen Erkenntnissen, wie diejenigen sind, von denen wir das letzte Mal gesprochen haben.",
        "Insbesondere gilt dieses für die­jenigen Völker, welche die Völker der neuen Welt, Europas und Ame­rikas, sind."
      ],
      [
        "Der physische Menschenleib in diesen Gebieten ist in weit geringe­rem Maße, als dies zum Beispiel in Asien und Afrika der Fall ist, von innen heraus gebildet.",
        "Bei den Völkerschaften Asiens und Afrikas ist der physische Leib mehr von innen heraus, von den im Ätherleibe lie­genden Kräften gebildet, formiert.",
        "Bei den Völkern Europas und Ame­rikas rührt der größere Einfluß in den Bildungs- und Formierungskräf­ten des physischen Leibes von den Einflüssen von außen her."
      ],
      [
        "Wir können etwa so sagen: Sobald wir nach den Kräften suchen, welche des Menschen physischen Leib bilden, formieren, müssen wir ätherische Kräfte finden.",
        "Diese ätherischen Kräfte liegen für die Be­wohner Afrikas und Asiens mehr im Inneren des eigenen Ätherleibes.",
        "Für die Bewohner Europas und Amerikas liegen sie mehr in der Äther­welt, die den Menschen von außen umgibt."
      ],
      [
        "Der Mensch Afrikas und Asiens steht also mehr mit den inneren Ätherkräften, der Mensch Europas und Amerikas mehr mit den äußeren Ätherkräften in Beziehung und dadurch mehr mit den Naturgeistern."
      ],
      [
        "Wenn ich mich primitiv ausdrücken, weniger auf das Rücksicht nehmen will, was uns klargeworden ist gerade durch die geisteswissen­schaftliche Betrachtung, so müßte ich sagen: Der physische Leib der afrikanischen und asiatischen Völker ist mehr von innen heraus, mehr durch innere Bildungskräfte geprägt.",
        "Der Leib der europäischen und amerikanischen Völker wird mehr durch die Hinwendung zu den Ver­hältnissen der Außenwelt geprägt.",
        "Die äußeren Kräfte drücken sich mehr in die plastischen Formen ein und bilden daher mehr die Formen des physischen Leibes."
      ],
      [
        "Ich habe in der Schrift «Die Schwelle der geistigen Welt» aufmerk­sam darauf gemacht, wie wir beim Menschen, sobald wir auf seinen Ätherleib Rücksicht nehmen, finden, daß er in einem größeren Maße, als man glauben könnte, wenn man das Auge bloß auf den physischen Leib richtet, mit dem ganzen Organismus der Erde in Beziehung steht.",
        "Die Erde selbst ist eine Art lebendiges Wesen.",
        "Aber, während uns der Mensch als lebendiges Wesen gewissermaßen wie eine abgeschlossene Einheit erscheint, so daß wir ihn auch als Einheit empfinden müssen, müssen wir die Erde als einen lebendigen Organismus so betrachten, daß wir in ihr ein Vielfaches von Naturwesen, die durcheinander-wirken, sehen."
      ],
      [
        "Zur Erde gehört zunächst die feste Erde selber, welche die Konti­nente bildet.",
        "Das, was wir aber als dieses Materielle, Feste der Erde an­sprechen, ist nichts anderes als Maja.",
        "Die Wirklichkeit ist eine große Summe von Naturgeistern, die wieder geführt werden von Geistern höherer Hierarchien.",
        "Daß sich das gleichsam zusammenballt und als feste Erde wirkt, ist Maja.",
        "Die Erde ist durch und durch Geist.",
        "Das ist oftmals betont worden."
      ],
      [
        "Nun gehört zur Erde nicht nur die feste Erde, sondern auch das, was als Gewässer die Erde durchsetzt, und insofern sich die Materie der Erde im Flüssigen auslebt, haben wir es wieder zu tun mit dem Wasser als der Maja.",
        "In Wirklichkeit aber haben wir es zu tun mit einer großen Anzahl von Naturgeistern.",
        "Ebenso ist es bei der Luft und ebenso bei der die Erde durchsetzenden und umspülenden Wärme.",
        "Das alles ist eine Summe von Naturgeistern, und das Materielle ist nur die äußere Maja."
      ],
      [
        "Mehr als das in Asien und Afrika der Fall ist, ist beim europäischen Menschen - beschränken wir uns darauf zunächst - gleichsam ein fort­währender Austausch der Impulse zwischen den inneren Ätherkräften und den Elementarwesen, welche in Feuer, Wasser, Luft und Erde ent­halten sind.",
        "Diese Elementarwesen wirken von außen herein auf die menschlichen Ätherleiber, und dadurch erhalten sie die formenden und bildenden Kräfte, die dann in dem Aussehen und den Verrichtungen des physischen Leibes bis in die Sprache hinein zum Vorschein kommen.",
        "Denn die Sprache ist durchaus auch eine Verrichtung des physischen Leibes.",
        "Aber selbstverständlich liegen die Impulse dazu im Ätherleibe."
      ],
      [
        "Nun, sehen Sie, muß man, wenn man den Menschen, so wie er auf der Erde lebt, wie er also auf dem Umwege über den Ätherleib ein Erdenwesen ist, der Erde angehört, darauf Rücksicht nehmen, in welch verschiedener Weise die einzelnen Wesenheiten der Erde, des Wassers, der Luft und so weiter auf den menschlichen Ätherleib wirken.",
        "Denn von ganz anderer Natur sind die elementarischen und ätherischen We­senheiten der Erde, von ganz anderer Natur die ätherischen und ele­mentarischen Wesenheiten des Wassers, so daß wir sagen können: Ein­fach dadurch, daß irgendein Mensch als physisches Wesen im Gebirge lebt oder am Meeresstrande, haben andere Wesenheiten auf seinen äthe­rischen Leib einen größeren Einfluß.",
        "Bei dem, der am Meeresstrande lebt, haben die elementarischen Wesenheiten, die ihren Majaausdruck im Wasser haben, einen viel größeren Einfluß als bei dem Menschen, der im Gebirge lebt.",
        "Bei einem Menschen, der im Gebirge lebt, haben die Wesen, die in der Erde leben, einen größeren Einfluß als die Wesen­heiten, die ihren Majaausdruck im Wasser haben."
      ],
      [
        "Nun wird dasjenige, was aus dem Menschen formiert, gemacht wird, durch dieses Zusammenwirken - ich rede jetzt immer hauptsächlich vom europäischen Menschen - der elementarischen Geister mitgewirkt, ich sage mitgewirkt, und in der Art, wie diese elementarischen Geister der Natur wirken, liegt etwas von dem, was aus der geistigen Welt her­aus den Menschen bildet, insofern dieser Mensch ein Erdenwesen ist."
      ],
      [
        "Ich habe Ihnen das letzte Mal davon gesprochen, daß der östlichen Kultur Europas voranging, sagen wir, eine Kulturschicht, deren Men-schen so beschaffen waren, daß sie in ihren Seelen noch etwas hatten von dem, was bei den heutigen Menschen mehr in das Unterbewußtsein zurückgedrängt ist, daß sie etwas im gewöhnlichen Leben hatten von einer Spaltung der Seele in Empfindungs-, Verstandes- oder Gemüts-und Bewußtseinsseele.",
        "Ich habe Sie darauf hingewiesen, daß das finni­sche Volk, das in alten Zeiten große finnische Volk - das heutige ist nur ein Rest eines einstmals ausgebreiteten finnischen Volkes -, eine solche Seele hatte, daß die Seelen dieser Menschen bei einem gewissen alten Hellsehen, das bei ihnen ausgebildet war, bei ihrem unmittelbaren Er-leben des Tages, etwas hatten von einer Spaltung der Seele in Empfin­dungs-, Verstandes- oder Gemüts- und Bewußtseinsseele."
      ],
      [
        "Ich habe Ihnen gesagt, daß in dem großartigen Epos Kalewala in den drei Figuren: Wäinämöinen, Ilmarinen und Lemminkäinen zum Ausdruck kommt die Darstellung, wie aus dem Kosmos herein diese dreigespaltene Seele bedingt wird, gleichsam gerichtet wird."
      ],
      [
        "Nun, wie konnte denn so etwas überhaupt zustande kommen?",
        "Wie konnte an einem bestimmten Punkte Europas - so stellen wir uns die Frage - ein großes Volk sich entwickeln, welches eine so geartete Seele hatte, wie ich es beschrieben habe?"
      ],
      [
        "Nun, sehen Sie, wie der Mensch sein eigentliches Ich, die Gabe der Erde, entwickelt, das rührt davon her, daß die Geister der Erde von unten herauf, durch die Maja der irdischen Materie auf ihn wirken.",
        "Von unten herauf, gleichsam durch die feste Erde hindurch, wirken die Geister der Erde, und in unserem Zyklus ist es so, daß diese Geister der Erde im wesentlichen dazu benutzt werden, um in dem Menschen die Ich-Natur hervorzurufen."
      ],
      [
        "Sollte nun in einem Volksstamme, wie es das alte finnische Volk war, in die Seele hereinleuchten etwas von dem, was gleichsam unter der Ich-Natur liegt, was geistiger ist als die Ich-Natur, was mehr zusam­menhängt mit den göttlichen Kräften - denn wenn die Seele sich drei-gespalten empfindet, hängt sie mehr zusammen mit den göttlichen Kräften, als wenn sie das nicht tut -, sollte so etwas entstehen, so durfte in einer gewissen Weise nicht bloß das Irdische mit seinen elementari­schen Geistern von unten herauf in das Irdische des Menschen strahlen, sondern es mußte etwas anderes in dieses Irdische hereinstrahlen, ein anderer elementarischer Einfluß."
      ],
      [
        "Ebenso nun wie des Menschen physisches Dasein innig zusammen­hängt mit den Geistern der Erde - physisches Dasein, insofern es ein irdisches Dasein ist, und es in ihm sein Ich entwickelt -, zusammen­hängt mit den Geistern, die von der Erde selber, von unten nach oben, wirken, so hängt zusammen das Seelische des Menschen, das sich wie natürliches, temperamenthaftes, charakterhaftes seelisches Dasein des Menschen bekundet, mit alledem, was als wässeriges Element, als flüs­siges Element auf der Erde lebt.",
        "Es müssen also Geister des wässerigen, des flüssigen Elementes hereinwirken in diese Seelen, die also drei-gespalten sind."
      ],
      [
        "Nun ist einmal für unseren Zeitenzyklus das irdische Element das Ich-bildende Element, also dasjenige, worauf es ankommt.",
        "Wenn ein anderes Element hereinragt, wie zum Beispiel das wässerige Element, so ragt dieses mehr aus der geistigen Welt herein.",
        "Es ist nicht in dem Menschen selber enthalten.",
        "Es muß sich gleichsam als ein geistiges We­sen in den Menschen hineinsenken, damit er hereinbekommt in seine irdische Natur etwas, was ihn in die geistige Welt hineinführt."
      ],
      [
        "Nehmen Sie an, die Fläche der Tafel wäre das, wo die elementari­schen Kräfte der Erde herauskommen, so muß, wenn ein geistiges Ele­ment sich da hineinsenken will, dies von dem Organismus der Erde selber ausgehen, von etwas, was an sich geistig ist.",
        "Ein Wesen muß da sein, ein wirkliches Wesen, das nicht der Mensch selber ist, das den Menschen gleichsam inspiriert zu der Dreigespaltenheit der Seele.",
        "Ein Wesen also muß da sein, das gleichsam so auf die Seele wirkt, aus der Naturgeistigkeit heraus wirkt, daß die Empfindungsseele, die Verstan­des- oder Gemütsseele und die Bewußtseinsseele sich auseinanderlegen, so daß die Seelen wirklich sagen können: Für meine Empfindungsseele wirkt da aus der Natur herein etwas, wie Wäinämöinen, das mir ent­gegenströmt wie ein Naturwesen, das mir die Kräfte der Empfindungs­seele gibt."
      ],
      [
        "Aber es wirkt auch etwas herein wie Ilmarinen, etwas, was mir die Kräfte der Verstandes- oder Gemütsseele gibt, und es wirkt ferner etwas herein wie Lemminkäinen, etwas, was mir die Kräfte der Be­wußtseinsseele gibt.",
        "Wenn da ein Wesen ist, das gleichsam seine Fühler in die Natur vorstreckt wie durch eine Art von Hals, wenn ein Wesen, das hier gleichsam seinen Hauptgruppenleib hat und hier seine Fühler ausstreckt, so daß wir den einen der Fühler mit der Empfindungsseele hier haben, und sich hier hereinstreckt das zweite Fühlhorn und hier das dritte Fühlhorn, so hat das Naturwesen einen Leib und streckt sein Seelisches gleichsam wie seelische Fühler da hinein, um zu inspirieren, und da können die Ätherleiber sich bilden, welche der Seele die Fähig­keit geben, sich dreigeteilt zu fühlen."
      ],
      [
        "Die alten Finnen, die Bevölkerung des alten Finnland, sagten: Wir leben hier, aber wir fühlen etwas wie drei gewaltige Wesen, die nicht Wesen des physischen Planes sind, die Naturwesen sind.",
        "Sie enthüllen"
      ],
      [
        "sich von Westen her, sie sind drei Teile, gleichsam Organe eines großen Wesens, das seinen Leib hat da drüben, aber es streckt uns seine Fühl­hörner hier entgegen: Wäinämöinen, Ilmarinen, Lemminkäinen.",
        "Ein mächtiges Meereswesen breitet sich von Westen nach Osten hin aus, das seine Fühlhörner ausstreckt und diesen Stamm mit demjenigen begabt, was die dreigeteilte Seele ist."
      ],
      [
        "# Bild s. 64"
      ],
      [
        "Die Völker, die das noch empfunden haben, haben so gefühlt und auch gesprochen, auch in Kalewala, wie ich es auseinandergesetzt habe.",
        "Der moderne Mensch, der heute nur noch auf dem physischen Plane lebt, sagt, das westliche Meer erstreckt sich hier hinein; das ist der Bottnische, das ist der Finnische und das ist der Rigaische Meerbusen.",
        "Wir nehmen zusammen aber, indem wir das Geistige des äußeren Phy­sischen durchschauen wollen, dasjenige, was uns wie in einem Quer­schnitt von der Natur heraus erscheint, wir nehmen zusammen das Folgende.",
        "Da drunten ist noch viel Wasser, da drüben ist die Luft, der"
      ],
      [
        "Mensch atmet Luft, und die Meereswelt da ist ein großes, mächtiges Wesen, das nur anders formiert ist, als wir es gewohnt sind.",
        "Das ist ein mächtiges Wesen, das sich darüber ausbreitet, und mit diesem Wesen stand der Mensch der früheren Rasse in einem ganz ausgesprochenen, bestimmt konfigurierten Zusammenhang.",
        "Und wenn wir jetzt sprechen von Volksgeistern, so haben diese Volksgeister in den Elementarwesen, die in zahlreichen solchen Seelenäußerungen leben, die Werkzeuge, um zu wirken.",
        "Sie organisieren sich gleichsam ein Heer, um zu wirken, um hineinzuwirken bis in den Ätherleib und vom Ätherleib aus den Men­schen so zu machen, daß sein physischer Leib ein Werkzeug ist für das­jenige, was er gerade für seine spezielle Mission auf der Erde sein soll."
      ],
      [
        "Nur dann, wenn wir die Formen, die uns in der Natur entgegen­treten, als Ausdruck von Geistigem ansehen können, verstehen wir die Natur selbst in ihrem Zusammenhange mit dem Menschen, wenn wir nicht so einfach gedankenlos hinblicken auf die Meeres- und Landes-grenzen, sondern verstehen, was sich in diesen Formen ausdrückt.",
        "Es könnte ja auch jemandem beim Gesicht des Menschen einfallen, zu"
      ],
      [
        "# Bild s. 65"
      ],
      [
        "sagen: Ja, es sind da solche Formen.",
        "Da grenzen Fleisch und Luft zu­sammen. - Wenn dieses jemand sagt, so wird man aber wenig verstan­den haben davon.",
        "Man hat das doch erst verstanden, wenn man es als"
      ],
      [
        "Ausdruck des Menschen, als Gesicht auffaßt.",
        "So hat man das hier auch erst verstanden, wenn man es als eine gewisse Physiognomie eines mächtigen Wesens betrachtet, das aus dem Ozean heraus gewisse Teile seines Hauptkörpers vorstreckt, das diesen Teil seiner Physiognomie vorstreckt."
      ],
      [
        "Vieles geht eben wirklich unterhalb der Schwelle des Bewußtseins vor, und die Geister der Form haben die Formen in die Natur nicht umsonst hineingestellt.",
        "Diese Formen können verstanden werden.",
        "Sie sind der Ausdruck innerer Wesenheit.",
        "Und wenn wir die Schüler der Geister der Form werden, dann bilden wir selber Formen, welche aus­drücken, was in der inneren Wesenheit des Natürlichen und des Gei­stigen lebt."
      ],
      [
        "So sollten auch zum Beispiel in unseren Architraven, in dem, was über den Säulen ist, Formen gebildet werden, die wirklich der Aus­druck sind für diejenige Geistigkeit, die in Zusammenhang gebracht werden soll mit dem, was innerhalb des Baues geschehen soll.",
        "Der Mensch ist durchaus ein Wesen, welches gleichsam wie aus einem Meer heraustaucht mit seiner Oberfläche, aus einem Meer von Realität, von verborgener Realität, in das er eingetaucht ist."
      ],
      [
        "Sehen Sie, das ist wiederum ein Beispiel, wie wir eigentlich hinter die Maja dringen müssen, wenn wir das, was uns vorliegt in der Welt, wirklich verstehen wollen, namentlich wenn wir den Menschen ver­stehen wollen mit all seinen Äußerungen.",
        "Da müssen wir oft hinunter-gehen in das, was im Menschen lebt, ohne daß er es weiß, oder das er erst nach und nach lernt durch Vermittelung des Wissens."
      ],
      [
        "Wir können nämlich gar nicht anders, wenn wir irgendwohin den Blick wenden, ak daß wir zunächst auf die äußere Maja schauen, und dann müssen wir uns klar sein darüber, daß hinter dieser äußeren Maja etwas außerordentlich Kompliziertes liegt."
      ],
      [
        "Würden wir die Neigung haben, überall einzugehen auf dasjenige, was hinter der Maja liegt, dann würde es eine unendliche Harmonie, einen Zusammenklang geben können in der ganzen Menschenwesen­heit, denn gewissermaßen steht diese Menschenwesenheit durch un­endliche unterirdische Impulse mit einer harmonischen Einheitswesen­heit in Beziehung, und alles, was in der Welt vorhanden ist, kann nur"
      ],
      [
        "verstanden werden, wenn man es in bezug auf das, was unter der Ober­fläche des Daseins liegt, prüft."
      ],
      [
        "Es bleibt immer eine Einseitigkeit, wenn man irgend etwas nur be­trachtet in bezug auf die Maja.",
        "Ich will hier etwas einschalten.",
        "Nicht wahr, solche Dinge, wie wir sie jetzt besprochen haben, kann man nur nach und nach ganz verstehen.",
        "Ich will zeigen, wie schon iin gewöhn­lichen Leben es schwer ist, auf alles das, was in den Dingen liegt, die an uns herantreten,wirklich einzugehen.",
        "So zum Beispiel werden vielleicht die wenigsten unserer lieben Freunde bemerkt haben, daß ich in einem Vortrage der letzten Zeit einmal intensiv über die Schweiz gesprochen habe, über etwas, was intensiv mit der schweizerischen Natur zusam­menhängt.",
        "Ich weiß nicht, in wieviel Gemütern jetzt eigentlich ein Be­wußtsein davon lebt, wovon ich spreche.",
        "Sie erinnern sich aber viel­leicht, daß ich an die vier Vorträge, die ich gehalten habe über okkultes Lesen und Hören, einen Vortrag angeschlossen habe, in dem ich rein äußerlich, geschichtlich, viel von Herman Grimm gesprochen habe.",
        "Das war ein Vortrag, in dem tatsächlich außerordentlich viel über die Schweiz gesprochen worden ist, aber man muß zurückgehen auf das Innere der Sache, auf das, was unter der Oberfläche liegt.",
        "Wieso denn?"
      ],
      [
        "Sehen Sie, der Mensch - ich wiederhole etwas ganz Elementares -besteht, wie wir wissen, aus seinem physischen Leibe, seinem Äther-leibe, seinem Astralleibe und seiner Ich-Natur.",
        "Wir wissen, daß die Ich-Natur und der astralische Leib beim schlafenden Menschen den physischen und den Ätherleib verlassen und gleichsam sich außen, mehr in der geistigen Welt aufhalten, in einer Welt, von der wir sagen kön­nen also: In der Nacht sind wir darinnen in dieser Welt, wo auch die elementarischen, ätherischen Wesenheiten sind. - Da sind aber auch diejenigen geistigen elementarischen Wesenheiten darinnen, welche zu­sammenhängen mit dem ganzen Aufbau unseres physischen Seins.",
        "Die sind und wirken alle darinnen.",
        "Mit dem ganzen Aufbau unseres phy­sischen Seins hängt eine Anzahl von elementarischen Wesenheiten zu­sammen.",
        "Ich habe einmal aufmerksam gemacht in einem Vortrags-zyklus, den ich in Kassel gehalten habe über den Zusammenhang des Johannes-Evangeliums mit den andern Evangelien, wie der Mensch durch seine Vorfahren zusammenhängt mit den Wesenheiten der elementarischen"
      ],
      [
        "Natur.",
        "Ich habe aufmerksam gemacht - Sie können es in diesem Vortragszyklus nachlesen -, daß der Mensch, wenn wir in dieser Weise seine vier Glieder anordnen, hier den physischen Leib, hier das Ich, hier den Ätherleib, hier den astralischen Leib hat, daß er dann ererbt hat dasjenige, was mehr in seinem physischen Leibe und seinem Ich lebt, von der väterlichen Seite her."
      ],
      [
        "# Bild s. 68"
      ],
      [
        "Derjenige, welcher den Vortragszyklus aufmerksam gelesen hat, wird sich erinnern, daß das, was mehr im Ätherleibe und im astrali­schen Leibe lebt, von der mütterlichen Seite her vererbt wird.",
        "Wenn wir nun schlafen, so haben wir den physischen und den ätherischen Leib im Bette liegen, also etwas Väterliches und etwas Mütterliches.",
        "Wir haben aber das Ich und den astralischen Leib draußen.",
        "Der astra­lische Leib enthält dasjenige, was unseren Empfindungen, unserer gan­zen Temperamentsanlage sich einprägt, dasjenige, was uns den Seelen-charakter gibt.",
        "Und in dieses, was uns da den Seelencharakter gibt, wirken wiederum herein in der Zeitenfolge elementarische Wesen­heiten, Wesenheiten, die von den Vorfahren zu den Nachkommen hin­tragen die Kräfte, so daß diese Nachkommen in einer gewissen Weise werden."
      ],
      [
        "Bei einer solchen Persönlichkeit, wie Herman Grimm war, wirkt etwas ganz Eigentümliches.",
        "Man hat eine Nachwirkung bei Herman Grimm von dem, was seine unmittelbaren Vorfahren waren.",
        "Seine un­mittelbaren Vorfahren, sein Vater und sein Onkel, waren die Sammler der Kinder- und Hausmärchen, und diese Kinder- und Hausmärchen"
      ],
      [
        "haben sie erzählen hören.",
        "Sie haben einfach hingehört, wenn man sie ihnen erzählt hat, und haben sie dann aufgeschrieben.",
        "Aber man tut so etwas nicht, wenn man nicht einen besonders zugerichteten astralischen Leib hat, der dazu veranlagt ist.",
        "Solche Dinge müssen tief begründet sein in dem ganzen Hergang der Sache."
      ],
      [
        "Ilerman Grimm hat eine gewisse Art, sich fein geistig auszudrücken, eine Art, die schon fast herankommt an das Geisteswissenschaftliche.",
        "Das ist dadurch in ihm enthalten, daß schon in seiner Vorfahrenschaft eine Hinneigung zum Märchenhaften war und zu demjenigen, worin Naturgeistigkeit lebt.",
        "Da sehen wir, wie die Naturgeister etwas in ihn hineinget?agen haben, was sie noch nachklingen ließen, wenn Herman Grimm mit seinem Ich und seinem Astralleibe außerhalb des physischen und Ätherleibes war.",
        "Wer hat denn dem Vater und dem Oheim zu­nächst in besonderer Anschaulichkeit - wie in einem Elementarwesen darinnen stehend - die Märchen erzählt?",
        "Die Frau des Vaters Herman Grimms, also die Mutter Herman Grimms.",
        "Die Mutter Herman Grimms war das belebende Element bei dieser Märchenübertragung.",
        "Sie hat eine besondere Freude gehabt, hinzuhorchen auf diese Märchen, wo sie im Volke lebten, und sie hat sie so aufgenommen, daß sie die beiden Brüder Grimm, Herman Grimms Vater und Oheim, aufschreiben konnten."
      ],
      [
        "Wer war diese Mutter?",
        "Dorothea Grimm, geborene Wild, war aus einem alten Berner Geschlecht.",
        "Sie selbst war noch Bürgerin dieser Stadt.",
        "Die Vorfahren hatten noch mitgekämpft in der Schlacht von Murten.",
        "Das ganze Gefühl, das sie da gewonnen hatte, mit all den Ele­mentargeistern, wurde dann ins Hessische hinaufgetragen, weil der Vater, der ausgewandert war von Bern, oder der Großvater von Her-man Grimm, das Apothekerhandwerk gelernt hatte, dann nach Kassel gezogen war und dort die Sonnenapotheke gegründet hatte.",
        "Wenn wir also suchen nach dem, was die Elementargeister wirkten gerade in Her-man Grimm, was sozusagen gerade die besondere Konfiguration dieses Geistes machte, weil sozusagen diese Geister, während er schlief, in ihm wirkten, dann müssen wir an die Schweiz denken, und wir reden eigent­lich, indem wir von dem Charakteristischen bei Herman Grimm spre­chen, von charakteristisch Bernerisch-Schweizerischem."
      ],
      [
        "So tritt uns manchmal, äußerlich ganz und gar von Maja überstrahlt,"
      ],
      [
        "dasjenige entgegen, was das Wesentliche ist.",
        "Man horcht hin auf das, was das Wesen im Gemüte der Mutter Herman Grimms ist, wenn man das eigentümliche Gefüge seines Geistes in Betracht zieht, so daß ich eigentlich in dem Geistigen, in dem, was ich als unter der Schwelle des Bewußtseins liegend hervorgehoben habe, etwas unmittelbar Schwei­zerisches sagte und von dem Schweizerischen, speziell Bernerischen ge­sprochen habe, als ich von Herman Grimm sprach.",
        "Daher war voraus­zusetzen, daß gerade diese Art, von der da Andeutungen gemacht wor­den sind, unter manchen unserer Freunde recht vertraute, heimische Gefühle hervorgerufen haben wird."
      ],
      [
        "Es kommt also nicht bloß darauf an, was sozusagen äußerlich uns entgegentritt, sondern, was in dem lebt, was uns äußerlich entgegen­tritt.",
        "Die Erde mit allem, was auf ihr ist, ist tatsächlich im innigen Zu­sammenhange, die Erde als Einheitswesen ist tatsächlich im innigen Zusammenhange mit dem, was der Mensch auf ihr sein kann, mit dem, was auf dem Umwege durch den Ätherleib um den Menschen sich ge­staltet, figuriert."
      ],
      [
        "Nun gehen wir, nachdem ich durch das vorliegende Beispiel klar­gemacht habe, wie wir durch die Maja hindurchgehen müssen, wenn wir verstehen wollen, was da ist, nochmals zu dem Meeresdrachen zu­rück, der gleichsam der Inspirator der europäischen Menschheit ist, der sich vom Atlantischen Ozean herüberdrängte, um der Inspirator der europäischen Menschheit zu sein.",
        "Er enthält, wenn wir die Gesamtheit seiner elementarisch-ätherischen Wesenheiten ins Auge fassen, alles das­jenige, was geistig ist in der europäischen Menschheit.",
        "Würden wir ihn vollständig verstehen, diesen Drachen, würden wir uns ihm ganz hin­geben können, dann würden wir alle Hellseher sein.",
        "Aber die europä­ische Menschheit hat nicht die Aufgabe, etwa bloß hellsehend zu sein, sondern sie hat die Aufgabe, gerade denjenigen Teil des Seelenhaften zu entwickeln, der über das Hellsehen hinausragt, wie die Inseln aus dem Meere herausragen.",
        "Dasjenige, was nun ganz besonders sich ent­wickeln mußte als, ich möchte sagen, die Grundtypen der fünften nach-atlantischen Kulturperiode, mußte das Grundgepräge haben, sich her­auszuheben als Bewußtseinsnatur, sich herauszuheben aus dem bloß Seelenhaften.",
        "Das mußte inspiriert werden von den durch die Erde"
      ],
      [
        "wirkenden Naturgeistern.",
        "Es mußte die Möglichkeit haben, überall zu­sammenzuhängen, gleichsam durch unzählige fließende Impulse zu­sammenzuhängen mit diesem inspirierenden Wesen.",
        "Aber es mußte sich herausheben, es mußte hineinschicken in das Wässerige das Erdenhafte.",
        "Und das ist dadurch geschehen, daß die britischen Inseln sich heraushoben mit der Summe aller ihrer Naturgeister aus dem sie ganz um­gebenden inspirierenden Meere."
      ],
      [
        "# Bild s. 71"
      ],
      [
        "Wenn es einmal eine wirkliche Geisteswissenschaft geben wird, dann wird man wissen, daß auf einem solchen kontinentalen Gebiet des Men­schen Seelenträger, sein physischer und sein Ätherleib, sich so bilden müssen, wie das Verhältnis von Meer und Land das bedingt.",
        "Genauso wie die Hebung über das Meer, die Hebung des Landes über das Meer das bedingt, genau ebenso ist es, wie der Mensch in seiner Natur be­stimmte Räume dadurch ausfüllen muß, daß er sie nicht Muskeln sein läßt, sondern zu Knochen werden läßt, also so, daß das weiche Wesen und das harte Wesen ein bestimmtes Verhältnis zueinander haben."
      ],
      [
        "So gestaltet sich auch draußen in der großen Erdenmutter die Sache, und zwar so, daß aus dem flüssigen Elemente das feste Element auf­taucht.",
        "Man kann sagen: Die Erde schickt aus ihren Tiefen die elementarischen"
      ],
      [
        "Geister herauf, welche die Erde bilden in bestimmter Kon­figuration, an einer bestimmten Stelle der geistigen Inspiration, damit ein solcher Boden entsteht, auf welchem solche Leiber wohnen können, in denen die Bewußtseinsseele sich entwickelt."
      ],
      [
        "Das feste Land im Meere ist wirklich wie ein Knochengerüst in der elementarischen Wesenheit.",
        "Geradeso wie unser Knochensystem im weichen Muskelsystem darinnen sitzt, so sitzt konfiguriert das Feste der Erde im Meere darinnen.",
        "Und die Länder entstehen nicht so regellos, wie es die Geologie darstellt, sondern entstehen in ihren Formen ebenso regelmäßig, wie in uns das Knochensystem regelmäßig entsteht, allerdings nicht durch Zellen gerade, wie sich die Knochen bilden.",
        "Wir müssen nur verstehen lernen, warum die einzelnen Kontinente in dieser oder jener Form gebildet sind.",
        "Ich möchte noch einen Vergleich ge­brauchen, der Sie nur nicht zu einem Mißverständnisse verführen soll.",
        "Ich möchte sagen: Damit hier bei diesem alten finnischen Volke jene Anschauung entstehen konnte, von der wir gesprochen haben, war es notwendig, daß eine solche Landkonfiguration entstand in den Meer-busen."
      ],
      [
        "Wie die menschliche Lunge hereinläßt die Luft, so sind in dieser Landkonfiguration vorgezeichnet - wie hineingenommen - Fangarme jenes großen Wesens, das zusammenhängt mit aller Konfiguration Eu­ropas."
      ],
      [
        "Wir haben nun das letzte Mal gesprochen von den Leibern, die der russischen Seele verliehen werden, wenn sich diese Seele in einem rus­sischen Leibe inkarniert.",
        "Wir haben gezeigt, das letzte Mal und auch im Verlaufe anderer Betrachtungen, daß in einem russischen Leibe die russische Seele sich erwartungsvoll bildet, daß sie dasjenige vorbildet in sich, was einmal ein Zukünftiges empfangen kann.",
        "Dazu ist not­wendig, daß diese Seele in einer gewissen Weise mit dem Geistigen in Beziehung bleibt.",
        "Sonst würde nicht das Geistselbst einmal gebildet werden können.",
        "Aber auf der andern Seite muß diese Seele verhindert werden, allzu früh sich in diejenigen Regionen zu entwickeln, die ihr eigentlich vorgebildet sind."
      ],
      [
        "Nehmen wir einmal an, es wäre hier - wo die Ostsee jetzt ist - Land und das hier - wo Rußland ist - wäre alles Meer.",
        "Es würden sich nur"
      ],
      [
        "halbinselförmige Gebilde vorstrecken wie Italien und so weiter.",
        "Der Bottnische, Finnische, Rigaische Meerbusen würden bis zum Kaspischen Meer sich ausdehnen, statt daß wir russisches Land hier haben würden.",
        "Dann würden wir hier ein Seefahrervolk haben, daß diese Seezungen hier befahren würden.",
        "Dadurch würden sich aber die Leiber hier nicht bilden können, wie sie sich bilden sollen.",
        "Da würde jenes Wesen, wel­ches die Fangarme hier herüberstreckt, dasjenige ausatmen, was emp­fangen würden diese Seefahrer, und sie würden vorzeitig - also in zu früher Zeit - ihre Anlagen entfalten.",
        "Sie würden dasjenige, was auf eine spätere Zeit warten müßte, zu früh entfalten.",
        "Das Geistselbst muß eine gewisse Zeit warten, darf nicht zu früh entfaltet werden.",
        "Daher muß hier nicht Meer sein, sondern das Land muß so weit auftauchen, daß nicht zu früh das Geistselbst entwickelt werde, daß aber noch die Mög­lichkeit bleibt, die Inspirationen dieses großen Wesens zu empfangen.",
        "Es dürfen also nicht hohe Gebirge wie die Alpen vorhanden sein und auch nicht flache Länder, nur solche Erhebungen, daß nicht zu früh das Geistselbst empfangen wird.",
        "Gerade soviel Land muß es sein, um das Geistselbst zu erzeugen: also ausgedehnte, mehr flache Landgebiete.",
        "Wäre hier ein seefahrendes Volk, so würde dieses seefahrende Volk längst das Geistselbst entwickelt haben.",
        "Aber das wäre unreif, da würde zur Unzeit die Entwickelung eintreten."
      ],
      [
        "Und jetzt kommen wir auf den kosmischen Verstand der Erde.",
        "Die Erde hat kosmischen Verstand, der ihre Form bedingt, ihre Form so bedingt, daß sie überall aufwirft das Land so weit, als es nötig ist, da­mit die richtigen Elementargeister mit den auf der Erde befindlichen Wesen in Zusammenhang kommen, und andererseits das Wasser be­stehen läßt, so weit es nötig ist, damit die inspirierenden Genien wirken können."
      ],
      [
        "Wir bekommen den Eindruck, daß wir förmlich auf unsere Erde hinschauen und in einem solchen Aufwerfen von Land etwas Ähn­liches sehen können, wie wenn wir diese oder jene Miene im Gesichte bilden, wo auch das Seelische in der Miene in dieser oder jener Kon­figuration des Ausdruckes zum Vorschein kommt.",
        "Das Seelische der Erde tritt uns in der Konfiguration der Erde entgegen.",
        "Tatsächlich:"
      ],
      [
        "sobald wir auf den menschlichen Ätherleib kommen, dehnt sich gleichsam"
      ],
      [
        "diese Wesenheit des menschlichen Ätherleibes über die ganze Or­ganisation der Erde aus, und es steht überall im Zusammenhang der menschliche Ätherleib mit dem Organismus der Erde.",
        "Überall finden wir, daß das eigentlich Irdische - die Maja also für die Erdgeister - für den jetzigen Menschen zusammenhängt mit seiner Ich-Natur, mit der äußeren physischen Natur.",
        "Alles dasjenige, was Wasser und Luft -geistig betrachtet - ist, hängt zusammen mit dem, was er im Wider­spruch mit der Ich-Natur entwickelt.",
        "Denn die ganze Erde ist dazu da, um eben den irdischen Menschen zu bilden.",
        "Das andere besteht dar­innen, diesen irdischen Menschen zu nuancieren.",
        "Dieses Nuancieren wird eben durch das gegenseitige Verhältnis von Land und Wasser und Luft durch die Erde bewirkt."
      ],
      [
        "Wenn wir Europa im Süden anschauen und insbesondere die grie­chische und die italienische Halbinsel betrachten, so finden wir durch die Art, in der hier Land und Wasser verteilt sind, die Erde vorbereitet für solche Leiber, die gerade die vierte nachatlantische Kultur tragen konnten, in welcher die Verstandes- oder Gemütsseele so ganz beson­ders zum Ausdruck kommt."
      ],
      [
        "Wären die Länder im Süden Europas größer und die Meereinschnitte kleiner gewesen, so hätte in Griechenland und Italien etwas entstehen müssen, was erst später entstehen sollte, das heißt, es würde für die Evolution etwas in unbrauchbarer Weise entstanden sein.",
        "Damit in sol­cher Weise, wie ich es dargestellt habe, das griechische Wesen in dem romanischen Wesen seine Wiederholung hat finden können, mußte gegen die Meere hin eine breitere Landmasse vorgestreckt werden, als es bei Griechenland der Fall ist.",
        "Das ist aber in Frankreich der Fall.",
        "Und in dem Verhältnisse, von dem ich gesagt habe, wie es besteht zwi­schen Frankreich und Griechenland, können Sie genau ausgedrückt finden in der Physiognomie Griechenlands, wie es überall eingeschnit­ten ist von dem Meere, und in der Physiognomie Frankreichs, wie es mehr im großen seine Vorsprünge gegen das Meer vorstreckt."
      ],
      [
        "Ich wollte Ihnen heute einige Anhaltspunkte geben für allerlei Dinge, die noch weiter in unserem Zusammensein ausgeführt werden müssen.",
        "Zunächst werden wir auf diesen Anhaltspunkten dann morgen weiterbauen."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "DRITTER VORTRAG Dornach, 15. November 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Inwiefern die Erde selbst ein Inspirator ist für die Menschen, die auf der Erde leben, davon haben wir gestern wenigstens in einigen Andeu­tungen gesprochen, denn nur Andeutungen können selbstverständlich in einem Gebiete gegeben werden, das so umfassend wie nur irgend möglich ist.",
      "Wichtig, bedeutungsvoll ist es gerade in unserer Zeit, sich bewußt zu werden, daß solche Zusammenhänge existieren, wie die sind, von denen wir gesprochen haben, denn der Mensch innerhalb der Erdenentwicke­lung ist gerade in unserer Gegenwart auf dem Punkte, sich gewisser­maßen wieder zu emanzipieren von diesem Erdeinfluß, gewissermaßen wiederum sich durchdringen zu lassen von denjenigen Einflüssen, die nicht aus der Erdenwelt, sondern aus der die Erde umgebenden geisti­gen Welt kommen.",
      "Dieses Bestreben, gleichsam in die menschlichen Fähigkeiten, in das menschliche Denken und Empfinden hereinzubekommen dasjenige, was nicht bloß irdisch ist, liegt zugrunde unserem geisteswissenschaftlichen Streben. Nach diesem geisteswissenschaftlichen Bestreben geht wirklich alle Tendenz der modernen Bildung hin, und man darf wohl sagen, zwei Dinge sind es, die immer mehr und mehr dem Menschen der Ge­genwart zum Bewußtsein kommen müssen.",
      "Das eine ist, daß der Mensch in bezug auf seine eigene seelische We­senheit einer Welt angehört, die sich nicht für die äußeren Sinne ent­hüllt, sondern die erst hinter der äußeren Sinneswelt liegt, daß der Mensch einer solchen Welt angehört mit seinem innersten Seelenwesen, zu der man weder durch Sinnesbeobachtung kommen kann noch auch durch Schlüsse und die Logik, die sich auf die Sinnesbeobachtung grün­den. Es wird die Aufgabe unserer Zeit sein, über diesen Punkt sich Klarheit zu verschaffen, daß alles Wissen, welches die äußeren Sinne vermitteln und ihre Philosophie, die sich nur gründet auf das äußere Sinneswissen, nicht herankommen können an dasjenige, was die mensch­liche Seele eigentlich ist.",
      "Das zweite ist eine Wahrheit, die Ihnen aus Ihrem geisteswissen­schaftlichen Leben heraus geläufig ist, von der Sie aber wissen, daß sie dem allgemeinen Bewußtsein der Gegenwart noch ganz fern steht. Es ist die wichtige Wahrheit von den wiederholten Erdenleben, davon, daß des Menschen Seele sich nicht erschöpft in dem Leibe, in dem sie lebt zwischen Geburt und Tod, in alledem, was mit diesem Leibe zu­sammenhängt, sondern daß sie von Leben zu Leben geht.",
      "Weil diese beiden Wahrheiten, daß die Seele einer Welt angehört, die hinter der Sinneswelt liegt, und daß sie von Leben zu Leben geht, zu den allerwichtigsten für unsere Zeit gehören, die zunächst begriffen werden müssen, deshalb habe ich im zweiten Bande meiner «Rätsel der Philosophie» ein Kapitel angefügt, in dem aus dem Entwickelungsgang der Menschheit selber gerade auf diese beiden Wahrheiten in intensiver Weise hingedeutet wird, denn das ist ein dringendes Erfordernis unserer Zeit, daß immer mehr und mehr Menschen gerade diese beiden Wahr­heiten begreifen lernen.",
      "Da dieses Buch «Die Rätsel der Philosophie» ein solches ist, das sich nicht speziell an Anthroposophen wendet, sondern an alle Menschen, die lesen und Gelesenes verstehen können, so mußte versucht wer­den, in Kürze, aber so scharf als möglich, auf diese beiden Wahrheiten hinzudeuten. Man darf sagen, es liegt im tieferen Bewußtsein der Menschen der neueren Zeit, nach diesen Wahrheiten hin ihre Gedan­ken zu richten. Ich will zunächst nur sagen, ihre Gedanken zu richten. Wir können überall solche Tendenzen, die Gedanken nach diesen Wahrheiten zu richten, bemerken. Ich habe manchmal versucht, aus der neuen Geistesgeschichte Menschen anzuführen, welche nach sol­chen Wahrheiten hin tendieren. Ich möchte heute noch ein Beispiel an­führen.",
      "Einer der größten Geister des 19. Jahrhunderts ist ohne Zweifel Emerson, der so bedeutsam eindringlich,wenn auch nicht in pedantisch­philosophischer Sprache, so doch in einer eindringlichen Sprache ge­schrieben hat. Emerson weist überall, ob er über die Natur spricht oder über das Menschengeschlecht, darauf hin, daß das äußere Gefüge der Welt, welches der Mensch mit seinen Sinnen überschaut und mit dem Verstande begreift, nur die Hülle, die Phantasmagorie ist, und daß man",
      "zu der Wahrheit nur kommt, wenn man hinter die Phantasmagorie versucht einzudringen.",
      "Aber solche Geister wie Emerson gehen noch weiter. Und davon möchte ich ein Beispiel geben. Emerson hat unter seinen sehr bedeut­samen Büchern auch eines geschrieben, welches heißt «Die Repräsen­tanten des Menschengeschlechtes». In diesem Buche hat er behandelt Plato als Repräsentanten alles philosophischen Menschheitsstrebens; Swedenborg als Repräsentanten des mystischen Menschheitsstrebens; Montaigne, einen bedeutsamen Geist des 16.Jahrhunderts, als Reprä­sentanten des Skeptizismus; Shakespeare als Repräsentanten des dich­terischen Vermögens; Goethe als Repräsentanten des schriftstellerischen Vermögens und Napoleon als den Tatenmenschen, als den Repräsen­tanten des Menschen der Tat.",
      "Mit diesem Buche ist allerdings etwas Bedeutsames getan. Es sind herausgehoben die Typen des Menschentums in bezug auf das Seelen-leben. Es würde eine interessante Betrachtung abgeben, wenn man be­leuchten würde, wie in der Tat das Repräsentative des philosophischen Strebens in Plato, das Repräsentative des skeptischen Strebens in Mon­taigne getroffen ist. Dieses Buch bedeutet eine der größten Taten des geistigen Menschheitsstrebens. Nun widmet Emerson merkwürdiger­weise Montaigne, ich möchte sagen, eine ganz besonders liebevolle Dar­stellung, obwohl gerade diese liebevolle Darstellung einem erst ent­gegentritt, wenn man sich gründlich genug auf dieses Kapitel über Montaigne einläßt. Das ist auch wieder sehr bedeutungsvoll für das Hintendieren Emersons zur geisteswissenschaftlichen Weltauffassung. Derjenige, der sich auf diese Weltauffassung im Ernste einläßt, wird gewahr, wie wirklich jedes Ding zwei Seiten hat, wie, wenn man ver­sucht, eine Wahrheit auszusprechen, man nur etwas Einseitiges sagen kann, und die zweite Seite gleichsam im Hintergrunde lauern muß.",
      "Der Skeptiker, der ein lebendiges Gefühl dafür hat, daß man ge­wissermaßen schon ein Unrecht tut, wenn man eine Wahrheit strikt formuliert, ist im tiefsten Sinne berührt von dem geistig-seelischen Fluidum, das in der Menschenseele immer da ist und das einen ver­hindert, sobald man nur von der geistigen Welt berührt ist, mit allzu­viel Aplomb eine scharf konturierte Wahrheit hinzustellen, ohne darauf",
      "hinzuweisen, daß in gewissem Sinne auch das Gegenteil davon eine Berechtigung hat.",
      "Dieses in gewissem Sinne Berührtsein von einem Gefühle, das aus der Geistigkeit herauskommt, macht Montaigne zu einer bedeutenden Persönlichkeit. Aber das ist es nicht, worauf ich hinweisen wollte. Hin­weisen wollte ich auf das, wie Emerson erzählt, wie er auf Montaigne gekommen ist. Er sagt da: Schon als Knabe fand ich einen Band von Montaigne in der Bibliothek meines Vaters, den ich aber nicht ver­stand. - Als er dann die Hochschule absolviert hatte, sah er sich das Buch noch einmal an, und da bekam er den merkwürdigen Drang, Satz für Satz kennenzulernen von dem, was Montaigne geschrieben hat. Und das tat er, diesem Drange folgend. Nun sehen wir in dem Kapitel über Montaigne, welches Emerson schrieb, daß er nach einem Ausdruck da­für suchte, warum er plötzlich damals wie besessen war von Montaigne und plötzlich anfing, ihn ganz in sich aufzunehmen. Da findet er keinen besseren Ausdruck dafür, als daß er sagt: Es war mir so, als wenn ich diese Bücher von Montaigne in einem früheren Leben selber geschrieben hätte. - Daraus ersehen Sie, wie ein im eminentesten Sinne moderner Geist, der an das herandringt, was Forderung der Gegenwart ist, da, wo er sich über das Intimste in seiner Seele ausdrücken will, gezwungen ist, sich einen Ausdruck zu bilden, der ganz nach der geisteswissen­schaftlichen Wahrheit der Reinkarnation hin tendiert. Er findet keinen besseren Ausdruck und muß daher die Idee der wiederholten Erden-leben zu Hilfe nehmen.",
      "So etwas ist außerordentlich charakteristisch, ist ungeheuer bedeu­tungsvoll, und dies führt uns nun dahin, anzuknüpfen an den Gedan­ken, der gestern ausgeführt worden ist. Sehen wir uns gerade die vor­nehmsten Geister unserer Zeit an - und einer der vornehmsten ist Emerson -, so haben Sie auf der einen Seite, wenn sie so bedeutende Geister sind wie Emerson, das Erdenwissen, das sie übernommen haben, insofern sie hineingestellt sind in den Evolutionsprozeß der Erde. Das wissen sie, was man heute aufnimmt als Mensch. Sie wissen, daß man, wenn man an einen gewissen Punkt der Erde gesetzt ist, eine bestimmte Sprache spricht und so weiter, daß es üblich ist, an dem Orte, wo man hinversetzt ist, dem Kinde, dem jungen Menschen diese Dinge zu überliefern",
      "und so dasjenige, was man Bildung nennt, an den Menschen her-anzubringen. Dieses Wissen, das einem Volke auf diese Weise über­liefert wird, ist ein Wissen eines großen Umkreises. Man darf schon sagen, daß das ein Wissen eines großen Umkreises ist, das kann man sagen, wenn man sieht, wie Emerson eigentlich vorgeht.",
      "Wir wissen, daß bei ihm, wenn er einen Vortrag zu halten hatte, es so erschien, als ob das, was er sagte, unmittelbar, während er es sagte, aus seinem Geiste hervorsprühte. Wie improvisiert erschien alles. Wenn er besucht wurde an einem Tage, wo er einen Vortrag halten sollte, konnten die Besucher sehen, daß im ganzen Zimmer alle möglichen Notizen herumlagen, aus denen er zusammengeholt hatte dasjenige, was er sozusagen über das Äußere seines Stoffes zu sagen hatte. Aber hinter dem, was er so der Menschheit überlieferte, lagen Intimitäten, und die­ses ist eben eine Intimität, was ich ausgesprochen habe, daß durch­schimmert die Idee der wiederholten Erdenleben ganz keusch an einer Stelle.",
      "Man kann sehen, wie sogar die Besten unserer Zeit, indem sie solche Wahrheiten in der Seele durchempfinden, durchfühlen und auch aus­sprechen, keusch in sich selbst bleiben, diese Wahrheiten noch nicht hereintragen wollen in das Gebiet, dem das äußere Wissen entspringt.",
      "Wenn wir nun geisteswissenschaftlich an die Sache herangehen, so müssen wir sie noch anders beleuchten, denn unsere Zeit ist einmal die­jenige, deren Mission es ist, das, was bisher in der Seele zurückgehalten und nur zuweilen angedeutet worden ist, zur Klarheit, zur wirklichen Erkenntnis zu bringen, in Wissensformen zu prägen, so daß unsere Zeit wirklich die Aufgabe hat, manches, was bis zu dieser unserer Zeit sich wie herausdrängt aus den Seelen der Besten, zur vollen Klarheit, zu einer für die Menschen selbstverständlichen Wahrheit zu machen. Und da können wir ganz genau beschreiben, wie es war, wenn Emerson in seinen gehaltreichen Vorträgen bald einen Satz sagte, der eine Erkennt­nis ausdrückte über das industrielle Leben seiner Umgebung und dann wenige Zeilen später etwas bringt, was von dem alten Indien handelt, und dann wieder etwas, was von Shakespeare handelt. So trägt er sozu­sagen das Erdenwissen zusammen und dann entschlüpft ihm oft eine Bemerkung so mittenhinein, die aus dem Intimen seiner Seele kommt.",
      "Woher kommt denn das, was in einer solchen Bemerkung liegt? Das kann man sich nur beantworten,wenn man alle Seiten der menschlichen Natur in Betracht zieht. Der Mensch erkennt in der Erdenzeit nur das wenigste, nur ein Stück seines Lebens, das sich abspielt vom Aufwachen bis zum Einschlafen. Der andere Teil des Lebens wird verbracht im Schlafe, und dieser Teil des Menschenlebens ist recht, recht mannig­faltig.",
      "Es ist einmal wahr, daß für viele, viele Menschen dieses Leben im Schlafe so verläuft, daß sie da in Berührung kommen mit elementari­schen Weltenwesenheiten, die mit niedrigeren Äußerungen der mensch­lichen Natur zusammenhängen, als die Tagesäußerungen sind. Man möchte sagen, die Menschen treiben vom Einschlafen bis zum Auf­wachen, also im Bereiche elementarischen Lebens, des Nachtlebens, allerlei Allotria, Dinge, über die sie hinaus sind, wenn sie im äußeren Leben stehen. Wer wüßte nicht, daß er sich oft seiner Träume schämen muß. Das ist eine allgemeine Erfahrung, die jeder machen kann. Der Mensch treibt also während des Schlafes allerlei Allotria, in einer Ge­sellschaft, die nicht etwa eine gute ist, die sich vielmehr wendet an seine Leidenschaften, seine Triebe, die viel schlechter ist als die, in welcher er während seines Wachlebens erzogen ist.",
      "Nur wenn man das versteht, versteht man manches besser, was sich geschichtlich ereignet hat. Der heutige Mensch muß, damit er nicht all­zu stark Allotria auch im physischen Leben treibt, schon einmal mit der Gabe ausgestattet sein, daß er nicht allzu großen Wert auf die Träume legt. Er vergißt seine Träume daher sehr leicht, vergißt die Allotria aus den Träumen, und das ist gut für ihn, denn er soll vor­bereitet werden dazu, im Wachbewußtsein einzutreten in die geistige Welt, während die Vorzeit dazu da war, den Menschen während des Schlafens bis zum Aufwachen in diese geistige Welt eintreten zu lassen.",
      "Im Grunde genommen liegt ein stärkeres Bewußtsein von dieser Welt noch gar nicht so weit hinter uns, wie man gewöhnlich glaubt. Auch dafür will ich Ihnen ein Beispiel geben. Es gibt ein Bild von Albrecht Dürer, das vielen Leuten, namentlich aber den Gelehrten, viele Rätsel aufgegeben hat. Die Radierung hat ungefähr das zum In­halt, daß eine satyrhafte, faunenhafte Gestalt da ist, die gleichsam umschlungen",
      "hält ein weibliches Wesen. Aus dem Hintergrunde erscheint ein anderes weibliches Wesen, welches sich wie strafend diesem Paare nähert. Und eine lierkulesartige männliche Gestalt steht in der Nähe, die eine Keule in der Hand hält, welche das strafende weibliche Wesen von der Gruppe des Weibes mit dem Satyr zurückhält, so daß sie nicht heran kann.",
      "Es ist, man möchte sagen, ganz merkwürdig, äußerst merk­würdig, wie sich die Gelehrten abgemüht haben, dieses Bild zu ver­stehen. Man nennt es gewöhnlich «Herkules». Aber das, was damit aus­gedrückt ist, gibt es nicht in der gewöhnlichen Herkules-Sage.",
      "Man frägt sich daher: Wie ist Albrecht Dürer zu dieser Szene gekommen? -Und da sind die kuriosesten Ideen aufgestellt worden. Man kann sehen zum Beispiel bei Herman Grimm, wie hilflos er diesem Bilde gegen­über ist.",
      "Er weiß nichts damit anzufangen. Er stellt die kuriosesten Ideen auf. Und warum geschieht das? Warum wissen die Menschen nichts damit anzufangen? Weil er und die Gelehrten nicht wissen - was Albrecht Dürer noch wußte -, daß die Menschen im Schlafe noch ein­dringen können in eine geistige Welt.",
      "Heute ist dieses Bewußtsein ver­lorengegangen. Dürer wußte aber noch, daß es zum Beispiel Männer gibt, welche während der Schlafenszeit in Gemeinschaft mit der ele­mentaren Welt allerlei Allotria treiben, Männer, die während der ge­wöhnlichen Zeit ganz gesittete Männer sind, aber während der Schla­fenszeit in die Triebwelt zurückfallen und allerlei unnütze Dinge, aller­lei Allotria treiben.",
      "In dem Bilde des Albrecht Dürer sehen wir den Satyr und den Her­kules mit der Keule. Der gute Herkules, der dasteht, möchte gern selber dieser Satyr sein. Aber er lebt in der physischen Welt, in einer sittlichen Welt auf dem physischen Plan, und das gestattet ihm die Gattin nicht. Die kommt daher und will ihn wegtreiben. Ihm aber gefällt das doch, und er hält sie zurück.",
      "Wir sehen hier einen inneren Seelenprozeß und wissen, daß Albrecht Dürer noch etwas von diesen Dingen wußte. So ist vieles in der Kunst gar nicht so weit zurückliegender Jahrhunderte zu erklären, weil da­mals noch ein Bewußtsein des Zusammenhanges des Menschen mit der unmittelbar an das Physische anstoßenden geistig-elementaren Welt vorhanden war.",
      "Aber wenn wir den Blick wenden auf solche vornehme Geister, wie Emerson einer war, so müssen wir sagen, sie treiben während ihres Schlaflebens keine Allotria, sondern eben Vornehmes. Wenn sie so mit ihrem Ich und mit dem astralischen Leibe in der geistigen Welt sind, kommen sie mit den Wahrheiten in Beziehung, was in der Menschheit wahrhafte Anthroposophie sein soll. Da drängt sich in ihr Bewußtsein, was künftiges physisches Wissen werden soll. Man könnte sagen, Emer­son empfängt so etwas im Schlafe. Daher stellt es sich so keusch, intim in dasjenige hinein, was er mit den physischen Sinnen und dem Ver­stande, überblickend das weite Erdenleben, über das physische Leben zu sagen hat.",
      "Nun würde es nicht gehen im Sinne der Evolution der Menschheit, daß es einfach dabei bliebe, daß die Menschen nur so, ich möchte sagen, in ihrem Schlafleben erfassen, was da hinter dem Sinnenschein, hinter der Sinnesphantasmagorie liegt. Denn das ist wieder der Sinn der Evo­lution, daß das Schlafleben immer mehr und mehr bei der Erkenntnis an Bedeutung verliert. Man muß schon ein bedeutender Geist sein wie Emerson, wenn man sich aus dem Schlafleben heraus so etwas erobern will wie die Idee der wiederholten Erdenleben. Das aber, was geistig ist, muß in die Menschheit kommen, muß in der Menschheit Einzug halten. So, wie im Zusammenhange mit dem innersten menschlichen Seelenleben diese Wahrheiten sind, wie sie sich da gleichsam wie in einer Art von Morgenröte verkündigen gerade bei solchen Geistern wie Emerson, muß auf der andern Seite wieder eine irdische Veranlagung da sein, solche Wahrheiten im hellen Wachbewußtsein zu verstehen. Es muß die irdische Veranlagung vorhanden sein, sich selber so zu emp­finden, daß man es natürlich findet, diese Wahrheiten anzuerkennen. Daß das noch nicht natürlich ist in der Gegenwart, begreifen Sie, denn wir sind als Geisteswissenschafter noch ein so kleines Häuflein, und alle, die außerhalb des geisteswissenschaftlichen Strebens stehen, sehen uns als Narren oder etwas Ähnliches an.",
      "Es liegt nicht in der modernen Bildung, diese Wahrheiten unmittel­bar anzuerkennen. Das natürliche Temperament des Menschen spricht dagegen. Was die Leute Logisches vorbringen gegen die Geisteswissen­schaft, ist in der Regel außerordentlich minderwertig, denn aus logischen",
      "Gründen sträuben sich die Menschen nicht; sie sträuben sich, weil sie ihrer Natur nach durch alles, was sie durch die Kräfte der Erde sind, nicht veranlagt sind im allgemeinen, solche Wahrheiten heute schon aufzunehmen.",
      "Aber es muß eine Zeit kommen, in der des Menschen Natur so kon­stituiert sein wird, daß er unmittelbar diese Wahrheiten einsehen kann, so wie er heute die mathematischen Wahrheiten einsehen kann. Der Mensch muß naturhaft so organisiert werden, daß er diese Wahrheiten einsehen kann. Dazu ist notwendig, daß er für die Zeit, die verläuft zwischen der Geburt und dem Tode, auch physisch so konstituiert ist, daß sein Gehirn so durchgebildet ist, daß er diese Wahrheiten einsehen kann.",
      "Im Sinne der gestrigen Auseinandersetzung gesprochen, muß ein sol­ches Verhältnis hergestellt werden zwischen den Geistern, die in der Erde wirken, und den Menschen, daß die Menschen so konstituiert wer-den, daß sie diese Wahrheiten aufnehmen können, und das geschieht auf die Weise, daß eine Land fläche, wie ich das gestern gezeigt und auf­gezeichnet habe, sich herüberneigt von Osten nach Westen gegen die drei Meerbusen, von denen ich gestern gesprochen habe. Diese Landes-fläche ist äußerlich nur eine Phantasmagorie Diese Landesfläche ist in Wirklichkeit zusammengesetzt aus den Geistern der Erde.",
      "In Wirklich­keit ist es so, daß die Geister dieser Landesfläche wirken auf die Men­schen und sie physisch bilden so, daß sie die Wahrheiten von der geistig-seelischen Konstitution des Menschen und den wiederholten Erden-leben einsehen. Was, ich möchte sagen, mehr westliche Geister wie aus dem Schlafe heraus sich erobern müssen, das wird im Wachen eine mehr selbstverständliche Wahrheit werden müssen bei denjenigen, die sich vom Osten herüber zuneigen der Evolution der Menschheit.",
      "Die Erde bereitet zu ihre Leiber, möchte man sagen, zu dem, was sie für die Evo­lution brauchen. Diese Erde ist durchaus dasjenige, was ich gestern aus­einandergesetzt habe: ein weit umgreifender Organismus, der beseelt ist und der aus seinem Seelenleben heraus von Zeit zu Zeit die Erden-geister ausschickt, welche die Leiber so durchorganisieren, daß sie in entsprechender Weise in die Evolution eingreifen können.",
      "Sehen Sie, diese Dinge sind außerordentlich tief und bedeutsam, und",
      "man muß sich schon auf solche Dinge einlassen, wenn man verstehen will, um was es sich da handelt. Wenn man allerdings die Erde als einen beseelten und durchgeistigten Organismus vergleicht mit dem, was der Mensch ist als durchseelter und durchgeistigter Organismus, so gibt es einen großen Unterschied. Der Mensch steht durch das Äußere seines physischen Leibes, in dem er eigentlich für gewöhnlich gar nicht darin lebt, aber in dem er darinnensteckt, in Beziehung zu den eigentlichen Geistern der Erde. Durch den Ätherleib steht er in Beziehung zu den Geistern deswassers; durch den Astralleib in Beziehung zu den Geistern der Luft, und durch seine Verbindung mit dem Ich steht er in Beziehung zu den Geistern des Feuers.",
      "Wenn der Mensch im Schlafe den physischen Leib und ätherischen Leib verläßt, dann lebt er mit seinem Ich und dem Astralleibe nur in Beziehung zu der die Erde durchwogenden Wärme und der die Erde durchflutenden und durchhauchenden Luft. Er ist herausgerissen aus alledem, was Erde und Wasser im physischen Leib konfigurieren. Da ist der Mensch wirklich herausgerissen, wenn er schläft, aus alledem, was, ich möchte sagen, der physische und Ätherleib als Erdenwesen machen. Natürlich gehören die Luft und dieWärme auch zur Erde, aber nur zur Erde, nicht zu den Teilen der Erde. Nun ist für den Menschen als beseeltes, durchgeistigtes Wesen die Wärme gewissermaßen das­jenige, in dem er sich aufhält wie in seinem eigenen Elemente. Bei den höheren Tieren ist schon eine Vorbereitung dazu vorhanden. Sie haben Eigenwärme, nicht bloß die Wärme ihrer Umgebung. Sie leben in ihrem Seelischen, in ihrer Eigenwärme. Der Mensch hat das insbesondere aus­gebildet, daß er in seiner Eigenwärme lebt, daß er seine eigene Tem­peratur hat. Das ist etwas, was ihn abschließt von dem, was in der Außenwelt so verschiedenartig ist. Die Wärme ist gleichsam etwas, wo­von jeder Mensch sein Quantum in sich trägt und es mit sich trägt. Da ist er in seinem eigentlichen Ich darinnen, da ist er zu Hause in der Wärme.",
      "In der Luft lebt er schon weniger allgemein darinnen. Ich möchte sagen, da übt schon die Differenzierung der Erde einen gewissen Ein­fluß auf ihn aus. Ob er in Höhenluft, Wasserluft oder Landluft lebt, das macht schon einen gewissen Unterschied. Da kommt der Mensch in",
      "Beziehung zu dem, was von außen auf ihn wirkt. So ist es bei dem Men­schen als einem durchseelten und durchgeistigten Organismus.",
      "Das Umgekehrte ist bei der Erde als durchseeltem, durchgeistigtem Organismus der Fall. Was für den Menschen die Wärme ist, das ist für die Erde eben die Erde, das feste Irdische, und die Wärme ist für sie das Äußerlichste, was zu der beseelten Erde ein Verhältnis hat wie zu uns die Erde.",
      "Die Erde ist Erde durch und durch, wie wir durch und durch Wärme sind. Die Erde ist nach außen differenziert in bezug auf die Wärme. Je nachdem sie in die Eisregionen ihre Glieder erstreckt oder in die schwüle Region der Tropen, öffnet sie nach außen hin ihr See­lisches so nach der Wärme, wie wir in bezug auf unseren physischen Leib hinneigen nach der Gegend, in der wir gerade wohnen.",
      "Es ist bei der Erde gerade das Entgegengesetzte wie beim Menschen, und darauf beruht das Zusammenwirken der Erde als beseelter und geistiger Orga­nismus mit dem Menschen als beseeltem und geistigem Organismus. Durch dieses Zusammenwirken entsteht dann dasjenige, was im phy­sischen Menschenleibe zustande kommt, damit dieser physische Men­schenleib in der Nacheinanderfolge der Nationen und Völker in rich­tiger Weise in die Evolution des ganzen Erdendaseins eintritt.",
      "Wir haben gerade in den Völkern, welche als Völkermassen von Osten nach Westen herüberrückten, ein intensives Verhältnis des Irdischen zu dem Menschlichen. Und man könnte dieses intensive Verhältnis so aus­sprechen, wie wenn man in der Erde selber sehen würde ein mächtiges Wesen, und dieses mächtige Wesen würde sich entschließen, in die Evo­lution in entsprechender Weise einzugreifen, sagen wir vom 20.",
      "Jahr­hundert ab. Da muß es sich sagen: Ich muß gewisse geistigewesenheiten hinauflenken nach meiner Oberfläche, ich muß sie tätig sein lassen so,",
      "# Bild s. 85",
      "daß sie physische Leiber zubereiten, damit die physischen Leiber durch das Gehirn die Wahrheiten aufnehmen können, die in dieser Zeit der Evolution der Menschheit frommen.",
      "Wie ein Gedanke, den die Erde hat, ist dasjenige, was ich eben aus­gesprochen habe. Man erfaßt diesen Gedanken nur, wenn man ihn in der richtigen Frömmigkeit und Ehrerbietung erfaßt, wenn man ihn nicht nimmt wie die Gedanken der äußeren Wissenschaft, sondern wenn man ihn betrachtet wie etwas Heiliges, wie etwas, das man nicht ohne Ehrerbietung aussprechen kann, weil man erinnert wird an den Zusammenhang des Menschen mit der geistigen Welt, weil man un­mittelbar darinnensteht in dem Verkehr des Menschlichen mit dem Göttlichen, wo solche Dinge ausgesprochen werden. Daher sollte auch überall darauf geachtet werden, daß die nötige Atmosphäre des Füh­lens und Empfindens da sein sollte, wo solche Dinge ausgesprochen werden. Das ist ungeheuer wichtig bei solchen Dingen. Man möchte sagen: In einem gewissen Sinne dürfen solche Dinge nicht anders aus­gesprochen werden, als daß ihnen das Gefühl, die Stimmung des Gebet­artigen zugrunde liegt. Ein Aufschauen zu den geistigen Welten muß durchpulsen dasjenige, was wir so durchdenken, indem wir uns solchen Gedanken nähern. - Und daß dies auf eine naturgemäße Weise ge­schehen kann, schon durch das äußere Milieu, dazu wird unser Bau aufgeführt, und dazu wird alles das gemacht, was darin zum Vorschein kommen soll.",
      "So sehen wir in dem, was ich eben dargestellt habe, eine Art Beispiel, wie die Erde als Erde durch das, was in ihrem festen Elemente enthal­ten ist, geistig wirkt, wie sie dasjenige schafft und schöpft, was auf ihr in der Evolution lebt.",
      "Gehen wir dagegen mehr nach Westen herüber, so haben wir andere Verhältnisse. Ich habe Ihnen gestern ein Verhältnis auseinandergesetzt, wo der Westen mit dem Osten zusammenwirkt, wo sich das flüssige Element wie ein mächtiges Wesen herüberneigt nach dem Osten und die dreigeteilte Seelennatur ausdrückend sich herüberneigt in den drei großen Meerbusen, die noch die spirituell veranlagten Völker des alten Finnland als Wäinämöinen, Ilmarinen und Lemminkäinen empfanden, und die man heute so prosaisch als Finnischen, Bottnischen und Rigaischen",
      "Meerbusen bezeichnet. Da wirkte zusammen in dem alten finni­schen Volk dasjenige, was aus dem flüssigen und dasjenige, was aus dem festen Elemente kommt. In dem finnischen Volke vereinigte sich das Element, das mehr den ätherischen Menschen konstituiert und den physischen Menschen verfeinert, das Flüssige, und das Element der Erde, das, was aus der Erde herauskommt, was den physischen Men­schen konstituiert.",
      "Es kann die Frage aufgeworfen werden, welche Bedeutung ein sol­ches Volk hat, das eine solche eminente Mission im Verlaufe der Erden-mission vollzogen hat wie das große finnische Volk, und das doch noch bleibt für die spätere Zeit. Das hat alles seine Bedeutung in dem ganzen Fortschritt der Evolution, daß ein solches Volk dableibt, daß es nicht verschwindet von der Erde, wenn es seine Mission vollzogen hat. So wie der Mensch selber die Gedanken, welche er in einem bestimmten Lebensalter gefaßt hat, für ein späteres Lebensalter im lebendigen Ge­dächtnisse behält, so müssen auch frühere Völker bleiben wie ein Ge­wissen, wie ein lebendig fortwirkendes Gedächtnis gegenüber dem, was in späterer Zeit geschieht: wie ein Gewissen.",
      "Und nun könnte man sagen: Des europäischen Ostens Gewissen wird dasjenige sein, was das finnische Volk bewahrt hat. - Es muß eine Zeit kommen, wenn ein Verständnis die Herzen ergreifen soll für die Aufgaben der Evolution, wo gerade aus der Mitte des finnischen Vol­kes heraus ein Aufblühen der Ideen von Kalewala stattfinden wird, wo durchgeistigt und durchsetzt werden wird mit den modernen geistes­wissenschaftlichen Ideen dieses wunderbare Epos von Kalewala, wo es in seiner Tiefe dem ganzen Europäertum wiederum zum Bewußtsein gebracht werden wird.",
      "Die europäischen Völker verehrten die homerischen Epen. Allein aus noch tieferen Gründen des Seelenlebens heraus floß das Epos Kale­wala. Nur kann man das noch nicht einsehen heute. Das wird man aber, wenn man die Lehren der Geisteswissenschaft in entsprechender Weise verwenden wird für die Erklärung geistiger Erscheinungen der Erdenevolution. Ein solches Epos wie Kalewala kann nicht erhalten werden, ohne daß es im lebendigen Dasein erhalten wird, ohne die See­len, welche im Leibe wohnen, welche verwandt sind mit den Schöpferkräften",
      "von Kalewala. Als lebendiges Gewissen bleibt es. Dadurch kann es fortwirken, dadurch daß nicht die Worte, sondern daß das, was in ihm selber gelebt hat, weiterlebt, daß ein Zentrum da ist, von dem es ausstrahlen kann. Darauf kommt es an, daß dieses da ist, wie die Gedanken, die wir früher gehabt haben, da sind im späteren Lebens­alter.",
      "Im Westen ist mehr dasjenige, was den ätherischen Leib formiert und gestaltet. Es sind dies schwierige Wahrheiten, und Sie müssen sich schon daran gewöhnen, weil ich nicht die Möglichkeit habe, die man hoffent­lich aber einmal haben wird in der Erdenevolution, die Möglichkeit, die Dinge, die ich in einer Stunde auseinandersetzen muß, in einem ganzen Jahre auseinanderzusetzen, Sie müssen sich darauf einlassen, vieles durch Ihre Gedanken zu ergänzen, das Gesagte meditativ zu durch­denken. Dann wird es Ihnen voll geläufig werden. Namentlich ver­suchen Sie nicht, mit diesen oder jenen voreiligen Empfindungsnuancen an die Dinge heranzukommen.",
      "Im Westen ist mehr eine Wirkung auf den ätherischen Leib vor­handen, der da in derselben Weise, aber in früherer Zeit, als es für den Osten mit dem physischen Leib geschehen muß, geformt, gebildet wer­den mußte.",
      "Sehen Sie, man kann in solchen Dingen sich sehr leicht Mißver­ständnissen hingeben, denn die Unterschiede sind fein, sehr subtil. Wenn man zum Beispiel im Westen sieht, daß es bei den Völkern dar­auf ankommt, daß der ätherische Leib mehr von den Geistern des Was­sers gebildet worden ist, so ist es selbstverständlich - weil der physische Leib ein Abdruck davon ist -, daß auch der physische Leib als Abdruck des Ätherleibes damit gebildet worden ist, aus den Kräften des Wassers heraus. Aber es kommt darauf an, daß im Osten die Kräfte direkt mehr in den physischen Leib hineinwirken. Man muß also sein Augenmerk auf dasjenige richten, auf das es ankommt. Die äußere physische Wis­senschaft kann diesen feinen Unterschied nicht machen. Sie sieht, daß der östliche physische Leib so konfiguriert ist und der westliche phy­sische Leib anders. Mehr sieht sie nicht. Erst die Geisteswissenschaft kann auf solche Unterschiede näher eingehen. Außerdem ist die Sprache so ungeschickt und sehr wenig geeignet, solche Unterschiede auszudrücken.",
      "Wenn man ganz etwas Verschiedenes sagt, hat man oft den Eindruck, man sage eigentlich das Gleiche. Gestern habe ich zum Bei­spiel sagen müssen, daß bei den asiatischen Völkern es darauf ankomme, daß die Kräfte, die den physischen Leib aufbauen, im eigenen Äther­leib liegen. Heute muß ich sagen, daß es von den Völkern des Westens darauf ankommt, daß der Ätherleib geformt wird aus den Kräften des Wassers. Wenn Sie das Ganze zusammennehmen, werden Sie verstehen, daß in den alten Zeiten es der Fall gewesen ist, daß bei den östlichen Völkern Europas der Ätherleib geformt werden mußte, aber es ist heute, jetzt, die Zeit, wo der physische Leib geformt werden muß, während bei den westlichen Völkern der Fall so ist, daß ihr Ätherleib geformt wird, nachdem ihr physischer Leib schon das Gepräge mehr von außen erhalten hat, daß ihr Ätherleib unmittelbar den Genien des Meeres, den Genien des Wassers ausgesetzt wird.",
      "Bei den Völkern des Westens kommt das, was sie sind, dadurch zu­stande, daß die Impulse in den Ätherleib hineingehen. Da, wo die Im­pulse mehr in den Ätherleib hineingehen, kommt es weniger auf das Räumliche, sondern mehr auf das Zeitliche an. Wie in der Aufeinander­folge der Zeit die Impulse wirken, darauf kommt es mehr an.",
      "Wenn wir nach dem Osten hinüberschauen, sehen wir, wie gleich­sam die Gedanken aus der Erde herausquillen, um den Menschen vor­zubereiten zur zukünftigen Evolution. Wenn wir nach dem Westen schauen, so sehen wir aus dem Flüssigen herausquellen die Gedanken, die Kräfte, welche die Ätherleiber formen in der Aufeinanderfolge der Zeit.",
      "Und da sehen wir, wie geformt wurde schon in den alten Zeiten im Westen bis weit nach Mitteleuropa herein an dem Ätherleibe des Men­schen, so geformt wurde, daß dieser Ätherleib sein unmittelbares Leben leibhaft, lebendig, äußerlich auslebt.",
      "Was heißt das? Das heißt, meine lieben Freunde, es lebten in alten Zeiten in Europas Westen Menschen, welche ihre Lebensart so aus dem Ätherleibe heraus zutage brachten, wie jetzt, wo der Ätherleib schon gewirkt hat mit diesen alten Impulsen, der Mensch aus dem physischen Leibe heraus wirkt. Menschen lebten, die noch einen lebendigen Um­gang hatten mit der geistigen Welt, namentlich mit der elementarischen",
      "Welt. Das gehört den alten Zeiten an. Diese Zeiten sind gewissermaßen schon vorüber, wo in der allerlebendigsten Weise die Genien des flüs­sigen Elementes zum Ätherleibe des Menschen im Westen sprachen. Wenn aber zu diesem Ätherleibe gesprochen wird, ist es anders als in unserer Zeit, wo vorzugsweise zum physischen Leibe des Menschen ge­sprochen wird. Zum physischen Leibe des Menschen wird so gespro­chen, daß auf seine Sinne Eindruck gemacht wird, daß er sich ein Wis­sen aneignet und gewisse Lebensgewohnheiten annimmt, die mit den Eindrücken der Sinne zusammenhängen.",
      "Bei diesen alten Menschen des Westens war es so, daß sie in ihren Lebensgewohnheiten, in dem, was innerlich in ihnen lebte, noch mehr mit der elementarischenWelt zusammenhingen. Bei den Kelten hat man solche Menschen, die geradeso wußten von der elementarischen Welt, wie wir heute wissen von der physischen Welt, Menschen, denen die elementarische Welt nicht verschlossen war, die von Naturgenien, von Wassergenien, von Erdengenien reden konnten, wie wir von den Bäu­men, Pflanzen, Bergen, Wolken reden, die unmittelbaren Umgang hat­ten mit diesen Naturgenien. Und die Eigenart des Lebens in Europa beruht darauf, daß das eben in der alten Zeit so gewesen ist, weil da­mals so, wie man heute durch die Sinne auf den physischen Leib wirkt, gewirkt wurde auf den ätherischen Leib des Menschen.",
      "Dann wurde weiter gewirkt allerdings gerade auf den ätherischen Leib des Menschen, aber daß dieser ätherische Leib so formiert, gebil­det wird, daß das Verhältnis der Genien des Flüssigen zu ihm sich mehr im Unterbewußtsein abspielt, daß mehr zurücktritt der bewußte Ver­kehr mit den Naturgeistern.",
      "Wodurch kam das zustande? Für Frankreich zum Beispiel kam das zustande dadurch, daß über die Welle der keltischen Entwickelung sich die Welle der romanischen Entwickelung zog, daß das keltische Ele­ment von dem romanischen durchsetzt wurde. In dem Zusammenfluß des Keltischen mit dem Romanischen haben wir zwei Impulse. Einen alten Impuls, der unmittelbar den Verkehr vermittelt zwischen der elementarischen Welt und dem Ätherleibe, und in dem neuen Impuls, in dem Einfluß des Romanischen haben wir dasjenige, was auch in den Ätherleib einzieht, aber so einzieht, daß es wie eine historische, eine",
      "geschichtliche Welle ist, so daß das eintreten konnte, was ich in den früheren Vorträgen schon gesagt habe, daß in dem französischen Elemente ein Aufleben des alten griechischen Elementes stattfinden konnte.",
      "Will man diese westliche Menschenart richtig verstehen, so muß man diese verschiedenen Impulse, die auch in den Ätherleib einfließen, in der richtigen Weise taxieren. Und nun haben wir gewissermaßen von charakteristischen Erscheinungen in bezug auf die Einflüsse auf den physischen Leib und in bezug auf die Einflüsse auf den ätherischen Leib gesprochen. Anders stehen die Sachen, wenn wir die mittlere Re­gion ins Auge fassen. Da liegen die Sachen etwas anders. Da haben wir es zu tun mit etwas, ich möchte sagen, viel Unausgesprochenerem, mit etwas, was sich weniger deutlich charakterisieren läßt. Da haben wir es zu tun damit, daß sowohl Geister der Erde wie Geister des flüssigen Elementes unmittelbar auf den physischen Leib einwirken.",
      "Sie sehen, es ist ein Übergang. Hier, im Westen, wirken unmittelbar Geister des flüssigen Elementes auf den Ätherleib. Die Geister des flüs­sigen Elementes lassen nach, in Mitteleuropa, und es gesellen sich zu ihnen gewisse Geister des irdischen Elementes. Sie wirken auf den phy­sischen Leib unmittelbar; weniger stark auf den Ätherleib. Die Geister des irdischen Elementes verfeinern den physischen Leib, wenn Sie wei­ter nach Osten gehen. Daher haben wir irgendwie mit Mitteleuropa zusammenhängend all dasjenige, was Europa durch lange Zeit mit sol­chen physischen Leibern versorgt, die zugänglich sind dem flüssigen Elemente und dem festen Elemente, und daher sehen wir, wie sich kom­plizieren muß dasjenige, was in die Menschheitsevolution einfließt. Wir sehen, wie aus diesem Fonds, diesem Reservoir, das Volk der Franken, vorbereitet, wie ich es geschildert habe, durch die Genien des Flüssigen und des Festen, sich wieder hineinschiebt in das keltisch-romanische Volkselement; und dann erst entsteht dasjenige, was uns entgegen­getreten ist als das Wirksame in der Menschheitsevolution.",
      "Die Franken, die zurückbleiben, behalten damit die Eigentümlich­keit, die Eigenschaft, vorzugsweise in dem physischen Leibe dasjenige aufzunehmen - die Sachsen sind damit verwandt -, was von den flüs­sigen und irdischen Geistern ausgeht. Die Franken, die nach dem Westen",
      "zogen, vereinigten ihr Wesen mit demjenigen Wesen, das aus dem un­mittelbaren Einfluß der Genien des Meeres kommt, was dadurch noch bedeutsamer wird, daß es aufnimmt das Historische des romanischen Elementes.",
      "So schieben sich die Impulse ineinander und so können wir begrei­fen, wie, vor allen Dingen wenn wir Westeuropa charakterisieren wol­len, wir gar nicht anders zu einem Verständnis kommen, als wenn wir Rücksicht auf alles dasjenige nehmen, was in den ätherischen Leib ein­greift.",
      "Wenn wir Mitteleuropa charakterisieren wollen, so müssen wir sagen, da kommt es mehr auf den physischen Leib an, kommt es mehr darauf an, was im physischen Leibe konfiguriert wird. Nun sehen wir, wie sich solche Impulse, wie die ausgesprochenen, in gewissen Zentren gleichsam konzentrieren, wie sie charakteristisch hervortreten in gewissen Zen­tren.",
      "Zwei solcher Zentren, die sich wirklich charakteristisch zueinan­der verhalten, sind gegeben in Mitteleuropa auf der einen Seite und in den britischen Inseln auf der andern Seite. In Mitteleuropa, wo es am stärksten zum Ausdrucke kommt, haben wir dasjenige, was ich das feste Element genannt habe und wo einfließt in den physischen Leib das, was von den Genien des Flüssigen und von den Genien des Festen kommt, wo sich das also vermischt, und auf den britischen Inseln, wo - in ge­wisser Weise stärker, als das zum Beispiel in Frankreich der Fall ist -in die ätherischen Leiber vorzugsweise hineinwirkt das, was von den Genien des flüssigen Elementes kommt.",
      "Das hat bewirkt, daß auf die­sen zwei Gebieten Menschen leben, die im Grunde genommen dieselben Impulse in sich tragen; nur die einen tragen sie im physischen Leibe und sind zu alledem geeignet, was mit dem Wirken dieser Genien im phy­sischen Leibe zusammenhängt; die andern, auf den britischen Inseln, tragen sie im Ätherleibe und sind dadurch berufen, alles dasjenige zu bewirken, was mit den Impulsen des ätherischen Leibes zusammen­hängt. Wenn ich das grotesk sagen darf, so könnte ich sagen, wenn man einen Deutschen und einen Engländer zusammenstellt, so merkt man den Unterschied, wenn man sie als physische Leiber betrachtet.",
      "Man merkt erst die Ähnlichkeit, wenn man den physischen Leib des Deut­schen mit dem ätherischen Leibe des Engländers zusammenstellt.",
      "tritt erst dasjenige hervor, was uns zeigt, daß dieselben Impulse da leben, richtig dieselben Impulse da leben.",
      "Sie sehen, was in der äußeren Anschauung, die bei der äußeren Phan­tasmagorie bleibt, ich möchte sagen, karikiert hervortritt. Mißverstehen Sie das Wort nicht. Das tritt einem in seiner wahren Gestalt erst ent­gegen, wenn man das, was Lebensgrundlage wird, was die Wahrheit ist, ins Auge faßt. Aber weil in der Welt die Wesenheiten zusammenwirken müssen, weil es gar nicht anders sein kann, als daß die Wesenheiten zu­sammenwirken, denn die Welt ist ein Ganzes, so muß das so sein, daß auf der einen Seite gewisse Impulse durch den physischen Leib, auf der an­dern Seite durch den Ätherleib wirken. Ich möchte sagen, das gehört sich so. Dadurch entsteht das entsprechende wirkliche Zusammenwirken.",
      "Dadurch, sehen Sie, ist dasjenige gekommen, was in der geistigen Welt erscheint als ein ganz besonderes Verhältnis zwischen der deut­schen Welt und der britischen Welt. Ich habe dieses ganz besondere Verhältnis für den Osten und Westen in einer vorigen Stunde ausein­andergelegt, indem ich Ihnen gezeigt habe, wie für den Osten und Westen ein gewisser Kampf stattfindet in der geistigen Welt, durch die Verschiedenheit bewirkt der Seelen, die aus einem östlichen und der Seelen, die aus einem westlichen Leibe kommen.",
      "Dasjenige, was durch die eben geschilderten Verhältnisse bewirkt wird, ist etwas anderes. Ich bitte Sie, auch das, was ich heute zu sagen habe, nicht so zu nehmen, als ob man es verstandesgemäß oder speku­lierend nehmen kann. Man muß da schon in der geistigen Welt beob­achten, sonst wird man nicht auf das Richtige kommen können. Es bildet sich nach und nach heraus ein Zusammenklang zwischen dem, was von Mitteleuropa und den britischen Inseln zurückwirkt, eine Har­monie, ein richtiges geistiges Bündnis, das allmählich eine solche Stär­kung erfahren hat, daß man sagen kann, geistig gefaßt, lieben sich heute keine Erdenseelen mehr als die Erdenseelen Mitteleuropas und die Er­denseelen der britischen Inseln. Es ist da die stärkste Liebe, geistig ge­faßt, vorhanden, und das drückt sich äußerlich in dem aus, was wir jetzt vor uns sehen. So verwickelt sind die Dinge.",
      "Man würde solche Dinge wahrhaft nicht aussprechen, wenn sie nur auf einer leicht fundierten Erkenntnis beruhten, wenn man sie sich",
      "nicht durch schmerzlichste Erfahrungen errungen hätte. Glauben Sie nicht, daß Sie schablonisieren dürfen, indem Sie denken, daß jedes Bündnis in der physischen Welt ein Krieg in der geistigen Welt ist, und ein Krieg in der physischen Welt ein Bündnis in der geistigen Welt. Die Dinge sind so, wie ich sie Ihnen geschildert habe. Und daß das als Kampf zum Ausdruck kommt, ist der Ausdruck in der heutigen mate­rialistischen Kultur für die Schwierigkeit, die Sache im Geistigen wirk­lich auszuleben.",
      "Es sträubt sich unsere Zeit nicht nur in Worten, sondern auch in Taten, das anzuerkennen, was in der geistigen Welt vorhanden ist. Sie versucht, das Gegenteil dessen hinzustellen, was in der geistigen Welt vorhanden ist, weil sich das materialistische Zeitalter gegen die An­erkennung des Geistigen auch in Taten sträubt. Und so wird das, wohin die geistige Welt tendiert - nämlich nach der Harmonie des im Phy­sischen Errungenen in Mitteleuropa und des im Ätherischen Errungenen auf den britischen Inseln -, in der Maja übertönt durch das, was man heute als Kampf und gegenseitigen Haß vor sich hat.",
      "Sehen Sie, es lohnt sich schon für diejenigen, die keine Geisteswissen­schafter sind, uns für Narren zu halten, da die Erkenntnisse, die aus der geistigen Welt dringen, gar sehr widersprechen dem, was man auf der physischen Welt beobachten kann. Aber dessen können wir uns doch versichert halten, daß die Fortentwickelung der Menschheit davon ab­hängt, daß wirklich die geistigen Wahrheiten durchdringen werden, daß wirklich die Menschen hinter die Sinneswelt sehen lernen. Dazu sind Ereignisse notwendig, von denen ich mehr oder weniger deutlich in diesen Tagen gesprochen habe.",
      "Man darf froh sein, daß das Karma uns hier zusammengeführt hat in einem neutralen Gebiete, wo es geht, so rückhaltlos über diese Dinge zu sprechen, denn es ist nicht ganz leicht, gerade heute über diese Dinge zu sprechen. Aber für die Geisteswissenschafter ist es gut, sich in diese Dinge hineinzufinden, weil sie betrachten dürfen dasjenige, was in der äußeren Welt geschieht, gerade als Ansporn dafür, hinter den Schleier zu schauen. Es müßte vieles ganz unverständlich bleiben, wenn man nicht hinter diesen Schleier schauen könnte. Die Dinge bekommen erst ihre volle Bedeutung, wenn man hinter diesen Schleier sieht."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Inwiefern die Erde selbst ein Inspirator ist für die Menschen, die auf der Erde leben, davon haben wir gestern wenigstens in einigen Andeu­tungen gesprochen, denn nur Andeutungen können selbstverständlich in einem Gebiete gegeben werden, das so umfassend wie nur irgend möglich ist."
      ],
      [
        "Wichtig, bedeutungsvoll ist es gerade in unserer Zeit, sich bewußt zu werden, daß solche Zusammenhänge existieren, wie die sind, von denen wir gesprochen haben, denn der Mensch innerhalb der Erdenentwicke­lung ist gerade in unserer Gegenwart auf dem Punkte, sich gewisser­maßen wieder zu emanzipieren von diesem Erdeinfluß, gewissermaßen wiederum sich durchdringen zu lassen von denjenigen Einflüssen, die nicht aus der Erdenwelt, sondern aus der die Erde umgebenden geisti­gen Welt kommen."
      ],
      [
        "Dieses Bestreben, gleichsam in die menschlichen Fähigkeiten, in das menschliche Denken und Empfinden hereinzubekommen dasjenige, was nicht bloß irdisch ist, liegt zugrunde unserem geisteswissenschaftlichen Streben.",
        "Nach diesem geisteswissenschaftlichen Bestreben geht wirklich alle Tendenz der modernen Bildung hin, und man darf wohl sagen, zwei Dinge sind es, die immer mehr und mehr dem Menschen der Ge­genwart zum Bewußtsein kommen müssen."
      ],
      [
        "Das eine ist, daß der Mensch in bezug auf seine eigene seelische We­senheit einer Welt angehört, die sich nicht für die äußeren Sinne ent­hüllt, sondern die erst hinter der äußeren Sinneswelt liegt, daß der Mensch einer solchen Welt angehört mit seinem innersten Seelenwesen, zu der man weder durch Sinnesbeobachtung kommen kann noch auch durch Schlüsse und die Logik, die sich auf die Sinnesbeobachtung grün­den.",
        "Es wird die Aufgabe unserer Zeit sein, über diesen Punkt sich Klarheit zu verschaffen, daß alles Wissen, welches die äußeren Sinne vermitteln und ihre Philosophie, die sich nur gründet auf das äußere Sinneswissen, nicht herankommen können an dasjenige, was die mensch­liche Seele eigentlich ist."
      ],
      [
        "Das zweite ist eine Wahrheit, die Ihnen aus Ihrem geisteswissen­schaftlichen Leben heraus geläufig ist, von der Sie aber wissen, daß sie dem allgemeinen Bewußtsein der Gegenwart noch ganz fern steht.",
        "Es ist die wichtige Wahrheit von den wiederholten Erdenleben, davon, daß des Menschen Seele sich nicht erschöpft in dem Leibe, in dem sie lebt zwischen Geburt und Tod, in alledem, was mit diesem Leibe zu­sammenhängt, sondern daß sie von Leben zu Leben geht."
      ],
      [
        "Weil diese beiden Wahrheiten, daß die Seele einer Welt angehört, die hinter der Sinneswelt liegt, und daß sie von Leben zu Leben geht, zu den allerwichtigsten für unsere Zeit gehören, die zunächst begriffen werden müssen, deshalb habe ich im zweiten Bande meiner «Rätsel der Philosophie» ein Kapitel angefügt, in dem aus dem Entwickelungsgang der Menschheit selber gerade auf diese beiden Wahrheiten in intensiver Weise hingedeutet wird, denn das ist ein dringendes Erfordernis unserer Zeit, daß immer mehr und mehr Menschen gerade diese beiden Wahr­heiten begreifen lernen."
      ],
      [
        "Da dieses Buch «Die Rätsel der Philosophie» ein solches ist, das sich nicht speziell an Anthroposophen wendet, sondern an alle Menschen, die lesen und Gelesenes verstehen können, so mußte versucht wer­den, in Kürze, aber so scharf als möglich, auf diese beiden Wahrheiten hinzudeuten.",
        "Man darf sagen, es liegt im tieferen Bewußtsein der Menschen der neueren Zeit, nach diesen Wahrheiten hin ihre Gedan­ken zu richten.",
        "Ich will zunächst nur sagen, ihre Gedanken zu richten.",
        "Wir können überall solche Tendenzen, die Gedanken nach diesen Wahrheiten zu richten, bemerken.",
        "Ich habe manchmal versucht, aus der neuen Geistesgeschichte Menschen anzuführen, welche nach sol­chen Wahrheiten hin tendieren.",
        "Ich möchte heute noch ein Beispiel an­führen."
      ],
      [
        "Einer der größten Geister des 19.",
        "Jahrhunderts ist ohne Zweifel Emerson, der so bedeutsam eindringlich,wenn auch nicht in pedantisch­philosophischer Sprache, so doch in einer eindringlichen Sprache ge­schrieben hat.",
        "Emerson weist überall, ob er über die Natur spricht oder über das Menschengeschlecht, darauf hin, daß das äußere Gefüge der Welt, welches der Mensch mit seinen Sinnen überschaut und mit dem Verstande begreift, nur die Hülle, die Phantasmagorie ist, und daß man"
      ],
      [
        "zu der Wahrheit nur kommt, wenn man hinter die Phantasmagorie versucht einzudringen."
      ],
      [
        "Aber solche Geister wie Emerson gehen noch weiter.",
        "Und davon möchte ich ein Beispiel geben.",
        "Emerson hat unter seinen sehr bedeut­samen Büchern auch eines geschrieben, welches heißt «Die Repräsen­tanten des Menschengeschlechtes».",
        "In diesem Buche hat er behandelt Plato als Repräsentanten alles philosophischen Menschheitsstrebens; Swedenborg als Repräsentanten des mystischen Menschheitsstrebens; Montaigne, einen bedeutsamen Geist des 16.Jahrhunderts, als Reprä­sentanten des Skeptizismus; Shakespeare als Repräsentanten des dich­terischen Vermögens; Goethe als Repräsentanten des schriftstellerischen Vermögens und Napoleon als den Tatenmenschen, als den Repräsen­tanten des Menschen der Tat."
      ],
      [
        "Mit diesem Buche ist allerdings etwas Bedeutsames getan.",
        "Es sind herausgehoben die Typen des Menschentums in bezug auf das Seelen-leben.",
        "Es würde eine interessante Betrachtung abgeben, wenn man be­leuchten würde, wie in der Tat das Repräsentative des philosophischen Strebens in Plato, das Repräsentative des skeptischen Strebens in Mon­taigne getroffen ist.",
        "Dieses Buch bedeutet eine der größten Taten des geistigen Menschheitsstrebens.",
        "Nun widmet Emerson merkwürdiger­weise Montaigne, ich möchte sagen, eine ganz besonders liebevolle Dar­stellung, obwohl gerade diese liebevolle Darstellung einem erst ent­gegentritt, wenn man sich gründlich genug auf dieses Kapitel über Montaigne einläßt.",
        "Das ist auch wieder sehr bedeutungsvoll für das Hintendieren Emersons zur geisteswissenschaftlichen Weltauffassung.",
        "Derjenige, der sich auf diese Weltauffassung im Ernste einläßt, wird gewahr, wie wirklich jedes Ding zwei Seiten hat, wie, wenn man ver­sucht, eine Wahrheit auszusprechen, man nur etwas Einseitiges sagen kann, und die zweite Seite gleichsam im Hintergrunde lauern muß."
      ],
      [
        "Der Skeptiker, der ein lebendiges Gefühl dafür hat, daß man ge­wissermaßen schon ein Unrecht tut, wenn man eine Wahrheit strikt formuliert, ist im tiefsten Sinne berührt von dem geistig-seelischen Fluidum, das in der Menschenseele immer da ist und das einen ver­hindert, sobald man nur von der geistigen Welt berührt ist, mit allzu­viel Aplomb eine scharf konturierte Wahrheit hinzustellen, ohne darauf"
      ],
      [
        "hinzuweisen, daß in gewissem Sinne auch das Gegenteil davon eine Berechtigung hat."
      ],
      [
        "Dieses in gewissem Sinne Berührtsein von einem Gefühle, das aus der Geistigkeit herauskommt, macht Montaigne zu einer bedeutenden Persönlichkeit.",
        "Aber das ist es nicht, worauf ich hinweisen wollte.",
        "Hin­weisen wollte ich auf das, wie Emerson erzählt, wie er auf Montaigne gekommen ist.",
        "Er sagt da: Schon als Knabe fand ich einen Band von Montaigne in der Bibliothek meines Vaters, den ich aber nicht ver­stand. - Als er dann die Hochschule absolviert hatte, sah er sich das Buch noch einmal an, und da bekam er den merkwürdigen Drang, Satz für Satz kennenzulernen von dem, was Montaigne geschrieben hat.",
        "Und das tat er, diesem Drange folgend.",
        "Nun sehen wir in dem Kapitel über Montaigne, welches Emerson schrieb, daß er nach einem Ausdruck da­für suchte, warum er plötzlich damals wie besessen war von Montaigne und plötzlich anfing, ihn ganz in sich aufzunehmen.",
        "Da findet er keinen besseren Ausdruck dafür, als daß er sagt: Es war mir so, als wenn ich diese Bücher von Montaigne in einem früheren Leben selber geschrieben hätte. - Daraus ersehen Sie, wie ein im eminentesten Sinne moderner Geist, der an das herandringt, was Forderung der Gegenwart ist, da, wo er sich über das Intimste in seiner Seele ausdrücken will, gezwungen ist, sich einen Ausdruck zu bilden, der ganz nach der geisteswissen­schaftlichen Wahrheit der Reinkarnation hin tendiert.",
        "Er findet keinen besseren Ausdruck und muß daher die Idee der wiederholten Erden-leben zu Hilfe nehmen."
      ],
      [
        "So etwas ist außerordentlich charakteristisch, ist ungeheuer bedeu­tungsvoll, und dies führt uns nun dahin, anzuknüpfen an den Gedan­ken, der gestern ausgeführt worden ist.",
        "Sehen wir uns gerade die vor­nehmsten Geister unserer Zeit an - und einer der vornehmsten ist Emerson -, so haben Sie auf der einen Seite, wenn sie so bedeutende Geister sind wie Emerson, das Erdenwissen, das sie übernommen haben, insofern sie hineingestellt sind in den Evolutionsprozeß der Erde.",
        "Das wissen sie, was man heute aufnimmt als Mensch.",
        "Sie wissen, daß man, wenn man an einen gewissen Punkt der Erde gesetzt ist, eine bestimmte Sprache spricht und so weiter, daß es üblich ist, an dem Orte, wo man hinversetzt ist, dem Kinde, dem jungen Menschen diese Dinge zu überliefern"
      ],
      [
        "und so dasjenige, was man Bildung nennt, an den Menschen her-anzubringen.",
        "Dieses Wissen, das einem Volke auf diese Weise über­liefert wird, ist ein Wissen eines großen Umkreises.",
        "Man darf schon sagen, daß das ein Wissen eines großen Umkreises ist, das kann man sagen, wenn man sieht, wie Emerson eigentlich vorgeht."
      ],
      [
        "Wir wissen, daß bei ihm, wenn er einen Vortrag zu halten hatte, es so erschien, als ob das, was er sagte, unmittelbar, während er es sagte, aus seinem Geiste hervorsprühte.",
        "Wie improvisiert erschien alles.",
        "Wenn er besucht wurde an einem Tage, wo er einen Vortrag halten sollte, konnten die Besucher sehen, daß im ganzen Zimmer alle möglichen Notizen herumlagen, aus denen er zusammengeholt hatte dasjenige, was er sozusagen über das Äußere seines Stoffes zu sagen hatte.",
        "Aber hinter dem, was er so der Menschheit überlieferte, lagen Intimitäten, und die­ses ist eben eine Intimität, was ich ausgesprochen habe, daß durch­schimmert die Idee der wiederholten Erdenleben ganz keusch an einer Stelle."
      ],
      [
        "Man kann sehen, wie sogar die Besten unserer Zeit, indem sie solche Wahrheiten in der Seele durchempfinden, durchfühlen und auch aus­sprechen, keusch in sich selbst bleiben, diese Wahrheiten noch nicht hereintragen wollen in das Gebiet, dem das äußere Wissen entspringt."
      ],
      [
        "Wenn wir nun geisteswissenschaftlich an die Sache herangehen, so müssen wir sie noch anders beleuchten, denn unsere Zeit ist einmal die­jenige, deren Mission es ist, das, was bisher in der Seele zurückgehalten und nur zuweilen angedeutet worden ist, zur Klarheit, zur wirklichen Erkenntnis zu bringen, in Wissensformen zu prägen, so daß unsere Zeit wirklich die Aufgabe hat, manches, was bis zu dieser unserer Zeit sich wie herausdrängt aus den Seelen der Besten, zur vollen Klarheit, zu einer für die Menschen selbstverständlichen Wahrheit zu machen.",
        "Und da können wir ganz genau beschreiben, wie es war, wenn Emerson in seinen gehaltreichen Vorträgen bald einen Satz sagte, der eine Erkennt­nis ausdrückte über das industrielle Leben seiner Umgebung und dann wenige Zeilen später etwas bringt, was von dem alten Indien handelt, und dann wieder etwas, was von Shakespeare handelt.",
        "So trägt er sozu­sagen das Erdenwissen zusammen und dann entschlüpft ihm oft eine Bemerkung so mittenhinein, die aus dem Intimen seiner Seele kommt."
      ],
      [
        "Woher kommt denn das, was in einer solchen Bemerkung liegt?",
        "Das kann man sich nur beantworten,wenn man alle Seiten der menschlichen Natur in Betracht zieht.",
        "Der Mensch erkennt in der Erdenzeit nur das wenigste, nur ein Stück seines Lebens, das sich abspielt vom Aufwachen bis zum Einschlafen.",
        "Der andere Teil des Lebens wird verbracht im Schlafe, und dieser Teil des Menschenlebens ist recht, recht mannig­faltig."
      ],
      [
        "Es ist einmal wahr, daß für viele, viele Menschen dieses Leben im Schlafe so verläuft, daß sie da in Berührung kommen mit elementari­schen Weltenwesenheiten, die mit niedrigeren Äußerungen der mensch­lichen Natur zusammenhängen, als die Tagesäußerungen sind.",
        "Man möchte sagen, die Menschen treiben vom Einschlafen bis zum Auf­wachen, also im Bereiche elementarischen Lebens, des Nachtlebens, allerlei Allotria, Dinge, über die sie hinaus sind, wenn sie im äußeren Leben stehen.",
        "Wer wüßte nicht, daß er sich oft seiner Träume schämen muß.",
        "Das ist eine allgemeine Erfahrung, die jeder machen kann.",
        "Der Mensch treibt also während des Schlafes allerlei Allotria, in einer Ge­sellschaft, die nicht etwa eine gute ist, die sich vielmehr wendet an seine Leidenschaften, seine Triebe, die viel schlechter ist als die, in welcher er während seines Wachlebens erzogen ist."
      ],
      [
        "Nur wenn man das versteht, versteht man manches besser, was sich geschichtlich ereignet hat.",
        "Der heutige Mensch muß, damit er nicht all­zu stark Allotria auch im physischen Leben treibt, schon einmal mit der Gabe ausgestattet sein, daß er nicht allzu großen Wert auf die Träume legt.",
        "Er vergißt seine Träume daher sehr leicht, vergißt die Allotria aus den Träumen, und das ist gut für ihn, denn er soll vor­bereitet werden dazu, im Wachbewußtsein einzutreten in die geistige Welt, während die Vorzeit dazu da war, den Menschen während des Schlafens bis zum Aufwachen in diese geistige Welt eintreten zu lassen."
      ],
      [
        "Im Grunde genommen liegt ein stärkeres Bewußtsein von dieser Welt noch gar nicht so weit hinter uns, wie man gewöhnlich glaubt.",
        "Auch dafür will ich Ihnen ein Beispiel geben.",
        "Es gibt ein Bild von Albrecht Dürer, das vielen Leuten, namentlich aber den Gelehrten, viele Rätsel aufgegeben hat.",
        "Die Radierung hat ungefähr das zum In­halt, daß eine satyrhafte, faunenhafte Gestalt da ist, die gleichsam umschlungen"
      ],
      [
        "hält ein weibliches Wesen.",
        "Aus dem Hintergrunde erscheint ein anderes weibliches Wesen, welches sich wie strafend diesem Paare nähert.",
        "Und eine lierkulesartige männliche Gestalt steht in der Nähe, die eine Keule in der Hand hält, welche das strafende weibliche Wesen von der Gruppe des Weibes mit dem Satyr zurückhält, so daß sie nicht heran kann."
      ],
      [
        "Es ist, man möchte sagen, ganz merkwürdig, äußerst merk­würdig, wie sich die Gelehrten abgemüht haben, dieses Bild zu ver­stehen.",
        "Man nennt es gewöhnlich «Herkules».",
        "Aber das, was damit aus­gedrückt ist, gibt es nicht in der gewöhnlichen Herkules-Sage."
      ],
      [
        "Man frägt sich daher: Wie ist Albrecht Dürer zu dieser Szene gekommen? -Und da sind die kuriosesten Ideen aufgestellt worden.",
        "Man kann sehen zum Beispiel bei Herman Grimm, wie hilflos er diesem Bilde gegen­über ist."
      ],
      [
        "Er weiß nichts damit anzufangen.",
        "Er stellt die kuriosesten Ideen auf.",
        "Und warum geschieht das?",
        "Warum wissen die Menschen nichts damit anzufangen?",
        "Weil er und die Gelehrten nicht wissen - was Albrecht Dürer noch wußte -, daß die Menschen im Schlafe noch ein­dringen können in eine geistige Welt."
      ],
      [
        "Heute ist dieses Bewußtsein ver­lorengegangen.",
        "Dürer wußte aber noch, daß es zum Beispiel Männer gibt, welche während der Schlafenszeit in Gemeinschaft mit der ele­mentaren Welt allerlei Allotria treiben, Männer, die während der ge­wöhnlichen Zeit ganz gesittete Männer sind, aber während der Schla­fenszeit in die Triebwelt zurückfallen und allerlei unnütze Dinge, aller­lei Allotria treiben."
      ],
      [
        "In dem Bilde des Albrecht Dürer sehen wir den Satyr und den Her­kules mit der Keule.",
        "Der gute Herkules, der dasteht, möchte gern selber dieser Satyr sein.",
        "Aber er lebt in der physischen Welt, in einer sittlichen Welt auf dem physischen Plan, und das gestattet ihm die Gattin nicht.",
        "Die kommt daher und will ihn wegtreiben.",
        "Ihm aber gefällt das doch, und er hält sie zurück."
      ],
      [
        "Wir sehen hier einen inneren Seelenprozeß und wissen, daß Albrecht Dürer noch etwas von diesen Dingen wußte.",
        "So ist vieles in der Kunst gar nicht so weit zurückliegender Jahrhunderte zu erklären, weil da­mals noch ein Bewußtsein des Zusammenhanges des Menschen mit der unmittelbar an das Physische anstoßenden geistig-elementaren Welt vorhanden war."
      ],
      [
        "Aber wenn wir den Blick wenden auf solche vornehme Geister, wie Emerson einer war, so müssen wir sagen, sie treiben während ihres Schlaflebens keine Allotria, sondern eben Vornehmes.",
        "Wenn sie so mit ihrem Ich und mit dem astralischen Leibe in der geistigen Welt sind, kommen sie mit den Wahrheiten in Beziehung, was in der Menschheit wahrhafte Anthroposophie sein soll.",
        "Da drängt sich in ihr Bewußtsein, was künftiges physisches Wissen werden soll.",
        "Man könnte sagen, Emer­son empfängt so etwas im Schlafe.",
        "Daher stellt es sich so keusch, intim in dasjenige hinein, was er mit den physischen Sinnen und dem Ver­stande, überblickend das weite Erdenleben, über das physische Leben zu sagen hat."
      ],
      [
        "Nun würde es nicht gehen im Sinne der Evolution der Menschheit, daß es einfach dabei bliebe, daß die Menschen nur so, ich möchte sagen, in ihrem Schlafleben erfassen, was da hinter dem Sinnenschein, hinter der Sinnesphantasmagorie liegt.",
        "Denn das ist wieder der Sinn der Evo­lution, daß das Schlafleben immer mehr und mehr bei der Erkenntnis an Bedeutung verliert.",
        "Man muß schon ein bedeutender Geist sein wie Emerson, wenn man sich aus dem Schlafleben heraus so etwas erobern will wie die Idee der wiederholten Erdenleben.",
        "Das aber, was geistig ist, muß in die Menschheit kommen, muß in der Menschheit Einzug halten.",
        "So, wie im Zusammenhange mit dem innersten menschlichen Seelenleben diese Wahrheiten sind, wie sie sich da gleichsam wie in einer Art von Morgenröte verkündigen gerade bei solchen Geistern wie Emerson, muß auf der andern Seite wieder eine irdische Veranlagung da sein, solche Wahrheiten im hellen Wachbewußtsein zu verstehen.",
        "Es muß die irdische Veranlagung vorhanden sein, sich selber so zu emp­finden, daß man es natürlich findet, diese Wahrheiten anzuerkennen.",
        "Daß das noch nicht natürlich ist in der Gegenwart, begreifen Sie, denn wir sind als Geisteswissenschafter noch ein so kleines Häuflein, und alle, die außerhalb des geisteswissenschaftlichen Strebens stehen, sehen uns als Narren oder etwas Ähnliches an."
      ],
      [
        "Es liegt nicht in der modernen Bildung, diese Wahrheiten unmittel­bar anzuerkennen.",
        "Das natürliche Temperament des Menschen spricht dagegen.",
        "Was die Leute Logisches vorbringen gegen die Geisteswissen­schaft, ist in der Regel außerordentlich minderwertig, denn aus logischen"
      ],
      [
        "Gründen sträuben sich die Menschen nicht; sie sträuben sich, weil sie ihrer Natur nach durch alles, was sie durch die Kräfte der Erde sind, nicht veranlagt sind im allgemeinen, solche Wahrheiten heute schon aufzunehmen."
      ],
      [
        "Aber es muß eine Zeit kommen, in der des Menschen Natur so kon­stituiert sein wird, daß er unmittelbar diese Wahrheiten einsehen kann, so wie er heute die mathematischen Wahrheiten einsehen kann.",
        "Der Mensch muß naturhaft so organisiert werden, daß er diese Wahrheiten einsehen kann.",
        "Dazu ist notwendig, daß er für die Zeit, die verläuft zwischen der Geburt und dem Tode, auch physisch so konstituiert ist, daß sein Gehirn so durchgebildet ist, daß er diese Wahrheiten einsehen kann."
      ],
      [
        "Im Sinne der gestrigen Auseinandersetzung gesprochen, muß ein sol­ches Verhältnis hergestellt werden zwischen den Geistern, die in der Erde wirken, und den Menschen, daß die Menschen so konstituiert wer-den, daß sie diese Wahrheiten aufnehmen können, und das geschieht auf die Weise, daß eine Land fläche, wie ich das gestern gezeigt und auf­gezeichnet habe, sich herüberneigt von Osten nach Westen gegen die drei Meerbusen, von denen ich gestern gesprochen habe.",
        "Diese Landes-fläche ist äußerlich nur eine Phantasmagorie Diese Landesfläche ist in Wirklichkeit zusammengesetzt aus den Geistern der Erde."
      ],
      [
        "In Wirklich­keit ist es so, daß die Geister dieser Landesfläche wirken auf die Men­schen und sie physisch bilden so, daß sie die Wahrheiten von der geistig-seelischen Konstitution des Menschen und den wiederholten Erden-leben einsehen.",
        "Was, ich möchte sagen, mehr westliche Geister wie aus dem Schlafe heraus sich erobern müssen, das wird im Wachen eine mehr selbstverständliche Wahrheit werden müssen bei denjenigen, die sich vom Osten herüber zuneigen der Evolution der Menschheit."
      ],
      [
        "Die Erde bereitet zu ihre Leiber, möchte man sagen, zu dem, was sie für die Evo­lution brauchen.",
        "Diese Erde ist durchaus dasjenige, was ich gestern aus­einandergesetzt habe: ein weit umgreifender Organismus, der beseelt ist und der aus seinem Seelenleben heraus von Zeit zu Zeit die Erden-geister ausschickt, welche die Leiber so durchorganisieren, daß sie in entsprechender Weise in die Evolution eingreifen können."
      ],
      [
        "Sehen Sie, diese Dinge sind außerordentlich tief und bedeutsam, und"
      ],
      [
        "man muß sich schon auf solche Dinge einlassen, wenn man verstehen will, um was es sich da handelt.",
        "Wenn man allerdings die Erde als einen beseelten und durchgeistigten Organismus vergleicht mit dem, was der Mensch ist als durchseelter und durchgeistigter Organismus, so gibt es einen großen Unterschied.",
        "Der Mensch steht durch das Äußere seines physischen Leibes, in dem er eigentlich für gewöhnlich gar nicht darin lebt, aber in dem er darinnensteckt, in Beziehung zu den eigentlichen Geistern der Erde.",
        "Durch den Ätherleib steht er in Beziehung zu den Geistern deswassers; durch den Astralleib in Beziehung zu den Geistern der Luft, und durch seine Verbindung mit dem Ich steht er in Beziehung zu den Geistern des Feuers."
      ],
      [
        "Wenn der Mensch im Schlafe den physischen Leib und ätherischen Leib verläßt, dann lebt er mit seinem Ich und dem Astralleibe nur in Beziehung zu der die Erde durchwogenden Wärme und der die Erde durchflutenden und durchhauchenden Luft.",
        "Er ist herausgerissen aus alledem, was Erde und Wasser im physischen Leib konfigurieren.",
        "Da ist der Mensch wirklich herausgerissen, wenn er schläft, aus alledem, was, ich möchte sagen, der physische und Ätherleib als Erdenwesen machen.",
        "Natürlich gehören die Luft und dieWärme auch zur Erde, aber nur zur Erde, nicht zu den Teilen der Erde.",
        "Nun ist für den Menschen als beseeltes, durchgeistigtes Wesen die Wärme gewissermaßen das­jenige, in dem er sich aufhält wie in seinem eigenen Elemente.",
        "Bei den höheren Tieren ist schon eine Vorbereitung dazu vorhanden.",
        "Sie haben Eigenwärme, nicht bloß die Wärme ihrer Umgebung.",
        "Sie leben in ihrem Seelischen, in ihrer Eigenwärme.",
        "Der Mensch hat das insbesondere aus­gebildet, daß er in seiner Eigenwärme lebt, daß er seine eigene Tem­peratur hat.",
        "Das ist etwas, was ihn abschließt von dem, was in der Außenwelt so verschiedenartig ist.",
        "Die Wärme ist gleichsam etwas, wo­von jeder Mensch sein Quantum in sich trägt und es mit sich trägt.",
        "Da ist er in seinem eigentlichen Ich darinnen, da ist er zu Hause in der Wärme."
      ],
      [
        "In der Luft lebt er schon weniger allgemein darinnen.",
        "Ich möchte sagen, da übt schon die Differenzierung der Erde einen gewissen Ein­fluß auf ihn aus.",
        "Ob er in Höhenluft, Wasserluft oder Landluft lebt, das macht schon einen gewissen Unterschied.",
        "Da kommt der Mensch in"
      ],
      [
        "Beziehung zu dem, was von außen auf ihn wirkt.",
        "So ist es bei dem Men­schen als einem durchseelten und durchgeistigten Organismus."
      ],
      [
        "Das Umgekehrte ist bei der Erde als durchseeltem, durchgeistigtem Organismus der Fall.",
        "Was für den Menschen die Wärme ist, das ist für die Erde eben die Erde, das feste Irdische, und die Wärme ist für sie das Äußerlichste, was zu der beseelten Erde ein Verhältnis hat wie zu uns die Erde."
      ],
      [
        "Die Erde ist Erde durch und durch, wie wir durch und durch Wärme sind.",
        "Die Erde ist nach außen differenziert in bezug auf die Wärme.",
        "Je nachdem sie in die Eisregionen ihre Glieder erstreckt oder in die schwüle Region der Tropen, öffnet sie nach außen hin ihr See­lisches so nach der Wärme, wie wir in bezug auf unseren physischen Leib hinneigen nach der Gegend, in der wir gerade wohnen."
      ],
      [
        "Es ist bei der Erde gerade das Entgegengesetzte wie beim Menschen, und darauf beruht das Zusammenwirken der Erde als beseelter und geistiger Orga­nismus mit dem Menschen als beseeltem und geistigem Organismus.",
        "Durch dieses Zusammenwirken entsteht dann dasjenige, was im phy­sischen Menschenleibe zustande kommt, damit dieser physische Men­schenleib in der Nacheinanderfolge der Nationen und Völker in rich­tiger Weise in die Evolution des ganzen Erdendaseins eintritt."
      ],
      [
        "Wir haben gerade in den Völkern, welche als Völkermassen von Osten nach Westen herüberrückten, ein intensives Verhältnis des Irdischen zu dem Menschlichen.",
        "Und man könnte dieses intensive Verhältnis so aus­sprechen, wie wenn man in der Erde selber sehen würde ein mächtiges Wesen, und dieses mächtige Wesen würde sich entschließen, in die Evo­lution in entsprechender Weise einzugreifen, sagen wir vom 20."
      ],
      [
        "Jahr­hundert ab.",
        "Da muß es sich sagen: Ich muß gewisse geistigewesenheiten hinauflenken nach meiner Oberfläche, ich muß sie tätig sein lassen so,"
      ],
      [
        "# Bild s. 85"
      ],
      [
        "daß sie physische Leiber zubereiten, damit die physischen Leiber durch das Gehirn die Wahrheiten aufnehmen können, die in dieser Zeit der Evolution der Menschheit frommen."
      ],
      [
        "Wie ein Gedanke, den die Erde hat, ist dasjenige, was ich eben aus­gesprochen habe.",
        "Man erfaßt diesen Gedanken nur, wenn man ihn in der richtigen Frömmigkeit und Ehrerbietung erfaßt, wenn man ihn nicht nimmt wie die Gedanken der äußeren Wissenschaft, sondern wenn man ihn betrachtet wie etwas Heiliges, wie etwas, das man nicht ohne Ehrerbietung aussprechen kann, weil man erinnert wird an den Zusammenhang des Menschen mit der geistigen Welt, weil man un­mittelbar darinnensteht in dem Verkehr des Menschlichen mit dem Göttlichen, wo solche Dinge ausgesprochen werden.",
        "Daher sollte auch überall darauf geachtet werden, daß die nötige Atmosphäre des Füh­lens und Empfindens da sein sollte, wo solche Dinge ausgesprochen werden.",
        "Das ist ungeheuer wichtig bei solchen Dingen.",
        "Man möchte sagen: In einem gewissen Sinne dürfen solche Dinge nicht anders aus­gesprochen werden, als daß ihnen das Gefühl, die Stimmung des Gebet­artigen zugrunde liegt.",
        "Ein Aufschauen zu den geistigen Welten muß durchpulsen dasjenige, was wir so durchdenken, indem wir uns solchen Gedanken nähern. - Und daß dies auf eine naturgemäße Weise ge­schehen kann, schon durch das äußere Milieu, dazu wird unser Bau aufgeführt, und dazu wird alles das gemacht, was darin zum Vorschein kommen soll."
      ],
      [
        "So sehen wir in dem, was ich eben dargestellt habe, eine Art Beispiel, wie die Erde als Erde durch das, was in ihrem festen Elemente enthal­ten ist, geistig wirkt, wie sie dasjenige schafft und schöpft, was auf ihr in der Evolution lebt."
      ],
      [
        "Gehen wir dagegen mehr nach Westen herüber, so haben wir andere Verhältnisse.",
        "Ich habe Ihnen gestern ein Verhältnis auseinandergesetzt, wo der Westen mit dem Osten zusammenwirkt, wo sich das flüssige Element wie ein mächtiges Wesen herüberneigt nach dem Osten und die dreigeteilte Seelennatur ausdrückend sich herüberneigt in den drei großen Meerbusen, die noch die spirituell veranlagten Völker des alten Finnland als Wäinämöinen, Ilmarinen und Lemminkäinen empfanden, und die man heute so prosaisch als Finnischen, Bottnischen und Rigaischen"
      ],
      [
        "Meerbusen bezeichnet.",
        "Da wirkte zusammen in dem alten finni­schen Volk dasjenige, was aus dem flüssigen und dasjenige, was aus dem festen Elemente kommt.",
        "In dem finnischen Volke vereinigte sich das Element, das mehr den ätherischen Menschen konstituiert und den physischen Menschen verfeinert, das Flüssige, und das Element der Erde, das, was aus der Erde herauskommt, was den physischen Men­schen konstituiert."
      ],
      [
        "Es kann die Frage aufgeworfen werden, welche Bedeutung ein sol­ches Volk hat, das eine solche eminente Mission im Verlaufe der Erden-mission vollzogen hat wie das große finnische Volk, und das doch noch bleibt für die spätere Zeit.",
        "Das hat alles seine Bedeutung in dem ganzen Fortschritt der Evolution, daß ein solches Volk dableibt, daß es nicht verschwindet von der Erde, wenn es seine Mission vollzogen hat.",
        "So wie der Mensch selber die Gedanken, welche er in einem bestimmten Lebensalter gefaßt hat, für ein späteres Lebensalter im lebendigen Ge­dächtnisse behält, so müssen auch frühere Völker bleiben wie ein Ge­wissen, wie ein lebendig fortwirkendes Gedächtnis gegenüber dem, was in späterer Zeit geschieht: wie ein Gewissen."
      ],
      [
        "Und nun könnte man sagen: Des europäischen Ostens Gewissen wird dasjenige sein, was das finnische Volk bewahrt hat. - Es muß eine Zeit kommen, wenn ein Verständnis die Herzen ergreifen soll für die Aufgaben der Evolution, wo gerade aus der Mitte des finnischen Vol­kes heraus ein Aufblühen der Ideen von Kalewala stattfinden wird, wo durchgeistigt und durchsetzt werden wird mit den modernen geistes­wissenschaftlichen Ideen dieses wunderbare Epos von Kalewala, wo es in seiner Tiefe dem ganzen Europäertum wiederum zum Bewußtsein gebracht werden wird."
      ],
      [
        "Die europäischen Völker verehrten die homerischen Epen.",
        "Allein aus noch tieferen Gründen des Seelenlebens heraus floß das Epos Kale­wala.",
        "Nur kann man das noch nicht einsehen heute.",
        "Das wird man aber, wenn man die Lehren der Geisteswissenschaft in entsprechender Weise verwenden wird für die Erklärung geistiger Erscheinungen der Erdenevolution.",
        "Ein solches Epos wie Kalewala kann nicht erhalten werden, ohne daß es im lebendigen Dasein erhalten wird, ohne die See­len, welche im Leibe wohnen, welche verwandt sind mit den Schöpferkräften"
      ],
      [
        "von Kalewala.",
        "Als lebendiges Gewissen bleibt es.",
        "Dadurch kann es fortwirken, dadurch daß nicht die Worte, sondern daß das, was in ihm selber gelebt hat, weiterlebt, daß ein Zentrum da ist, von dem es ausstrahlen kann.",
        "Darauf kommt es an, daß dieses da ist, wie die Gedanken, die wir früher gehabt haben, da sind im späteren Lebens­alter."
      ],
      [
        "Im Westen ist mehr dasjenige, was den ätherischen Leib formiert und gestaltet.",
        "Es sind dies schwierige Wahrheiten, und Sie müssen sich schon daran gewöhnen, weil ich nicht die Möglichkeit habe, die man hoffent­lich aber einmal haben wird in der Erdenevolution, die Möglichkeit, die Dinge, die ich in einer Stunde auseinandersetzen muß, in einem ganzen Jahre auseinanderzusetzen, Sie müssen sich darauf einlassen, vieles durch Ihre Gedanken zu ergänzen, das Gesagte meditativ zu durch­denken.",
        "Dann wird es Ihnen voll geläufig werden.",
        "Namentlich ver­suchen Sie nicht, mit diesen oder jenen voreiligen Empfindungsnuancen an die Dinge heranzukommen."
      ],
      [
        "Im Westen ist mehr eine Wirkung auf den ätherischen Leib vor­handen, der da in derselben Weise, aber in früherer Zeit, als es für den Osten mit dem physischen Leib geschehen muß, geformt, gebildet wer­den mußte."
      ],
      [
        "Sehen Sie, man kann in solchen Dingen sich sehr leicht Mißver­ständnissen hingeben, denn die Unterschiede sind fein, sehr subtil.",
        "Wenn man zum Beispiel im Westen sieht, daß es bei den Völkern dar­auf ankommt, daß der ätherische Leib mehr von den Geistern des Was­sers gebildet worden ist, so ist es selbstverständlich - weil der physische Leib ein Abdruck davon ist -, daß auch der physische Leib als Abdruck des Ätherleibes damit gebildet worden ist, aus den Kräften des Wassers heraus.",
        "Aber es kommt darauf an, daß im Osten die Kräfte direkt mehr in den physischen Leib hineinwirken.",
        "Man muß also sein Augenmerk auf dasjenige richten, auf das es ankommt.",
        "Die äußere physische Wis­senschaft kann diesen feinen Unterschied nicht machen.",
        "Sie sieht, daß der östliche physische Leib so konfiguriert ist und der westliche phy­sische Leib anders.",
        "Mehr sieht sie nicht.",
        "Erst die Geisteswissenschaft kann auf solche Unterschiede näher eingehen.",
        "Außerdem ist die Sprache so ungeschickt und sehr wenig geeignet, solche Unterschiede auszudrücken."
      ],
      [
        "Wenn man ganz etwas Verschiedenes sagt, hat man oft den Eindruck, man sage eigentlich das Gleiche.",
        "Gestern habe ich zum Bei­spiel sagen müssen, daß bei den asiatischen Völkern es darauf ankomme, daß die Kräfte, die den physischen Leib aufbauen, im eigenen Äther­leib liegen.",
        "Heute muß ich sagen, daß es von den Völkern des Westens darauf ankommt, daß der Ätherleib geformt wird aus den Kräften des Wassers.",
        "Wenn Sie das Ganze zusammennehmen, werden Sie verstehen, daß in den alten Zeiten es der Fall gewesen ist, daß bei den östlichen Völkern Europas der Ätherleib geformt werden mußte, aber es ist heute, jetzt, die Zeit, wo der physische Leib geformt werden muß, während bei den westlichen Völkern der Fall so ist, daß ihr Ätherleib geformt wird, nachdem ihr physischer Leib schon das Gepräge mehr von außen erhalten hat, daß ihr Ätherleib unmittelbar den Genien des Meeres, den Genien des Wassers ausgesetzt wird."
      ],
      [
        "Bei den Völkern des Westens kommt das, was sie sind, dadurch zu­stande, daß die Impulse in den Ätherleib hineingehen.",
        "Da, wo die Im­pulse mehr in den Ätherleib hineingehen, kommt es weniger auf das Räumliche, sondern mehr auf das Zeitliche an.",
        "Wie in der Aufeinander­folge der Zeit die Impulse wirken, darauf kommt es mehr an."
      ],
      [
        "Wenn wir nach dem Osten hinüberschauen, sehen wir, wie gleich­sam die Gedanken aus der Erde herausquillen, um den Menschen vor­zubereiten zur zukünftigen Evolution.",
        "Wenn wir nach dem Westen schauen, so sehen wir aus dem Flüssigen herausquellen die Gedanken, die Kräfte, welche die Ätherleiber formen in der Aufeinanderfolge der Zeit."
      ],
      [
        "Und da sehen wir, wie geformt wurde schon in den alten Zeiten im Westen bis weit nach Mitteleuropa herein an dem Ätherleibe des Men­schen, so geformt wurde, daß dieser Ätherleib sein unmittelbares Leben leibhaft, lebendig, äußerlich auslebt."
      ],
      [
        "Was heißt das?",
        "Das heißt, meine lieben Freunde, es lebten in alten Zeiten in Europas Westen Menschen, welche ihre Lebensart so aus dem Ätherleibe heraus zutage brachten, wie jetzt, wo der Ätherleib schon gewirkt hat mit diesen alten Impulsen, der Mensch aus dem physischen Leibe heraus wirkt.",
        "Menschen lebten, die noch einen lebendigen Um­gang hatten mit der geistigen Welt, namentlich mit der elementarischen"
      ],
      [
        "Welt.",
        "Das gehört den alten Zeiten an.",
        "Diese Zeiten sind gewissermaßen schon vorüber, wo in der allerlebendigsten Weise die Genien des flüs­sigen Elementes zum Ätherleibe des Menschen im Westen sprachen.",
        "Wenn aber zu diesem Ätherleibe gesprochen wird, ist es anders als in unserer Zeit, wo vorzugsweise zum physischen Leibe des Menschen ge­sprochen wird.",
        "Zum physischen Leibe des Menschen wird so gespro­chen, daß auf seine Sinne Eindruck gemacht wird, daß er sich ein Wis­sen aneignet und gewisse Lebensgewohnheiten annimmt, die mit den Eindrücken der Sinne zusammenhängen."
      ],
      [
        "Bei diesen alten Menschen des Westens war es so, daß sie in ihren Lebensgewohnheiten, in dem, was innerlich in ihnen lebte, noch mehr mit der elementarischenWelt zusammenhingen.",
        "Bei den Kelten hat man solche Menschen, die geradeso wußten von der elementarischen Welt, wie wir heute wissen von der physischen Welt, Menschen, denen die elementarische Welt nicht verschlossen war, die von Naturgenien, von Wassergenien, von Erdengenien reden konnten, wie wir von den Bäu­men, Pflanzen, Bergen, Wolken reden, die unmittelbaren Umgang hat­ten mit diesen Naturgenien.",
        "Und die Eigenart des Lebens in Europa beruht darauf, daß das eben in der alten Zeit so gewesen ist, weil da­mals so, wie man heute durch die Sinne auf den physischen Leib wirkt, gewirkt wurde auf den ätherischen Leib des Menschen."
      ],
      [
        "Dann wurde weiter gewirkt allerdings gerade auf den ätherischen Leib des Menschen, aber daß dieser ätherische Leib so formiert, gebil­det wird, daß das Verhältnis der Genien des Flüssigen zu ihm sich mehr im Unterbewußtsein abspielt, daß mehr zurücktritt der bewußte Ver­kehr mit den Naturgeistern."
      ],
      [
        "Wodurch kam das zustande?",
        "Für Frankreich zum Beispiel kam das zustande dadurch, daß über die Welle der keltischen Entwickelung sich die Welle der romanischen Entwickelung zog, daß das keltische Ele­ment von dem romanischen durchsetzt wurde.",
        "In dem Zusammenfluß des Keltischen mit dem Romanischen haben wir zwei Impulse.",
        "Einen alten Impuls, der unmittelbar den Verkehr vermittelt zwischen der elementarischen Welt und dem Ätherleibe, und in dem neuen Impuls, in dem Einfluß des Romanischen haben wir dasjenige, was auch in den Ätherleib einzieht, aber so einzieht, daß es wie eine historische, eine"
      ],
      [
        "geschichtliche Welle ist, so daß das eintreten konnte, was ich in den früheren Vorträgen schon gesagt habe, daß in dem französischen Elemente ein Aufleben des alten griechischen Elementes stattfinden konnte."
      ],
      [
        "Will man diese westliche Menschenart richtig verstehen, so muß man diese verschiedenen Impulse, die auch in den Ätherleib einfließen, in der richtigen Weise taxieren.",
        "Und nun haben wir gewissermaßen von charakteristischen Erscheinungen in bezug auf die Einflüsse auf den physischen Leib und in bezug auf die Einflüsse auf den ätherischen Leib gesprochen.",
        "Anders stehen die Sachen, wenn wir die mittlere Re­gion ins Auge fassen.",
        "Da liegen die Sachen etwas anders.",
        "Da haben wir es zu tun mit etwas, ich möchte sagen, viel Unausgesprochenerem, mit etwas, was sich weniger deutlich charakterisieren läßt.",
        "Da haben wir es zu tun damit, daß sowohl Geister der Erde wie Geister des flüssigen Elementes unmittelbar auf den physischen Leib einwirken."
      ],
      [
        "Sie sehen, es ist ein Übergang.",
        "Hier, im Westen, wirken unmittelbar Geister des flüssigen Elementes auf den Ätherleib.",
        "Die Geister des flüs­sigen Elementes lassen nach, in Mitteleuropa, und es gesellen sich zu ihnen gewisse Geister des irdischen Elementes.",
        "Sie wirken auf den phy­sischen Leib unmittelbar; weniger stark auf den Ätherleib.",
        "Die Geister des irdischen Elementes verfeinern den physischen Leib, wenn Sie wei­ter nach Osten gehen.",
        "Daher haben wir irgendwie mit Mitteleuropa zusammenhängend all dasjenige, was Europa durch lange Zeit mit sol­chen physischen Leibern versorgt, die zugänglich sind dem flüssigen Elemente und dem festen Elemente, und daher sehen wir, wie sich kom­plizieren muß dasjenige, was in die Menschheitsevolution einfließt.",
        "Wir sehen, wie aus diesem Fonds, diesem Reservoir, das Volk der Franken, vorbereitet, wie ich es geschildert habe, durch die Genien des Flüssigen und des Festen, sich wieder hineinschiebt in das keltisch-romanische Volkselement; und dann erst entsteht dasjenige, was uns entgegen­getreten ist als das Wirksame in der Menschheitsevolution."
      ],
      [
        "Die Franken, die zurückbleiben, behalten damit die Eigentümlich­keit, die Eigenschaft, vorzugsweise in dem physischen Leibe dasjenige aufzunehmen - die Sachsen sind damit verwandt -, was von den flüs­sigen und irdischen Geistern ausgeht.",
        "Die Franken, die nach dem Westen"
      ],
      [
        "zogen, vereinigten ihr Wesen mit demjenigen Wesen, das aus dem un­mittelbaren Einfluß der Genien des Meeres kommt, was dadurch noch bedeutsamer wird, daß es aufnimmt das Historische des romanischen Elementes."
      ],
      [
        "So schieben sich die Impulse ineinander und so können wir begrei­fen, wie, vor allen Dingen wenn wir Westeuropa charakterisieren wol­len, wir gar nicht anders zu einem Verständnis kommen, als wenn wir Rücksicht auf alles dasjenige nehmen, was in den ätherischen Leib ein­greift."
      ],
      [
        "Wenn wir Mitteleuropa charakterisieren wollen, so müssen wir sagen, da kommt es mehr auf den physischen Leib an, kommt es mehr darauf an, was im physischen Leibe konfiguriert wird.",
        "Nun sehen wir, wie sich solche Impulse, wie die ausgesprochenen, in gewissen Zentren gleichsam konzentrieren, wie sie charakteristisch hervortreten in gewissen Zen­tren."
      ],
      [
        "Zwei solcher Zentren, die sich wirklich charakteristisch zueinan­der verhalten, sind gegeben in Mitteleuropa auf der einen Seite und in den britischen Inseln auf der andern Seite.",
        "In Mitteleuropa, wo es am stärksten zum Ausdrucke kommt, haben wir dasjenige, was ich das feste Element genannt habe und wo einfließt in den physischen Leib das, was von den Genien des Flüssigen und von den Genien des Festen kommt, wo sich das also vermischt, und auf den britischen Inseln, wo - in ge­wisser Weise stärker, als das zum Beispiel in Frankreich der Fall ist -in die ätherischen Leiber vorzugsweise hineinwirkt das, was von den Genien des flüssigen Elementes kommt."
      ],
      [
        "Das hat bewirkt, daß auf die­sen zwei Gebieten Menschen leben, die im Grunde genommen dieselben Impulse in sich tragen; nur die einen tragen sie im physischen Leibe und sind zu alledem geeignet, was mit dem Wirken dieser Genien im phy­sischen Leibe zusammenhängt; die andern, auf den britischen Inseln, tragen sie im Ätherleibe und sind dadurch berufen, alles dasjenige zu bewirken, was mit den Impulsen des ätherischen Leibes zusammen­hängt.",
        "Wenn ich das grotesk sagen darf, so könnte ich sagen, wenn man einen Deutschen und einen Engländer zusammenstellt, so merkt man den Unterschied, wenn man sie als physische Leiber betrachtet."
      ],
      [
        "Man merkt erst die Ähnlichkeit, wenn man den physischen Leib des Deut­schen mit dem ätherischen Leibe des Engländers zusammenstellt."
      ],
      [
        "tritt erst dasjenige hervor, was uns zeigt, daß dieselben Impulse da leben, richtig dieselben Impulse da leben."
      ],
      [
        "Sie sehen, was in der äußeren Anschauung, die bei der äußeren Phan­tasmagorie bleibt, ich möchte sagen, karikiert hervortritt.",
        "Mißverstehen Sie das Wort nicht.",
        "Das tritt einem in seiner wahren Gestalt erst ent­gegen, wenn man das, was Lebensgrundlage wird, was die Wahrheit ist, ins Auge faßt.",
        "Aber weil in der Welt die Wesenheiten zusammenwirken müssen, weil es gar nicht anders sein kann, als daß die Wesenheiten zu­sammenwirken, denn die Welt ist ein Ganzes, so muß das so sein, daß auf der einen Seite gewisse Impulse durch den physischen Leib, auf der an­dern Seite durch den Ätherleib wirken.",
        "Ich möchte sagen, das gehört sich so.",
        "Dadurch entsteht das entsprechende wirkliche Zusammenwirken."
      ],
      [
        "Dadurch, sehen Sie, ist dasjenige gekommen, was in der geistigen Welt erscheint als ein ganz besonderes Verhältnis zwischen der deut­schen Welt und der britischen Welt.",
        "Ich habe dieses ganz besondere Verhältnis für den Osten und Westen in einer vorigen Stunde ausein­andergelegt, indem ich Ihnen gezeigt habe, wie für den Osten und Westen ein gewisser Kampf stattfindet in der geistigen Welt, durch die Verschiedenheit bewirkt der Seelen, die aus einem östlichen und der Seelen, die aus einem westlichen Leibe kommen."
      ],
      [
        "Dasjenige, was durch die eben geschilderten Verhältnisse bewirkt wird, ist etwas anderes.",
        "Ich bitte Sie, auch das, was ich heute zu sagen habe, nicht so zu nehmen, als ob man es verstandesgemäß oder speku­lierend nehmen kann.",
        "Man muß da schon in der geistigen Welt beob­achten, sonst wird man nicht auf das Richtige kommen können.",
        "Es bildet sich nach und nach heraus ein Zusammenklang zwischen dem, was von Mitteleuropa und den britischen Inseln zurückwirkt, eine Har­monie, ein richtiges geistiges Bündnis, das allmählich eine solche Stär­kung erfahren hat, daß man sagen kann, geistig gefaßt, lieben sich heute keine Erdenseelen mehr als die Erdenseelen Mitteleuropas und die Er­denseelen der britischen Inseln.",
        "Es ist da die stärkste Liebe, geistig ge­faßt, vorhanden, und das drückt sich äußerlich in dem aus, was wir jetzt vor uns sehen.",
        "So verwickelt sind die Dinge."
      ],
      [
        "Man würde solche Dinge wahrhaft nicht aussprechen, wenn sie nur auf einer leicht fundierten Erkenntnis beruhten, wenn man sie sich"
      ],
      [
        "nicht durch schmerzlichste Erfahrungen errungen hätte.",
        "Glauben Sie nicht, daß Sie schablonisieren dürfen, indem Sie denken, daß jedes Bündnis in der physischen Welt ein Krieg in der geistigen Welt ist, und ein Krieg in der physischen Welt ein Bündnis in der geistigen Welt.",
        "Die Dinge sind so, wie ich sie Ihnen geschildert habe.",
        "Und daß das als Kampf zum Ausdruck kommt, ist der Ausdruck in der heutigen mate­rialistischen Kultur für die Schwierigkeit, die Sache im Geistigen wirk­lich auszuleben."
      ],
      [
        "Es sträubt sich unsere Zeit nicht nur in Worten, sondern auch in Taten, das anzuerkennen, was in der geistigen Welt vorhanden ist.",
        "Sie versucht, das Gegenteil dessen hinzustellen, was in der geistigen Welt vorhanden ist, weil sich das materialistische Zeitalter gegen die An­erkennung des Geistigen auch in Taten sträubt.",
        "Und so wird das, wohin die geistige Welt tendiert - nämlich nach der Harmonie des im Phy­sischen Errungenen in Mitteleuropa und des im Ätherischen Errungenen auf den britischen Inseln -, in der Maja übertönt durch das, was man heute als Kampf und gegenseitigen Haß vor sich hat."
      ],
      [
        "Sehen Sie, es lohnt sich schon für diejenigen, die keine Geisteswissen­schafter sind, uns für Narren zu halten, da die Erkenntnisse, die aus der geistigen Welt dringen, gar sehr widersprechen dem, was man auf der physischen Welt beobachten kann.",
        "Aber dessen können wir uns doch versichert halten, daß die Fortentwickelung der Menschheit davon ab­hängt, daß wirklich die geistigen Wahrheiten durchdringen werden, daß wirklich die Menschen hinter die Sinneswelt sehen lernen.",
        "Dazu sind Ereignisse notwendig, von denen ich mehr oder weniger deutlich in diesen Tagen gesprochen habe."
      ],
      [
        "Man darf froh sein, daß das Karma uns hier zusammengeführt hat in einem neutralen Gebiete, wo es geht, so rückhaltlos über diese Dinge zu sprechen, denn es ist nicht ganz leicht, gerade heute über diese Dinge zu sprechen.",
        "Aber für die Geisteswissenschafter ist es gut, sich in diese Dinge hineinzufinden, weil sie betrachten dürfen dasjenige, was in der äußeren Welt geschieht, gerade als Ansporn dafür, hinter den Schleier zu schauen.",
        "Es müßte vieles ganz unverständlich bleiben, wenn man nicht hinter diesen Schleier schauen könnte.",
        "Die Dinge bekommen erst ihre volle Bedeutung, wenn man hinter diesen Schleier sieht."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "DIE WELT ALS ERGEBNIS VON GLEICHGEWICHTSWIRKUNGEN VIERTER VORTRAG Dornach, 20. November 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Es ist uns durch unsere Betrachtungen schon geläufig geworden, daß wir unter oder hinter der physischen Welt, die vor uns liegt, den Beginn anderer Welten finden. Ich möchte heute als Einleitung von einigen Eigentümlichkeiten dieser geistigen Welten sprechen, von denen wir zum Teil schon wissen, die wir durch manches ergänzen wollen, um auch sonstiges noch vor die Seele zu rücken.",
      "Sie wissen, die nächste Welt, welche an die unsrige angrenzt, ist die sogenannte imaginative Welt. Diese Welt ist in sich viel beweglicher als unsere physische Welt. Unsere physische Welt stellt sich dar mit schar­fen Konturen, scharfen Grenzlinien, stellt eine Welt scharf umrissener Gegenstände dar.",
      "Eine gleichsam flüssige, flüchtige Welt ist diejenige, in die wir hineinkommen, wenn wir den Schleier zerreißen, den die physische Welt bildet. Auch wissen wir, daß gegenüber dieser ersten geistigen Welt das Gefühl, die Empfindung beginnt, daß wir außerhalb unseres physischen Leibes sind.",
      "Zu diesem unserem physischen Leib be­kommen wir in dem Augenblicke, wo wir in die geistige Welt hinauf­steigen, gewissermaßen ein neues Verhältnis, ein Verhältnis, wie wir es innerhalb des physischen Leibes etwa haben zu unseren Augen oder zu unseren Ohren. Der physische Leib wirkt mehr als ein Ganzes wie eine Art Wahrnehmungsorgan, aber wir merken sehr bald, es handelt sich eigentlich nicht richtig um den physischen Leib, wenn uns so dieser physische Leib als eine Art Wahrnehmungsorgan zum Gefühl kommt, sondern es handelt sich da um den ätherischen Leib.",
      "Der physische Leib gibt uns gleichsam nur ein Gerüst, das den ätherischen Leib hält. Wir blicken von außerhalb nach unserem ätherischen Leibe hin, verspüren ihn auch noch, verspüren ihn als das Sinnesorgan, das eine Welt wahr­nimmt webender, schwebender Bilder und Töne.",
      "Wie unser Verhältnis zum Ohr und Auge, so wird unser Verhältnis zu dem vom physischen Leibe gehaltenen Ätherleibe.",
      "Wenn wir uns nun so außerhalb unseres physischen Leibes fühlen, so ist dieses Erlebnis ähnlich dem Schlaferlebnis. Das Schlaferlebnis",
      "besteht darin, daß wir mit unserer geistig-seelischen Menschlichkeit außerhalb unseres physischen und Ätherleibes sind, nur daß während des Schlaferlebnisses unser Bewußtsein herabgestimmt ist, und wir nichts wissen von dem, was eigentlich mit uns und um uns vorgeht. Man kann also sagen, daß es noch ein anderes Verhältnis des Menschen zu seinem physischen Leibe gibt als dasjenige, woran wir gewohnt sind. Auf das, worauf die Geisteswissenschaft so aufmerksam machen muß, wird die Menschheit durch ihre Evolution immer mehr und mehr hin­gelenkt werden, je weiter wir der Zukunft entgegengehen.",
      "Ich habe es aus vielen Zusammenhängen heraus betont, daß es nicht eine Willkür ist, daß wir heute Geisteswissenschaft treiben, sondern daß die Beschäftigung mit dieser Geisteswissenschaft von uns gefordert wird durch die Evolution der Menschheit, durch das, was im gegen­wärtigen Zeitpunkte in der Menschheitsevolution sich vorbereitet. Man kann nämlich dieses gleichsam Sich-Getrenntfühlen in seiner mensch­lichen Wesenheit von seinem physischen Leibe als etwas bezeichnen, was wie ein unverstandenes Erlebnis immer mehr und mehr über die Menschen wie von selbst kommen wird, je weiter wir als Menschheit der Zukunft entgegengehen.",
      "Es wird eine Zeit kommen, wo an viele, viele Menschen immer mehr die Empfindung herantreten wird: Ja, was ist denn das, ich fühle mich so, wie wenn ich mich gespalten hätte, wie wenn da noch ein Zweiter neben mir wäre. - Und diese Empfindung, dieses Gefühl, das als etwas Natürliches auftreten wird, geradeso wie Hunger oder Durst oder andere Erlebnisse, darf nicht unverstanden bleiben bei den Menschen der Gegenwart und Zukunft. Verständlich wird es sein, wenn die Menschen sich bequemen werden, durch die Geisteswissenschaft die eigentliche Bedeutung dieses Gespaltenseins zu verstehen.",
      "Insbesondere wird auch die Pädagogik, die Erziehung, je mehr wir diesen Dingen entgegengehen, darauf Rücksicht nehmen müs­sen. Man wird lernen müssen, auf gewisse Erlebnisse der Kinder sorg­fältiger zu achten, als man das bisher getan hat, wo diese Erlebnisse auch nicht in demselben Maße da waren.",
      "Gewiß, in dem späteren, robusteren Leben, unter dem Eindrucke der physischen Welt werden diese Gefühle und Empfindungen, die ich cha­rakterisiert habe, nicht so besonders stark sein in der allernächsten Zukunft,",
      "aber in einer ferneren Zukunft werden sie immer stärker und stärker werden. Zunächst werden sie beim heranwachsenden Kinde auftreten, und die Erwachsenen werden von den Kindern gar mancher­lei hören, was sie werden verstehen müssen, mancherlei, über das man hinweggehen kann wie über ein Nichts, über das man aber nicht hinweggehen sollte, weil es mit den tiefsten Evolutionsgeheimnissen der Welt zusammenhängt.",
      "Kinder werden andeuten: Da oder dort habe ich ein Wesen gesehen, das hat zu mir dies oder jenes gesagt, was ich tun soll. - Der materia­listisch gesinnte Mensch wird sagen: Du bist ein dummer Bub oder ein dummes Mädchen, das gibt es ja gar nicht. - Wer aber Geisteswissen­schaft verstehen will, muß wissen lernen, daß es sich da um eine bedeut­same Erscheinung handelt. Wenn ein Kind sagt: Da habe ich jemanden gesehen, der ist wieder verschwunden, aber er kommt immer wieder und wieder; er sagt zu mir immer das und jenes, und ich kann nicht aufkommen gegen ihn -, so wird der, welcher die Geisteswissenschaft versteht, erkennen, daß sich da etwas in dem Kinde ankündigt, was immer deutlicher in der Menschheitsevolution hervortreten wird. Was ist denn das, was sich da ankündigt?",
      "Wir werden es verstehen, wenn wir zwei Grunderlebnisse des Men­schen ins Auge fassen, von denen das erste ganz besonders wichtig war für den vierten nachatlantischen, den griechisch-lateinischen Zeitraum, und das andere wichtig ist für unseren Zeitraum, in dem es sich langsam erst vorbereitet. Während das erste Grunderlebnis in dem griechisch lateinischen Zeitraum seinen Abschluß gefunden hat, gehen wir dem zweiten langsam entgegen. In das menschliche Leben spielen immer Er­lebnisse herein, die von Luzifer und Ahriman stammen. In das Grund-erlebnis der vierten nachatlantischen Periode spielte insbesondere Luzi­fer herein; in unsere Periode spielt Ahriman herein und bedingt das Grunderlebnis. Nun hängt Luzifer mit alledem zusammen, was noch nicht bis zur Deutlichkeit der einzelnen Sinne sich ausgewachsen hat, was undeutlich an den Menschen, undifferenziert an ihn herankommt. Mit andern Worten, Luzifer hängt mit dem Atemerlebnis zusammen, mit dem Erlebnis des Ein- und Ausatmens. Das Atmen des Menschen ist etwas, was in einem ganz bestimmten geregelten Verhältnis stehen",
      "muß zu seiner Gesamtorganisation. In dem Augenblick, wo der At­mungsprozeß in irgendeiner Weise gestört ist, verwandelt sich sogleich die Atmung aus dem, wie sie sonst auftritt, nämlich als unbewußter Vorgang, auf den wir nicht zu achten brauchen, in einen bewußten, in einen mehr oder weniger traumhaft bewußten Vorgang. Und wenn -wir können es ganz trivial ausdrücken - der Atmungsprozeß zu ener­gisch wird, wenn er größere Anforderungen an den Organismus stellt, als dieser Organismus leisten kann, dann hat Luzifer die Möglichkeit, mit dem Atmen einzudringen in den menschlichen Organismus. Er muß es ja nicht selbst sein, aber seine Scharen tun es, diejenigen, die zu ihm gehören.",
      "Ich weise damit auf eine Erscheinung hin, welche jeder kennt als Traumerlebnis. Dieses Traumerlebnis kann sich in beliebiger Weise steigern. Der Alptraum, wo also der Mensch durch das gestörte Atmen zum Traumbewußtsein kommt, so daß sich Erlebnisse der geistigen Welt hineinmischen können, und auch alle Angst- und Furchterlebnisse, die mit Alpträumen verbunden sind, haben in dem luziferischen Element der Welt ihren Ursprung. Alles, was vom gewöhnlichen Atmungs­prozeß übergeht zum Würgen, zu dem Gefühl des Gewürgtwerdens, das hängt zusammen mit dieser Möglichkeit, daß Luzifer sich einmischt in den Atmungsprozeß. Das ist der grobe Prozeß, wo durch eine Herabminderung des Bewußtseins Luzifer sich in das Atemerlebnis hineinmischt, gestaltenhaft in das Traumbewußtsein tritt und da zum Würger wird. Das ist das grobe Erlebnis.",
      "Es gibt aber auch ein feineres Erlebnis, das uns dieses Würgeerlebnis gleichsam verfeinert, nicht so grob wie ein physisches Würgen darstellt. Man achtet gewöhnlich nicht darauf, daß eine solche Verfeinerung des Würgens zu den menschlichen Erlebnissen gehört. Aber jedesmal, wenn an die menschliche Seele dasjenige herantritt, was zu einer Frage wird oder zu einem Zweifel an diesem oder jenem in der Welt, dann ist in verfeinerter Weise ein Würgeerlebnis da. Man kann schon sagen: Wenn wir eine Frage aufstellen müssen, wenn ein kleines oder ein großes Wel­tenrätsel sich uns aufdrängt, dann werden wir gewürgt, aber so, daß wir es nicht merken. - Jeder Zweifel, jede Frage ist ein verfeinertes Alpdrücken oder ein verfeinerter Alptraum.",
      "So verwandeln sich die Erlebnisse, die uns sonst grob entgegentreten, in feinere Erlebnisse, wenn sie mehr seelisch auftreten. Man kann sich schon denken, daß die Wissenschaft einmal dazu kommen wird, den Zusammenhang des Atmungsprozesses mit der Fragestellung oder der Empfindung eines Zweifels in der Menschenseele zu studieren. Aber auch alles das, was mit Fragen und Zweifeln zusammenhängt, alles das, was damit zusammenhängt, daß wir unbefriedigt sind, weil die Welt an uns herantritt und eine Antwort verlangt, oder weil wir gezwungen sind, eine Antwort zu geben durch das, was wir sind, hängt mit dem Luziferischen zusammen.",
      "Wenn wir nun die Sache geisteswissenschaftlich betrachten, so kön­nen wir sagen: Bei allem, wo der Würgeengel im Alptraum uns be­drückt, oder wo wir durch die Fragestellung eine innere Bedrückung, einen Anflug von Beängstigung erfahren, haben wir es mit einem gleich­sam stärkeren, energischeren Atmungsprozeß zu tun, mit etwas, was im Atem lebt, was aber, damit die menschliche Natur in der richtigen Weise funktioniert, harmonisiert, abgeschwächt werden muß, damit das Leben richtig verläuft. Was findet nun statt, wenn ein energischerer Atmungsprozeß eintritt? Da ist gleichsam der Ätherleib und alles, was mit der ätherischen Natur des Menschen zusammenhängt, zu weit aus­gedehnt, zu sehr auseinandergedrängt, und da sich das dann auslebt im physischen Leibe, so kann es sich nicht auf den physischen Leib beschränken, es will ihn gewissermaßen auseinanderzerren. Ein zu üppiger, ein zu weit ausgedehnter Ätherleib liegt einem verstärkten Atmungsprozeß zugrunde, und dann besteht die Möglichkeit für das luziferische Element, sich besonders geltend zu machen.",
      "Man kann also sagen: Das Luziferische kann sich in die menschliche Natur hineinschleichen, wenn der Ätherleib geweitet ist. - Man kann auch sagen: Das Luziferische hat die Tendenz, in einem der mensch­lichen Form gegenüber geweiteten Ätherleibe sich auszudrücken, also in einem Ätherleibe, der mehr Raum braucht, als in der menschlichen Haut eingeschlossen ist, der die Form üppiger gibt. - Man kann sich nun denken, daß man künstlerisch diese Frage beantworten will, und da kann man sagen: So wie der menschliche Ätherleib normal ist, ist er der Bildner der menschlichen Gestalt, die physisch vor uns steht. Aber",
      "sobald er sich weitet, sobald er sich einen größeren Raum, weitere Gren­zen verschaffen will, als in der menschlichen Haut darinnen sind, will er auch andere Formen geben. Es kann da nicht die menschliche Form bleiben. Er will überall über die menschliche Form hinaus. - Dieses Problem hat man in alter Zeit schon gelöst. Was für eine Form kommt da heraus, wenn der geweitete Ätherleib, der nicht für das menschliche Wesen, sondern für das luziferische Wesen paßt, sich Geltung ver­schafft und formhaft vor die menschliche Seele tritt? Was kommt da heraus? Die Sphinx!",
      "Hier haben wir eine besondere Art, uns in die Sphinx hinein zu ver­tiefen. Die Sphinx ist es, was eigentlich an einem würgt. Wenn der Ätherleib des Menschen durch die Energie des Atmens sich ausweitet, taucht ein luziferisches Wesen in der Seele auf. Es lebt in diesem Äther-leibe nicht die menschliche Gestalt, sondern die luziferische Gestalt, die Sphinxgestalt. Die Sphinx taucht auf als die Zweifelaufwerferin, als die Fragepeinigerin. Diese Sphinx hat also eine besondere Beziehung zum Atmungsprozeß. Wiederum wissen wir aber, daß der Atmungs-prozeß eine besondere Beziehung zur Blutbildung hat. Daher lebt das Luziferische auch im Blute, durchwogt und durchwallt das Blut. Überall kann auf dem Umwege durch die Atmung das Luziferische in das Blut des Menschen hinein, und wenn zuviel Energie in das Blut hineinkommt, dann ist das Luziferische, die Sphinx, besonders stark.",
      "So steht der Mensch dadurch, daß er in seinem Atmungsprozeß dem Kosmos geöffnet ist, der Sphinxnatur gegenüber. Dieses Erlebnis, in seinem Atmen der Sphinxnatur des Kosmos gegenüberzustehen, dieses Grunderlebnis ging besonders in der vierten nachatlantischen, der grie­chisch-lateinischen Kulturperiode auf. Und in der Ödipus-Sage sehen wir, wie der Mensch der Sphinx gegenübersteht, wie die Sphinx sich an ihn kettet, zur Fragepeinigerin wird. Der Mensch und die Sphinx, oder wir können auch sagen, der Mensch und das Luziferische im Weltall soJlten gleichsam als ein Grunderlebnis der vierten nachatlantischen Kulturperiode so hingestellt werden, daß,wenn der Mensch sein äußeres normales Leben auf dem physischen Plan nur ein wenig durchbricht, er mit der Sphinxnatur in Berührung kommt. Da tritt Luzifer in seinem",
      "Leben an ihn heran, und er muß mit Luzifer, mit der Sphinx fertig werden.",
      "Anders ist das Grunderlebnis des fünften nachatlantischen Kultur­zeitraumes, unseres Zeitraumes. Für unseren Zeitraum ist das besonders vorbereitet, daß der Ätherleib nicht aufgeplustert, nicht ausgedehnt, sondern zusammengezogen ist, daß er nicht zu groß, sondern eher zu klein ist, und das wird immer stärker und stärker werden, je weiter die Evolution fortgeht. Wenn wir sagen können: Die normale Gestalt des",
      "# Bild s. 103",
      "Menschen beim Griechen ist so, daß der Ätherleib zu groß ist -, so können wir sagen: Beim modernen Menschen ist es so, daß der Äther-leib sich zusammenschnürt, sich zusammenzieht, zu klein wird. - Je weiter der Mensch kommen wird in der materialistischen Verachtung des Spirituellen, desto mehr wird sich dieser Ätherleib zusammen­ziehen und austrocknen. Da aber die Durchorganisierung des physi­schen Leibes davon abhängt, daß der Ätherleib ihn ganz richtig durch­dringt, so wird für den physischen Leib immer eine Tendenz auftreten, wenn der Ätherleib zu sehr zusammengedrängt ist, daß der physische Leib auch auszutrocknen beginnt. Und wenn er ganz besonders stark austrocknen würde, so würde er statt der natürlichen Menschenfüße hornartige Füße bekommen. Der Mensch wird sie ja nicht bekommen,",
      "aber die Tendenz dazu liegt in ihm, und sie ist begründet in dieser Ten­denz des Ätherleibes, auszutrocknen, zu wenig Ätherkraft zu ent­wickeln. In diesen vertrockneten Ätherleib kann sich nun besonders Ahriman hineinleben, wie Luzifer in den erweiterten Ätherleib. Ahri­man wird die Gestalt annehmen, die auf eine Ärmlichkeit des Ätherleibes hinweist. Er wird zu wenig Ätherkraft entwickeln, um richtig organisierte Füße zu haben, und die erwähnten hornartigen Füße -Bocksfüße - ausbilden.",
      "Mephistopheles ist ja Ahriman; er hat die Bocksfüße nicht umsonst, er hat die Bocksfüße aus diesem Grunde, den ich angedeutet habe. Die Mythen und Sagen sind eben sehr bedeutungsvoll; deshalb erscheint Mephistopheles sehr oft mit Pferdefüßen, wo also die Füße zu Hufen vertrocknet sind. Wenn Goethe das Problem des Mephisto schon voll­ständig durchdrungen hätte, so hätte er nicht seinen Mephisto wie einen modernen Kavalier auftreten lassen, denn es gehört schon einmal zum Wesen des Ahriman-Mephisto, nicht so viel Ätherkraft zu haben, daß er die menschliche physische Gestalt vollständig durchorganisieren kann.",
      "Aber noch eine Eigentümlichkeit ist dadurch hervorgerufen, daß der Ätherleib gleichsam zusammengezogen ist, ärmer ist an Ätherkräften, als es im Normalen der Fall ist. Diese Eigentümlichkeit wird uns am klarsten, wenn wir einen Blick auf die gesamte menschliche Natur wer­fen. Wir sind in gewisser Beziehung schon physisch eine Zweiheit. Denken Sie doch, wenn Sie so dastehen, sind Sie eben der physische Mensch. Aber zu dem physischen Menschen gehört es, daß die Atemluft immerfort in ihm darinnen ist. Diese Atemluft jedoch ist bei dem näch­sten Ausatmen schon wieder nach außen befördert, so daß der Atem­luftmensch, der Sie durchdringt, fortwährend wechselt. Sie sind nicht bloß das, was aus Muskeln und Knochen besteht, der Fleisch- und Knochenmensch, sondern Sie sind auch der Atemmensch. Der aber wechselt fortwährend, geht hin und her, aus und ein. Und der Atem-mensch ist es, der wieder im Zusammenhang steht mit dem immerfort zirkulierenden Blute.",
      "Wie getrennt von diesem ganzen Atmungsmenschen liegt in Ihnen der Nervenmensch, der andere Pol, in dem das Nervenfluidum zirkuliert,",
      "und es ist nur eine Art äußere Berührung, ein äußeres Zusammen­kommen zwischen dem Nervenmenschen und dem Blutmenschen. So wie nur diejenigen Ätherkräfte, die nach dem Luziferischen hin ten­dieren, durch das Atmen leicht an das Blutsystem herankommen kön­nen, so können die Ätherkräfte, welche nach dem Mephistophelischen oder Ahrimanischen hin tendieren, nur an das Nervensystem heran­kommen, aber nicht an das Blutsystem. Ahriman ist es versagt, in das Blut unterzutauchen; er kann fortwährend in den Nerven leben, bis zum Vertrocknen, zur Nüchternheit leben, weil er nicht an die Wärme des Blutes heran kann. Will er aber eine Beziehung zur Menschennatur hin entwickeln, dann wird er lechzen müssen nach einem Tröpfchen Blut, weil er so schwer herankommen kann an das Blut. Ein Abgrund liegt zwischen Mephistopheles und dem Blute. Will er an den Menschen herankommen, an das, was im Menschen lebt, will er mit dem Menschen in Verbindung treten, dann wird er gewahr, daß das Menschliche in dem Blute lebt. Er muß nach dem Blute trachten.",
      "Sehen Sie, damit hängt zusammen die Weisheit der Mephistopheles-Sage, daß die Verschreibung mit Blut geschieht. Faust muß sich dem Mephisto durch das Blut verschreiben, weil dieser nach dem Blute lech­zen muß, weil er abgetrennt ist vom Blute. Geradeso wie der griechische Mensch der Sphinx gegenüberstand, die im Atmungssystem lebt, so steht der Mensch des fünften nachatlantischen Kulturzeitraumes dem Mephistopheles gegenüber, der im Nervenprozesse lebt, der kalt und nüchtern ist, weil er an Blutleere leidet, weil die Wärme des Blutes ihm fehlt. Und dadurch wird er zum Spötter, zum nüchternen Begleiter des Menschen.",
      "Wie Ödipus mit der Sphinx, so hat der Mensch der fünften nach-atlantischen Kulturepoche mit Mephistopheles fertigzuwerden. Er steht diesem Mephistopheles wie einem zweiten Wesen gegenüber. Der Grie­che stand der Sphinx durch den energisch gewordenen Blut- und At­mungsprozeß gegenüber; ihm stand gegenüber, was mit der energische-ren Atmung in seine Natur hineinkam. Der moderne Mensch steht mit allem, was aus seinem Verstande, seiner Nüchternheit drängt, dem gegenüber, was an den Nervenprozeß gebannt ist. Prophetisch konnte dieses Gegenüberstehen des Menschen dem Mephistophelischen, ich",
      "möchte sagen, dichterisch vorausgeahnt werden. Aber es wird immer mehr und mehr heraufziehen als ein Grunderlebnis, je weiter wir in der Evolution des fünften nachatlantischen Zeitraumes kommen. Und das, wovon ich erzählt habe, daß es im kindlichen Erlebnisse auftreten wird, wird dieses mephistophelische Erlebnis sein.",
      "Während der griechische Mensch unter der Pein einer Überfülle von Fragen gestanden hat, wird der moderne Mensch nicht so sehr einer Fragepein entgegengehen als vielmehr der Pein, in seine Vorurteile hin­ein verzaubert zu sein, einen zweiten Leib neben sich zu haben, der seine Vorurteile enthält. Und wie bereitet sich das vor?",
      "Betrachten Sie einmal ganz unbefangen die Evolution. Wieviel hat im Verlaufe des fünften nachatlantischen Kulturzeitalters aufgehört, in warmer unmittelbarer Weise an den Menschen heranzutreten. Nehmen Sie die unzähligen Fragen, die wirklich an uns herantreten, wenn wir uns in die Geisteswissenschaft vertiefen.",
      "Sie sind alle für den modernen materialistisch gesinnten Menschen nicht da. Das Rätsel der Sphinx empfindet er nicht; das hat der Grieche noch in lebendiger Weise emp­funden. Der moderne Mensch wird aber ein anderes empfinden müssen.",
      "Er weiß eigentlich alles so gut nach seiner Meinung, beobachtet die Sinneswelt, kombiniert sie mit seinem Verstande, und dann lösen sich ihm alle Rätsel. Er ahnt nicht, wie sehr er in der äußeren Phantasma­gorie herumtappt.",
      "Das aber verdichtet immer mehr seinen Ätherleib, trocknet immer mehr seinen Ätherleib aus und führt endlich dazu, daß das mephistophelische Element wie eine zweite Natur sich heften wird an das Wesen des Menschen der Gegenwart in die Zukunft hinein. Alles das, was an materialistischen Vorurteilen, an materialistischer Beschränktheit sich entwickelt, wird die mephistophelische Natur ver­stärken, und wir können jetzt schon sagen: Wir sehen in eine Zukunft hinein, wo jeder geboren wird mit einem zweiten Menschen, welcher sagen wird, die da von der geistigen Welt reden, sind Narren.",
      "Ich weiß alles, ich verlasse mich auf meine Sinne. - Gewiß, der Mensch wird ab­weisen, so wie das Sphinxrätsel, auch das Mephistopheles-Rätsel, aber er wird heften an seine Fersen ein zweites Wesen. Das wird ihn so be­gleiten, daß er den Zwang empfinden wird, materialistisch zu denken nicht durch sich, sondern durch ein zweites Wesen, das sein Begleiter ist.",
      "Die materialistische Gesinnung wird den Ätherleib vertrocknen, und in dem vertrockneten Ätherleib wird Mephistopheles leben. Das wer­den wir verstehen müssen, und die Menschheit wird dem Kinde in zu­künftigen Zeiten so viel an Bildung mitgeben müssen - sei es durch Eurythmie, sei es durch geisteswissenschaftliche Gesinnung -, durch welche der Ätherleib belebt werden muß, daß der Mensch seine richtige Stellung wird einnehmen können, daß er erkennen wird, was sein Be­gleiter bedeutet. Sonst wird er diesen Begleiter nicht verstehen, sonst wird er sich ihm gegenüber fühlen, wie wenn er verzaubert, gebannt wäre. Wie der Grieche mit der Sphinx hat fertig werden müssen, so wird der moderne Mensch mit Mephistopheles fertig werden müssen, mit der satyrhaften, faunhaften Gestalt, die Bocks- oder Pferdefüße hat.",
      "Man kann schon sagen: Ein jedes Zeitalter weiß dasjenige, was sein Charakteristisches ist, in eine Grund- oder Ursage zu fassen. - Solche Grund- oder Ursagen sind die Ödipus-Sage in Griechenland und die Mephistopheles-Sage in der neueren Zeit. Aber diese Dinge müssen möglichst aus den Fundamenten heraus wirklich verstanden werden. Sie sehen, was sonst nur als Dichtung auftritt - die Auseinander­setzungen von Faust und Mephisto -, das wird, man möchte sagen, zum Fundament für die Zukunftspädagogik. Das Vorspiel davon besteht darin, daß das Volk oder der Dichter den Begleiter geahnt haben. Aber das Nachspiel wird darin bestehen, daß ein jeder Mensch diesen Be­gleiter haben wird, der ihm nicht unverständlich bleiben darf, und daß dieser Begleiter am lebendigsten, am mächtigsten in der Kindheit des Menschen auftreten wird. Und wenn die erwachsenen Erzieher nicht die richtige Stellung einnehmen werden gegenüber dem, was das Kind äußert, dann wird durch das unverstandene Gegenüberstehen den Ver­zauberungen des Mephistopheles die menschliche Natur verdorben werden.",
      "Es ist sehr merkwürdig, daß man in der Sagen- und Märchenlitera­tur, wenn man sie verfolgt, überall diese Züge finden kann. Sagen und Märchen, die so unverständig von den Gelehrten unserer Gegenwart betrachtet werden, weisen ihrer Struktur nach entweder nach dem Mephistophelischen, dem Ahrimanischen hin, oder nach dem Sphinx-artigen, dem Luziferischen. Alle Sagen und Märchen rühren davon her,",
      "daß ihr Inhalt ursprünglich entweder durch das Verhältnis, das der Mensch zur Sphinx hat, erlebt worden ist oder durch das Verhältnis, das der Mensch zu Mephisto hat. In den Sagen und Märchen finden wir mehr oder weniger verborgen auttreten entweder das Fragemotiv: das ist das Sphinxmotiv, das Motiv, daß irgend etwas gelöst werden muß, daß eine Frage beantwortet werden muß, oder das Motiv der Verzau­berung, des Gebanntseins an irgend etwas: das ist das mephistophe­lische, das ahrimanische Motiv. Denn worin besteht das ahrimanische Motiv im genaueren? Es besteht darin, daß, wenn wir Ahriman neben uns haben, wir fortwährend in der Gefahr sind, ihm zu verfallen, in seine Natur überzugehen, uns nicht mehr losreißen zu können von ihm. Und man möchte sagen: Der Sphinx gegenüber empfindet der Mensch etwas, was in ihn eindringt und ihn gleichsam auseinanderreißt; dem Mephistophelischen gegenüber empfindet der Mensch etwas wie: er muß untertauchen in dieses Mephistophelische, er muß sich ihm ver­schreiben, er muß ihm verfallen.",
      "Die Griechen hatten keine Theologie in unserem modernen Sinne, aber sie standen in bezug auf alles, was Weisheit ist, doch noch der Natur und ihren Erscheinungen näher als der moderne Mensch. Ohne Theologie näherten sie sich den Weistümern der Natur, und dadurch entstand in ihnen die Fragepein.",
      "Der Mensch ist näher der Natur in seinem Atmungsprozeß als in seinem Nervenprozesse. Daher empfand der Grieche besonders leben­dig dieses Entgegengehen der Weisheit in seinem Verhältnis zur Sphinx. Anders ist das beim Menschen in der modernen Zeit geworden. Die Theologie kommt herauf. Nicht in dem unmittelbaren Verkehr mit der Natur glaubt der Mensch der göttlichen Weltweisheit nahe zu sein, sondern er will sie studieren; er will sich ihr nähern nicht durch den Atmungs- und Blutprozeß, sondern durch den Nervenprozeß. Nervenprozeß wird das Suchen nach Weisheit, Theologie. Aber dadurch bannt der Mensch seine Weisheit in den Nervenprozeß hinein, nähert sich dem Mephistopheles. Und als der fünfte nachatlantische Zeitraum her­aufkam, entwickelte sich gerade aus diesem Bannen der Weisheits­wandelung in seinen Nervenprozeß die Ahnung, daß man den Mephisto an seine Fersen kettet, daß man ihn neben sich hinstellt.",
      "Wenn man die Faust-Sage von allem Rankenwerk befreit, das sich um sie herumschlingt, so haben wir doch immer die Tatsache, daß ein junger Theologe nach Weisheit strebt, von Zweifeln geplagt wird und sich deshalb dem Teufel, dem Mephisto verschreibt, und dadurch in seinen Wirkungskreis gezogen wird. So wie aber der Grieche mit der Sphinx fertig werden mußte dadurch, daß er die Ich-Natur des Men­schen völlig ausbildete, so wie man fertig werden mußte mit der Sphinx durch die Ausbildung der Ich-Natur, so muß man fertig werden in unserem Zeitraum mit Mephistopheles durch die Erweiterung und Er­füllung des Ich mit jener Weisheit, die allein von der Erforschung der geistigen Welt, durch die Erkenntnis der geistigen Welt, durch die Gei­steswissenschaft kommen kann.",
      "Ödipus sollte der Mächtigste dieser Sphinxbesieger sein. Jeder Grie­che, der sein Menschentum ernst nahm, war im Grunde genommen im kleinen mehr oder weniger ein Sphinxbesieger. Ödipus sollte nur das, was jeder Grieche erleben mußte, in besonders typischer Gestalt dar­stellen. Was geschieht also? Ödipus sollte dasjenige, was im Atmungs-und Blutprozesse lebt, besiegen. Dem Menschen, der in diesem lebt, soll er gegenüberstellen den gleichsam mit verarmten Ätherkräften leben­den Nervenmenschen. Wodurch kommt er dazu? Dadurch, daß er in seine eigene Natur die Kräfte, die mit dem Nervenprozeß verwandt sind, also die mephistophelischen Kräfte, aufnimmt, aber in gesunder Weise aufnimmt, so daß sie nicht nebenhergehen und ihm zum Begleiter werden, sondern daß sie in ihm sind und er durch diese Kräfte der Sphinxnatur gegenübertreten kann.",
      "Da sehen wir, wie im Grunde genommen Luzifer und Ahriman an ihrem richtigen Orte segensreich wirken, an dem Orte, wohin sie gleich­sam erst versetzt sind, und daß sie, wo sie nicht stehen sollen, nachteilig wirken. Für den Griechen war die Sphinxnatur etwas, womit er fertig werden sollte, was er aus sich heraussetzen sollte. Wenn er sie in den Abgrund stürzen, also den erweiterten Ätherleib in den physischen Leib hineinbringen konnte, dann hatte er die Sphinx überwunden. Der Abgrund ist nicht da draußen, der Abgrund ist der eigene physische Leib, in den in gesunder Weise die Sphinx untergetaucht werden muß. Aber da muß der andere Pol, der Nervenpol, der entgegengesetzte Prozeß,",
      "vom Ich ausgehend, stärker werden, nicht das, was draußen ist, sondern das, was drinnen sein muß. Das Ahrimanische wird im Men­schen aufgenommen und dadurch an den richtigen Ort gestellt.",
      "Ödipus ist der Sohn des Laios. Diesem war vorausgesagt worden, daß, wenn er ein Kind haben würde, dieses Unglück bringen würde für sein ganzes Geschlecht. Daher setzte er das Knäblein, das ihm geboren wurde, aus. Er durchstach ihm die Füße, und daher bekam es den Namen Ödipus, das heißt Klumpfuß. Da haben wir die mephistophe­lischen Kräfte in dem Ödipus-Drama.",
      "Ich habe gesagt, wenn durch diese Kräfte die Ätherkraft verarmt, können sich die Füße nicht mehr entwickeln, sie müssen verkümmern, verdorren. Bei Ödipus wurde das künstlich bewirkt. Er wurde be­kanntlich an einem Baum aufgehängt von dem Hirten gefunden, der ihn aufzieht, während er hätte zugrunde gehen sollen. Er trägt nun die Klumpfüße durch die Welt. Er ist gewissermaßen der ins Heilige über­setzte Mephistopheles. Da ist er an der richtigen Stelle, da kann er das Ich kräftig durchpulsen, wo es gilt, die Aufgabe des vierten nachatlan­tischen Zeitraumes zu lösen. Alles dasjenige, wodurch der Grieche groß geworden ist, wodurch er so recht zum Griechen geworden ist, der har­monische Einklang zwischen dem Ätherleibe und dem physischen Leibe, den wir noch so lebendig an den griechischen Gestalten in ihrer Wohl-ges talt bewundern, alles das geht dem Ödipus ab, damit er «Persönlich­keit» werden kann, damit er gerade der Repräsentant wird des Men­schen, in dem das Ich stark wird. Das zum Kopfe heraufwandernde Ich wird stark, indem die Füße verkümmern.",
      "Dem muß gegenüberstehen der Mensch der fünften nachatlantischen Kulturperiode. So wie der Ödipus, um der Sphinx gegenuberzustehen, um sie zu besiegen, den Ahriman aufnehmen mußte, so muß der Mensch der fünften nachatlantischen Kulturperiode, der dem Ahriman-Mephi­stopheles gegenübersteht, den Luzifer in sich aufnehmen, das heißt, er muß den umgekehrten Prozeß durchmachen wie Ödipus. Er mußte das, was vom Ich aufgehäuft war im Kopfe, hinunterdrängen von dem Kopfe in die andere Menschennatur. Da hat sich angehäuft in dem Ich, insofern dieses Ich im Nervenprozeß lebt, Philosophie, Juristerei, Me­dizin und leider auch Theologie - alles Nervenprozesse! Da entsteht",
      "der Drang, alles wegzukriegen aus dem Kopfe und durch die Sinnlich­keit zur ganzen Welt durchzudringen.",
      "Jetzt nehmen Sie den Faust, wie er dasteht, mit alledem, was das Ich sich errungen hat, und wie er das alles gleichsam aus dem Kopfe heraus­werfen will, das, was Goethe zusammenfaßt in die Worte: «Habe nun, ach! Philosophie, Juristerei und Medizin, und leider auch Theologie! durchaus studiert mit heißem Bemühn.» Das suchte er nun alles aus dem Kopfe wegzubekommen. Er tut es auch, indem er sich dem Leben ergibt, das nicht an den Kopf gebunden ist. Er ist der umgekehrte Ödi­pus, der die Luzifernatur in sich hereinbekommt.",
      "Und nun verfolgen Sie, was Faust alles macht, damit er den Luzifer in sich hereinbekommt, damit er den Ahriman, den Mephisto neben sich bekämpfen kann. Das alles zeigt uns, inwiefern wirklich dieser Faust der umgekehrte Ödipus ist. Während alles dasjenige, was durch die umgekehrte Ahrimannatur in Ödipus geschieht, in Zusammenhang steht mit Luzifer, steht alles dasjenige, was durch die umgekehrte Luzi­fernatur in Faust geschieht, in Zusammenhang mit Ahriman-Mephisto. Wie Ahriman-Mephisto mehr in der äußeren Welt lebt, so lebt Luzifer mehr in der inneren Welt. All das Unglück, das Ödipus dadurch trifft, daß er sich mit der Ahrimannatur durchdringen muß, besteht in äu­ßeren Dingen. Über das Geschlecht kommt Verhängnis, nicht bloß über ihn selber. Und auch das Verhängnis, das über ihn selber kommt, ist äußerlich angedeutet. Daß er sich die Augen durchsticht und sich blen­det, das sind auch äußere Dinge. Daß die Pest kommt über seine Vater-stadt, ist etwas Äußeres. Alles, was bei Faust auftritt, sind innere See­lenerlebnisse, ist ein Tragisches in des Menschen Inneren, so daß Faust sich auch hier als der umgekehrte Ödipus darstellt.",
      "Wenn wir diese zwei Gestalten oder vielmehr diese zwei Doppel-gestalten: Ödipus und Sphinx, Faust und Mephisto, vor unser Auge hinstellen, so haben wir in typischer Weise vor uns die Evolution des vierten und des fünften nachatlantischen Zeitraums. Wenn einmal die Zeit kommen wird, wo man weniger darstellen wird als Geschichte die äußere Phantasmagorie, dasjenige, was als Abdruck des Äußeren ge­schehen ist, sondern darstellen wird, was die Menschen erleben, dann wird man erst sehen, wie bedeutungsvoll und wichtig diese Grunderlebnisse",
      "des Menschen sind. Dann wird man erst bemerken, was im fortlaufenden Evolutionsprozeß wirklich lebt, wie übergeht die Ge­schichte, die äußere Phantasmagorie von derjenigen Darstellung, die gewöhnlich als Geschichte gegeben wird, in das, wovon die äußeren Ereignisse, wenn sie auch noch so bedeutungsvoll auftreten, im Grunde nur der äußere phantasmagorische Abdruck sind.",
      "Wie das Ich einerseits sich kräftigen mußte dadurch, daß Ahriman­Mephistopheles in den Ödipus, das heißt, in den Griechen einzog, so ist andererseits im modernen Menschen dieses Ich zu stark geworden. Und der moderne Mensch muß von diesem Ich wieder loskommen dadurch, daß er sich in die geistigen Geschehnisse vertieft, vertieft in dasjenige, was zusammenhängt mit der Welt, der das Ich angehört, wenn dieses Ich sich bewußt wird, daß es nicht nur im Menschenleibe lebt, sondern ein Bürger der spirituellen Welt ist. Und in diesem Zeitalter leben wir. Während im vierten nachatlantischen Zeitalter der Mensch streben mußte, mit aller Gewalt sich bewußt zu werden des Ich im physischen Leibe, so muß der Mensch unseres fünften nachatlantischen Zeitraumes darauf hinarbeiten, sich bewußt zu werden, daß das Ich der geistigen Welt angehört. Und die Erweiterung des Ich-Bewußtseins über die geistige Welt, das ist Geisteswissenschaft. Daher ist diese Geisteswissen­schaft auch im Tiefsten zusammenhängend mit den höchsten Forde­rungen der menschlichen Evolution in unserem fünften nachatlan­tischen Zeitraume."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Es ist uns durch unsere Betrachtungen schon geläufig geworden, daß wir unter oder hinter der physischen Welt, die vor uns liegt, den Beginn anderer Welten finden.",
        "Ich möchte heute als Einleitung von einigen Eigentümlichkeiten dieser geistigen Welten sprechen, von denen wir zum Teil schon wissen, die wir durch manches ergänzen wollen, um auch sonstiges noch vor die Seele zu rücken."
      ],
      [
        "Sie wissen, die nächste Welt, welche an die unsrige angrenzt, ist die sogenannte imaginative Welt.",
        "Diese Welt ist in sich viel beweglicher als unsere physische Welt.",
        "Unsere physische Welt stellt sich dar mit schar­fen Konturen, scharfen Grenzlinien, stellt eine Welt scharf umrissener Gegenstände dar."
      ],
      [
        "Eine gleichsam flüssige, flüchtige Welt ist diejenige, in die wir hineinkommen, wenn wir den Schleier zerreißen, den die physische Welt bildet.",
        "Auch wissen wir, daß gegenüber dieser ersten geistigen Welt das Gefühl, die Empfindung beginnt, daß wir außerhalb unseres physischen Leibes sind."
      ],
      [
        "Zu diesem unserem physischen Leib be­kommen wir in dem Augenblicke, wo wir in die geistige Welt hinauf­steigen, gewissermaßen ein neues Verhältnis, ein Verhältnis, wie wir es innerhalb des physischen Leibes etwa haben zu unseren Augen oder zu unseren Ohren.",
        "Der physische Leib wirkt mehr als ein Ganzes wie eine Art Wahrnehmungsorgan, aber wir merken sehr bald, es handelt sich eigentlich nicht richtig um den physischen Leib, wenn uns so dieser physische Leib als eine Art Wahrnehmungsorgan zum Gefühl kommt, sondern es handelt sich da um den ätherischen Leib."
      ],
      [
        "Der physische Leib gibt uns gleichsam nur ein Gerüst, das den ätherischen Leib hält.",
        "Wir blicken von außerhalb nach unserem ätherischen Leibe hin, verspüren ihn auch noch, verspüren ihn als das Sinnesorgan, das eine Welt wahr­nimmt webender, schwebender Bilder und Töne."
      ],
      [
        "Wie unser Verhältnis zum Ohr und Auge, so wird unser Verhältnis zu dem vom physischen Leibe gehaltenen Ätherleibe."
      ],
      [
        "Wenn wir uns nun so außerhalb unseres physischen Leibes fühlen, so ist dieses Erlebnis ähnlich dem Schlaferlebnis.",
        "Das Schlaferlebnis"
      ],
      [
        "besteht darin, daß wir mit unserer geistig-seelischen Menschlichkeit außerhalb unseres physischen und Ätherleibes sind, nur daß während des Schlaferlebnisses unser Bewußtsein herabgestimmt ist, und wir nichts wissen von dem, was eigentlich mit uns und um uns vorgeht.",
        "Man kann also sagen, daß es noch ein anderes Verhältnis des Menschen zu seinem physischen Leibe gibt als dasjenige, woran wir gewohnt sind.",
        "Auf das, worauf die Geisteswissenschaft so aufmerksam machen muß, wird die Menschheit durch ihre Evolution immer mehr und mehr hin­gelenkt werden, je weiter wir der Zukunft entgegengehen."
      ],
      [
        "Ich habe es aus vielen Zusammenhängen heraus betont, daß es nicht eine Willkür ist, daß wir heute Geisteswissenschaft treiben, sondern daß die Beschäftigung mit dieser Geisteswissenschaft von uns gefordert wird durch die Evolution der Menschheit, durch das, was im gegen­wärtigen Zeitpunkte in der Menschheitsevolution sich vorbereitet.",
        "Man kann nämlich dieses gleichsam Sich-Getrenntfühlen in seiner mensch­lichen Wesenheit von seinem physischen Leibe als etwas bezeichnen, was wie ein unverstandenes Erlebnis immer mehr und mehr über die Menschen wie von selbst kommen wird, je weiter wir als Menschheit der Zukunft entgegengehen."
      ],
      [
        "Es wird eine Zeit kommen, wo an viele, viele Menschen immer mehr die Empfindung herantreten wird: Ja, was ist denn das, ich fühle mich so, wie wenn ich mich gespalten hätte, wie wenn da noch ein Zweiter neben mir wäre. - Und diese Empfindung, dieses Gefühl, das als etwas Natürliches auftreten wird, geradeso wie Hunger oder Durst oder andere Erlebnisse, darf nicht unverstanden bleiben bei den Menschen der Gegenwart und Zukunft.",
        "Verständlich wird es sein, wenn die Menschen sich bequemen werden, durch die Geisteswissenschaft die eigentliche Bedeutung dieses Gespaltenseins zu verstehen."
      ],
      [
        "Insbesondere wird auch die Pädagogik, die Erziehung, je mehr wir diesen Dingen entgegengehen, darauf Rücksicht nehmen müs­sen.",
        "Man wird lernen müssen, auf gewisse Erlebnisse der Kinder sorg­fältiger zu achten, als man das bisher getan hat, wo diese Erlebnisse auch nicht in demselben Maße da waren."
      ],
      [
        "Gewiß, in dem späteren, robusteren Leben, unter dem Eindrucke der physischen Welt werden diese Gefühle und Empfindungen, die ich cha­rakterisiert habe, nicht so besonders stark sein in der allernächsten Zukunft,"
      ],
      [
        "aber in einer ferneren Zukunft werden sie immer stärker und stärker werden.",
        "Zunächst werden sie beim heranwachsenden Kinde auftreten, und die Erwachsenen werden von den Kindern gar mancher­lei hören, was sie werden verstehen müssen, mancherlei, über das man hinweggehen kann wie über ein Nichts, über das man aber nicht hinweggehen sollte, weil es mit den tiefsten Evolutionsgeheimnissen der Welt zusammenhängt."
      ],
      [
        "Kinder werden andeuten: Da oder dort habe ich ein Wesen gesehen, das hat zu mir dies oder jenes gesagt, was ich tun soll. - Der materia­listisch gesinnte Mensch wird sagen: Du bist ein dummer Bub oder ein dummes Mädchen, das gibt es ja gar nicht. - Wer aber Geisteswissen­schaft verstehen will, muß wissen lernen, daß es sich da um eine bedeut­same Erscheinung handelt.",
        "Wenn ein Kind sagt: Da habe ich jemanden gesehen, der ist wieder verschwunden, aber er kommt immer wieder und wieder; er sagt zu mir immer das und jenes, und ich kann nicht aufkommen gegen ihn -, so wird der, welcher die Geisteswissenschaft versteht, erkennen, daß sich da etwas in dem Kinde ankündigt, was immer deutlicher in der Menschheitsevolution hervortreten wird.",
        "Was ist denn das, was sich da ankündigt?"
      ],
      [
        "Wir werden es verstehen, wenn wir zwei Grunderlebnisse des Men­schen ins Auge fassen, von denen das erste ganz besonders wichtig war für den vierten nachatlantischen, den griechisch-lateinischen Zeitraum, und das andere wichtig ist für unseren Zeitraum, in dem es sich langsam erst vorbereitet.",
        "Während das erste Grunderlebnis in dem griechisch lateinischen Zeitraum seinen Abschluß gefunden hat, gehen wir dem zweiten langsam entgegen.",
        "In das menschliche Leben spielen immer Er­lebnisse herein, die von Luzifer und Ahriman stammen.",
        "In das Grund-erlebnis der vierten nachatlantischen Periode spielte insbesondere Luzi­fer herein; in unsere Periode spielt Ahriman herein und bedingt das Grunderlebnis.",
        "Nun hängt Luzifer mit alledem zusammen, was noch nicht bis zur Deutlichkeit der einzelnen Sinne sich ausgewachsen hat, was undeutlich an den Menschen, undifferenziert an ihn herankommt.",
        "Mit andern Worten, Luzifer hängt mit dem Atemerlebnis zusammen, mit dem Erlebnis des Ein- und Ausatmens.",
        "Das Atmen des Menschen ist etwas, was in einem ganz bestimmten geregelten Verhältnis stehen"
      ],
      [
        "muß zu seiner Gesamtorganisation.",
        "In dem Augenblick, wo der At­mungsprozeß in irgendeiner Weise gestört ist, verwandelt sich sogleich die Atmung aus dem, wie sie sonst auftritt, nämlich als unbewußter Vorgang, auf den wir nicht zu achten brauchen, in einen bewußten, in einen mehr oder weniger traumhaft bewußten Vorgang.",
        "Und wenn -wir können es ganz trivial ausdrücken - der Atmungsprozeß zu ener­gisch wird, wenn er größere Anforderungen an den Organismus stellt, als dieser Organismus leisten kann, dann hat Luzifer die Möglichkeit, mit dem Atmen einzudringen in den menschlichen Organismus.",
        "Er muß es ja nicht selbst sein, aber seine Scharen tun es, diejenigen, die zu ihm gehören."
      ],
      [
        "Ich weise damit auf eine Erscheinung hin, welche jeder kennt als Traumerlebnis.",
        "Dieses Traumerlebnis kann sich in beliebiger Weise steigern.",
        "Der Alptraum, wo also der Mensch durch das gestörte Atmen zum Traumbewußtsein kommt, so daß sich Erlebnisse der geistigen Welt hineinmischen können, und auch alle Angst- und Furchterlebnisse, die mit Alpträumen verbunden sind, haben in dem luziferischen Element der Welt ihren Ursprung.",
        "Alles, was vom gewöhnlichen Atmungs­prozeß übergeht zum Würgen, zu dem Gefühl des Gewürgtwerdens, das hängt zusammen mit dieser Möglichkeit, daß Luzifer sich einmischt in den Atmungsprozeß.",
        "Das ist der grobe Prozeß, wo durch eine Herabminderung des Bewußtseins Luzifer sich in das Atemerlebnis hineinmischt, gestaltenhaft in das Traumbewußtsein tritt und da zum Würger wird.",
        "Das ist das grobe Erlebnis."
      ],
      [
        "Es gibt aber auch ein feineres Erlebnis, das uns dieses Würgeerlebnis gleichsam verfeinert, nicht so grob wie ein physisches Würgen darstellt.",
        "Man achtet gewöhnlich nicht darauf, daß eine solche Verfeinerung des Würgens zu den menschlichen Erlebnissen gehört.",
        "Aber jedesmal, wenn an die menschliche Seele dasjenige herantritt, was zu einer Frage wird oder zu einem Zweifel an diesem oder jenem in der Welt, dann ist in verfeinerter Weise ein Würgeerlebnis da.",
        "Man kann schon sagen: Wenn wir eine Frage aufstellen müssen, wenn ein kleines oder ein großes Wel­tenrätsel sich uns aufdrängt, dann werden wir gewürgt, aber so, daß wir es nicht merken. - Jeder Zweifel, jede Frage ist ein verfeinertes Alpdrücken oder ein verfeinerter Alptraum."
      ],
      [
        "So verwandeln sich die Erlebnisse, die uns sonst grob entgegentreten, in feinere Erlebnisse, wenn sie mehr seelisch auftreten.",
        "Man kann sich schon denken, daß die Wissenschaft einmal dazu kommen wird, den Zusammenhang des Atmungsprozesses mit der Fragestellung oder der Empfindung eines Zweifels in der Menschenseele zu studieren.",
        "Aber auch alles das, was mit Fragen und Zweifeln zusammenhängt, alles das, was damit zusammenhängt, daß wir unbefriedigt sind, weil die Welt an uns herantritt und eine Antwort verlangt, oder weil wir gezwungen sind, eine Antwort zu geben durch das, was wir sind, hängt mit dem Luziferischen zusammen."
      ],
      [
        "Wenn wir nun die Sache geisteswissenschaftlich betrachten, so kön­nen wir sagen: Bei allem, wo der Würgeengel im Alptraum uns be­drückt, oder wo wir durch die Fragestellung eine innere Bedrückung, einen Anflug von Beängstigung erfahren, haben wir es mit einem gleich­sam stärkeren, energischeren Atmungsprozeß zu tun, mit etwas, was im Atem lebt, was aber, damit die menschliche Natur in der richtigen Weise funktioniert, harmonisiert, abgeschwächt werden muß, damit das Leben richtig verläuft.",
        "Was findet nun statt, wenn ein energischerer Atmungsprozeß eintritt?",
        "Da ist gleichsam der Ätherleib und alles, was mit der ätherischen Natur des Menschen zusammenhängt, zu weit aus­gedehnt, zu sehr auseinandergedrängt, und da sich das dann auslebt im physischen Leibe, so kann es sich nicht auf den physischen Leib beschränken, es will ihn gewissermaßen auseinanderzerren.",
        "Ein zu üppiger, ein zu weit ausgedehnter Ätherleib liegt einem verstärkten Atmungsprozeß zugrunde, und dann besteht die Möglichkeit für das luziferische Element, sich besonders geltend zu machen."
      ],
      [
        "Man kann also sagen: Das Luziferische kann sich in die menschliche Natur hineinschleichen, wenn der Ätherleib geweitet ist. - Man kann auch sagen: Das Luziferische hat die Tendenz, in einem der mensch­lichen Form gegenüber geweiteten Ätherleibe sich auszudrücken, also in einem Ätherleibe, der mehr Raum braucht, als in der menschlichen Haut eingeschlossen ist, der die Form üppiger gibt. - Man kann sich nun denken, daß man künstlerisch diese Frage beantworten will, und da kann man sagen: So wie der menschliche Ätherleib normal ist, ist er der Bildner der menschlichen Gestalt, die physisch vor uns steht.",
        "Aber"
      ],
      [
        "sobald er sich weitet, sobald er sich einen größeren Raum, weitere Gren­zen verschaffen will, als in der menschlichen Haut darinnen sind, will er auch andere Formen geben.",
        "Es kann da nicht die menschliche Form bleiben.",
        "Er will überall über die menschliche Form hinaus. - Dieses Problem hat man in alter Zeit schon gelöst.",
        "Was für eine Form kommt da heraus, wenn der geweitete Ätherleib, der nicht für das menschliche Wesen, sondern für das luziferische Wesen paßt, sich Geltung ver­schafft und formhaft vor die menschliche Seele tritt?",
        "Was kommt da heraus?",
        "Die Sphinx!"
      ],
      [
        "Hier haben wir eine besondere Art, uns in die Sphinx hinein zu ver­tiefen.",
        "Die Sphinx ist es, was eigentlich an einem würgt.",
        "Wenn der Ätherleib des Menschen durch die Energie des Atmens sich ausweitet, taucht ein luziferisches Wesen in der Seele auf.",
        "Es lebt in diesem Äther-leibe nicht die menschliche Gestalt, sondern die luziferische Gestalt, die Sphinxgestalt.",
        "Die Sphinx taucht auf als die Zweifelaufwerferin, als die Fragepeinigerin.",
        "Diese Sphinx hat also eine besondere Beziehung zum Atmungsprozeß.",
        "Wiederum wissen wir aber, daß der Atmungs-prozeß eine besondere Beziehung zur Blutbildung hat.",
        "Daher lebt das Luziferische auch im Blute, durchwogt und durchwallt das Blut.",
        "Überall kann auf dem Umwege durch die Atmung das Luziferische in das Blut des Menschen hinein, und wenn zuviel Energie in das Blut hineinkommt, dann ist das Luziferische, die Sphinx, besonders stark."
      ],
      [
        "So steht der Mensch dadurch, daß er in seinem Atmungsprozeß dem Kosmos geöffnet ist, der Sphinxnatur gegenüber.",
        "Dieses Erlebnis, in seinem Atmen der Sphinxnatur des Kosmos gegenüberzustehen, dieses Grunderlebnis ging besonders in der vierten nachatlantischen, der grie­chisch-lateinischen Kulturperiode auf.",
        "Und in der Ödipus-Sage sehen wir, wie der Mensch der Sphinx gegenübersteht, wie die Sphinx sich an ihn kettet, zur Fragepeinigerin wird.",
        "Der Mensch und die Sphinx, oder wir können auch sagen, der Mensch und das Luziferische im Weltall soJlten gleichsam als ein Grunderlebnis der vierten nachatlantischen Kulturperiode so hingestellt werden, daß,wenn der Mensch sein äußeres normales Leben auf dem physischen Plan nur ein wenig durchbricht, er mit der Sphinxnatur in Berührung kommt.",
        "Da tritt Luzifer in seinem"
      ],
      [
        "Leben an ihn heran, und er muß mit Luzifer, mit der Sphinx fertig werden."
      ],
      [
        "Anders ist das Grunderlebnis des fünften nachatlantischen Kultur­zeitraumes, unseres Zeitraumes.",
        "Für unseren Zeitraum ist das besonders vorbereitet, daß der Ätherleib nicht aufgeplustert, nicht ausgedehnt, sondern zusammengezogen ist, daß er nicht zu groß, sondern eher zu klein ist, und das wird immer stärker und stärker werden, je weiter die Evolution fortgeht.",
        "Wenn wir sagen können: Die normale Gestalt des"
      ],
      [
        "# Bild s. 103"
      ],
      [
        "Menschen beim Griechen ist so, daß der Ätherleib zu groß ist -, so können wir sagen: Beim modernen Menschen ist es so, daß der Äther-leib sich zusammenschnürt, sich zusammenzieht, zu klein wird. - Je weiter der Mensch kommen wird in der materialistischen Verachtung des Spirituellen, desto mehr wird sich dieser Ätherleib zusammen­ziehen und austrocknen.",
        "Da aber die Durchorganisierung des physi­schen Leibes davon abhängt, daß der Ätherleib ihn ganz richtig durch­dringt, so wird für den physischen Leib immer eine Tendenz auftreten, wenn der Ätherleib zu sehr zusammengedrängt ist, daß der physische Leib auch auszutrocknen beginnt.",
        "Und wenn er ganz besonders stark austrocknen würde, so würde er statt der natürlichen Menschenfüße hornartige Füße bekommen.",
        "Der Mensch wird sie ja nicht bekommen,"
      ],
      [
        "aber die Tendenz dazu liegt in ihm, und sie ist begründet in dieser Ten­denz des Ätherleibes, auszutrocknen, zu wenig Ätherkraft zu ent­wickeln.",
        "In diesen vertrockneten Ätherleib kann sich nun besonders Ahriman hineinleben, wie Luzifer in den erweiterten Ätherleib.",
        "Ahri­man wird die Gestalt annehmen, die auf eine Ärmlichkeit des Ätherleibes hinweist.",
        "Er wird zu wenig Ätherkraft entwickeln, um richtig organisierte Füße zu haben, und die erwähnten hornartigen Füße -Bocksfüße - ausbilden."
      ],
      [
        "Mephistopheles ist ja Ahriman; er hat die Bocksfüße nicht umsonst, er hat die Bocksfüße aus diesem Grunde, den ich angedeutet habe.",
        "Die Mythen und Sagen sind eben sehr bedeutungsvoll; deshalb erscheint Mephistopheles sehr oft mit Pferdefüßen, wo also die Füße zu Hufen vertrocknet sind.",
        "Wenn Goethe das Problem des Mephisto schon voll­ständig durchdrungen hätte, so hätte er nicht seinen Mephisto wie einen modernen Kavalier auftreten lassen, denn es gehört schon einmal zum Wesen des Ahriman-Mephisto, nicht so viel Ätherkraft zu haben, daß er die menschliche physische Gestalt vollständig durchorganisieren kann."
      ],
      [
        "Aber noch eine Eigentümlichkeit ist dadurch hervorgerufen, daß der Ätherleib gleichsam zusammengezogen ist, ärmer ist an Ätherkräften, als es im Normalen der Fall ist.",
        "Diese Eigentümlichkeit wird uns am klarsten, wenn wir einen Blick auf die gesamte menschliche Natur wer­fen.",
        "Wir sind in gewisser Beziehung schon physisch eine Zweiheit.",
        "Denken Sie doch, wenn Sie so dastehen, sind Sie eben der physische Mensch.",
        "Aber zu dem physischen Menschen gehört es, daß die Atemluft immerfort in ihm darinnen ist.",
        "Diese Atemluft jedoch ist bei dem näch­sten Ausatmen schon wieder nach außen befördert, so daß der Atem­luftmensch, der Sie durchdringt, fortwährend wechselt.",
        "Sie sind nicht bloß das, was aus Muskeln und Knochen besteht, der Fleisch- und Knochenmensch, sondern Sie sind auch der Atemmensch.",
        "Der aber wechselt fortwährend, geht hin und her, aus und ein.",
        "Und der Atem-mensch ist es, der wieder im Zusammenhang steht mit dem immerfort zirkulierenden Blute."
      ],
      [
        "Wie getrennt von diesem ganzen Atmungsmenschen liegt in Ihnen der Nervenmensch, der andere Pol, in dem das Nervenfluidum zirkuliert,"
      ],
      [
        "und es ist nur eine Art äußere Berührung, ein äußeres Zusammen­kommen zwischen dem Nervenmenschen und dem Blutmenschen.",
        "So wie nur diejenigen Ätherkräfte, die nach dem Luziferischen hin ten­dieren, durch das Atmen leicht an das Blutsystem herankommen kön­nen, so können die Ätherkräfte, welche nach dem Mephistophelischen oder Ahrimanischen hin tendieren, nur an das Nervensystem heran­kommen, aber nicht an das Blutsystem.",
        "Ahriman ist es versagt, in das Blut unterzutauchen; er kann fortwährend in den Nerven leben, bis zum Vertrocknen, zur Nüchternheit leben, weil er nicht an die Wärme des Blutes heran kann.",
        "Will er aber eine Beziehung zur Menschennatur hin entwickeln, dann wird er lechzen müssen nach einem Tröpfchen Blut, weil er so schwer herankommen kann an das Blut.",
        "Ein Abgrund liegt zwischen Mephistopheles und dem Blute.",
        "Will er an den Menschen herankommen, an das, was im Menschen lebt, will er mit dem Menschen in Verbindung treten, dann wird er gewahr, daß das Menschliche in dem Blute lebt.",
        "Er muß nach dem Blute trachten."
      ],
      [
        "Sehen Sie, damit hängt zusammen die Weisheit der Mephistopheles-Sage, daß die Verschreibung mit Blut geschieht.",
        "Faust muß sich dem Mephisto durch das Blut verschreiben, weil dieser nach dem Blute lech­zen muß, weil er abgetrennt ist vom Blute.",
        "Geradeso wie der griechische Mensch der Sphinx gegenüberstand, die im Atmungssystem lebt, so steht der Mensch des fünften nachatlantischen Kulturzeitraumes dem Mephistopheles gegenüber, der im Nervenprozesse lebt, der kalt und nüchtern ist, weil er an Blutleere leidet, weil die Wärme des Blutes ihm fehlt.",
        "Und dadurch wird er zum Spötter, zum nüchternen Begleiter des Menschen."
      ],
      [
        "Wie Ödipus mit der Sphinx, so hat der Mensch der fünften nach-atlantischen Kulturepoche mit Mephistopheles fertigzuwerden.",
        "Er steht diesem Mephistopheles wie einem zweiten Wesen gegenüber.",
        "Der Grie­che stand der Sphinx durch den energisch gewordenen Blut- und At­mungsprozeß gegenüber; ihm stand gegenüber, was mit der energische-ren Atmung in seine Natur hineinkam.",
        "Der moderne Mensch steht mit allem, was aus seinem Verstande, seiner Nüchternheit drängt, dem gegenüber, was an den Nervenprozeß gebannt ist.",
        "Prophetisch konnte dieses Gegenüberstehen des Menschen dem Mephistophelischen, ich"
      ],
      [
        "möchte sagen, dichterisch vorausgeahnt werden.",
        "Aber es wird immer mehr und mehr heraufziehen als ein Grunderlebnis, je weiter wir in der Evolution des fünften nachatlantischen Zeitraumes kommen.",
        "Und das, wovon ich erzählt habe, daß es im kindlichen Erlebnisse auftreten wird, wird dieses mephistophelische Erlebnis sein."
      ],
      [
        "Während der griechische Mensch unter der Pein einer Überfülle von Fragen gestanden hat, wird der moderne Mensch nicht so sehr einer Fragepein entgegengehen als vielmehr der Pein, in seine Vorurteile hin­ein verzaubert zu sein, einen zweiten Leib neben sich zu haben, der seine Vorurteile enthält.",
        "Und wie bereitet sich das vor?"
      ],
      [
        "Betrachten Sie einmal ganz unbefangen die Evolution.",
        "Wieviel hat im Verlaufe des fünften nachatlantischen Kulturzeitalters aufgehört, in warmer unmittelbarer Weise an den Menschen heranzutreten.",
        "Nehmen Sie die unzähligen Fragen, die wirklich an uns herantreten, wenn wir uns in die Geisteswissenschaft vertiefen."
      ],
      [
        "Sie sind alle für den modernen materialistisch gesinnten Menschen nicht da.",
        "Das Rätsel der Sphinx empfindet er nicht; das hat der Grieche noch in lebendiger Weise emp­funden.",
        "Der moderne Mensch wird aber ein anderes empfinden müssen."
      ],
      [
        "Er weiß eigentlich alles so gut nach seiner Meinung, beobachtet die Sinneswelt, kombiniert sie mit seinem Verstande, und dann lösen sich ihm alle Rätsel.",
        "Er ahnt nicht, wie sehr er in der äußeren Phantasma­gorie herumtappt."
      ],
      [
        "Das aber verdichtet immer mehr seinen Ätherleib, trocknet immer mehr seinen Ätherleib aus und führt endlich dazu, daß das mephistophelische Element wie eine zweite Natur sich heften wird an das Wesen des Menschen der Gegenwart in die Zukunft hinein.",
        "Alles das, was an materialistischen Vorurteilen, an materialistischer Beschränktheit sich entwickelt, wird die mephistophelische Natur ver­stärken, und wir können jetzt schon sagen: Wir sehen in eine Zukunft hinein, wo jeder geboren wird mit einem zweiten Menschen, welcher sagen wird, die da von der geistigen Welt reden, sind Narren."
      ],
      [
        "Ich weiß alles, ich verlasse mich auf meine Sinne. - Gewiß, der Mensch wird ab­weisen, so wie das Sphinxrätsel, auch das Mephistopheles-Rätsel, aber er wird heften an seine Fersen ein zweites Wesen.",
        "Das wird ihn so be­gleiten, daß er den Zwang empfinden wird, materialistisch zu denken nicht durch sich, sondern durch ein zweites Wesen, das sein Begleiter ist."
      ],
      [
        "Die materialistische Gesinnung wird den Ätherleib vertrocknen, und in dem vertrockneten Ätherleib wird Mephistopheles leben.",
        "Das wer­den wir verstehen müssen, und die Menschheit wird dem Kinde in zu­künftigen Zeiten so viel an Bildung mitgeben müssen - sei es durch Eurythmie, sei es durch geisteswissenschaftliche Gesinnung -, durch welche der Ätherleib belebt werden muß, daß der Mensch seine richtige Stellung wird einnehmen können, daß er erkennen wird, was sein Be­gleiter bedeutet.",
        "Sonst wird er diesen Begleiter nicht verstehen, sonst wird er sich ihm gegenüber fühlen, wie wenn er verzaubert, gebannt wäre.",
        "Wie der Grieche mit der Sphinx hat fertig werden müssen, so wird der moderne Mensch mit Mephistopheles fertig werden müssen, mit der satyrhaften, faunhaften Gestalt, die Bocks- oder Pferdefüße hat."
      ],
      [
        "Man kann schon sagen: Ein jedes Zeitalter weiß dasjenige, was sein Charakteristisches ist, in eine Grund- oder Ursage zu fassen. - Solche Grund- oder Ursagen sind die Ödipus-Sage in Griechenland und die Mephistopheles-Sage in der neueren Zeit.",
        "Aber diese Dinge müssen möglichst aus den Fundamenten heraus wirklich verstanden werden.",
        "Sie sehen, was sonst nur als Dichtung auftritt - die Auseinander­setzungen von Faust und Mephisto -, das wird, man möchte sagen, zum Fundament für die Zukunftspädagogik.",
        "Das Vorspiel davon besteht darin, daß das Volk oder der Dichter den Begleiter geahnt haben.",
        "Aber das Nachspiel wird darin bestehen, daß ein jeder Mensch diesen Be­gleiter haben wird, der ihm nicht unverständlich bleiben darf, und daß dieser Begleiter am lebendigsten, am mächtigsten in der Kindheit des Menschen auftreten wird.",
        "Und wenn die erwachsenen Erzieher nicht die richtige Stellung einnehmen werden gegenüber dem, was das Kind äußert, dann wird durch das unverstandene Gegenüberstehen den Ver­zauberungen des Mephistopheles die menschliche Natur verdorben werden."
      ],
      [
        "Es ist sehr merkwürdig, daß man in der Sagen- und Märchenlitera­tur, wenn man sie verfolgt, überall diese Züge finden kann.",
        "Sagen und Märchen, die so unverständig von den Gelehrten unserer Gegenwart betrachtet werden, weisen ihrer Struktur nach entweder nach dem Mephistophelischen, dem Ahrimanischen hin, oder nach dem Sphinx-artigen, dem Luziferischen.",
        "Alle Sagen und Märchen rühren davon her,"
      ],
      [
        "daß ihr Inhalt ursprünglich entweder durch das Verhältnis, das der Mensch zur Sphinx hat, erlebt worden ist oder durch das Verhältnis, das der Mensch zu Mephisto hat.",
        "In den Sagen und Märchen finden wir mehr oder weniger verborgen auttreten entweder das Fragemotiv: das ist das Sphinxmotiv, das Motiv, daß irgend etwas gelöst werden muß, daß eine Frage beantwortet werden muß, oder das Motiv der Verzau­berung, des Gebanntseins an irgend etwas: das ist das mephistophe­lische, das ahrimanische Motiv.",
        "Denn worin besteht das ahrimanische Motiv im genaueren?",
        "Es besteht darin, daß, wenn wir Ahriman neben uns haben, wir fortwährend in der Gefahr sind, ihm zu verfallen, in seine Natur überzugehen, uns nicht mehr losreißen zu können von ihm.",
        "Und man möchte sagen: Der Sphinx gegenüber empfindet der Mensch etwas, was in ihn eindringt und ihn gleichsam auseinanderreißt; dem Mephistophelischen gegenüber empfindet der Mensch etwas wie: er muß untertauchen in dieses Mephistophelische, er muß sich ihm ver­schreiben, er muß ihm verfallen."
      ],
      [
        "Die Griechen hatten keine Theologie in unserem modernen Sinne, aber sie standen in bezug auf alles, was Weisheit ist, doch noch der Natur und ihren Erscheinungen näher als der moderne Mensch.",
        "Ohne Theologie näherten sie sich den Weistümern der Natur, und dadurch entstand in ihnen die Fragepein."
      ],
      [
        "Der Mensch ist näher der Natur in seinem Atmungsprozeß als in seinem Nervenprozesse.",
        "Daher empfand der Grieche besonders leben­dig dieses Entgegengehen der Weisheit in seinem Verhältnis zur Sphinx.",
        "Anders ist das beim Menschen in der modernen Zeit geworden.",
        "Die Theologie kommt herauf.",
        "Nicht in dem unmittelbaren Verkehr mit der Natur glaubt der Mensch der göttlichen Weltweisheit nahe zu sein, sondern er will sie studieren; er will sich ihr nähern nicht durch den Atmungs- und Blutprozeß, sondern durch den Nervenprozeß.",
        "Nervenprozeß wird das Suchen nach Weisheit, Theologie.",
        "Aber dadurch bannt der Mensch seine Weisheit in den Nervenprozeß hinein, nähert sich dem Mephistopheles.",
        "Und als der fünfte nachatlantische Zeitraum her­aufkam, entwickelte sich gerade aus diesem Bannen der Weisheits­wandelung in seinen Nervenprozeß die Ahnung, daß man den Mephisto an seine Fersen kettet, daß man ihn neben sich hinstellt."
      ],
      [
        "Wenn man die Faust-Sage von allem Rankenwerk befreit, das sich um sie herumschlingt, so haben wir doch immer die Tatsache, daß ein junger Theologe nach Weisheit strebt, von Zweifeln geplagt wird und sich deshalb dem Teufel, dem Mephisto verschreibt, und dadurch in seinen Wirkungskreis gezogen wird.",
        "So wie aber der Grieche mit der Sphinx fertig werden mußte dadurch, daß er die Ich-Natur des Men­schen völlig ausbildete, so wie man fertig werden mußte mit der Sphinx durch die Ausbildung der Ich-Natur, so muß man fertig werden in unserem Zeitraum mit Mephistopheles durch die Erweiterung und Er­füllung des Ich mit jener Weisheit, die allein von der Erforschung der geistigen Welt, durch die Erkenntnis der geistigen Welt, durch die Gei­steswissenschaft kommen kann."
      ],
      [
        "Ödipus sollte der Mächtigste dieser Sphinxbesieger sein.",
        "Jeder Grie­che, der sein Menschentum ernst nahm, war im Grunde genommen im kleinen mehr oder weniger ein Sphinxbesieger.",
        "Ödipus sollte nur das, was jeder Grieche erleben mußte, in besonders typischer Gestalt dar­stellen.",
        "Was geschieht also?",
        "Ödipus sollte dasjenige, was im Atmungs-und Blutprozesse lebt, besiegen.",
        "Dem Menschen, der in diesem lebt, soll er gegenüberstellen den gleichsam mit verarmten Ätherkräften leben­den Nervenmenschen.",
        "Wodurch kommt er dazu?",
        "Dadurch, daß er in seine eigene Natur die Kräfte, die mit dem Nervenprozeß verwandt sind, also die mephistophelischen Kräfte, aufnimmt, aber in gesunder Weise aufnimmt, so daß sie nicht nebenhergehen und ihm zum Begleiter werden, sondern daß sie in ihm sind und er durch diese Kräfte der Sphinxnatur gegenübertreten kann."
      ],
      [
        "Da sehen wir, wie im Grunde genommen Luzifer und Ahriman an ihrem richtigen Orte segensreich wirken, an dem Orte, wohin sie gleich­sam erst versetzt sind, und daß sie, wo sie nicht stehen sollen, nachteilig wirken.",
        "Für den Griechen war die Sphinxnatur etwas, womit er fertig werden sollte, was er aus sich heraussetzen sollte.",
        "Wenn er sie in den Abgrund stürzen, also den erweiterten Ätherleib in den physischen Leib hineinbringen konnte, dann hatte er die Sphinx überwunden.",
        "Der Abgrund ist nicht da draußen, der Abgrund ist der eigene physische Leib, in den in gesunder Weise die Sphinx untergetaucht werden muß.",
        "Aber da muß der andere Pol, der Nervenpol, der entgegengesetzte Prozeß,"
      ],
      [
        "vom Ich ausgehend, stärker werden, nicht das, was draußen ist, sondern das, was drinnen sein muß.",
        "Das Ahrimanische wird im Men­schen aufgenommen und dadurch an den richtigen Ort gestellt."
      ],
      [
        "Ödipus ist der Sohn des Laios.",
        "Diesem war vorausgesagt worden, daß, wenn er ein Kind haben würde, dieses Unglück bringen würde für sein ganzes Geschlecht.",
        "Daher setzte er das Knäblein, das ihm geboren wurde, aus.",
        "Er durchstach ihm die Füße, und daher bekam es den Namen Ödipus, das heißt Klumpfuß.",
        "Da haben wir die mephistophe­lischen Kräfte in dem Ödipus-Drama."
      ],
      [
        "Ich habe gesagt, wenn durch diese Kräfte die Ätherkraft verarmt, können sich die Füße nicht mehr entwickeln, sie müssen verkümmern, verdorren.",
        "Bei Ödipus wurde das künstlich bewirkt.",
        "Er wurde be­kanntlich an einem Baum aufgehängt von dem Hirten gefunden, der ihn aufzieht, während er hätte zugrunde gehen sollen.",
        "Er trägt nun die Klumpfüße durch die Welt.",
        "Er ist gewissermaßen der ins Heilige über­setzte Mephistopheles.",
        "Da ist er an der richtigen Stelle, da kann er das Ich kräftig durchpulsen, wo es gilt, die Aufgabe des vierten nachatlan­tischen Zeitraumes zu lösen.",
        "Alles dasjenige, wodurch der Grieche groß geworden ist, wodurch er so recht zum Griechen geworden ist, der har­monische Einklang zwischen dem Ätherleibe und dem physischen Leibe, den wir noch so lebendig an den griechischen Gestalten in ihrer Wohl-ges talt bewundern, alles das geht dem Ödipus ab, damit er «Persönlich­keit» werden kann, damit er gerade der Repräsentant wird des Men­schen, in dem das Ich stark wird.",
        "Das zum Kopfe heraufwandernde Ich wird stark, indem die Füße verkümmern."
      ],
      [
        "Dem muß gegenüberstehen der Mensch der fünften nachatlantischen Kulturperiode.",
        "So wie der Ödipus, um der Sphinx gegenuberzustehen, um sie zu besiegen, den Ahriman aufnehmen mußte, so muß der Mensch der fünften nachatlantischen Kulturperiode, der dem Ahriman-Mephi­stopheles gegenübersteht, den Luzifer in sich aufnehmen, das heißt, er muß den umgekehrten Prozeß durchmachen wie Ödipus.",
        "Er mußte das, was vom Ich aufgehäuft war im Kopfe, hinunterdrängen von dem Kopfe in die andere Menschennatur.",
        "Da hat sich angehäuft in dem Ich, insofern dieses Ich im Nervenprozeß lebt, Philosophie, Juristerei, Me­dizin und leider auch Theologie - alles Nervenprozesse!",
        "Da entsteht"
      ],
      [
        "der Drang, alles wegzukriegen aus dem Kopfe und durch die Sinnlich­keit zur ganzen Welt durchzudringen."
      ],
      [
        "Jetzt nehmen Sie den Faust, wie er dasteht, mit alledem, was das Ich sich errungen hat, und wie er das alles gleichsam aus dem Kopfe heraus­werfen will, das, was Goethe zusammenfaßt in die Worte: «Habe nun, ach!",
        "Philosophie, Juristerei und Medizin, und leider auch Theologie! durchaus studiert mit heißem Bemühn.» Das suchte er nun alles aus dem Kopfe wegzubekommen.",
        "Er tut es auch, indem er sich dem Leben ergibt, das nicht an den Kopf gebunden ist.",
        "Er ist der umgekehrte Ödi­pus, der die Luzifernatur in sich hereinbekommt."
      ],
      [
        "Und nun verfolgen Sie, was Faust alles macht, damit er den Luzifer in sich hereinbekommt, damit er den Ahriman, den Mephisto neben sich bekämpfen kann.",
        "Das alles zeigt uns, inwiefern wirklich dieser Faust der umgekehrte Ödipus ist.",
        "Während alles dasjenige, was durch die umgekehrte Ahrimannatur in Ödipus geschieht, in Zusammenhang steht mit Luzifer, steht alles dasjenige, was durch die umgekehrte Luzi­fernatur in Faust geschieht, in Zusammenhang mit Ahriman-Mephisto.",
        "Wie Ahriman-Mephisto mehr in der äußeren Welt lebt, so lebt Luzifer mehr in der inneren Welt.",
        "All das Unglück, das Ödipus dadurch trifft, daß er sich mit der Ahrimannatur durchdringen muß, besteht in äu­ßeren Dingen.",
        "Über das Geschlecht kommt Verhängnis, nicht bloß über ihn selber.",
        "Und auch das Verhängnis, das über ihn selber kommt, ist äußerlich angedeutet.",
        "Daß er sich die Augen durchsticht und sich blen­det, das sind auch äußere Dinge.",
        "Daß die Pest kommt über seine Vater-stadt, ist etwas Äußeres.",
        "Alles, was bei Faust auftritt, sind innere See­lenerlebnisse, ist ein Tragisches in des Menschen Inneren, so daß Faust sich auch hier als der umgekehrte Ödipus darstellt."
      ],
      [
        "Wenn wir diese zwei Gestalten oder vielmehr diese zwei Doppel-gestalten: Ödipus und Sphinx, Faust und Mephisto, vor unser Auge hinstellen, so haben wir in typischer Weise vor uns die Evolution des vierten und des fünften nachatlantischen Zeitraums.",
        "Wenn einmal die Zeit kommen wird, wo man weniger darstellen wird als Geschichte die äußere Phantasmagorie, dasjenige, was als Abdruck des Äußeren ge­schehen ist, sondern darstellen wird, was die Menschen erleben, dann wird man erst sehen, wie bedeutungsvoll und wichtig diese Grunderlebnisse"
      ],
      [
        "des Menschen sind.",
        "Dann wird man erst bemerken, was im fortlaufenden Evolutionsprozeß wirklich lebt, wie übergeht die Ge­schichte, die äußere Phantasmagorie von derjenigen Darstellung, die gewöhnlich als Geschichte gegeben wird, in das, wovon die äußeren Ereignisse, wenn sie auch noch so bedeutungsvoll auftreten, im Grunde nur der äußere phantasmagorische Abdruck sind."
      ],
      [
        "Wie das Ich einerseits sich kräftigen mußte dadurch, daß Ahriman­Mephistopheles in den Ödipus, das heißt, in den Griechen einzog, so ist andererseits im modernen Menschen dieses Ich zu stark geworden.",
        "Und der moderne Mensch muß von diesem Ich wieder loskommen dadurch, daß er sich in die geistigen Geschehnisse vertieft, vertieft in dasjenige, was zusammenhängt mit der Welt, der das Ich angehört, wenn dieses Ich sich bewußt wird, daß es nicht nur im Menschenleibe lebt, sondern ein Bürger der spirituellen Welt ist.",
        "Und in diesem Zeitalter leben wir.",
        "Während im vierten nachatlantischen Zeitalter der Mensch streben mußte, mit aller Gewalt sich bewußt zu werden des Ich im physischen Leibe, so muß der Mensch unseres fünften nachatlantischen Zeitraumes darauf hinarbeiten, sich bewußt zu werden, daß das Ich der geistigen Welt angehört.",
        "Und die Erweiterung des Ich-Bewußtseins über die geistige Welt, das ist Geisteswissenschaft.",
        "Daher ist diese Geisteswissen­schaft auch im Tiefsten zusammenhängend mit den höchsten Forde­rungen der menschlichen Evolution in unserem fünften nachatlan­tischen Zeitraume."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "FÜNFTER VORTRAG Dornach, 21. November 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Es wird Ihnen in dem einen Vortrag, den ich im Anschlusse an Kalewala gehalten habe, etwas aufgefallen sein. Als Sie diesen Vortrag durchdacht haben, werden Sie sich gesagt haben, denn das ist naheliegend, da wurde ausgeführt, daß gewissermaßen ein Wesen herüberragt vom Westen nach dem Osten und drei Ausläufer wie drei Gliedmaßen vorstreckt, die von dem alten finnischen Volk empfunden wurden als Wäinämöinen, Ilmarinen und Lemminkäinen, und die man heute in der materialisti­schen Sprache den Rigaischen, den Finnischen, den Bottnischen  Meerbusen nennt. Nur werden Sie sich gefragt haben: Ja, aber wie kann er sagen, daß das etwas zu tun hat mit einer Wesenheit, denn das ist doch nur eine Fläche, die Oberfläche des Meeres mit ihren Grenzen, die da so sich vorgestreckt hat. Es hat nichts Körperhaftes, und doch redet er uns von einer Wesenheit! - So werden Sie sich gesagt haben.",
      "Dieses, was da in Ihrer Seele vorgegangen ist beim Durchdenken einer geisteswissenschaftlichen Wahrheit, ist typisch, denn immer wieder und wieder muß es vorkommen, daß man gegen dasjenige, was an Wahr­heiten zunächst herausgeholt wird aus der geistigen Welt, Widerspruch erhebt. Und gerade dies ist das Bedeutungsvolle und Richtige, daß sich solche Widersprüche erheben. Solche Widersprüche können nur dadurch beseitigt werden, daß man noch tiefer auf die Dinge eingeht. Das wollen wir heute in bezug auf gewisse Fragen der geistigen Erkenntnis tun. Dazu muß ich einiges vorausschicken.",
      "Wir lenken zunächst den Blick hin auf die materialistischen Vor­urteile unserer Zeit in bezug auf den Menschen. Nicht wahr, da ist es ein sehr begreifliches Vorurteil, daß im Menschen mannigfaltige phy­sische Vorgänge stattfinden, unter anderem auch Vorgänge in seinem Nervensystem und im Gehirn, und daß, indem diese physischen Vor­gänge sich vollziehen, die Seelenprozesse sich abspielen, die eigentlich für den Materialisten nur der Ausdruck dieser physischen Vorgänge sind. Der Materialist studiert dasjenige, was im Körper des Menschen vorgeht, findet - oder setzt es heute noch hypothetisch voraus - gewisse",
      "feine Nervenvorgänge und sagt: Das sind die Gründe für die Denk-, Gefühls- und Willensvorgänge; diese Denk-, Gefühls- und Willens-vorgänge sind eigentlich nur die Begleiterscheinungen desjenigen, was da physisch vorgeht. - Das ist heute eine weitverbreitete Anschauung, die in dem materialistischen Denken der neueren Zeit selbstverständlich noch tiefer Wurzel schlagen wird. Ebenso gescheit wie diese Ansicht, ist logisch die folgende. Nehmen wir an, jemand findet, indem er einen Weg geht, daß da allerlei Spuren in diesem Wege eingegraben sind; er findet Spuren, die so verlaufen, daß da so etwas wie Rinnen im Wege sind, und auch solche Spuren, welche Eindrücke von Füßen sind. Nun denkt er nach und sagt sich: Nun ja, da hat dasjenige, was diesen Weg bildet, die Materie, die dadrinnen ist, gewisse Prozesse entwickelt, und dadurch hat die Materie sich zusammengezogen, stückweise, und hat solche Rinnen gebildet; und dann hat sie wiederum an gewissen Stellen sich nach unten gezogen, und dann haben sich solche Eindrücke gebildet, die wie Fußsohlen aussehen.",
      "# Bild s. 114",
      "Nicht wahr, das ist natürlich ein großer Irrtum. Denn die Wahrheit ist, daß da ein Wagen gefahren ist und diese zwei Rinnen mit den Rä­dern gemacht hat, und daß da ein Mensch gegangen ist, der mit den Füßen diese Eindrücke gemacht hat. Nicht die Natur des Bodens hat diese Eindrücke gemacht, sondern der Mensch mit seinen Füßen und der Wagen mit seinen Rädern.",
      "So ist es aber auch mit den Vorgängen in unserem Nervensystem. Indem wir als Seelen denken, fühlen und wollen, bilden wir fortwäh­rend geistig-seelische Vorgänge. Die verlaufen, solange wir in der phy­sischen Welt leben, gebunden an den physischen Leib, wie der Wagen über den Weg fährt, und der Mensch über den Weg geht, und lassen dort",
      "ihre Spuren zurück. Diese Spuren, die sie dort zurücklassen, haben eben­sowenig mit der Materie zu tun, wie die Spuren im Wege etwas zu tun haben mit irgendeiner Materie, die darunter liegt. Gar nichts haben im Grunde genommen die Vorgänge in der Gehirnmaterie, in der Nerven-materie mit den Denkvorgängen zu tun, ebensowenig wie das, was der Wagen oder der Mensch vollführt, mit dem zu tun hat, was da auf der Oberfläche der Erde vor sich geht.",
      "Das ist sehr bedeutsam, daß man sich einmal einer solchen Betrach­tung hingibt, damit man verstehen lernt, daß der Anatom, der Physio­loge, wenn er bloß die Vorgänge im Organismus untersucht, einem Geist gleicht, der unten in der Erde sich bewegt, aber niemals über die Ober­fläche der Erde empordringt, niemals Menschen und Wagen gesehen hat. Er sieht nur innerhalb der Erde, daß da Unebenheiten entstehen, kommt aber nie heran, sieht sie noch dazu von der andern Seite. Das untersucht er dann und glaubt, daß die Erde selber dies durch ihre eigene Tätigkeit macht. In dem Augenblick, wo ein solcher Geist, der da immer unter der Erde ist, über die Erdoberfläche käme, würde er sich über den wahren Tatbestand aufklären. So ist es auch mit dem materialistischen Anatomen und dem materialistischen Physiologen; er ist immer unter der Erde, das heißt, er weiß nichts von Geisteswissenschaft, und das ist ein Unter-der-Erde-Sein. Er untersucht nur die Vorgänge in der Ma­terie, die gar nichts zu tun haben mit dem, was da oben geschieht im Geistig-Seelischen.",
      "Das wird die Aufgabe der neueren Zeit sein, daß die Menschen aus dem anatomischen, physiologischen Denken in das geisteswissenschaft­liche Denken eindringen. So ähnlich würde ein Kobold, der bisher nur unter der Erde gewesen ist, eindringen in die Wahrheit, wenn er hinauf-gehoben würde über die Erde und sehen würde, wie eigentlich die Ein­drücke zustande kommen, die in der Materie sind. Unter der Erde wühlende Kobolde sind im Grunde genommen die materialistischen Forscher, die sich nur mit dem unter der Erde befindlichen Geistigen beschäftigen, denn auch das Materielle ist Geistiges. Und die Mensch­heit muß durchmachen jenen großen Schock, der sich ergeben wird, wenn diese Kobolde, diese Erdengeister in die Region des Geistig-Seelischen eindringen.",
      "Nun, ich mußte das vorausschicken aus dem Grunde, weil ich Ihnen einiges zur Aufklärung sagen will über den vorhin angedeuteten Wider­spruch, daß der Bottnische, Finnische, Rigaische Meerbusen eigentlich Flächen sind, Ebenen, und ich doch so gesprochen habe, als ob das Wesen wären oder Teile von einer mächtigen Wesenheit, die sich vom Westen nach dem Osten erstreckt.",
      "Nun, sehen Sie, Raumeswesen, räumliche Wesen - ja, Sie sagen so ohne weiteres, ich bin doch als Mensch ein räumliches Wesen. Das ist wohl richtig. Aber das, was Sie als Mensch, als räumliches Wesen sind, sind Sie nicht in der Wirklichkeit. Denn mit diesem Menschen verhält es sich ganz anders, als man glauben kann, wenn man ihn nur in der äußeren Maja, in der äußeren Phantasmagorie anschaut. Da erscheint er allerdings als ein Wesen, das räumlich dasteht, räumlich in der Haut eingeschlossen ist, das räumlich sich ausdehnt. Aber hier verbergen sich in der Tat in bezug auf die menschliche Gestalt drei bedeutsame Rätsel, drei bedeutsame Fragen.",
      "Die erste Frage, die sich da verbirgt, tritt, möchte ich sagen, unter allerlei Vexieransichten auf, unter allerlei Täuschungen. Über unser eigenes Dasein werden wir durch die äußere Phantasmagorie, durch die äußere Maja eigentlich getäuscht. Die Spuren dieser Täuschung fin­den sich in der heutigen Wissenschaft, und zwar in dem Kapitel, wo diese Wissenschaft recht hilflos ist und alle möglichen Hypothesen auf­gestellt hat. Die Frage, die ich meine, verbirgt sich in der Wissenschaft dahinter, daß immer wieder Hypothesen aufgestellt werden, warum der Mensch eigentlich zwei Augen, zwei Ohren hat, und doch die Dinge nicht zweifach sieht und hört, warum eigentlich die Organe symme­trisch angeordnet sind, warum sie nicht einfach, sondern doppelt vor­handen sind. Das einfache Wahrnehmen bildet ein großes Problem, eine große Frage für die Wissenschaft, und wenn Sie die Literatur durch­nehmen, werden Sie finden, was da alles geschrieben worden ist über die Frage, warum wir eigentlich mit zwei Augen einfach sehen, mit zwei Ohren einfach hören und so weiter.",
      "Der Mensch ist in gewisser Weise recht grob organisiert und drückt das manchmal schon in seiner Sprache aus. Eigentlich hat er auch zwei Nasen, nur sind diese so zusammengewachsen, daß sie sich nicht so leicht",
      "überschauen lassen wie die beiden Augen, die beiden Ohren. Deshalb spricht man nicht von zwei Nasen, sondern nur von einer Nase, aber in Wirklichkeit hat der Mensch ebensogut zwei Nasen und nicht eine Nase.",
      "Nur ist er so grob organisiert, daß da, wo etwas zusammengewachsen ist, es ihm gar nicht auffällt. Aber auf jeden Fall ist es eine Tatsache, daß sich im menschlichen Wahrnehmen eine ganze Symmetrie, ein Links-Rechts ausdrückt.",
      "Wenn der Mensch nämlich nicht zwei Ohren hätte, zwei Augen, zwei Nasen, so würde in Wahrheit seine Ich-Empfindung nicht zustande kommen. Auch zwei Hände braucht er dazu. Indem wir die Hände zusammenschlagen und eine Hand an der andern fühlen, kommt schon etwas von der Ich-Empfindung zustande.",
      "Etwas ganz Ähnliches aber tun wir, indem wir das Ergebnis der beiden Augen, der beiden Ohren in eine Einheit zusammenfügen. Wir nehmen die Welt immer von zwei Seiten her wahr, von links und von rechts, wenn es sich um die Sinneswahrnehmung handelt.",
      "Und nur dadurch, daß wir diese zwei Wahrnehmungsrichtungen haben von links und von rechts und diese zum Schnitt bringen, sind wir dieser Ich-Mensch, der wir sind. Sonst wären wir gar nicht dieser Ich-Mensch.",
      "Wenn wir zum Beispiel die Augen so hätten, daß sie in der Nähe der Ohren stehen würden, und wir die Visierlinie nicht zusammenfügen könnten, so würden wir immer ein Wesen bleiben, das in der Gruppenseele befangen ist. Wir müssen, um ein Ich-Wesen zu sein, das Links und Rechts zum Schnitt bringen.",
      "Alles, was auf dem Gebiete der Wahrnehmung links und rechts ist, bringen wir zum Schnitt in der Mitte. Stellen Sie sich eine Fläche (es wird gezeichnet) vor, also eine Fläche, die von diesem Strich herausgeht",
      "# Bild s. 117",
      "von der Tafel. Da kommt alles zum Schnitt, von links her und von rechts her, und in dieser Ebene sind wir wirklich darinnen. Wir sind gar nicht im Raume, sondern in dieser Ebene darinnen, in dieser Fläche. Wir sind nicht der räumlich ausgedehnte Mensch in Wahrheit, sondern wir sind ein Flächenwesen, das dadurch zustande kommt, daß sich die Links­impulse mit den Rechtsimpulsen schneiden. Und wenn Sie jemandem Antwort erteilen wollen - ich meine in der Wirklichkeit, nicht in der Maja - auf die Frage: Wo bist du denn eigentlich?, so müssen Sie ihm nicht sagen: Ich bin da oder dort, in dem vom Körper ausgefüllten Raum -, sondern Sie müssen ihm sagen: Ich bin da, wo mein Links-mensch und mein Rechtsmensch sich schneiden. - Da sind Sie in Wirk­lichkeit nur. Genauso wie Flächen da sind bei dem Wesen, das ich vor­her meinte, in welchem sich die Lufthälfte und Wasserhälfte schneiden -da sind die beiden Hälften verschieden -, so sind beim Menschen die Linkshälfte und die Rechtshälfte da, - aber gleich. In Wahrheit ist auch der Mensch ein Flächenwesen, eine Ebene, und das schon ist Maja, daß er seine wirkliche Gestalt hat.",
      "Aber woher kommt sie denn, die wirkliche Gestalt? Ja, sehen Sie, sie kommt daher, daß der Mensch mitten darinnensteht in einer Art von Kampf. Von links her kämpft ein Wesen mit einem Wesen, das von rechts her kämpft. Würde das geistig wahrgenommen, was an unserer linken Seite ist, so würden wir dieses eine Wesen wahrnehmen wie Licht. Würde das an unserer rechten Seite Wirkende geistig wahrgenommen, so würden wir das andere Wesen mit andern Eigenschaften wahrneh­men. Als zweierlei Mensch kommen wir nämlich dadurch zustande, daß von links her kämpft die luziferische Wesenheit, von rechts her die ahrimanische Wesenheit.",
      "Nun denken Sie sich einmal, um sich das genau vorzustellen, von links kämpft die luziferische Wesenheit, staut da auf, was sie aufführt als Befestigungswerk; von rechts kämpft die ahrimanische Wesenheit und staut da auf, was sie aufführt als Befestigungswerk. Das, was Ihr Linksmensch ist, sind die Befestigungswerke des Luzifer; Ihr Rechts-mensch sind die Befestigungswerke des Ahriman. Und Sie haben über­haupt nur die Möglichkeit, zwischendrinnen in der Mitte zu sein. Unsere Lebenskunst besteht darin, daß wir das richtige Gleichgewicht finden.",
      "# Bild s. 119",
      "Unbewußt tun wir das, wenn wir sinnlich wahrnehmen. Wenn wir mit dem linken Ohr hören und mit dem rechten Ohr hören, und dann die Impulse zusammenfügen zu einer Wahrnehmung, oder wenn wir mit der linken Hand wahrnehmen und mit der rechten Hand wahrnehmen und die Wahrnehmungen zusammenfügen, so setzen wir uns immer in die Fläche, die gerade an der Grenze des Kampfes zwischen Luzifer und Ahriman liegt. Wie des Messers Schneide, ja noch schärfer als des Mes­sers Schneide ist der Spielraum, der uns in der Mitte gelassen ist. Unser Organismus gehört nicht uns) sondern er ist aufgeworfen durch den Kampf der luziferischen und ahrimanischen Mächte, aber auch der­jenigen Mächte, die gleichartig sind mit Luzifer und Ahriman. Das aber ist etwas, was jetzt nicht weiter berührt werden soll.",
      "So sind wir als Flächenwesen eingeschaltet zwischen etwas, was uns als Menschen gar nichts angeht. Unser linker Mensch geht uns eigentlich gar nichts an, unser rechter Mensch auch nicht, sondern der Prozeß, der Vorgang, der sich zwischen beiden abspielt.",
      "Und jetzt können Sie sich das Bild, das ich vorhin gebrauchte, weiter ausdenken. Nicht wahr, da geschehen fortwährend Prozesse, Vorgänge. Ja, in der Erde geschehen auch fortwährend Prozesse, Vorgänge. Aber das, was in der Erde vor sich geht, macht nicht diese Spuren. Was in Ihnen geschieht, in der linken oder rechten Hälfte des Organismus, das hat gar nichts zu tun mit dem, was der Mensch seelisch erlebt; das sind",
      "Prozesse, die sich zwischen Luzifer und Ahriman abspielen. Die Pro­zesse, die unten, unter der Erdoberfläche sind, alles, was da geschieht, meinetwegen sagen wir das Herumkriechen der Würmer, das Kalt- und Warmwerden in den Jahreszeiten, all diese Prozesse, die nichts zu tun haben mit diesen Spuren, die da eingedrückt werden, müssen Sie ver­gleichen mit dem, was drinnen vorgeht in der Menschenorganisation.",
      "So daß man sagen muß: Durch die geistige Beobachtung der physiolo­gischen und anatomischen Vorgänge muß man darauf kommen, wie Luzifer und Ahriman miteinander kämpfen, muß sich aber nicht der Meinung hingeben, daß durch diese Prozesse zwischen Luzifer und Ahriman das seelische Leben bewirkt wird. Das ist nicht richtig, denn das verläuft in der Seele selber.",
      "Und das verläuft im Grunde genommen in der Fläche, in der Ebene, nicht in dem Organismus darinnen, in dem räumlichen Organismus; es stuft sich ab, und die Betrachtung dieser Abstufung ist außerordentlich interessant. In bezug auf den Kopf des Menschen, da ist es so, daß Luzifer und Ahriman ziemlich gleiche Be­festigungswerke links und rechts aufgeworfen haben.",
      "Die linke und rechte Kopfhälfte sind sehr ähnlich, da sind die Kräfte so, daß sie wenig ineinanderspielen können, daß sie die Fläche in der Mitte wenig berüh­ren. In der Mitte ist die Fläche, links Luzifer, rechts Ahriman; aber weil linke und rechte Kopfhälfte so ähnlich gebildet sind, prallen sie an­einander ab: Luzifer und Ahriman, und der Mensch kann in der Mitte hier eine ruhige Tätigkeit entwickeln (siehe Zeichnung Seite 121).",
      "Sein Denken wird recht wenig gestört durch den Einfluß von Luzifer und Ahriman, weil sie da aneinander abprallen.",
      "Kommt man weiter nach unten, ist es schon nicht mehr so. Auf der einen Seite gelingt es Luzifer, den Magen aufzutürmen, auf der andern Seite gelingt es Ahriman, die Leber aufzutürmen. Und der Magen ist das Mittel, durch das Luzifer kämpft von links nach rechts, die Leber ist etwas, durch das Ahriman kämpft von rechts nach links. Das Verhältnis von Magen und Leber betrachtet man in der richtigen Weise, wenn man ins Auge faßt, daß es Luzifer gelingt, links den Magen aufzutürmen als eine Art Kampfmittel, und daß es rechts Ahriman gelingt, die Leber aufzutürmen. Das steht in einem fortwährenden Kampf, und die Wis­senschaft würde gut tun, diesen Kampf zwischen Magen und Leber",
      "# Bild s. 121",
      "wirklich zu studieren. Und wenn die Lage des Herzens einmal ein wenig nach der linken Seite herüber tendiert, so ist diese Lage ein Ausdruck für das, wie auf der einen Seite Luzifer etwas für sich erhaschen will, während auf der andern Seite Ahriman etwas erhaschen will. Das ganze Links-Rechtsverhältnis ist ein Ausdruck für dasjenige, in welchem sich Luzifer und Ahriman im Menschen bekämpfen, nur daß beim Men­schen, wie gesagt, das, was auf beiden Seiten der Fläche liegt, in gewisser Beziehung gleich ist. Aber wir sehen ja, eigentlich gleich ist es nur da oben; es hört auf, gleich zu sein, je weiter wir den Menschen nach unten verfolgen.",
      "Bei dem Wesen, von dem ich gesprochen habe, daß es wie drei Fang­arme - Lemminkäinen, Ilmarinen und Wäinämöinen - vorstreckt, ist es so, da ist die eine Hälfte Luft, die andere Wasser; da sind sie noch verschieden. Sobald man nun zur hellsichtigen Erkenntnis kommt, fällt einem aber gleich auf, daß der Mensch im Grunde genommen auch nur eine Fläche ist zwischen zwei Hälften, denn sobald man sich absugge­riert den physischen Leib und auf den Ätherleib hinblickt, findet man, daß die linke Hälfte wesentlich heller wird als die rechte Hälfte. Die linke Hälfte sieht sich an viel mehr durchhellt, durchstrahlt, durch-glitzert, durchglimmert; die rechte Hälfte viel mehr durchfinstert, durchdunkelt. So ist es mit Bezug auf den Links-Rechtsmenschen.",
      "Nun ist aber der Mensch auch in bezug auf andere Richtungen hin­eingestellt in den Raum, das heißt aber - okkultistisch ausgedrückt -nichts anderes als hineingestellt in den Kampf zwischen Luzifer und Ahriman. So ist er hineingestellt in das Vorne und Hinten, Vorne und Rückwärts.",
      "Wenn Sie sich nun nicht das Links und Rechts denken, sondern das Vorne und Rückwärts am Menschen - den ganzen Menschen müssen Sie sich denken -, dann ist der Mensch auch nicht in der Richtung von vorne nach hinten dieses Raumeswesen (siehe Zeichnung), sondern gerade so, wie von links herüber und von rechts herüber Luzifer und Ahriman sich bekämpfen, und das Räumliche nur die Barrikaden sind, die sie auf­gerichtet haben gegeneinander, kämpft auch von rückwärts Ahriman wieder gegen den Menschen und von vorne wiederum Luzifer. Von rückwärts schiebt sozusagen seine Tätigkeit Ahriman vor; von vorne schiebt seine Tätigkeit Luzifer dem Ahriman entgegen. Und der Mensch steht wieder mitten darinnen.",
      "# Bild s. 122",
      "Allerdings kommen wir jetzt dazu, ausführen zu müssen, daß es in bezug auf diese Richtung vorne-rückwärts den beiden nicht so gelungen ist, ich möchte sagen, so nahe aneinander heranzukommen, daß sie nur eine Fläche bildeten. Hier ist es schon anders. Ahriman kommt nämlich",
      "nur bis zu einer Fläche, die Sie sich durch das Rückgrat legen können, und Luzifer kommt bis zu einer Fläche, die Sie sich durch das Brustbein legen können, etwa da, wo die Rippen zusammenstoßen. Und da­zwischen ist ein Raum, durch den sie getrennt sind, wo ihre Wirkungen durcheinandergehen. Sie kämpfen da, man möchte sagen, nicht un­mittelbar aneinander stoßend, sondern sie senden ihre Geschosse durch diesen Raum hindurch. Aber Ahriman kommt nur bis zum Rückgrat und Luzifer nur bis dahin, wo die Rippen an das Brustbein anstoßen. Und wir stehen da drinnen, zwischen diesem Kampf von Luzifer und Ahriman. Also in bezug auf die Vorwärts- und Rückwärts richtung sind wir in der Tat ein solches Wesen, welches Raum hat. In bezug auf links und rechts haben wir keinen Raum.",
      "# Bild s. 123",
      "In der Richtung links-rechts kämpfen Luzifer und Ahriman vor­zugsweise durch die Gedanken. Da schwirren die Gedanken von links und von rechts herüber und berühren sich in dieser Fläche. Es sind kos­mische Gedankenbildungen, die da aneinanderstoßen und sich in der menschlichen Mittelfläche berühren. Vorne und rückwärts kämpfen",
      "Luzifer und Ahriman mehr mit Gefühlen, da wird der Kampf mehr durch die Gefühle geführt. Und weil hier die Kräfte nicht so recht an­einanderkommen, bleibt für uns in der Mitte ein Spielraum, in welchem wir mit unseren Gefühlen in uns selber sind. Wir spüren, wenn wir Ge­danken haben, die von links und rechts einander bekämpfen, daß diese Gedanken eigentlich der Welt angehören. Mit den Gedanken denken wir die Dinge, die draußen sind.Wenn wir uns eigene Gedanken machen, so sind das Phantasmagorien, dann gehören sie eigentlich nicht mehr der Welt an. In unseren Gefühlen gehören wir uns selber an, weil Luzi­fer und Ahriman da nicht ganz aneinanderstoßen, weil wir da Spiel­raum haben zwischen den beiden Gebieten. Deshalb sind wir mit un­seren Gefühlen so in uns selber.",
      "Sehen Sie, wir sind als Menschen Geschöpfe durch die Wirkungs­weise der Wesen der höheren Hierarchien. Und wir sind dieses Flä­chenwesen links und rechts dadurch, daß die höheren Hierarchien uns Menschen da hineinstellen als Flächenwesen. Da lassen sie Luzifer und Ahriman nicht zusammenkommen. Wir sind insofern ein Wesen der guten Götter, als diese guten Götter aus ihren Schöpfungsgedan­ken heraus gesagt haben: Da liegt vor uns ein Kampf zwischen Luzifer und Ahriman. Nun müssen wir eine Grenze aufrichten für ein Gebiet, in das sie nicht hineinkommen, daß sie nicht unmittelbar aneinander herankönnen. - Wir Menschen sind hineingestellt in diesen Kampf als Geschöpfe der guten Götter, und je mehr wir uns bewähren in diesem Kampf, desto mehr sind wir Geschöpfe der guten Götter.",
      "In bezug auf das Vorne und Rückwärts ist es so, daß die guten Götter Luzifer nicht ganz in uns hineinlassen. Da haben sie in dem Rippenabschluß nach vorne ihm Barrikaden aufgerichtet. Und in der Ausbildung dieses wunderbaren Turmes, der das Rückenmark und das Gehirn umschließt, haben die guten Götter ein Befestigungswerk gegen Ahriman aufgerichtet. Das kann er nicht passieren, da kann er höch­stens seine Gefühlsgeschosse hinüberschicken zu Luzifer. Da stehen wir wirklich darinnen, um die beiden voneinander zu trennen durch einen Spielraum.",
      "Es gibt noch eine dritte Richtung, das ist die von oben nach unten. Da müssen wir uns klar sein darüber, daß die Sache sich auch nicht",
      "so verhält, wie sie in der äußeren Phantasmagorie, der Maja aussieht. Da ist es so, daß von unten herauf Ahriman spielt, von oben herunter Luzifer. Und auch da haben die guten, fortschreitenden Götterwesen eine Barriere errichtet gegenüber Luzifer. Seine Wirkungen von oben nach unten werden sozusagen aufgehalten durch eine Fläche. Sie be­kommen diese Fläche, wenn Sie ein Skelett nehmen und den Schädel herunternehmen. Da, wo der Schädel auf den Halswirbeln aufsitzt, müssen Sie sich eine Fläche denken. Diese unsichtbare horizontale Fläche, wo der Schädel aufsitzt auf dem Halswirbel, ist die Barriere. Wenn ein Mensch sich da hineinstellt, kann er die von oben nach un­ten gehenden luziferischen Wirkungen aufhalten. Luzifer kann nur von oben seine Geschosse hineinschicken; und das sind jetzt Willens­geschosse. Von links nach rechts Gedankengeschosse, von vorne nach rückwärts Gefühlsgeschosse, von oben nach unten und von unten nach oben gehen die Willensgeschosse.",
      "# Bild s. 125",
      "Aber auch hier ist ein Spielraum. Wenn Sie unten das Zwerchfell nehmen, so haben Sie ungefähr dem Zwerchfell entlang gehend die Fläche, die wieder aufgerichtet ist gegen den von unten nach oben",
      "drängenden Ahriman. Also mit seinem Wollen, mit seinen Willens­geschossen, mit seinem eigenen Wesen kann Ahriman nur von unten nach oben bis zum Zwerchfell gelangen. Weiter kann er nie mit seinen Geschossen wirken. Das ist unser eigener Spielraum, was darüber ist.",
      "Nun sehen Sie, wie kompliziert eigentlich der Mensch ist. Nehmen Sie irgendein Stück der Menschennatur, ich will sagen, die linke Seite des Antlitzes. Als Gedankenwesen kann Luzifer diese linke Seite ganz durchdringen, auch noch als Gefühlswesen kann er sie in gewisser Weise durchdringen bis zu einer gewissen Fläche; als Willenswesen kann er sie wiederum durchdringen von oben nach unten. So können Sie von jeder Partie des Menschen durch diese Angaben herausfinden, wie Lu­zifer und Ahriman durch kosmische Gedanken-, Gefühls- oder Wil­lensimpulse in dem Raumesmenschen darinnen wirken.",
      "Aber klar muß man sich darüber sein, daß wir als Gedankenmensch eigentlich ein Flächenwesen sind. Als Gefühlsmensch haben wir einen gewissen Spielraum zwischen vorn und rückwärts, als Willensmensch haben wir einen gewissen Spielraum zwischen oben und unten, zwischen dieser Fläche hier - durch den oberen Halswirbel - und der Fläche des Zwerchfells. Und nur wenn Sie sich dasjenige aussondern, was gar nicht zum Menschen gehört, dann bekommen Sie die wahre Gestalt des Men­schen. Die können Sie sich nun konstruieren.",
      "Aber Sie sehen, daß der Mensch in Wirklichkeit von außen her zu­sammengefügt ist, daß er von außen her sein Gepräge erhält, und daß wir ihn nicht verstehen, wenn wir einfach die Formen so nehmen, wie sie uns entgegentreten, sondern daß wir ihn erst dann verstehen, wenn wir wissen, wie er mit dem ganzen Geistig-Kosmischen zusammen­hängt, wie da von rechts und links, von unten und oben, von vorne und rückwärts die luziferisch-ahrimanischen Kräfte an den Menschen herankommen und wie sie so sein Wesen als Raumeswesen prägen.",
      "Sehen Sie, so müssen Sie auch dasjenige betrachten, was in gewisser Weise nachgebildet ist dem wahren kosmischen Wirken in der Welt, so müssen Sie unseren Bau betrachten. Wenn wir ihn als Phantas­magorie betrachten, so könnten wir zunächst glauben, daß das Haupt­sächlichste an diesem Bau dasjenige ist, was da von Holz ausgefüllt ist im Raum. Das ist aber nicht die Hauptsache, sondern die Hauptsache",
      "ist das, wo scheinbar nichts ist. Wenn irgendeine Form in un­serem Bau so geht (siehe Zeichnung) und da ist das Holz, so ist das",
      "# Bild s. 127",
      "Wesentliche nicht dieses hier, das Holz, sondern dasjenige, wo nichts ist, wo die Luft angrenzt. Und unseren richtigen Bau würden Sie be­kommen, wenn Sie einen riesigen Wachsklumpen nehmen würden und einen Abdruck machten von dem Inneren, und würden dann den Ab­druck anschauen. Also dasjenige, in dem Sie, wenn Sie in den Bau hin­eingehen, darinnenstehen, was Sie nicht sehen können, sondern fühlen müssen, das ist es eigentlich, worauf es ankommt. Ich habe schon frü­her gesagt: Das Prinzip unseres Baues ist das eines Gugelhupftopfes. -Gugelhupftopf ist ein Ausdruck, den man hier nicht gut verstehen wird. Aber denken Sie sich hier einen Topf: das ist die Form, da drin­nen backt man einen Gugelhupf. Auf was kommt es denn da an bei diesem Gugelhupftopfe? Es kommt nicht auf den Topf an, sondern es kommt auf den Kuchen an, daß der eine richtige Form bekommt und in der richtigen Weise drinnen gedeiht. Der Topf muß nur so sein, daß, wenn man Teig hineingießt und ihn bäckt, der Gugelhupf in der richtigen Weise zustande kommt.",
      "So kommt es bei unserem Bau auch nicht darauf an, was die Um­gebung ist, sondern auf das, was darinnen ist. Und darinnen werden sein die Gefühle und Gedanken derer, die im Bau darinnen sind. Die werden dadurch entstehen, daß der Mensch bis an die Grenze des",
      "Baues sieht, daß er die Formen fühlt, und daß er sich ausfüllt mit Ge­dankenformen. Das, was darinnen ist, das wird der Gugelhupf sein, und das, was wir bauen, ist die Hülle, die Form. Aber die muß so sein, daß das Richtige darinnen gedacht, gefühlt und empfunden wird. Und das ist das Prinzip, sehen Sie, der neueren Kunst gegenüber der alten Kunst. Bei den alten Künsten kam es immer darauf an, was draußen im Raume ist. Bei der neuen Kunst kommt es nicht darauf an, was im Raume draußen ist. Was draußen ist, das ist der Topf, und das, wor­auf es ankommt, das kann man eigentlich gar nicht machen, sondern das ist darinnen. Das gilt nicht nur in bezug auf plastische Formen, sondern auch in bezug auf Malerei. Es kommt auch da nicht darauf an, was gemalt wird, sondern was dabei empfunden und erlebt wird. Auch die Malerei ist bloß «Gugelhupftopf».",
      "Das ist, möchte ich sagen, der Kernpunkt des Evolutionsfortschrit­tes, in dem wir darinnenstehen, daß wir wirklich - verzeihen Sie den Ausdruck - aus dem Topf in den Kuchen hineinkommen. Im Topfe bleiben, heißt Materialismus; in den Kuchen hineinkommen, heißt bei uns Spiritualismus, und der ist dasjenige, dem wir entgegenarbeiten. Wenn man das nicht berücksichtigt, wird man auch alles Künstlerische, um das es sich bei uns handelt, nicht in der richtigen Weise beurteilen können. Wenn man künstlerisch unseren Bau nach dem Muster des Alten auffaßt, so wird man sagen können: Ja, aber um Gotteswillen, du hast gar keinen schönen Topf gemacht! - Man wird nämlich nicht wissen, daß es auf den Topf nicht ankommt, sondern auf den Gugel­hupf. Damit nähern wir uns, mit einem solchen künstlerischen Prin­zip, dem ganzen Sinn und der ganzen Bedeutung des Evolutionsfort­schrittes durch die Geisteswissenschaft. Der Mensch muß sich durch den Fortschritt der Geisteswissenschaft herausarbeiten aus dem Topf und muß sich in den Gugelhupf hineinarbeiten.",
      "Und so muß er von dem Glauben loskommen, daß zum Beispiel in den Gehirnprozessen die Ursachen der Gedanken liegen, während in den Eigenprozessen des Gehirns kosmische Vorgänge liegen, und die Kämpfe zwischen Luzifer und Ahriman sich abspielen. Und er muß einsehen, daß die menschlichen Seelenvorgänge, die Gedanken und Empfindungen nur die Spuren sind, die in diese Kampfverschanzungen",
      "eingegraben werden, die aber mit den sogenannten materiellen Vorgängen - mit andern Worten mit den luziferisch-ahrimanischen Vorgängen - nichts zu tun haben.",
      "Ich möchte noch ein anderes Bild gebrauchen. Nehmen wir an, wir kommen in einen schönen Garten, schön dadurch, daß die Anordnung der Bäume schön ist, die Arrangements in bezug auf die Blumenver­teilung schön sind und so weiter, und wir wollen uns eine Ansicht dar­über bilden. Da käme, wenn wir durch ein Loch in die Erde hinein­blicken könnten, so ein Kobold an uns heran. Dieser Kobold - nehmen wir an - sagte uns nun: Ich will dir sagen, warum da Rosen, Veil­chen, warum da ein Busch und da Blumen sind. Ich krieche nämlich da unten unter der Erdoberfläche überall herum, und da sehe ich den Grund, der die Bäume, Veilchen, Rosen hat hervorsprießen lassen. -Wir können sagen: Ja, du erzählst uns ganz schön diese Vorgänge. Das, was du da erzählst, muß alles geschehen können in der physischen Welt. Aber damit die Pflanzen gedeihen können, der Garten entstan­den ist, mußte ein Gärtner da sein. Das aber sind Regionen, in die du gar nicht hineingeschaut hast, um die du dich gar nicht gekümmert hast.",
      "So müssen wir lernen, zu den materialistischen Anatomen, den ma­terialistischen Physiologen zu sagen: Deine Tätigkeit finde ich erst, wenn ich durch das Guckloch in die Erde schaue. Da kriechst du her­um und studierst Vorgänge, die geschehen müssen, die aber nichts zu tun haben mit dem, was da oben an Seelisch-Geistigem vorgeht. Und du wirst das, was da unten vorgeht, erst richtig deuten, wenn du dich darauf einläßt, zu erkennen, welche Beziehungen herrschen zwischen Luzifer und Ahriman und den andern Hierarchien, welche Luzifer und Ahriman wieder in den Gleichgewichtszustand bringen. - Und es wird sich dasjenige, was bisher gewissermaßen nur wie in der Ich-Vor­stellung gewirkt hat, bereichern durch die Geisteswissenschaft.",
      "Es wird eine Zeit kommen, da werden sich die Menschen sagen:",
      "Uns wird mitgeteilt in der biblischen Schöpfungsurkunde von dem Hauche, von dem Ateinzuge des Jahve, der eingehaucht wurde dem Menschen. - Dann werden die Menschen der Zukunft fragen: Ja, wenn dieser Atemzug eingehaucht wird, wohin wird er denn eingehaucht? -",
      "Wenn Sie zusammenhalten, was ich gesagt habe, so werden Sie finden, daß das nächste, wohin gehaucht wurde, diese Zwischenräume sind, wo sich von vorne und rückwärts, von oben und unten gleichsam als einen Kubus Jahve den Menschen schafft (siehe Zeichnung) und ihn so ausfüllt mit seinem eigenen Wesen, mit seinem Zauberhauche, daß dann im übrigen Menschen sich nun ausbreitet die Wirkung dieses Zauberhauches in die Regionen von Luzifer und Ahriman. Aber hier ist ein Zwischenraum, begrenzt von rechts und links, von oben und unten, von vorne und rückwärts, wo hinein unmittelbar als in den Raumesmenschen Jahves Hauch geht. Was ich gesagt habe, ist zu­nächst in bezug auf diesen physischen Raumesmenschen gesagt.",
      "# Bild s. 130",
      "Sie sehen, dies macht uns die Aussicht frei, von der aus wir er­blicken den Menschen darinnenstehend im ganzen Kosmos. Ich möchte sagen: In bezug auf dasjenige, was er scheinbar äußerlich räumlich ausfüllt, dieser Mensch, von alledem gibt es auch moralisch-seelische Aspekte. Denn auch in dem, was als Moralisch-Seelisches in uns wirkt, haben wir zunächst, wenn auch nicht in so starkem Grade wie in dem Raumesmenschen, eine Phantasmagorie Und in allem Moralischen, in allem Logischen, in allem, was in unserer Seelentätigkeit ist, wirken Luzifer und Ahriman aufeinander, und der Mensch ist aufgestellt an der Grenze.",
      "Wie das ist, dieses für uns ganz besonders bedeutungsvolle und wich­tige Kapitel wollen wir dann morgen besprechen."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Es wird Ihnen in dem einen Vortrag, den ich im Anschlusse an Kalewala gehalten habe, etwas aufgefallen sein.",
        "Als Sie diesen Vortrag durchdacht haben, werden Sie sich gesagt haben, denn das ist naheliegend, da wurde ausgeführt, daß gewissermaßen ein Wesen herüberragt vom Westen nach dem Osten und drei Ausläufer wie drei Gliedmaßen vorstreckt, die von dem alten finnischen Volk empfunden wurden als Wäinämöinen, Ilmarinen und Lemminkäinen, und die man heute in der materialisti­schen Sprache den Rigaischen, den Finnischen, den Bottnischen Meerbusen nennt.",
        "Nur werden Sie sich gefragt haben: Ja, aber wie kann er sagen, daß das etwas zu tun hat mit einer Wesenheit, denn das ist doch nur eine Fläche, die Oberfläche des Meeres mit ihren Grenzen, die da so sich vorgestreckt hat.",
        "Es hat nichts Körperhaftes, und doch redet er uns von einer Wesenheit! - So werden Sie sich gesagt haben."
      ],
      [
        "Dieses, was da in Ihrer Seele vorgegangen ist beim Durchdenken einer geisteswissenschaftlichen Wahrheit, ist typisch, denn immer wieder und wieder muß es vorkommen, daß man gegen dasjenige, was an Wahr­heiten zunächst herausgeholt wird aus der geistigen Welt, Widerspruch erhebt.",
        "Und gerade dies ist das Bedeutungsvolle und Richtige, daß sich solche Widersprüche erheben.",
        "Solche Widersprüche können nur dadurch beseitigt werden, daß man noch tiefer auf die Dinge eingeht.",
        "Das wollen wir heute in bezug auf gewisse Fragen der geistigen Erkenntnis tun.",
        "Dazu muß ich einiges vorausschicken."
      ],
      [
        "Wir lenken zunächst den Blick hin auf die materialistischen Vor­urteile unserer Zeit in bezug auf den Menschen.",
        "Nicht wahr, da ist es ein sehr begreifliches Vorurteil, daß im Menschen mannigfaltige phy­sische Vorgänge stattfinden, unter anderem auch Vorgänge in seinem Nervensystem und im Gehirn, und daß, indem diese physischen Vor­gänge sich vollziehen, die Seelenprozesse sich abspielen, die eigentlich für den Materialisten nur der Ausdruck dieser physischen Vorgänge sind.",
        "Der Materialist studiert dasjenige, was im Körper des Menschen vorgeht, findet - oder setzt es heute noch hypothetisch voraus - gewisse"
      ],
      [
        "feine Nervenvorgänge und sagt: Das sind die Gründe für die Denk-, Gefühls- und Willensvorgänge; diese Denk-, Gefühls- und Willens-vorgänge sind eigentlich nur die Begleiterscheinungen desjenigen, was da physisch vorgeht. - Das ist heute eine weitverbreitete Anschauung, die in dem materialistischen Denken der neueren Zeit selbstverständlich noch tiefer Wurzel schlagen wird.",
        "Ebenso gescheit wie diese Ansicht, ist logisch die folgende.",
        "Nehmen wir an, jemand findet, indem er einen Weg geht, daß da allerlei Spuren in diesem Wege eingegraben sind; er findet Spuren, die so verlaufen, daß da so etwas wie Rinnen im Wege sind, und auch solche Spuren, welche Eindrücke von Füßen sind.",
        "Nun denkt er nach und sagt sich: Nun ja, da hat dasjenige, was diesen Weg bildet, die Materie, die dadrinnen ist, gewisse Prozesse entwickelt, und dadurch hat die Materie sich zusammengezogen, stückweise, und hat solche Rinnen gebildet; und dann hat sie wiederum an gewissen Stellen sich nach unten gezogen, und dann haben sich solche Eindrücke gebildet, die wie Fußsohlen aussehen."
      ],
      [
        "# Bild s. 114"
      ],
      [
        "Nicht wahr, das ist natürlich ein großer Irrtum.",
        "Denn die Wahrheit ist, daß da ein Wagen gefahren ist und diese zwei Rinnen mit den Rä­dern gemacht hat, und daß da ein Mensch gegangen ist, der mit den Füßen diese Eindrücke gemacht hat.",
        "Nicht die Natur des Bodens hat diese Eindrücke gemacht, sondern der Mensch mit seinen Füßen und der Wagen mit seinen Rädern."
      ],
      [
        "So ist es aber auch mit den Vorgängen in unserem Nervensystem.",
        "Indem wir als Seelen denken, fühlen und wollen, bilden wir fortwäh­rend geistig-seelische Vorgänge.",
        "Die verlaufen, solange wir in der phy­sischen Welt leben, gebunden an den physischen Leib, wie der Wagen über den Weg fährt, und der Mensch über den Weg geht, und lassen dort"
      ],
      [
        "ihre Spuren zurück.",
        "Diese Spuren, die sie dort zurücklassen, haben eben­sowenig mit der Materie zu tun, wie die Spuren im Wege etwas zu tun haben mit irgendeiner Materie, die darunter liegt.",
        "Gar nichts haben im Grunde genommen die Vorgänge in der Gehirnmaterie, in der Nerven-materie mit den Denkvorgängen zu tun, ebensowenig wie das, was der Wagen oder der Mensch vollführt, mit dem zu tun hat, was da auf der Oberfläche der Erde vor sich geht."
      ],
      [
        "Das ist sehr bedeutsam, daß man sich einmal einer solchen Betrach­tung hingibt, damit man verstehen lernt, daß der Anatom, der Physio­loge, wenn er bloß die Vorgänge im Organismus untersucht, einem Geist gleicht, der unten in der Erde sich bewegt, aber niemals über die Ober­fläche der Erde empordringt, niemals Menschen und Wagen gesehen hat.",
        "Er sieht nur innerhalb der Erde, daß da Unebenheiten entstehen, kommt aber nie heran, sieht sie noch dazu von der andern Seite.",
        "Das untersucht er dann und glaubt, daß die Erde selber dies durch ihre eigene Tätigkeit macht.",
        "In dem Augenblick, wo ein solcher Geist, der da immer unter der Erde ist, über die Erdoberfläche käme, würde er sich über den wahren Tatbestand aufklären.",
        "So ist es auch mit dem materialistischen Anatomen und dem materialistischen Physiologen; er ist immer unter der Erde, das heißt, er weiß nichts von Geisteswissenschaft, und das ist ein Unter-der-Erde-Sein.",
        "Er untersucht nur die Vorgänge in der Ma­terie, die gar nichts zu tun haben mit dem, was da oben geschieht im Geistig-Seelischen."
      ],
      [
        "Das wird die Aufgabe der neueren Zeit sein, daß die Menschen aus dem anatomischen, physiologischen Denken in das geisteswissenschaft­liche Denken eindringen.",
        "So ähnlich würde ein Kobold, der bisher nur unter der Erde gewesen ist, eindringen in die Wahrheit, wenn er hinauf-gehoben würde über die Erde und sehen würde, wie eigentlich die Ein­drücke zustande kommen, die in der Materie sind.",
        "Unter der Erde wühlende Kobolde sind im Grunde genommen die materialistischen Forscher, die sich nur mit dem unter der Erde befindlichen Geistigen beschäftigen, denn auch das Materielle ist Geistiges.",
        "Und die Mensch­heit muß durchmachen jenen großen Schock, der sich ergeben wird, wenn diese Kobolde, diese Erdengeister in die Region des Geistig-Seelischen eindringen."
      ],
      [
        "Nun, ich mußte das vorausschicken aus dem Grunde, weil ich Ihnen einiges zur Aufklärung sagen will über den vorhin angedeuteten Wider­spruch, daß der Bottnische, Finnische, Rigaische Meerbusen eigentlich Flächen sind, Ebenen, und ich doch so gesprochen habe, als ob das Wesen wären oder Teile von einer mächtigen Wesenheit, die sich vom Westen nach dem Osten erstreckt."
      ],
      [
        "Nun, sehen Sie, Raumeswesen, räumliche Wesen - ja, Sie sagen so ohne weiteres, ich bin doch als Mensch ein räumliches Wesen.",
        "Das ist wohl richtig.",
        "Aber das, was Sie als Mensch, als räumliches Wesen sind, sind Sie nicht in der Wirklichkeit.",
        "Denn mit diesem Menschen verhält es sich ganz anders, als man glauben kann, wenn man ihn nur in der äußeren Maja, in der äußeren Phantasmagorie anschaut.",
        "Da erscheint er allerdings als ein Wesen, das räumlich dasteht, räumlich in der Haut eingeschlossen ist, das räumlich sich ausdehnt.",
        "Aber hier verbergen sich in der Tat in bezug auf die menschliche Gestalt drei bedeutsame Rätsel, drei bedeutsame Fragen."
      ],
      [
        "Die erste Frage, die sich da verbirgt, tritt, möchte ich sagen, unter allerlei Vexieransichten auf, unter allerlei Täuschungen.",
        "Über unser eigenes Dasein werden wir durch die äußere Phantasmagorie, durch die äußere Maja eigentlich getäuscht.",
        "Die Spuren dieser Täuschung fin­den sich in der heutigen Wissenschaft, und zwar in dem Kapitel, wo diese Wissenschaft recht hilflos ist und alle möglichen Hypothesen auf­gestellt hat.",
        "Die Frage, die ich meine, verbirgt sich in der Wissenschaft dahinter, daß immer wieder Hypothesen aufgestellt werden, warum der Mensch eigentlich zwei Augen, zwei Ohren hat, und doch die Dinge nicht zweifach sieht und hört, warum eigentlich die Organe symme­trisch angeordnet sind, warum sie nicht einfach, sondern doppelt vor­handen sind.",
        "Das einfache Wahrnehmen bildet ein großes Problem, eine große Frage für die Wissenschaft, und wenn Sie die Literatur durch­nehmen, werden Sie finden, was da alles geschrieben worden ist über die Frage, warum wir eigentlich mit zwei Augen einfach sehen, mit zwei Ohren einfach hören und so weiter."
      ],
      [
        "Der Mensch ist in gewisser Weise recht grob organisiert und drückt das manchmal schon in seiner Sprache aus.",
        "Eigentlich hat er auch zwei Nasen, nur sind diese so zusammengewachsen, daß sie sich nicht so leicht"
      ],
      [
        "überschauen lassen wie die beiden Augen, die beiden Ohren.",
        "Deshalb spricht man nicht von zwei Nasen, sondern nur von einer Nase, aber in Wirklichkeit hat der Mensch ebensogut zwei Nasen und nicht eine Nase."
      ],
      [
        "Nur ist er so grob organisiert, daß da, wo etwas zusammengewachsen ist, es ihm gar nicht auffällt.",
        "Aber auf jeden Fall ist es eine Tatsache, daß sich im menschlichen Wahrnehmen eine ganze Symmetrie, ein Links-Rechts ausdrückt."
      ],
      [
        "Wenn der Mensch nämlich nicht zwei Ohren hätte, zwei Augen, zwei Nasen, so würde in Wahrheit seine Ich-Empfindung nicht zustande kommen.",
        "Auch zwei Hände braucht er dazu.",
        "Indem wir die Hände zusammenschlagen und eine Hand an der andern fühlen, kommt schon etwas von der Ich-Empfindung zustande."
      ],
      [
        "Etwas ganz Ähnliches aber tun wir, indem wir das Ergebnis der beiden Augen, der beiden Ohren in eine Einheit zusammenfügen.",
        "Wir nehmen die Welt immer von zwei Seiten her wahr, von links und von rechts, wenn es sich um die Sinneswahrnehmung handelt."
      ],
      [
        "Und nur dadurch, daß wir diese zwei Wahrnehmungsrichtungen haben von links und von rechts und diese zum Schnitt bringen, sind wir dieser Ich-Mensch, der wir sind.",
        "Sonst wären wir gar nicht dieser Ich-Mensch."
      ],
      [
        "Wenn wir zum Beispiel die Augen so hätten, daß sie in der Nähe der Ohren stehen würden, und wir die Visierlinie nicht zusammenfügen könnten, so würden wir immer ein Wesen bleiben, das in der Gruppenseele befangen ist.",
        "Wir müssen, um ein Ich-Wesen zu sein, das Links und Rechts zum Schnitt bringen."
      ],
      [
        "Alles, was auf dem Gebiete der Wahrnehmung links und rechts ist, bringen wir zum Schnitt in der Mitte.",
        "Stellen Sie sich eine Fläche (es wird gezeichnet) vor, also eine Fläche, die von diesem Strich herausgeht"
      ],
      [
        "# Bild s. 117"
      ],
      [
        "von der Tafel.",
        "Da kommt alles zum Schnitt, von links her und von rechts her, und in dieser Ebene sind wir wirklich darinnen.",
        "Wir sind gar nicht im Raume, sondern in dieser Ebene darinnen, in dieser Fläche.",
        "Wir sind nicht der räumlich ausgedehnte Mensch in Wahrheit, sondern wir sind ein Flächenwesen, das dadurch zustande kommt, daß sich die Links­impulse mit den Rechtsimpulsen schneiden.",
        "Und wenn Sie jemandem Antwort erteilen wollen - ich meine in der Wirklichkeit, nicht in der Maja - auf die Frage: Wo bist du denn eigentlich?, so müssen Sie ihm nicht sagen: Ich bin da oder dort, in dem vom Körper ausgefüllten Raum -, sondern Sie müssen ihm sagen: Ich bin da, wo mein Links-mensch und mein Rechtsmensch sich schneiden. - Da sind Sie in Wirk­lichkeit nur.",
        "Genauso wie Flächen da sind bei dem Wesen, das ich vor­her meinte, in welchem sich die Lufthälfte und Wasserhälfte schneiden -da sind die beiden Hälften verschieden -, so sind beim Menschen die Linkshälfte und die Rechtshälfte da, - aber gleich.",
        "In Wahrheit ist auch der Mensch ein Flächenwesen, eine Ebene, und das schon ist Maja, daß er seine wirkliche Gestalt hat."
      ],
      [
        "Aber woher kommt sie denn, die wirkliche Gestalt?",
        "Ja, sehen Sie, sie kommt daher, daß der Mensch mitten darinnensteht in einer Art von Kampf.",
        "Von links her kämpft ein Wesen mit einem Wesen, das von rechts her kämpft.",
        "Würde das geistig wahrgenommen, was an unserer linken Seite ist, so würden wir dieses eine Wesen wahrnehmen wie Licht.",
        "Würde das an unserer rechten Seite Wirkende geistig wahrgenommen, so würden wir das andere Wesen mit andern Eigenschaften wahrneh­men.",
        "Als zweierlei Mensch kommen wir nämlich dadurch zustande, daß von links her kämpft die luziferische Wesenheit, von rechts her die ahrimanische Wesenheit."
      ],
      [
        "Nun denken Sie sich einmal, um sich das genau vorzustellen, von links kämpft die luziferische Wesenheit, staut da auf, was sie aufführt als Befestigungswerk; von rechts kämpft die ahrimanische Wesenheit und staut da auf, was sie aufführt als Befestigungswerk.",
        "Das, was Ihr Linksmensch ist, sind die Befestigungswerke des Luzifer; Ihr Rechts-mensch sind die Befestigungswerke des Ahriman.",
        "Und Sie haben über­haupt nur die Möglichkeit, zwischendrinnen in der Mitte zu sein.",
        "Unsere Lebenskunst besteht darin, daß wir das richtige Gleichgewicht finden."
      ],
      [
        "# Bild s. 119"
      ],
      [
        "Unbewußt tun wir das, wenn wir sinnlich wahrnehmen.",
        "Wenn wir mit dem linken Ohr hören und mit dem rechten Ohr hören, und dann die Impulse zusammenfügen zu einer Wahrnehmung, oder wenn wir mit der linken Hand wahrnehmen und mit der rechten Hand wahrnehmen und die Wahrnehmungen zusammenfügen, so setzen wir uns immer in die Fläche, die gerade an der Grenze des Kampfes zwischen Luzifer und Ahriman liegt.",
        "Wie des Messers Schneide, ja noch schärfer als des Mes­sers Schneide ist der Spielraum, der uns in der Mitte gelassen ist.",
        "Unser Organismus gehört nicht uns) sondern er ist aufgeworfen durch den Kampf der luziferischen und ahrimanischen Mächte, aber auch der­jenigen Mächte, die gleichartig sind mit Luzifer und Ahriman.",
        "Das aber ist etwas, was jetzt nicht weiter berührt werden soll."
      ],
      [
        "So sind wir als Flächenwesen eingeschaltet zwischen etwas, was uns als Menschen gar nichts angeht.",
        "Unser linker Mensch geht uns eigentlich gar nichts an, unser rechter Mensch auch nicht, sondern der Prozeß, der Vorgang, der sich zwischen beiden abspielt."
      ],
      [
        "Und jetzt können Sie sich das Bild, das ich vorhin gebrauchte, weiter ausdenken.",
        "Nicht wahr, da geschehen fortwährend Prozesse, Vorgänge.",
        "Ja, in der Erde geschehen auch fortwährend Prozesse, Vorgänge.",
        "Aber das, was in der Erde vor sich geht, macht nicht diese Spuren.",
        "Was in Ihnen geschieht, in der linken oder rechten Hälfte des Organismus, das hat gar nichts zu tun mit dem, was der Mensch seelisch erlebt; das sind"
      ],
      [
        "Prozesse, die sich zwischen Luzifer und Ahriman abspielen.",
        "Die Pro­zesse, die unten, unter der Erdoberfläche sind, alles, was da geschieht, meinetwegen sagen wir das Herumkriechen der Würmer, das Kalt- und Warmwerden in den Jahreszeiten, all diese Prozesse, die nichts zu tun haben mit diesen Spuren, die da eingedrückt werden, müssen Sie ver­gleichen mit dem, was drinnen vorgeht in der Menschenorganisation."
      ],
      [
        "So daß man sagen muß: Durch die geistige Beobachtung der physiolo­gischen und anatomischen Vorgänge muß man darauf kommen, wie Luzifer und Ahriman miteinander kämpfen, muß sich aber nicht der Meinung hingeben, daß durch diese Prozesse zwischen Luzifer und Ahriman das seelische Leben bewirkt wird.",
        "Das ist nicht richtig, denn das verläuft in der Seele selber."
      ],
      [
        "Und das verläuft im Grunde genommen in der Fläche, in der Ebene, nicht in dem Organismus darinnen, in dem räumlichen Organismus; es stuft sich ab, und die Betrachtung dieser Abstufung ist außerordentlich interessant.",
        "In bezug auf den Kopf des Menschen, da ist es so, daß Luzifer und Ahriman ziemlich gleiche Be­festigungswerke links und rechts aufgeworfen haben."
      ],
      [
        "Die linke und rechte Kopfhälfte sind sehr ähnlich, da sind die Kräfte so, daß sie wenig ineinanderspielen können, daß sie die Fläche in der Mitte wenig berüh­ren.",
        "In der Mitte ist die Fläche, links Luzifer, rechts Ahriman; aber weil linke und rechte Kopfhälfte so ähnlich gebildet sind, prallen sie an­einander ab: Luzifer und Ahriman, und der Mensch kann in der Mitte hier eine ruhige Tätigkeit entwickeln (siehe Zeichnung Seite 121)."
      ],
      [
        "Sein Denken wird recht wenig gestört durch den Einfluß von Luzifer und Ahriman, weil sie da aneinander abprallen."
      ],
      [
        "Kommt man weiter nach unten, ist es schon nicht mehr so.",
        "Auf der einen Seite gelingt es Luzifer, den Magen aufzutürmen, auf der andern Seite gelingt es Ahriman, die Leber aufzutürmen.",
        "Und der Magen ist das Mittel, durch das Luzifer kämpft von links nach rechts, die Leber ist etwas, durch das Ahriman kämpft von rechts nach links.",
        "Das Verhältnis von Magen und Leber betrachtet man in der richtigen Weise, wenn man ins Auge faßt, daß es Luzifer gelingt, links den Magen aufzutürmen als eine Art Kampfmittel, und daß es rechts Ahriman gelingt, die Leber aufzutürmen.",
        "Das steht in einem fortwährenden Kampf, und die Wis­senschaft würde gut tun, diesen Kampf zwischen Magen und Leber"
      ],
      [
        "# Bild s. 121"
      ],
      [
        "wirklich zu studieren.",
        "Und wenn die Lage des Herzens einmal ein wenig nach der linken Seite herüber tendiert, so ist diese Lage ein Ausdruck für das, wie auf der einen Seite Luzifer etwas für sich erhaschen will, während auf der andern Seite Ahriman etwas erhaschen will.",
        "Das ganze Links-Rechtsverhältnis ist ein Ausdruck für dasjenige, in welchem sich Luzifer und Ahriman im Menschen bekämpfen, nur daß beim Men­schen, wie gesagt, das, was auf beiden Seiten der Fläche liegt, in gewisser Beziehung gleich ist.",
        "Aber wir sehen ja, eigentlich gleich ist es nur da oben; es hört auf, gleich zu sein, je weiter wir den Menschen nach unten verfolgen."
      ],
      [
        "Bei dem Wesen, von dem ich gesprochen habe, daß es wie drei Fang­arme - Lemminkäinen, Ilmarinen und Wäinämöinen - vorstreckt, ist es so, da ist die eine Hälfte Luft, die andere Wasser; da sind sie noch verschieden.",
        "Sobald man nun zur hellsichtigen Erkenntnis kommt, fällt einem aber gleich auf, daß der Mensch im Grunde genommen auch nur eine Fläche ist zwischen zwei Hälften, denn sobald man sich absugge­riert den physischen Leib und auf den Ätherleib hinblickt, findet man, daß die linke Hälfte wesentlich heller wird als die rechte Hälfte.",
        "Die linke Hälfte sieht sich an viel mehr durchhellt, durchstrahlt, durch-glitzert, durchglimmert; die rechte Hälfte viel mehr durchfinstert, durchdunkelt.",
        "So ist es mit Bezug auf den Links-Rechtsmenschen."
      ],
      [
        "Nun ist aber der Mensch auch in bezug auf andere Richtungen hin­eingestellt in den Raum, das heißt aber - okkultistisch ausgedrückt -nichts anderes als hineingestellt in den Kampf zwischen Luzifer und Ahriman.",
        "So ist er hineingestellt in das Vorne und Hinten, Vorne und Rückwärts."
      ],
      [
        "Wenn Sie sich nun nicht das Links und Rechts denken, sondern das Vorne und Rückwärts am Menschen - den ganzen Menschen müssen Sie sich denken -, dann ist der Mensch auch nicht in der Richtung von vorne nach hinten dieses Raumeswesen (siehe Zeichnung), sondern gerade so, wie von links herüber und von rechts herüber Luzifer und Ahriman sich bekämpfen, und das Räumliche nur die Barrikaden sind, die sie auf­gerichtet haben gegeneinander, kämpft auch von rückwärts Ahriman wieder gegen den Menschen und von vorne wiederum Luzifer.",
        "Von rückwärts schiebt sozusagen seine Tätigkeit Ahriman vor; von vorne schiebt seine Tätigkeit Luzifer dem Ahriman entgegen.",
        "Und der Mensch steht wieder mitten darinnen."
      ],
      [
        "# Bild s. 122"
      ],
      [
        "Allerdings kommen wir jetzt dazu, ausführen zu müssen, daß es in bezug auf diese Richtung vorne-rückwärts den beiden nicht so gelungen ist, ich möchte sagen, so nahe aneinander heranzukommen, daß sie nur eine Fläche bildeten.",
        "Hier ist es schon anders.",
        "Ahriman kommt nämlich"
      ],
      [
        "nur bis zu einer Fläche, die Sie sich durch das Rückgrat legen können, und Luzifer kommt bis zu einer Fläche, die Sie sich durch das Brustbein legen können, etwa da, wo die Rippen zusammenstoßen.",
        "Und da­zwischen ist ein Raum, durch den sie getrennt sind, wo ihre Wirkungen durcheinandergehen.",
        "Sie kämpfen da, man möchte sagen, nicht un­mittelbar aneinander stoßend, sondern sie senden ihre Geschosse durch diesen Raum hindurch.",
        "Aber Ahriman kommt nur bis zum Rückgrat und Luzifer nur bis dahin, wo die Rippen an das Brustbein anstoßen.",
        "Und wir stehen da drinnen, zwischen diesem Kampf von Luzifer und Ahriman.",
        "Also in bezug auf die Vorwärts- und Rückwärts richtung sind wir in der Tat ein solches Wesen, welches Raum hat.",
        "In bezug auf links und rechts haben wir keinen Raum."
      ],
      [
        "# Bild s. 123"
      ],
      [
        "In der Richtung links-rechts kämpfen Luzifer und Ahriman vor­zugsweise durch die Gedanken.",
        "Da schwirren die Gedanken von links und von rechts herüber und berühren sich in dieser Fläche.",
        "Es sind kos­mische Gedankenbildungen, die da aneinanderstoßen und sich in der menschlichen Mittelfläche berühren.",
        "Vorne und rückwärts kämpfen"
      ],
      [
        "Luzifer und Ahriman mehr mit Gefühlen, da wird der Kampf mehr durch die Gefühle geführt.",
        "Und weil hier die Kräfte nicht so recht an­einanderkommen, bleibt für uns in der Mitte ein Spielraum, in welchem wir mit unseren Gefühlen in uns selber sind.",
        "Wir spüren, wenn wir Ge­danken haben, die von links und rechts einander bekämpfen, daß diese Gedanken eigentlich der Welt angehören.",
        "Mit den Gedanken denken wir die Dinge, die draußen sind.Wenn wir uns eigene Gedanken machen, so sind das Phantasmagorien, dann gehören sie eigentlich nicht mehr der Welt an.",
        "In unseren Gefühlen gehören wir uns selber an, weil Luzi­fer und Ahriman da nicht ganz aneinanderstoßen, weil wir da Spiel­raum haben zwischen den beiden Gebieten.",
        "Deshalb sind wir mit un­seren Gefühlen so in uns selber."
      ],
      [
        "Sehen Sie, wir sind als Menschen Geschöpfe durch die Wirkungs­weise der Wesen der höheren Hierarchien.",
        "Und wir sind dieses Flä­chenwesen links und rechts dadurch, daß die höheren Hierarchien uns Menschen da hineinstellen als Flächenwesen.",
        "Da lassen sie Luzifer und Ahriman nicht zusammenkommen.",
        "Wir sind insofern ein Wesen der guten Götter, als diese guten Götter aus ihren Schöpfungsgedan­ken heraus gesagt haben: Da liegt vor uns ein Kampf zwischen Luzifer und Ahriman.",
        "Nun müssen wir eine Grenze aufrichten für ein Gebiet, in das sie nicht hineinkommen, daß sie nicht unmittelbar aneinander herankönnen. - Wir Menschen sind hineingestellt in diesen Kampf als Geschöpfe der guten Götter, und je mehr wir uns bewähren in diesem Kampf, desto mehr sind wir Geschöpfe der guten Götter."
      ],
      [
        "In bezug auf das Vorne und Rückwärts ist es so, daß die guten Götter Luzifer nicht ganz in uns hineinlassen.",
        "Da haben sie in dem Rippenabschluß nach vorne ihm Barrikaden aufgerichtet.",
        "Und in der Ausbildung dieses wunderbaren Turmes, der das Rückenmark und das Gehirn umschließt, haben die guten Götter ein Befestigungswerk gegen Ahriman aufgerichtet.",
        "Das kann er nicht passieren, da kann er höch­stens seine Gefühlsgeschosse hinüberschicken zu Luzifer.",
        "Da stehen wir wirklich darinnen, um die beiden voneinander zu trennen durch einen Spielraum."
      ],
      [
        "Es gibt noch eine dritte Richtung, das ist die von oben nach unten.",
        "Da müssen wir uns klar sein darüber, daß die Sache sich auch nicht"
      ],
      [
        "so verhält, wie sie in der äußeren Phantasmagorie, der Maja aussieht.",
        "Da ist es so, daß von unten herauf Ahriman spielt, von oben herunter Luzifer.",
        "Und auch da haben die guten, fortschreitenden Götterwesen eine Barriere errichtet gegenüber Luzifer.",
        "Seine Wirkungen von oben nach unten werden sozusagen aufgehalten durch eine Fläche.",
        "Sie be­kommen diese Fläche, wenn Sie ein Skelett nehmen und den Schädel herunternehmen.",
        "Da, wo der Schädel auf den Halswirbeln aufsitzt, müssen Sie sich eine Fläche denken.",
        "Diese unsichtbare horizontale Fläche, wo der Schädel aufsitzt auf dem Halswirbel, ist die Barriere.",
        "Wenn ein Mensch sich da hineinstellt, kann er die von oben nach un­ten gehenden luziferischen Wirkungen aufhalten.",
        "Luzifer kann nur von oben seine Geschosse hineinschicken; und das sind jetzt Willens­geschosse.",
        "Von links nach rechts Gedankengeschosse, von vorne nach rückwärts Gefühlsgeschosse, von oben nach unten und von unten nach oben gehen die Willensgeschosse."
      ],
      [
        "# Bild s. 125"
      ],
      [
        "Aber auch hier ist ein Spielraum.",
        "Wenn Sie unten das Zwerchfell nehmen, so haben Sie ungefähr dem Zwerchfell entlang gehend die Fläche, die wieder aufgerichtet ist gegen den von unten nach oben"
      ],
      [
        "drängenden Ahriman.",
        "Also mit seinem Wollen, mit seinen Willens­geschossen, mit seinem eigenen Wesen kann Ahriman nur von unten nach oben bis zum Zwerchfell gelangen.",
        "Weiter kann er nie mit seinen Geschossen wirken.",
        "Das ist unser eigener Spielraum, was darüber ist."
      ],
      [
        "Nun sehen Sie, wie kompliziert eigentlich der Mensch ist.",
        "Nehmen Sie irgendein Stück der Menschennatur, ich will sagen, die linke Seite des Antlitzes.",
        "Als Gedankenwesen kann Luzifer diese linke Seite ganz durchdringen, auch noch als Gefühlswesen kann er sie in gewisser Weise durchdringen bis zu einer gewissen Fläche; als Willenswesen kann er sie wiederum durchdringen von oben nach unten.",
        "So können Sie von jeder Partie des Menschen durch diese Angaben herausfinden, wie Lu­zifer und Ahriman durch kosmische Gedanken-, Gefühls- oder Wil­lensimpulse in dem Raumesmenschen darinnen wirken."
      ],
      [
        "Aber klar muß man sich darüber sein, daß wir als Gedankenmensch eigentlich ein Flächenwesen sind.",
        "Als Gefühlsmensch haben wir einen gewissen Spielraum zwischen vorn und rückwärts, als Willensmensch haben wir einen gewissen Spielraum zwischen oben und unten, zwischen dieser Fläche hier - durch den oberen Halswirbel - und der Fläche des Zwerchfells.",
        "Und nur wenn Sie sich dasjenige aussondern, was gar nicht zum Menschen gehört, dann bekommen Sie die wahre Gestalt des Men­schen.",
        "Die können Sie sich nun konstruieren."
      ],
      [
        "Aber Sie sehen, daß der Mensch in Wirklichkeit von außen her zu­sammengefügt ist, daß er von außen her sein Gepräge erhält, und daß wir ihn nicht verstehen, wenn wir einfach die Formen so nehmen, wie sie uns entgegentreten, sondern daß wir ihn erst dann verstehen, wenn wir wissen, wie er mit dem ganzen Geistig-Kosmischen zusammen­hängt, wie da von rechts und links, von unten und oben, von vorne und rückwärts die luziferisch-ahrimanischen Kräfte an den Menschen herankommen und wie sie so sein Wesen als Raumeswesen prägen."
      ],
      [
        "Sehen Sie, so müssen Sie auch dasjenige betrachten, was in gewisser Weise nachgebildet ist dem wahren kosmischen Wirken in der Welt, so müssen Sie unseren Bau betrachten.",
        "Wenn wir ihn als Phantas­magorie betrachten, so könnten wir zunächst glauben, daß das Haupt­sächlichste an diesem Bau dasjenige ist, was da von Holz ausgefüllt ist im Raum.",
        "Das ist aber nicht die Hauptsache, sondern die Hauptsache"
      ],
      [
        "ist das, wo scheinbar nichts ist.",
        "Wenn irgendeine Form in un­serem Bau so geht (siehe Zeichnung) und da ist das Holz, so ist das"
      ],
      [
        "# Bild s. 127"
      ],
      [
        "Wesentliche nicht dieses hier, das Holz, sondern dasjenige, wo nichts ist, wo die Luft angrenzt.",
        "Und unseren richtigen Bau würden Sie be­kommen, wenn Sie einen riesigen Wachsklumpen nehmen würden und einen Abdruck machten von dem Inneren, und würden dann den Ab­druck anschauen.",
        "Also dasjenige, in dem Sie, wenn Sie in den Bau hin­eingehen, darinnenstehen, was Sie nicht sehen können, sondern fühlen müssen, das ist es eigentlich, worauf es ankommt.",
        "Ich habe schon frü­her gesagt: Das Prinzip unseres Baues ist das eines Gugelhupftopfes. -Gugelhupftopf ist ein Ausdruck, den man hier nicht gut verstehen wird.",
        "Aber denken Sie sich hier einen Topf: das ist die Form, da drin­nen backt man einen Gugelhupf.",
        "Auf was kommt es denn da an bei diesem Gugelhupftopfe?",
        "Es kommt nicht auf den Topf an, sondern es kommt auf den Kuchen an, daß der eine richtige Form bekommt und in der richtigen Weise drinnen gedeiht.",
        "Der Topf muß nur so sein, daß, wenn man Teig hineingießt und ihn bäckt, der Gugelhupf in der richtigen Weise zustande kommt."
      ],
      [
        "So kommt es bei unserem Bau auch nicht darauf an, was die Um­gebung ist, sondern auf das, was darinnen ist.",
        "Und darinnen werden sein die Gefühle und Gedanken derer, die im Bau darinnen sind.",
        "Die werden dadurch entstehen, daß der Mensch bis an die Grenze des"
      ],
      [
        "Baues sieht, daß er die Formen fühlt, und daß er sich ausfüllt mit Ge­dankenformen.",
        "Das, was darinnen ist, das wird der Gugelhupf sein, und das, was wir bauen, ist die Hülle, die Form.",
        "Aber die muß so sein, daß das Richtige darinnen gedacht, gefühlt und empfunden wird.",
        "Und das ist das Prinzip, sehen Sie, der neueren Kunst gegenüber der alten Kunst.",
        "Bei den alten Künsten kam es immer darauf an, was draußen im Raume ist.",
        "Bei der neuen Kunst kommt es nicht darauf an, was im Raume draußen ist.",
        "Was draußen ist, das ist der Topf, und das, wor­auf es ankommt, das kann man eigentlich gar nicht machen, sondern das ist darinnen.",
        "Das gilt nicht nur in bezug auf plastische Formen, sondern auch in bezug auf Malerei.",
        "Es kommt auch da nicht darauf an, was gemalt wird, sondern was dabei empfunden und erlebt wird.",
        "Auch die Malerei ist bloß «Gugelhupftopf»."
      ],
      [
        "Das ist, möchte ich sagen, der Kernpunkt des Evolutionsfortschrit­tes, in dem wir darinnenstehen, daß wir wirklich - verzeihen Sie den Ausdruck - aus dem Topf in den Kuchen hineinkommen.",
        "Im Topfe bleiben, heißt Materialismus; in den Kuchen hineinkommen, heißt bei uns Spiritualismus, und der ist dasjenige, dem wir entgegenarbeiten.",
        "Wenn man das nicht berücksichtigt, wird man auch alles Künstlerische, um das es sich bei uns handelt, nicht in der richtigen Weise beurteilen können.",
        "Wenn man künstlerisch unseren Bau nach dem Muster des Alten auffaßt, so wird man sagen können: Ja, aber um Gotteswillen, du hast gar keinen schönen Topf gemacht! - Man wird nämlich nicht wissen, daß es auf den Topf nicht ankommt, sondern auf den Gugel­hupf.",
        "Damit nähern wir uns, mit einem solchen künstlerischen Prin­zip, dem ganzen Sinn und der ganzen Bedeutung des Evolutionsfort­schrittes durch die Geisteswissenschaft.",
        "Der Mensch muß sich durch den Fortschritt der Geisteswissenschaft herausarbeiten aus dem Topf und muß sich in den Gugelhupf hineinarbeiten."
      ],
      [
        "Und so muß er von dem Glauben loskommen, daß zum Beispiel in den Gehirnprozessen die Ursachen der Gedanken liegen, während in den Eigenprozessen des Gehirns kosmische Vorgänge liegen, und die Kämpfe zwischen Luzifer und Ahriman sich abspielen.",
        "Und er muß einsehen, daß die menschlichen Seelenvorgänge, die Gedanken und Empfindungen nur die Spuren sind, die in diese Kampfverschanzungen"
      ],
      [
        "eingegraben werden, die aber mit den sogenannten materiellen Vorgängen - mit andern Worten mit den luziferisch-ahrimanischen Vorgängen - nichts zu tun haben."
      ],
      [
        "Ich möchte noch ein anderes Bild gebrauchen.",
        "Nehmen wir an, wir kommen in einen schönen Garten, schön dadurch, daß die Anordnung der Bäume schön ist, die Arrangements in bezug auf die Blumenver­teilung schön sind und so weiter, und wir wollen uns eine Ansicht dar­über bilden.",
        "Da käme, wenn wir durch ein Loch in die Erde hinein­blicken könnten, so ein Kobold an uns heran.",
        "Dieser Kobold - nehmen wir an - sagte uns nun: Ich will dir sagen, warum da Rosen, Veil­chen, warum da ein Busch und da Blumen sind.",
        "Ich krieche nämlich da unten unter der Erdoberfläche überall herum, und da sehe ich den Grund, der die Bäume, Veilchen, Rosen hat hervorsprießen lassen. -Wir können sagen: Ja, du erzählst uns ganz schön diese Vorgänge.",
        "Das, was du da erzählst, muß alles geschehen können in der physischen Welt.",
        "Aber damit die Pflanzen gedeihen können, der Garten entstan­den ist, mußte ein Gärtner da sein.",
        "Das aber sind Regionen, in die du gar nicht hineingeschaut hast, um die du dich gar nicht gekümmert hast."
      ],
      [
        "So müssen wir lernen, zu den materialistischen Anatomen, den ma­terialistischen Physiologen zu sagen: Deine Tätigkeit finde ich erst, wenn ich durch das Guckloch in die Erde schaue.",
        "Da kriechst du her­um und studierst Vorgänge, die geschehen müssen, die aber nichts zu tun haben mit dem, was da oben an Seelisch-Geistigem vorgeht.",
        "Und du wirst das, was da unten vorgeht, erst richtig deuten, wenn du dich darauf einläßt, zu erkennen, welche Beziehungen herrschen zwischen Luzifer und Ahriman und den andern Hierarchien, welche Luzifer und Ahriman wieder in den Gleichgewichtszustand bringen. - Und es wird sich dasjenige, was bisher gewissermaßen nur wie in der Ich-Vor­stellung gewirkt hat, bereichern durch die Geisteswissenschaft."
      ],
      [
        "Es wird eine Zeit kommen, da werden sich die Menschen sagen:"
      ],
      [
        "Uns wird mitgeteilt in der biblischen Schöpfungsurkunde von dem Hauche, von dem Ateinzuge des Jahve, der eingehaucht wurde dem Menschen. - Dann werden die Menschen der Zukunft fragen: Ja, wenn dieser Atemzug eingehaucht wird, wohin wird er denn eingehaucht? -"
      ],
      [
        "Wenn Sie zusammenhalten, was ich gesagt habe, so werden Sie finden, daß das nächste, wohin gehaucht wurde, diese Zwischenräume sind, wo sich von vorne und rückwärts, von oben und unten gleichsam als einen Kubus Jahve den Menschen schafft (siehe Zeichnung) und ihn so ausfüllt mit seinem eigenen Wesen, mit seinem Zauberhauche, daß dann im übrigen Menschen sich nun ausbreitet die Wirkung dieses Zauberhauches in die Regionen von Luzifer und Ahriman.",
        "Aber hier ist ein Zwischenraum, begrenzt von rechts und links, von oben und unten, von vorne und rückwärts, wo hinein unmittelbar als in den Raumesmenschen Jahves Hauch geht.",
        "Was ich gesagt habe, ist zu­nächst in bezug auf diesen physischen Raumesmenschen gesagt."
      ],
      [
        "# Bild s. 130"
      ],
      [
        "Sie sehen, dies macht uns die Aussicht frei, von der aus wir er­blicken den Menschen darinnenstehend im ganzen Kosmos.",
        "Ich möchte sagen: In bezug auf dasjenige, was er scheinbar äußerlich räumlich ausfüllt, dieser Mensch, von alledem gibt es auch moralisch-seelische Aspekte.",
        "Denn auch in dem, was als Moralisch-Seelisches in uns wirkt, haben wir zunächst, wenn auch nicht in so starkem Grade wie in dem Raumesmenschen, eine Phantasmagorie Und in allem Moralischen, in allem Logischen, in allem, was in unserer Seelentätigkeit ist, wirken Luzifer und Ahriman aufeinander, und der Mensch ist aufgestellt an der Grenze."
      ],
      [
        "Wie das ist, dieses für uns ganz besonders bedeutungsvolle und wich­tige Kapitel wollen wir dann morgen besprechen."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SECHSTER VORTRAG Dornach, 22. November 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Aus den gestrigen Auseinandersetzungen werden Sie haben entnehmen können, daß selbst unsere Leibesform dadurch so ist, wie sie ist, daß sie gleichsam ein Ergebnis des Zusammenwirkens der luziferischen und ahrimanischen Mächte darstellt.",
      "Es ist gerade für unsere Zeit sehr wichtig, dieses Zusammenwirken der luziferischen und ahrimanischen Mächte wirklich zu kennen, denn erst dadurch wird allmählich in die Menschheit ein Verständnis für die Kräfte einziehen können, die hinter der äußeren Phantasmagorie des Daseins wirken. Wir wissen, daß wir weder Ahriman zu hassen noch uns vor Luzifer zu fürchten brauchen, weil diese Mächte nur so lange gewissermaßen feindliche Mächte in der Welt sind, als sie nicht in ihren eigenen Gebieten wirken. Davon ist ja voriges Jahr in Mün­chen viel gesprochen worden. Darüber sind auch schon hier Andeu­tungen gemacht worden.",
      "Indem wir nun gestern gesehen haben, wie der physische, räum­liche Menschenleib in seiner Form zustande kommt durch das Widerspiel der luziferischen und ahrimanischen Mächte, haben wir auf das Äußerlichste im Menschenleben hingewiesen, in dem Luzifer und Ahri­man ihre Rolle spielen. Sie wissen, wir kommen etwas mehr in das In­nere des Menschenlebens, wenn wir vom physischen Leibe fortschrei­ten zum ätherischen Leibe. Der Atherleib ist gewissermaßen der Bildner des physischen Leibes. Er ist eingebettet in die ganze ätherische Welt, er liegt als ein beweglicher, als ein immer in sich beweglicher ätherischer Organismus unserem physischen Organismus zugrunde. Nun ist in bezug auf den ätherischen Leib zu sagen, daß auch in ihm, geradeso wie wir das für den physischen Leib gesehen haben, luziferische und ahrimanische Mächte wirksam sind, daß der Mensch auch als äthe­risches Wesen hineingestellt ist - das müssen wir betonen - in das Wi­derspiel der luziferischen und ahrimanischen Kräfte.",
      "Um nun auf dasjenige hinzuweisen, auf welches es dabei ankommt, wollen wir einmal einen Blick auf die drei Grundtätigkeiten des menschlichen",
      "Wesens werfen, insofern der Mensch nicht ein physisches Wesen ist, auf das Wollen, Fühlen und Denken. Dieses Wollen, Fühlen und Denken sehen wir natürlich nicht, wenn wir den Menschen in bezug auf seinen physischen Leib ansehen. Nur insofern der physische Leib seinen Ausdruck hat in einer gewissen Physiognomie, in Gesten und dergleichen, können wir durch den physischen Leib hindurch ahnen, was im menschlichen Inneren ist. Der Ätherleib aber ist schon als ein in sich beweglicher Organismus ein immerwährender Ausdruck des Denkens, Fühlens und Wollens des Menschen.",
      "In bezug auf dieses Denken, Fühlen und Wollen hat es wieder die rein äußere Wissenschaft etwas schwierig, und wenn man die philo­sophischen Weltanschauungen durchgeht, wird man sehen, daß bald der eine Philosoph das Wollen voranstellt und bald ein anderer das Denken. Auch solche gibt es, welche das Fühlen als die hauptsächlichste Kraft betrachten.",
      "Aber wie eigentlich dieses Denken, Fühlen und Wollen im Menschen eine Einheit bildet, darüber können sich diese philosophischen Weltanschauungen keinen rechten Begriff bilden. Die­ses Sich keinen rechten Begriff bilden Können über das Verhältnis von Denken, Fühlen und Wollen in dem menschlichen Seelenleben ist ge­rade so, als wenn der Mensch Schwierigkeiten empfinden würde, in dem Auseinandersetzen mit dem Begriffe des Menschen überhaupt zu­rechtzukommen.",
      "Ich weiß nicht recht - sagen die Philosophen -, ist die menschliche Seele mehr willensartiger, mehr gefühlsartiger oder mehr denkerischer Natur? Ist sie mehr das eine oder das andere? - Das ist gerade so, wie wenn jemand sagen wollte: Nun weiß ich wirklich nicht mehr recht, was ein Mensch ist.",
      "Da hat mir eben einer gesagt, er wolle mir einen Menschen bringen, und da bringt er mir ein kleines Wesen, ein fünfjähriges Kind, und sagt: Das ist ein Mensch. - Dann ist ein anderer gekommen und sagte auch, er wolle mir einen Menschen zeigen und da hat er mir ein Wesen gebracht, das viel größer ist als das erste, also ein Wesen in den mittleren Menschenjahren. Ein dritter ist endlich gekommen und hat mir auch gesagt, er wolle mir ein Men­schenwesen zeigen.",
      "Er zeigte mir ein ganz anderes Wesen, das runzelig im Gesichte war, graue Haare hatte und so weiter. Und jetzt weiß ich wirklich nicht mehr, was ein Mensch ist. Drei verschiedene Wesen hat",
      "man mir gezeigt! - Ja, alle drei, nicht wahr, sind Menschen. Nur ist der eine ganz jung, der andere ist etwas älter, und der dritte ist schon ganz alt geworden. Sie sind sehr verschieden in ihrer Erscheinung. Aber so­bald man die drei Alter zusammenhält, weiß man, was ein Mensch ist.",
      "So ist es aber auch mit dem Wollen, Fühlen und Denken. Der Unterschied ist nur der, daß das Wollen wohl dieselbe Seelentätigkeit ist wie das Denken, nur ganz jung noch, kindlich. Und wenn das Wollen älter wird, dann wird es Fühlen, und das ganz alte Wollen ist das Denken. Es ist nur ein Unterschied im Alter beim Wollen, Fühlen und Denken, nur daß sie in unserer Seele zusammenleben, die Lebens­alter für diese Seelentätigkeiten, das macht die Sache schwierig. Aber wir haben schon auseinandergesetzt - Sie brauchen es nur nachzulesen in meinem Buche «Die Schwelle der geistigen Welt» -, daß, sobald wir aus der physischen Welt hinauskommen, das Gesetz der Verwandlung gilt, nicht das der Starrheit. Da verwandelt sich alles. Das Alte wird plötzlich jung, das Junge wird alt und so weiter. So daß wirklich gleichzeitig in uns auftreten können die drei Seelentätigkeiten: das Wollen, das sich bald als junges Wollen zeigt, bald als älteres Wollen, das heißt als Fühlen, und auch als ältestes Wollen, als ganz altes Wol­len, das heißt als Denken. Da gehen die Lebensalter durcheinander, es wird dann alles flüssig. So ist es im Ätherleib des Menschen.",
      "Aber diese Verwandlung kann nicht so ohne weiteres durch sich selbst zustande kommen. Dasjenige, was einheitliche Seelentätigkeit wäre, das kommt uns überhaupt im gewöhnlichen Leben nicht zum Bewußtsein, das können wir gar nicht ins Bewußtsein hereinbringen. Wenn wir - weil ja das Ganze im Ätherleib beobachtet werden muß, und der Ätherleib etwas Bewegliches, Flüssiges ist - den Ätherleib wie einen fortlaufenden Strom symbolisch zeichnen, so kommt uns dieser Strom der Seelentätigkeit im gewöhnlichen Leben überhaupt nicht zum Bewußtsein, sondern in diesen Strom, in dieses fortwährende Bewegen des Ätherleibes, das mit der Zeit fortfließt, gliedert sich hinein einmal luziferische und dann wieder ahrimanische Tätigkeit.",
      "Die luziferische Tätigkeit macht das Wollen jung. Unsere Seelen-tätigkeit, durchzogen von Luziferischem, ist Wollen. Wenn das Luzi­ferische in unserer Seelentätigkeit überwiegt, wenn in unserer Seele nur",
      "Luzifer seine Kräfte geltend macht, so ist das Wollen. Luzifer wirkt ver­jüngend auf den Gesamtstrom unserer Seelentätigkeit. Wenn Ahriman dagegen hauptsächlich seine Wirkungen äußert in unserer Seelentätig­keit, dann verhärtet er unsere Seelentätigkeit, sie wird alt, und das ist das Denken. Dieses Denken, dieses Gedankenhaben ist gar nicht mög­lich im gewöhnlichen Leben, ohne daß in dem ätherischen Leibe Ahri­man seine Kräfte entfaltet. Man kann im Seelenleben, insofern es sich im Ätherleibe äußert, nicht ohne Ahriman und Luzifer auskommen.",
      "# Bild s. 134",
      "Würde Luzifer sich ganz zurückziehen von unserem ätherischen Leibe, dann würden wir kein luziferisches Feuer haben zum Wollen. Würde Ahriman sich ganz zurückziehen von unserem Seelenleben, dann wür­den wir niemals die Kühle des Denkens entwickeln können. In der Mitte von beiden ist eine Region, wo sie miteinander kämpfen. Hier durchdringen sie sich, Luzifer und Ahriman, hier spielen ihre Tätig­keiten ineinander. Das ist die Region des Fühlens. In der Tat, so er­scheint der menschliche Ätherleib, daß man darinnen wahrnehmen kann das luziferische Licht und die ahrimanische Härte. Wenn man",
      "den menschlichen Ätherleib überblickt, so ist das natürlich nicht so an-geordnet, wie hier (auf der Zeichnung) symbolisch, sondern da ist ein Durcheinander. Da sind Einschiebsel, in denen der Ätherleib undurch­sichtig erscheint, so, wie wenn er, ich möchte sagen, Eiseinschläge hätte. Figuren treten im Ätherleibe auf, die man vergleichen kann mit Eis­figuren, wie sie auf Fensterscheiben erscheinen. Das sind die Verhär­tungen in dem Ätherleibe. An solchen Stellen wird er undurchsichtig. Das sind aber die Auslebungen des Gedankenlebens im Ätherleibe. Die­ses Gefrieren des Ätherleibes an gewissen Stellen rührt von Ahriman her, der seine Kräfte da hineinschickt durch das Denken.",
      "# Bild s. 135",
      "An andern Stellen des Ätherleibes ist es so, als wenn er Vakuolen, ganz lichte Stellen in sich hätte, die durchsichtig sind, die glänzend, lichtglitzernd sind. Da sendet Luzifer seine Strahlen, seine Kräfte hin­ein, das sind die Willenszentren im Ätherleibe. Und in dem, was da­zwischen liegt, wo gleichsam fortwährende Tätigkeit ist im Ätherleibe, ist es so, daß man sieht, hier ist eine harte Stelle, aber nun wird sie so­gleich von einer solchen Lichtstelle gefaßt und aufgelöst. Ein fort­währendes Festwerden und Wiederauflösen. Das ist der Ausdruck der Gefühlstätigkeit im Ätherleibe.",
      "So können wir sagen: Nicht nur die Form des physischen Leibes ist durch das Ineinanderspielen der das Gleichgewicht störenden oder bewirkenden luziferischen und ahrimanischen Kräfte hervorgerufen, sondern auch im ganzen Ätherleibe spielen luziferische und ahrima­nische Kräfte. Wenn die ahrimanischen Kräfte die Überhand haben, so ist das ein Ausdruck des Denkens, wenn die luziferischen Kräfte die Überhand haben, so ist das ein Ausdruck des Wollens, und wenn sie sich gegenseitig raufen, könnte man sagen, so ist das ein Ausdruck des Fühlens.",
      "Da haben wir die Art, wie im Ätherleibe luziferische und ahrima­nische Kräfte ineinanderspielen. Wir sind gewissermaßen ganz das Er­gebnis von solchen Kräften, und sind eigentlich in der Zwischenlage zwischen solchen Kräften darinnen.",
      "Nun müssen wir uns darüber klar sein, daß wir in dem, was da spielt, nicht mit unserem vollen Ich immer darinnen sind. Unser Ich, unser irdisches Ich, das wir uns erst im Laufe der Erdenentwickelung erworben haben, kann seine volle Tätigkeit und sein volles Bewußtsein zunächst nur im physischen Leibe entfalten. Im Ätherleibe wird es sich erst während der Jupiterzeit voll entfalten können, so daß in alledem, was im Ätherleibe spielt, das eigentliche Ich des Menschen nicht un­mittelbar tätig ist. Würde zu der fortschreitenden Weltevolution nichts hinzugekommen sein von ahrimanischen und luziferischen Kräften, dann würde der Mensch ein ganz anderes Wesen sein, dann würde der Mensch in seinem physischen Leibe Wahrnehmungen haben können, aber er würde nicht eigentlich Gedanken haben können. Gedanken hat er dadurch, daß auf seinen Ätherleib Ahriman Einfluß gewinnen kann. Willensimpulse hat er dadurch, daß auf seinen Ätherleib luzi­ferische Kräfte Einfluß gewinnen können. Diese Kräfte müssen also da sein.",
      "Wir müssen uns also klar darüber sein, daß wir für unser irdisches Bewußtsein nicht voll hinunter können in den Ätherleib. Wir können nur im physischen Leibe unser volles Ich-Bewußtsein ausleben. In den Ätherleib können wir nicht vollständig hinunter. Mit diesem Äther-leib tauchen wir daher unter in eine Welt, worin wir selbst nicht voll­ständig sind. Und mit Ahriman, der gedankenbildend in unseren Ätherleib",
      "eintritt, treten nicht nur unsere Gedanken in unseren Ätherleib ein. Mit Luzifer, der willensbildend in unserem Ätherleib ist, treten nicht nur unsere Willensimpulse in unseren Ätherleib ein. Und so ist es auch mit den Gefühlen, dem Gebiet, wo sich die beiden raufen. In­sofern nun Ahriman in unserem Ätherleibe lebt, tauchen wir mit dem Ätherleibe unter in die Sphäre der Naturgeister, der elementarischen Naturgeister, der Erd-, Wasser-, Luft- und Feuergeister. Wir wissen das nur nicht, weil wir mit unserem Ich nicht voll in unseren Äther-leib hinunter können. Aber es ist immer so, daß in diesem Ätherleibe nicht nur dasjenige als Gedankenmacht lebt, was wir selbst denken, sondern da dringen auch die Einflüsse der Naturgeister ein. Insbeson­dere jedesmal wenn der Mensch diesen Naturgeistern gegenübertritt, weiß er zu erzählen davon, daß er etwas erlebt hat, was er im gewöhn­lichen Ich-Bewußtsein nicht erlebt hat, und zwar tritt er diesen Natur-geistern dann gegenüber, wenn irgend etwas Abnormes bei ihm eintritt, wenn der Ätherleib gleichsam etwas losgerissen wird aus dem physi­schen Leibe.",
      "Wodurch kann so etwas geschehen? Sehen Sie, der Ätherleib des Menschen steht in Verbindung mit der ganzen umliegenden ätherischen Welt, also auch mit der ganzen Sphäre der Naturgeister um uns herum. Nehmen wir nun einmal an, um ein Beispiel anzuführen, ein Mensch ginge bei Tage auf der Straße. Wenn er mit seinem gewöhnlichen Bewußtsein auf der Straße geht, dann ist sein Ätherleib richtig in seinem physischen Leibe darinnen, und er nimmt mit seinem Ich-Bewußtsein wahr, was man eben mit dem Ich-Bewußtsein wahr­nehmen kann.",
      "Nehmen wir aber einmal an, er geht in der Nacht über einen Weg. Wenn man nachts über einen Weg geht, so ist es gewöhnlich finster, was ja bei manchem Menschen schon grauselig-gruselige Zustände be­wirkt. Dadurch nun, daß er in einen solchen grauselig-gruseligen Zu­stand kommt, lockert sich durch diese eigentümlichen Empfindungen, die da kommen, in denen Luzifer ihn besonders ergreift, der ätherische Leib aus dem physischen Leib heraus, und dadurch kann jetzt dieser befreite ätherische Leib, der sich herausgelöst hat aus dem physischen Leib, in Beziehung treten zu der umliegenden ätherischen Welt.",
      "Nehmen wir nun an, der Betreffende komme in die Nähe eines Kirchhofes, wo noch Ätherleiber sind auf den Gräbern eben Verstor­bener. Da kann er vielleicht in diesem Zustand, wenn sich sein Äther­leib herausgelockert hat, irgend etwas von den Gedanken, die noch in den Ätherleibern der Verstorbenen sitzen, wahrnehmen. Nehmen wir an, es sei jemand verstorben vor kurzer Zeit, der habe Schulden hinter­lassen und sei mit dem Gedanken, Schulden gemacht zu haben, ge­storben. Dieser Gedanke nun kann noch darinnensitzen in dem Äther-leibe des Verstorbenen. Man nimmt selbstverständlich diese Gedanken im Ä therleibe des andern nicht wahr, wenn der eigene Ätherleib nicht gelockert ist, aber in dem Zustande, den ich geschildert habe, kann man es wahrnehmen. Man kann mit dem Ätherleibe des andern in Beziehung treten und kann daher diesen Gedanken: Ich habe Schulden gemacht -wahrnehmen. Und jetzt, weil durch dieses die luziferische Macht in ihm verstärkt wird, regt sich in ihm das Gefühl: Ich muß diesem die Schuld bezahlen.",
      "So ein Mensch erlebt also etwas in seinem ätherischen Leibe, was er niemals im physischen Leibe im normalen Leben erleben würde. Man erlebt so etwas nicht alle Tage im gewöhnlichen Menschenleben, daher bringt es auch etwas sehr Bedeutsames im Bewußtsein hervor, wenn man das erlebt. Es bringt das im Bewußtsein hervor, daß man weiß, jetzt hast du etwas erlebt, das hast du nicht in deinem Leibe erlebt, das kannst du in deinem Leibe nicht erleben. Man fühlt, man ist irgendwo anders als in seinem Leibe, und das empfindet man als eine ungewohnte Lage. Man ist woanders als in seinem Leibe; und man fühlt dann den Drang, in seinen Leib wieder zurückzukehren; man sehnt sich nach Hilfe, um in seinen Leib wieder zurückzukehren.",
      "Solch ein Gefühl, das man da hat, das Gefühl der Sehnsucht, in seinen Leib wieder zurückzukehren, ruft irgendwelche Elementargei­ster, Naturgeister heran, für die das Gefühl des Menschen gleichsam Speise, Nahrung ist. Sie kommen dadurch heran, daß sie gleichsam an­gezogen werden durch das Gefühl: Ich möchte in meinen physischen Leib herein. - Sie verhelfen einem dazu, den Weg zurückzufinden in den physischen Leib. Wenn man in gewöhnlicher Art schläft, findet man den Weg leicht zurück; wenn man aber so etwas erlebt wie das,",
      "was ich geschildert habe, findet man ihn schwer zurück. Aber man nimmt es nicht so wahr, wie man es im physischen Leibe wahrnimmt, sondern man nimmt es imaginativ, in Bildern wahr. Es kommt irgend­einer heran, der eigentlich ein Naturgeist ist, der vielleicht in der Ge­stalt eines Hirten, in der Gestalt eines Schäfers erscheint und der einem den Rat gibt: Gehe hin zu irgendeinem Schlosse. Ich werde dich dahin bringen auf einem Wagen - und dergleichen mehr.",
      "Mit solchen Vorstellungen kann sich noch etwas anderes verknüp­fen. Es kann sich damit verknüpfen, daß einem der Leib, den man ver­lassen hat, außerhalb dessen man das Erlebnis hatte, wie ein verzauber­tes Schlöß erscheint, aus dem man jemanden erlösen muß, wenn man hineinkommt. So imaginiert man diese Sehnsucht nach dem physischen Leibe und das Helfen der Naturgeister. Dann kommt man wieder in den physischen Leib zurück, das heißt, man wacht auf.",
      "Solche Erlebnisse erzählen die Menschen dann, die es in der Realität erlebt haben, weil sie das Gefühl haben, auf diese Weise gleichsam mit den Gedanken eines Verstorbenen in Beziehung getreten zu sein. Sie sagen sich: Das war ein Gefühl von etwas, das nicht bloß in mir war, das nicht bloß etwas Geträumtes in mir war; das war ein Gefühl, das mir einen Vorgang draußen in der Welt vermittelt hat. - Das drückt sich natürlich in Bildern aus, aber es entspricht einem Vorgange.",
      "Ich will Ihnen ein solches Bild vorlesen, wo einer nacherzählt hat, was er da erlebt hat> und zwar etwas Ähnliches wie das, was ich eben erzählt habe. Das schildert er etwa so: «Als ich von den Soldaten verabschiedet wurde, traf ich auf meinem Wege drei Männer.",
      "Die wollten einen To­ten ausgraben, weil er ihnen drei Mark schuldig war. Da wurde ich von Mitleid ergriffen und berichtigte die Schuld, damit der Verstorbene Ruhe habe und nicht mehr gestört werde in seinem Grabe.",
      "Ich wanderte weiter. Da schloß sich mir ein fremder Mann mit bleichem Gesichte an und lud mich ein, ein bleiernes Fahrzeug zu besteigen, und er überredete mich, zu einem Schloß mit ihm zu fahren. In dem Schloß wohne eine Prinzessin, die erklärt habe, sie wolle nur den Menschen heiraten, der auf einem bleiernen Wagen zu ihr käme.",
      "Dann ging er zu dem Kutscher und sagte: Da kam ein Schäfer und sagte: von Ravensburg!> Er befahl dem Kutscher, schneller zu fahren. Wir kamen an ein Tor, und es wurde ein Tumult hörbar. Das Tor wurde aufgeschlossen.",
      "Die Prinzessin fragte nun den Mann, woher er sei, wie er mit dem alten Manne hätte fahren können, und ich merkte, daß der, welcher mich dahin geführt hatte, ein Geist sei. Da kam ich dann in das Tor hinein.",
      "Ich trat ein und war Besitzer des Schlosses.» Das heißt, er kam zurück in seinen Leib. Da finden Sie ein solches Erlebnis ge­schildert, wie ich es angeführt habe.",
      "Und was ist denn das, wenn es einem andern passiert, und der er­zählt es dann weiter? Das ist ein Märchen.",
      "Auf keine andere Art als auf diese Weise sind die Märchen ent­standen. Alles andere, was über die Märchenentstehung gesagt wird, ist nichts weiter als eine wüste Phantasie. Alle wirklichen Märchen sind ein Beweis dafür, daß es Erlebnisse außerhalb des physischen Lei­bes des Menschen gibt, wenn der Ätherleib in gewisser Weise gelockert wird und der Mensch in Beziehung zur äußeren ätherischen Welt tritt. Das ist die eine Art, wie der Mensch durch seinen Ätherleib mit der äußeren Welt in Beziehung tritt.",
      "Aber er tritt noch auf eine andere Weise mit der äußeren ätherischen Welt in Beziehung. Er tritt mit ihr auch in Beziehung da, wo, man möchte sagen, eine halbbewußte, eine halb vom Ich durchsetzte Tätig­keit vorliegt. Das ist bei der Sprache der Fall. Wir sprechen ja nicht so vollbewußt, wie wir denken. Es ist gar nicht wahr, daß wir das Sprechen als etwas, was uns angehört, in unserer Gewalt haben. In der Sprache leben sich ätherische Gewalten aus, und ein gut Teil Unbe­wußtheit ist in der Sprache. Das Ich reicht nicht vollständig in die Sprache hinunter. Wir stehen, indem wir sprechen, mit unserem Äther-leibe mit der uns umgebenden ätherischen Welt in Beziehung. Denken lernen wir als Individuum, sprechen aber nicht. Sprechen werden wir gelehrt durch das Karma, das uns hineinstellt in einen gewissen Lebens-zusammenhang. Während wir gleichsam in abnormen Zuständen, wenn der Ätherleib gelockert ist, mit den Naturgeistern in Beziehung kom­men, kommen wir einfach, indem wir sprechen, indem wir nicht bloß stumm denken, mit den Volksgeistern in Beziehung. Und es leben sich in unsere Ätherleiber - nicht bis zu unserem Bewußtsein heraufreichend",
      "- die Volksgeister ein. Was in dieser Weise in dem Men­schen lebt, gehört im Grunde genommen ebensowenig zu seiner voll­bewußten Ich-Tätigkeit wie das, was der Mensch uns als Märchen hier nacherzählt.",
      "Wir haben damit das Hineinspielen von Luzifer und Ahriman in den Ätherleib des Menschen dargestellt. Aber auch in den astralischen Leib spielen die luziferischen und ahrimanischen Kräfte hinein. Nun, wenn wir den astralischen Menschenleib studieren, müssen wir auf das Hervorragendste hinweisen, was den astralischen Menschen, wie er auf der Erde ist, charakterisiert. Das ist das Bewußtsein. Im physischen Leibe ist die Form und die Kraft das Wesentliche; im Ätherleibe die Bewegung, das Leben; im Astralleibe das Bewußtsein. Wir haben aber nicht bloß einen Bewußtseinszustand im menschlichen Leibe, wir haben zwei Bewußtseinszustände: den gewöhnlichen Wachzustand und den Schlafzustand. Aber nun ist da das Merkwürdige, daß uns beide eigent­lich nicht voll natürlich sind. Man könnte sagen, weder der Wach-zustand noch der Schlafzustand sind uns voll natürlich. Natürlich wäre uns ein Zwischenzustand zwischen beiden, in dem wir eigentlich nie­mals wirklich bewußt leben.",
      "Würden wir fortwährend wachen, so würden wir uns kaum als Menschen durch die verschiedenen Lebensalter ordentlich entwickeln können. Nur dadurch, daß gleichsam immer etwas in uns ist, was weni­ger wach ist, als wir bei Tage wach sind, sind wir imstande, uns zu ent­wickeln. Fragen Sie sich selber, wieviel Sie daran denken, sich zu ent­wickeln durch das, was Sie im gewöhnlichen Leben erfahren und auf­nehmen? Wir befriedigen dadurch mehr die Neugierde, das Sensations­bedürfnis. Aber wie wenig geht man darauf aus, das, was man im wachen Tagesleben erfährt, in den Dienst der Entwickelung zu stellen. Nur dadurch entwickelt man sich, daß auch immer etwas mitschläft in uns, wenn wir bei Tage wach sind. Ich meine nicht, wenn der Mensch einschläft, sondern auch wenn er bei Tage ganz wach ist, schläft immer noch etwas. Und dieses Mitschlafende bewirkt, daß er nicht immer eigentlich ein Kind bleibt, sondern sich weiterentwickelt.",
      "Das, was uns bewußt ist durch unseren Astralleib, ist der gewöhn­liche Wachzustand. Der gewöhnliche Wachzustand aber ist so, daß wir",
      "dabei zu stark wach sind. Wir sind zu stark an die äußere Welt hin­gegeben im gewöhnlichen Wachzustande, gehen ganz auf in der äuße­ren Welt. Und woher kommt das? Das kommt davon her, weil das Wachbewußtsein unter dem starken Einflusse, unter der Übermacht des Ahriman lebt. Wachbewußtsein = Ahriman.",
      "Anders ist das beim Schlafbewußtsein. Beim Schlafbewußtsein sind wir wieder zu wenig wach. Da tuii wir alles zu sehr für unsere Ent­wickelung, für uns selber. Wir sind da ganz in uns und so stark in uns, daß alles Bewußtsein ausgelöscht wird. Im Schlafbewußtsein hat Luzi­fer die Oberhand. Schlafbewußtsein = Luzifer.",
      "So sind wir also mit Bezug auf unseren astralischen Leib so, daß, wenn wir wachen, Ahriman die Oberhand über Luzifer hat, und wenn wir schlafen, Luzifer die Oberhand hat über Ahriman. Das Gleichge­wicht halten sie sich nur, wenn wir träumen; da raufen sie sich, da hal­ten sie sich das Gleichgewicht. Da werden die Vorstellungen, die von Ahriman hervorgerufen sind im Tagesbewußtsein, die er verhärten, kristallisieren läßt, durch den Einfluß von Luzifer aufgelöst und wie­der zum Verschwinden gebracht. Alles wird zu Bildern, indem er sie nicht zu festen Vorstellungen erstarren läßt, sie werden wieder auf­gelöst und beweglich in sich. So wie bei einer Waage das Gleichgewicht dadurch zustande kommt in einem Punkte oder in einer Linie, daß die Waage auf beiden Seiten gleichmäßig belastet wird, so daß wir es nicht mehr mit einer Ruhe, sondern mit einem Gleichgewichte zu tun haben, so haben wir es auch im Menschenleben nicht mit einer Ruhe, sondern mit einem Gleichgewichte zu tun. Und die beiden Kräfte, die sich da die Waage halten, von denen die eine oder die andere zeitweise das Übergewicht hat, sind Luzifer und Ahriman. Im Wachbewußtsein sinkt die Waagschale des Ahriman, im Schlafbewußtsein die Waag­schale des Luzifer herunter. Nur in dem Zwischenzustande, in dem wir träumen, schaukelt die Waage auf und ab, nicht etwa als ob sie in Ruhe wäre, sondern sie schaukelt auf und ab.",
      "Aber auch dann, wenn wir noch weiter heraufgehen in das mensch­liche Leben, zeigt sich uns, daß das Durchwalltsein der Welt von Luzi­fer und Ahriman darin wirksam ist. Zwei Begriffe spielen ja für das Leben eine große Rolle. Der eine Begriff ist der Begriff der Pflicht,",
      "wir könnten auch sagen, wenn wir die Sache religiös fassen, der Be­griff des Gebotes. Wir sagen ja auch Pflichtgebot. Der andere Begriff, den wir dabei ins Auge fassen wollen, ist der Begriff des Rechtes.",
      "Wenn Sie sich überlegen, wie im menschlichen Leben der Begriff der Pflicht und der Begriff des Rechtes eine Rolle spielen - des Rechtes, das der Mensch hat zu dem oder jenem -, so werden Sie bald gewahr werden, daß Pflicht und Recht polarische Begriffe, polarische Gegen­sätze sind, und daß gewissermaßen auch die Neigungen der Menschen so sind, daß sie bald mehr nach der Pflicht, bald mehr nach dem Rechte gehen. Wir leben allerdings in einer Epoche, wo die Menschen lieber von ihren Rechten sprechen als von ihren Pflichten. Alle möglichen Gebiete machen ihre Rechte geltend. Wir haben daher Arbeiterrecht, Frauenrecht und so weiter.",
      "Pflicht ist der entgegengesetzte Begriff des Rechtes. Unsere Zeit wird abgelöst werden von einer solchen Zeit, in welcher geltend ge­macht werden gerade unter dem Einflusse der anthroposophisch spi­rituellen Weltanschauung die Pflichten. Und erst in der Zukunft, aller­dings mehr in einer späteren Zukunft, wird man Bewegungen haben, wo immer weniger betont werden wird die Rechtsforderung, sondern viel mehr die Pflichtforderung. Es wird dann mehr gefragt werden:",
      "Was hat man als Frau, als Mann an dieser oder jener Stelle für Pflich­ten? So wird die Epoche der Pflichtforderung die Epoche der Rechts-forderung ablösen.",
      "Wie polarische Gegensätze, wie Polaritäten spielen in unser Leben hinein Recht und Pflicht. Nun kann man sagen: Wenn der Mensch nach der Pflicht hinblickt mit seiner Seele, so blickt er eigentlich aus sich hinaus. - Kant hat das ja so grandios zum Ausdruck gebracht, in­dem er die Pflicht hingestellt hat wie eine hehre Göttin, zu der der Mensch aufschaut: «Pflicht! du erhabener großer Name, der du nichts Beliebtes, was Einschmeichelung bei sich führt, in dir fassest, sondern Unterwerfung verlangst... » - Der Mensch sieht die Pflicht gleichsam herabstrahlen aus Regionen der geistigen Welt. Religiös empfindet er die Pflicht als einen von den Wesenheiten der höheren Hierarchien auf­erlegten Impuls. Und indem der Mensch sich der Pflicht unterwirft, geht er in dem Pflichtgefühl aus sich heraus. Und dieses In-dem-Pflichtgefühl-aus-sich-Herausgehen",
      "ist schon etwas, was den Menschen aus seinem gewöhnlichen Selbst herausbringt.",
      "Aber alles derartige Herausgehen aus dem gewöhnlichen Selbst, sol­ches Streben nach Vergeistigung würde den Menschen in eine Lage bringen, in der er gleichsam den Boden unter den Füßen verlöre, wenn er nur dieser einen Tendenz sich hingeben würde, des Strebens aus sich heraus. Der Mensch würde gleichsam die Schwere verlieren, wenn er nur immer aus sich heraus wollte. Daher muß der Mensch, wenn er der Pflicht sich unterwirft, versuchen, in sich selbst eine Hilfe zu finden, die ihm gleichsam Schwere gibt, wenn er sich der Pflicht unterwirft. Schön hat das Schiller ausgedrückt, welcher das Wort gesprochen hat, daß der Mensch das schönste Verhältnis zur Pflicht habe, wenn er die Pflicht zugleich lieben lernt.",
      "Mit diesem Gedanken ist eigentlich viel gesagt. Wenn der Mensch davon spricht, daß er die Pflicht lieben lernt, da unterwirft er sich nicht mehr bloß der Pflicht, da steigt er heraus aus sich und nimmt die Liebe mit, mit der er sonst nur sich selber liebt. Die Liebe, die in seinem Leibe lebt und Egoismus war, nimmt er heraus und liebt die Pflicht. Solange sie Selbstliebe ist, so lange ist sie luziferische Kraft. Wenn der Mensch aber diese Selbstliebe aus sich herausnimmt und die Pflicht liebt, wie er sonst nur sich selbst liebt, so erlöst er Luzifer, nimmt ihn hinaus in das Gebiet der Pflicht und macht sozusagen Luzifer zu einem berechtigten Wesen im Wirken, im Impulsfühlen der Pflicht.",
      "Dagegen, wenn der Mensch das nicht kann, wenn er nicht die Liebe aus sich herausholen und sie der Pflicht darbringen kann, so fährt er fort, nur sich zu lieben. Kann er nicht die Pflicht lieben, dann kann er sich nur der Pflicht unterwerfen, dann wird er der Sklave der Pflicht, dann vertrocknet er, dann verhärtet er als Pflichtenmensch, wird kalt und nüchtern, obwohl er der Pflicht hingegeben ist. Er verhärtet ahri­manisch, trotzdem er der Pflicht folgt.",
      "# Bild s. 144",
      "Sie sehen, wie die Pflicht gleichsam mitten darinnensteht. Unter­werfen wir uns ihr, so vernichtet sie unsere Freiheit. Wir werden Sklaven der Pflicht, weil Ahriman von der einen Seite sich mit seinen Impulsen der Pflicht nähert. Bringen wir aber uns selbst, bringen wir der Pflicht die Kraft der Selbstliebe als Opfer dar, bringen wir die luziferische Wärme als Liebe der Pflicht entgegen, dann ist die Folge davon, daß wir durch den Gleichgewichtszustand zwischen Luzifer und Ahriman zu der Pflicht ein entsprechendes Verhältnis finden. Im Moralischen bringen wir selber also einen Gleichgewichtszustand her­vor zwischen Luzifer und Ahriman. Ahriman ist draußen im Geistigen und vertrocknet uns die Pflicht, der wir uns unterwerfen müssen, so daß sie uns die Freiheit nimmt. Wir aber führen ihm aus unserem eige­nen Organismus die Liebe entgegen, bringen ihm uns selbst entgegen. Durch den Kampf zwischen Luzifer und Ahriman bringen wir das rechte Verhältnis hervor zu der Pflicht. So sind wir in gewisser Be­ziehung auch die Erlöser des Luzifer. Wenn wir anfangen, unsere Pflichten lieben zu können, dann ist der Moment eingetreten, wo wir zur Erlösung der luziferischen Mächte beitragen, wo wir die luziferi­schen Kräfte, die sonst verzaubert, zur Selbstliebe verzaubert in uns sind, aus uns herausführen zum Kampfe mit Ahriman. Dadurch erlösen wir den in Selbstliebe verzauberten Luzifer; wir befreien ihn, wenn wir unsere Pflicht lieben lernen.",
      "Schiller hat in seinen Briefen «Über die ästhetische Erziehung des Menschen» sich dieselbe Frage gestellt: Wie kommt man über die Ver­sklavung unter die Pflicht hinweg zum Lieben der Pflicht? Nur hat er nicht die Ausdrücke gebraucht: Luzifer und Ahriman, weil er die Sache nicht kosmisch gedacht hat. Aber unmittelbar übersetzbar in die Geisteswissenschaft sind diese wunderbaren Briefe Schillers über die ästhetische Erziehung des Menschen.",
      "Beim Rechte ist es so, daß das Recht, indem wir es geltend machen, sich sogleich mit Luzifer verbunden zeigt. Sein Recht braucht der Mensch nicht lieben zu lernen, er liebt es, und es ist ganz naturgemäß, daß er sein Recht liebt. Es ist eine natürliche Verbindung zwischen Luzifer und dem Rechte im Fühlen, dem Erfühlen des Rechtes. Und überall da, wo Rechte geltend gemacht werden, spricht Luzifer mit.",
      "Manchmal kann man es schon äußerlich recht deutlich sehen, wie in der Propagierung vori diesem oder jenem Recht Luzifers Macht stark mit­spricht. Hier handelt es sich darum, daß wir gegenüber dem Rechte zu dem Entgegengesetzten kommen, daß wir gleichsam Ahriman her­beirufen, um dem Luzifer, der schon mit dem Rechte verknüpft ist, einen Gegenpol zu bieten. Und das können wir gewissermaßen durch den Gegenpol der Liebe. Die Liebe ist inneres Feuer; ihr Gegenpol ist die Gelassenheit, das Hinnehmen dessen, was einmal im Weltenkarma an uns herantritt; das Verstehen desjenigen, was geschieht in der Welt, die verstehende Gelassenheit. Sobald wir mit der verstehenden Gelas­senheit an unsere Rechte herankommen, rufen wir Ahriman von drau­ßen herein. Hier ist er nur schwerer zu erkennen. Wir erlösen ihn von seinem bloß äußeren Sein, rufen ihn in uns herein, wärmen ihn durch die Liebe, die schon mit dem Rechte verknüpft ist. Die Gelassenheit hat die Kälte des Ahriman. In dem Verstehen dessen, was in der Welt ist, verbinden wir unsere verstehende warme Liebe mit dem, was Kälte draußen in der Welt ist. Da erlösen wir Ahriman, wenn wir verstehend dem, was geworden ist, gegenüberstehen, wenn wir nicht nur aus unse­rer Selbstliebe heraus dem Recht gegenüber fordern, sondern verstehen, was in der Welt geworden ist.",
      "Das ist der ewige Kampf zwischen Luzifer und Ahriman in der Welt. Es ist so, daß der Mensch auf der einen Seite in konservativer Art die Zustände verstehen lernt, daß er die Zustände, wie sie gewor­den sind aus kosmischer, karmischer Notwendigkeit heraus, verstehen lernt. Das ist die eine Seite. Und die andere Seite ist die, daß man in seiner Brust fühlt den Drang, immer Neues werden zu lassen, die revo­lutionäre Strömung. In der revolutionären Strömung lebt Luzifer. In der konservativen Strömung lebt Ahriman. Und der Mensch lebt zwi­schen diesen beiden polarischen Gegensätzen darinnen, indem er in seinem Rechtsleben darinnensteht.",
      "So sehen wir, wie auch Recht und Pflicht die Gleichgewichtslage darstellen zwischen Luzifer und Ahriman. Wie sich solche Dinge, wie der menschliche physische Leib, der ätherische Leib und astralische Leib im Leben, wie sich Pflicht und Recht im Rechts- und Pflichten-leben darstellen, wie diese Dinge überhaupt in der Welt stehen, das",
      "lernen wir nur erkennen, wenn wir das Ineinanderspielen der geistigen Mächte kennenlernen, vor allen Dingen auch derjenigen geistigen Mächte, welche die Gleichgewichtslage bewirken.",
      "Genauso wie wir das betrachten können, was schon da ist, unter dem Einflusse der das Gleichgewicht bewirkenden geistigen Kräfte steht, so fügt sich auch hinein in die Welt der polarischen Gegensätze dasjenige, was wir in unserem moralischen Leben darleben. Auch die ganze Moral, die Ethik, das sittliche Leben mit seinen Polen des Pflicht-lebens und des Rechtslebens werden erst verständlich, wenn man die Einstrahlungen von Ahriman und Luzifer in Betracht zieht. Ebenso das historische, das geschichtliche Leben der Menschen, welches sich so abspielt, daß revolutionär-kriegerische, das heißt luziferische Bewe­gungen im Wechsel mit den konservativ-friedlichen, das heißt ahri­manischen Bewegungen auftreten. Es stellt sich uns dar wiederum als ein Gleichgewichtszustand zwischen dem Luziferischen und Ahrima-nischen. Anders können wir die Welt nicht verstehen, als wenn wir sie so in Gegensätzen erkennend betrachten. Was uns draußen in der Welt entgegentritt, stellt sich uns in Gegensätzen dar, ist richtig dualistisch. Und in dieser Beziehung ist der Manichäismus, der richtig verstandene Manichäismus, der dualistisch ist, voll begründet. Wie dieser Manichä­ismus auch innerhalb eines spirituellen Monismus voll begründet ist, davon werden wir in Zukunft noch verschiedentlich reden können.",
      "Was ich beabsichtige in diesen Vorträgen, ist, Ihnen zu zeigen, wie die Welt das Ergebnis von Gleichgewichtswirkungen ist. Und ein sol­ches Ergebnis von Gleichgewichtswirkungen spricht sich insbesondere auch im künstlerischen Leben aus. Von diesem Punkte ausgehend, wer­den wir später einmal die Künste und ihre Entwickelung in der Welt betrachten und den Anteil, den die verschiedenen geistigen Mächte an der Entwickelung des künstlerischen Lebens in der Menschheit haben."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Aus den gestrigen Auseinandersetzungen werden Sie haben entnehmen können, daß selbst unsere Leibesform dadurch so ist, wie sie ist, daß sie gleichsam ein Ergebnis des Zusammenwirkens der luziferischen und ahrimanischen Mächte darstellt."
      ],
      [
        "Es ist gerade für unsere Zeit sehr wichtig, dieses Zusammenwirken der luziferischen und ahrimanischen Mächte wirklich zu kennen, denn erst dadurch wird allmählich in die Menschheit ein Verständnis für die Kräfte einziehen können, die hinter der äußeren Phantasmagorie des Daseins wirken.",
        "Wir wissen, daß wir weder Ahriman zu hassen noch uns vor Luzifer zu fürchten brauchen, weil diese Mächte nur so lange gewissermaßen feindliche Mächte in der Welt sind, als sie nicht in ihren eigenen Gebieten wirken.",
        "Davon ist ja voriges Jahr in Mün­chen viel gesprochen worden.",
        "Darüber sind auch schon hier Andeu­tungen gemacht worden."
      ],
      [
        "Indem wir nun gestern gesehen haben, wie der physische, räum­liche Menschenleib in seiner Form zustande kommt durch das Widerspiel der luziferischen und ahrimanischen Mächte, haben wir auf das Äußerlichste im Menschenleben hingewiesen, in dem Luzifer und Ahri­man ihre Rolle spielen.",
        "Sie wissen, wir kommen etwas mehr in das In­nere des Menschenlebens, wenn wir vom physischen Leibe fortschrei­ten zum ätherischen Leibe.",
        "Der Atherleib ist gewissermaßen der Bildner des physischen Leibes.",
        "Er ist eingebettet in die ganze ätherische Welt, er liegt als ein beweglicher, als ein immer in sich beweglicher ätherischer Organismus unserem physischen Organismus zugrunde.",
        "Nun ist in bezug auf den ätherischen Leib zu sagen, daß auch in ihm, geradeso wie wir das für den physischen Leib gesehen haben, luziferische und ahrimanische Mächte wirksam sind, daß der Mensch auch als äthe­risches Wesen hineingestellt ist - das müssen wir betonen - in das Wi­derspiel der luziferischen und ahrimanischen Kräfte."
      ],
      [
        "Um nun auf dasjenige hinzuweisen, auf welches es dabei ankommt, wollen wir einmal einen Blick auf die drei Grundtätigkeiten des menschlichen"
      ],
      [
        "Wesens werfen, insofern der Mensch nicht ein physisches Wesen ist, auf das Wollen, Fühlen und Denken.",
        "Dieses Wollen, Fühlen und Denken sehen wir natürlich nicht, wenn wir den Menschen in bezug auf seinen physischen Leib ansehen.",
        "Nur insofern der physische Leib seinen Ausdruck hat in einer gewissen Physiognomie, in Gesten und dergleichen, können wir durch den physischen Leib hindurch ahnen, was im menschlichen Inneren ist.",
        "Der Ätherleib aber ist schon als ein in sich beweglicher Organismus ein immerwährender Ausdruck des Denkens, Fühlens und Wollens des Menschen."
      ],
      [
        "In bezug auf dieses Denken, Fühlen und Wollen hat es wieder die rein äußere Wissenschaft etwas schwierig, und wenn man die philo­sophischen Weltanschauungen durchgeht, wird man sehen, daß bald der eine Philosoph das Wollen voranstellt und bald ein anderer das Denken.",
        "Auch solche gibt es, welche das Fühlen als die hauptsächlichste Kraft betrachten."
      ],
      [
        "Aber wie eigentlich dieses Denken, Fühlen und Wollen im Menschen eine Einheit bildet, darüber können sich diese philosophischen Weltanschauungen keinen rechten Begriff bilden.",
        "Die­ses Sich keinen rechten Begriff bilden Können über das Verhältnis von Denken, Fühlen und Wollen in dem menschlichen Seelenleben ist ge­rade so, als wenn der Mensch Schwierigkeiten empfinden würde, in dem Auseinandersetzen mit dem Begriffe des Menschen überhaupt zu­rechtzukommen."
      ],
      [
        "Ich weiß nicht recht - sagen die Philosophen -, ist die menschliche Seele mehr willensartiger, mehr gefühlsartiger oder mehr denkerischer Natur?",
        "Ist sie mehr das eine oder das andere? - Das ist gerade so, wie wenn jemand sagen wollte: Nun weiß ich wirklich nicht mehr recht, was ein Mensch ist."
      ],
      [
        "Da hat mir eben einer gesagt, er wolle mir einen Menschen bringen, und da bringt er mir ein kleines Wesen, ein fünfjähriges Kind, und sagt: Das ist ein Mensch. - Dann ist ein anderer gekommen und sagte auch, er wolle mir einen Menschen zeigen und da hat er mir ein Wesen gebracht, das viel größer ist als das erste, also ein Wesen in den mittleren Menschenjahren.",
        "Ein dritter ist endlich gekommen und hat mir auch gesagt, er wolle mir ein Men­schenwesen zeigen."
      ],
      [
        "Er zeigte mir ein ganz anderes Wesen, das runzelig im Gesichte war, graue Haare hatte und so weiter.",
        "Und jetzt weiß ich wirklich nicht mehr, was ein Mensch ist.",
        "Drei verschiedene Wesen hat"
      ],
      [
        "man mir gezeigt! - Ja, alle drei, nicht wahr, sind Menschen.",
        "Nur ist der eine ganz jung, der andere ist etwas älter, und der dritte ist schon ganz alt geworden.",
        "Sie sind sehr verschieden in ihrer Erscheinung.",
        "Aber so­bald man die drei Alter zusammenhält, weiß man, was ein Mensch ist."
      ],
      [
        "So ist es aber auch mit dem Wollen, Fühlen und Denken.",
        "Der Unterschied ist nur der, daß das Wollen wohl dieselbe Seelentätigkeit ist wie das Denken, nur ganz jung noch, kindlich.",
        "Und wenn das Wollen älter wird, dann wird es Fühlen, und das ganz alte Wollen ist das Denken.",
        "Es ist nur ein Unterschied im Alter beim Wollen, Fühlen und Denken, nur daß sie in unserer Seele zusammenleben, die Lebens­alter für diese Seelentätigkeiten, das macht die Sache schwierig.",
        "Aber wir haben schon auseinandergesetzt - Sie brauchen es nur nachzulesen in meinem Buche «Die Schwelle der geistigen Welt» -, daß, sobald wir aus der physischen Welt hinauskommen, das Gesetz der Verwandlung gilt, nicht das der Starrheit.",
        "Da verwandelt sich alles.",
        "Das Alte wird plötzlich jung, das Junge wird alt und so weiter.",
        "So daß wirklich gleichzeitig in uns auftreten können die drei Seelentätigkeiten: das Wollen, das sich bald als junges Wollen zeigt, bald als älteres Wollen, das heißt als Fühlen, und auch als ältestes Wollen, als ganz altes Wol­len, das heißt als Denken.",
        "Da gehen die Lebensalter durcheinander, es wird dann alles flüssig.",
        "So ist es im Ätherleib des Menschen."
      ],
      [
        "Aber diese Verwandlung kann nicht so ohne weiteres durch sich selbst zustande kommen.",
        "Dasjenige, was einheitliche Seelentätigkeit wäre, das kommt uns überhaupt im gewöhnlichen Leben nicht zum Bewußtsein, das können wir gar nicht ins Bewußtsein hereinbringen.",
        "Wenn wir - weil ja das Ganze im Ätherleib beobachtet werden muß, und der Ätherleib etwas Bewegliches, Flüssiges ist - den Ätherleib wie einen fortlaufenden Strom symbolisch zeichnen, so kommt uns dieser Strom der Seelentätigkeit im gewöhnlichen Leben überhaupt nicht zum Bewußtsein, sondern in diesen Strom, in dieses fortwährende Bewegen des Ätherleibes, das mit der Zeit fortfließt, gliedert sich hinein einmal luziferische und dann wieder ahrimanische Tätigkeit."
      ],
      [
        "Die luziferische Tätigkeit macht das Wollen jung.",
        "Unsere Seelen-tätigkeit, durchzogen von Luziferischem, ist Wollen.",
        "Wenn das Luzi­ferische in unserer Seelentätigkeit überwiegt, wenn in unserer Seele nur"
      ],
      [
        "Luzifer seine Kräfte geltend macht, so ist das Wollen.",
        "Luzifer wirkt ver­jüngend auf den Gesamtstrom unserer Seelentätigkeit.",
        "Wenn Ahriman dagegen hauptsächlich seine Wirkungen äußert in unserer Seelentätig­keit, dann verhärtet er unsere Seelentätigkeit, sie wird alt, und das ist das Denken.",
        "Dieses Denken, dieses Gedankenhaben ist gar nicht mög­lich im gewöhnlichen Leben, ohne daß in dem ätherischen Leibe Ahri­man seine Kräfte entfaltet.",
        "Man kann im Seelenleben, insofern es sich im Ätherleibe äußert, nicht ohne Ahriman und Luzifer auskommen."
      ],
      [
        "# Bild s. 134"
      ],
      [
        "Würde Luzifer sich ganz zurückziehen von unserem ätherischen Leibe, dann würden wir kein luziferisches Feuer haben zum Wollen.",
        "Würde Ahriman sich ganz zurückziehen von unserem Seelenleben, dann wür­den wir niemals die Kühle des Denkens entwickeln können.",
        "In der Mitte von beiden ist eine Region, wo sie miteinander kämpfen.",
        "Hier durchdringen sie sich, Luzifer und Ahriman, hier spielen ihre Tätig­keiten ineinander.",
        "Das ist die Region des Fühlens.",
        "In der Tat, so er­scheint der menschliche Ätherleib, daß man darinnen wahrnehmen kann das luziferische Licht und die ahrimanische Härte.",
        "Wenn man"
      ],
      [
        "den menschlichen Ätherleib überblickt, so ist das natürlich nicht so an-geordnet, wie hier (auf der Zeichnung) symbolisch, sondern da ist ein Durcheinander.",
        "Da sind Einschiebsel, in denen der Ätherleib undurch­sichtig erscheint, so, wie wenn er, ich möchte sagen, Eiseinschläge hätte.",
        "Figuren treten im Ätherleibe auf, die man vergleichen kann mit Eis­figuren, wie sie auf Fensterscheiben erscheinen.",
        "Das sind die Verhär­tungen in dem Ätherleibe.",
        "An solchen Stellen wird er undurchsichtig.",
        "Das sind aber die Auslebungen des Gedankenlebens im Ätherleibe.",
        "Die­ses Gefrieren des Ätherleibes an gewissen Stellen rührt von Ahriman her, der seine Kräfte da hineinschickt durch das Denken."
      ],
      [
        "# Bild s. 135"
      ],
      [
        "An andern Stellen des Ätherleibes ist es so, als wenn er Vakuolen, ganz lichte Stellen in sich hätte, die durchsichtig sind, die glänzend, lichtglitzernd sind.",
        "Da sendet Luzifer seine Strahlen, seine Kräfte hin­ein, das sind die Willenszentren im Ätherleibe.",
        "Und in dem, was da­zwischen liegt, wo gleichsam fortwährende Tätigkeit ist im Ätherleibe, ist es so, daß man sieht, hier ist eine harte Stelle, aber nun wird sie so­gleich von einer solchen Lichtstelle gefaßt und aufgelöst.",
        "Ein fort­währendes Festwerden und Wiederauflösen.",
        "Das ist der Ausdruck der Gefühlstätigkeit im Ätherleibe."
      ],
      [
        "So können wir sagen: Nicht nur die Form des physischen Leibes ist durch das Ineinanderspielen der das Gleichgewicht störenden oder bewirkenden luziferischen und ahrimanischen Kräfte hervorgerufen, sondern auch im ganzen Ätherleibe spielen luziferische und ahrima­nische Kräfte.",
        "Wenn die ahrimanischen Kräfte die Überhand haben, so ist das ein Ausdruck des Denkens, wenn die luziferischen Kräfte die Überhand haben, so ist das ein Ausdruck des Wollens, und wenn sie sich gegenseitig raufen, könnte man sagen, so ist das ein Ausdruck des Fühlens."
      ],
      [
        "Da haben wir die Art, wie im Ätherleibe luziferische und ahrima­nische Kräfte ineinanderspielen.",
        "Wir sind gewissermaßen ganz das Er­gebnis von solchen Kräften, und sind eigentlich in der Zwischenlage zwischen solchen Kräften darinnen."
      ],
      [
        "Nun müssen wir uns darüber klar sein, daß wir in dem, was da spielt, nicht mit unserem vollen Ich immer darinnen sind.",
        "Unser Ich, unser irdisches Ich, das wir uns erst im Laufe der Erdenentwickelung erworben haben, kann seine volle Tätigkeit und sein volles Bewußtsein zunächst nur im physischen Leibe entfalten.",
        "Im Ätherleibe wird es sich erst während der Jupiterzeit voll entfalten können, so daß in alledem, was im Ätherleibe spielt, das eigentliche Ich des Menschen nicht un­mittelbar tätig ist.",
        "Würde zu der fortschreitenden Weltevolution nichts hinzugekommen sein von ahrimanischen und luziferischen Kräften, dann würde der Mensch ein ganz anderes Wesen sein, dann würde der Mensch in seinem physischen Leibe Wahrnehmungen haben können, aber er würde nicht eigentlich Gedanken haben können.",
        "Gedanken hat er dadurch, daß auf seinen Ätherleib Ahriman Einfluß gewinnen kann.",
        "Willensimpulse hat er dadurch, daß auf seinen Ätherleib luzi­ferische Kräfte Einfluß gewinnen können.",
        "Diese Kräfte müssen also da sein."
      ],
      [
        "Wir müssen uns also klar darüber sein, daß wir für unser irdisches Bewußtsein nicht voll hinunter können in den Ätherleib.",
        "Wir können nur im physischen Leibe unser volles Ich-Bewußtsein ausleben.",
        "In den Ätherleib können wir nicht vollständig hinunter.",
        "Mit diesem Äther-leib tauchen wir daher unter in eine Welt, worin wir selbst nicht voll­ständig sind.",
        "Und mit Ahriman, der gedankenbildend in unseren Ätherleib"
      ],
      [
        "eintritt, treten nicht nur unsere Gedanken in unseren Ätherleib ein.",
        "Mit Luzifer, der willensbildend in unserem Ätherleib ist, treten nicht nur unsere Willensimpulse in unseren Ätherleib ein.",
        "Und so ist es auch mit den Gefühlen, dem Gebiet, wo sich die beiden raufen.",
        "In­sofern nun Ahriman in unserem Ätherleibe lebt, tauchen wir mit dem Ätherleibe unter in die Sphäre der Naturgeister, der elementarischen Naturgeister, der Erd-, Wasser-, Luft- und Feuergeister.",
        "Wir wissen das nur nicht, weil wir mit unserem Ich nicht voll in unseren Äther-leib hinunter können.",
        "Aber es ist immer so, daß in diesem Ätherleibe nicht nur dasjenige als Gedankenmacht lebt, was wir selbst denken, sondern da dringen auch die Einflüsse der Naturgeister ein.",
        "Insbeson­dere jedesmal wenn der Mensch diesen Naturgeistern gegenübertritt, weiß er zu erzählen davon, daß er etwas erlebt hat, was er im gewöhn­lichen Ich-Bewußtsein nicht erlebt hat, und zwar tritt er diesen Natur-geistern dann gegenüber, wenn irgend etwas Abnormes bei ihm eintritt, wenn der Ätherleib gleichsam etwas losgerissen wird aus dem physi­schen Leibe."
      ],
      [
        "Wodurch kann so etwas geschehen?",
        "Sehen Sie, der Ätherleib des Menschen steht in Verbindung mit der ganzen umliegenden ätherischen Welt, also auch mit der ganzen Sphäre der Naturgeister um uns herum.",
        "Nehmen wir nun einmal an, um ein Beispiel anzuführen, ein Mensch ginge bei Tage auf der Straße.",
        "Wenn er mit seinem gewöhnlichen Bewußtsein auf der Straße geht, dann ist sein Ätherleib richtig in seinem physischen Leibe darinnen, und er nimmt mit seinem Ich-Bewußtsein wahr, was man eben mit dem Ich-Bewußtsein wahr­nehmen kann."
      ],
      [
        "Nehmen wir aber einmal an, er geht in der Nacht über einen Weg.",
        "Wenn man nachts über einen Weg geht, so ist es gewöhnlich finster, was ja bei manchem Menschen schon grauselig-gruselige Zustände be­wirkt.",
        "Dadurch nun, daß er in einen solchen grauselig-gruseligen Zu­stand kommt, lockert sich durch diese eigentümlichen Empfindungen, die da kommen, in denen Luzifer ihn besonders ergreift, der ätherische Leib aus dem physischen Leib heraus, und dadurch kann jetzt dieser befreite ätherische Leib, der sich herausgelöst hat aus dem physischen Leib, in Beziehung treten zu der umliegenden ätherischen Welt."
      ],
      [
        "Nehmen wir nun an, der Betreffende komme in die Nähe eines Kirchhofes, wo noch Ätherleiber sind auf den Gräbern eben Verstor­bener.",
        "Da kann er vielleicht in diesem Zustand, wenn sich sein Äther­leib herausgelockert hat, irgend etwas von den Gedanken, die noch in den Ätherleibern der Verstorbenen sitzen, wahrnehmen.",
        "Nehmen wir an, es sei jemand verstorben vor kurzer Zeit, der habe Schulden hinter­lassen und sei mit dem Gedanken, Schulden gemacht zu haben, ge­storben.",
        "Dieser Gedanke nun kann noch darinnensitzen in dem Äther-leibe des Verstorbenen.",
        "Man nimmt selbstverständlich diese Gedanken im Ä therleibe des andern nicht wahr, wenn der eigene Ätherleib nicht gelockert ist, aber in dem Zustande, den ich geschildert habe, kann man es wahrnehmen.",
        "Man kann mit dem Ätherleibe des andern in Beziehung treten und kann daher diesen Gedanken: Ich habe Schulden gemacht -wahrnehmen.",
        "Und jetzt, weil durch dieses die luziferische Macht in ihm verstärkt wird, regt sich in ihm das Gefühl: Ich muß diesem die Schuld bezahlen."
      ],
      [
        "So ein Mensch erlebt also etwas in seinem ätherischen Leibe, was er niemals im physischen Leibe im normalen Leben erleben würde.",
        "Man erlebt so etwas nicht alle Tage im gewöhnlichen Menschenleben, daher bringt es auch etwas sehr Bedeutsames im Bewußtsein hervor, wenn man das erlebt.",
        "Es bringt das im Bewußtsein hervor, daß man weiß, jetzt hast du etwas erlebt, das hast du nicht in deinem Leibe erlebt, das kannst du in deinem Leibe nicht erleben.",
        "Man fühlt, man ist irgendwo anders als in seinem Leibe, und das empfindet man als eine ungewohnte Lage.",
        "Man ist woanders als in seinem Leibe; und man fühlt dann den Drang, in seinen Leib wieder zurückzukehren; man sehnt sich nach Hilfe, um in seinen Leib wieder zurückzukehren."
      ],
      [
        "Solch ein Gefühl, das man da hat, das Gefühl der Sehnsucht, in seinen Leib wieder zurückzukehren, ruft irgendwelche Elementargei­ster, Naturgeister heran, für die das Gefühl des Menschen gleichsam Speise, Nahrung ist.",
        "Sie kommen dadurch heran, daß sie gleichsam an­gezogen werden durch das Gefühl: Ich möchte in meinen physischen Leib herein. - Sie verhelfen einem dazu, den Weg zurückzufinden in den physischen Leib.",
        "Wenn man in gewöhnlicher Art schläft, findet man den Weg leicht zurück; wenn man aber so etwas erlebt wie das,"
      ],
      [
        "was ich geschildert habe, findet man ihn schwer zurück.",
        "Aber man nimmt es nicht so wahr, wie man es im physischen Leibe wahrnimmt, sondern man nimmt es imaginativ, in Bildern wahr.",
        "Es kommt irgend­einer heran, der eigentlich ein Naturgeist ist, der vielleicht in der Ge­stalt eines Hirten, in der Gestalt eines Schäfers erscheint und der einem den Rat gibt: Gehe hin zu irgendeinem Schlosse.",
        "Ich werde dich dahin bringen auf einem Wagen - und dergleichen mehr."
      ],
      [
        "Mit solchen Vorstellungen kann sich noch etwas anderes verknüp­fen.",
        "Es kann sich damit verknüpfen, daß einem der Leib, den man ver­lassen hat, außerhalb dessen man das Erlebnis hatte, wie ein verzauber­tes Schlöß erscheint, aus dem man jemanden erlösen muß, wenn man hineinkommt.",
        "So imaginiert man diese Sehnsucht nach dem physischen Leibe und das Helfen der Naturgeister.",
        "Dann kommt man wieder in den physischen Leib zurück, das heißt, man wacht auf."
      ],
      [
        "Solche Erlebnisse erzählen die Menschen dann, die es in der Realität erlebt haben, weil sie das Gefühl haben, auf diese Weise gleichsam mit den Gedanken eines Verstorbenen in Beziehung getreten zu sein.",
        "Sie sagen sich: Das war ein Gefühl von etwas, das nicht bloß in mir war, das nicht bloß etwas Geträumtes in mir war; das war ein Gefühl, das mir einen Vorgang draußen in der Welt vermittelt hat. - Das drückt sich natürlich in Bildern aus, aber es entspricht einem Vorgange."
      ],
      [
        "Ich will Ihnen ein solches Bild vorlesen, wo einer nacherzählt hat, was er da erlebt hat> und zwar etwas Ähnliches wie das, was ich eben erzählt habe.",
        "Das schildert er etwa so: «Als ich von den Soldaten verabschiedet wurde, traf ich auf meinem Wege drei Männer."
      ],
      [
        "Die wollten einen To­ten ausgraben, weil er ihnen drei Mark schuldig war.",
        "Da wurde ich von Mitleid ergriffen und berichtigte die Schuld, damit der Verstorbene Ruhe habe und nicht mehr gestört werde in seinem Grabe."
      ],
      [
        "Ich wanderte weiter.",
        "Da schloß sich mir ein fremder Mann mit bleichem Gesichte an und lud mich ein, ein bleiernes Fahrzeug zu besteigen, und er überredete mich, zu einem Schloß mit ihm zu fahren.",
        "In dem Schloß wohne eine Prinzessin, die erklärt habe, sie wolle nur den Menschen heiraten, der auf einem bleiernen Wagen zu ihr käme."
      ],
      [
        "Dann ging er zu dem Kutscher und sagte: Da kam ein Schäfer und sagte: von Ravensburg!> Er befahl dem Kutscher, schneller zu fahren.",
        "Wir kamen an ein Tor, und es wurde ein Tumult hörbar.",
        "Das Tor wurde aufgeschlossen."
      ],
      [
        "Die Prinzessin fragte nun den Mann, woher er sei, wie er mit dem alten Manne hätte fahren können, und ich merkte, daß der, welcher mich dahin geführt hatte, ein Geist sei.",
        "Da kam ich dann in das Tor hinein."
      ],
      [
        "Ich trat ein und war Besitzer des Schlosses.» Das heißt, er kam zurück in seinen Leib.",
        "Da finden Sie ein solches Erlebnis ge­schildert, wie ich es angeführt habe."
      ],
      [
        "Und was ist denn das, wenn es einem andern passiert, und der er­zählt es dann weiter?",
        "Das ist ein Märchen."
      ],
      [
        "Auf keine andere Art als auf diese Weise sind die Märchen ent­standen.",
        "Alles andere, was über die Märchenentstehung gesagt wird, ist nichts weiter als eine wüste Phantasie.",
        "Alle wirklichen Märchen sind ein Beweis dafür, daß es Erlebnisse außerhalb des physischen Lei­bes des Menschen gibt, wenn der Ätherleib in gewisser Weise gelockert wird und der Mensch in Beziehung zur äußeren ätherischen Welt tritt.",
        "Das ist die eine Art, wie der Mensch durch seinen Ätherleib mit der äußeren Welt in Beziehung tritt."
      ],
      [
        "Aber er tritt noch auf eine andere Weise mit der äußeren ätherischen Welt in Beziehung.",
        "Er tritt mit ihr auch in Beziehung da, wo, man möchte sagen, eine halbbewußte, eine halb vom Ich durchsetzte Tätig­keit vorliegt.",
        "Das ist bei der Sprache der Fall.",
        "Wir sprechen ja nicht so vollbewußt, wie wir denken.",
        "Es ist gar nicht wahr, daß wir das Sprechen als etwas, was uns angehört, in unserer Gewalt haben.",
        "In der Sprache leben sich ätherische Gewalten aus, und ein gut Teil Unbe­wußtheit ist in der Sprache.",
        "Das Ich reicht nicht vollständig in die Sprache hinunter.",
        "Wir stehen, indem wir sprechen, mit unserem Äther-leibe mit der uns umgebenden ätherischen Welt in Beziehung.",
        "Denken lernen wir als Individuum, sprechen aber nicht.",
        "Sprechen werden wir gelehrt durch das Karma, das uns hineinstellt in einen gewissen Lebens-zusammenhang.",
        "Während wir gleichsam in abnormen Zuständen, wenn der Ätherleib gelockert ist, mit den Naturgeistern in Beziehung kom­men, kommen wir einfach, indem wir sprechen, indem wir nicht bloß stumm denken, mit den Volksgeistern in Beziehung.",
        "Und es leben sich in unsere Ätherleiber - nicht bis zu unserem Bewußtsein heraufreichend"
      ],
      [
        "- die Volksgeister ein.",
        "Was in dieser Weise in dem Men­schen lebt, gehört im Grunde genommen ebensowenig zu seiner voll­bewußten Ich-Tätigkeit wie das, was der Mensch uns als Märchen hier nacherzählt."
      ],
      [
        "Wir haben damit das Hineinspielen von Luzifer und Ahriman in den Ätherleib des Menschen dargestellt.",
        "Aber auch in den astralischen Leib spielen die luziferischen und ahrimanischen Kräfte hinein.",
        "Nun, wenn wir den astralischen Menschenleib studieren, müssen wir auf das Hervorragendste hinweisen, was den astralischen Menschen, wie er auf der Erde ist, charakterisiert.",
        "Das ist das Bewußtsein.",
        "Im physischen Leibe ist die Form und die Kraft das Wesentliche; im Ätherleibe die Bewegung, das Leben; im Astralleibe das Bewußtsein.",
        "Wir haben aber nicht bloß einen Bewußtseinszustand im menschlichen Leibe, wir haben zwei Bewußtseinszustände: den gewöhnlichen Wachzustand und den Schlafzustand.",
        "Aber nun ist da das Merkwürdige, daß uns beide eigent­lich nicht voll natürlich sind.",
        "Man könnte sagen, weder der Wach-zustand noch der Schlafzustand sind uns voll natürlich.",
        "Natürlich wäre uns ein Zwischenzustand zwischen beiden, in dem wir eigentlich nie­mals wirklich bewußt leben."
      ],
      [
        "Würden wir fortwährend wachen, so würden wir uns kaum als Menschen durch die verschiedenen Lebensalter ordentlich entwickeln können.",
        "Nur dadurch, daß gleichsam immer etwas in uns ist, was weni­ger wach ist, als wir bei Tage wach sind, sind wir imstande, uns zu ent­wickeln.",
        "Fragen Sie sich selber, wieviel Sie daran denken, sich zu ent­wickeln durch das, was Sie im gewöhnlichen Leben erfahren und auf­nehmen?",
        "Wir befriedigen dadurch mehr die Neugierde, das Sensations­bedürfnis.",
        "Aber wie wenig geht man darauf aus, das, was man im wachen Tagesleben erfährt, in den Dienst der Entwickelung zu stellen.",
        "Nur dadurch entwickelt man sich, daß auch immer etwas mitschläft in uns, wenn wir bei Tage wach sind.",
        "Ich meine nicht, wenn der Mensch einschläft, sondern auch wenn er bei Tage ganz wach ist, schläft immer noch etwas.",
        "Und dieses Mitschlafende bewirkt, daß er nicht immer eigentlich ein Kind bleibt, sondern sich weiterentwickelt."
      ],
      [
        "Das, was uns bewußt ist durch unseren Astralleib, ist der gewöhn­liche Wachzustand.",
        "Der gewöhnliche Wachzustand aber ist so, daß wir"
      ],
      [
        "dabei zu stark wach sind.",
        "Wir sind zu stark an die äußere Welt hin­gegeben im gewöhnlichen Wachzustande, gehen ganz auf in der äuße­ren Welt.",
        "Und woher kommt das?",
        "Das kommt davon her, weil das Wachbewußtsein unter dem starken Einflusse, unter der Übermacht des Ahriman lebt.",
        "Wachbewußtsein = Ahriman."
      ],
      [
        "Anders ist das beim Schlafbewußtsein.",
        "Beim Schlafbewußtsein sind wir wieder zu wenig wach.",
        "Da tuii wir alles zu sehr für unsere Ent­wickelung, für uns selber.",
        "Wir sind da ganz in uns und so stark in uns, daß alles Bewußtsein ausgelöscht wird.",
        "Im Schlafbewußtsein hat Luzi­fer die Oberhand.",
        "Schlafbewußtsein = Luzifer."
      ],
      [
        "So sind wir also mit Bezug auf unseren astralischen Leib so, daß, wenn wir wachen, Ahriman die Oberhand über Luzifer hat, und wenn wir schlafen, Luzifer die Oberhand hat über Ahriman.",
        "Das Gleichge­wicht halten sie sich nur, wenn wir träumen; da raufen sie sich, da hal­ten sie sich das Gleichgewicht.",
        "Da werden die Vorstellungen, die von Ahriman hervorgerufen sind im Tagesbewußtsein, die er verhärten, kristallisieren läßt, durch den Einfluß von Luzifer aufgelöst und wie­der zum Verschwinden gebracht.",
        "Alles wird zu Bildern, indem er sie nicht zu festen Vorstellungen erstarren läßt, sie werden wieder auf­gelöst und beweglich in sich.",
        "So wie bei einer Waage das Gleichgewicht dadurch zustande kommt in einem Punkte oder in einer Linie, daß die Waage auf beiden Seiten gleichmäßig belastet wird, so daß wir es nicht mehr mit einer Ruhe, sondern mit einem Gleichgewichte zu tun haben, so haben wir es auch im Menschenleben nicht mit einer Ruhe, sondern mit einem Gleichgewichte zu tun.",
        "Und die beiden Kräfte, die sich da die Waage halten, von denen die eine oder die andere zeitweise das Übergewicht hat, sind Luzifer und Ahriman.",
        "Im Wachbewußtsein sinkt die Waagschale des Ahriman, im Schlafbewußtsein die Waag­schale des Luzifer herunter.",
        "Nur in dem Zwischenzustande, in dem wir träumen, schaukelt die Waage auf und ab, nicht etwa als ob sie in Ruhe wäre, sondern sie schaukelt auf und ab."
      ],
      [
        "Aber auch dann, wenn wir noch weiter heraufgehen in das mensch­liche Leben, zeigt sich uns, daß das Durchwalltsein der Welt von Luzi­fer und Ahriman darin wirksam ist.",
        "Zwei Begriffe spielen ja für das Leben eine große Rolle.",
        "Der eine Begriff ist der Begriff der Pflicht,"
      ],
      [
        "wir könnten auch sagen, wenn wir die Sache religiös fassen, der Be­griff des Gebotes.",
        "Wir sagen ja auch Pflichtgebot.",
        "Der andere Begriff, den wir dabei ins Auge fassen wollen, ist der Begriff des Rechtes."
      ],
      [
        "Wenn Sie sich überlegen, wie im menschlichen Leben der Begriff der Pflicht und der Begriff des Rechtes eine Rolle spielen - des Rechtes, das der Mensch hat zu dem oder jenem -, so werden Sie bald gewahr werden, daß Pflicht und Recht polarische Begriffe, polarische Gegen­sätze sind, und daß gewissermaßen auch die Neigungen der Menschen so sind, daß sie bald mehr nach der Pflicht, bald mehr nach dem Rechte gehen.",
        "Wir leben allerdings in einer Epoche, wo die Menschen lieber von ihren Rechten sprechen als von ihren Pflichten.",
        "Alle möglichen Gebiete machen ihre Rechte geltend.",
        "Wir haben daher Arbeiterrecht, Frauenrecht und so weiter."
      ],
      [
        "Pflicht ist der entgegengesetzte Begriff des Rechtes.",
        "Unsere Zeit wird abgelöst werden von einer solchen Zeit, in welcher geltend ge­macht werden gerade unter dem Einflusse der anthroposophisch spi­rituellen Weltanschauung die Pflichten.",
        "Und erst in der Zukunft, aller­dings mehr in einer späteren Zukunft, wird man Bewegungen haben, wo immer weniger betont werden wird die Rechtsforderung, sondern viel mehr die Pflichtforderung.",
        "Es wird dann mehr gefragt werden:"
      ],
      [
        "Was hat man als Frau, als Mann an dieser oder jener Stelle für Pflich­ten?",
        "So wird die Epoche der Pflichtforderung die Epoche der Rechts-forderung ablösen."
      ],
      [
        "Wie polarische Gegensätze, wie Polaritäten spielen in unser Leben hinein Recht und Pflicht.",
        "Nun kann man sagen: Wenn der Mensch nach der Pflicht hinblickt mit seiner Seele, so blickt er eigentlich aus sich hinaus. - Kant hat das ja so grandios zum Ausdruck gebracht, in­dem er die Pflicht hingestellt hat wie eine hehre Göttin, zu der der Mensch aufschaut: «Pflicht! du erhabener großer Name, der du nichts Beliebtes, was Einschmeichelung bei sich führt, in dir fassest, sondern Unterwerfung verlangst... » - Der Mensch sieht die Pflicht gleichsam herabstrahlen aus Regionen der geistigen Welt.",
        "Religiös empfindet er die Pflicht als einen von den Wesenheiten der höheren Hierarchien auf­erlegten Impuls.",
        "Und indem der Mensch sich der Pflicht unterwirft, geht er in dem Pflichtgefühl aus sich heraus.",
        "Und dieses In-dem-Pflichtgefühl-aus-sich-Herausgehen"
      ],
      [
        "ist schon etwas, was den Menschen aus seinem gewöhnlichen Selbst herausbringt."
      ],
      [
        "Aber alles derartige Herausgehen aus dem gewöhnlichen Selbst, sol­ches Streben nach Vergeistigung würde den Menschen in eine Lage bringen, in der er gleichsam den Boden unter den Füßen verlöre, wenn er nur dieser einen Tendenz sich hingeben würde, des Strebens aus sich heraus.",
        "Der Mensch würde gleichsam die Schwere verlieren, wenn er nur immer aus sich heraus wollte.",
        "Daher muß der Mensch, wenn er der Pflicht sich unterwirft, versuchen, in sich selbst eine Hilfe zu finden, die ihm gleichsam Schwere gibt, wenn er sich der Pflicht unterwirft.",
        "Schön hat das Schiller ausgedrückt, welcher das Wort gesprochen hat, daß der Mensch das schönste Verhältnis zur Pflicht habe, wenn er die Pflicht zugleich lieben lernt."
      ],
      [
        "Mit diesem Gedanken ist eigentlich viel gesagt.",
        "Wenn der Mensch davon spricht, daß er die Pflicht lieben lernt, da unterwirft er sich nicht mehr bloß der Pflicht, da steigt er heraus aus sich und nimmt die Liebe mit, mit der er sonst nur sich selber liebt.",
        "Die Liebe, die in seinem Leibe lebt und Egoismus war, nimmt er heraus und liebt die Pflicht.",
        "Solange sie Selbstliebe ist, so lange ist sie luziferische Kraft.",
        "Wenn der Mensch aber diese Selbstliebe aus sich herausnimmt und die Pflicht liebt, wie er sonst nur sich selbst liebt, so erlöst er Luzifer, nimmt ihn hinaus in das Gebiet der Pflicht und macht sozusagen Luzifer zu einem berechtigten Wesen im Wirken, im Impulsfühlen der Pflicht."
      ],
      [
        "Dagegen, wenn der Mensch das nicht kann, wenn er nicht die Liebe aus sich herausholen und sie der Pflicht darbringen kann, so fährt er fort, nur sich zu lieben.",
        "Kann er nicht die Pflicht lieben, dann kann er sich nur der Pflicht unterwerfen, dann wird er der Sklave der Pflicht, dann vertrocknet er, dann verhärtet er als Pflichtenmensch, wird kalt und nüchtern, obwohl er der Pflicht hingegeben ist.",
        "Er verhärtet ahri­manisch, trotzdem er der Pflicht folgt."
      ],
      [
        "# Bild s. 144"
      ],
      [
        "Sie sehen, wie die Pflicht gleichsam mitten darinnensteht.",
        "Unter­werfen wir uns ihr, so vernichtet sie unsere Freiheit.",
        "Wir werden Sklaven der Pflicht, weil Ahriman von der einen Seite sich mit seinen Impulsen der Pflicht nähert.",
        "Bringen wir aber uns selbst, bringen wir der Pflicht die Kraft der Selbstliebe als Opfer dar, bringen wir die luziferische Wärme als Liebe der Pflicht entgegen, dann ist die Folge davon, daß wir durch den Gleichgewichtszustand zwischen Luzifer und Ahriman zu der Pflicht ein entsprechendes Verhältnis finden.",
        "Im Moralischen bringen wir selber also einen Gleichgewichtszustand her­vor zwischen Luzifer und Ahriman.",
        "Ahriman ist draußen im Geistigen und vertrocknet uns die Pflicht, der wir uns unterwerfen müssen, so daß sie uns die Freiheit nimmt.",
        "Wir aber führen ihm aus unserem eige­nen Organismus die Liebe entgegen, bringen ihm uns selbst entgegen.",
        "Durch den Kampf zwischen Luzifer und Ahriman bringen wir das rechte Verhältnis hervor zu der Pflicht.",
        "So sind wir in gewisser Be­ziehung auch die Erlöser des Luzifer.",
        "Wenn wir anfangen, unsere Pflichten lieben zu können, dann ist der Moment eingetreten, wo wir zur Erlösung der luziferischen Mächte beitragen, wo wir die luziferi­schen Kräfte, die sonst verzaubert, zur Selbstliebe verzaubert in uns sind, aus uns herausführen zum Kampfe mit Ahriman.",
        "Dadurch erlösen wir den in Selbstliebe verzauberten Luzifer; wir befreien ihn, wenn wir unsere Pflicht lieben lernen."
      ],
      [
        "Schiller hat in seinen Briefen «Über die ästhetische Erziehung des Menschen» sich dieselbe Frage gestellt: Wie kommt man über die Ver­sklavung unter die Pflicht hinweg zum Lieben der Pflicht?",
        "Nur hat er nicht die Ausdrücke gebraucht: Luzifer und Ahriman, weil er die Sache nicht kosmisch gedacht hat.",
        "Aber unmittelbar übersetzbar in die Geisteswissenschaft sind diese wunderbaren Briefe Schillers über die ästhetische Erziehung des Menschen."
      ],
      [
        "Beim Rechte ist es so, daß das Recht, indem wir es geltend machen, sich sogleich mit Luzifer verbunden zeigt.",
        "Sein Recht braucht der Mensch nicht lieben zu lernen, er liebt es, und es ist ganz naturgemäß, daß er sein Recht liebt.",
        "Es ist eine natürliche Verbindung zwischen Luzifer und dem Rechte im Fühlen, dem Erfühlen des Rechtes.",
        "Und überall da, wo Rechte geltend gemacht werden, spricht Luzifer mit."
      ],
      [
        "Manchmal kann man es schon äußerlich recht deutlich sehen, wie in der Propagierung vori diesem oder jenem Recht Luzifers Macht stark mit­spricht.",
        "Hier handelt es sich darum, daß wir gegenüber dem Rechte zu dem Entgegengesetzten kommen, daß wir gleichsam Ahriman her­beirufen, um dem Luzifer, der schon mit dem Rechte verknüpft ist, einen Gegenpol zu bieten.",
        "Und das können wir gewissermaßen durch den Gegenpol der Liebe.",
        "Die Liebe ist inneres Feuer; ihr Gegenpol ist die Gelassenheit, das Hinnehmen dessen, was einmal im Weltenkarma an uns herantritt; das Verstehen desjenigen, was geschieht in der Welt, die verstehende Gelassenheit.",
        "Sobald wir mit der verstehenden Gelas­senheit an unsere Rechte herankommen, rufen wir Ahriman von drau­ßen herein.",
        "Hier ist er nur schwerer zu erkennen.",
        "Wir erlösen ihn von seinem bloß äußeren Sein, rufen ihn in uns herein, wärmen ihn durch die Liebe, die schon mit dem Rechte verknüpft ist.",
        "Die Gelassenheit hat die Kälte des Ahriman.",
        "In dem Verstehen dessen, was in der Welt ist, verbinden wir unsere verstehende warme Liebe mit dem, was Kälte draußen in der Welt ist.",
        "Da erlösen wir Ahriman, wenn wir verstehend dem, was geworden ist, gegenüberstehen, wenn wir nicht nur aus unse­rer Selbstliebe heraus dem Recht gegenüber fordern, sondern verstehen, was in der Welt geworden ist."
      ],
      [
        "Das ist der ewige Kampf zwischen Luzifer und Ahriman in der Welt.",
        "Es ist so, daß der Mensch auf der einen Seite in konservativer Art die Zustände verstehen lernt, daß er die Zustände, wie sie gewor­den sind aus kosmischer, karmischer Notwendigkeit heraus, verstehen lernt.",
        "Das ist die eine Seite.",
        "Und die andere Seite ist die, daß man in seiner Brust fühlt den Drang, immer Neues werden zu lassen, die revo­lutionäre Strömung.",
        "In der revolutionären Strömung lebt Luzifer.",
        "In der konservativen Strömung lebt Ahriman.",
        "Und der Mensch lebt zwi­schen diesen beiden polarischen Gegensätzen darinnen, indem er in seinem Rechtsleben darinnensteht."
      ],
      [
        "So sehen wir, wie auch Recht und Pflicht die Gleichgewichtslage darstellen zwischen Luzifer und Ahriman.",
        "Wie sich solche Dinge, wie der menschliche physische Leib, der ätherische Leib und astralische Leib im Leben, wie sich Pflicht und Recht im Rechts- und Pflichten-leben darstellen, wie diese Dinge überhaupt in der Welt stehen, das"
      ],
      [
        "lernen wir nur erkennen, wenn wir das Ineinanderspielen der geistigen Mächte kennenlernen, vor allen Dingen auch derjenigen geistigen Mächte, welche die Gleichgewichtslage bewirken."
      ],
      [
        "Genauso wie wir das betrachten können, was schon da ist, unter dem Einflusse der das Gleichgewicht bewirkenden geistigen Kräfte steht, so fügt sich auch hinein in die Welt der polarischen Gegensätze dasjenige, was wir in unserem moralischen Leben darleben.",
        "Auch die ganze Moral, die Ethik, das sittliche Leben mit seinen Polen des Pflicht-lebens und des Rechtslebens werden erst verständlich, wenn man die Einstrahlungen von Ahriman und Luzifer in Betracht zieht.",
        "Ebenso das historische, das geschichtliche Leben der Menschen, welches sich so abspielt, daß revolutionär-kriegerische, das heißt luziferische Bewe­gungen im Wechsel mit den konservativ-friedlichen, das heißt ahri­manischen Bewegungen auftreten.",
        "Es stellt sich uns dar wiederum als ein Gleichgewichtszustand zwischen dem Luziferischen und Ahrima-nischen.",
        "Anders können wir die Welt nicht verstehen, als wenn wir sie so in Gegensätzen erkennend betrachten.",
        "Was uns draußen in der Welt entgegentritt, stellt sich uns in Gegensätzen dar, ist richtig dualistisch.",
        "Und in dieser Beziehung ist der Manichäismus, der richtig verstandene Manichäismus, der dualistisch ist, voll begründet.",
        "Wie dieser Manichä­ismus auch innerhalb eines spirituellen Monismus voll begründet ist, davon werden wir in Zukunft noch verschiedentlich reden können."
      ],
      [
        "Was ich beabsichtige in diesen Vorträgen, ist, Ihnen zu zeigen, wie die Welt das Ergebnis von Gleichgewichtswirkungen ist.",
        "Und ein sol­ches Ergebnis von Gleichgewichtswirkungen spricht sich insbesondere auch im künstlerischen Leben aus.",
        "Von diesem Punkte ausgehend, wer­den wir später einmal die Künste und ihre Entwickelung in der Welt betrachten und den Anteil, den die verschiedenen geistigen Mächte an der Entwickelung des künstlerischen Lebens in der Menschheit haben."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "OLAF ASTESON SIEBENTER VORTRAG Hannover, 1. Januar 1912, Neujahrsfeier",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Das sogenannte «Traumlied», das heute zum Vortrag gebracht werden wird, erfordert einige Bemerkungen, die vorausgeschickt werden sollen.",
      "Es ist auf dieses Traumlied schon in der vor einigen Tagen von mir Ihnen gegebenen Weihnachtsansprache hingewiesen worden. Da konnte ich sagen, daß die Feststellung des Weihnachtsfestes keineswegs eine nur ausgedachte, eine aus dem Gedanken entsprungene sei, sondern daß die Feststellung des Weihnachtsfestes im Laufe des Jahres ent­springt ganz bestimmten inneren Vorgängen, die sich zutragen können in der menschlichen Seele, wenn diese Seele zu hellseherischen Visionen als höchsten Seelenfrüchten entweder durch gewisse im natürlichen Lauf der Dinge gelegene Kräfte oder durch geschultes Hellsehertum kommt. Was da eigentlich der menschlichen Seele zugrunde liegen kann, das können wir uns am besten dadurch klarmachen, daß wir den folgenden Gedanken vor unsere Seele hinstellen.",
      "All das an Pflanzen, all das an sprießenden, sprossenden Gewäch­sen, was Sonnenlicht und Sonnenwärme hervorzaubert im Frühling und gedeihen läßt den Sommer hindurch, all das geht gleichsam ein zu einem winterlichen Schlafe, zu winterlicher Finsternis auf einer Art Winterpfad ein in derjenigen Zeit, in welche verlegt wurde von dem geschichtlichen Bewußtsein der Menschheit das Weihnachtsfest. Wie Schlaf, wie Finsternis der Naturwesen, so erscheint uns die Zeit, in wel­cher das Weihnachtsfest festgesetzt ist. Umgekehrt wie mit der äußeren Natur, ist es mit der menschlichen Seele. Während die Naturwesen hinuntersteigen in die Finsternis und sie die menschliche Seele in dieses Reich äußerer Sonnenfinsternis begleitet, wird es in dieser menschlichen Seele - oder kann es wenigstens werden - heller. Sie kann durch den natürlichen Verlauf der Dinge, den wir öfter als ein gewisses vererbtes Hellsehertum angedeutet haben, oder durch geschultes Hellsehertum gerade in die lichteste Geisteswelt eintauchen, wo ihr aufgehen dann die Geheimnisse des Geistes, die hinter den äußeren sinnlichen Dingen verborgen liegen. Und so wie dieses Heruntersteigen der Pflanzenwelt",
      "um die Zeit des Winterpfades einem regelmäßigen Gesetz unterliegt, so unterliegt auch das spirituelle Aufblühen der Menschen solch einem Gesetz, so daß es zusammenfällt in seiner lichten Helligkeit mit der natürlichen Finsternis, in welche das Weihnachtsfest verlegt ist.",
      "Es könnte nun scheinen, als ob solche Dinge ausgesprochen würden bloß aus dem heutigen geschulten Hellsehertum, oder, wie unsere Geg­ner sagen, aus der bloßen Phantastik. Dagegen wird aber immer ein lebendiger, vollgültiger Beweis das sein, was Menschen, was Völker äußerlich erleben.",
      "Daher war es mir außerordentlich interessant, daß, als ich mehrere Jahre hindurch innerhalb unserer Bewegung von die­sem weihnachtlichen Hellsehertum gesprochen hatte, das uns einführt in die Bedeutung des Christus-Wesens, in das Aufgehen des Christus-Wesens gerade dann, wenn am stärksten die menschliche Seele in Hell­sichtigkeit untertaucht, und ich dann wiederum einmal zu einem Vor­tragszyklus nach dem in spiritueller Beziehung uns so befreundeten Norwegen kam - daß mir da entgegengebracht wurde eine dort oben lebende merkwürdige Vision, von der allerdings derjenige, der mit sol­chen Dingen bekannt ist, sich gleich sagen muß: Ja, das klingt an vieles an, was an ähnlichen Visionen innerhalb germanischer Völker immer gelebt hat, was viele Menschen im Grunde genommen hellsichtig ge­schaut haben in der Zeit der dreizehn Nächte vom Weihnachtsabend bis zum Erscheinungsfeste Christi, dem 6. Januar. - Da kann die menschliche Seele hineinschauen in die geistige Welt und sieht da das Schicksal der Menschenseele im entkörperten Zustande, wenn sie durch­geht durch Kamaloka und es ihr dann klar wird, wie ein Verhältnis der höheren geistigen Welten zu den Taten der Menschen hier auf Erden hergestellt wird.",
      "Und interessant ist es, daß derjenige, von dem uns nun in diesem Traumlied erzählt wird und dem diese Visionen in dieser nordischen Gegend durch dieses Traumlied zugeschrieben wer­den, ein Mensch ist, der den Namen trägt: Olaf Asteson. Von diesem wird erzählt, daß er während dieser dreizehn Nächte in einer Art hell­sichtiger Erfahrung dasjenige durchmachte, was der nordische Mensch in seiner Art als Vision empfinden kann.",
      "Er erfuhr zunächst, wie sich die menschlichen Taten weiter gestalten, wenn der Mensch durch die Todespforte gegangen ist, er erfuhr aber auch, wie in das Walten und",
      "Weben der Seele nach der Entkörperung das eingreift, was wir die Christus-Wesenheit nennen, wie hineinfällt in die nordische Geistes­ordnung des Lebens nach dem Tode das Richteramt des Jesus, des Christus, der da an die Seite tritt des alten Weltenrichters, des soge­nannten Angesichtes Jehovas, des Erzengels Michael. So daß neben allem übrigen, was der Hellsichtigkeit des Olaf Asteson auftaucht, das Eindringen des Christentums in den Norden mit anklingt, und daß ihm alles in der Zeit des Jesus-Geburtstagsfestes in den dreizehn Näch­ten hellsichtig klar wird, die er hindurch schlief.",
      "Welchem Bewußtsein wird das klar? Das ist nun merkwürdig, daß uns das schon im Namen angedeutet wird, der ganz offenbar im Nor­den ursprünglich bedeutete ein solches menschliches Bewußtsein, das ererbt ist von den Urvätern, von den Ahnen.",
      "Olaf ist so recht Olaf in den Zeiten, wo das uralte, hellseherische Ahnenbewußtsein in ihm wie­der aufgeht. Der von den Ahnen sein Bewußtsein, sein inneres Wesen ererbt Habende: das ist in dem Namen Olaf enthalten.",
      "Und Äste heißt die Liebe, die Liebe, die sich im Blute fortpflanzt von Generation zu Generation. Dieser Liebe Sohn, Asteson, ist Olaf, ist das Bewußtsein, das sich von Generation zu Generation von der alten hellsichtigen Zeit her fortgepflanzt hat, ist wie wiedererstandenes Ahnentum.",
      "Olaf, der mit diesem hellsichtigen Bewußtsein geboren ist, erkennt der Menschen-seele Schicksal, schaut zugleich das Eingreifen desjenigen Wesens, das wir feiern in Jesu Geburtstagfest als seinen Eintritt in das Erdendasein. Und merkwürdig, während ganz sicher solche Visionen immer wieder­um, namentlich in germanischen Ländern, erlebt worden sind, scheint vergessen gewesen zu sein dieses Traumlied.",
      "Denn 1850 machte sich der Prediger Landstad in Telemarken, einem einsamen Gebirgstal, wo damals wenig Menschen wohnten, daran, Volkslieder zu sammeln. Und unter den mancherlei Volksliedern war lebendig im Volksmund - er wußte nicht seit wann, er wußte nicht wie lange - das Lied vom Olaf Asteson, der in den dreizehn Nächten gesehen hat der Menschenseele Schicksal, nachdem sie durch die Pforte des Todes gegangen ist, und das Hereintreten des Christus Jesus in die Weltgeschichte.",
      "Er wußte nicht, wann sich hineingelebt hat dieses Einweihungslied der Menschen-seele, dieses Initiationslied, denn es lebte und wurde anlehnend an eine",
      "musikalische Stimmung im Volksmund immerdar rezitiert. Es erfreuten sich daran die wenigen Menschen des einsamen Gebirgstals, und da las es auf der Prediger Landstad, indem es ihm sprach von den Geheim­nissen, die erkundet waren - wie von dem Volksgemüt selber - über die Initiation in uralten Zeiten. So hat es sich herübergelebt, bis es Landstad im Volksmund fand. Viele Leute glauben natürlich, daß es anspielt an Sankt Olaf, der 1030 nach Christi das Christentum ein­geführt hat und dessen Mutter Aste geheißen hat, die Liebe. Damit ver­hält es sich so wie mit vielem, daß zugleich Geschichtliches und Spiri­tuelles vorliegt.",
      "Interessant ist es fernerhin, daß dieses Traumlied nun schnell in einen großen Teil des nordischen Volkes eingedrungen ist und in den Herzen des norwegischen Volkes lebt. Es besteht ja in Norwegen eine große Bewegung, die dahin geht, die alten Zeiten wieder lebendig zu machen, und damit die alte Sprache, welche der urgermanischen Sprache sehr nahesteht, die nordische Sprache wieder aufleben zu las­sen gegenüber der später eingedrungenen dänischen Sprache.",
      "Nun ist dieses Lied in einer Sprache, die anklingt an die älteste Sprache, die sich dort erhalten hat, und die Leute, die ihr Altertum überhaupt wie­der herauftragen wollen, denen sprach dieses Lied wiederum zu Her­zen, und es drang in den letzten zehn bis fünfzehn Jahren nicht nur in die Volksherzen, sondern auch in die Schulen ein. Überall wird es gesungen, rezitiert, überall hört man sozusagen da, wo die Seele er­wacht an dem alten Volkstum, das Traumlied vom Olaf Asteson, der in den dreizehn Nächten von Weihnachten bis zum 6.",
      "Januar sozusagen natürlicherweise in die heiligen Geheimnisse der Menschheit einge­weiht worden ist. Und aus diesem Grunde möchten wir Ihnen heute dieses Traumlied vom Olaf Asteson vorführen. Fräulein von Sivers wird es rezitieren.",
      "Ich versuchte es zunächst provisorisch so herzu-richten, daß es in deutscher Sprache rezitiert werden kann, nachdem mir Frau Lindholm an die Hand gegangen ist, die eigentümliche Sprache, in der das Lied eben lebt und jetzt immer mehr und mehr lebt und zu einer Art von Volkslied geworden ist, in deutscher Sprache möglich zu machen. So werden wir es in dieser zunächst provisorischen Einrichtung, die ich in wenigen Tagen geben konnte, jetzt hören.",
      "So höre meinen Sang!",
      "Ich will dir singen",
      "Von einem flinken Jüngling:",
      "Es war das Olaf Asteson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "Er ging zur Ruh' am Weihnachtsabend.",
      "Ein starker Schlaf umfing ihn bald,",
      "Und nicht konnt' er erwachen,",
      "Bevor am dreizehnten Tag",
      "Das Volk zur Kirche ging.",
      "Es war das Olaf Asteson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "Er ging zur Ruh' am Weihnachtsabend.",
      "Er hat geschlafen gar lange!",
      "Erwachen konnt' er nicht,",
      "Bevor am dreizehnten Tag",
      "Der Vogel spreitet die Flügel!",
      "Es war das Olaf Asteson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "Nicht konnte erwachen Olaf,",
      "Bevor am dreizehnten Tag",
      "Die Sonne über den Bergen glänzte.",
      "Dann sattelt' er sein flinkes Pferd,",
      "Und eilig ritt er zu der Kirche.",
      "Es war das Olaf Asteson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "Schon stand der Priester",
      "Am Altar lesend die Messe,",
      "Als an dem Kirchentore",
      "Sich Olaf setzte, zu künden",
      "Von vieler Träume Inhalt,",
      "Die in dem langen Schlafe",
      "Die Seele ihm erfüllten.",
      "Es war das Olaf Asteson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "Und junge und auch alte Leute,",
      "Sie lauschten achtsam der Worte,",
      "Die Olaf sprach von seinen Träumen.",
      "Es war das Olaf Asteson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "«Ich ging zur Ruh' am Weihnachtsabend.",
      "Ein starker Schlaf umfing mich bald;",
      "Und nicht konnt' ich erwachen,",
      "Bevor am dreizehnten Tag",
      "Das Volk zur Kirche ging.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Erhoben ward ich in Wolkenhöhe",
      "Und in den Meeresgrund geworfen,",
      "Und wer mir folgen will,",
      "Ihn kann nicht Heiterkeit befallen.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Erhoben ward ich in Wolkenhöhe",
      "Gestoßen dann in trübe Sümpfe,",
      "Erschauend der Hölle Schrecken",
      "Und auch des Himmels Licht.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Und fahren mußt' ich in Erdentiefen,",
      "Wo furchtbar rauschen Götterströme.",
      "Zu schauen nicht vermocht' ich sie,",
      "Doch hören konnte ich das Rauschen.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Es wiehert' nicht mein schwarzes Pferd,",
      "Und meine Hunde bellten nicht,",
      "Es sang auch nicht der Morgenvogel,",
      "Es war ein einzig Wunder überall.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Befahren mußt' ich im Geisterland",
      "Der Dornenheide weites Feld,",
      "Zerrissen ward mir mein Scharlachmantel",
      "Und auch die Nägel meiner Füße",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Ich kam an die Gjallarbrücke.",
      "In höchsten Windeshöhen hänget diese,",
      "Mit rotem Gold ist sie beschlagen",
      "Und Nägel mit scharfen Spitzen hat sie.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Es schlug mich die Geisterschlange,",
      "Es biß mich der Geisterhund,",
      "Der Stier, er stand in Weges Mitte.",
      "Das sind der Brücke drei Geschöpfe.",
      "Sie sind von furchtbar böser Art.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Gar bissig ist der Hund,",
      "Und stechen will die Schlange,",
      "Der Stier, er dräut gewaltig!",
      "Sie lassen keinen über die Brücke,",
      "Der Wahrheit nicht will ehren!",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Ich bin gewandelt über die Brücke,",
      "Die schmal ist und schwindelerregend.",
      "In Sümpfen mußt' ich waten . . .",
      "Sie liegen nun hinter mir!",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "In Sümpfen mußt' ich waten,",
      "Sie schienen bodenlos dem Fuß.",
      "Als ich die Brücke überschritt,",
      "Da fühlt' ich im Munde Erde",
      "Wie Tote, die in Gräbern liegen.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "An Wasser kam ich dann,",
      "In welchen wie blaue Flammen",
      "Die Eismassen hell erglänzten . . .",
      "Und Gott, er lenkte meinen Sinn,",
      "Daß ich die Gegend mied.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Zum Winterpfad lenkt' ich die Schritte.",
      "Zur Rechten konnt' ich ihn sehn:",
      "Ich schaute wie in das Paradies,",
      "Das weithin leuchtend strahlte.",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.",
      "Und Gottes hohe Mutter,",
      "Ich sah sie dort im Glanze!",
      "Nach Brooksvalin zu fahren,",
      "So hieß sie mich, kündend,",
      "Daß Seelen dort gerichtet werden!",
      "Der Mond schien hell",
      "Und weithin dehnten sich die Wege.»",
      "«In andern Welten weilte ich",
      "Durch vieler Nächte Längen;",
      "Und Gott nur kann es wissen,",
      "Wie viel der Seelennot ich sah -",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Ich konnte schauen einen jungen Mann,",
      "Er hatte einen Knaben hingemordet:",
      "Nun mußte er ihn ewig tragen",
      "Auf seinen eignen Armen!",
      "Er stand im Schlamme so tief",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgeric1hte unterstehen.",
      "Einen alten Mann auch sah ich,",
      "Er trug einen Mantel wie von Blei;",
      "So ward gestraft er, daß er",
      "Im Geize auf der Erde lebte,",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Und Männer tauchten auf,",
      "Die feurige Stoffe trugen;",
      "Unredlichkeit lastet",
      "Auf ihren armen Seelen",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Auch Kinder konnt ich schauen,",
      "Die Kohlengluten unter ihren Füßen hatten;",
      "Den Eltern taten sie im Leben Böses,",
      "Das traf gar schwer ihre Geister",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Und jenem Hause zu nahen,",
      "Es ward mir auferlegt,",
      "Wo Hexen Arbeit leisten sollten",
      "Im Blute, das sie im Leben erzürnt,",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Von Norden her, in wilden Scharen,",
      "Da kamen geritten böse Geister,",
      "Vom Höllenfürsten geleitet,",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Was aus dem Norden kam,",
      "Das schien vor allem böse:",
      "Voran ritt er, der Höllenfürst,",
      "Auf seinem schwarzen Rosse",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Doch aus dem Süden kamen",
      "In hehrer Ruhe andre Scharen.",
      "Es ritt voran Sankt Michael",
      "An Jesu Christi Seite",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.*",
      "Die Seelen, die sündenbeladen,",
      "Sie mußten angstvoll zittern!",
      "Die Tränen rannen in Strömen",
      "Als böser Taten Folgen",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "In Hoheit stand da Michael",
      "Und wog die Menschenseelen",
      "Auf seiner Sündenwaage,",
      "Und richtend stand dabei",
      "Der Weltenrichter Jesus Christ",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.»",
      "*    Siehe Seite 227/28",
      "«Wie selig ist, wer im Erdenleben",
      "Den Armen Schuhe gibt;",
      "Er braucht nicht mit nackten Füßen",
      "Zu wandeln im Dornenfeld.",
      "Da spricht der Waage Zunge,",
      "Und Weltenwahrheit",
      "Ertönt im Geistesstand.",
      "Wie selig ist, wer im Erdenleben",
      "Den Armen Brot gereicht!",
      "Ihn können nicht verletzen",
      "Die Hunde in jener Welt.",
      "Da spricht der Waage Zunge,",
      "Und Weltenwahrheit",
      "Ertönt im Geistesstand.",
      "Wie selig ist, wer im Erdenleben",
      "Den Armen Korn gereicht!",
      "Ihm kann nicht drohen",
      "Das scharfe Horn des Stieres,",
      "Wenn er die Gjallarbrücke überschreiten muß.",
      "Da spricht der Waage Zunge,",
      "Und Weltenwahrheit",
      "Ertönt im Geistesstand.",
      "Wie selig ist, wer im Erdenleben",
      "Den Armen Kleider reicht!",
      "Ihn können nicht erfrieren",
      "Die Eisesmassen in Brooksvalin.",
      "Da spricht der Waage Zunge,",
      "Und Weltenwahrheit",
      "Ertönt im Geistesstand.»",
      "Und junge und auch alte Leute,",
      "Sie lauschten achtsam der Worte,",
      "Die Olaf sprach von seinen Träumen.",
      "Du schliefest ja gar lange . . .",
      "Erwache nun, o Olaf Asteson!"
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Das sogenannte «Traumlied», das heute zum Vortrag gebracht werden wird, erfordert einige Bemerkungen, die vorausgeschickt werden sollen."
      ],
      [
        "Es ist auf dieses Traumlied schon in der vor einigen Tagen von mir Ihnen gegebenen Weihnachtsansprache hingewiesen worden.",
        "Da konnte ich sagen, daß die Feststellung des Weihnachtsfestes keineswegs eine nur ausgedachte, eine aus dem Gedanken entsprungene sei, sondern daß die Feststellung des Weihnachtsfestes im Laufe des Jahres ent­springt ganz bestimmten inneren Vorgängen, die sich zutragen können in der menschlichen Seele, wenn diese Seele zu hellseherischen Visionen als höchsten Seelenfrüchten entweder durch gewisse im natürlichen Lauf der Dinge gelegene Kräfte oder durch geschultes Hellsehertum kommt.",
        "Was da eigentlich der menschlichen Seele zugrunde liegen kann, das können wir uns am besten dadurch klarmachen, daß wir den folgenden Gedanken vor unsere Seele hinstellen."
      ],
      [
        "All das an Pflanzen, all das an sprießenden, sprossenden Gewäch­sen, was Sonnenlicht und Sonnenwärme hervorzaubert im Frühling und gedeihen läßt den Sommer hindurch, all das geht gleichsam ein zu einem winterlichen Schlafe, zu winterlicher Finsternis auf einer Art Winterpfad ein in derjenigen Zeit, in welche verlegt wurde von dem geschichtlichen Bewußtsein der Menschheit das Weihnachtsfest.",
        "Wie Schlaf, wie Finsternis der Naturwesen, so erscheint uns die Zeit, in wel­cher das Weihnachtsfest festgesetzt ist.",
        "Umgekehrt wie mit der äußeren Natur, ist es mit der menschlichen Seele.",
        "Während die Naturwesen hinuntersteigen in die Finsternis und sie die menschliche Seele in dieses Reich äußerer Sonnenfinsternis begleitet, wird es in dieser menschlichen Seele - oder kann es wenigstens werden - heller.",
        "Sie kann durch den natürlichen Verlauf der Dinge, den wir öfter als ein gewisses vererbtes Hellsehertum angedeutet haben, oder durch geschultes Hellsehertum gerade in die lichteste Geisteswelt eintauchen, wo ihr aufgehen dann die Geheimnisse des Geistes, die hinter den äußeren sinnlichen Dingen verborgen liegen.",
        "Und so wie dieses Heruntersteigen der Pflanzenwelt"
      ],
      [
        "um die Zeit des Winterpfades einem regelmäßigen Gesetz unterliegt, so unterliegt auch das spirituelle Aufblühen der Menschen solch einem Gesetz, so daß es zusammenfällt in seiner lichten Helligkeit mit der natürlichen Finsternis, in welche das Weihnachtsfest verlegt ist."
      ],
      [
        "Es könnte nun scheinen, als ob solche Dinge ausgesprochen würden bloß aus dem heutigen geschulten Hellsehertum, oder, wie unsere Geg­ner sagen, aus der bloßen Phantastik.",
        "Dagegen wird aber immer ein lebendiger, vollgültiger Beweis das sein, was Menschen, was Völker äußerlich erleben."
      ],
      [
        "Daher war es mir außerordentlich interessant, daß, als ich mehrere Jahre hindurch innerhalb unserer Bewegung von die­sem weihnachtlichen Hellsehertum gesprochen hatte, das uns einführt in die Bedeutung des Christus-Wesens, in das Aufgehen des Christus-Wesens gerade dann, wenn am stärksten die menschliche Seele in Hell­sichtigkeit untertaucht, und ich dann wiederum einmal zu einem Vor­tragszyklus nach dem in spiritueller Beziehung uns so befreundeten Norwegen kam - daß mir da entgegengebracht wurde eine dort oben lebende merkwürdige Vision, von der allerdings derjenige, der mit sol­chen Dingen bekannt ist, sich gleich sagen muß: Ja, das klingt an vieles an, was an ähnlichen Visionen innerhalb germanischer Völker immer gelebt hat, was viele Menschen im Grunde genommen hellsichtig ge­schaut haben in der Zeit der dreizehn Nächte vom Weihnachtsabend bis zum Erscheinungsfeste Christi, dem 6.",
        "Januar. - Da kann die menschliche Seele hineinschauen in die geistige Welt und sieht da das Schicksal der Menschenseele im entkörperten Zustande, wenn sie durch­geht durch Kamaloka und es ihr dann klar wird, wie ein Verhältnis der höheren geistigen Welten zu den Taten der Menschen hier auf Erden hergestellt wird."
      ],
      [
        "Und interessant ist es, daß derjenige, von dem uns nun in diesem Traumlied erzählt wird und dem diese Visionen in dieser nordischen Gegend durch dieses Traumlied zugeschrieben wer­den, ein Mensch ist, der den Namen trägt: Olaf Asteson.",
        "Von diesem wird erzählt, daß er während dieser dreizehn Nächte in einer Art hell­sichtiger Erfahrung dasjenige durchmachte, was der nordische Mensch in seiner Art als Vision empfinden kann."
      ],
      [
        "Er erfuhr zunächst, wie sich die menschlichen Taten weiter gestalten, wenn der Mensch durch die Todespforte gegangen ist, er erfuhr aber auch, wie in das Walten und"
      ],
      [
        "Weben der Seele nach der Entkörperung das eingreift, was wir die Christus-Wesenheit nennen, wie hineinfällt in die nordische Geistes­ordnung des Lebens nach dem Tode das Richteramt des Jesus, des Christus, der da an die Seite tritt des alten Weltenrichters, des soge­nannten Angesichtes Jehovas, des Erzengels Michael.",
        "So daß neben allem übrigen, was der Hellsichtigkeit des Olaf Asteson auftaucht, das Eindringen des Christentums in den Norden mit anklingt, und daß ihm alles in der Zeit des Jesus-Geburtstagsfestes in den dreizehn Näch­ten hellsichtig klar wird, die er hindurch schlief."
      ],
      [
        "Welchem Bewußtsein wird das klar?",
        "Das ist nun merkwürdig, daß uns das schon im Namen angedeutet wird, der ganz offenbar im Nor­den ursprünglich bedeutete ein solches menschliches Bewußtsein, das ererbt ist von den Urvätern, von den Ahnen."
      ],
      [
        "Olaf ist so recht Olaf in den Zeiten, wo das uralte, hellseherische Ahnenbewußtsein in ihm wie­der aufgeht.",
        "Der von den Ahnen sein Bewußtsein, sein inneres Wesen ererbt Habende: das ist in dem Namen Olaf enthalten."
      ],
      [
        "Und Äste heißt die Liebe, die Liebe, die sich im Blute fortpflanzt von Generation zu Generation.",
        "Dieser Liebe Sohn, Asteson, ist Olaf, ist das Bewußtsein, das sich von Generation zu Generation von der alten hellsichtigen Zeit her fortgepflanzt hat, ist wie wiedererstandenes Ahnentum."
      ],
      [
        "Olaf, der mit diesem hellsichtigen Bewußtsein geboren ist, erkennt der Menschen-seele Schicksal, schaut zugleich das Eingreifen desjenigen Wesens, das wir feiern in Jesu Geburtstagfest als seinen Eintritt in das Erdendasein.",
        "Und merkwürdig, während ganz sicher solche Visionen immer wieder­um, namentlich in germanischen Ländern, erlebt worden sind, scheint vergessen gewesen zu sein dieses Traumlied."
      ],
      [
        "Denn 1850 machte sich der Prediger Landstad in Telemarken, einem einsamen Gebirgstal, wo damals wenig Menschen wohnten, daran, Volkslieder zu sammeln.",
        "Und unter den mancherlei Volksliedern war lebendig im Volksmund - er wußte nicht seit wann, er wußte nicht wie lange - das Lied vom Olaf Asteson, der in den dreizehn Nächten gesehen hat der Menschenseele Schicksal, nachdem sie durch die Pforte des Todes gegangen ist, und das Hereintreten des Christus Jesus in die Weltgeschichte."
      ],
      [
        "Er wußte nicht, wann sich hineingelebt hat dieses Einweihungslied der Menschen-seele, dieses Initiationslied, denn es lebte und wurde anlehnend an eine"
      ],
      [
        "musikalische Stimmung im Volksmund immerdar rezitiert.",
        "Es erfreuten sich daran die wenigen Menschen des einsamen Gebirgstals, und da las es auf der Prediger Landstad, indem es ihm sprach von den Geheim­nissen, die erkundet waren - wie von dem Volksgemüt selber - über die Initiation in uralten Zeiten.",
        "So hat es sich herübergelebt, bis es Landstad im Volksmund fand.",
        "Viele Leute glauben natürlich, daß es anspielt an Sankt Olaf, der 1030 nach Christi das Christentum ein­geführt hat und dessen Mutter Aste geheißen hat, die Liebe.",
        "Damit ver­hält es sich so wie mit vielem, daß zugleich Geschichtliches und Spiri­tuelles vorliegt."
      ],
      [
        "Interessant ist es fernerhin, daß dieses Traumlied nun schnell in einen großen Teil des nordischen Volkes eingedrungen ist und in den Herzen des norwegischen Volkes lebt.",
        "Es besteht ja in Norwegen eine große Bewegung, die dahin geht, die alten Zeiten wieder lebendig zu machen, und damit die alte Sprache, welche der urgermanischen Sprache sehr nahesteht, die nordische Sprache wieder aufleben zu las­sen gegenüber der später eingedrungenen dänischen Sprache."
      ],
      [
        "Nun ist dieses Lied in einer Sprache, die anklingt an die älteste Sprache, die sich dort erhalten hat, und die Leute, die ihr Altertum überhaupt wie­der herauftragen wollen, denen sprach dieses Lied wiederum zu Her­zen, und es drang in den letzten zehn bis fünfzehn Jahren nicht nur in die Volksherzen, sondern auch in die Schulen ein.",
        "Überall wird es gesungen, rezitiert, überall hört man sozusagen da, wo die Seele er­wacht an dem alten Volkstum, das Traumlied vom Olaf Asteson, der in den dreizehn Nächten von Weihnachten bis zum 6."
      ],
      [
        "Januar sozusagen natürlicherweise in die heiligen Geheimnisse der Menschheit einge­weiht worden ist.",
        "Und aus diesem Grunde möchten wir Ihnen heute dieses Traumlied vom Olaf Asteson vorführen.",
        "Fräulein von Sivers wird es rezitieren."
      ],
      [
        "Ich versuchte es zunächst provisorisch so herzu-richten, daß es in deutscher Sprache rezitiert werden kann, nachdem mir Frau Lindholm an die Hand gegangen ist, die eigentümliche Sprache, in der das Lied eben lebt und jetzt immer mehr und mehr lebt und zu einer Art von Volkslied geworden ist, in deutscher Sprache möglich zu machen.",
        "So werden wir es in dieser zunächst provisorischen Einrichtung, die ich in wenigen Tagen geben konnte, jetzt hören."
      ],
      [
        "So höre meinen Sang!"
      ],
      [
        "Ich will dir singen"
      ],
      [
        "Von einem flinken Jüngling:"
      ],
      [
        "Es war das Olaf Asteson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Er ging zur Ruh' am Weihnachtsabend."
      ],
      [
        "Ein starker Schlaf umfing ihn bald,"
      ],
      [
        "Und nicht konnt' er erwachen,"
      ],
      [
        "Bevor am dreizehnten Tag"
      ],
      [
        "Das Volk zur Kirche ging."
      ],
      [
        "Es war das Olaf Asteson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Er ging zur Ruh' am Weihnachtsabend."
      ],
      [
        "Er hat geschlafen gar lange!"
      ],
      [
        "Erwachen konnt' er nicht,"
      ],
      [
        "Bevor am dreizehnten Tag"
      ],
      [
        "Der Vogel spreitet die Flügel!"
      ],
      [
        "Es war das Olaf Asteson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Nicht konnte erwachen Olaf,"
      ],
      [
        "Bevor am dreizehnten Tag"
      ],
      [
        "Die Sonne über den Bergen glänzte."
      ],
      [
        "Dann sattelt' er sein flinkes Pferd,"
      ],
      [
        "Und eilig ritt er zu der Kirche."
      ],
      [
        "Es war das Olaf Asteson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Schon stand der Priester"
      ],
      [
        "Am Altar lesend die Messe,"
      ],
      [
        "Als an dem Kirchentore"
      ],
      [
        "Sich Olaf setzte, zu künden"
      ],
      [
        "Von vieler Träume Inhalt,"
      ],
      [
        "Die in dem langen Schlafe"
      ],
      [
        "Die Seele ihm erfüllten."
      ],
      [
        "Es war das Olaf Asteson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Und junge und auch alte Leute,"
      ],
      [
        "Sie lauschten achtsam der Worte,"
      ],
      [
        "Die Olaf sprach von seinen Träumen."
      ],
      [
        "Es war das Olaf Asteson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "«Ich ging zur Ruh' am Weihnachtsabend."
      ],
      [
        "Ein starker Schlaf umfing mich bald;"
      ],
      [
        "Und nicht konnt' ich erwachen,"
      ],
      [
        "Bevor am dreizehnten Tag"
      ],
      [
        "Das Volk zur Kirche ging."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Erhoben ward ich in Wolkenhöhe"
      ],
      [
        "Und in den Meeresgrund geworfen,"
      ],
      [
        "Und wer mir folgen will,"
      ],
      [
        "Ihn kann nicht Heiterkeit befallen."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Erhoben ward ich in Wolkenhöhe"
      ],
      [
        "Gestoßen dann in trübe Sümpfe,"
      ],
      [
        "Erschauend der Hölle Schrecken"
      ],
      [
        "Und auch des Himmels Licht."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Und fahren mußt' ich in Erdentiefen,"
      ],
      [
        "Wo furchtbar rauschen Götterströme."
      ],
      [
        "Zu schauen nicht vermocht' ich sie,"
      ],
      [
        "Doch hören konnte ich das Rauschen."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Es wiehert' nicht mein schwarzes Pferd,"
      ],
      [
        "Und meine Hunde bellten nicht,"
      ],
      [
        "Es sang auch nicht der Morgenvogel,"
      ],
      [
        "Es war ein einzig Wunder überall."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Befahren mußt' ich im Geisterland"
      ],
      [
        "Der Dornenheide weites Feld,"
      ],
      [
        "Zerrissen ward mir mein Scharlachmantel"
      ],
      [
        "Und auch die Nägel meiner Füße"
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Ich kam an die Gjallarbrücke."
      ],
      [
        "In höchsten Windeshöhen hänget diese,"
      ],
      [
        "Mit rotem Gold ist sie beschlagen"
      ],
      [
        "Und Nägel mit scharfen Spitzen hat sie."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Es schlug mich die Geisterschlange,"
      ],
      [
        "Es biß mich der Geisterhund,"
      ],
      [
        "Der Stier, er stand in Weges Mitte."
      ],
      [
        "Das sind der Brücke drei Geschöpfe."
      ],
      [
        "Sie sind von furchtbar böser Art."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Gar bissig ist der Hund,"
      ],
      [
        "Und stechen will die Schlange,"
      ],
      [
        "Der Stier, er dräut gewaltig!"
      ],
      [
        "Sie lassen keinen über die Brücke,"
      ],
      [
        "Der Wahrheit nicht will ehren!"
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Ich bin gewandelt über die Brücke,"
      ],
      [
        "Die schmal ist und schwindelerregend."
      ],
      [
        "In Sümpfen mußt' ich waten . . ."
      ],
      [
        "Sie liegen nun hinter mir!"
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "In Sümpfen mußt' ich waten,"
      ],
      [
        "Sie schienen bodenlos dem Fuß."
      ],
      [
        "Als ich die Brücke überschritt,"
      ],
      [
        "Da fühlt' ich im Munde Erde"
      ],
      [
        "Wie Tote, die in Gräbern liegen."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "An Wasser kam ich dann,"
      ],
      [
        "In welchen wie blaue Flammen"
      ],
      [
        "Die Eismassen hell erglänzten . . ."
      ],
      [
        "Und Gott, er lenkte meinen Sinn,"
      ],
      [
        "Daß ich die Gegend mied."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Zum Winterpfad lenkt' ich die Schritte."
      ],
      [
        "Zur Rechten konnt' ich ihn sehn:"
      ],
      [
        "Ich schaute wie in das Paradies,"
      ],
      [
        "Das weithin leuchtend strahlte."
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege."
      ],
      [
        "Und Gottes hohe Mutter,"
      ],
      [
        "Ich sah sie dort im Glanze!"
      ],
      [
        "Nach Brooksvalin zu fahren,"
      ],
      [
        "So hieß sie mich, kündend,"
      ],
      [
        "Daß Seelen dort gerichtet werden!"
      ],
      [
        "Der Mond schien hell"
      ],
      [
        "Und weithin dehnten sich die Wege.»"
      ],
      [
        "«In andern Welten weilte ich"
      ],
      [
        "Durch vieler Nächte Längen;"
      ],
      [
        "Und Gott nur kann es wissen,"
      ],
      [
        "Wie viel der Seelennot ich sah -"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Ich konnte schauen einen jungen Mann,"
      ],
      [
        "Er hatte einen Knaben hingemordet:"
      ],
      [
        "Nun mußte er ihn ewig tragen"
      ],
      [
        "Auf seinen eignen Armen!"
      ],
      [
        "Er stand im Schlamme so tief"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgeric1hte unterstehen."
      ],
      [
        "Einen alten Mann auch sah ich,"
      ],
      [
        "Er trug einen Mantel wie von Blei;"
      ],
      [
        "So ward gestraft er, daß er"
      ],
      [
        "Im Geize auf der Erde lebte,"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Und Männer tauchten auf,"
      ],
      [
        "Die feurige Stoffe trugen;"
      ],
      [
        "Unredlichkeit lastet"
      ],
      [
        "Auf ihren armen Seelen"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Auch Kinder konnt ich schauen,"
      ],
      [
        "Die Kohlengluten unter ihren Füßen hatten;"
      ],
      [
        "Den Eltern taten sie im Leben Böses,"
      ],
      [
        "Das traf gar schwer ihre Geister"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Und jenem Hause zu nahen,"
      ],
      [
        "Es ward mir auferlegt,"
      ],
      [
        "Wo Hexen Arbeit leisten sollten"
      ],
      [
        "Im Blute, das sie im Leben erzürnt,"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Von Norden her, in wilden Scharen,"
      ],
      [
        "Da kamen geritten böse Geister,"
      ],
      [
        "Vom Höllenfürsten geleitet,"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Was aus dem Norden kam,"
      ],
      [
        "Das schien vor allem böse:"
      ],
      [
        "Voran ritt er, der Höllenfürst,"
      ],
      [
        "Auf seinem schwarzen Rosse"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Doch aus dem Süden kamen"
      ],
      [
        "In hehrer Ruhe andre Scharen."
      ],
      [
        "Es ritt voran Sankt Michael"
      ],
      [
        "An Jesu Christi Seite"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen.*"
      ],
      [
        "Die Seelen, die sündenbeladen,"
      ],
      [
        "Sie mußten angstvoll zittern!"
      ],
      [
        "Die Tränen rannen in Strömen"
      ],
      [
        "Als böser Taten Folgen"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "In Hoheit stand da Michael"
      ],
      [
        "Und wog die Menschenseelen"
      ],
      [
        "Auf seiner Sündenwaage,"
      ],
      [
        "Und richtend stand dabei"
      ],
      [
        "Der Weltenrichter Jesus Christ"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen.»"
      ],
      [
        "* Siehe Seite 227/28"
      ],
      [
        "«Wie selig ist, wer im Erdenleben"
      ],
      [
        "Den Armen Schuhe gibt;"
      ],
      [
        "Er braucht nicht mit nackten Füßen"
      ],
      [
        "Zu wandeln im Dornenfeld."
      ],
      [
        "Da spricht der Waage Zunge,"
      ],
      [
        "Und Weltenwahrheit"
      ],
      [
        "Ertönt im Geistesstand."
      ],
      [
        "Wie selig ist, wer im Erdenleben"
      ],
      [
        "Den Armen Brot gereicht!"
      ],
      [
        "Ihn können nicht verletzen"
      ],
      [
        "Die Hunde in jener Welt."
      ],
      [
        "Da spricht der Waage Zunge,"
      ],
      [
        "Und Weltenwahrheit"
      ],
      [
        "Ertönt im Geistesstand."
      ],
      [
        "Wie selig ist, wer im Erdenleben"
      ],
      [
        "Den Armen Korn gereicht!"
      ],
      [
        "Ihm kann nicht drohen"
      ],
      [
        "Das scharfe Horn des Stieres,"
      ],
      [
        "Wenn er die Gjallarbrücke überschreiten muß."
      ],
      [
        "Da spricht der Waage Zunge,"
      ],
      [
        "Und Weltenwahrheit"
      ],
      [
        "Ertönt im Geistesstand."
      ],
      [
        "Wie selig ist, wer im Erdenleben"
      ],
      [
        "Den Armen Kleider reicht!"
      ],
      [
        "Ihn können nicht erfrieren"
      ],
      [
        "Die Eisesmassen in Brooksvalin."
      ],
      [
        "Da spricht der Waage Zunge,"
      ],
      [
        "Und Weltenwahrheit"
      ],
      [
        "Ertönt im Geistesstand.»"
      ],
      [
        "Und junge und auch alte Leute,"
      ],
      [
        "Sie lauschten achtsam der Worte,"
      ],
      [
        "Die Olaf sprach von seinen Träumen."
      ],
      [
        "Du schliefest ja gar lange . . ."
      ],
      [
        "Erwache nun, o Olaf Asteson!"
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "ACHTER VORTRAG Berlin, 7. Januar 1913",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Die Zeit von Weihnachten bis etwa in unsere Tage herein ist tatsächlich eine wichtige, eine bedeutungsvolle Zeit des Jahres, auch in okkulter Beziehung. Man nennt sie die Zeit der dreizehn Tage. Und das Merk-würdige ist, daß diese Zeit der dreizehn Tage in ihrer Wichtigkeit von denjenigen Menschen empfunden wird, welche ihrer ganzen Seelenver­anlagung nach noch etwas zurückbehalten haben von dem alten Zu­sammenhange der Menschenseele mit der geistigen Welt, von dem wir oftmals gesprochen haben. Wir wissen, mehr als der Mensch der heu­tigen Stadtbevölkerung hat von dem Zusammenhange mit der geistigen Welt, der einmal in alten Zeiten bestanden hat, der primitive Mensch zurückbehalten, der draußen auf dem Lande oder in einer Bevölkerung lebt, die noch weniger angekränkelt ist von unserer Stadtkultur. Und da finden wir dann so manches, was in der Volkspoesie von Erlebnissen der Seele handelt, von Erlebnissen der Seele in der Zeit von Weihnacht bis zu dem Dreikönigstage, dem 6. Januar.",
      "Es ist dies die Zeit, in der, nachdem die Jahresfinsternis über die Erde am meisten hereingebrochen ist, unmittelbar nach der Winter­sonnenwende, wenn die Sonne wieder ihren Siegeslauf beginnt, mit dem tiefsten Eintauchen und Befreitwerden und Erlöstwerden der Natur, auch die menschliche Seele ganz besondere Erlebnisse durchmachen kann, wenn sie noch besondere Zusammenhänge mit der geistigen Welt hat. Diejenigen Menschen, die nicht mehr das alte Hellsehen haben, aber in ihrer Seele noch zusammenhängen mit der geistigen Welt, füh­len einen Unterschied in der abnormen Welt der Träume in dieser Zeit des Jahres. Bedeutungsvoll wird das, was die Seele da erleben kann, bedeutungsvoll wird es, weil die Seele, wenn sie noch empfänglich ist, sich wirklich da am meisten einleben kann in die geistige Welt. Für den ganz modernen Menschen ist wirklich das Jahr in seinem Verlauf so, daß er nicht mehr besonders die einzelnen Jahreszeiten unterscheidet, denn während draußen der Schnee stürmt, die Finsternis schon um vier Uhr des Nachmittags beginnt und es spät wiederum hell wird, empfindet",
      "der Stadtmensch dasselbe wie in den Sommermonaten, wo die Sonne ihre volle Macht entfalten kann. Der Mensch ist herausgerissen aus dem alten Zusammenhange mit dem Kosmos, in dem er gelebt hat, als er in der Natur draußen war. Aber für die, welche sich einen Zu­sammenhang mit der Natur bewahrt haben, ist es nicht das gleiche, was in die Zeit des Weihnachtsfestes fällt, oder was in einer andern Zeit, zum Beispiel im Hochsommer geschieht. Während im Hochsommer die Seele am meisten emanzipiert ist von dem, was mit der geistigen Welt zusammenhängt, hängt sie in der Zeit, in welcher die Natur am meisten erstorben ist, am meisten zusammen mit der geistigen Welt und erlebte früher während dieser Zeit besondere Dinge.",
      "Nun gibt es eine schöne Volksdichtung in der alten norwegischen Sprache, eine Dichtung, die vor kurzer Zeit wieder aufgefunden wurde und durch das eigentümliche Verständnis der norwegischen Bevölke­rung schnell wieder populär geworden ist. Sie handelt von einem Men­schen, der noch einen Zusammenhang mit der geistigen Welt hatte, von Olaf Ästeson. Was Olaf Ästeson erlebt in der Zeit zwischen Weih­nachten und dem Dreikönigstage, wird in dieser Dichtung in schöner Weise dargestellt.",
      "Zunächst versuchte ich zu der Neujahrsfeier in Hannover 1912 diese Volksdichtung vom Olaf Ästeson in deutsche Zeilen zu bringen, so daß sie auch vor unsere Seelen treten kann. Es soll der heutige Abend ein­geleitet werden mit dem Gesang vom Olaf Ästeson, der die Erlebnisse Olaf Ästesons in den dreizehn Nächten enthält.",
      "Es folgte die Rezitation durch Marje von Sivers.",
      "Die Dichtung selber ist alt. Aber, wie gesagt, sie ist in der letzten Zeit im norwegischen Volke wie von selbst auferstanden und breitet sich mit großer Schnelligkeit aus. Die Tatsache, daß sich so etwas ausbreitet, wird unter vielen in der Gegenwart herrschenden Tatsachen auch eine sein, welche beweist, wie es zum Verständnisse jener Geheimnisse hin-drängt, die uns heute durch die Anthroposophie werden können. Denn daß in einer Seele so etwas, wie es hier geschildert ist, vorgeht, oder wenigstens vor verhältnismäßig kurzer Zeit vorgehen konnte, das ist nicht bloß eine «Dichtung». Diese Dichtung ist eben nicht bloß Phantasie,",
      "sondern sie ist Realität, ist Wirklichkeit. Und es wird mit Olaf Asteson hingewiesen auf Menschen jener nordischen Gegenden, welche noch im Mittelalter, etwa in der Mitte des Mittelalters, durchaus die Möglichkeit hatten, man möchte sagen, wörtlich so etwas zu erleben, wie es hier ausgedrückt ist.",
      "Als unsere norwegischen Freunde mir bei meinem vorletzten Besuch in Kristiania diese Dichtung gaben und einiges darüber von mir hören wollten, war es zunächst diese allgemein-geisteswissenschaftliche inter­essante Tatsache, die eben hervorgehoben war, was sich vor die Seelen drängte. Was aber dazu führte, daß wir überhaupt diese Dichtung so­zusagen in unser geisteswissenschaftliches Programm aufnehmen woll­ten, ist, daß man auch auf die Einzelheiten immer weiter und weiter eingehen kann.",
      "Man findet sich tatsächlich durch das anthroposo­phische Verständnis immer tiefer und tiefer in dasjenige hinein, was da in der Dichtung zutage tritt. So zum Beispiel war es mir schon bedeut­sam, daß Olaf - das ist ein alter norwegischer Name - den Beinamen Asteson hat: Ästeson.",
      "Der Sohn von was? Von Äste. Und ich versuchte herauszubekommen, von was für einer Mutter denn eigentlich dieser Sohn ist. Nun kann man natürlich über die Bedeutung des Wortes «Äst» mannigfaltige und auch solche Dinge vorbringen, über die zu streiten ist.",
      "Es ist heute auch nicht möglich, alles auseinanderzusetzen, was da­bei in Frage kommt. Aber wenn man alles berücksichtigt, was in Frage kommt, so heißt etwa Olaf Ästeson: der, der da noch ein Sohn ist jener Seele, die von Generation zu Generation heruntergeht, und mit dem Blute, das von Generation zu Generation rinnt, zusammenhängt.",
      "So haben wir diesen Namen aber zurückgeführt zu dem, was wir so oft auf anthroposophischem Felde besprochen haben, daß in alten Zeiten das alte Hellsehen zusammenhing mit der Verwandtschaft des Blutes, das durch die Generationen rinnt. Und man würde etwa Olaf Ästeson übersetzen können mit: Olaf, der aus vielen Generationen Geborene und die Charaktere aus vielen Generationen noch in der Seele Tra­gende.",
      "Wenn wir nun auf die Erlebnisse eingehen, so ist es ungeheuer inte­ressant, was der schlafende Olaf Ästeson durchmacht vom Weihnachts­abend durch dreizehn Tage, in denen er nicht aufwacht, das heißt, in",
      "einer Art von psychischem Zustande ist. Wenn man die einzelnen Stro­phen auf sich wirken läßt, die mit volkstümlicher, breiter Behaglichkeit die einzelnen Erlebnisse vor die Seele treten lassen, so wird man erin­nert an gewisse Schilderungen der ersten Stufen der Einweihung, wo es heißt, daß der und der bis an die Pforte des Todes geführt worden ist.",
      "Überall wird in dem Gedicht gezeigt, daß Olaf Ästeson bis an die Pforte des Todes kommt. Und besonders anschaulich wird es noch da­durch hervorgehen, daß er sich selber fühlt wie ein Leichnam - bis auf die Erde, die er zwischen den Zähnen fühlt.",
      "Wenn wir uns erinnern, daß beim Einzuweihenden der Atherleib über die Grenzen der Haut hinauswächst und der Mensch immer größer und größer wird, so daß sich also der Mensch hineinlebt in weite Weltenräume, so werden wir in diesem Gedicht durchaus darauf hingewiesen, wie der Mensch tief heruntersteigt, sich ein fühlt in die Erdentiefen und hinaufsteigt in Wol­kenhöhen. Was der Mensch nach dem Tode durchzumachen hat, zum Beispiel in der Sphäre des Mondes, das ist auch das, was Olaf Ästeson durchzumachen hat.",
      "Es wird poetisch dargestellt, wie der Mond hell scheint und wie sich weithin die Wege dehnen. Dann wird die Kluft dargestellt, die zu überschreiten ist in der Welt, die zwischen der menschlichen und derjenigen liegt, die hinaus in die kosmischen Wei­ten führt.",
      "Und die Himmelsbrücke verbindet das, was menschlich ist, und das, was kosmisch ist. Dann werden wir darauf aufmerksam ge­macht, wie hereinspielen die Wesenheiten, die ihren Ausdruck finden in den Sternbildern: Stier, Schlange.",
      "Aber für den, der geistig in die Welt hineinschauen kann, sind die Sternbilder nur der Ausdruck für das, was geistig in den Raumesweiten vorhanden ist. Und dann wird die Kamalokawelt dargestellt in der Schilderung von «Brooksvalin».",
      "Es wird dargestellt, wie eine Art Vergeltung stattfindet, wie dort die Menschen durchmachen - aber durchaus in ausgleichender Art -, was sie sich hier auf der Erde nicht angeeignet haben. Doch man braucht nicht etwa alle Einzelheiten dieser Dichtung deuten, das sollte man überhaupt nicht bei solchen Dichtungen.",
      "Empfinden sollte man aber, daß sie aus einer solchen Stimmung hervorgegangen sind, die eng zu­sammenhängt mit dem, was bei einem solchen Volke viel länger noch vorhanden war als bei Völkern, die mehr im Inneren der Kontinente",
      "wohnten oder mit Großstadtkultur zusammengekommen sind. Bei die­sem norwegischen Volke, das noch in seiner Volkssprache vieles hat, was hart herangeht an die Grenze der okkulten Geheimnisse, war län­ger die Möglichkeit vorhanden, die Seelen im Zusammenhange zu las­sen mit dem, was lebt und webt hinter den äußeren materiellen Er­scheinungen.",
      "Erinnern Sie sich, wie von mir auseinandergesetzt worden ist, wie der Jahreslauf seine geistige parallele Tatsachenreihe hat. Wie wir im Frühling, wenn die Pflanzen aus der Erde sprießen, wenn alles wie auflebt, wenn die Tage heller werden, das zu erkennen haben, was wir nennen können eine Art Einschlafen der elementarischen und höheren Geister, die mit der Erde verknüpft sind.",
      "Im Frühling, wenn die Erde äußerlich aufwacht, hat man es in der geistigen Betrachtung mit einer Art Einschlafen der Erde zu tun. Wenn die äußere Natur wieder er-stirbt, hat man es mit einem Aufwachen der geistigen Natur der Erde zu tun.",
      "Und wenn wie schlafend um die Weihnachtszeit herum die äußere Natur ist, dann ist das die Zeit, in welcher sozusagen das Gei­stige der Erde, das sowohl an elementaren, weniger bedeutenden We­sen wie auch an großen, gewaltigen Wesen mit dem Erdensein zusam­menhängt, am allerregsamsten ist. Nur äußerlich betrachtet, sieht es so aus, als wenn wir mit dem Aufwachen der Erde den Frühling und mit dem Einschlafen den Winter vergleichen müßten.",
      "Umgekehrt ist es für die okkulte Beobachtung. Der Geist der Erde, der aber aus vielen Gei­stern besteht, wacht auf zur Winterzeit und schläft zur Sommerzeit. Wie im Inneren der menschlichen Organismen das Organische und Ve­getabilische am regsamsten ist während des Schlafes, wie da die Kräfte hinaufspielen bis ins Gehirn, und wie die rein organische Tätigkeit während des Wachens abgetötet wird, so ist es mit der Erde.",
      "Wenn die Erde am regsamsten ist, wenn alles herausgesprossen ist, wenn die Sonne um Johanni ihren höchsten Stand hat, da schläft der Geist der Erde. Und nicht ohne Zusammenhang mit diesen okkulten Wahrheiten ist das Weihnachtsfest, das Fest des Erwachens des Geistes, gerade in die Winterzeit verlegt worden.",
      "Die Dinge, die als Gebräuche aus alten Zeiten herübergekommen sind, entsprechen vielfach diesen okkulten Einsichten.",
      "Wer nun zu leben weiß mit den Geistern der Erde, der feiert zum Beispiel das Johannifest im Sommer. Denn die Feier des Johannifestes im Sommer ist schon eine Art materialistische Feier. Man feiert, was äußere materialistische Offenbarung zeigt.",
      "Wer aber den Zusammen­hang mit dem Geiste der Erde hat, mit dem, was geistig in der Erde lebt, der wacht für sein Inneres auf, das heißt, er schläft für sein Auße­res, wie Olaf Ästeson, am besten zur Weihnachtszeit in den dreizehn Tagen. Das ist auch eine okkulte Tatsache, die für den Okkultismus genau dasselbe bedeutet wie zum Beispiel die Tatsache des äußeren Sonnenstandes für die äußere materialistische Wissenschaft.",
      "Gewiß, die materialistische Wissenschaft wird es für eine Selbstverständlich­keit halten, daß sie innerhalb der Astronomie die Tätigkeit der Sonne im Sommer und im Winter in einer gewissen Weise rein äußerlich be­schreibt, sie wird es für eine Narretei halten, was für den Okkultisten eine Tatsache ist, daß der geistige Sonnenstand am intensivsten ist in der Winterzeit und daß daher dann die Verhältnisse am günstigsten liegen für den, der einer Seelenvertiefung, die mit dem Geist der Erde und mit allem Geistigen zusammenhängt, nahekommen will. Daher kann sich für den, der eine Vertiefung seiner Seele suchen will, heraus­stellen, daß er die besten Erlebnisse in den dreizehn Tagen der Weih­nachtszeit machen kann, daß dann, ohne daß wir es merken, die Erleb­nisse aus der Seele heraufkommen, obwohl der moderne Mensch schon so dasteht, daß er emanzipiert ist von den äußeren Vorgängen, so daß die okkulten Erlebnisse jederzeit kommen können.",
      "Aber insofern das Äußere dennoch einen Einfluß haben kann, ist die Zeit zwischen Weih­nachten und Neujahr die allerwichtigste.",
      "So werden wir durch dieses Gedicht in ganz naturgemäßer Weise daran erinnert, wie manches von dem, was wir bei der Besprechung der Zeit zwischen dem Tode und der nächsten Geburt erwähnen konnten, für gewisse Gegenden der Erde verhältnismäßig vor kurzem noch recht nahelag, wie es mancher noch aus unmittelbarer Erfahrung wußte."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Die Zeit von Weihnachten bis etwa in unsere Tage herein ist tatsächlich eine wichtige, eine bedeutungsvolle Zeit des Jahres, auch in okkulter Beziehung.",
        "Man nennt sie die Zeit der dreizehn Tage.",
        "Und das Merk-würdige ist, daß diese Zeit der dreizehn Tage in ihrer Wichtigkeit von denjenigen Menschen empfunden wird, welche ihrer ganzen Seelenver­anlagung nach noch etwas zurückbehalten haben von dem alten Zu­sammenhange der Menschenseele mit der geistigen Welt, von dem wir oftmals gesprochen haben.",
        "Wir wissen, mehr als der Mensch der heu­tigen Stadtbevölkerung hat von dem Zusammenhange mit der geistigen Welt, der einmal in alten Zeiten bestanden hat, der primitive Mensch zurückbehalten, der draußen auf dem Lande oder in einer Bevölkerung lebt, die noch weniger angekränkelt ist von unserer Stadtkultur.",
        "Und da finden wir dann so manches, was in der Volkspoesie von Erlebnissen der Seele handelt, von Erlebnissen der Seele in der Zeit von Weihnacht bis zu dem Dreikönigstage, dem 6.",
        "Januar."
      ],
      [
        "Es ist dies die Zeit, in der, nachdem die Jahresfinsternis über die Erde am meisten hereingebrochen ist, unmittelbar nach der Winter­sonnenwende, wenn die Sonne wieder ihren Siegeslauf beginnt, mit dem tiefsten Eintauchen und Befreitwerden und Erlöstwerden der Natur, auch die menschliche Seele ganz besondere Erlebnisse durchmachen kann, wenn sie noch besondere Zusammenhänge mit der geistigen Welt hat.",
        "Diejenigen Menschen, die nicht mehr das alte Hellsehen haben, aber in ihrer Seele noch zusammenhängen mit der geistigen Welt, füh­len einen Unterschied in der abnormen Welt der Träume in dieser Zeit des Jahres.",
        "Bedeutungsvoll wird das, was die Seele da erleben kann, bedeutungsvoll wird es, weil die Seele, wenn sie noch empfänglich ist, sich wirklich da am meisten einleben kann in die geistige Welt.",
        "Für den ganz modernen Menschen ist wirklich das Jahr in seinem Verlauf so, daß er nicht mehr besonders die einzelnen Jahreszeiten unterscheidet, denn während draußen der Schnee stürmt, die Finsternis schon um vier Uhr des Nachmittags beginnt und es spät wiederum hell wird, empfindet"
      ],
      [
        "der Stadtmensch dasselbe wie in den Sommermonaten, wo die Sonne ihre volle Macht entfalten kann.",
        "Der Mensch ist herausgerissen aus dem alten Zusammenhange mit dem Kosmos, in dem er gelebt hat, als er in der Natur draußen war.",
        "Aber für die, welche sich einen Zu­sammenhang mit der Natur bewahrt haben, ist es nicht das gleiche, was in die Zeit des Weihnachtsfestes fällt, oder was in einer andern Zeit, zum Beispiel im Hochsommer geschieht.",
        "Während im Hochsommer die Seele am meisten emanzipiert ist von dem, was mit der geistigen Welt zusammenhängt, hängt sie in der Zeit, in welcher die Natur am meisten erstorben ist, am meisten zusammen mit der geistigen Welt und erlebte früher während dieser Zeit besondere Dinge."
      ],
      [
        "Nun gibt es eine schöne Volksdichtung in der alten norwegischen Sprache, eine Dichtung, die vor kurzer Zeit wieder aufgefunden wurde und durch das eigentümliche Verständnis der norwegischen Bevölke­rung schnell wieder populär geworden ist.",
        "Sie handelt von einem Men­schen, der noch einen Zusammenhang mit der geistigen Welt hatte, von Olaf Ästeson.",
        "Was Olaf Ästeson erlebt in der Zeit zwischen Weih­nachten und dem Dreikönigstage, wird in dieser Dichtung in schöner Weise dargestellt."
      ],
      [
        "Zunächst versuchte ich zu der Neujahrsfeier in Hannover 1912 diese Volksdichtung vom Olaf Ästeson in deutsche Zeilen zu bringen, so daß sie auch vor unsere Seelen treten kann.",
        "Es soll der heutige Abend ein­geleitet werden mit dem Gesang vom Olaf Ästeson, der die Erlebnisse Olaf Ästesons in den dreizehn Nächten enthält."
      ],
      [
        "Es folgte die Rezitation durch Marje von Sivers."
      ],
      [
        "Die Dichtung selber ist alt.",
        "Aber, wie gesagt, sie ist in der letzten Zeit im norwegischen Volke wie von selbst auferstanden und breitet sich mit großer Schnelligkeit aus.",
        "Die Tatsache, daß sich so etwas ausbreitet, wird unter vielen in der Gegenwart herrschenden Tatsachen auch eine sein, welche beweist, wie es zum Verständnisse jener Geheimnisse hin-drängt, die uns heute durch die Anthroposophie werden können.",
        "Denn daß in einer Seele so etwas, wie es hier geschildert ist, vorgeht, oder wenigstens vor verhältnismäßig kurzer Zeit vorgehen konnte, das ist nicht bloß eine «Dichtung».",
        "Diese Dichtung ist eben nicht bloß Phantasie,"
      ],
      [
        "sondern sie ist Realität, ist Wirklichkeit.",
        "Und es wird mit Olaf Asteson hingewiesen auf Menschen jener nordischen Gegenden, welche noch im Mittelalter, etwa in der Mitte des Mittelalters, durchaus die Möglichkeit hatten, man möchte sagen, wörtlich so etwas zu erleben, wie es hier ausgedrückt ist."
      ],
      [
        "Als unsere norwegischen Freunde mir bei meinem vorletzten Besuch in Kristiania diese Dichtung gaben und einiges darüber von mir hören wollten, war es zunächst diese allgemein-geisteswissenschaftliche inter­essante Tatsache, die eben hervorgehoben war, was sich vor die Seelen drängte.",
        "Was aber dazu führte, daß wir überhaupt diese Dichtung so­zusagen in unser geisteswissenschaftliches Programm aufnehmen woll­ten, ist, daß man auch auf die Einzelheiten immer weiter und weiter eingehen kann."
      ],
      [
        "Man findet sich tatsächlich durch das anthroposo­phische Verständnis immer tiefer und tiefer in dasjenige hinein, was da in der Dichtung zutage tritt.",
        "So zum Beispiel war es mir schon bedeut­sam, daß Olaf - das ist ein alter norwegischer Name - den Beinamen Asteson hat: Ästeson."
      ],
      [
        "Der Sohn von was?",
        "Von Äste.",
        "Und ich versuchte herauszubekommen, von was für einer Mutter denn eigentlich dieser Sohn ist.",
        "Nun kann man natürlich über die Bedeutung des Wortes «Äst» mannigfaltige und auch solche Dinge vorbringen, über die zu streiten ist."
      ],
      [
        "Es ist heute auch nicht möglich, alles auseinanderzusetzen, was da­bei in Frage kommt.",
        "Aber wenn man alles berücksichtigt, was in Frage kommt, so heißt etwa Olaf Ästeson: der, der da noch ein Sohn ist jener Seele, die von Generation zu Generation heruntergeht, und mit dem Blute, das von Generation zu Generation rinnt, zusammenhängt."
      ],
      [
        "So haben wir diesen Namen aber zurückgeführt zu dem, was wir so oft auf anthroposophischem Felde besprochen haben, daß in alten Zeiten das alte Hellsehen zusammenhing mit der Verwandtschaft des Blutes, das durch die Generationen rinnt.",
        "Und man würde etwa Olaf Ästeson übersetzen können mit: Olaf, der aus vielen Generationen Geborene und die Charaktere aus vielen Generationen noch in der Seele Tra­gende."
      ],
      [
        "Wenn wir nun auf die Erlebnisse eingehen, so ist es ungeheuer inte­ressant, was der schlafende Olaf Ästeson durchmacht vom Weihnachts­abend durch dreizehn Tage, in denen er nicht aufwacht, das heißt, in"
      ],
      [
        "einer Art von psychischem Zustande ist.",
        "Wenn man die einzelnen Stro­phen auf sich wirken läßt, die mit volkstümlicher, breiter Behaglichkeit die einzelnen Erlebnisse vor die Seele treten lassen, so wird man erin­nert an gewisse Schilderungen der ersten Stufen der Einweihung, wo es heißt, daß der und der bis an die Pforte des Todes geführt worden ist."
      ],
      [
        "Überall wird in dem Gedicht gezeigt, daß Olaf Ästeson bis an die Pforte des Todes kommt.",
        "Und besonders anschaulich wird es noch da­durch hervorgehen, daß er sich selber fühlt wie ein Leichnam - bis auf die Erde, die er zwischen den Zähnen fühlt."
      ],
      [
        "Wenn wir uns erinnern, daß beim Einzuweihenden der Atherleib über die Grenzen der Haut hinauswächst und der Mensch immer größer und größer wird, so daß sich also der Mensch hineinlebt in weite Weltenräume, so werden wir in diesem Gedicht durchaus darauf hingewiesen, wie der Mensch tief heruntersteigt, sich ein fühlt in die Erdentiefen und hinaufsteigt in Wol­kenhöhen.",
        "Was der Mensch nach dem Tode durchzumachen hat, zum Beispiel in der Sphäre des Mondes, das ist auch das, was Olaf Ästeson durchzumachen hat."
      ],
      [
        "Es wird poetisch dargestellt, wie der Mond hell scheint und wie sich weithin die Wege dehnen.",
        "Dann wird die Kluft dargestellt, die zu überschreiten ist in der Welt, die zwischen der menschlichen und derjenigen liegt, die hinaus in die kosmischen Wei­ten führt."
      ],
      [
        "Und die Himmelsbrücke verbindet das, was menschlich ist, und das, was kosmisch ist.",
        "Dann werden wir darauf aufmerksam ge­macht, wie hereinspielen die Wesenheiten, die ihren Ausdruck finden in den Sternbildern: Stier, Schlange."
      ],
      [
        "Aber für den, der geistig in die Welt hineinschauen kann, sind die Sternbilder nur der Ausdruck für das, was geistig in den Raumesweiten vorhanden ist.",
        "Und dann wird die Kamalokawelt dargestellt in der Schilderung von «Brooksvalin»."
      ],
      [
        "Es wird dargestellt, wie eine Art Vergeltung stattfindet, wie dort die Menschen durchmachen - aber durchaus in ausgleichender Art -, was sie sich hier auf der Erde nicht angeeignet haben.",
        "Doch man braucht nicht etwa alle Einzelheiten dieser Dichtung deuten, das sollte man überhaupt nicht bei solchen Dichtungen."
      ],
      [
        "Empfinden sollte man aber, daß sie aus einer solchen Stimmung hervorgegangen sind, die eng zu­sammenhängt mit dem, was bei einem solchen Volke viel länger noch vorhanden war als bei Völkern, die mehr im Inneren der Kontinente"
      ],
      [
        "wohnten oder mit Großstadtkultur zusammengekommen sind.",
        "Bei die­sem norwegischen Volke, das noch in seiner Volkssprache vieles hat, was hart herangeht an die Grenze der okkulten Geheimnisse, war län­ger die Möglichkeit vorhanden, die Seelen im Zusammenhange zu las­sen mit dem, was lebt und webt hinter den äußeren materiellen Er­scheinungen."
      ],
      [
        "Erinnern Sie sich, wie von mir auseinandergesetzt worden ist, wie der Jahreslauf seine geistige parallele Tatsachenreihe hat.",
        "Wie wir im Frühling, wenn die Pflanzen aus der Erde sprießen, wenn alles wie auflebt, wenn die Tage heller werden, das zu erkennen haben, was wir nennen können eine Art Einschlafen der elementarischen und höheren Geister, die mit der Erde verknüpft sind."
      ],
      [
        "Im Frühling, wenn die Erde äußerlich aufwacht, hat man es in der geistigen Betrachtung mit einer Art Einschlafen der Erde zu tun.",
        "Wenn die äußere Natur wieder er-stirbt, hat man es mit einem Aufwachen der geistigen Natur der Erde zu tun."
      ],
      [
        "Und wenn wie schlafend um die Weihnachtszeit herum die äußere Natur ist, dann ist das die Zeit, in welcher sozusagen das Gei­stige der Erde, das sowohl an elementaren, weniger bedeutenden We­sen wie auch an großen, gewaltigen Wesen mit dem Erdensein zusam­menhängt, am allerregsamsten ist.",
        "Nur äußerlich betrachtet, sieht es so aus, als wenn wir mit dem Aufwachen der Erde den Frühling und mit dem Einschlafen den Winter vergleichen müßten."
      ],
      [
        "Umgekehrt ist es für die okkulte Beobachtung.",
        "Der Geist der Erde, der aber aus vielen Gei­stern besteht, wacht auf zur Winterzeit und schläft zur Sommerzeit.",
        "Wie im Inneren der menschlichen Organismen das Organische und Ve­getabilische am regsamsten ist während des Schlafes, wie da die Kräfte hinaufspielen bis ins Gehirn, und wie die rein organische Tätigkeit während des Wachens abgetötet wird, so ist es mit der Erde."
      ],
      [
        "Wenn die Erde am regsamsten ist, wenn alles herausgesprossen ist, wenn die Sonne um Johanni ihren höchsten Stand hat, da schläft der Geist der Erde.",
        "Und nicht ohne Zusammenhang mit diesen okkulten Wahrheiten ist das Weihnachtsfest, das Fest des Erwachens des Geistes, gerade in die Winterzeit verlegt worden."
      ],
      [
        "Die Dinge, die als Gebräuche aus alten Zeiten herübergekommen sind, entsprechen vielfach diesen okkulten Einsichten."
      ],
      [
        "Wer nun zu leben weiß mit den Geistern der Erde, der feiert zum Beispiel das Johannifest im Sommer.",
        "Denn die Feier des Johannifestes im Sommer ist schon eine Art materialistische Feier.",
        "Man feiert, was äußere materialistische Offenbarung zeigt."
      ],
      [
        "Wer aber den Zusammen­hang mit dem Geiste der Erde hat, mit dem, was geistig in der Erde lebt, der wacht für sein Inneres auf, das heißt, er schläft für sein Auße­res, wie Olaf Ästeson, am besten zur Weihnachtszeit in den dreizehn Tagen.",
        "Das ist auch eine okkulte Tatsache, die für den Okkultismus genau dasselbe bedeutet wie zum Beispiel die Tatsache des äußeren Sonnenstandes für die äußere materialistische Wissenschaft."
      ],
      [
        "Gewiß, die materialistische Wissenschaft wird es für eine Selbstverständlich­keit halten, daß sie innerhalb der Astronomie die Tätigkeit der Sonne im Sommer und im Winter in einer gewissen Weise rein äußerlich be­schreibt, sie wird es für eine Narretei halten, was für den Okkultisten eine Tatsache ist, daß der geistige Sonnenstand am intensivsten ist in der Winterzeit und daß daher dann die Verhältnisse am günstigsten liegen für den, der einer Seelenvertiefung, die mit dem Geist der Erde und mit allem Geistigen zusammenhängt, nahekommen will.",
        "Daher kann sich für den, der eine Vertiefung seiner Seele suchen will, heraus­stellen, daß er die besten Erlebnisse in den dreizehn Tagen der Weih­nachtszeit machen kann, daß dann, ohne daß wir es merken, die Erleb­nisse aus der Seele heraufkommen, obwohl der moderne Mensch schon so dasteht, daß er emanzipiert ist von den äußeren Vorgängen, so daß die okkulten Erlebnisse jederzeit kommen können."
      ],
      [
        "Aber insofern das Äußere dennoch einen Einfluß haben kann, ist die Zeit zwischen Weih­nachten und Neujahr die allerwichtigste."
      ],
      [
        "So werden wir durch dieses Gedicht in ganz naturgemäßer Weise daran erinnert, wie manches von dem, was wir bei der Besprechung der Zeit zwischen dem Tode und der nächsten Geburt erwähnen konnten, für gewisse Gegenden der Erde verhältnismäßig vor kurzem noch recht nahelag, wie es mancher noch aus unmittelbarer Erfahrung wußte."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "NEUNTER VORTRAG Dornach, 31. Dezember 1914",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Wir beginnen diese Feier unseres Jahresschlusses damit, daß uns Frau Dr. Steiner die schöne norwegische Legende von Olaf Ästeson zum Vortrag bringen wird, von jenem Olaf Ästeson, der, als dieWeihnachts­zeit herannahte, in eine Art von Schlaf verfiel, welcher dreizehn Tage dauerte: die heiligen dreizehn Tage, die wir ja bei verschiedenen unse­rer Betrachtungen kennengelernt haben. Während dieses Schlafes hatte er wichtige Erlebnisse, von denen er dann, als er wieder erwachte, zu erzählen wußte.",
      "Wir haben verschiedene Betrachtungen angestellt, die uns darauf aufmerksam machen konnten, wie wir durch die geisteswissenschaft­liche Weltanschauung in einer andern Weise alte Erkenntnisschätze für die menschliche Erkenntnis wiedergewinnen, die in vergangenen Tagen gewußt worden sind von den Menschen als dasjenige, was den geistigen Welten angehört. Immer wieder und wieder werden wir durch das eine oder andere auf dieses vorweltliche Wissen von den geistigen Welten stoßen, und immer wieder werden wir daran erinnert, daß dieses Wis­sen der Vorzeit darauf beruhte, daß der Mensch vermöge seiner frü­heren Organisation in einem solchen Zusammenhang stehen konnte mit dem ganzen Weltenall und seinem Geschehen, daß, wie wir uns in unserer Sprache ausdrücken, der menschliche Mikrokosmos eintauchte in die Gesetzmäßigkeit, in das Geschehen des Makrokosmos, und daß er bei diesem Eintauchen in den Makrokosmos Erlebnisse haben konnte über Dinge, die sein Seelenleben innig angehen, die ihm aber verborgen bleiben müssen, solange er auf dem physischen Plane als Mikrokosmos wandelt und nur mit derjenigen Erkenntnis ausgestattet ist, die den Sinnen und dem an die Sinne gebundenen Verstande gegeben ist.",
      "Wir wissen ja, wie nur eine materialistische Weltanschauung des Glaubens sein kann, daß allein der Mensch innerhalb der Weltenord­nung mit einem Erkenntnis-, Gefühls- und Willensvermögen begabt sei; während man anerkennen muß vom Standpunkte einer spirituellen Weltanschauung, daß ebenso, wie es unterhalb der Menschenstufe Wesenheiten",
      "gibt, es auch Wesenheiten gibt oberhalb der menschlichen Stufe des Denkens, Fühlens und Wollens. In diese Wesenheiten kann sich der Mensch einleben, wenn er eben als Mikrokosmos im Makro-kosmos untertaucht. Wir müssen aber dann von diesem Makrokosmos so sprechen, wie wenn er nicht nur ein Raumesmakrokosmos sei, son­dern wie wenn die Zeit in ihrem Verlaufe Bedeutung habe im Leben des Makrokosmos. Wie der Mensch sich zurückziehen muß von all den Eindrücken, die auf seine Sinne ausgeübt werden können aus seiner Umgebung, wie er gleichsam um sich herum durch das Abschließen seiner Sinneswahrnehmung Finsternis erzeugen muß, um im Inneren das Licht des Geistes anzuzünden, wenn er in die Tiefen seiner Seele hinuntersteigen will, so muß derjenige Geist, den wir als den Erdgeist bezeichnen können, abgeschlossen sein von den Eindrücken des übrigen Kosmos. Es muß das geringste Maß von Wirkungen von dem äußeren Kosmos auf den Erdgeist ausgeübt werden, damit der Erdgeist selber sich innerlich konzentrieren, seine Fähigkeiten innerlich zusammen­ziehen kann. Denn dann werden die Geheimnisse entdeckt, die der Mensch deshalb durchzumachen hat mit diesem Erdgeist, weil die Erde als Erde aus dem Kosmos herausgesondert ist.",
      "Solch eine Zeit, wo das größte Maß der Eindrücke vom äußeren Makrokosmos auf die Erde ausgeübt wird, ist die Sommersonnenwende­zeit, die Johannizeit. Es erinnern uns daher viele Nachrichten aus alten Zeiten, die an Festesdarstellungen und Festesbegehungen anknüpfen, wie solche Feste inmitten der Sommerzeit stattfanden, wie die Seele in der Mitte des Sommers dadurch, daß sie sich des Ich entäußert und auf­geht im Leben des Makrokosmos, trunken hingegeben ist den Eindrük­ken vom Makrokosmos.",
      "Aber umgekehrt erinnern uns die legendarischen oder sonstigen Dar­stellungen desjenigen, was in der Vorzeit erlebt werden konnte, dann, wenn das geringste Maß der Eindrücke vom Makrokosmos zur Erde kommt, daran, daß der Erdgeist, in sich konzentriert, die Geheimnisse des Erdenseelenlebens im unendlichen All erlebt, und daß der Mensch, wenn er sich hineinbegibt in dieses Erleben zu der Zeit, in welcher am wenigsten Licht und Wärme gesendet wird aus dem Makrokosmos zur Erde, dann die heiligsten Geheimnisse miterlebt. Daher wurden diese",
      "Tage um die Weihnachtszeit herum immer so heilig gehalten, weil der Mensch, als er in seinem Organismus noch die Fähigkeit hatte, mitzu­erleben das Erdenerleben in der Zeit, wo es am konzentriertesten ist, mit dem Erdgeist zusammensein konnte.",
      "Olaf Ästeson, Olaf der Erdensohn, erlebt in diesen dreizehn kür­zesten Tagen, indem er entrückt ist in den Makrokosmos, mancherlei Geheimnisse des Weltenalls. Und die nordische Legende, die in neuerer Zeit wieder ausgegraben worden ist aus alten Nachrichten, berichtet uns von den Erlebnissen, die Olaf Ästeson hatte zwischen der Weih­nachts- und Neujahrszeit bis zum 6. Januar. Und wir haben wohl Ver­anlassung, meine lieben Freunde, öfter zu gedenken dieser alten Art des Einlebens des Mikrokosmos in den Makrokosmos; unsere Betrach­tung wird ja an solche Dinge dann anknüpfen können. Vorerst aber wollen wir hören die Legende von Olaf dem Erdensohn, der in der Zeit, in der wir jetzt sind, die Geheimnisse des Weltendaseins erlebte da­durch, daß er mit dem Erdgeist zusammenlebte. Hören wir also diese Erlebnisse.",
      "Es folgte die Rezitation.",
      "Meine lieben Freunde, wir haben gehört, wie Olaf Ästeson entschlief in jenem Schlaf, der für ihn eine Offenbarung werden sollte der Ge­heimnisse derjenigen Welten, die dem Sinnenleben, dem gewöhnlichen Leben auf dem physischen Plane entzogen sind. Wir haben in der Le­gende erhalten die Kunde von jenen alten Erkenntnissen, von jenen alten Einsichten in die geistigen Welten, die wiedererrungen werden sollen durch dasjenige, was wir die geisteswissenschaftliche Weltan­schauung nennen.",
      "Oftmals ist angeführt worden der Ausspruch, der durch alle Kund­gebungen hindurchgeht, die von dem Eintritt der Menschenseele in die geistige Welt handeln, und der da besagt, daß der Mensch erst dann die geistige Welt schauen kann, wenn er mit seinem Erleben an die Pforte des Todes kommt und dann untertaucht in die Elemente. So daß er die Elemente des Erdendaseins nicht sÖ um sich herum hat, wie sie im gewöhnlichen Leben des physischen Planes um ihn herum sind als die Erde, das Wasser, die Luft, das Feuer, sondern daß er herausgehoben",
      "ist über diese Außenseite, diese sinnliche Außenseite der Ele­mente, und untertaucht in dasjenige, was diese Elemente sind, wenn man sie ihrer wahren Natur, ihrer nächst wahren Natur nach kennen-lernt, wo Wesen in ihnen anwesend sind, die im Zusammenhange ste­hen mit dem Erleben der Menschenseele.",
      "Daß Olaf Ästeson etwas von diesem Untertauchen in die Elemente erlebte, man konnte es noch nachspüren da, wo zunächst erzählt wird, wie Olaf an die Gjallarbrücke kommt, und wie er über die Brücke wandelt in den Wegen der geistigen Welt, die weithin sich dehnen. Wie anschaulich wird uns geschildert das Erlebnis mit dem Erdenelement, wird dargestellt, wie er in das Erdenelement eintaucht. Das wird bis zu jener Anschaulichkeit gebracht, die uns sagt, daß er wie Tote, die in Gräbern liegen, selbst Erde im Munde fühlt. Und deutlich wird uns dann angedeutet, wie er das Wasserelement durchlebt und alles das­jenige, was im Wasserelement erlebt werden kann, wenn man dieses Wasserelement zugleich mit seinem moralischen Inhalt erlebt. Dann wiederum wird angedeutet, wie der Mensch zusammenkommt mit dem Feuerelement, mit dem Luftelement.",
      "Das alles ist in einer wunderbar anschaulichen Weise geschildert und zusammengebracht in dem Erleben des Zusammenseins der Men­schenseele mit den Geheimnissen der geistigen Welt. Die Legende ist später aufgefunden worden; sie ist gesammelt worden da, wo sie noch lebte im Munde des Volkes. Und es ist manches in dieser Legende, so wie sie heute ist, nicht mehr so, wie es ursprünglich war. Ursprüng­lich war ohne Zweifel erst die anschauliche' Schilderung der Erleb­nisse im Erdengebiete, dann der Erlebnisse im Wassergebiete. Und dann waren die Erlebnisse im Luft- und im Feuergebiete wohl noch viel differenzierter, als es der Fall ist in dem schwachen Nachklange, der nach Jahrhunderten aufgefunden worden ist und der uns heute vorliegt.",
      "Ebenso war zweifellos viel großartiger und weniger sentimental der Schluß, der gar nicht mehr, so wie er heute dasteht, an die ursprüng­lich ungeheuer grandiose Sprache erinnert, an das übermenschlich Er­greifende, das in solchen Volkslegenden lag, während der heutige Schluß eben nur menschlich ergreifend ist; ergreifend deshalb, weil er",
      "mit so tiefen Geheimnissen des Makrokosmos und des menschlichen Er-lebens im Zusammenhange steht.",
      "In solchen Zeiten, wie diejenige ist, in der wir jetzt leben, in solchen Jahreszeiten, wenn wir sie richtig verstehen, ist viel Veranlassung ge­geben, zu gedenken der Tatsache, daß die Menschheit - allerdings mit einem andersgearteten, mehr dumpfen, dämmerigen Erkennen - in der Vorzeit durchdrungen war von einem Wissen, das verlorengegangen ist und das wiedererrungen werden muß. Und da kann vor unsere Seele die Frage wiederum hintreten: Müssen wir es nicht, da wir heute schon erkennen können, wie ein solches Wissen wiederum zum Heil der Menschheit kommen muß, als eine unserer dringendsten Aufgaben be­trachten, alles zu tun, was ein solches Wissen herbeiführen kann, was die jetzige Menschheitskultur mit einem solchen Wissen durchdringen kann?",
      "Mancherlei wird notwendig sein, damit in der richtigen Weise die­ser eben angedeutete Umschwung im ganzen menschlichen, ich möchte jetzt sagen, Weltanschauungsfühlen eintreten kann. Vor allen Dingen wird eines notwendig sein; eines sage ich, denn es ist eines unter vielen; aber man kann immer nur eines nehmen. Notwendig wird sein, daß sich die Menschenseelen aneignen auf dem Boden unserer geisteswissen­schaftlichen Weltanschauungsströmung Ehrfurcht und Hingebung ge­genüber dem, was in uralten Zeiten in alter Art gewußt worden ist von den großen Geheimnissen des Daseins. Zu der Empfindung wird man gelangen müssen, wie es in den materialistischen Zeiten versäumt worden ist, diese Ehrfurcht und diese Hingebung in der Seele zu ent­wickeln.",
      "Eine Empfindung wird man davon bekommen müssen, wie trok­ken und nüchtern diese materialistische Zeit ist, und wie hochmütig auf die Verstandeserkenntnis die Menschheit in den ersten Jahrhunder­ten der fünften nachatlantischen Kulturperiode dagestanden hat vor den Offenbarungen alter Religions- und alter Wissensüberlieferungen, die wahrhaftig, wenn man mit der nötigen Ehrfurcht ihnen naht, ahnen lassen, daß tiefe, tiefe Weisheit in ihnen ruht. Wie ehrfurchtslos im Grunde genommen stehen wir heute auch vor der Bibel! Ich will gar nicht sprechen von jener Art moderner Greuelforschung, welche die",
      "ganze Bibel zerzaust und zerfasert. Ich will nur sprechen von der nüch­ternen, trockenen Art, wie wir heute, gleichsam ausgerüstet nur mit Sinnenerkenntnis und den gewöhnlichen Verstandeskräften, uns der Bibel nahen, und wie wir nicht mehr eine Empfindung aufbringen können für die ungeheure Größe menschlicher Anschauung, die aus manchen Stellen uns entgegentritt. Auf eine Stelle aus dem 2. Moses-buche, 33. Kapitel, Vers 18, möchte ich hinweisen: Und Moses spricht zu Gott: «Zeige mir doch die Gestalt deiner Offenbarung.»",
      "Worauf Jehova sprach: «Ich will vorüberziehen lassen alle meine Güte an deinem Angesicht, und ich will rufen den Namen Jehovas vor dir und will gnadevoll sein dem, den ich begnaden darf, und will Erbarmen üben mit dem, mit dem ich Erbarmen üben darf.»",
      "Dann aber spricht Jehova: «Du kannst mein Antlitz nicht sehen, denn mich sieht kein Mensch, der dann noch lebend bleiben kann.»",
      "Und es spricht Jahve: «Hier ist ein Ort bei mir, stelle dich auf den Felsen, und wenn meine Herrlichkeit vorüberzieht, so will ich dich in eine Höhlung des Felsens stellen und meine Hand über dich decken, bis ich vorüber bin. Wenn ich dann meine Hand entferne, so wirst du meine Rückseite sehen, aber mein Antlitz kann nicht geschaut werden.»",
      "Wenn man zusammennimmt so manches, was in den verflossenen Jahren unseres geisteswissenschaftlichen Strebens in unsere Seelen und unsere Herzen hineinziehen konnte, und sich naht dieser Stelle, dann kann man die Empfindung haben: Ja, was spricht denn da für eine unendliche Weisheit aus dieser Stelle, und wie taub sind die Menschen-ohren des materialistischen Zeitalters, daß s'ie so gar nichts vernehmen können von der unendlich tiefen Weisheit, die aus dieser Stelle spricht. -Ich möchte zugleich die Gelegenheit ergreifen, Sie hinzuweisen auf ein Büchelchen, das erschienen ist mit dem Titel: «Worte Mosis» in Bruns' Verlag in Minden in Westfalen, und zwar deshalb, weil manches in die­sem Büchelchen aus den Fünf Büchern Moses besser übersetzt ist als in andern Ausgaben. Es hat sich da Dr. Hugo Bergmann, welcher der Herausgeber der «Worte Mosis» ist, für die Interpretation viele Mühe gegeben.",
      "Daß im Grunde genommen der Mensch sich aneignen müsse eine ganz andere Art des Sich-Verhaltens zur Welt, wenn er in die geistigen Welten",
      "eintauchen will, als das Verhalten zur Sinneswelt ist, das haben wir öfter hervorgehoben. Die Sinneswelt hat der Mensch um sich. Er schaut hin auf die Sinneswelt, er sieht sie in ihren Farben und Formen, hört ihre Töne. Die Sinneswelt ist da; wir stehen ihr gegenüber; sie wirkt auf uns; wir nehmen sie in der Wahrnehmung auf, wir denken über sie nach. So ist unser Verhalten zur Sinneswelt. Wir sind passiv; sie arbei­tet sich gleichsam in unsere Seele hinein. Wir denken über die Sinnes-welt, wir stellen die Sin'neswelt vor.",
      "Ganz anders ist unser Verhalten, wenn wir uns hinaufleben in die geistige Welt. Darin besteht eine der Schwierigkeiten, richtige Vorstel­lungen zu gewinnen über das, was der Mensch erlebt, wenn er in die geistige Welt eintritt.",
      "Ich habe versucht, einige dieser Schwierigkeiten zu charakterisieren in dem Büchelchen: «Die Schwelle der geistigen Welt.» Wir stellen die Sinneswelt vor, wir denken über die Sinneswelt. Wenn wir alles das durchmachen, was derjenige durchzumachen hat, der den Pfad der Initiation gehen will, dann tritt etwas ein, was man so charakterisieren kann: Wie die Dinge um uns herum sich zu uns ver­halten, so verhalten wir uns selber zu den Wesenheiten der höheren Hierarchien: die stellen uns vor, die denken uns.",
      "Wir denken die Ge­genstände außer uns, die Mineralien, Pflanzen und Tiere: sie werden unsere Gedanken. Wir wiederum sind die Vorstellungen, Gedanken und Wahrnehmungen der Geister der höheren Hierarchien.",
      "Wir wer­den zu den Gedanken der Angeloi, Archangeloi, Archai und so weiter. Wir werden aufgenommen von ihnen, wie wir selber aufnehmen die Pflanzen, Tiere und Menschen. Und wir müssen uns geborgen fühlen, indem wir uns sagen können: Es denken uns die Wesen der höheren Hierarchien, sie stellen uns vor.",
      "Diese Wesen der höheren Hierarchien ergreifen uns mit ihren Seelen. - Ja, wir können uns geradezu vor­stellen: indem jener Olaf Ästeson vor dem Kirchentor einschlief, wurde er eine Vorstellung der Geister der höheren Hierarchien, und während er schlief, erlebten die Wesen der höheren Hierarchien dasjenige, was erleben die Wesen des Erdgeistes, der für uns ja eine Pluralität ist. Und indem Olaf Ästeson wieder heruntersinkt in die physische Welt, er­innert er sich an dasjenige, was die Geister der höheren Hierarchien in ihm erlebt haben.",
      "Stellen wir uns einmal vor: wir begeben uns auf den Pfad der Ini­tiation! Wie können wir uns verhalten zu den geistigen Welten, in die wir als in eine Summe von geistigen Wesenheiten der höheren Hier­archien unseren Einzug halten wollen? Wie können wir uns zu ihnen verhalten? - Wir können sie ansprechen und können zu ihnen sagen: Wie gelangen wir in Euch hinein, wie offenbart Ihr Euch uns? - Und dann, wenn wir Verständnis gewonnen haben für die andere Art des Verhaltens der Menschenseele zu den höheren Welten, wird uns ge­wissermaßen entgegentönen aus den geistigen Welten: Ja, so wie du die Sinneswelt wahrnimmst, daß sie vor deinem Blicke erscheint, vor deinen Sinnen auftritt, so kannst du die geistige Welt nicht wahrneh­men. Wir müssen dich vorstellen, und du mußt dich in uns empfinden. Du mußt dich so empfinden, wie der Gedanke, den du in der Sinnes-welt denkst, sich erleben würde, wenn er sich in dir erleben könnte. Du mußt dich hingeben der geistigen Welt, dann wird in dich einziehen alles das, was sich dir offenbaren kann an Wesenheiten der höheren Hierarchien. Dann wird es in deine Seele einfließen und gnadevoll in deiner Seele leben, wie du in deinen Gedanken lebst, wenn du über die Sinneswelt denkst. Wenn dich die geistige Welt begnadigen will, dann wird sie dich durchdringen mit ihrer Liebe! Wenn sie sich deiner er­barmen und dich mit ihrer Liebe durchdringen will.",
      "Denn du mußt nicht glauben, daß du dich den geistigen Wesen so gegenüberstellen kannst wie der sinnlichen Welt. Wie Moses in die Höhlung gehen mußte, so mußt du in die Höhlung der geistigen Welt dich hineinbegeben. Du mußt dich da hineinstellen. Wie der Gedanke in dir lebt, so mußt du dich in die geistigen Wesen hineinleben. Du mußt selber alsweltgedanke in dem Makrokosmos darinnen leben. Das, was du so erlebst, von selbst zu erleben, das kannst du nicht während deines Erdenlebens zwischen der Geburt und dem Tode; das kannst du nur nach dem Tode, wenn du gestorben bist. Niemand kann die geistige Welt so erleben, bevor er gestorben ist, aber vorüberziehen kann an dir die geistige Welt, dich begnadigen, dich mit ihrer Liebe durchfluten. Und dann, wenn du nachher oder während du darinnen bist in dieser geistigen Welt, dein Erdenbewußtsein entwickelst, dann erglänzt dir herein in dein Erdenbewußtsein dasjenige, was die geistige Welt ist.",
      "Wie der Gegenstand draußen ist und der Mensch gegenübersteht dem Gegenstande, wie der Gegenstand hineinragt in sein Bewußtsein und dann darinnen ist, so ist der Mensch mit seiner Seele in der Höh­lung der geistigen Welt. Die geistige Welt zieht durch ihn durch. Hier ist der Mensch vor den Dingen. Wenn der Mensch eingeht in die gei­stige Welt, sind die Wesenheiten der höheren Hierarchien hinter ihm. Da kann er nicht ihr Angesicht sehen, so wie die Gedanken nicht unser Antlitz sehen, wenn sie in uns sind. Das Antlitz ist vorn; die Gedanken sind dahinter, sie sehen nicht das Antlitz. Das ganze Geheimnis der Initiation ruht in den Worten, die Jahve zu Moses spricht.",
      "Und Moses spricht zu Gott: «Zeige mir doch die Gestalt deiner Offenbarung.»",
      "Worauf Jehova sprach: «Ich will vorüberziehen lassen alle meine Güte an deinem Angesicht, und ich will rufen den Namen Jehovas vor dir und will gnadevoll sein dem, den ich begnaden darf, und will Er­barmen üben mit dem, mit dem ich Erbarmen üben darf.»",
      "Dann aber spricht Jehova: «Du kannst mein Antlitz nicht sehen, denn mich sieht kein Mensch, der dann noch lebend bleiben kann.»",
      "An die Pforte des Todes kommt man ja durch die Initiation.",
      "Und es spricht Jahve: «Hier ist ein Ort bei mir, stelle dich auf den Felsen, und wenn meine Herrlichkeit vorüberzieht, so will ich dich in eine Höhlung des Felsens stellen und meine Hand über dich decken, bis ich vorüber bin. Wenn ich dann meine Hand entferne, so wirst du meine Rückseite sehen, aber mein Antlitz kann nicht geschaut werden.»",
      "Es ist die entgegengesetzte Art, wie man die Sinneswelt wahr­nimmt. Man muß vieles von dem, was man sich durch Jahre hindurch erwirbt an geisteswissenschaftlichem Streben, aufbringen, um in der richtigen Weise in Ehrfurcht und Hingabe vor einer solchen Offen­barung zu stehen. Dann aber kommt allmählich immer mehr und mehr dieses Gefühl der Ehrfurcht gegenüber diesen Offenbarungen in die Menschenseele hinein, und unter dem mancherlei, was wir brauchen, damit der angedeutete Umschwung in der geistigen Menschheitskultur hervortreten kann, ist diese Ehrfurcht, diese Hingebung.",
      "Die Zeit, in welcher das geringste Maß von Eindrücken aus dem Makrokosmos zur Erde kommt, die Zeit von Weihnachten bis über das",
      "Neujahr hinaus, ungefähr bis zum 6. Januar, ist wohl geeignet, daß man sich nicht nur erinnere an das Gegenständliche der geistigen Er­kenntnis, sondern an die Empfindungen, die wir in uns entwickeln müssen durch das Aufnehmen der Geisteswissenschaft. Wahrhaft leben wir uns also wieder hinein in den Erdgeist, mit dem wir zusammen doch eine Ganzheit bilden, und mit dem lebte das alte, hellseherische Erkennen, wie es uns etwa in dieser Legende von Olaf Ästeson darge­stellt ist. Ehrfurcht und Hingebung gegenüber dem geistigen Leben hat die Menschheit des materialistischen Zeitalters vielfach verlernt. Not­wendig ist es vor allen Dingen, darauf zu achten, daß diese Ehrfurcht und diese Hingebung wiederum kommt, denn nur dadurch werden wir die Stimmung entwickeln können, die uns auch in der richtigen Weise an die neue Geisteswissenschaft heranbringt. Vorerst ist immer noch jene Stimmung da, welche an diese Geisteswissenschaft so herantritt, wie man an die andere, gewöhnliche Wissenschaft herantritt. In dieser Beziehung muß aber eine gründliche Umkehr stattfinden.",
      "Dadurch, daß der Menschheit verlorengegangen ist die Einsicht in die geistige Welt, ist auch verlorengegangen das richtige Verhältnis des Menschen zum ganzen Menschenwesen, zur Menschheit. Die materia­listische Weltanschauung erzeugt chaotische Empfindungen über das Weltendasein. Diese chaotischen Empfindungen über das Welt- und Menschheitsdasein mußten hereinbrechen in der Zeit des Materialismus. Nehmen wir eine Zeit - und diese Zeit ist die unsrige: es sind die ersten Jahrhunderte der fünften nachatlantischen Kulturperiode -, wo man so gar keine wirkliche Ahnung mehr davon hatte, daß des Menschen Wesen ein dreifaches ist: das leibliche, das seelische und das geistige Wesen. Denn wahrhaftig, so ist es. Dasjenige, was für uns schon zu den ersten Elementen des geisteswissenschaftlichen Erkennens gehören muß: die Dreigliederung des Menschen in Leib, Seele und Geist, es fehlte von den ersten vier Jahrhunderten der fünften nachatlantischen Kulturperiode an bis in unsere Zeit hinein jede Ahnung davon. Der Mensch war eben Mensch, und alles Sprechen über eine menschliche Gliederung von der Art, wie wir sie haben in Leib, Seele und Geist, galt als törichte, phantastische Rederei.",
      "Man könnte glauben, daß diese Dinge nur bedeutsam sind für die",
      "Erkenntnis. Das sind sie aber nicht. Sie sind nicht allein bedeutsam für die Erkenntnis, sondern sie sind auch bedeutsam für die ganze Art, wie sich der Mensch in das Leben hineinstellt. Im dritten Jahrhundert der neuzeitlichen Entwickelung oder auch, wie wir in unserer Sprache sagen, der Entwickelung der fünften nachatlantischen Kulturperiode, brachen in diese Zeit hinein drei gewaltige Worte, in denen gewisser­maßen verstand oder wenigstens zu verstehen versuchte diese Zeit das Zentrum menschlichen Wollens im Erdenerleben. Drei Worte, die be­deutsam sind, die aber ihre Eigentümlichkeit erhielten dadurch, daß sie in der Zeit in die Menschheit hineinbrachen, in welcher man nichts wußte von der Dreigliederung der menschlichen Natur. Die Mensch­heit hörte von Freiheit, Gleichheit und Brüderlichkeit.",
      "Daß diese Worte hineintönten in einer bestimmten Zeit in die neu­zeitliche Kultur, war eine tiefe Notwendigkeit. Verstehen wird man diese Worte wirklich erst, wenn man die dreifache Gliederung der menschlichen Natur verstehen wird, weil man dann erst wissen wird, welche Bedeutung diese Worte für die Menschennatur, im wahren Sinne des Wortes, haben können. Solange man mit jenen chaotischen Empfindungen diese drei Worte erfüllt, die da ausgehen von dem Ge­danken: Mensch ist Mensch, und die Dreigliederung des Menschen ist ein törichtes Wahngebilde - so lange kann der Mensch auch nicht inner­halb des Gebietes der Richtlinie dieser drei Worte sich zurechtfinden. Denn so, wie uns die drei Worte entgegentreten, können sie nicht un­mittelbar, man möchte sagen, auf gleichen Niveauflächen des mensch­lichen Erlebens angewendet werden. Das können sie nicht. Einfache Erwägungen, die Ihnen vielleicht deshalb, weil sie so einfach sind, nicht gleich in dem Schwerwiegenden, das sie bedeuten, vor das Seelenauge treten werden, können Ihnen andeuten, wie auf der gleichen Niveau-fläche des Lebens das, was diese drei Worte bedeuten, in ernste Lebens-konflikte geraten kann.",
      "Nehmen wir zunächst das Gebiet, in dem uns auf die natürlichste Weise der Welt die Brüderlichkeit entgegentritt. Nehmen wir die menschliche Blutsverwandtschaft, die Familie, wo wir die Brüderlich­keit nicht erst herzustellen brauchen, wo sie dem Menschen naturge­mäß angeboren ist, und bedenken wir, wie es zu unseren Empfindungen",
      "spricht, wenn wir sehen können, daß in einer Familie echte, wahre Brüderlichkeit herrscht, daß alles brüderlich verbunden ist. Aber jetzt -ohne daß wir in geringstem Maße etwas zu dämpfen brauchen von der wundervollen Empfindung, die wir von dieser Brüderlichkeit haben können - werfen wir den Blick hinein, um zu sehen, was innerhalb der Brüderlichkeit der Familie entstehen kann, gerade wegen der Brüder­lichkeit der Familie. Ein Glied kann in der Familie sein, welches sich gerade wegen der innerhalb der Familie gerechtfertigten Brüderlichkeit nicht wohl fühlt, sich heraussehnt aus der Brüderlichkeit der Familie, weil es fühlt, daß es die Seele nicht entfalten kann in der Brüderlich­keit der Familie, weil es fühlt, daß es heraus muß zur freien Entfaltung der Seele aus der Familie, in der es so brüderlich leben kann. Wir sehen:",
      "die Freiheit, die freie Entfaltung des Seelenlebens, kann in Konflikt kommen mit der allerbestgemeinten Brüderlichkeit.",
      "Selbstverständlich kann der Oberflächling sagen, das wäre nicht die rechte Brüderlichkeit, die mit der Freiheit einer Seele innerhalb der Brüderlichkeit sich nicht verträgt. Aber sagen kann man alles, was sich vorstellen läßt. Man kann sagen, daß sich alles miteinander ver­trägt, daran ist ja gar kein Zweifel. Ich habe neulich einmal eine Dis­sertation in die Hand bekommen. Unter den Thesen, die da zu ver­teidigen waren, war die These aufgestellt: Ein Dreieck ist ein Viereck. Man kann natürlich auch das verteidigen - ja, man kann es sogar streng beweisen, daß ein Dreieck ein Viereck ist! So kann man auch voll bewei­sen, daß Brüderlichkeit und Freiheit vereinbar sind. Aber darum han­delt es sich nicht, sondern es handelt sich darum, wie um der Freiheit willen manches Gebiet der Brüderlichkeit verlassen werden muß und auch verlassen wird. So könnten wir noch manches andere anführen.",
      "Wenn man die Diskrepanzen zwischen Brüderlichkeit und Gleich­heit aufzählen wollte, so würde man sehr lange darüber reden müssen. Selbstverständlich, in abstracto kann man sich wieder vorstellen: alle können gleich sein, und kann zeigen, daß sich Brüderlichkeit und Gleichheit vertragen. Aber es handelt sich nicht um Abstraktionen, sondern um die Beobachtung der Wirklichkeit, wenn wir es mit dem Leben ernst und ehrlich nehmen. In dem Augenblicke, da wir wissen, daß die menschliche Wesenheit aus dem Leiblichen, das auf dem physischen",
      "Plane sich auslebt, besteht, aus dem Seelischen, das in der See­lenwelt eigentlich sich auslebt, und aus dem Geistigen, das in der gei­stigen Welt sich auslebt, in diesem Augenblicke eröffnet sich auch die richtige Perspektive für den Zusammenhang der drei gewaltigen Worte, die wir angeführt haben. Brüderlichkeit ist das wichtigste Ideal für die physische Welt. Freiheit für die Seelenwelt, und - insofern der Mensch in der Seelenwelt darinnensteht, sollte man sprechen von der Freiheit der Seele, das heißt von einem solchen sozialen Zustande, welcher der Freiheit der Seele volle Gewähr leistet. Und wenn man bedenkt, daß wir, jeder von uns, streben müssen von unserem individuellen Stand­punkte aus nach Geist-Erkenntnis, nach der Entwickelung unseres Geistes, um mit dem Geiste im Geisterland darinnenzustehen, so wird uns sehr bald vor das geistige Auge treten, wohin wir kämen mit unse­rer Geistauffassung, wenn jeder nur auf seinem eigenen Wege suchte und jeder zu einem ganz andern Geistesinhalt käme.",
      "Wir können uns überhaupt als Menschen nur im Leben zusammen­finden, wenn wir - jeder für sich selber - den Geist suchen und zuletzt zu einem gleichen geistigen Inhalte kommen können. Von der Gleich­heit des Geisteslebens kann gesprochen werden. Von Brüderlichkeit auf dem phyischen Plane und in bezug auf alles das, was mit den Ge­setzen des physischen Planes zusammenhängt und in die Menschen­seele sich hineinlebt von dem physischen Plane aus. Freiheit in bezug auf alles das, was sich als Gesetze der Seelenwelt in die menschliche Seele hineinlebt; Gleichheit in bezug auf alles, was von den Gesetzen des Geisterlandes in die menschliche Seele sich hineinlebt.",
      "Sie sehen, ein Weltenneujahr muß angehen, in dem eine Sonne wach­sen wird in bezug auf ihre wärmende und leuchtende Kraft: jene Sonne, welche für manches, was in der Zeit der Verdunkelung zwar lebt, aber unverstanden lebt, die leuchtende Wärme geben muß. Das ist gerade das Eigentümliche unserer Zeit, daß manches erstrebt, manches aus­gesprochen wird, ohne daß es verstanden wird.",
      "Aber auch dieses kann uns zur Ehrfurcht führen und zur Hingebung gegenüber der geistigen Welt. Denn wenn wir bedenken, daß viele im dritten Jahrhundert der fünften nachatlantischen Periode die Worte Brüderlichkeit, Freiheit und Gleichheit erstrebten und ausgesprochen",
      "haben, ohne daß sie im Grunde genommen verstanden wurden, dann haben wir schon die Möglichkeit, zu verstehen und eine Antwort zu finden auf die Frage: Woher also sind diese Worte gekommen? Die göttlich-geistige Weltenordnung hat sie zunächst im voraus der noch nicht verstehenden Menschenseele eingeimpft, damit sich diese an sol­chen Leitworten hinaufranke zum wahren Weltverständnis. Selbst in solchen Tatsachen können wir die weisheitsvolle Führung in der Wel­tenevolution beobachten. In uns mehr oder weniger fern- oder nahe­liegenden Zeiten können wir überall diese Führung beobachten; beob­achten, wie wir oftmals erst hinterher einsehen, daß das, was wir vor­her gemacht haben, eigentlich weisheitsvoller war, als wir es mit der damaligen Weisheit, die wir beherrscht haben, hätten machen können. Ich habe darauf aufmerksam gemacht gleich im Beginne meiner Schrift über «Die geistige Führung des Menschen und der Menschheit».",
      "Aber wenn Sie so etwas nehmen wie die Tatsache, daß in die Welt-entwickelung, in die Entwickelung des Menschen hineinfallen Rich­tungsworte, die erst nach und nach verstanden werden können, dann werden Sie wohl aufmerksam werden auf ein Bild, das man gebrauchen kann, wenn man diese abgelaufene Periode der fünften nachatlanti­schen Kulturepoche charakterisieren will. Sie ist nämlich wirklich in bezug auf gewisse Dinge zu vergleichen mit der Zeit des Advents, wo die Zeiten des Tageslichtes immer kürzer und kürzer werden. Und nun tritt die Entwickelung in dieser unserer Zeit, in der wir wiederum etwas wissen können von den Offenbarungen der geistigen Welt, in die Phase ein, in der wir die Vorstellung gewinnen können, daß die licht-vollen Zeiten länger und länger werden und wir davon sprechen kön­nen, daß uns dieser Zeitenlauf wirklich analog erscheinen kann den dreizehn Tagen und dem Wiederhineinleben in die wieder wachsenden Tage.",
      "Aber die Sache geht noch tiefer. Es ist nicht richtig, ganz und gar nicht richtig, wenn wir nur böse Worte finden für die materialistische Zeit der letzten vier Jahrhunderte. Es kam ja diese neue Zeit dadurch herauf, daß man die großen Entdeckungen und Erfindungen machte, wie man sie eben «groß» nennt im materialistischen Zeitalter, zum Bei­spiel, daß man die Erde umschiffte, Länder entdeckte, die man früher",
      "nicht gekannt hat, daß man begann, die Erde zu kolonisieren. Das war der Beginn der materiellen Kultur. Und dann rückte nach und nach die Zeit heran, in der man fast erstickte in der materiellen Kultur. Die Zeit kam herauf, wo man alles, was man an geistigen Kräften hatte, zum Begreifen und Erfassen des materiellen Lebens anwendete. Immer mehr und mehr wurde vergessen, wie wir gesehen haben, dasjenige, was an Einblicken und Einsichten, an Schauungen in die geistige Welt aus alten Erkenntnissen vorhanden war.",
      "Aber es ist nicht richtig, wenn man nur böse Worte für die materia­listische Zeit hat. Richtig ist vielmehr ein anderes; richtig ist, wenn man bedenkt, daß diese Menschenseele in ihrem wachen Teile materia­listisch gedacht, materialistisch gesonnen hat, daß sie materialistisch die Wissenschaft und die Kultur begründet hat, daß aber diese Men­schenseele ein Ganzes ist. Man könnte sagen: der eine Teil der Men­schenseele begründete die materialistische Kultur. Früher war dieser Teil untätig, die Menschen wußten nichts von äußerer Wissenschaft, wußten nichts von äußerlichem, materiellem Leben; da war der spiri­tuelle Teil mehr wach. (Es wurde gezeichnet.) In den letzten vier Jahr­hunderten war gerade jener Teil wach, der die materialistische Kultur begründete; der andere aber hat geschlafen; er schlief, dieser andere Teil der Menschenseele. Und wahrhaftig, das, was wir jetzt an Kräften entwickeln in der Menschheit, um uns wieder hinaufzuarbeiten zur Spiritualität, ist veranlagt worden in der Zeit der materialistischen Kul­tur in den Seelengliedern, die unten geschlafen haben. Die «Menschheit» war wirklich in bezug auf die Geist-Erkenntnis in diesen Zeiten: Olaf Ästeson. Das war sie wirklich. Nur ist sie noch nicht erwacht, diese Menschheit! Die Geisteswissenschaft muß sie zum Erwachen bringen.",
      "Die Zeit muß kommen, wo junge und auch alte Leute Worte hören, die gesprochen werden aus dem Teil der Menschenseele heraus, der geschlafen hat in der finsteren Zeit. Gar lange hat diese Menschenseele also geschlafen, aber es werden die Weltengeister an diese Menschen-seele herantreten und ihr schon zurufen: Erwache nun, 0 Olaf Äste­son! - Wir müssen uns nur in der richtigen Weise vorbereiten, daß wir nicht vor den Ruf gestellt werden: Erwache nun, 0 Olaf Ästeson! -und nicht Ohren haben, zu hören. Dazu betreiben wir eben die Geisteswissenschaft,",
      "daß wir Ohren haben, wenn der Ruf nach dem spirituel­len Wachsein in der Menschheitsentwickelung ertönen wird.",
      "Es ist gut, wenn der Mensch manchmal sich erinnert, daß er ein Mikrokosmos ist und daß ihm manches werden kann an Erlebnissen, wenn er in dem Makrokosmos aufgeht. Und wir haben gesehen: die Zeit, die Jahreszeit ist günstig, in der wir jetzt leben. Versuchen wir einmal, uns diese Neujahresnacht das Symbolum sein zu lassen für jene der Erdenentwickelung der Menschheit notwendige Neujahrsnacht, in der heranrücken wird die neue Zeitepoche, in der wachsen wird und immer mehr wachsen wird das Licht, das Seelenlicht, das Schauen, das Erkennen desjenigen, was im Spirituellen lebt und von dem Spirituellen aus die Menschenseele durchwallen und durchfluten kann. Bringen wir den Mikrokosmos unseres Erlebens in dieser Neujahrsnacht in Zusam­menhang mit dem Makrokosmos des Menschheitserlebens über die Erde hin: dann werden wir erleben können, was wir an Empfindungen er­leben sollen, da wir etwas ahnen können von dem Anbruch des neuen großen Weltentages in der fünften nachatlantischen Periode, an dessen Anbruch wir stehen, dessen Mitternacht wir würdig erleben wollen."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Wir beginnen diese Feier unseres Jahresschlusses damit, daß uns Frau Dr.",
        "Steiner die schöne norwegische Legende von Olaf Ästeson zum Vortrag bringen wird, von jenem Olaf Ästeson, der, als dieWeihnachts­zeit herannahte, in eine Art von Schlaf verfiel, welcher dreizehn Tage dauerte: die heiligen dreizehn Tage, die wir ja bei verschiedenen unse­rer Betrachtungen kennengelernt haben.",
        "Während dieses Schlafes hatte er wichtige Erlebnisse, von denen er dann, als er wieder erwachte, zu erzählen wußte."
      ],
      [
        "Wir haben verschiedene Betrachtungen angestellt, die uns darauf aufmerksam machen konnten, wie wir durch die geisteswissenschaft­liche Weltanschauung in einer andern Weise alte Erkenntnisschätze für die menschliche Erkenntnis wiedergewinnen, die in vergangenen Tagen gewußt worden sind von den Menschen als dasjenige, was den geistigen Welten angehört.",
        "Immer wieder und wieder werden wir durch das eine oder andere auf dieses vorweltliche Wissen von den geistigen Welten stoßen, und immer wieder werden wir daran erinnert, daß dieses Wis­sen der Vorzeit darauf beruhte, daß der Mensch vermöge seiner frü­heren Organisation in einem solchen Zusammenhang stehen konnte mit dem ganzen Weltenall und seinem Geschehen, daß, wie wir uns in unserer Sprache ausdrücken, der menschliche Mikrokosmos eintauchte in die Gesetzmäßigkeit, in das Geschehen des Makrokosmos, und daß er bei diesem Eintauchen in den Makrokosmos Erlebnisse haben konnte über Dinge, die sein Seelenleben innig angehen, die ihm aber verborgen bleiben müssen, solange er auf dem physischen Plane als Mikrokosmos wandelt und nur mit derjenigen Erkenntnis ausgestattet ist, die den Sinnen und dem an die Sinne gebundenen Verstande gegeben ist."
      ],
      [
        "Wir wissen ja, wie nur eine materialistische Weltanschauung des Glaubens sein kann, daß allein der Mensch innerhalb der Weltenord­nung mit einem Erkenntnis-, Gefühls- und Willensvermögen begabt sei; während man anerkennen muß vom Standpunkte einer spirituellen Weltanschauung, daß ebenso, wie es unterhalb der Menschenstufe Wesenheiten"
      ],
      [
        "gibt, es auch Wesenheiten gibt oberhalb der menschlichen Stufe des Denkens, Fühlens und Wollens.",
        "In diese Wesenheiten kann sich der Mensch einleben, wenn er eben als Mikrokosmos im Makro-kosmos untertaucht.",
        "Wir müssen aber dann von diesem Makrokosmos so sprechen, wie wenn er nicht nur ein Raumesmakrokosmos sei, son­dern wie wenn die Zeit in ihrem Verlaufe Bedeutung habe im Leben des Makrokosmos.",
        "Wie der Mensch sich zurückziehen muß von all den Eindrücken, die auf seine Sinne ausgeübt werden können aus seiner Umgebung, wie er gleichsam um sich herum durch das Abschließen seiner Sinneswahrnehmung Finsternis erzeugen muß, um im Inneren das Licht des Geistes anzuzünden, wenn er in die Tiefen seiner Seele hinuntersteigen will, so muß derjenige Geist, den wir als den Erdgeist bezeichnen können, abgeschlossen sein von den Eindrücken des übrigen Kosmos.",
        "Es muß das geringste Maß von Wirkungen von dem äußeren Kosmos auf den Erdgeist ausgeübt werden, damit der Erdgeist selber sich innerlich konzentrieren, seine Fähigkeiten innerlich zusammen­ziehen kann.",
        "Denn dann werden die Geheimnisse entdeckt, die der Mensch deshalb durchzumachen hat mit diesem Erdgeist, weil die Erde als Erde aus dem Kosmos herausgesondert ist."
      ],
      [
        "Solch eine Zeit, wo das größte Maß der Eindrücke vom äußeren Makrokosmos auf die Erde ausgeübt wird, ist die Sommersonnenwende­zeit, die Johannizeit.",
        "Es erinnern uns daher viele Nachrichten aus alten Zeiten, die an Festesdarstellungen und Festesbegehungen anknüpfen, wie solche Feste inmitten der Sommerzeit stattfanden, wie die Seele in der Mitte des Sommers dadurch, daß sie sich des Ich entäußert und auf­geht im Leben des Makrokosmos, trunken hingegeben ist den Eindrük­ken vom Makrokosmos."
      ],
      [
        "Aber umgekehrt erinnern uns die legendarischen oder sonstigen Dar­stellungen desjenigen, was in der Vorzeit erlebt werden konnte, dann, wenn das geringste Maß der Eindrücke vom Makrokosmos zur Erde kommt, daran, daß der Erdgeist, in sich konzentriert, die Geheimnisse des Erdenseelenlebens im unendlichen All erlebt, und daß der Mensch, wenn er sich hineinbegibt in dieses Erleben zu der Zeit, in welcher am wenigsten Licht und Wärme gesendet wird aus dem Makrokosmos zur Erde, dann die heiligsten Geheimnisse miterlebt.",
        "Daher wurden diese"
      ],
      [
        "Tage um die Weihnachtszeit herum immer so heilig gehalten, weil der Mensch, als er in seinem Organismus noch die Fähigkeit hatte, mitzu­erleben das Erdenerleben in der Zeit, wo es am konzentriertesten ist, mit dem Erdgeist zusammensein konnte."
      ],
      [
        "Olaf Ästeson, Olaf der Erdensohn, erlebt in diesen dreizehn kür­zesten Tagen, indem er entrückt ist in den Makrokosmos, mancherlei Geheimnisse des Weltenalls.",
        "Und die nordische Legende, die in neuerer Zeit wieder ausgegraben worden ist aus alten Nachrichten, berichtet uns von den Erlebnissen, die Olaf Ästeson hatte zwischen der Weih­nachts- und Neujahrszeit bis zum 6.",
        "Januar.",
        "Und wir haben wohl Ver­anlassung, meine lieben Freunde, öfter zu gedenken dieser alten Art des Einlebens des Mikrokosmos in den Makrokosmos; unsere Betrach­tung wird ja an solche Dinge dann anknüpfen können.",
        "Vorerst aber wollen wir hören die Legende von Olaf dem Erdensohn, der in der Zeit, in der wir jetzt sind, die Geheimnisse des Weltendaseins erlebte da­durch, daß er mit dem Erdgeist zusammenlebte.",
        "Hören wir also diese Erlebnisse."
      ],
      [
        "Es folgte die Rezitation."
      ],
      [
        "Meine lieben Freunde, wir haben gehört, wie Olaf Ästeson entschlief in jenem Schlaf, der für ihn eine Offenbarung werden sollte der Ge­heimnisse derjenigen Welten, die dem Sinnenleben, dem gewöhnlichen Leben auf dem physischen Plane entzogen sind.",
        "Wir haben in der Le­gende erhalten die Kunde von jenen alten Erkenntnissen, von jenen alten Einsichten in die geistigen Welten, die wiedererrungen werden sollen durch dasjenige, was wir die geisteswissenschaftliche Weltan­schauung nennen."
      ],
      [
        "Oftmals ist angeführt worden der Ausspruch, der durch alle Kund­gebungen hindurchgeht, die von dem Eintritt der Menschenseele in die geistige Welt handeln, und der da besagt, daß der Mensch erst dann die geistige Welt schauen kann, wenn er mit seinem Erleben an die Pforte des Todes kommt und dann untertaucht in die Elemente.",
        "So daß er die Elemente des Erdendaseins nicht sÖ um sich herum hat, wie sie im gewöhnlichen Leben des physischen Planes um ihn herum sind als die Erde, das Wasser, die Luft, das Feuer, sondern daß er herausgehoben"
      ],
      [
        "ist über diese Außenseite, diese sinnliche Außenseite der Ele­mente, und untertaucht in dasjenige, was diese Elemente sind, wenn man sie ihrer wahren Natur, ihrer nächst wahren Natur nach kennen-lernt, wo Wesen in ihnen anwesend sind, die im Zusammenhange ste­hen mit dem Erleben der Menschenseele."
      ],
      [
        "Daß Olaf Ästeson etwas von diesem Untertauchen in die Elemente erlebte, man konnte es noch nachspüren da, wo zunächst erzählt wird, wie Olaf an die Gjallarbrücke kommt, und wie er über die Brücke wandelt in den Wegen der geistigen Welt, die weithin sich dehnen.",
        "Wie anschaulich wird uns geschildert das Erlebnis mit dem Erdenelement, wird dargestellt, wie er in das Erdenelement eintaucht.",
        "Das wird bis zu jener Anschaulichkeit gebracht, die uns sagt, daß er wie Tote, die in Gräbern liegen, selbst Erde im Munde fühlt.",
        "Und deutlich wird uns dann angedeutet, wie er das Wasserelement durchlebt und alles das­jenige, was im Wasserelement erlebt werden kann, wenn man dieses Wasserelement zugleich mit seinem moralischen Inhalt erlebt.",
        "Dann wiederum wird angedeutet, wie der Mensch zusammenkommt mit dem Feuerelement, mit dem Luftelement."
      ],
      [
        "Das alles ist in einer wunderbar anschaulichen Weise geschildert und zusammengebracht in dem Erleben des Zusammenseins der Men­schenseele mit den Geheimnissen der geistigen Welt.",
        "Die Legende ist später aufgefunden worden; sie ist gesammelt worden da, wo sie noch lebte im Munde des Volkes.",
        "Und es ist manches in dieser Legende, so wie sie heute ist, nicht mehr so, wie es ursprünglich war.",
        "Ursprüng­lich war ohne Zweifel erst die anschauliche' Schilderung der Erleb­nisse im Erdengebiete, dann der Erlebnisse im Wassergebiete.",
        "Und dann waren die Erlebnisse im Luft- und im Feuergebiete wohl noch viel differenzierter, als es der Fall ist in dem schwachen Nachklange, der nach Jahrhunderten aufgefunden worden ist und der uns heute vorliegt."
      ],
      [
        "Ebenso war zweifellos viel großartiger und weniger sentimental der Schluß, der gar nicht mehr, so wie er heute dasteht, an die ursprüng­lich ungeheuer grandiose Sprache erinnert, an das übermenschlich Er­greifende, das in solchen Volkslegenden lag, während der heutige Schluß eben nur menschlich ergreifend ist; ergreifend deshalb, weil er"
      ],
      [
        "mit so tiefen Geheimnissen des Makrokosmos und des menschlichen Er-lebens im Zusammenhange steht."
      ],
      [
        "In solchen Zeiten, wie diejenige ist, in der wir jetzt leben, in solchen Jahreszeiten, wenn wir sie richtig verstehen, ist viel Veranlassung ge­geben, zu gedenken der Tatsache, daß die Menschheit - allerdings mit einem andersgearteten, mehr dumpfen, dämmerigen Erkennen - in der Vorzeit durchdrungen war von einem Wissen, das verlorengegangen ist und das wiedererrungen werden muß.",
        "Und da kann vor unsere Seele die Frage wiederum hintreten: Müssen wir es nicht, da wir heute schon erkennen können, wie ein solches Wissen wiederum zum Heil der Menschheit kommen muß, als eine unserer dringendsten Aufgaben be­trachten, alles zu tun, was ein solches Wissen herbeiführen kann, was die jetzige Menschheitskultur mit einem solchen Wissen durchdringen kann?"
      ],
      [
        "Mancherlei wird notwendig sein, damit in der richtigen Weise die­ser eben angedeutete Umschwung im ganzen menschlichen, ich möchte jetzt sagen, Weltanschauungsfühlen eintreten kann.",
        "Vor allen Dingen wird eines notwendig sein; eines sage ich, denn es ist eines unter vielen; aber man kann immer nur eines nehmen.",
        "Notwendig wird sein, daß sich die Menschenseelen aneignen auf dem Boden unserer geisteswissen­schaftlichen Weltanschauungsströmung Ehrfurcht und Hingebung ge­genüber dem, was in uralten Zeiten in alter Art gewußt worden ist von den großen Geheimnissen des Daseins.",
        "Zu der Empfindung wird man gelangen müssen, wie es in den materialistischen Zeiten versäumt worden ist, diese Ehrfurcht und diese Hingebung in der Seele zu ent­wickeln."
      ],
      [
        "Eine Empfindung wird man davon bekommen müssen, wie trok­ken und nüchtern diese materialistische Zeit ist, und wie hochmütig auf die Verstandeserkenntnis die Menschheit in den ersten Jahrhunder­ten der fünften nachatlantischen Kulturperiode dagestanden hat vor den Offenbarungen alter Religions- und alter Wissensüberlieferungen, die wahrhaftig, wenn man mit der nötigen Ehrfurcht ihnen naht, ahnen lassen, daß tiefe, tiefe Weisheit in ihnen ruht.",
        "Wie ehrfurchtslos im Grunde genommen stehen wir heute auch vor der Bibel!",
        "Ich will gar nicht sprechen von jener Art moderner Greuelforschung, welche die"
      ],
      [
        "ganze Bibel zerzaust und zerfasert.",
        "Ich will nur sprechen von der nüch­ternen, trockenen Art, wie wir heute, gleichsam ausgerüstet nur mit Sinnenerkenntnis und den gewöhnlichen Verstandeskräften, uns der Bibel nahen, und wie wir nicht mehr eine Empfindung aufbringen können für die ungeheure Größe menschlicher Anschauung, die aus manchen Stellen uns entgegentritt.",
        "Auf eine Stelle aus dem 2.",
        "Moses-buche, 33.",
        "Kapitel, Vers 18, möchte ich hinweisen: Und Moses spricht zu Gott: «Zeige mir doch die Gestalt deiner Offenbarung.»"
      ],
      [
        "Worauf Jehova sprach: «Ich will vorüberziehen lassen alle meine Güte an deinem Angesicht, und ich will rufen den Namen Jehovas vor dir und will gnadevoll sein dem, den ich begnaden darf, und will Erbarmen üben mit dem, mit dem ich Erbarmen üben darf.»"
      ],
      [
        "Dann aber spricht Jehova: «Du kannst mein Antlitz nicht sehen, denn mich sieht kein Mensch, der dann noch lebend bleiben kann.»"
      ],
      [
        "Und es spricht Jahve: «Hier ist ein Ort bei mir, stelle dich auf den Felsen, und wenn meine Herrlichkeit vorüberzieht, so will ich dich in eine Höhlung des Felsens stellen und meine Hand über dich decken, bis ich vorüber bin.",
        "Wenn ich dann meine Hand entferne, so wirst du meine Rückseite sehen, aber mein Antlitz kann nicht geschaut werden.»"
      ],
      [
        "Wenn man zusammennimmt so manches, was in den verflossenen Jahren unseres geisteswissenschaftlichen Strebens in unsere Seelen und unsere Herzen hineinziehen konnte, und sich naht dieser Stelle, dann kann man die Empfindung haben: Ja, was spricht denn da für eine unendliche Weisheit aus dieser Stelle, und wie taub sind die Menschen-ohren des materialistischen Zeitalters, daß s'ie so gar nichts vernehmen können von der unendlich tiefen Weisheit, die aus dieser Stelle spricht. -Ich möchte zugleich die Gelegenheit ergreifen, Sie hinzuweisen auf ein Büchelchen, das erschienen ist mit dem Titel: «Worte Mosis» in Bruns' Verlag in Minden in Westfalen, und zwar deshalb, weil manches in die­sem Büchelchen aus den Fünf Büchern Moses besser übersetzt ist als in andern Ausgaben.",
        "Es hat sich da Dr.",
        "Hugo Bergmann, welcher der Herausgeber der «Worte Mosis» ist, für die Interpretation viele Mühe gegeben."
      ],
      [
        "Daß im Grunde genommen der Mensch sich aneignen müsse eine ganz andere Art des Sich-Verhaltens zur Welt, wenn er in die geistigen Welten"
      ],
      [
        "eintauchen will, als das Verhalten zur Sinneswelt ist, das haben wir öfter hervorgehoben.",
        "Die Sinneswelt hat der Mensch um sich.",
        "Er schaut hin auf die Sinneswelt, er sieht sie in ihren Farben und Formen, hört ihre Töne.",
        "Die Sinneswelt ist da; wir stehen ihr gegenüber; sie wirkt auf uns; wir nehmen sie in der Wahrnehmung auf, wir denken über sie nach.",
        "So ist unser Verhalten zur Sinneswelt.",
        "Wir sind passiv; sie arbei­tet sich gleichsam in unsere Seele hinein.",
        "Wir denken über die Sinnes-welt, wir stellen die Sin'neswelt vor."
      ],
      [
        "Ganz anders ist unser Verhalten, wenn wir uns hinaufleben in die geistige Welt.",
        "Darin besteht eine der Schwierigkeiten, richtige Vorstel­lungen zu gewinnen über das, was der Mensch erlebt, wenn er in die geistige Welt eintritt."
      ],
      [
        "Ich habe versucht, einige dieser Schwierigkeiten zu charakterisieren in dem Büchelchen: «Die Schwelle der geistigen Welt.» Wir stellen die Sinneswelt vor, wir denken über die Sinneswelt.",
        "Wenn wir alles das durchmachen, was derjenige durchzumachen hat, der den Pfad der Initiation gehen will, dann tritt etwas ein, was man so charakterisieren kann: Wie die Dinge um uns herum sich zu uns ver­halten, so verhalten wir uns selber zu den Wesenheiten der höheren Hierarchien: die stellen uns vor, die denken uns."
      ],
      [
        "Wir denken die Ge­genstände außer uns, die Mineralien, Pflanzen und Tiere: sie werden unsere Gedanken.",
        "Wir wiederum sind die Vorstellungen, Gedanken und Wahrnehmungen der Geister der höheren Hierarchien."
      ],
      [
        "Wir wer­den zu den Gedanken der Angeloi, Archangeloi, Archai und so weiter.",
        "Wir werden aufgenommen von ihnen, wie wir selber aufnehmen die Pflanzen, Tiere und Menschen.",
        "Und wir müssen uns geborgen fühlen, indem wir uns sagen können: Es denken uns die Wesen der höheren Hierarchien, sie stellen uns vor."
      ],
      [
        "Diese Wesen der höheren Hierarchien ergreifen uns mit ihren Seelen. - Ja, wir können uns geradezu vor­stellen: indem jener Olaf Ästeson vor dem Kirchentor einschlief, wurde er eine Vorstellung der Geister der höheren Hierarchien, und während er schlief, erlebten die Wesen der höheren Hierarchien dasjenige, was erleben die Wesen des Erdgeistes, der für uns ja eine Pluralität ist.",
        "Und indem Olaf Ästeson wieder heruntersinkt in die physische Welt, er­innert er sich an dasjenige, was die Geister der höheren Hierarchien in ihm erlebt haben."
      ],
      [
        "Stellen wir uns einmal vor: wir begeben uns auf den Pfad der Ini­tiation!",
        "Wie können wir uns verhalten zu den geistigen Welten, in die wir als in eine Summe von geistigen Wesenheiten der höheren Hier­archien unseren Einzug halten wollen?",
        "Wie können wir uns zu ihnen verhalten? - Wir können sie ansprechen und können zu ihnen sagen: Wie gelangen wir in Euch hinein, wie offenbart Ihr Euch uns? - Und dann, wenn wir Verständnis gewonnen haben für die andere Art des Verhaltens der Menschenseele zu den höheren Welten, wird uns ge­wissermaßen entgegentönen aus den geistigen Welten: Ja, so wie du die Sinneswelt wahrnimmst, daß sie vor deinem Blicke erscheint, vor deinen Sinnen auftritt, so kannst du die geistige Welt nicht wahrneh­men.",
        "Wir müssen dich vorstellen, und du mußt dich in uns empfinden.",
        "Du mußt dich so empfinden, wie der Gedanke, den du in der Sinnes-welt denkst, sich erleben würde, wenn er sich in dir erleben könnte.",
        "Du mußt dich hingeben der geistigen Welt, dann wird in dich einziehen alles das, was sich dir offenbaren kann an Wesenheiten der höheren Hierarchien.",
        "Dann wird es in deine Seele einfließen und gnadevoll in deiner Seele leben, wie du in deinen Gedanken lebst, wenn du über die Sinneswelt denkst.",
        "Wenn dich die geistige Welt begnadigen will, dann wird sie dich durchdringen mit ihrer Liebe!",
        "Wenn sie sich deiner er­barmen und dich mit ihrer Liebe durchdringen will."
      ],
      [
        "Denn du mußt nicht glauben, daß du dich den geistigen Wesen so gegenüberstellen kannst wie der sinnlichen Welt.",
        "Wie Moses in die Höhlung gehen mußte, so mußt du in die Höhlung der geistigen Welt dich hineinbegeben.",
        "Du mußt dich da hineinstellen.",
        "Wie der Gedanke in dir lebt, so mußt du dich in die geistigen Wesen hineinleben.",
        "Du mußt selber alsweltgedanke in dem Makrokosmos darinnen leben.",
        "Das, was du so erlebst, von selbst zu erleben, das kannst du nicht während deines Erdenlebens zwischen der Geburt und dem Tode; das kannst du nur nach dem Tode, wenn du gestorben bist.",
        "Niemand kann die geistige Welt so erleben, bevor er gestorben ist, aber vorüberziehen kann an dir die geistige Welt, dich begnadigen, dich mit ihrer Liebe durchfluten.",
        "Und dann, wenn du nachher oder während du darinnen bist in dieser geistigen Welt, dein Erdenbewußtsein entwickelst, dann erglänzt dir herein in dein Erdenbewußtsein dasjenige, was die geistige Welt ist."
      ],
      [
        "Wie der Gegenstand draußen ist und der Mensch gegenübersteht dem Gegenstande, wie der Gegenstand hineinragt in sein Bewußtsein und dann darinnen ist, so ist der Mensch mit seiner Seele in der Höh­lung der geistigen Welt.",
        "Die geistige Welt zieht durch ihn durch.",
        "Hier ist der Mensch vor den Dingen.",
        "Wenn der Mensch eingeht in die gei­stige Welt, sind die Wesenheiten der höheren Hierarchien hinter ihm.",
        "Da kann er nicht ihr Angesicht sehen, so wie die Gedanken nicht unser Antlitz sehen, wenn sie in uns sind.",
        "Das Antlitz ist vorn; die Gedanken sind dahinter, sie sehen nicht das Antlitz.",
        "Das ganze Geheimnis der Initiation ruht in den Worten, die Jahve zu Moses spricht."
      ],
      [
        "Und Moses spricht zu Gott: «Zeige mir doch die Gestalt deiner Offenbarung.»"
      ],
      [
        "Worauf Jehova sprach: «Ich will vorüberziehen lassen alle meine Güte an deinem Angesicht, und ich will rufen den Namen Jehovas vor dir und will gnadevoll sein dem, den ich begnaden darf, und will Er­barmen üben mit dem, mit dem ich Erbarmen üben darf.»"
      ],
      [
        "Dann aber spricht Jehova: «Du kannst mein Antlitz nicht sehen, denn mich sieht kein Mensch, der dann noch lebend bleiben kann.»"
      ],
      [
        "An die Pforte des Todes kommt man ja durch die Initiation."
      ],
      [
        "Und es spricht Jahve: «Hier ist ein Ort bei mir, stelle dich auf den Felsen, und wenn meine Herrlichkeit vorüberzieht, so will ich dich in eine Höhlung des Felsens stellen und meine Hand über dich decken, bis ich vorüber bin.",
        "Wenn ich dann meine Hand entferne, so wirst du meine Rückseite sehen, aber mein Antlitz kann nicht geschaut werden.»"
      ],
      [
        "Es ist die entgegengesetzte Art, wie man die Sinneswelt wahr­nimmt.",
        "Man muß vieles von dem, was man sich durch Jahre hindurch erwirbt an geisteswissenschaftlichem Streben, aufbringen, um in der richtigen Weise in Ehrfurcht und Hingabe vor einer solchen Offen­barung zu stehen.",
        "Dann aber kommt allmählich immer mehr und mehr dieses Gefühl der Ehrfurcht gegenüber diesen Offenbarungen in die Menschenseele hinein, und unter dem mancherlei, was wir brauchen, damit der angedeutete Umschwung in der geistigen Menschheitskultur hervortreten kann, ist diese Ehrfurcht, diese Hingebung."
      ],
      [
        "Die Zeit, in welcher das geringste Maß von Eindrücken aus dem Makrokosmos zur Erde kommt, die Zeit von Weihnachten bis über das"
      ],
      [
        "Neujahr hinaus, ungefähr bis zum 6.",
        "Januar, ist wohl geeignet, daß man sich nicht nur erinnere an das Gegenständliche der geistigen Er­kenntnis, sondern an die Empfindungen, die wir in uns entwickeln müssen durch das Aufnehmen der Geisteswissenschaft.",
        "Wahrhaft leben wir uns also wieder hinein in den Erdgeist, mit dem wir zusammen doch eine Ganzheit bilden, und mit dem lebte das alte, hellseherische Erkennen, wie es uns etwa in dieser Legende von Olaf Ästeson darge­stellt ist.",
        "Ehrfurcht und Hingebung gegenüber dem geistigen Leben hat die Menschheit des materialistischen Zeitalters vielfach verlernt.",
        "Not­wendig ist es vor allen Dingen, darauf zu achten, daß diese Ehrfurcht und diese Hingebung wiederum kommt, denn nur dadurch werden wir die Stimmung entwickeln können, die uns auch in der richtigen Weise an die neue Geisteswissenschaft heranbringt.",
        "Vorerst ist immer noch jene Stimmung da, welche an diese Geisteswissenschaft so herantritt, wie man an die andere, gewöhnliche Wissenschaft herantritt.",
        "In dieser Beziehung muß aber eine gründliche Umkehr stattfinden."
      ],
      [
        "Dadurch, daß der Menschheit verlorengegangen ist die Einsicht in die geistige Welt, ist auch verlorengegangen das richtige Verhältnis des Menschen zum ganzen Menschenwesen, zur Menschheit.",
        "Die materia­listische Weltanschauung erzeugt chaotische Empfindungen über das Weltendasein.",
        "Diese chaotischen Empfindungen über das Welt- und Menschheitsdasein mußten hereinbrechen in der Zeit des Materialismus.",
        "Nehmen wir eine Zeit - und diese Zeit ist die unsrige: es sind die ersten Jahrhunderte der fünften nachatlantischen Kulturperiode -, wo man so gar keine wirkliche Ahnung mehr davon hatte, daß des Menschen Wesen ein dreifaches ist: das leibliche, das seelische und das geistige Wesen.",
        "Denn wahrhaftig, so ist es.",
        "Dasjenige, was für uns schon zu den ersten Elementen des geisteswissenschaftlichen Erkennens gehören muß: die Dreigliederung des Menschen in Leib, Seele und Geist, es fehlte von den ersten vier Jahrhunderten der fünften nachatlantischen Kulturperiode an bis in unsere Zeit hinein jede Ahnung davon.",
        "Der Mensch war eben Mensch, und alles Sprechen über eine menschliche Gliederung von der Art, wie wir sie haben in Leib, Seele und Geist, galt als törichte, phantastische Rederei."
      ],
      [
        "Man könnte glauben, daß diese Dinge nur bedeutsam sind für die"
      ],
      [
        "Erkenntnis.",
        "Das sind sie aber nicht.",
        "Sie sind nicht allein bedeutsam für die Erkenntnis, sondern sie sind auch bedeutsam für die ganze Art, wie sich der Mensch in das Leben hineinstellt.",
        "Im dritten Jahrhundert der neuzeitlichen Entwickelung oder auch, wie wir in unserer Sprache sagen, der Entwickelung der fünften nachatlantischen Kulturperiode, brachen in diese Zeit hinein drei gewaltige Worte, in denen gewisser­maßen verstand oder wenigstens zu verstehen versuchte diese Zeit das Zentrum menschlichen Wollens im Erdenerleben.",
        "Drei Worte, die be­deutsam sind, die aber ihre Eigentümlichkeit erhielten dadurch, daß sie in der Zeit in die Menschheit hineinbrachen, in welcher man nichts wußte von der Dreigliederung der menschlichen Natur.",
        "Die Mensch­heit hörte von Freiheit, Gleichheit und Brüderlichkeit."
      ],
      [
        "Daß diese Worte hineintönten in einer bestimmten Zeit in die neu­zeitliche Kultur, war eine tiefe Notwendigkeit.",
        "Verstehen wird man diese Worte wirklich erst, wenn man die dreifache Gliederung der menschlichen Natur verstehen wird, weil man dann erst wissen wird, welche Bedeutung diese Worte für die Menschennatur, im wahren Sinne des Wortes, haben können.",
        "Solange man mit jenen chaotischen Empfindungen diese drei Worte erfüllt, die da ausgehen von dem Ge­danken: Mensch ist Mensch, und die Dreigliederung des Menschen ist ein törichtes Wahngebilde - so lange kann der Mensch auch nicht inner­halb des Gebietes der Richtlinie dieser drei Worte sich zurechtfinden.",
        "Denn so, wie uns die drei Worte entgegentreten, können sie nicht un­mittelbar, man möchte sagen, auf gleichen Niveauflächen des mensch­lichen Erlebens angewendet werden.",
        "Das können sie nicht.",
        "Einfache Erwägungen, die Ihnen vielleicht deshalb, weil sie so einfach sind, nicht gleich in dem Schwerwiegenden, das sie bedeuten, vor das Seelenauge treten werden, können Ihnen andeuten, wie auf der gleichen Niveau-fläche des Lebens das, was diese drei Worte bedeuten, in ernste Lebens-konflikte geraten kann."
      ],
      [
        "Nehmen wir zunächst das Gebiet, in dem uns auf die natürlichste Weise der Welt die Brüderlichkeit entgegentritt.",
        "Nehmen wir die menschliche Blutsverwandtschaft, die Familie, wo wir die Brüderlich­keit nicht erst herzustellen brauchen, wo sie dem Menschen naturge­mäß angeboren ist, und bedenken wir, wie es zu unseren Empfindungen"
      ],
      [
        "spricht, wenn wir sehen können, daß in einer Familie echte, wahre Brüderlichkeit herrscht, daß alles brüderlich verbunden ist.",
        "Aber jetzt -ohne daß wir in geringstem Maße etwas zu dämpfen brauchen von der wundervollen Empfindung, die wir von dieser Brüderlichkeit haben können - werfen wir den Blick hinein, um zu sehen, was innerhalb der Brüderlichkeit der Familie entstehen kann, gerade wegen der Brüder­lichkeit der Familie.",
        "Ein Glied kann in der Familie sein, welches sich gerade wegen der innerhalb der Familie gerechtfertigten Brüderlichkeit nicht wohl fühlt, sich heraussehnt aus der Brüderlichkeit der Familie, weil es fühlt, daß es die Seele nicht entfalten kann in der Brüderlich­keit der Familie, weil es fühlt, daß es heraus muß zur freien Entfaltung der Seele aus der Familie, in der es so brüderlich leben kann.",
        "Wir sehen:"
      ],
      [
        "die Freiheit, die freie Entfaltung des Seelenlebens, kann in Konflikt kommen mit der allerbestgemeinten Brüderlichkeit."
      ],
      [
        "Selbstverständlich kann der Oberflächling sagen, das wäre nicht die rechte Brüderlichkeit, die mit der Freiheit einer Seele innerhalb der Brüderlichkeit sich nicht verträgt.",
        "Aber sagen kann man alles, was sich vorstellen läßt.",
        "Man kann sagen, daß sich alles miteinander ver­trägt, daran ist ja gar kein Zweifel.",
        "Ich habe neulich einmal eine Dis­sertation in die Hand bekommen.",
        "Unter den Thesen, die da zu ver­teidigen waren, war die These aufgestellt: Ein Dreieck ist ein Viereck.",
        "Man kann natürlich auch das verteidigen - ja, man kann es sogar streng beweisen, daß ein Dreieck ein Viereck ist!",
        "So kann man auch voll bewei­sen, daß Brüderlichkeit und Freiheit vereinbar sind.",
        "Aber darum han­delt es sich nicht, sondern es handelt sich darum, wie um der Freiheit willen manches Gebiet der Brüderlichkeit verlassen werden muß und auch verlassen wird.",
        "So könnten wir noch manches andere anführen."
      ],
      [
        "Wenn man die Diskrepanzen zwischen Brüderlichkeit und Gleich­heit aufzählen wollte, so würde man sehr lange darüber reden müssen.",
        "Selbstverständlich, in abstracto kann man sich wieder vorstellen: alle können gleich sein, und kann zeigen, daß sich Brüderlichkeit und Gleichheit vertragen.",
        "Aber es handelt sich nicht um Abstraktionen, sondern um die Beobachtung der Wirklichkeit, wenn wir es mit dem Leben ernst und ehrlich nehmen.",
        "In dem Augenblicke, da wir wissen, daß die menschliche Wesenheit aus dem Leiblichen, das auf dem physischen"
      ],
      [
        "Plane sich auslebt, besteht, aus dem Seelischen, das in der See­lenwelt eigentlich sich auslebt, und aus dem Geistigen, das in der gei­stigen Welt sich auslebt, in diesem Augenblicke eröffnet sich auch die richtige Perspektive für den Zusammenhang der drei gewaltigen Worte, die wir angeführt haben.",
        "Brüderlichkeit ist das wichtigste Ideal für die physische Welt.",
        "Freiheit für die Seelenwelt, und - insofern der Mensch in der Seelenwelt darinnensteht, sollte man sprechen von der Freiheit der Seele, das heißt von einem solchen sozialen Zustande, welcher der Freiheit der Seele volle Gewähr leistet.",
        "Und wenn man bedenkt, daß wir, jeder von uns, streben müssen von unserem individuellen Stand­punkte aus nach Geist-Erkenntnis, nach der Entwickelung unseres Geistes, um mit dem Geiste im Geisterland darinnenzustehen, so wird uns sehr bald vor das geistige Auge treten, wohin wir kämen mit unse­rer Geistauffassung, wenn jeder nur auf seinem eigenen Wege suchte und jeder zu einem ganz andern Geistesinhalt käme."
      ],
      [
        "Wir können uns überhaupt als Menschen nur im Leben zusammen­finden, wenn wir - jeder für sich selber - den Geist suchen und zuletzt zu einem gleichen geistigen Inhalte kommen können.",
        "Von der Gleich­heit des Geisteslebens kann gesprochen werden.",
        "Von Brüderlichkeit auf dem phyischen Plane und in bezug auf alles das, was mit den Ge­setzen des physischen Planes zusammenhängt und in die Menschen­seele sich hineinlebt von dem physischen Plane aus.",
        "Freiheit in bezug auf alles das, was sich als Gesetze der Seelenwelt in die menschliche Seele hineinlebt; Gleichheit in bezug auf alles, was von den Gesetzen des Geisterlandes in die menschliche Seele sich hineinlebt."
      ],
      [
        "Sie sehen, ein Weltenneujahr muß angehen, in dem eine Sonne wach­sen wird in bezug auf ihre wärmende und leuchtende Kraft: jene Sonne, welche für manches, was in der Zeit der Verdunkelung zwar lebt, aber unverstanden lebt, die leuchtende Wärme geben muß.",
        "Das ist gerade das Eigentümliche unserer Zeit, daß manches erstrebt, manches aus­gesprochen wird, ohne daß es verstanden wird."
      ],
      [
        "Aber auch dieses kann uns zur Ehrfurcht führen und zur Hingebung gegenüber der geistigen Welt.",
        "Denn wenn wir bedenken, daß viele im dritten Jahrhundert der fünften nachatlantischen Periode die Worte Brüderlichkeit, Freiheit und Gleichheit erstrebten und ausgesprochen"
      ],
      [
        "haben, ohne daß sie im Grunde genommen verstanden wurden, dann haben wir schon die Möglichkeit, zu verstehen und eine Antwort zu finden auf die Frage: Woher also sind diese Worte gekommen?",
        "Die göttlich-geistige Weltenordnung hat sie zunächst im voraus der noch nicht verstehenden Menschenseele eingeimpft, damit sich diese an sol­chen Leitworten hinaufranke zum wahren Weltverständnis.",
        "Selbst in solchen Tatsachen können wir die weisheitsvolle Führung in der Wel­tenevolution beobachten.",
        "In uns mehr oder weniger fern- oder nahe­liegenden Zeiten können wir überall diese Führung beobachten; beob­achten, wie wir oftmals erst hinterher einsehen, daß das, was wir vor­her gemacht haben, eigentlich weisheitsvoller war, als wir es mit der damaligen Weisheit, die wir beherrscht haben, hätten machen können.",
        "Ich habe darauf aufmerksam gemacht gleich im Beginne meiner Schrift über «Die geistige Führung des Menschen und der Menschheit»."
      ],
      [
        "Aber wenn Sie so etwas nehmen wie die Tatsache, daß in die Welt-entwickelung, in die Entwickelung des Menschen hineinfallen Rich­tungsworte, die erst nach und nach verstanden werden können, dann werden Sie wohl aufmerksam werden auf ein Bild, das man gebrauchen kann, wenn man diese abgelaufene Periode der fünften nachatlanti­schen Kulturepoche charakterisieren will.",
        "Sie ist nämlich wirklich in bezug auf gewisse Dinge zu vergleichen mit der Zeit des Advents, wo die Zeiten des Tageslichtes immer kürzer und kürzer werden.",
        "Und nun tritt die Entwickelung in dieser unserer Zeit, in der wir wiederum etwas wissen können von den Offenbarungen der geistigen Welt, in die Phase ein, in der wir die Vorstellung gewinnen können, daß die licht-vollen Zeiten länger und länger werden und wir davon sprechen kön­nen, daß uns dieser Zeitenlauf wirklich analog erscheinen kann den dreizehn Tagen und dem Wiederhineinleben in die wieder wachsenden Tage."
      ],
      [
        "Aber die Sache geht noch tiefer.",
        "Es ist nicht richtig, ganz und gar nicht richtig, wenn wir nur böse Worte finden für die materialistische Zeit der letzten vier Jahrhunderte.",
        "Es kam ja diese neue Zeit dadurch herauf, daß man die großen Entdeckungen und Erfindungen machte, wie man sie eben «groß» nennt im materialistischen Zeitalter, zum Bei­spiel, daß man die Erde umschiffte, Länder entdeckte, die man früher"
      ],
      [
        "nicht gekannt hat, daß man begann, die Erde zu kolonisieren.",
        "Das war der Beginn der materiellen Kultur.",
        "Und dann rückte nach und nach die Zeit heran, in der man fast erstickte in der materiellen Kultur.",
        "Die Zeit kam herauf, wo man alles, was man an geistigen Kräften hatte, zum Begreifen und Erfassen des materiellen Lebens anwendete.",
        "Immer mehr und mehr wurde vergessen, wie wir gesehen haben, dasjenige, was an Einblicken und Einsichten, an Schauungen in die geistige Welt aus alten Erkenntnissen vorhanden war."
      ],
      [
        "Aber es ist nicht richtig, wenn man nur böse Worte für die materia­listische Zeit hat.",
        "Richtig ist vielmehr ein anderes; richtig ist, wenn man bedenkt, daß diese Menschenseele in ihrem wachen Teile materia­listisch gedacht, materialistisch gesonnen hat, daß sie materialistisch die Wissenschaft und die Kultur begründet hat, daß aber diese Men­schenseele ein Ganzes ist.",
        "Man könnte sagen: der eine Teil der Men­schenseele begründete die materialistische Kultur.",
        "Früher war dieser Teil untätig, die Menschen wußten nichts von äußerer Wissenschaft, wußten nichts von äußerlichem, materiellem Leben; da war der spiri­tuelle Teil mehr wach. (Es wurde gezeichnet.) In den letzten vier Jahr­hunderten war gerade jener Teil wach, der die materialistische Kultur begründete; der andere aber hat geschlafen; er schlief, dieser andere Teil der Menschenseele.",
        "Und wahrhaftig, das, was wir jetzt an Kräften entwickeln in der Menschheit, um uns wieder hinaufzuarbeiten zur Spiritualität, ist veranlagt worden in der Zeit der materialistischen Kul­tur in den Seelengliedern, die unten geschlafen haben.",
        "Die «Menschheit» war wirklich in bezug auf die Geist-Erkenntnis in diesen Zeiten: Olaf Ästeson.",
        "Das war sie wirklich.",
        "Nur ist sie noch nicht erwacht, diese Menschheit!",
        "Die Geisteswissenschaft muß sie zum Erwachen bringen."
      ],
      [
        "Die Zeit muß kommen, wo junge und auch alte Leute Worte hören, die gesprochen werden aus dem Teil der Menschenseele heraus, der geschlafen hat in der finsteren Zeit.",
        "Gar lange hat diese Menschenseele also geschlafen, aber es werden die Weltengeister an diese Menschen-seele herantreten und ihr schon zurufen: Erwache nun, 0 Olaf Äste­son! - Wir müssen uns nur in der richtigen Weise vorbereiten, daß wir nicht vor den Ruf gestellt werden: Erwache nun, 0 Olaf Ästeson! -und nicht Ohren haben, zu hören.",
        "Dazu betreiben wir eben die Geisteswissenschaft,"
      ],
      [
        "daß wir Ohren haben, wenn der Ruf nach dem spirituel­len Wachsein in der Menschheitsentwickelung ertönen wird."
      ],
      [
        "Es ist gut, wenn der Mensch manchmal sich erinnert, daß er ein Mikrokosmos ist und daß ihm manches werden kann an Erlebnissen, wenn er in dem Makrokosmos aufgeht.",
        "Und wir haben gesehen: die Zeit, die Jahreszeit ist günstig, in der wir jetzt leben.",
        "Versuchen wir einmal, uns diese Neujahresnacht das Symbolum sein zu lassen für jene der Erdenentwickelung der Menschheit notwendige Neujahrsnacht, in der heranrücken wird die neue Zeitepoche, in der wachsen wird und immer mehr wachsen wird das Licht, das Seelenlicht, das Schauen, das Erkennen desjenigen, was im Spirituellen lebt und von dem Spirituellen aus die Menschenseele durchwallen und durchfluten kann.",
        "Bringen wir den Mikrokosmos unseres Erlebens in dieser Neujahrsnacht in Zusam­menhang mit dem Makrokosmos des Menschheitserlebens über die Erde hin: dann werden wir erleben können, was wir an Empfindungen er­leben sollen, da wir etwas ahnen können von dem Anbruch des neuen großen Weltentages in der fünften nachatlantischen Periode, an dessen Anbruch wir stehen, dessen Mitternacht wir würdig erleben wollen."
      ]
    ]
  },
  {
    "order": 11,
    "title_de": "ANSPRACHE zu einer Vorlesung des Traumliedes von Olaf Ästeson",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Es soll zum Vortrage gebracht werden eine bedeutsame Volksdichtung. Von dem jungen Olaf Ästeson handelt sie, der in der Sage des nor­wegischen Volkes lebt. Ein Traum dieses Olaf Ästeson wird in echt volkstümlich dichterischer Form erzählt.",
      "Ein Traum, von welchem sich das Volk vorstellte, daß er einen langen Schlaf von dreizehn Tagen und Nächten ausfüllte, jenen dreizehn Nächten und Tagen, welche zwischen dem Weihnachtsabend und dem Dreikönigstage, am 6. Januar, liegen.",
      "Diese dreizehn Tage spielen eine Rolle in vielen Volksüberlieferungen. Will man verstehen, was in solchen Überlieferungen ausgedrückt ist, so muß man sich vorstellen, wie vor verhältnismäßig kurzer Zeit das Volk in Land- und Gebirgsgegenden in innigem Zusammenleben mit dem Verlaufe der Natur sich fühlte.",
      "Es empfand anders, wenn die Pflanzen im Frühling aus der Erde hervorsproßten als wenn im Herbste kahl der Erdboden sich hindehnte; anders, wenn die Sonne zur Johanni-Zeit heiß am Himmel brannte, und anders, wenn die Schneewolken im De­zember alle Sonnenstrahlen verbargen. Im Sommer lebte die Seele mit der Natur mit; im Winter zog sie sich in sich selbst zurück, lebte in sich.",
      "Besonders innig wurde dieses Zurückziehen der Seele in sich gegen die Weihnachtszeit hin, wo die Nächte am längsten sind. Und es war dann für die Seele so, daß sie von aller Außenwelt sich zurückzog, wie im Einschlafen, wenn die Augen nicht mehr sehen, die Ohren nicht mehr hören.",
      "Ein Hinbrüten der mit sich selbst beschäftigten Seele trat ein, das bei besonders veranlagten Menschen wie zu einem Träumen wurde. Da erlebten dann manche Seelen besonders anschaulich ihre Versen­kung in die geistige Welt.",
      "Alles was sie fühlten, über Schuld und Sünde, über Lebenshoffnung und Seelensorgen trat vor sie hin. Und wie Träume besondere Formen annehmen, wenn es gegen den Morgen zu­geht und der erste Sonnenstrahl über das noch schlafende Antlitz des Träumers geht, so nimmt das Brüten und Träumen der Seele eine be­sondere Form an, wenn von Weihnacht an die Sonne wieder beginnt, früher am Tage zu erscheinen, wenn das Herannahen des neuen Naturmorgens",
      "verspürt wird. Wer mit Land- oder Gebirgsmenschen je gelebt hat, der kennt die hier in Betracht kommenden Traumerlebnisse, welche die Volksseele in andere Welten einführen. In der Gegenwart allerdings findet man nicht mehr vieles von solchen Erlebnissen. Sie entschwinden tatsächlich, wenn die Lokomotiven und Fabrikschlote in die Land­schaften eindringen. In vielen Gegenden ist es so, daß selbst die Sagen von jenen alten Traumwelten schon verklungen sind. In Gegenden, welche noch weniger von der neueren Industrie- und Verkehrskultur angenommen haben, wie in gewissen Gebieten Norwegens, haben sich so schöne Teile jener Sagenwelt erhalten, wie unser Lied von Olaf Ästeson ist. Es stammt aus alten Zeiten; lebte aber vor kurzem wieder im norwegischen Volke auf und verbreitet sich schnell, so daß es heute wieder viele Menschen kennen, nachdem es lange verschollen war.",
      "Es erzählt einen langen Traum, den Olaf Ästeson träumt, und in welchem er erlebt das Schicksal der Seelen nach dem Tode. Die Vor­stellung liegt zu Grunde, daß die Seele nach dem Tode in die Sternen-welten wandelt, daß sie zum Beispiel in Gebiete kommt, wo die Stern­bilder des Stieres, der Himmelsschlange, des Hundes nahe sind, daß sie in die geistige Nähe des Mondes kommt.",
      "In diese Welten dringt die Seele ein, indem sie die Gjallarbrücke überschreitet, welche die irdische Welt mit der geistigen verbindet. In vielen Volkssagen wird der Regen­bogen als diese Brücke vorgestellt.",
      "Ein Teil dieser geistigen Welt ist Brooksvalin, wo die Lebenstaten der Seelen gewogen werden und ihnen die Vergeltung zuerteilt wird. Die ganze Art, wie das Lied das Erlebnis darstellt, weist auf die Zeit hin, in welcher es sich durch die Volks­dichtung gebildet hat.",
      "Die Vorstellungen über das Leben nach dem Tode sind noch nicht ganz die christlichen; sie sind zum Teile diejeni­gen, welche sich noch in der alten Heidenzeit gebildet haben. Doch wird als die Zeit, in welcher Olaf seinen Traum erlebt, schon die christ­liche Zeit vorgestellt.",
      "Das zeigt sich ja nicht nur dadurch, daß er seinen Traum vor der Kirchentüre erzählt, sondern auch dadurch, daß mitten in die heidnischen Vorstellungen von der Gjallarbrücke und Brooks­valin, die christlichen Vorstellungen von Michael und Christus hinein-spielen. Ja man kann in dem Herankommen des Christus aus dem Süden unmittelbar das Eindringen des Christentums nach Norwegen von",
      "Süden her erkennen. Man hat es zu tun mit einer wohl acht bis neun Jahrhunderte alten Volksdichtung, denn vor so langer Zeit drang das Christentum in Norwegen ein.",
      "Wir möchten durch den Vortrag dieser Dichtung Ihren geistigen Blick auf das Leben der Volksseele lenken, die durch solche Sagen-bildung wie die von Olaf Ästeson zeigt, daß sie sich ihres Zusammen­hanges mit der geistigen Welt bewußt war, die von diesem Zusammen­hang innerlich Bilder erlebte, die ihr die Gewißheit gaben, daß die geistige Welt Dasein hat. Denn wer an Olaf Ästeson herangetreten wäre und etwa ihm gesagt hätte: so etwas gibt es nicht, das hat die Natur­wissenschaft bewiesen: den hätte Olaf Ästeson recht mitleidig an­geschaut, hätte dann wohl teilnahmsvoll gelächelt und gesagt: es gibt mehr Dinge im Himmel und auf Erden, als du dir mit deiner Schul­weisheit erträumst."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Es soll zum Vortrage gebracht werden eine bedeutsame Volksdichtung.",
        "Von dem jungen Olaf Ästeson handelt sie, der in der Sage des nor­wegischen Volkes lebt.",
        "Ein Traum dieses Olaf Ästeson wird in echt volkstümlich dichterischer Form erzählt."
      ],
      [
        "Ein Traum, von welchem sich das Volk vorstellte, daß er einen langen Schlaf von dreizehn Tagen und Nächten ausfüllte, jenen dreizehn Nächten und Tagen, welche zwischen dem Weihnachtsabend und dem Dreikönigstage, am 6.",
        "Januar, liegen."
      ],
      [
        "Diese dreizehn Tage spielen eine Rolle in vielen Volksüberlieferungen.",
        "Will man verstehen, was in solchen Überlieferungen ausgedrückt ist, so muß man sich vorstellen, wie vor verhältnismäßig kurzer Zeit das Volk in Land- und Gebirgsgegenden in innigem Zusammenleben mit dem Verlaufe der Natur sich fühlte."
      ],
      [
        "Es empfand anders, wenn die Pflanzen im Frühling aus der Erde hervorsproßten als wenn im Herbste kahl der Erdboden sich hindehnte; anders, wenn die Sonne zur Johanni-Zeit heiß am Himmel brannte, und anders, wenn die Schneewolken im De­zember alle Sonnenstrahlen verbargen.",
        "Im Sommer lebte die Seele mit der Natur mit; im Winter zog sie sich in sich selbst zurück, lebte in sich."
      ],
      [
        "Besonders innig wurde dieses Zurückziehen der Seele in sich gegen die Weihnachtszeit hin, wo die Nächte am längsten sind.",
        "Und es war dann für die Seele so, daß sie von aller Außenwelt sich zurückzog, wie im Einschlafen, wenn die Augen nicht mehr sehen, die Ohren nicht mehr hören."
      ],
      [
        "Ein Hinbrüten der mit sich selbst beschäftigten Seele trat ein, das bei besonders veranlagten Menschen wie zu einem Träumen wurde.",
        "Da erlebten dann manche Seelen besonders anschaulich ihre Versen­kung in die geistige Welt."
      ],
      [
        "Alles was sie fühlten, über Schuld und Sünde, über Lebenshoffnung und Seelensorgen trat vor sie hin.",
        "Und wie Träume besondere Formen annehmen, wenn es gegen den Morgen zu­geht und der erste Sonnenstrahl über das noch schlafende Antlitz des Träumers geht, so nimmt das Brüten und Träumen der Seele eine be­sondere Form an, wenn von Weihnacht an die Sonne wieder beginnt, früher am Tage zu erscheinen, wenn das Herannahen des neuen Naturmorgens"
      ],
      [
        "verspürt wird.",
        "Wer mit Land- oder Gebirgsmenschen je gelebt hat, der kennt die hier in Betracht kommenden Traumerlebnisse, welche die Volksseele in andere Welten einführen.",
        "In der Gegenwart allerdings findet man nicht mehr vieles von solchen Erlebnissen.",
        "Sie entschwinden tatsächlich, wenn die Lokomotiven und Fabrikschlote in die Land­schaften eindringen.",
        "In vielen Gegenden ist es so, daß selbst die Sagen von jenen alten Traumwelten schon verklungen sind.",
        "In Gegenden, welche noch weniger von der neueren Industrie- und Verkehrskultur angenommen haben, wie in gewissen Gebieten Norwegens, haben sich so schöne Teile jener Sagenwelt erhalten, wie unser Lied von Olaf Ästeson ist.",
        "Es stammt aus alten Zeiten; lebte aber vor kurzem wieder im norwegischen Volke auf und verbreitet sich schnell, so daß es heute wieder viele Menschen kennen, nachdem es lange verschollen war."
      ],
      [
        "Es erzählt einen langen Traum, den Olaf Ästeson träumt, und in welchem er erlebt das Schicksal der Seelen nach dem Tode.",
        "Die Vor­stellung liegt zu Grunde, daß die Seele nach dem Tode in die Sternen-welten wandelt, daß sie zum Beispiel in Gebiete kommt, wo die Stern­bilder des Stieres, der Himmelsschlange, des Hundes nahe sind, daß sie in die geistige Nähe des Mondes kommt."
      ],
      [
        "In diese Welten dringt die Seele ein, indem sie die Gjallarbrücke überschreitet, welche die irdische Welt mit der geistigen verbindet.",
        "In vielen Volkssagen wird der Regen­bogen als diese Brücke vorgestellt."
      ],
      [
        "Ein Teil dieser geistigen Welt ist Brooksvalin, wo die Lebenstaten der Seelen gewogen werden und ihnen die Vergeltung zuerteilt wird.",
        "Die ganze Art, wie das Lied das Erlebnis darstellt, weist auf die Zeit hin, in welcher es sich durch die Volks­dichtung gebildet hat."
      ],
      [
        "Die Vorstellungen über das Leben nach dem Tode sind noch nicht ganz die christlichen; sie sind zum Teile diejeni­gen, welche sich noch in der alten Heidenzeit gebildet haben.",
        "Doch wird als die Zeit, in welcher Olaf seinen Traum erlebt, schon die christ­liche Zeit vorgestellt."
      ],
      [
        "Das zeigt sich ja nicht nur dadurch, daß er seinen Traum vor der Kirchentüre erzählt, sondern auch dadurch, daß mitten in die heidnischen Vorstellungen von der Gjallarbrücke und Brooks­valin, die christlichen Vorstellungen von Michael und Christus hinein-spielen.",
        "Ja man kann in dem Herankommen des Christus aus dem Süden unmittelbar das Eindringen des Christentums nach Norwegen von"
      ],
      [
        "Süden her erkennen.",
        "Man hat es zu tun mit einer wohl acht bis neun Jahrhunderte alten Volksdichtung, denn vor so langer Zeit drang das Christentum in Norwegen ein."
      ],
      [
        "Wir möchten durch den Vortrag dieser Dichtung Ihren geistigen Blick auf das Leben der Volksseele lenken, die durch solche Sagen-bildung wie die von Olaf Ästeson zeigt, daß sie sich ihres Zusammen­hanges mit der geistigen Welt bewußt war, die von diesem Zusammen­hang innerlich Bilder erlebte, die ihr die Gewißheit gaben, daß die geistige Welt Dasein hat.",
        "Denn wer an Olaf Ästeson herangetreten wäre und etwa ihm gesagt hätte: so etwas gibt es nicht, das hat die Natur­wissenschaft bewiesen: den hätte Olaf Ästeson recht mitleidig an­geschaut, hätte dann wohl teilnahmsvoll gelächelt und gesagt: es gibt mehr Dinge im Himmel und auf Erden, als du dir mit deiner Schul­weisheit erträumst."
      ]
    ]
  },
  {
    "order": 12,
    "title_de": "ANSPRACHE für die russischen Zuhörer des Vortragszyklus «Die geistigen Wesenheiten in den Himmelskörpern und Naturreichen» Helsingfors, 11. April 1912",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Wir versuchen in das theosophische Leben und die theosophische Er­kenntnis nach und nach einzudringen, wir haben aber während dieses unseres Eindringens offenbar oftmals das Herzensbedürfnis, uns zu fragen: Warum wollen und suchen wir Theosophie im Geistesleben der Gegenwart? - Wir brauchen wohl nicht allzusehr unser Gemüt, unser Herz anzustrengen, wenn solch eine Frage auftaucht, und es wird in unsere Seele hereinkommen ein Wort, das sogleich für unser Gefühl aufklärend und mehr noch als aufklärend wirken wird, das Wort Ver­antwortung. Verantwortung!",
      "Es soll uns dieses Wort etwas geben, wel­ches von vornherein in unserer Seele, in unserem Herzen ausschließen soll, daß wir Theosophie treiben aus irgendeinem persönlichen Sehn­suchtsbedürfnis heraus. Wenn wir verfolgen, was uns, vielleicht ohne daß wir uns dessen ordentlich bewußt werden können, befällt bei dem Worte Verantwortlichkeit gegenüber jenem Geistesleben, das wir als theosophisch bezeichnen, dann werden wir immer mehr und mehr darauf kommen, daß wir es der gegenwärtigen Menschheit und dem Besten in uns, was dieser gegenwärtigen Menschheit dienen kann, schul­dig sind, uns um Theosophie zu kümmern.",
      "Wir dürfen Theosophie nicht treiben bloß uns zur Freude, um uns irgendwie, weil wir dieses oder jenes persönliche Sehnsuchtsgefühl haben, an Theosophie zu be­friedigen, sondern wir müssen fühlen, daß Theosophie etwas ist, was die gegenwärtige Menschheit braucht, wenn überhaupt der Mensch­heitsentwickelungsprozeß weitergehen soll. Wir brauchen uns nämlich nur vor Augen zu halten, daß ohne Theosophie, oder wie man es nen­nen mag, ohne jenes spirituelle Leben, das wir meinen, die Mensch­heit der Erde einer trostlosen Zukunft entgegengehen müßte, wahrhaft einer trostlosen Zukunft.",
      "Dies aus dem einfachen Grunde, weil alle geistigen Impulse der Vergangenheit, alles das, was in der Vergangenheit",
      "den Menschen hat gegeben werden können an geistigen Impulsen, erschöpft ist, sich nach und nach auslebt und nichts von neuen Keimen in die Menschheitsentwickelung hineinbringen kann. Das, was kom­men müßte, wenn nur die alten Impulse fortwirken würden, wäre ein vielleicht heute noch ungeahntes, die Menschen nicht nur Überwälti­gendes, in äußerer Beziehung Überwältigendes, sondern betäubendes Dominieren, Überhandnehmen der bloß äußerlichen Technik und ein Zugrundegehen, weil aus der Menschenseele fortziehend, alles religiö­sen, wissenschaftlichen, philosophischen, künstlerischen und auch im höheren Sinne ethischen Interesses. Zu einer Art lebendiger Automaten würden die Menschen, wenn nicht neue geistige Impulse kommen wür­den. So müssen wir uns fühlen, wenn wir an Theosophie denken, als diejenigen, die ihr Karma dazu gebracht hat, etwas zu wissen von dem, daß die Menschheit neue Impulse braucht.",
      "Da dürfen wir uns wohl die Frage dann vorhalten: Was können wir, jeder einzelne, nach unseren besonderen Qualitäten, nach unseren be­sonderen Eigenschaften tun gegenüber diesem allgemeinen Verant­wortlichkeitsgefühl? - Lehrreich zu einer Beantwortung dieser Ge­fühls- und Herzensfrage ist ja die Art und Weise, vielleicht ganz be­sonders für Euch, meine lieben Freunde, wie Theosophie in der letzten Zeit in die Welt gekommen ist, und wie sie sich im Laufe der letzten Jahrzehnte heranentwickelt hat bis in unsere Tage herein. Wir dürfen nämlich niemals vergessen, daß so, wie in der neueren Zeit das Wort Theosophie in die Welt hereingefallen ist, etwas vorliegt wie ein geisti­ges Kulturwunder. Dieses geistige Kulturwunder knüpft an an eine Persönlichkeit, die als Persönlichkeit Euch, meine lieben Freunde, ja nahesteht, da sie ihre geistigen Wurzeln in einer gewissen Weise aus Eurem Volkstum geholt hat. Ich meine Helena Petrowna Blavatsky. Und für den Westeuropäer ist es unleugbar, in jeder Beziehung un­leugbar, daß der Körper, in dem die Individualität, die in dieser Inkar­nation Helena Petrowna Blavatsky hieß, eingeschlossen war, eben nur aus dem Milieu Osteuropas, Rußlands hervorgehen konnte. Denn sie hatte alle russischen Eigenschaften. Aber Helena Petrowna Blavatsky ist Euch genommen worden durch Umstände ganz besonderer Art; Helena Petrowna Blavatsky ist versetzt worden durch die besonderen",
      "karmischen Verhältnisse der Gegenwart nach dem Westen. Nun, fassen wir einmal ins Auge, was eigentlich für ein sonderbares Kulturwunder vorlag.",
      "Nehmen wir diese Persönlichkeit von Helena Petrowna Blavatsky. Sie war eine Persönlichkeit im Grunde genommen, die ihr ganzes Leben hindurch in vieler, vieler Beziehung Kind geblieben ist, richtiges Kind; eine Persönlichkeit, die ihr ganzes Leben hindurch nicht gelernt hat, wirklich logisch zu denken; eine Persönlichkeit, die ihr ganzes Leben hindurch nicht gelernt hat, ihre Leidenschaften, Triebe und Begierden auch nur einigermaßen im Zügel zu halten, die ins Extreme zu verfallen jederzeit in der Lage war; eine Persönlichkeit, die im Grunde genom­men eine sehr geringe wissenschaftliche Bildung hatte.",
      "Durch diese Persönlichkeit wird der Welt geoffenbart, man möchte sagen, wie es nicht anders sein konnte, durch das Medium einer solchen Persönlich­keit geoffenbart, chaotisch, durcheinandergeworfen, bunt, eine Summe der allergrößten ewigen Weistümer der Menschheit. Und derjenige, der in diesen Sachen bewandert ist, findet in Helena Petrowna Blavatskys Werken Weistümer, Wahrheiten, Erkenntnisse der Menschheit, welche die Intellektualität und die Seele von Helena Petrowna Blavatsky nicht verstehen konnten, nicht im entferntesten verstehen konnten.",
      "Es gibt nichts Klareres, wenn man nur unbefangen auf die ganzen Tat­sachen eingeht, als daß für alles, was im Werke von Helena Petrowna Blavatsky lag, die äußere Seele, die äußere Intellektualität von Helena Petrowna Blavatsky nur ein Umweg, nur ein Mittel war, daß sich da bedeutende, große spirituelle Mächte der Menschheit mitteilen konn­ten. Und es gibt auch nichts Klareres, als daß in der Art und Weise, wie es dazumal im Beginne des letzten Drittels des 19.",
      "Jahrhunderts ge­schehen sollte, auf niemanden in Westeuropa die Impression hätte so geschehen können. Es brauchte die ganz sonderbare, auf der einen Seite selbstlose, fast entselbstete, und auf der andern Seite wiederum radikal selbstische, egoistische Natur von Helena Petrowna Blavatsky, um das geschehen zu lassen durch höhere geistige Mächte, was geschehen ist.",
      "Die selbstlose Natur aus dem Grunde, weil jedes westeuropäische Ge­müt in die eigenen Denkformen, in den eigenen Intellekt das gebracht hätte, was geoffenbart worden ist. Und es brauchte die ganz selbstische,",
      "egoistische Art, weil in der damaligen grobklotzigen materialistischen Lebensart Westeuropas keine Möglichkeit geboten war, anders als aus einer solch radikalen Gemütsart heraus wie, man möchte sagen, Eisen-fäuste zu machen über die zarten Hände, welche zu hegen und zu pfle­gen hatten den Okkultismus der neueren Zeit. Es ist eine eigentümliche Erscheinung. Aber, meine lieben Freunde, Helena Petrowna Blavatsky ging nach dem Westen, ging nach derjenigen Kulturstätte, die nach ihrer ganzen Eigenart, nach ihrer ganzen Struktur und Konfiguration auf allen Gebieten, außer Amerika, das allermaterialistischste Kultur­gebiet unserer Gegenwart ist, nach einem Kulturgebiet, das in seiner Sprache, in seinem Denken absolut in materialistischen Gedanken fährt, und in materialistischen Gefühlen lebt. Es würde hier zu weit führen, auseinanderzusetzen, welche Macht Helena Petrowna Blavatsky ge­rade nach England geführt hat. Und so sehen wir denn, daß die Summe des Okkultismus, der sich auf eine kulturwunderliche Art in einem Medium - ich meine das nicht in spiritistischem Sinne - auslebt, zu­nächst nach dem europäischen Westen strebt.",
      "Innerhalb dieses europäischen Westens war zunächst das Schicksal dieses Okkultismus nach einer gewissen Richtung hin besiegelt, denn es ging nicht anders, als daß sich mit der Begründung der theosophischen Bewegung in diesem materialistischen europäischen Westen ein bedeut­sames Karma erfüllte. Dieses Karma erfüllte sich auch. Dieser euro­päische Westen hat eine starke karmische Schuld; er kann nicht in die Geheimnisse (,es Daseins eindringen, ohne daß diese karmische Schuld in einer gewissen Weise sich geltend macht. Wenn Okkultismus irgend­wo in Frage kommt, dann vertieft sich sogleich das Karma, dann wer­den gleich Kräfte an die Oberfläche gespielt, die sonst mm Verborgenen bleiben. Und nicht um irgend etwas zu kritisieren, sondern um zu cha­rakterisieren, wird gesagt, was gesagt werden soll: Der europäische Westen hat, indem er etwas ausführte, was in geschichtlicher Weise notwendig ist, unzählige Ungerechtigkeiten vollzogen an dem Träger alter spiritueller Kultur, an dem Träger alter okkulter Geheimnisse, in dessen Leben zwar für die Gegenwart die spirituellen Dinge erstarrt, nicht mehr vorhanden sind, aber auf dem Grunde der Seele leben. -Denn so ist es in Wahrheit in Indien, in Südasien. In dem Augenblick,",
      "in welchem okkulte Impulse nach Westeuropa kamen, machte sich so­gleich die Reaktion geltend gegen die in den Tiefen des Indertums wir­kenden spirituellen Kräfte, und unmöglich wurde es nun - unmöglich wurde es schon zur Zeit von Helena Petrowna Blavatsky -, das zu be­halten, was allerdings von gewissen spirituellen Mächten intendiert war als die eigentliche in unserer Gegenwart notwendige spirituelle Bewegung. Unmöglich war das festzuhalten.",
      "Intendiert war, der Menschheit einmal eine Summe von okkulten Lehren zu geben, die für alle Menschen, für alle Herzen passen konnten, mit denen ein jeder, jeder hätte mitgehen können. Da aber durch gewisse Notwendigkeiten der Impuls verpflanzt wurde nach Westeuropa, machte sich eine ego­istische Reaktion geltend.",
      "Zurückgedrängt wurden diejenigen spirituel­len Mächte, die ohne Unterschied von irgendwelchen menschheitlichen Differenzen der Welt einen neuen Impuls geben wollten, und das einst­mals in seinem Okkultismus niedergedrückte Indien rächte sich kar­misch, indem es bei der ersten Gelegenheit, wo Okkultismus im Westen auftrat, diesen Okkultismus mit seinem eigenen nationalen egoistischen Okkultismus durchsetzte. Und das geschah zu Helena Petrowna Bla­vatskys Zeiten.",
      "Das geschah schon, indem Helena Petrowna Blavatsky die großen Wahrheiten und Weistumer ihrer «The Secret Doctrmne» ab-faßte. Ihr erstes Werk, die «Entschleierte Isis», zeigt nur das ganz Chao­tische und Unlogische und Leidenschaftliche und Durcheinanderwerfe­rische ihres Wesens, zeigt aber überall, daß hinter ihr wachende Mächte stehen, die sie nach dem allgemein Menschlichen hinführen wollen.",
      "In der «Sec ret Doctrin» waltet überall neben dem selbstverständlich Größ­ten menschliches Spezialinteresse, solches Interesse, das ausgeht von gewissen okkulten Zentren, die nicht heute das allgemein-menschliche Interesse im Auge haben, sondern ein partielles, ein Spezialinteresse. Tibetanische, indische, auch ägyptische Einweihung von heute haben überall partiell menschliches Interesse nur im Auge, wollen nur an der westlichen Welt den unterdrückten östlichen Okkultismus rächen, wol­len die Tatsache rächen, daß die westliche Welt durch materialistische Faktoren über die östliche Welt gesiegt hat.",
      "Sie hat durch materiali­stische Faktoren über die östliche Welt gesiegt; sie hat insofern gesiegt, als in die eigentliche fortschreitende Kultur der Menschheitsentwickelung,",
      "in das fortschreitende Leben der Menschheitsentwickelung das Christentum aufgenommen worden ist. Nach dem Osten von Asien ist das Christentum nicht hinübergegangen, nach dem Süden von Asien auch nicht; das Christentum ist nach Westen gezogen.",
      "Nun werdet Ihr vielleicht sagen, meine lieben theosophischen Freunde: Also ist es gut. Dann hat der Westen das Christentum ange­nommen, und da das Christentum eine Etappe im Weiterfortschreiten der Menschheit ist, so ist es selbstverständlich, daß der Westen über den Osten den Sieg davontrug. - Ja, wenn dies so wäre!",
      "Wenn es so wäre, wäre es selbstverständlich. Aber es ist nicht so. Das Christentum, das durch Jahrhunderte und Jahrtausende vorbereitet worden ist und das in die Welt gekommen ist, hat noch nirgends auf der Erde gesiegt.",
      "Und derjenige, der heute glauben würde, daß er in wahrem, echtem Sinn das Christus-Prinzip und den Christus-Impuls schon in der Gegen­wart vertreten könnte, würde einem unbeschreiblichen Hochmut zum Opfer gefallen sein. Was ist denn bisher überhaupt geschehen?",
      "Nichts anderes, als daß die westlichen Völker gewisse alleräußerste Außerlich­keiten von dem Christentum aufgenommen haben, den Christus-Namen okkupiert haben, und mit dem christlichen Namen ihre alten, vor dem Christentum in Europa seßhaft gewesenen Kulturen umkleidet haben, ihre nur in den modernen Industrialismus umgewandelten kriegerischen Kulturen. Herrscht der Christus innerhalb des christlichen Europa?",
      "Jeder Angehörige von okkulten Bewegungen wird niemals zugeben, daß der Christus innerhalb des christlichen Europas herrsche, sondern er wird sagen: Ihr sprecht «Christus», ihr meint aber immer noch das­selbe, was die alten mitteleuropäischen Völkerschaften gemeint haben, als sie von ihrem Gott Saxnot sprachen. - Das Symbolum des Cruci­fixus steht über den europäischen Völkern. In gewisser Beziehung herrschen aber die Traditionen des Gottes Saxnot, dessen Symbolum das ehemalige kurze sächsische Schwert ist, das da war zur Ausbrei­tung nur der materiellen Interessen zunächst, denn das war der Beruf der europäischen Völkerschaften.",
      "Daher hat auch dieser Beruf die edelste Blüte materialistischer Kultur hervorgebracht, eine Erscheinung, die edel ist auf dem Gebiet materialistischer Kultur: das Rittertum. Wo gibt es irgendwo in einer Kultur etwas Ahnliches wie das Rittertum",
      "der westlichen Kultur? Das gibt es sonst nicht. Niemandem wird es einfallen, die Helden des trojanischen Krieges zu vergleichen mit den mittelalterlichen Rittern. Der Christus lebt noch wenig bei den Men­schen. Von dem Christus sprechen die Menschen nur. Die östlichen Völker fühlen dann, wenn die westlichen von dem Christus sprechen, daß sie - diese östlichen Völker - allerdings in bezug auf die spirituelle Erfassung der Welt, in bezug auf das, was diese Völker wissen von den Geheimnissen des Daseins, weit voraus sind, weit, weit voraus sind. Das wissen diese östlichen Völker.",
      "Ganz gewöhnliche Dinge können es Euch erklären, daß die östlichen Völker in einer gewissen Weise ihre Vorzüge in spiritueller Beziehung schon zu schätzen wissen können. Was tun die westlichen Völker heute noch in ihrer Masse, in ihrer Mehrzahl, wenn Geheimnisse des Daseins enthüllt werden?",
      "Nun, wir sitzen noch in recht kleinen Scharen beisam­men, wenn wir sprechen, sagen wir von so etwas, wie gestern Abend gesprochen worden ist, von den waltenden spirituellen Mächten und Geheimnissen, die uns überall umgeben. Für den gewöhnlichen West-europäer ist das eine Torheit oder ein Wahnsinn, denn er kann noch immer nicht das Wort des Paulus verstehen: Was die Weisheit ist vor Gott, das ist vor den Menschen eben oftmals die Torheit, und was die Torheit ist vor den Menschen, das ist die Weisheit vor Gott. - Und nur diejenigen, die angesteckt sind von den Westeuropäern im Orient, wür­den wagen, auch nur im allergeringsten zu deuteln an den tiefen Wahr­heiten über die spirituellen Geheimnisse des Kosmos, wie wir sie ver­suchen wiederum zu enthüllen, wenn sie sie hören, denn als etwas Selbstverständliches gelten solche Dinge, wie sie zum Beispiel gestern gesagt worden sind, denjenigen, die im östlichen spirituellen Leben drinnen sind.",
      "Wundern wir uns daher nicht, daß es oftmals diesen öst­lichen Völkern vorgekommen ist, wenn die Europäer über sie herge­fallen sind, wie es eben einer Schar von Menschen vorkommt, wenn ihnen eine Herde wilder Tiere entgegenkommt, gegen die sie sich weh­ren, denen sie das, was sie tun, nicht übelnehmen, die sie aber als etwas Inferiores betrachten. Wir Westländer werden aus den angedeuteten Gründen - ob das heute berechtigt ist oder nicht, darauf kommt es hier nicht an - und nach den Traditionen des Ostens von jedem Angehörigen",
      "etwa des Brahmanentums selbstverständlich als inferiore Men­schen angesehen.",
      "Und wenn wir absehen von dem Brahmanentum und sehen etwa in die Kulturen Mittelasiens, in die tibetanische oder chinesische Kultur, die in der nächsten Zeit in einer Weise werden für die Welt Bedeutung gewinnen, wovon sich die Menschen heute nichts träumen lassen, trotz­dem uns nur kurze Zeit von dieser Sache trennt, wenn wir auf alle diese Dinge sehen und gewahr werden, wie die Seelen vieler Zarathu­stra-Schüler in diesen Kulturen noch verkörpert sind, dann werden wir versucht werden, diese Dinge sehr ernst zu nehmen. Wir werden es auch begreifen können, daß in dasjenige, was Helena Petrowna Bla­vatsky zu geben verstand, der indische, der tibetanische, der ägyptische Okkultist versucht sein konnten, aus ihrer Seele heraus - ihr eigenes Weisheitsgut hineinzuleiten, jenes Eigene aber, das in dem Menschen­werdeprozeß einer Vergangenheit angehört.",
      "Und wir müssen den Ver­gangenheitscharakter dieser orientalischen Weisheitsgüter erkennen, die innerhalb der Blavatskyschen Lehren stecken. Wir brauchen ja den Wert einer solchen Sache nicht zu verkennen, brauchen nicht zu ver­kennen, daß wenn nun überfluten wird das, man möchte sagen, seine Fesseln gesprengt habende Chinesentum die westlichen Welten, dann eine Spiritualität damit kommt, die richtig die Nachfolge ist, in vieler Beziehung die noch ungetrübte Nachfolge ist des alten Atlantiertums.",
      "Sie wird wirken, wie wenn aufspringen würde etwas, was zusammen­gehalten wird, und was nach aller Welt sich verbreiten kann; so wird es sich ausgießen - in kleinem Maßstabe hat sich so bei der ersten Ge­legenheit ausgegossen das alte Indertum.",
      "Daher war es möglich, meine lieben theosophischen Freunde, daß von jener Zeit an alles das eingetreten ist, wofür man in allem Okkul­tismus ein bezeichnendes Wort hat, daß von da ab im Grunde genom­men die theosophische Bewegung nicht mehr ein geeignetes Instrument war für die Fortbewegung der Kultur Europas. Jeder Okkultist kennt gut das Wort, das da heißt: Es darf niemals bei den leitenden Mächten des Okkultismus oder bei den in irgendeiner Weise okkult Tätigen irgendein spezielles Interesse überwiegen das allgemeine Interesse der Menschheit. - Es gibt keine Möglichkeit, okkult günstig zu wirken,",
      "wenn ein spezielles Interesse überwiegt das allgemeine menschliche In­teresse. In dem Augenblick, wo in den Okkultismus eindringt ein spe­zielles Interesse anstelle der allgemein-menschlichen Interessen, sind die Möglichkeiten zu realen Irrtümern gegeben.",
      "Daher kommt es, daß seit jener Zeit in die theosophische Bewegung jeder mögliche Irrtum hineinkonnte. Durch die Art und Weise, wie England mit Indien ver­knüpft ist karmisch im Weltzusammenhang, war einfach die Möglich­keit gegeben, daß jene erhabenen Mächte, die am Ausgangspunkt der theosophischen Bewegung stehen, gefälscht wurden.",
      "Denn das ist ein gewöhnlicher Vorgang im Okkultismus, daß Mächte, die ihr Spezial-interesse verfolgen wollen, die Gestalt derjenigen annehmen, welche die eigentlichen Impulse vorher gegeben haben. So gab es von einer gewissen Zeit der theosophischen Bewegung an gar keine Möglichkeit mehr, so ohne weiteres alles hinzunehmen, was innerhalb dieser theo­sophischen Bewegung lag, und das Karma hat es gewollt, daß dies immer weniger und weniger möglich geworden ist.",
      "Und so konnte denn nichts anderes getan werden, als in dem Augenblick, wo der Ruf an uns erging, uns zu vereinigen mit dieser theosophischen Bewegung, es konnte nichts anderes getan werden, als auf die ursprünglichen Quellen wieder zurückzugehen, auf diejenigen Quellen, die wir im Gegensatz zu den speziellen die allgemein-menschlichen nennen können. Und so habt Ihr vielleicht gesehen in Mitteleuropa, daß wir versuchen, an die okkulten Quellen heranzukommen so, daß Ihr nicht bemerken werdet an alldem, was Euch da entgegentritt, daß irgendein spezielles Interesse damit verknüpft ist.",
      "Alles, was an speziellen Interessen aufgefunden werden kann in Mitteleuropa, versucht Ihr es zu vergleichen mit dem, was Ihr kennenlernt als jene Theosophie, die unter uns getrieben wird:",
      "Es lassen sich die beiden Dinge wirklich nicht zusammenbringen. - Ihr könnt diese Theosophie nehmen und findet wahrscheinlich außerdem, daß, weil in einer Sprache schon einmal geschrieben werden muß, die Bücher von mir selber in deutscher Sprache geschrieben sind, findet Ihr wohl nichts Deutsches in der Theosophie, nichts, was irgendwie mit den äußeren Traditionen Mitteleuropas zusammenhängt. Und wo irgend die Tendenz auftritt, mit einem Spezialinteresse die Theosophie zu ver­binden, gibt es sogleich eine Unmöglichkeit.",
      "Das ist nun die besondere Aufgabe Mitteleuropas gewesen, die Theosophie zu erlösen von den speziellen Eigentümlichkeiten, die sie erhalten hat im europäischen Westen. Es war unsere Mission, die Theo­sophie rein, rein herauszulösen von allen Spezialinteressen.",
      "Und je weiter Ihr eingehen werdet auf die Dinge, werdet Ihr finden, daß ich gewissermaßen selber in der Lage war loszulösen alles, was ich theo­sophisch bringen durfte, von einem jeglichen Spezialinteresse. Es ist das eine symbolische Angabe, meine lieben theosophischen Freunde, aber symbolisch gesprochen - ich brauchte mich nur leiten zu lassen von dem, was als ein unmittelbarer Impuls in der gegenwärtigen Inkarna­tion vorhanden war, mißversteht es nicht, es gibt ja nur eine Tatsache wieder -: diejenigen, welche die äußeren Träger zum Beispiel jenes Blutes waren, aus dem ich stamme, sie stammten aus deutschen Gegen­den Österreichs; da konnte ich nicht geboren werden.",
      "Ich selber bin in einer slawischen Gegend, in einer Gegend, die vollständig fremd war dem ganzen Milieu und der ganzen Eigentümlichkeit, aus der meine Vorfahren stammen, geboren. So drängte sich mir - ich will das nur symbolisch anführen - im Ausgangspunkt meiner gegenwärtigen In­karnation sinnbildlich von selber auf, daß wir in Mitteleuropa den Be­ruf hatten, uns loszulösen von allem Spezialinteresse die Theosophie, so daß sie in Mitteleuropa wirklich vor uns steht wie eine Göttin, wie etwas ganz, ganz von allem Menschlichen losgelöstes Göttliches, das ebensoviel zu tun hat mit dem Menschen, der da lebt, wie mit jenem, der dort lebt, und das wird immer bleiben müssen.",
      "Das Ideal, das wir haben, meine lieben theosophischen Freunde, so einfach, als es sich ausdrückt, es wird immer vor uns stehen müssen, weil es schwerer zu erfüllen ist, als auszusprechen. Es wird vor uns stehen müssen als unser Ideal die Wahrheit und Aufrichtigkeit, die ungefärbte göttliche Wahrheit. Vielleicht gerade, wenn wir uns so be­streben, werden wir den Weg finden, nicht für uns, sondern für das, was in Mitteleuropa nach der ganzen Mission Europas unpersönlich war, für diese göttliche Theosophie hinüber nach dem Osten. Und da, wenn ich, ich möchte sagen, nun den Weg weiter beschreibe, wie die Theosophie im Westen Platz gegriffen hat, durch Europa durchgeht und nach dem Osten kommen soll, da möchte ich das Wort wiederum",
      "hierhersetzen, scharf, scharf das Wort: Verantwortlichkeitsgefühl. Die Kulturen in der Welt, sie entwickeln sich so, daß sich gleichsam wie in einer geistigen Hülle die eine Kultur mit der andern entwickelt. Die eine Kultur verbindet sich mit der andern. Dadurch, daß die Theo-sophie in Mitteleuropa so unpersönlich sein mußte, hat sie einen gewis­sen Charakter der Geistigkeit bekommen, der von allen Interessen los­gelösten Geistigkeit. Diese Theosophie hat dadurch, meine lieben theo­sophischen Freunde, etwas Sprödes; sie hat das Spröde, das die Unbe­rührtheit von den speziellen Interessen hat; sie wird daher denjenigen nicht gefallen, welche ihr Herz nicht aufschließen können gegenüber dem, das eben nicht irgendeinem speziellen Interesse dient.",
      "Das Geistige, das sie hat, diese Theosophie, kann aber gefunden werden von der Seele, die nach diesem Geistigen dürstet, die nach die­sem Geistigen sich sehnt. Und da muß ich sagen, meine lieben theoso­phischen Freunde, ich habe kennengelernt aus der geistigen Welt selber heraus eine Seele, die sich sehr sehnt nach dem Geiste, der durch die Theosophie sich ausdrückt.",
      "Ich habe kennengelernt diese Seele in der rein geistigen Welt. Wenn wir in der Reihenfolge der Hierarchien hin­aufgehen zu den einzelnen Völkergeistern und sprechen innerhalb der einzelnen Völkergeister von den Volksseelen, dann kommen wir auch unter den Volksseelen, die sozusagen heute noch jung sind und die sich fortentwickeln müssen, wie jedes Wesen sich entwickeln muß, zur rus­sischen Volksseele.",
      "Von dieser russischen Volksseele weiß ich, daß sie sich sehnt nach dem Geist, der in der Theosophie zum Ausdruck kommt. Sie sehnt sich mit allen Kräften, die sie entwickeln kann. Ich spreche von dem Verantwortlichkeitsgefühl, weil Ihr, meine lieben theosophi­schen Freunde, Kinder seid dieser russischen Volksseele.",
      "Sie waltet und wirkt in Euch und Ihr habt ihr gegenüber eine Verantwortung. Die Verantwortung, versteht sie zu lernen! Nehmt es nicht übel; viel, viel konnte mir sagen oftmals diese russische Volksseele.",
      "Am tragischsten trat mir das vor Augen, was diese russische Volksseele mir sagen konnte, etwa um das Jahr 1900 herum. Es trat am tragischsten dazumal zutage, weil einem da auffallen konnte etwas, das ich mir selber erst lange hinterher in der richtigen Weise interpretieren konnte, weil einem da auffallen konnte, wie wenig im Grunde genommen diese russische",
      "Volksseele heute noch verstanden wird. Wir haben in Westeuropa ken­nengelernt vieles, vieles aus Rußland, und vieles, vieles aus Rußland hat auf uns einen großen, gewaltigen Eindruck gemacht. Wir haben kennengelernt die großen Impulse Tolstojs, haben kennengelernt das Westeuropa so tief ergreifende der Psychologie von Dostojewskij und wmr haben endlich kennengelernt einen solchen Geist wie Solowjow, emnen Geist, der, wenn man ihn auf sich wirken läßt, überall den Ein­druck macht: so ist er, wie er geschrieben hat.",
      "Und wie er geschrieben hat, es bekommt erst das rechte Licht, wenn man hinter ihm stehend fühlt die russische Volksseele. Und diese russische Volksseele, sie weiß viel, viel mehr zu sagen, als selbst Solowjow zu sagen weiß, denn da kommt uns noch immer viel, viel zuviel von Westeuropa Angenommenes vor die Herzen.",
      "Denkt einmal, meine lieben Freunde, an das Wort Ver­antwortlichkeitsgefühl, denkt daran, daß ihr diese Aufgabe habt, Euch würdig zu zeigen der russischen Volksseele gegenüber, und daß Ihr kennenlernen sollt die Sehnsucht der russischen Volksseele nach der un­persönlichen Theosophie. Wenn Ihr Theosophie kennenlernt in dem, was sie in ihrem innersten Impuls will, dann, meine lieben Freunde, werdet Ihr allerhand Fragen zu stellen haben, die nur aus einer russi­schen Seele herauskommen können: Seelenfragen zu den Geistesfragen der Theosophie.",
      "Ich habe es erfahren, daß viel edles, herrliches, schönes Gefühl mir entgegengetreten ist von Osteuropa, so viel von echter, wahrer Menschenliebe und Menschengüte, von menschlichem Mitleid, von überfließendem Gefühl, als sich nur denken läßt, von feiner, in­timer Beobachtung dessen, was in der Welt gegeben ist, von einem in­tensiven persönlichen Verknüpftsein mit den Mächten des Daseins. Und aus solchen lieben und schönen und edlen Gefühlen sind viele, viele Fragen von Angehörigen des russischen Volkes an mich gestellt worden, viele Fragen - Fragen, die einmal gestellt werden müssen, weil sie Fragen sind, ohne deren Beantwortung die Menschheit in der Zukunft wird nicht leben können.",
      "Fragen, die nur vom Osten Europas kommen können, sie hat bisher an mich nur die russische Volksseele ge­stellt, die russische Volksseele auf den höheren Planen. Oftmals mußte ich denken, daß die Kinder dieser Volksseele noch einen Weg haben, um ihre Volksseele zu verstehen, um zu verstehen, was diese Volksseele",
      "eigentlich ersehnt, und wieviel sie noch trennt, diese Kinder der Volks­seele, von dieser Volksseele selbst. Scheut es deshalb nicht, den Weg zu suchen, den Ihr finden könnt, wenn Ihr wollt, zu Eurer Volksseele.",
      "Aus Eurer Volksseele heraus werdet Ihr diejenigen Fragen finden, ohne deren Beantwortung die Menschheit der Zukunft nicht wird sein kön­nen. Aber scheut es nicht, über das persönliche Interesse dabei heraus­zukommen, denn seid eingedenk des großen Verantwortlichkeitsge­fühls, das Ihr haben sollt gegenüber der russischen Volksseele, seid ein­gedenk dieses Gefühles, denn in der Zukunft brauchen die Volksseelen ihre Kinder, die Menschen, um ihre Ziele zu erreichen.",
      "Und vergeßt dabei eines nicht. Dasjenige, das einen am höchsten tragen kann, das einen in die schönsten, lichtesten Höhen der Welt bringen kann - das ist am meisten der Gefahr ausgesetzt, in Irrtümer zu verfallen. - Ihr sollt, meine lieben theosophischen Freunde, das Geistige durchseelen.",
      "Ihr sollt finden die Seele zum Geiste. Ihr könnt es, weil die russische Volksseele unermeßliche Tiefen und Möglichkeiten des Zukünftigen hat. Aber notwendig ist es, daß Ihr Euch bewußt seid, daß das See­lische, das sich zum Geiste erheben kann, den Geist selber zu durch-seelen hat, Euch vor die große Gefahr stellt, Euch zu verlieren und in dem Persönlichen, in dem individuell Persönlichen steckenzubleiben, zu verlieren in dem Persönlichen als solchem.",
      "Dann wird das Persön­liche nämlich stark, wenn es stammt aus dem Seelischen.",
      "Es werden nicht jene Hindernisse bei Euch auftreten, die so viel­fach in West- und Mitteleuropa auftreten. Zur Skepsis seid Ihr weniger geboren; Skepsis kann nur durch Einimpfung von Westen zu Euch kommen. Ihr werdet durch ein bestimmtes Gefühl die Wahrheit von der Unwahrheit und Unredlichkeit unterscheiden lernen auf dem Ge­biet des Okkultismus, wo Scharlatanerie und Wahrheit so dicht bei­sammenstehen. Nicht der Skeptizismus, der Zynismus werden Eure Gefahr bilden. Eure Gefahr wird bilden, daß das seelisch Machtvolle Eurer Persönlichkeiten Wolken um Euch verbreiten kann, astralische Wolken, durch die Ihr dann nicht durchkönnt bis zum objektiv Gei­stigen. Euer Feuer, Eure Wärme, sie können sich wie eine wolkige Aura um Euch herum breiten, nicht durchlassen das Geistige, weil Ihr meint, für den Geist begeistert zu sein, aber durch die Begeisterung verhindert",
      "den Geist, die Wege zu Euch zu finden. So versucht, das ins Auge zu fassen, daß Ihr in dem großen Vorteil seid - das jetzt in dem idealen spirituellen Sinn gemeint -, ein spezielles Interesse haben zu dürfen, weil Ihr prädestiniert seid, das heißt Eure Volksseele, in das spezielle Interesse des russischen Volkstums die Theosophie, die man in Mittel­europa noch ganz wie nur eine über allem Menschlichen erhabene gött­liche Macht nehmen mußte, empfangen zu dürfen, wie kein anderes Volk sie empfangen kann, wie etwas, was Ihr als Euer Eigenstes hegen und pflegen dürft. Denn durch Eure Prädestination seid Ihr dazu aus­gestattet, Seele dem Geist einzuhauchen. Das ist oftmals in unseren Reihen gesagt worden, aber an Euch liegt es, die Gelegenheit sobald als möglich herbeizuführen, sie nicht zu versäumen, nicht bloß Gefühl und Wille zu entwickeln, sondern vor allen Dingen Energie und Aus­dauer zu entwickeln, weniger - wenn auch ein Wort in bezug auf das Praktische geredet werden soll - reden über die Art, wie Theosophie im Westen sein muß und wie sie in Rußland sein muß und so weiter und was für das eine und andere gut ist, sondern zunächst aufnehmen Theosophie, aufnehmen, mit der Seele, mit dem Herzen vereinigen. Das Übrige wird sich schon ergeben; es wird sich sicher ergeben.",
      "Das ist so etwas von dem, meine lieben Freunde, was ich habe zu Euch sprechen wollen, sprechen wollen deshalb, weil überall, wo ich unmittelbar zum Menschen sprechen soll, vor Augen stehen muß eben das Verantwortlichkeitsgefühl, das wir Menschen der Gegenwart gegen­über der Theosophie haben. Im Westen sollen die Menschen das Gefühl haben, daß sie sich an der Menschheit versündigen, wenn sie etwas von Theosophie haben können und es nicht wollen, es abweisen - Sünde gegen die Menschheit! Es ist manchmal recht schwer zu fassen, denn man muß ein fast transzendentales Pflichtgefühl haben, meine lieben Freunde, wenn man solche Verpflichtung, solch ein Verantwortlich­keitsgefühl gegenüber der Menschheit haben soll. Euch sagt Eure Volks­seele, daß sie, diese Volksseele selber, Euch verpflichtet. Für Euch hat schon die Volksseele diese Verpflichtung gegenüber der Menschheit übernommen. Ihr braucht sie nur zu finden, diese Volksseele. Ihr braucht sie nur durch Eure Gedanken, Empfindungen und Willens-impulse sprechen zu lassen, und Ihr werdet, wenn Ihr die Verantwortlichkeit",
      "gegenüber der Volksseele fühlt, zugleich erfüllen die Pflicht gegenüber der Menschheit. Deshalb seid Ihr auch äußerlich örtlich hin­eingestellt zwischen den europäischen Westen, der Theosophie haben muj', für den sie aber in dem Grade wie für Euch nicht eine persönliche Angelegenheit werden kann, und den asiatischen Osten, der Okkultis­mus und spirituelle Kultur seit Urzeiten hat.",
      "Ihr seid hineingestellt. Ihr würdet vielleicht niemals dazukommen, Eure Aufgabe gegenüber der spirituellen Kultur der Menschheit zu erfüllen in dieser geographisch schwierigen Lage, möchte ich sagen, wenn Ihr nur an die Verpflichtung gegenüber der Menschheit denken müßtet.",
      "Denn die Versuchungen werden üngeheuer groß sein, wenn auf der einen Seite nicht nur der europäische Westen wirkt, der viele der Kinder Eurer Volksseele im Grunde genommen sich selber hat untreu werden lassen. Einem großen Teil dessen, was von Russen geschrieben und uns nach Westen gebracht wird, gegenüber haben wir das Gefühl, daß es nichts zu tun hat mit der russischen Volksseele, sondern ein Spiegelbild aller möglichen west­lichen Dinge ist.",
      "Die zweite Versuchung wird die von Osten sein, wenn die Macht spiritueller Kultur kommt. Da wird es die Pflicht sein, zu wissen, daß bei aller Größe dieser spirituellen Kultur des Ostens der Mensch der Gegenwart sich zu sagen hat: Nicht die Vergangenheit haben wir in die Zukunft hineinzutragen, sondern die neuen Impulse.",
      "Nicht aufzunehmen wird sein einfach irgendein spiritueller Impuls des Ostens, sondern zu pflegen das, was der Westen aus den spirituellen Quellen selber hervorbringen kann. - Dann wird die Zeit kommen, in der Europa anfangen wird, wenn Ihr Eure Pflichten auch erfüllt gegen­über Eurer Volksseele, ein wenig zu verstehen, was eigentlich der Chri­stus-Impuls in der geistigen Entwickelung der Menschheit ist. Sucht alles das, was ich habe mit und in diesen Worten sagen wollen, meine lieben Freunde, und sucht vor allen Dingen das in diesen Worten, was in Euch selber Impuls werden kann, nicht bloß zu fühlen und zu emp­finden, daß Theosophie etwas Bedeutendes und etwas Großes ist, son­dern sucht vor allen Dingen, Theosophie in die Tat und in die Willens­impulse Eurer Seele aufzunehmen und aus ihr heraus Euer Leben, aus ihr heraus Eure Taten einzurichten."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Wir versuchen in das theosophische Leben und die theosophische Er­kenntnis nach und nach einzudringen, wir haben aber während dieses unseres Eindringens offenbar oftmals das Herzensbedürfnis, uns zu fragen: Warum wollen und suchen wir Theosophie im Geistesleben der Gegenwart? - Wir brauchen wohl nicht allzusehr unser Gemüt, unser Herz anzustrengen, wenn solch eine Frage auftaucht, und es wird in unsere Seele hereinkommen ein Wort, das sogleich für unser Gefühl aufklärend und mehr noch als aufklärend wirken wird, das Wort Ver­antwortung.",
        "Verantwortung!"
      ],
      [
        "Es soll uns dieses Wort etwas geben, wel­ches von vornherein in unserer Seele, in unserem Herzen ausschließen soll, daß wir Theosophie treiben aus irgendeinem persönlichen Sehn­suchtsbedürfnis heraus.",
        "Wenn wir verfolgen, was uns, vielleicht ohne daß wir uns dessen ordentlich bewußt werden können, befällt bei dem Worte Verantwortlichkeit gegenüber jenem Geistesleben, das wir als theosophisch bezeichnen, dann werden wir immer mehr und mehr darauf kommen, daß wir es der gegenwärtigen Menschheit und dem Besten in uns, was dieser gegenwärtigen Menschheit dienen kann, schul­dig sind, uns um Theosophie zu kümmern."
      ],
      [
        "Wir dürfen Theosophie nicht treiben bloß uns zur Freude, um uns irgendwie, weil wir dieses oder jenes persönliche Sehnsuchtsgefühl haben, an Theosophie zu be­friedigen, sondern wir müssen fühlen, daß Theosophie etwas ist, was die gegenwärtige Menschheit braucht, wenn überhaupt der Mensch­heitsentwickelungsprozeß weitergehen soll.",
        "Wir brauchen uns nämlich nur vor Augen zu halten, daß ohne Theosophie, oder wie man es nen­nen mag, ohne jenes spirituelle Leben, das wir meinen, die Mensch­heit der Erde einer trostlosen Zukunft entgegengehen müßte, wahrhaft einer trostlosen Zukunft."
      ],
      [
        "Dies aus dem einfachen Grunde, weil alle geistigen Impulse der Vergangenheit, alles das, was in der Vergangenheit"
      ],
      [
        "den Menschen hat gegeben werden können an geistigen Impulsen, erschöpft ist, sich nach und nach auslebt und nichts von neuen Keimen in die Menschheitsentwickelung hineinbringen kann.",
        "Das, was kom­men müßte, wenn nur die alten Impulse fortwirken würden, wäre ein vielleicht heute noch ungeahntes, die Menschen nicht nur Überwälti­gendes, in äußerer Beziehung Überwältigendes, sondern betäubendes Dominieren, Überhandnehmen der bloß äußerlichen Technik und ein Zugrundegehen, weil aus der Menschenseele fortziehend, alles religiö­sen, wissenschaftlichen, philosophischen, künstlerischen und auch im höheren Sinne ethischen Interesses.",
        "Zu einer Art lebendiger Automaten würden die Menschen, wenn nicht neue geistige Impulse kommen wür­den.",
        "So müssen wir uns fühlen, wenn wir an Theosophie denken, als diejenigen, die ihr Karma dazu gebracht hat, etwas zu wissen von dem, daß die Menschheit neue Impulse braucht."
      ],
      [
        "Da dürfen wir uns wohl die Frage dann vorhalten: Was können wir, jeder einzelne, nach unseren besonderen Qualitäten, nach unseren be­sonderen Eigenschaften tun gegenüber diesem allgemeinen Verant­wortlichkeitsgefühl? - Lehrreich zu einer Beantwortung dieser Ge­fühls- und Herzensfrage ist ja die Art und Weise, vielleicht ganz be­sonders für Euch, meine lieben Freunde, wie Theosophie in der letzten Zeit in die Welt gekommen ist, und wie sie sich im Laufe der letzten Jahrzehnte heranentwickelt hat bis in unsere Tage herein.",
        "Wir dürfen nämlich niemals vergessen, daß so, wie in der neueren Zeit das Wort Theosophie in die Welt hereingefallen ist, etwas vorliegt wie ein geisti­ges Kulturwunder.",
        "Dieses geistige Kulturwunder knüpft an an eine Persönlichkeit, die als Persönlichkeit Euch, meine lieben Freunde, ja nahesteht, da sie ihre geistigen Wurzeln in einer gewissen Weise aus Eurem Volkstum geholt hat.",
        "Ich meine Helena Petrowna Blavatsky.",
        "Und für den Westeuropäer ist es unleugbar, in jeder Beziehung un­leugbar, daß der Körper, in dem die Individualität, die in dieser Inkar­nation Helena Petrowna Blavatsky hieß, eingeschlossen war, eben nur aus dem Milieu Osteuropas, Rußlands hervorgehen konnte.",
        "Denn sie hatte alle russischen Eigenschaften.",
        "Aber Helena Petrowna Blavatsky ist Euch genommen worden durch Umstände ganz besonderer Art; Helena Petrowna Blavatsky ist versetzt worden durch die besonderen"
      ],
      [
        "karmischen Verhältnisse der Gegenwart nach dem Westen.",
        "Nun, fassen wir einmal ins Auge, was eigentlich für ein sonderbares Kulturwunder vorlag."
      ],
      [
        "Nehmen wir diese Persönlichkeit von Helena Petrowna Blavatsky.",
        "Sie war eine Persönlichkeit im Grunde genommen, die ihr ganzes Leben hindurch in vieler, vieler Beziehung Kind geblieben ist, richtiges Kind; eine Persönlichkeit, die ihr ganzes Leben hindurch nicht gelernt hat, wirklich logisch zu denken; eine Persönlichkeit, die ihr ganzes Leben hindurch nicht gelernt hat, ihre Leidenschaften, Triebe und Begierden auch nur einigermaßen im Zügel zu halten, die ins Extreme zu verfallen jederzeit in der Lage war; eine Persönlichkeit, die im Grunde genom­men eine sehr geringe wissenschaftliche Bildung hatte."
      ],
      [
        "Durch diese Persönlichkeit wird der Welt geoffenbart, man möchte sagen, wie es nicht anders sein konnte, durch das Medium einer solchen Persönlich­keit geoffenbart, chaotisch, durcheinandergeworfen, bunt, eine Summe der allergrößten ewigen Weistümer der Menschheit.",
        "Und derjenige, der in diesen Sachen bewandert ist, findet in Helena Petrowna Blavatskys Werken Weistümer, Wahrheiten, Erkenntnisse der Menschheit, welche die Intellektualität und die Seele von Helena Petrowna Blavatsky nicht verstehen konnten, nicht im entferntesten verstehen konnten."
      ],
      [
        "Es gibt nichts Klareres, wenn man nur unbefangen auf die ganzen Tat­sachen eingeht, als daß für alles, was im Werke von Helena Petrowna Blavatsky lag, die äußere Seele, die äußere Intellektualität von Helena Petrowna Blavatsky nur ein Umweg, nur ein Mittel war, daß sich da bedeutende, große spirituelle Mächte der Menschheit mitteilen konn­ten.",
        "Und es gibt auch nichts Klareres, als daß in der Art und Weise, wie es dazumal im Beginne des letzten Drittels des 19."
      ],
      [
        "Jahrhunderts ge­schehen sollte, auf niemanden in Westeuropa die Impression hätte so geschehen können.",
        "Es brauchte die ganz sonderbare, auf der einen Seite selbstlose, fast entselbstete, und auf der andern Seite wiederum radikal selbstische, egoistische Natur von Helena Petrowna Blavatsky, um das geschehen zu lassen durch höhere geistige Mächte, was geschehen ist."
      ],
      [
        "Die selbstlose Natur aus dem Grunde, weil jedes westeuropäische Ge­müt in die eigenen Denkformen, in den eigenen Intellekt das gebracht hätte, was geoffenbart worden ist.",
        "Und es brauchte die ganz selbstische,"
      ],
      [
        "egoistische Art, weil in der damaligen grobklotzigen materialistischen Lebensart Westeuropas keine Möglichkeit geboten war, anders als aus einer solch radikalen Gemütsart heraus wie, man möchte sagen, Eisen-fäuste zu machen über die zarten Hände, welche zu hegen und zu pfle­gen hatten den Okkultismus der neueren Zeit.",
        "Es ist eine eigentümliche Erscheinung.",
        "Aber, meine lieben Freunde, Helena Petrowna Blavatsky ging nach dem Westen, ging nach derjenigen Kulturstätte, die nach ihrer ganzen Eigenart, nach ihrer ganzen Struktur und Konfiguration auf allen Gebieten, außer Amerika, das allermaterialistischste Kultur­gebiet unserer Gegenwart ist, nach einem Kulturgebiet, das in seiner Sprache, in seinem Denken absolut in materialistischen Gedanken fährt, und in materialistischen Gefühlen lebt.",
        "Es würde hier zu weit führen, auseinanderzusetzen, welche Macht Helena Petrowna Blavatsky ge­rade nach England geführt hat.",
        "Und so sehen wir denn, daß die Summe des Okkultismus, der sich auf eine kulturwunderliche Art in einem Medium - ich meine das nicht in spiritistischem Sinne - auslebt, zu­nächst nach dem europäischen Westen strebt."
      ],
      [
        "Innerhalb dieses europäischen Westens war zunächst das Schicksal dieses Okkultismus nach einer gewissen Richtung hin besiegelt, denn es ging nicht anders, als daß sich mit der Begründung der theosophischen Bewegung in diesem materialistischen europäischen Westen ein bedeut­sames Karma erfüllte.",
        "Dieses Karma erfüllte sich auch.",
        "Dieser euro­päische Westen hat eine starke karmische Schuld; er kann nicht in die Geheimnisse (,es Daseins eindringen, ohne daß diese karmische Schuld in einer gewissen Weise sich geltend macht.",
        "Wenn Okkultismus irgend­wo in Frage kommt, dann vertieft sich sogleich das Karma, dann wer­den gleich Kräfte an die Oberfläche gespielt, die sonst mm Verborgenen bleiben.",
        "Und nicht um irgend etwas zu kritisieren, sondern um zu cha­rakterisieren, wird gesagt, was gesagt werden soll: Der europäische Westen hat, indem er etwas ausführte, was in geschichtlicher Weise notwendig ist, unzählige Ungerechtigkeiten vollzogen an dem Träger alter spiritueller Kultur, an dem Träger alter okkulter Geheimnisse, in dessen Leben zwar für die Gegenwart die spirituellen Dinge erstarrt, nicht mehr vorhanden sind, aber auf dem Grunde der Seele leben. -Denn so ist es in Wahrheit in Indien, in Südasien.",
        "In dem Augenblick,"
      ],
      [
        "in welchem okkulte Impulse nach Westeuropa kamen, machte sich so­gleich die Reaktion geltend gegen die in den Tiefen des Indertums wir­kenden spirituellen Kräfte, und unmöglich wurde es nun - unmöglich wurde es schon zur Zeit von Helena Petrowna Blavatsky -, das zu be­halten, was allerdings von gewissen spirituellen Mächten intendiert war als die eigentliche in unserer Gegenwart notwendige spirituelle Bewegung.",
        "Unmöglich war das festzuhalten."
      ],
      [
        "Intendiert war, der Menschheit einmal eine Summe von okkulten Lehren zu geben, die für alle Menschen, für alle Herzen passen konnten, mit denen ein jeder, jeder hätte mitgehen können.",
        "Da aber durch gewisse Notwendigkeiten der Impuls verpflanzt wurde nach Westeuropa, machte sich eine ego­istische Reaktion geltend."
      ],
      [
        "Zurückgedrängt wurden diejenigen spirituel­len Mächte, die ohne Unterschied von irgendwelchen menschheitlichen Differenzen der Welt einen neuen Impuls geben wollten, und das einst­mals in seinem Okkultismus niedergedrückte Indien rächte sich kar­misch, indem es bei der ersten Gelegenheit, wo Okkultismus im Westen auftrat, diesen Okkultismus mit seinem eigenen nationalen egoistischen Okkultismus durchsetzte.",
        "Und das geschah zu Helena Petrowna Bla­vatskys Zeiten."
      ],
      [
        "Das geschah schon, indem Helena Petrowna Blavatsky die großen Wahrheiten und Weistumer ihrer «The Secret Doctrmne» ab-faßte.",
        "Ihr erstes Werk, die «Entschleierte Isis», zeigt nur das ganz Chao­tische und Unlogische und Leidenschaftliche und Durcheinanderwerfe­rische ihres Wesens, zeigt aber überall, daß hinter ihr wachende Mächte stehen, die sie nach dem allgemein Menschlichen hinführen wollen."
      ],
      [
        "In der «Sec ret Doctrin» waltet überall neben dem selbstverständlich Größ­ten menschliches Spezialinteresse, solches Interesse, das ausgeht von gewissen okkulten Zentren, die nicht heute das allgemein-menschliche Interesse im Auge haben, sondern ein partielles, ein Spezialinteresse.",
        "Tibetanische, indische, auch ägyptische Einweihung von heute haben überall partiell menschliches Interesse nur im Auge, wollen nur an der westlichen Welt den unterdrückten östlichen Okkultismus rächen, wol­len die Tatsache rächen, daß die westliche Welt durch materialistische Faktoren über die östliche Welt gesiegt hat."
      ],
      [
        "Sie hat durch materiali­stische Faktoren über die östliche Welt gesiegt; sie hat insofern gesiegt, als in die eigentliche fortschreitende Kultur der Menschheitsentwickelung,"
      ],
      [
        "in das fortschreitende Leben der Menschheitsentwickelung das Christentum aufgenommen worden ist.",
        "Nach dem Osten von Asien ist das Christentum nicht hinübergegangen, nach dem Süden von Asien auch nicht; das Christentum ist nach Westen gezogen."
      ],
      [
        "Nun werdet Ihr vielleicht sagen, meine lieben theosophischen Freunde: Also ist es gut.",
        "Dann hat der Westen das Christentum ange­nommen, und da das Christentum eine Etappe im Weiterfortschreiten der Menschheit ist, so ist es selbstverständlich, daß der Westen über den Osten den Sieg davontrug. - Ja, wenn dies so wäre!"
      ],
      [
        "Wenn es so wäre, wäre es selbstverständlich.",
        "Aber es ist nicht so.",
        "Das Christentum, das durch Jahrhunderte und Jahrtausende vorbereitet worden ist und das in die Welt gekommen ist, hat noch nirgends auf der Erde gesiegt."
      ],
      [
        "Und derjenige, der heute glauben würde, daß er in wahrem, echtem Sinn das Christus-Prinzip und den Christus-Impuls schon in der Gegen­wart vertreten könnte, würde einem unbeschreiblichen Hochmut zum Opfer gefallen sein.",
        "Was ist denn bisher überhaupt geschehen?"
      ],
      [
        "Nichts anderes, als daß die westlichen Völker gewisse alleräußerste Außerlich­keiten von dem Christentum aufgenommen haben, den Christus-Namen okkupiert haben, und mit dem christlichen Namen ihre alten, vor dem Christentum in Europa seßhaft gewesenen Kulturen umkleidet haben, ihre nur in den modernen Industrialismus umgewandelten kriegerischen Kulturen.",
        "Herrscht der Christus innerhalb des christlichen Europa?"
      ],
      [
        "Jeder Angehörige von okkulten Bewegungen wird niemals zugeben, daß der Christus innerhalb des christlichen Europas herrsche, sondern er wird sagen: Ihr sprecht «Christus», ihr meint aber immer noch das­selbe, was die alten mitteleuropäischen Völkerschaften gemeint haben, als sie von ihrem Gott Saxnot sprachen. - Das Symbolum des Cruci­fixus steht über den europäischen Völkern.",
        "In gewisser Beziehung herrschen aber die Traditionen des Gottes Saxnot, dessen Symbolum das ehemalige kurze sächsische Schwert ist, das da war zur Ausbrei­tung nur der materiellen Interessen zunächst, denn das war der Beruf der europäischen Völkerschaften."
      ],
      [
        "Daher hat auch dieser Beruf die edelste Blüte materialistischer Kultur hervorgebracht, eine Erscheinung, die edel ist auf dem Gebiet materialistischer Kultur: das Rittertum.",
        "Wo gibt es irgendwo in einer Kultur etwas Ahnliches wie das Rittertum"
      ],
      [
        "der westlichen Kultur?",
        "Das gibt es sonst nicht.",
        "Niemandem wird es einfallen, die Helden des trojanischen Krieges zu vergleichen mit den mittelalterlichen Rittern.",
        "Der Christus lebt noch wenig bei den Men­schen.",
        "Von dem Christus sprechen die Menschen nur.",
        "Die östlichen Völker fühlen dann, wenn die westlichen von dem Christus sprechen, daß sie - diese östlichen Völker - allerdings in bezug auf die spirituelle Erfassung der Welt, in bezug auf das, was diese Völker wissen von den Geheimnissen des Daseins, weit voraus sind, weit, weit voraus sind.",
        "Das wissen diese östlichen Völker."
      ],
      [
        "Ganz gewöhnliche Dinge können es Euch erklären, daß die östlichen Völker in einer gewissen Weise ihre Vorzüge in spiritueller Beziehung schon zu schätzen wissen können.",
        "Was tun die westlichen Völker heute noch in ihrer Masse, in ihrer Mehrzahl, wenn Geheimnisse des Daseins enthüllt werden?"
      ],
      [
        "Nun, wir sitzen noch in recht kleinen Scharen beisam­men, wenn wir sprechen, sagen wir von so etwas, wie gestern Abend gesprochen worden ist, von den waltenden spirituellen Mächten und Geheimnissen, die uns überall umgeben.",
        "Für den gewöhnlichen West-europäer ist das eine Torheit oder ein Wahnsinn, denn er kann noch immer nicht das Wort des Paulus verstehen: Was die Weisheit ist vor Gott, das ist vor den Menschen eben oftmals die Torheit, und was die Torheit ist vor den Menschen, das ist die Weisheit vor Gott. - Und nur diejenigen, die angesteckt sind von den Westeuropäern im Orient, wür­den wagen, auch nur im allergeringsten zu deuteln an den tiefen Wahr­heiten über die spirituellen Geheimnisse des Kosmos, wie wir sie ver­suchen wiederum zu enthüllen, wenn sie sie hören, denn als etwas Selbstverständliches gelten solche Dinge, wie sie zum Beispiel gestern gesagt worden sind, denjenigen, die im östlichen spirituellen Leben drinnen sind."
      ],
      [
        "Wundern wir uns daher nicht, daß es oftmals diesen öst­lichen Völkern vorgekommen ist, wenn die Europäer über sie herge­fallen sind, wie es eben einer Schar von Menschen vorkommt, wenn ihnen eine Herde wilder Tiere entgegenkommt, gegen die sie sich weh­ren, denen sie das, was sie tun, nicht übelnehmen, die sie aber als etwas Inferiores betrachten.",
        "Wir Westländer werden aus den angedeuteten Gründen - ob das heute berechtigt ist oder nicht, darauf kommt es hier nicht an - und nach den Traditionen des Ostens von jedem Angehörigen"
      ],
      [
        "etwa des Brahmanentums selbstverständlich als inferiore Men­schen angesehen."
      ],
      [
        "Und wenn wir absehen von dem Brahmanentum und sehen etwa in die Kulturen Mittelasiens, in die tibetanische oder chinesische Kultur, die in der nächsten Zeit in einer Weise werden für die Welt Bedeutung gewinnen, wovon sich die Menschen heute nichts träumen lassen, trotz­dem uns nur kurze Zeit von dieser Sache trennt, wenn wir auf alle diese Dinge sehen und gewahr werden, wie die Seelen vieler Zarathu­stra-Schüler in diesen Kulturen noch verkörpert sind, dann werden wir versucht werden, diese Dinge sehr ernst zu nehmen.",
        "Wir werden es auch begreifen können, daß in dasjenige, was Helena Petrowna Bla­vatsky zu geben verstand, der indische, der tibetanische, der ägyptische Okkultist versucht sein konnten, aus ihrer Seele heraus - ihr eigenes Weisheitsgut hineinzuleiten, jenes Eigene aber, das in dem Menschen­werdeprozeß einer Vergangenheit angehört."
      ],
      [
        "Und wir müssen den Ver­gangenheitscharakter dieser orientalischen Weisheitsgüter erkennen, die innerhalb der Blavatskyschen Lehren stecken.",
        "Wir brauchen ja den Wert einer solchen Sache nicht zu verkennen, brauchen nicht zu ver­kennen, daß wenn nun überfluten wird das, man möchte sagen, seine Fesseln gesprengt habende Chinesentum die westlichen Welten, dann eine Spiritualität damit kommt, die richtig die Nachfolge ist, in vieler Beziehung die noch ungetrübte Nachfolge ist des alten Atlantiertums."
      ],
      [
        "Sie wird wirken, wie wenn aufspringen würde etwas, was zusammen­gehalten wird, und was nach aller Welt sich verbreiten kann; so wird es sich ausgießen - in kleinem Maßstabe hat sich so bei der ersten Ge­legenheit ausgegossen das alte Indertum."
      ],
      [
        "Daher war es möglich, meine lieben theosophischen Freunde, daß von jener Zeit an alles das eingetreten ist, wofür man in allem Okkul­tismus ein bezeichnendes Wort hat, daß von da ab im Grunde genom­men die theosophische Bewegung nicht mehr ein geeignetes Instrument war für die Fortbewegung der Kultur Europas.",
        "Jeder Okkultist kennt gut das Wort, das da heißt: Es darf niemals bei den leitenden Mächten des Okkultismus oder bei den in irgendeiner Weise okkult Tätigen irgendein spezielles Interesse überwiegen das allgemeine Interesse der Menschheit. - Es gibt keine Möglichkeit, okkult günstig zu wirken,"
      ],
      [
        "wenn ein spezielles Interesse überwiegt das allgemeine menschliche In­teresse.",
        "In dem Augenblick, wo in den Okkultismus eindringt ein spe­zielles Interesse anstelle der allgemein-menschlichen Interessen, sind die Möglichkeiten zu realen Irrtümern gegeben."
      ],
      [
        "Daher kommt es, daß seit jener Zeit in die theosophische Bewegung jeder mögliche Irrtum hineinkonnte.",
        "Durch die Art und Weise, wie England mit Indien ver­knüpft ist karmisch im Weltzusammenhang, war einfach die Möglich­keit gegeben, daß jene erhabenen Mächte, die am Ausgangspunkt der theosophischen Bewegung stehen, gefälscht wurden."
      ],
      [
        "Denn das ist ein gewöhnlicher Vorgang im Okkultismus, daß Mächte, die ihr Spezial-interesse verfolgen wollen, die Gestalt derjenigen annehmen, welche die eigentlichen Impulse vorher gegeben haben.",
        "So gab es von einer gewissen Zeit der theosophischen Bewegung an gar keine Möglichkeit mehr, so ohne weiteres alles hinzunehmen, was innerhalb dieser theo­sophischen Bewegung lag, und das Karma hat es gewollt, daß dies immer weniger und weniger möglich geworden ist."
      ],
      [
        "Und so konnte denn nichts anderes getan werden, als in dem Augenblick, wo der Ruf an uns erging, uns zu vereinigen mit dieser theosophischen Bewegung, es konnte nichts anderes getan werden, als auf die ursprünglichen Quellen wieder zurückzugehen, auf diejenigen Quellen, die wir im Gegensatz zu den speziellen die allgemein-menschlichen nennen können.",
        "Und so habt Ihr vielleicht gesehen in Mitteleuropa, daß wir versuchen, an die okkulten Quellen heranzukommen so, daß Ihr nicht bemerken werdet an alldem, was Euch da entgegentritt, daß irgendein spezielles Interesse damit verknüpft ist."
      ],
      [
        "Alles, was an speziellen Interessen aufgefunden werden kann in Mitteleuropa, versucht Ihr es zu vergleichen mit dem, was Ihr kennenlernt als jene Theosophie, die unter uns getrieben wird:"
      ],
      [
        "Es lassen sich die beiden Dinge wirklich nicht zusammenbringen. - Ihr könnt diese Theosophie nehmen und findet wahrscheinlich außerdem, daß, weil in einer Sprache schon einmal geschrieben werden muß, die Bücher von mir selber in deutscher Sprache geschrieben sind, findet Ihr wohl nichts Deutsches in der Theosophie, nichts, was irgendwie mit den äußeren Traditionen Mitteleuropas zusammenhängt.",
        "Und wo irgend die Tendenz auftritt, mit einem Spezialinteresse die Theosophie zu ver­binden, gibt es sogleich eine Unmöglichkeit."
      ],
      [
        "Das ist nun die besondere Aufgabe Mitteleuropas gewesen, die Theosophie zu erlösen von den speziellen Eigentümlichkeiten, die sie erhalten hat im europäischen Westen.",
        "Es war unsere Mission, die Theo­sophie rein, rein herauszulösen von allen Spezialinteressen."
      ],
      [
        "Und je weiter Ihr eingehen werdet auf die Dinge, werdet Ihr finden, daß ich gewissermaßen selber in der Lage war loszulösen alles, was ich theo­sophisch bringen durfte, von einem jeglichen Spezialinteresse.",
        "Es ist das eine symbolische Angabe, meine lieben theosophischen Freunde, aber symbolisch gesprochen - ich brauchte mich nur leiten zu lassen von dem, was als ein unmittelbarer Impuls in der gegenwärtigen Inkarna­tion vorhanden war, mißversteht es nicht, es gibt ja nur eine Tatsache wieder -: diejenigen, welche die äußeren Träger zum Beispiel jenes Blutes waren, aus dem ich stamme, sie stammten aus deutschen Gegen­den Österreichs; da konnte ich nicht geboren werden."
      ],
      [
        "Ich selber bin in einer slawischen Gegend, in einer Gegend, die vollständig fremd war dem ganzen Milieu und der ganzen Eigentümlichkeit, aus der meine Vorfahren stammen, geboren.",
        "So drängte sich mir - ich will das nur symbolisch anführen - im Ausgangspunkt meiner gegenwärtigen In­karnation sinnbildlich von selber auf, daß wir in Mitteleuropa den Be­ruf hatten, uns loszulösen von allem Spezialinteresse die Theosophie, so daß sie in Mitteleuropa wirklich vor uns steht wie eine Göttin, wie etwas ganz, ganz von allem Menschlichen losgelöstes Göttliches, das ebensoviel zu tun hat mit dem Menschen, der da lebt, wie mit jenem, der dort lebt, und das wird immer bleiben müssen."
      ],
      [
        "Das Ideal, das wir haben, meine lieben theosophischen Freunde, so einfach, als es sich ausdrückt, es wird immer vor uns stehen müssen, weil es schwerer zu erfüllen ist, als auszusprechen.",
        "Es wird vor uns stehen müssen als unser Ideal die Wahrheit und Aufrichtigkeit, die ungefärbte göttliche Wahrheit.",
        "Vielleicht gerade, wenn wir uns so be­streben, werden wir den Weg finden, nicht für uns, sondern für das, was in Mitteleuropa nach der ganzen Mission Europas unpersönlich war, für diese göttliche Theosophie hinüber nach dem Osten.",
        "Und da, wenn ich, ich möchte sagen, nun den Weg weiter beschreibe, wie die Theosophie im Westen Platz gegriffen hat, durch Europa durchgeht und nach dem Osten kommen soll, da möchte ich das Wort wiederum"
      ],
      [
        "hierhersetzen, scharf, scharf das Wort: Verantwortlichkeitsgefühl.",
        "Die Kulturen in der Welt, sie entwickeln sich so, daß sich gleichsam wie in einer geistigen Hülle die eine Kultur mit der andern entwickelt.",
        "Die eine Kultur verbindet sich mit der andern.",
        "Dadurch, daß die Theo-sophie in Mitteleuropa so unpersönlich sein mußte, hat sie einen gewis­sen Charakter der Geistigkeit bekommen, der von allen Interessen los­gelösten Geistigkeit.",
        "Diese Theosophie hat dadurch, meine lieben theo­sophischen Freunde, etwas Sprödes; sie hat das Spröde, das die Unbe­rührtheit von den speziellen Interessen hat; sie wird daher denjenigen nicht gefallen, welche ihr Herz nicht aufschließen können gegenüber dem, das eben nicht irgendeinem speziellen Interesse dient."
      ],
      [
        "Das Geistige, das sie hat, diese Theosophie, kann aber gefunden werden von der Seele, die nach diesem Geistigen dürstet, die nach die­sem Geistigen sich sehnt.",
        "Und da muß ich sagen, meine lieben theoso­phischen Freunde, ich habe kennengelernt aus der geistigen Welt selber heraus eine Seele, die sich sehr sehnt nach dem Geiste, der durch die Theosophie sich ausdrückt."
      ],
      [
        "Ich habe kennengelernt diese Seele in der rein geistigen Welt.",
        "Wenn wir in der Reihenfolge der Hierarchien hin­aufgehen zu den einzelnen Völkergeistern und sprechen innerhalb der einzelnen Völkergeister von den Volksseelen, dann kommen wir auch unter den Volksseelen, die sozusagen heute noch jung sind und die sich fortentwickeln müssen, wie jedes Wesen sich entwickeln muß, zur rus­sischen Volksseele."
      ],
      [
        "Von dieser russischen Volksseele weiß ich, daß sie sich sehnt nach dem Geist, der in der Theosophie zum Ausdruck kommt.",
        "Sie sehnt sich mit allen Kräften, die sie entwickeln kann.",
        "Ich spreche von dem Verantwortlichkeitsgefühl, weil Ihr, meine lieben theosophi­schen Freunde, Kinder seid dieser russischen Volksseele."
      ],
      [
        "Sie waltet und wirkt in Euch und Ihr habt ihr gegenüber eine Verantwortung.",
        "Die Verantwortung, versteht sie zu lernen!",
        "Nehmt es nicht übel; viel, viel konnte mir sagen oftmals diese russische Volksseele."
      ],
      [
        "Am tragischsten trat mir das vor Augen, was diese russische Volksseele mir sagen konnte, etwa um das Jahr 1900 herum.",
        "Es trat am tragischsten dazumal zutage, weil einem da auffallen konnte etwas, das ich mir selber erst lange hinterher in der richtigen Weise interpretieren konnte, weil einem da auffallen konnte, wie wenig im Grunde genommen diese russische"
      ],
      [
        "Volksseele heute noch verstanden wird.",
        "Wir haben in Westeuropa ken­nengelernt vieles, vieles aus Rußland, und vieles, vieles aus Rußland hat auf uns einen großen, gewaltigen Eindruck gemacht.",
        "Wir haben kennengelernt die großen Impulse Tolstojs, haben kennengelernt das Westeuropa so tief ergreifende der Psychologie von Dostojewskij und wmr haben endlich kennengelernt einen solchen Geist wie Solowjow, emnen Geist, der, wenn man ihn auf sich wirken läßt, überall den Ein­druck macht: so ist er, wie er geschrieben hat."
      ],
      [
        "Und wie er geschrieben hat, es bekommt erst das rechte Licht, wenn man hinter ihm stehend fühlt die russische Volksseele.",
        "Und diese russische Volksseele, sie weiß viel, viel mehr zu sagen, als selbst Solowjow zu sagen weiß, denn da kommt uns noch immer viel, viel zuviel von Westeuropa Angenommenes vor die Herzen."
      ],
      [
        "Denkt einmal, meine lieben Freunde, an das Wort Ver­antwortlichkeitsgefühl, denkt daran, daß ihr diese Aufgabe habt, Euch würdig zu zeigen der russischen Volksseele gegenüber, und daß Ihr kennenlernen sollt die Sehnsucht der russischen Volksseele nach der un­persönlichen Theosophie.",
        "Wenn Ihr Theosophie kennenlernt in dem, was sie in ihrem innersten Impuls will, dann, meine lieben Freunde, werdet Ihr allerhand Fragen zu stellen haben, die nur aus einer russi­schen Seele herauskommen können: Seelenfragen zu den Geistesfragen der Theosophie."
      ],
      [
        "Ich habe es erfahren, daß viel edles, herrliches, schönes Gefühl mir entgegengetreten ist von Osteuropa, so viel von echter, wahrer Menschenliebe und Menschengüte, von menschlichem Mitleid, von überfließendem Gefühl, als sich nur denken läßt, von feiner, in­timer Beobachtung dessen, was in der Welt gegeben ist, von einem in­tensiven persönlichen Verknüpftsein mit den Mächten des Daseins.",
        "Und aus solchen lieben und schönen und edlen Gefühlen sind viele, viele Fragen von Angehörigen des russischen Volkes an mich gestellt worden, viele Fragen - Fragen, die einmal gestellt werden müssen, weil sie Fragen sind, ohne deren Beantwortung die Menschheit in der Zukunft wird nicht leben können."
      ],
      [
        "Fragen, die nur vom Osten Europas kommen können, sie hat bisher an mich nur die russische Volksseele ge­stellt, die russische Volksseele auf den höheren Planen.",
        "Oftmals mußte ich denken, daß die Kinder dieser Volksseele noch einen Weg haben, um ihre Volksseele zu verstehen, um zu verstehen, was diese Volksseele"
      ],
      [
        "eigentlich ersehnt, und wieviel sie noch trennt, diese Kinder der Volks­seele, von dieser Volksseele selbst.",
        "Scheut es deshalb nicht, den Weg zu suchen, den Ihr finden könnt, wenn Ihr wollt, zu Eurer Volksseele."
      ],
      [
        "Aus Eurer Volksseele heraus werdet Ihr diejenigen Fragen finden, ohne deren Beantwortung die Menschheit der Zukunft nicht wird sein kön­nen.",
        "Aber scheut es nicht, über das persönliche Interesse dabei heraus­zukommen, denn seid eingedenk des großen Verantwortlichkeitsge­fühls, das Ihr haben sollt gegenüber der russischen Volksseele, seid ein­gedenk dieses Gefühles, denn in der Zukunft brauchen die Volksseelen ihre Kinder, die Menschen, um ihre Ziele zu erreichen."
      ],
      [
        "Und vergeßt dabei eines nicht.",
        "Dasjenige, das einen am höchsten tragen kann, das einen in die schönsten, lichtesten Höhen der Welt bringen kann - das ist am meisten der Gefahr ausgesetzt, in Irrtümer zu verfallen. - Ihr sollt, meine lieben theosophischen Freunde, das Geistige durchseelen."
      ],
      [
        "Ihr sollt finden die Seele zum Geiste.",
        "Ihr könnt es, weil die russische Volksseele unermeßliche Tiefen und Möglichkeiten des Zukünftigen hat.",
        "Aber notwendig ist es, daß Ihr Euch bewußt seid, daß das See­lische, das sich zum Geiste erheben kann, den Geist selber zu durch-seelen hat, Euch vor die große Gefahr stellt, Euch zu verlieren und in dem Persönlichen, in dem individuell Persönlichen steckenzubleiben, zu verlieren in dem Persönlichen als solchem."
      ],
      [
        "Dann wird das Persön­liche nämlich stark, wenn es stammt aus dem Seelischen."
      ],
      [
        "Es werden nicht jene Hindernisse bei Euch auftreten, die so viel­fach in West- und Mitteleuropa auftreten.",
        "Zur Skepsis seid Ihr weniger geboren; Skepsis kann nur durch Einimpfung von Westen zu Euch kommen.",
        "Ihr werdet durch ein bestimmtes Gefühl die Wahrheit von der Unwahrheit und Unredlichkeit unterscheiden lernen auf dem Ge­biet des Okkultismus, wo Scharlatanerie und Wahrheit so dicht bei­sammenstehen.",
        "Nicht der Skeptizismus, der Zynismus werden Eure Gefahr bilden.",
        "Eure Gefahr wird bilden, daß das seelisch Machtvolle Eurer Persönlichkeiten Wolken um Euch verbreiten kann, astralische Wolken, durch die Ihr dann nicht durchkönnt bis zum objektiv Gei­stigen.",
        "Euer Feuer, Eure Wärme, sie können sich wie eine wolkige Aura um Euch herum breiten, nicht durchlassen das Geistige, weil Ihr meint, für den Geist begeistert zu sein, aber durch die Begeisterung verhindert"
      ],
      [
        "den Geist, die Wege zu Euch zu finden.",
        "So versucht, das ins Auge zu fassen, daß Ihr in dem großen Vorteil seid - das jetzt in dem idealen spirituellen Sinn gemeint -, ein spezielles Interesse haben zu dürfen, weil Ihr prädestiniert seid, das heißt Eure Volksseele, in das spezielle Interesse des russischen Volkstums die Theosophie, die man in Mittel­europa noch ganz wie nur eine über allem Menschlichen erhabene gött­liche Macht nehmen mußte, empfangen zu dürfen, wie kein anderes Volk sie empfangen kann, wie etwas, was Ihr als Euer Eigenstes hegen und pflegen dürft.",
        "Denn durch Eure Prädestination seid Ihr dazu aus­gestattet, Seele dem Geist einzuhauchen.",
        "Das ist oftmals in unseren Reihen gesagt worden, aber an Euch liegt es, die Gelegenheit sobald als möglich herbeizuführen, sie nicht zu versäumen, nicht bloß Gefühl und Wille zu entwickeln, sondern vor allen Dingen Energie und Aus­dauer zu entwickeln, weniger - wenn auch ein Wort in bezug auf das Praktische geredet werden soll - reden über die Art, wie Theosophie im Westen sein muß und wie sie in Rußland sein muß und so weiter und was für das eine und andere gut ist, sondern zunächst aufnehmen Theosophie, aufnehmen, mit der Seele, mit dem Herzen vereinigen.",
        "Das Übrige wird sich schon ergeben; es wird sich sicher ergeben."
      ],
      [
        "Das ist so etwas von dem, meine lieben Freunde, was ich habe zu Euch sprechen wollen, sprechen wollen deshalb, weil überall, wo ich unmittelbar zum Menschen sprechen soll, vor Augen stehen muß eben das Verantwortlichkeitsgefühl, das wir Menschen der Gegenwart gegen­über der Theosophie haben.",
        "Im Westen sollen die Menschen das Gefühl haben, daß sie sich an der Menschheit versündigen, wenn sie etwas von Theosophie haben können und es nicht wollen, es abweisen - Sünde gegen die Menschheit!",
        "Es ist manchmal recht schwer zu fassen, denn man muß ein fast transzendentales Pflichtgefühl haben, meine lieben Freunde, wenn man solche Verpflichtung, solch ein Verantwortlich­keitsgefühl gegenüber der Menschheit haben soll.",
        "Euch sagt Eure Volks­seele, daß sie, diese Volksseele selber, Euch verpflichtet.",
        "Für Euch hat schon die Volksseele diese Verpflichtung gegenüber der Menschheit übernommen.",
        "Ihr braucht sie nur zu finden, diese Volksseele.",
        "Ihr braucht sie nur durch Eure Gedanken, Empfindungen und Willens-impulse sprechen zu lassen, und Ihr werdet, wenn Ihr die Verantwortlichkeit"
      ],
      [
        "gegenüber der Volksseele fühlt, zugleich erfüllen die Pflicht gegenüber der Menschheit.",
        "Deshalb seid Ihr auch äußerlich örtlich hin­eingestellt zwischen den europäischen Westen, der Theosophie haben muj', für den sie aber in dem Grade wie für Euch nicht eine persönliche Angelegenheit werden kann, und den asiatischen Osten, der Okkultis­mus und spirituelle Kultur seit Urzeiten hat."
      ],
      [
        "Ihr seid hineingestellt.",
        "Ihr würdet vielleicht niemals dazukommen, Eure Aufgabe gegenüber der spirituellen Kultur der Menschheit zu erfüllen in dieser geographisch schwierigen Lage, möchte ich sagen, wenn Ihr nur an die Verpflichtung gegenüber der Menschheit denken müßtet."
      ],
      [
        "Denn die Versuchungen werden üngeheuer groß sein, wenn auf der einen Seite nicht nur der europäische Westen wirkt, der viele der Kinder Eurer Volksseele im Grunde genommen sich selber hat untreu werden lassen.",
        "Einem großen Teil dessen, was von Russen geschrieben und uns nach Westen gebracht wird, gegenüber haben wir das Gefühl, daß es nichts zu tun hat mit der russischen Volksseele, sondern ein Spiegelbild aller möglichen west­lichen Dinge ist."
      ],
      [
        "Die zweite Versuchung wird die von Osten sein, wenn die Macht spiritueller Kultur kommt.",
        "Da wird es die Pflicht sein, zu wissen, daß bei aller Größe dieser spirituellen Kultur des Ostens der Mensch der Gegenwart sich zu sagen hat: Nicht die Vergangenheit haben wir in die Zukunft hineinzutragen, sondern die neuen Impulse."
      ],
      [
        "Nicht aufzunehmen wird sein einfach irgendein spiritueller Impuls des Ostens, sondern zu pflegen das, was der Westen aus den spirituellen Quellen selber hervorbringen kann. - Dann wird die Zeit kommen, in der Europa anfangen wird, wenn Ihr Eure Pflichten auch erfüllt gegen­über Eurer Volksseele, ein wenig zu verstehen, was eigentlich der Chri­stus-Impuls in der geistigen Entwickelung der Menschheit ist.",
        "Sucht alles das, was ich habe mit und in diesen Worten sagen wollen, meine lieben Freunde, und sucht vor allen Dingen das in diesen Worten, was in Euch selber Impuls werden kann, nicht bloß zu fühlen und zu emp­finden, daß Theosophie etwas Bedeutendes und etwas Großes ist, son­dern sucht vor allen Dingen, Theosophie in die Tat und in die Willens­impulse Eurer Seele aufzunehmen und aus ihr heraus Euer Leben, aus ihr heraus Eure Taten einzurichten."
      ]
    ]
  },
  {
    "order": 13,
    "title_de": "ANSPRACHE für die russischen Zuhörer des Vortragszyklus «Die okkulten Grundlagen der Bhagavad Gita» Helsingfors, 5. Juni 1913",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Als wir uns im letzten Jahre hier versammelten, war gewissermaßen in den Herzen derjenigen, welche dazumal schon mit unseren russi­schen Freunden versammelt waren, dasjenige noch Knospe, was in einer gewissen Weise sich doch bis in dieses Jahr herein entfaltet hat, das Bewußtsein, das immer mehr und mehr Eure Herzen durchziehen soll, daß Theosophie, oder wie wir es auch nennen, Anthroposophie, nicht etwas ist, was der Mensch wie ein anderes Wissen oder wie ein anderes einzelnes Glaubensbekenntnis aufnehme, sondern was in einer gewissen Beziehung die ganze Seele jedes einzelnen ergreifen soll, was die Seele der ganzen Menschheit in unserem Zeitenzyklus ergreifen soll. Dieses Bewußtsein muß sich nach und nach entwickeln, und man sollte gar nicht glauben, man muß sich gar nicht der Illusion hingeben, daß man leicht zu der vollen Bedeutung und vollen Kraft dieses Bewußtseins kommt. Denn nur nach und nach, langsam und ganz allmählich können wir im Erleben uns erringen das Bewußtsein von der Bedeutung des theosophischen Impulses.",
      "Eine solche Wahrheit sieht scheinbar recht trivial aus, aber hier ist es gerade, wo wir dasjenige, was wie recht trivial ausschaut, mit aller­tiefstem Ernst nehmen müssen. Denn nehmt aus der Fülle dessen, was zu diesem Bewußtsein gehört, ein Einzelnes heraus, nehmt heraus, daß es nahezu zweitausend Jahre her ist, daß der Christus-Impuls sich aus höheren Welten in das Erdenleben hereingesenkt hat, nehmt die Tat­sache, daß das Evangelium zu den allerverbreitetsten Büchern der Welt gehört, nehmt die Tatsache, daß durch Jahrhunderte und aber Jahr­hunderte Millionen von Menschenseelen geglaubt haben, ein richtiges Verhältnis zum Christus zu haben, und stellt die Tatsache daneben, daß es wahr ist, daß die ehrliche Menschenseele, die nicht in Unbe­scheidenheit ein Verständnis sich zuschreiben will, das sie nicht hat,",
      "in unserer Zeit mit der Frage ringen muß: Was ist eigentlich dieser Christus-Impuls? - Und daß diese Seele erst hoffen kann von neuen Offenbarungen aus der geistigen Welt ein Verständnis dieses Christus-Impulses wirklich zu gewinnen! Nehmt andere Tatsachen. Mit einigen Freunden besuchte ich im vorigen Jahre den Ostergottesdienst der rus­sischen Kirche. Ich habe damals unmittelbar danach versucht, ein Wort auszusprechen, von dem ich angenommen habe, daß es Euch zu denken gibt. Der Gottesdienst strömte aus bloß das Bewußtsein von dem ge­storbenen Christus. Der Menschheit zum Heile muß in unserer Zeit und in Zukunft aber sein die Botschaft von dem immerfort lebenden Christus. t)och ein anderes Bild ergab sich mir, wie als der Hintergrund dieses Gottesdienstes, von dem hinweggedacht werden mußte, was die diesem Kultus nicht gewachsenen Persönlichkeiten dort taten. Es ergab sich als der Hintergrund ein Tableau uralt heiliger Mysterien, die sich doch fortentwickelt haben bis zu dem, was in diesem Kultus äußerlich in den Formen lebt,was viele Menschenherzen zwar fühlen,was aber ge­rade von denjenigen am wenigsten verstanden wird, welche die berufen­sten Interpreten sein sollten oder sich dafür halten in der Gegenwart.",
      "Versucht, den Gedanken durch solche Hinweise, wie sie soeben aus­gesprochen sind, tiefer und immer tiefer in Eure Seelen zu graben, daß die Theosophie von einem jeden einzelnen Herzen ausgeht, daß durch Theosophie oder Anthroposophie etwas völlig Neues in die Mensch­heitsentwickelung einströmen muß. Versucht einzugraben in Eure Her­zen die Wahrheit, daß die Zeichen der Zeit so stehen, daß wir wirklich wenigstens in unseren Seelen selber, in unseren Herzen selber, zuwei­len ganz still und intim, niemals einen Kompromiß schließen dürfen mit dem, was um uns herum ist. Aus einer Pflanze kann nicht ohne wei­teres eine neue Pflanze erstehen, aus einer Pflanze kann nur eine neue Pflanze werden, wenn die alte Pflanze abstirbt und sich wie aus einem einzigen Punkte heraus, aus dem Keim, eine neue Pflanze bildet. So ist Theosophie in der Tat etwas, meine lieben Freunde, was sich wie ein völlig neuer Keim entwickeln muß in unseren Seelen, in unseren Her­zen, was von allem, was die alte Menschheitspflanze gehabt hat, nur das eine behalten muß, was aber universell ist, nur das eine, was wir schauen bei dem Anblick des Mysteriums von Golgatha. Die Blätter,",
      "der Stamm der uralten Menschheitskultur, sie werden abfallen müssen; die Blüte, das Mysterium von Golgatha, wird wie eine Erinnerung bleiben müssen von dem Keime, der sich entwickeln soll in der Theo­sophie. Und dieser Keim, meine lieben Freunde, wird in sich tragen müssen das Bewußtsein, diese Blüte immer mehr und mehr zur vollen Entfaltung zu bringen auf eine neue und immer wieder neue Weise. Dann wird in vielen Formen der Christus-Impuls durch die Mensch­heitsevolution leben und doch immer derselbe sein, wie jede neue Blüte die Kraft und Schönheit der alten Blüte in sich trägt. Aber er wird zugleich dasjenige sein, was er im Intimsten sein will, ein immer neu und wieder neu Erstehendes, ein neu und wieder neu sich erwirkendes Verständnis desjenigen, was wie ein neuer Anfang der Menschheitsent­wickelung gegeben war, als das Blut floß aus den Wunden desjenigen, der menschliche Gestalt angenommen hat, um den Tod zu erleben in­nerhalb der Menschheit.",
      "Meine lieben Freunde! Alle Welten, die wir durchschreiten können von unserer physischen Welt durch die höheren Welten immer weiter und weiter, sie haben immer Gemeinsames. Es ist richtig, daß wir, wenn wir in eine höhere Welt kommen, zwar immer Neues und Neues finden, aber dennoch immer Gemeinsames mit der vorhergehenden Welt. Wenn wir aber die höheren Welten kennenlernen, so ist eines nicht darinnen, was als physische Erscheinung nur, als physische Er­scheinung allein existieren kann. Die Götter der höheren Welten kön­nen Mannigfaches erfahren, eines können sie niemals erfahren, den Tod. Denn der Tod existiert nicht in den übersinnlichen Welten. In den übersinnlichen Welten verwandeln sich die Wesen, sie gehen von einer Form in die andere über; sterben kann man nicht in der über­sinnlichen Welt. Der Tod als physische Erscheinung ist dasjenige, was nur vorhanden sein kann als physische Erscheinung. Und unter allen Göttern und Geistern war es der einzige, der, um mit der Menschheit ein Gemeinsames zu haben, heruntergestiegen ist in die Welt der Menschheit, der Christus, der sich durch seinen Tod verknüpft hat mit der Menschheit, nicht etwa nur durch sein Leben. Aber durch einen Tod hat er sich verknüpft, von dem ausgegangen sind neue Lebens-kräfte. Hinzuschauen auf den Tod auf Golgatha, das muß werden der",
      "Menschheit der Ausgangspunkt für immer neue und neue Lebenskräfte, denn mit diesem Tode ist in einem einzigen Punkte der Menschheits­entwickelung konzentriert dasjenige, was mit einem unendlichen Opfer nur ein Gott für die Menschheit hat vollbringen wollen. Man versuche diesen Gedanken durchzudenken, versuche diesen Gedanken zu einer lebendigen Meditation zu machen, und man wird sehen, daß von die­sem Gedanken die stärksten Lebenskräfte für eine jegliche menschliche Seele ausgehen können. Und so gibt es kein erhabeneres Bild, als das auf Golgatha errichtete Kreuz.",
      "Meine lieben Freunde! Mit einer solchen für die ganze Menschheit hingestellten Imagination wie das Kreuz auf Golgatha, mit einer sol­chen Imagination ist der Menschheit ein Unendliches gegeben. Hinge-stellt ist es vor nahezu zwei Jahrtausenden, dieses Symbolum, das zu­gleich reale Wirklichkeit war, und noch müssen wir es immer mehr und mehr verstehen lernen in der Menschheitsevolution der Zukunft. Das sind einfache, primitive Gedanken, aber sie sind nicht dazu da, um in uns einen metaphysischen Charakter anzunehmen, sondern um Emp­findungen anzunehmen, die uns geeignet machen, in der richtigen Weise uns hineinzustellen in die ganze Menschheitsentwickelung.",
      "Ihr wißt, meine lieben Freunde, daß die Menschheitsentwickelung differenziert vor sich gegangen ist; in einzelnen Nationen, Völkern ging sie vor sich. Jedes Volk hat einen ganz besonderen Grundcharak­ter, der davon herrührt, daß ein jedes Volk zu seinem Führer hat einen derjenigen Geister, die wir zuzählen der Hierarchie der Archangeloi. Archangeloi sind die obersten Vorsteher gewissermaßen der einzelnen Völker. Daß die Menschenseele als einzelne Seele in der Zukunft immer mehr und mehr Zusammenhang gewinnt mit der führenden Volksseele aus der Reihe der Archangeloi, das ist etwas, was uns die spirituelle Weltanschauung bringen muß. Und nur wenn wir Verständnis ent­gegenbringen demjenigen, was für uns diese Volksseele will, wenn diese Volksseele ein Wollen in die Zukunft zu entwickeln hat, können wir in geeigneter Weise mitarbeiten an der spirituellen Evolution der Mensch­heit. In dieser Beziehung müssen wir einen großen Unterschied machen zwischen den westeuropäischen Volksseelen und der osteuropäischen, russischen Volksseele.",
      "Ich rede jetzt nicht von der äußeren russischen Kultur, von dem, was auf dem äußeren physischen Plan als russische Volkskultur vor­handen ist. Ich rede von Eurer in der geistigen Welt wirklich vorhan­denen Volksseele, welche eben daran ist zu warten auf ihre Aufgabe in der Zukunft, welche in sich voll der Erwartung, voll der Hoffnung, voll der Zuversicht ist.",
      "Wenn man vergleicht mit westeuropäischen Volksseelen diese Volksseele, dann hat man den Eindruck des Jungen, Aufstrebenden auf der einen, und des Alten, Greisenhaften auf der an­dern Seite. Die mitteleuropäische Kultur ist ja hereingeschoben zwi­schen West- und Osteuropa als eine Vermittlungskultur, welche im Grunde mißverstanden wird, wenn man sie den andern Kulturen gleichschätzt.",
      "In einer ganz eigentümlichen Weise hat diese mitteleuro­päische Kultur die Aufgabe, zu wirken wie ein Herold aus alten Zeiten in spätere Zeiten. Bedenkt einmal, meine lieben Freunde, wie im Grunde genommen die ganze europäische Kultur der westlichen Welt überhaupt zustande gekommen ist.",
      "Da waren die vorgeschobenen Po­sten der orientalischen Völker bis ins alte Indien hinein und es haben diese Völker eine große eindringliche Kultur entwickelt, wie sie uns entgegenkommt aus der Kultur des alten Indien, aus der Bhagavad Gita-Zeit. Diese Völker wurden nach dem Süden Asiens vorgeschoben.",
      "Während in ihnen lehrten weisheitsvolle Lehrer wie die Rishis und Zarathustra, waren zurückgeblieben im weitesten Umkreis der euro­päischen Länder Völker, auch in Eurem Lande, die gewissermaßen verblieben durch die Weisheit der Weltevolution in primitiven Zu­ständen. Während in Asien weitumfassende Gedanken in der Sankhya­und der Vedantaphilosophie blühten, hatten diese europäischen Völ­ker einfache, primitive Kulturen.",
      "Warum? Weil die Kulturen so fort­schreiten müssen, daß alles dasjenige, was später als Impuls kommen soll, von primitiven Menschen aufgenommen werden muß. Die bis zu einer gewissen Höhe der Intellektualität aufgestiegenen Völker des Ostens konnten nimmermehr zum Beispiel den Christus-Impuls ver­stehen, sie waren hinaus über die Möglichkeit, den Christus-Impuls zu verstehen.",
      "Die Völker der westländischen Kultur waren noch nicht so weit, das Geistige im Kopfe aufzunehmen, dasjenige, was als Kraft lebt vom",
      "Herzen bis zum Kopf, war bei ihnen noch nicht bis zum Kopf ge­kommen. In Indien war alles Kopfkultur, in den europäischen Völkern war alles noch in primitiven Empfindungen in ursprünglicher Stärke im Herzen konzentriert. Nur solche Völker konnten, weil sie noch nicht hinaus waren über das Seelenhaftige des Herzens, die Mysterien von Golgatha nach und nach in die Empfindung sich einverweben. So war es die europäische Kultur, welche dadurch, daß sie zurückgeblieben war, in ursprünglicher, frischer Kraft dastand - und ursprüngliche frische Kraft ist näher mit dem Göttlichen verwandt -, bereit war, den Christus-Impuls aufzunehmen. So flossen zusammen innerhalb der abendländischen Welt zwei Strömungen, die für jeden, der dafür eine Empfindung hat, scharf zu unterscheiden sind. Wer würde nicht unter­scheiden können den eigentümlichen Grundton Fichtes, des mitteleuro­päischen Philosophen, und den eigentümlichen Grundton Spinozas, der ja auch ein europäischer Philosoph war. Es ist sogar in der Mensch­heitsevolution so, daß dasjenige, was der allgemeinen Kultur angehört, von derselben Individualität getragen werden kann. Denn dieselbe In­dividualität ist ja Spinoza und Fichte, wie vielleicht schon einige unse­rer Freunde wissen. Aber Fichte ist als einzelne Persönlichkeit des 18., 19. Jahrhunderts ein Geist, der durchdrungen werden konnte von der ganzen Kraft des Christus-Impulses; Spinoza, also dieselbe Indivi­dualität, steht aber in der andern Strömung darinnen und hat nichts davon.",
      "Es ist aber noch vieles nicht da, was in die europäische Kultur kom­men muß. Und es muß zusammenwirken dasjenige, was in gewisser Weise alt geworden ist, und dasjenige, was jung und hoffnungsfrisch ist. Die russische Volksseele, die Wesenheit aus der Reihe der Archan­geloi, ist jung und hoffnungsfrisch, sie hat ihre Aufgabe vor sich. Und an den russischen Theosophen wird es sein, die Brücke zu finden von der einzelnen Seele zur Volksseele, verstehen zu lernen, was die Volksseele von ihnen will. Ihr werdet finden, meine lieben Freunde, daß es unter gewissen Voraussetzungen gerade Euren Seelen leicht werden wird, den Christus-Impuls aus Euren Herzen heraus zu beleben durch das, was in Euren Seelen lebt. Ihr werdet auf der andern Seite erfahren müssen, daß auch, weil Ihr eine gewisse innere Leichtigkeit habt, um",
      "den Christus-Impuls zu beleben, auf der andern Seite wiederum Euch große Schwierigkeiten erwachsen. Ihr werdet zu erfahren haben, daß gerade für Euch die tiefe Wahrheit in erhöhtem Maße gilt, daß Ihr auf Eure eigene Seele Euch werdet stellen müssen, daß Ihr werdet das Theosophische in Euren Seelen beleben müssen.",
      "Denn, meine lieben Freunde, Theosophie als Verkündigung unseres Zeitalters, sie will kei­nen Kompromiß schließen mit andern Weltanschauungen. Sie spricht ein strenges Wort zu andern Weltanschauungen. Sie spricht ein Wort zu andern Weltanschauungen, das auch schon gehört worden ist im Laufe der Entwickelung.",
      "Diejenigen, die Theosophie finden wollen in den bisherigen äußerlichen, materialistischen Kulturen - und das sind alle Kulturen der Gegenwart, oder nähern sich wenigstens dazu -, alle, die Kompromisse suchen werden, denen wird immerdar mit aller Strenge das Wort entgegenklingen, das einstmals der Christus Jesus ge­sprochen hat: Lasset die Toten ihre Toten begraben! Ihr aber folget mir nach!",
      "Die Toten, das sind die einzelnen Kulturen, die sich dem Materialismus nähern, sie haben in sich schon die Fähigkeit, sich zum Grabe zu führen. «Lasset die Toten die Toten begraben!» Aber die Seelen sollen nachfolgen dem, was das Verständnis des spirituellen Impulses ist, der als Christus-Impuls durch die Welt waltet.",
      "Daher werdet Ihr nicht, meine lieben Freunde, finden, wenn Ihr anfragt bei demjenigen, was Euch alte Traditionen geben können, was Euch altes Herkommen geben kann, etwas, was Euch zur Theosophie führt. Es ist gut, dieses alte Herkommen, diese alten Traditionen aufzufinden, um zu zeigen, wie in ihnen das Göttliche waltet, aber zur Theosophie kommt heute der Mensch, gerade indem er eine Seele in sich trägt, in der nicht das Alte, Greisenhafte waltet, sondern eine Seele, wie Ihr sie tragt: frische, unmittelbare Seelen, wie Ihr sie unbeeinflußt von aller Tradition dieser Theosophie entgegenbringt.",
      "Lebenskraft, nicht bloße Erkenntniskraft erfordert der theosophische Impuls, fordert der theosophische Impuls von Euren Seelen.",
      "Meine lieben Freunde! Viele von Euch, vielleicht die meisten, viel­leicht sogar alle, fühlen in sich, wenn sie es auch vielleicht anders defi­nieren, den Schmerz, das Leid des Getrenntseins von der Volksseele, des vorläufigen Getrenntseins von Eurer Volksseele. Viele von Euch fühlen,",
      "wenn sie es auch anders glauben, vielleicht die meisten, vielleicht alle fühlen in sich, wie sie brauchen neuen Ansporn zu Wille und Kraft. Beginnt einmal, meine lieben Freunde, das, was Ihr so als Leid fühlt des oftmals mangelnden Willens und der oftmals mangelnden Kraft, beginnt einmal, entschließt Euch dieses anzusehen als das Jungfräu­liche Eures Willens, entschließt Euch, dieses anzusehen als einen Willen, der unberührt geblieben ist, und der nur auf das Angesporntwerden wartet von demjenigen, was theosophischer Impuls ist!",
      "Laßt den theo­sophischen Impuls in Euch Wille werden! Versucht das Leid in Kraft, den schwachen Willen in die in Euch wollende Theosophie zu wandeln, Ihr werdet können dadurch wirklich in das theosophische Leben hin­einkommen!",
      "Versucht umzuinterpretieren, was in Euch noch schwach, noch nicht ganz da ist! Ihr werdet so zu den besten Trägern der Theo­sophie werden können! Denn bedenkt, die Seelen, die jetzt in Euren Leibern sind, sind nicht dazu bestimmt, in der nächsten Inkarnation nur in Osteuropa wieder inkarniert zu werden.",
      "Sie sind dazu bestimmt, in den nächsten Inkarnationen verteilt zu werden über die ganze Erde hin. Und etwas wird vor Euch stehen zwischen Tod und einer neuen Geburt, das so zu Euch sprechen wird, wenn Ihr in eine neue Inkarna­tion kommen werdet.",
      "Zu dem Einen wird es sprechen: Du hast deine Aufgabe erfüllt, du kannst das, was du aufgenommen hast auf der Erde, in die Welt tragen, was nur auf dem Boden Osteuropas aufge­nommen werden konnte. - Zu dem andern wird es sprechen: Du kannst es nicht!",
      "Meine lieben Freunde, betrachtet dasjenige, was Ihr jetzt für Theo-sophie fühlt, als den Instinkt für das eben Ausgesprochene, als das un­bestimmte Fühlen, was in Euch ist von dieser Eurer Aufgabe. Betrachtet es so, daß es vom Ich in das Denken, Fühlen und Wollen, von da in das Leben, von da in das Blut Euch Kraft geben kann, dann werdet Ihr die­sen Instinkt, aus dem Ihr jetzt zur Theosophie eilt, in der richtigen Weise deuten.",
      "Ihr habt Euch nun in äußerlicher Weise gesammelt. Ihr habt die Möglichkeit gefunden, unter den großen Schwierigkeiten, die in Eurem Lande bestehen, ungehindert äußerlich sammeln zu können. Gebraucht diese Möglichkeit zu möglichst starker innerer Sammlung, um die",
      "Brücke zu schlagen, ein jeder einzelne von Euch, zu der Volksseele hin­auf. Es kann meine Aufgabe nicht sein, meine lieben Freunde, davon zu sprechen, welche Dienste im einzelnen dieser Volksseele geleistet werden müssen.",
      "Aber von etwas anderem darf ich Euch sprechen, von dem ich möchte, daß es zwar als Wort ausgesprochen wird, sich in Euch aber in ein Gefühl verwandele. Ihr seid in einer eigentümlichen Lage, meine lieben Freunde.",
      "Ihr seid gewissermaßen in der gegenteiligen Lage von einem Volke, das in einer gewissen Beziehung zu einem kurzen Glanze auch aufsteigender Art die Erde bevölkert. Ihr seid in einer gegenteiligen Lage wie das nordamerikanische Volk.",
      "Bedenkt, meine lieben Freunde, daß dieses nordamerikanische Volk, das Euer Gegenpol ist, von der Zeit ab begonnen hat, vom Westen allmählich gegen den Osten vorzurücken, in der in Europa das Zeitalter des Materialismus begonnen hat, und ihn weiter ausgebaut hat. Bedenkt, daß in den Wur­zeln des Amerikanertums der Materialismus waltet.",
      "Bedenkt einmal, daß diejenigen Menschen, die Amerika kultiviert haben, dies getan haben mit den Vorstellungen des kultivierten Europäers vor Jahrhun­derten, die so wenig weit hinter uns liegen. Was haben denn diese Men­schen gemacht?",
      "Diese Menschen haben mit den materialistischen Vor­stellungen der modernen Parlamente, mit den Vorstellungen der mo­dernen Naturwissenschaft, der modernen Gesellschaftsordnung das­jenige getan, was sonst die ungebildeten Menschen machen, wenn sie Urwälder ausroden, Stück für Stück Ackerboden erobern, Land be­reiten der Kultur. Das ist alles aus Materialismus entsprungen.",
      "Und wenn man heute betrachtet den als ihren bedeutendsten Schriftsteller Anerkannten, den ja auch die Amerikaner durch Wahl zu ihrem Leiter bestimmt haben, Woodrow Wilson, der für die heutigen Verhältnisse wirklich ein bedeutender Schriftsteller ist, der Glänzendes an schrift­stellerischen Leistungen für die soziale Anschauung geleistet hat, wenn man ihn anschaut, seine Begriffe und Ideen, alles, was er repräsentiert als Vertreter des amerikanischen Volkes, was ist es? Ein Kartenhaus.",
      "Ein Kartenhaus, von einem einzigen Hauch, wenn er einmal gehaucht würde aus den spirituellen Welten heraus, vernichtet. Dann würde diese ganze Kultur umfallen. Jede Einzelheit, aus der die amerikanische Kultur stammt, kann man nachweisen aus äußeren Geschichtsbüchern,",
      "aus der Kulturgeschichte der vorigen Jahrhunderte. Alles liegt offen da, alles ist Menschenwerk, woraus das entsprungen ist.",
      "Fragt nach, woher Euer Volkstum kommt, woher Euer Geistesleben stammt, fragt nach, woher das Beste kommt, was Ihr in Euren Seelen hegen könnt. Ihr werdet es auf der Erde nicht finden! Das ist nicht in dieser Weise zu finden, das wurzelt in der geistigen Welt selber. Das ist Organismus, Lebewesen, das ist kein Kartenhaus! Solche Dinge dür­fen wir niemals zur Veranlassung nehmen unseres Hochmutes, sondern zur Veranlassung unserer Demut, unserer Bescheidenheit, weil wir aus ihm nicht holen sollen ein waghalsiges Selbstbewußtsein, sondern Ver­antwortlichkeitsgefühl.",
      "Meine lieben Freunde! Ich habe gestern über die Freiheit gesprochen. Es wird viel Wasser hinunterfließen müssen die europäischen Ströme, bis eine gewisse Anzahl von Menschen voll versteht, was mit dieser Freiheit begriffen werden soll, was mit dieser Freiheit gemeint ist.",
      "Was ist Freiheit? Gehen wir vom Westen nach dem Osten! Was ist für den Amerikaner Freiheit? Dasjenige, was ihm das Leben am bequemsten einrichtet. Er nennt Freiheit dasjenige, was hineinverwoben werden soll in die soziale Ordnung, damit am besten ein jeder einzelne für die äu­ßere Welt vorwärtskommt.",
      "Wir kennen Freiheit anders - sagt Wood­row Wilson -, als der Europäer, wir kennen Freiheit, weil sie uns prak­tisch erscheint. - So sagt der Amerikaner selber. Ein Messer nimmt man zum Schneiden, eine Gabel zum Essen, weil sie praktisch sind dazu.",
      "Der Amerikaner nimmt die Freiheit, weil sie praktisch ist dafür, was er braucht, weil er am besten damit die Ordnung herstellen kann, die ihm angenehm ist. Freiheit ist für den Amerikaner ein Nützlichkeitspro­dukt, sie bringt ihm Nutzen.",
      "Meine lieben Freunde! Für den Westeuro­päer war die Freiheit etwas anderes, war Freiheit ein hohes Ideal, etwas, wozu er aufblickte. Man darf fast das Wort des Dichters auf die Freiheit anwenden. Dem Europäer ist sie die «hohe herrliche Göttin», für den Amerikaner ist sie die nützliche Melkkuh, die ihn mit Milch und Butter versorgt. ich sage das nicht, sondern derjenige, der in den nächsten Jahren verantwortlich ist für die Leitung der Amerikanischen Vereinigten Staaten, hat das gesagt.",
      "Es ist nun überhaupt nicht meine Aufgabe, meine Meinung vorzubringen, sondern nur der Interpret",
      "zu sein für dasjenige, was in der geistigen Weit lebt. In einem hervor­ragenden Amerikaner hat sich die amerikanische Freiheit selbst charak­terisiert. Und nehmen wir all dasjenige, was in Europa geistige Heroen geleistet haben, um diese göttliche Freiheit zu schildern als die hohe, hehre Göttin, so ist das allermeiste davon so, daß man sagen muß: All unser Enthusiasmus, all unsere Begeisterung, all unsere Empfindungen, Gedanken, Gefühle, sie wenden sich hin zu dem, was den Europäern vorgeschwebt hat als höchstes Ideal der Freiheit.",
      "Begreift, meine lieben Freunde, daß noch etwas ganz anderes die Freiheit werden muß für die Anhänger der spirituellen Weltbetrach­tung. Ihr werdet alles schlecht verstehen, wenn Ihr nicht das Bewußt­sein habt, daß alles neu sich gestalten muß. Wir stehen vor der Forde­rung, daß Freiheit noch etwas ganz anderes werden muß, als was bisher als hohes Ideal gefühlt haben, was verstanden haben selbst die Besten der Menschheit. Denn wir wissen, daß wir in der nächsten Zeit als Menschen werden gehen dürfen zu einer göttlichen Quelle, daß wir trinker werden dürfen Geisteswasser, und daß dieses Geisteswasser in unseren Seelen leben wird, und daß wir mit ihm werden verseelischen müssen die Freiheit, so wie wir mit unserem Körper verkörperlichen die Seele. Dem einen ist die Freiheit praktisch für das äußere Leben, dem andern ist sie ein hohes geistiges, hehres Ideal, dem dritten muß die Freiheit sein dasjenige, was er verseelischen darf, was höher ist als die Seele, soviel höher als die Seele, wie die Seele höher ist als der Leib. Wir sollen lernen zu verseelischen die Freiheit. Vieles sollen wir lernen, also die Freiheit zu verseelischen, dann schreiten wir so vorwärts, wie es die ewigen, geistigen Mächte für die Menschheitsevolution haben wollen, indem sie in Eure Seelen Theosophie haben einfließen lassen.",
      "So, meine lieben Freunde, wollen wir einfach gesprochene Worte, die nicht zu Eurem Verständnis, sondern zu Euren Herzen gesprochen sein wollten, so wollen wir diese Worte hinnehmen in dieser Stunde, da Ihr die Möglichkeit gefunden habt, auch in äußerer Weise innerhalb Eures Landes organisatorisch Euch der Theosophie zu ergeben; so wol­len wir zum Anlaß nehmen, in diesem Augenblick uns bewußt zu wer­den der hohen Aufgabe, die uns durch spirituelle Auffassung der Welt gegeben wird. Meine lieben Freunde! Dieses Bewußtsein wird es machen,",
      "daß, wenn wir in ihm leben, von jener stillen Arbeit in den theosophi­schen Zweigen ausstrahlen wird etwas, was von Heil sein wird für das ganze Land, denn der beginnt erst das spirituelle Leben zu verstehen, der da weiß, daß nicht nur dasjenige, was wir in äußerer Weise tun kön­nen zur Verbreitung der Theosophie, wirklich beiträgt zur Verbreitung der Theosophie, nein, daß auch, wenn wir zusammenarbeiten, so gut wie wir können, Verständnis zu gewinnen der Theosophie, daß auch dann unsichtbar ausstrahlen die Wirkungen unseres geistigen Strebens. Und wie wir ja wissen, daß eine Stadt, in der eine theosophische Loge ist, nach dreißig Jahren etwas ganz anderes ist, wenn auch nur wenige dort theosophisch gewirkt haben, als eine Stadt, in der sich keine theosophi­sche Loge befindet, so wird Euer Land ein ganz anderes werden, wenn Ihr mit innerem Verständnis empfindet, was Theosophie Euch geben kann.",
      "Ich spreche zu Euch nicht als Westeuropäer, nicht als Ange­höriger dieser oder jener Nation. Ich weiß, daß das nicht der Fall ist. Aber vielleicht gerade deshalb darf ich zu Euch sagen: Es gibt ein Heil für Rußland, es gibt ein Heil, aber dieses Heil darf nicht auf falschem Wege gesucht werden.",
      "Auch nicht deshalb, weil ich die Theosophie liebe, sage ich dieses, sondern deshalb, weil die ganze Menschheitsent­wickelung uns das lehren kann als die Wahrheit. Es gibt ein Heil für Rußland und dieses Heil heißt: die Theosophie.",
      "Für andere Gegenden der Erde wird Theosophie ein Vortreffliches, ein die Menschen Wei­terbringendes sein. Für Rußland wird Theosophie das einzige Heil sein, dasjenige, was da sein muß, damit das russische Volkstum den Anschluß findet an seine Volksseele, damit diese Volksseele nicht zu andern Auf­gaben in der Welt berufen wird als die, welche ihr vorbestimmt ist.",
      "Mit diesen Worten möchte ich Eure neugegründeten Zweige ein­weihen, denn ich weiß, wie in Euren Herzen aufgeht die heilige Be­deutung dieser Worte. Dann wird in Euren Seelen jene Verbindung wirken können, die zum Heile Eures Landes notwendig ist: die Ver­bindung des Mysteriums von Golgatha mit dem menschlichen Ver­ständnis dieses Mysteriums. Dann wird walten in Euren Herzen der Geist, welcher der Regenerator Eures Landes werden soll; dann wird ausstrahlen aus Euren Versammlungen dasjenige, was Euer Erdenge­biet braucht. Aus diesem Bewußtsein heraus und aufblickend zu den",
      "führenden Mächten der Menschheitsevolution in Andacht und Ehr­furcht spreche ich es aus, daß ich allen Segen herabrufen möchte auf Eure Arbeit, herabrufen möchte in die Kraft Eurer Herzen, herab­rufen möchte den Segen derjenigen Mächte, die heute in Menschenher­zen das Geheimnis von Golgatha einfließen lassen, damit dieser Segen von Euren Seelen weiterwirkt in Strahlen von Eurer Arbeit ausgehend in Euer Land. Und ich weiß, daß dieser Segen immer vorhanden ist, wenn wir seiner würdig sind. So schwebe uns denn, da wir gewisser­maßen am Ausgangspunkte Eurer Arbeit stehen, so schwebe uns vor das Bild unseres Bewußtseins wie ein neuer Impuls, der spirituelle Im­puls, der sich ergießen muß in die Menschheitsentwickelung, wie hel­fend die geistigen Führer dieses Impulses überschweben unsere Arbeit, die wir in Aufrichtigkeit vollführen wollen. Dann entspringt aus die­sem Bilde das Bewußtsein, daß wir für das engere Gebiet tun, was getan werden muß, und damit auch für das ganze weite Gebiet der Mensch­heitsentwickelung, dann entspringt aus diesem Bilde unsere Pflicht. Möge in diesem Sinne der Segen der weisen Welt- und Menschheits­lenker über Eurer Arbeit walten, möge kraftvoll aufgehen in Euren Seelen dieser Segen, Licht sein in Euren Seelen, dann wird dieses Licht herausströmen können und Ihr werdet vieles tun können, was vieles Bedeutsames zum Heil, zum Fortschritt, zur wahren Menschheitsent wickelung ist."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Als wir uns im letzten Jahre hier versammelten, war gewissermaßen in den Herzen derjenigen, welche dazumal schon mit unseren russi­schen Freunden versammelt waren, dasjenige noch Knospe, was in einer gewissen Weise sich doch bis in dieses Jahr herein entfaltet hat, das Bewußtsein, das immer mehr und mehr Eure Herzen durchziehen soll, daß Theosophie, oder wie wir es auch nennen, Anthroposophie, nicht etwas ist, was der Mensch wie ein anderes Wissen oder wie ein anderes einzelnes Glaubensbekenntnis aufnehme, sondern was in einer gewissen Beziehung die ganze Seele jedes einzelnen ergreifen soll, was die Seele der ganzen Menschheit in unserem Zeitenzyklus ergreifen soll.",
        "Dieses Bewußtsein muß sich nach und nach entwickeln, und man sollte gar nicht glauben, man muß sich gar nicht der Illusion hingeben, daß man leicht zu der vollen Bedeutung und vollen Kraft dieses Bewußtseins kommt.",
        "Denn nur nach und nach, langsam und ganz allmählich können wir im Erleben uns erringen das Bewußtsein von der Bedeutung des theosophischen Impulses."
      ],
      [
        "Eine solche Wahrheit sieht scheinbar recht trivial aus, aber hier ist es gerade, wo wir dasjenige, was wie recht trivial ausschaut, mit aller­tiefstem Ernst nehmen müssen.",
        "Denn nehmt aus der Fülle dessen, was zu diesem Bewußtsein gehört, ein Einzelnes heraus, nehmt heraus, daß es nahezu zweitausend Jahre her ist, daß der Christus-Impuls sich aus höheren Welten in das Erdenleben hereingesenkt hat, nehmt die Tat­sache, daß das Evangelium zu den allerverbreitetsten Büchern der Welt gehört, nehmt die Tatsache, daß durch Jahrhunderte und aber Jahr­hunderte Millionen von Menschenseelen geglaubt haben, ein richtiges Verhältnis zum Christus zu haben, und stellt die Tatsache daneben, daß es wahr ist, daß die ehrliche Menschenseele, die nicht in Unbe­scheidenheit ein Verständnis sich zuschreiben will, das sie nicht hat,"
      ],
      [
        "in unserer Zeit mit der Frage ringen muß: Was ist eigentlich dieser Christus-Impuls? - Und daß diese Seele erst hoffen kann von neuen Offenbarungen aus der geistigen Welt ein Verständnis dieses Christus-Impulses wirklich zu gewinnen!",
        "Nehmt andere Tatsachen.",
        "Mit einigen Freunden besuchte ich im vorigen Jahre den Ostergottesdienst der rus­sischen Kirche.",
        "Ich habe damals unmittelbar danach versucht, ein Wort auszusprechen, von dem ich angenommen habe, daß es Euch zu denken gibt.",
        "Der Gottesdienst strömte aus bloß das Bewußtsein von dem ge­storbenen Christus.",
        "Der Menschheit zum Heile muß in unserer Zeit und in Zukunft aber sein die Botschaft von dem immerfort lebenden Christus. t)och ein anderes Bild ergab sich mir, wie als der Hintergrund dieses Gottesdienstes, von dem hinweggedacht werden mußte, was die diesem Kultus nicht gewachsenen Persönlichkeiten dort taten.",
        "Es ergab sich als der Hintergrund ein Tableau uralt heiliger Mysterien, die sich doch fortentwickelt haben bis zu dem, was in diesem Kultus äußerlich in den Formen lebt,was viele Menschenherzen zwar fühlen,was aber ge­rade von denjenigen am wenigsten verstanden wird, welche die berufen­sten Interpreten sein sollten oder sich dafür halten in der Gegenwart."
      ],
      [
        "Versucht, den Gedanken durch solche Hinweise, wie sie soeben aus­gesprochen sind, tiefer und immer tiefer in Eure Seelen zu graben, daß die Theosophie von einem jeden einzelnen Herzen ausgeht, daß durch Theosophie oder Anthroposophie etwas völlig Neues in die Mensch­heitsentwickelung einströmen muß.",
        "Versucht einzugraben in Eure Her­zen die Wahrheit, daß die Zeichen der Zeit so stehen, daß wir wirklich wenigstens in unseren Seelen selber, in unseren Herzen selber, zuwei­len ganz still und intim, niemals einen Kompromiß schließen dürfen mit dem, was um uns herum ist.",
        "Aus einer Pflanze kann nicht ohne wei­teres eine neue Pflanze erstehen, aus einer Pflanze kann nur eine neue Pflanze werden, wenn die alte Pflanze abstirbt und sich wie aus einem einzigen Punkte heraus, aus dem Keim, eine neue Pflanze bildet.",
        "So ist Theosophie in der Tat etwas, meine lieben Freunde, was sich wie ein völlig neuer Keim entwickeln muß in unseren Seelen, in unseren Her­zen, was von allem, was die alte Menschheitspflanze gehabt hat, nur das eine behalten muß, was aber universell ist, nur das eine, was wir schauen bei dem Anblick des Mysteriums von Golgatha.",
        "Die Blätter,"
      ],
      [
        "der Stamm der uralten Menschheitskultur, sie werden abfallen müssen; die Blüte, das Mysterium von Golgatha, wird wie eine Erinnerung bleiben müssen von dem Keime, der sich entwickeln soll in der Theo­sophie.",
        "Und dieser Keim, meine lieben Freunde, wird in sich tragen müssen das Bewußtsein, diese Blüte immer mehr und mehr zur vollen Entfaltung zu bringen auf eine neue und immer wieder neue Weise.",
        "Dann wird in vielen Formen der Christus-Impuls durch die Mensch­heitsevolution leben und doch immer derselbe sein, wie jede neue Blüte die Kraft und Schönheit der alten Blüte in sich trägt.",
        "Aber er wird zugleich dasjenige sein, was er im Intimsten sein will, ein immer neu und wieder neu Erstehendes, ein neu und wieder neu sich erwirkendes Verständnis desjenigen, was wie ein neuer Anfang der Menschheitsent­wickelung gegeben war, als das Blut floß aus den Wunden desjenigen, der menschliche Gestalt angenommen hat, um den Tod zu erleben in­nerhalb der Menschheit."
      ],
      [
        "Meine lieben Freunde!",
        "Alle Welten, die wir durchschreiten können von unserer physischen Welt durch die höheren Welten immer weiter und weiter, sie haben immer Gemeinsames.",
        "Es ist richtig, daß wir, wenn wir in eine höhere Welt kommen, zwar immer Neues und Neues finden, aber dennoch immer Gemeinsames mit der vorhergehenden Welt.",
        "Wenn wir aber die höheren Welten kennenlernen, so ist eines nicht darinnen, was als physische Erscheinung nur, als physische Er­scheinung allein existieren kann.",
        "Die Götter der höheren Welten kön­nen Mannigfaches erfahren, eines können sie niemals erfahren, den Tod.",
        "Denn der Tod existiert nicht in den übersinnlichen Welten.",
        "In den übersinnlichen Welten verwandeln sich die Wesen, sie gehen von einer Form in die andere über; sterben kann man nicht in der über­sinnlichen Welt.",
        "Der Tod als physische Erscheinung ist dasjenige, was nur vorhanden sein kann als physische Erscheinung.",
        "Und unter allen Göttern und Geistern war es der einzige, der, um mit der Menschheit ein Gemeinsames zu haben, heruntergestiegen ist in die Welt der Menschheit, der Christus, der sich durch seinen Tod verknüpft hat mit der Menschheit, nicht etwa nur durch sein Leben.",
        "Aber durch einen Tod hat er sich verknüpft, von dem ausgegangen sind neue Lebens-kräfte.",
        "Hinzuschauen auf den Tod auf Golgatha, das muß werden der"
      ],
      [
        "Menschheit der Ausgangspunkt für immer neue und neue Lebenskräfte, denn mit diesem Tode ist in einem einzigen Punkte der Menschheits­entwickelung konzentriert dasjenige, was mit einem unendlichen Opfer nur ein Gott für die Menschheit hat vollbringen wollen.",
        "Man versuche diesen Gedanken durchzudenken, versuche diesen Gedanken zu einer lebendigen Meditation zu machen, und man wird sehen, daß von die­sem Gedanken die stärksten Lebenskräfte für eine jegliche menschliche Seele ausgehen können.",
        "Und so gibt es kein erhabeneres Bild, als das auf Golgatha errichtete Kreuz."
      ],
      [
        "Meine lieben Freunde!",
        "Mit einer solchen für die ganze Menschheit hingestellten Imagination wie das Kreuz auf Golgatha, mit einer sol­chen Imagination ist der Menschheit ein Unendliches gegeben.",
        "Hinge-stellt ist es vor nahezu zwei Jahrtausenden, dieses Symbolum, das zu­gleich reale Wirklichkeit war, und noch müssen wir es immer mehr und mehr verstehen lernen in der Menschheitsevolution der Zukunft.",
        "Das sind einfache, primitive Gedanken, aber sie sind nicht dazu da, um in uns einen metaphysischen Charakter anzunehmen, sondern um Emp­findungen anzunehmen, die uns geeignet machen, in der richtigen Weise uns hineinzustellen in die ganze Menschheitsentwickelung."
      ],
      [
        "Ihr wißt, meine lieben Freunde, daß die Menschheitsentwickelung differenziert vor sich gegangen ist; in einzelnen Nationen, Völkern ging sie vor sich.",
        "Jedes Volk hat einen ganz besonderen Grundcharak­ter, der davon herrührt, daß ein jedes Volk zu seinem Führer hat einen derjenigen Geister, die wir zuzählen der Hierarchie der Archangeloi.",
        "Archangeloi sind die obersten Vorsteher gewissermaßen der einzelnen Völker.",
        "Daß die Menschenseele als einzelne Seele in der Zukunft immer mehr und mehr Zusammenhang gewinnt mit der führenden Volksseele aus der Reihe der Archangeloi, das ist etwas, was uns die spirituelle Weltanschauung bringen muß.",
        "Und nur wenn wir Verständnis ent­gegenbringen demjenigen, was für uns diese Volksseele will, wenn diese Volksseele ein Wollen in die Zukunft zu entwickeln hat, können wir in geeigneter Weise mitarbeiten an der spirituellen Evolution der Mensch­heit.",
        "In dieser Beziehung müssen wir einen großen Unterschied machen zwischen den westeuropäischen Volksseelen und der osteuropäischen, russischen Volksseele."
      ],
      [
        "Ich rede jetzt nicht von der äußeren russischen Kultur, von dem, was auf dem äußeren physischen Plan als russische Volkskultur vor­handen ist.",
        "Ich rede von Eurer in der geistigen Welt wirklich vorhan­denen Volksseele, welche eben daran ist zu warten auf ihre Aufgabe in der Zukunft, welche in sich voll der Erwartung, voll der Hoffnung, voll der Zuversicht ist."
      ],
      [
        "Wenn man vergleicht mit westeuropäischen Volksseelen diese Volksseele, dann hat man den Eindruck des Jungen, Aufstrebenden auf der einen, und des Alten, Greisenhaften auf der an­dern Seite.",
        "Die mitteleuropäische Kultur ist ja hereingeschoben zwi­schen West- und Osteuropa als eine Vermittlungskultur, welche im Grunde mißverstanden wird, wenn man sie den andern Kulturen gleichschätzt."
      ],
      [
        "In einer ganz eigentümlichen Weise hat diese mitteleuro­päische Kultur die Aufgabe, zu wirken wie ein Herold aus alten Zeiten in spätere Zeiten.",
        "Bedenkt einmal, meine lieben Freunde, wie im Grunde genommen die ganze europäische Kultur der westlichen Welt überhaupt zustande gekommen ist."
      ],
      [
        "Da waren die vorgeschobenen Po­sten der orientalischen Völker bis ins alte Indien hinein und es haben diese Völker eine große eindringliche Kultur entwickelt, wie sie uns entgegenkommt aus der Kultur des alten Indien, aus der Bhagavad Gita-Zeit.",
        "Diese Völker wurden nach dem Süden Asiens vorgeschoben."
      ],
      [
        "Während in ihnen lehrten weisheitsvolle Lehrer wie die Rishis und Zarathustra, waren zurückgeblieben im weitesten Umkreis der euro­päischen Länder Völker, auch in Eurem Lande, die gewissermaßen verblieben durch die Weisheit der Weltevolution in primitiven Zu­ständen.",
        "Während in Asien weitumfassende Gedanken in der Sankhya­und der Vedantaphilosophie blühten, hatten diese europäischen Völ­ker einfache, primitive Kulturen."
      ],
      [
        "Warum?",
        "Weil die Kulturen so fort­schreiten müssen, daß alles dasjenige, was später als Impuls kommen soll, von primitiven Menschen aufgenommen werden muß.",
        "Die bis zu einer gewissen Höhe der Intellektualität aufgestiegenen Völker des Ostens konnten nimmermehr zum Beispiel den Christus-Impuls ver­stehen, sie waren hinaus über die Möglichkeit, den Christus-Impuls zu verstehen."
      ],
      [
        "Die Völker der westländischen Kultur waren noch nicht so weit, das Geistige im Kopfe aufzunehmen, dasjenige, was als Kraft lebt vom"
      ],
      [
        "Herzen bis zum Kopf, war bei ihnen noch nicht bis zum Kopf ge­kommen.",
        "In Indien war alles Kopfkultur, in den europäischen Völkern war alles noch in primitiven Empfindungen in ursprünglicher Stärke im Herzen konzentriert.",
        "Nur solche Völker konnten, weil sie noch nicht hinaus waren über das Seelenhaftige des Herzens, die Mysterien von Golgatha nach und nach in die Empfindung sich einverweben.",
        "So war es die europäische Kultur, welche dadurch, daß sie zurückgeblieben war, in ursprünglicher, frischer Kraft dastand - und ursprüngliche frische Kraft ist näher mit dem Göttlichen verwandt -, bereit war, den Christus-Impuls aufzunehmen.",
        "So flossen zusammen innerhalb der abendländischen Welt zwei Strömungen, die für jeden, der dafür eine Empfindung hat, scharf zu unterscheiden sind.",
        "Wer würde nicht unter­scheiden können den eigentümlichen Grundton Fichtes, des mitteleuro­päischen Philosophen, und den eigentümlichen Grundton Spinozas, der ja auch ein europäischer Philosoph war.",
        "Es ist sogar in der Mensch­heitsevolution so, daß dasjenige, was der allgemeinen Kultur angehört, von derselben Individualität getragen werden kann.",
        "Denn dieselbe In­dividualität ist ja Spinoza und Fichte, wie vielleicht schon einige unse­rer Freunde wissen.",
        "Aber Fichte ist als einzelne Persönlichkeit des 18., 19.",
        "Jahrhunderts ein Geist, der durchdrungen werden konnte von der ganzen Kraft des Christus-Impulses; Spinoza, also dieselbe Indivi­dualität, steht aber in der andern Strömung darinnen und hat nichts davon."
      ],
      [
        "Es ist aber noch vieles nicht da, was in die europäische Kultur kom­men muß.",
        "Und es muß zusammenwirken dasjenige, was in gewisser Weise alt geworden ist, und dasjenige, was jung und hoffnungsfrisch ist.",
        "Die russische Volksseele, die Wesenheit aus der Reihe der Archan­geloi, ist jung und hoffnungsfrisch, sie hat ihre Aufgabe vor sich.",
        "Und an den russischen Theosophen wird es sein, die Brücke zu finden von der einzelnen Seele zur Volksseele, verstehen zu lernen, was die Volksseele von ihnen will.",
        "Ihr werdet finden, meine lieben Freunde, daß es unter gewissen Voraussetzungen gerade Euren Seelen leicht werden wird, den Christus-Impuls aus Euren Herzen heraus zu beleben durch das, was in Euren Seelen lebt.",
        "Ihr werdet auf der andern Seite erfahren müssen, daß auch, weil Ihr eine gewisse innere Leichtigkeit habt, um"
      ],
      [
        "den Christus-Impuls zu beleben, auf der andern Seite wiederum Euch große Schwierigkeiten erwachsen.",
        "Ihr werdet zu erfahren haben, daß gerade für Euch die tiefe Wahrheit in erhöhtem Maße gilt, daß Ihr auf Eure eigene Seele Euch werdet stellen müssen, daß Ihr werdet das Theosophische in Euren Seelen beleben müssen."
      ],
      [
        "Denn, meine lieben Freunde, Theosophie als Verkündigung unseres Zeitalters, sie will kei­nen Kompromiß schließen mit andern Weltanschauungen.",
        "Sie spricht ein strenges Wort zu andern Weltanschauungen.",
        "Sie spricht ein Wort zu andern Weltanschauungen, das auch schon gehört worden ist im Laufe der Entwickelung."
      ],
      [
        "Diejenigen, die Theosophie finden wollen in den bisherigen äußerlichen, materialistischen Kulturen - und das sind alle Kulturen der Gegenwart, oder nähern sich wenigstens dazu -, alle, die Kompromisse suchen werden, denen wird immerdar mit aller Strenge das Wort entgegenklingen, das einstmals der Christus Jesus ge­sprochen hat: Lasset die Toten ihre Toten begraben!",
        "Ihr aber folget mir nach!"
      ],
      [
        "Die Toten, das sind die einzelnen Kulturen, die sich dem Materialismus nähern, sie haben in sich schon die Fähigkeit, sich zum Grabe zu führen.",
        "«Lasset die Toten die Toten begraben!» Aber die Seelen sollen nachfolgen dem, was das Verständnis des spirituellen Impulses ist, der als Christus-Impuls durch die Welt waltet."
      ],
      [
        "Daher werdet Ihr nicht, meine lieben Freunde, finden, wenn Ihr anfragt bei demjenigen, was Euch alte Traditionen geben können, was Euch altes Herkommen geben kann, etwas, was Euch zur Theosophie führt.",
        "Es ist gut, dieses alte Herkommen, diese alten Traditionen aufzufinden, um zu zeigen, wie in ihnen das Göttliche waltet, aber zur Theosophie kommt heute der Mensch, gerade indem er eine Seele in sich trägt, in der nicht das Alte, Greisenhafte waltet, sondern eine Seele, wie Ihr sie tragt: frische, unmittelbare Seelen, wie Ihr sie unbeeinflußt von aller Tradition dieser Theosophie entgegenbringt."
      ],
      [
        "Lebenskraft, nicht bloße Erkenntniskraft erfordert der theosophische Impuls, fordert der theosophische Impuls von Euren Seelen."
      ],
      [
        "Meine lieben Freunde!",
        "Viele von Euch, vielleicht die meisten, viel­leicht sogar alle, fühlen in sich, wenn sie es auch vielleicht anders defi­nieren, den Schmerz, das Leid des Getrenntseins von der Volksseele, des vorläufigen Getrenntseins von Eurer Volksseele.",
        "Viele von Euch fühlen,"
      ],
      [
        "wenn sie es auch anders glauben, vielleicht die meisten, vielleicht alle fühlen in sich, wie sie brauchen neuen Ansporn zu Wille und Kraft.",
        "Beginnt einmal, meine lieben Freunde, das, was Ihr so als Leid fühlt des oftmals mangelnden Willens und der oftmals mangelnden Kraft, beginnt einmal, entschließt Euch dieses anzusehen als das Jungfräu­liche Eures Willens, entschließt Euch, dieses anzusehen als einen Willen, der unberührt geblieben ist, und der nur auf das Angesporntwerden wartet von demjenigen, was theosophischer Impuls ist!"
      ],
      [
        "Laßt den theo­sophischen Impuls in Euch Wille werden!",
        "Versucht das Leid in Kraft, den schwachen Willen in die in Euch wollende Theosophie zu wandeln, Ihr werdet können dadurch wirklich in das theosophische Leben hin­einkommen!"
      ],
      [
        "Versucht umzuinterpretieren, was in Euch noch schwach, noch nicht ganz da ist!",
        "Ihr werdet so zu den besten Trägern der Theo­sophie werden können!",
        "Denn bedenkt, die Seelen, die jetzt in Euren Leibern sind, sind nicht dazu bestimmt, in der nächsten Inkarnation nur in Osteuropa wieder inkarniert zu werden."
      ],
      [
        "Sie sind dazu bestimmt, in den nächsten Inkarnationen verteilt zu werden über die ganze Erde hin.",
        "Und etwas wird vor Euch stehen zwischen Tod und einer neuen Geburt, das so zu Euch sprechen wird, wenn Ihr in eine neue Inkarna­tion kommen werdet."
      ],
      [
        "Zu dem Einen wird es sprechen: Du hast deine Aufgabe erfüllt, du kannst das, was du aufgenommen hast auf der Erde, in die Welt tragen, was nur auf dem Boden Osteuropas aufge­nommen werden konnte. - Zu dem andern wird es sprechen: Du kannst es nicht!"
      ],
      [
        "Meine lieben Freunde, betrachtet dasjenige, was Ihr jetzt für Theo-sophie fühlt, als den Instinkt für das eben Ausgesprochene, als das un­bestimmte Fühlen, was in Euch ist von dieser Eurer Aufgabe.",
        "Betrachtet es so, daß es vom Ich in das Denken, Fühlen und Wollen, von da in das Leben, von da in das Blut Euch Kraft geben kann, dann werdet Ihr die­sen Instinkt, aus dem Ihr jetzt zur Theosophie eilt, in der richtigen Weise deuten."
      ],
      [
        "Ihr habt Euch nun in äußerlicher Weise gesammelt.",
        "Ihr habt die Möglichkeit gefunden, unter den großen Schwierigkeiten, die in Eurem Lande bestehen, ungehindert äußerlich sammeln zu können.",
        "Gebraucht diese Möglichkeit zu möglichst starker innerer Sammlung, um die"
      ],
      [
        "Brücke zu schlagen, ein jeder einzelne von Euch, zu der Volksseele hin­auf.",
        "Es kann meine Aufgabe nicht sein, meine lieben Freunde, davon zu sprechen, welche Dienste im einzelnen dieser Volksseele geleistet werden müssen."
      ],
      [
        "Aber von etwas anderem darf ich Euch sprechen, von dem ich möchte, daß es zwar als Wort ausgesprochen wird, sich in Euch aber in ein Gefühl verwandele.",
        "Ihr seid in einer eigentümlichen Lage, meine lieben Freunde."
      ],
      [
        "Ihr seid gewissermaßen in der gegenteiligen Lage von einem Volke, das in einer gewissen Beziehung zu einem kurzen Glanze auch aufsteigender Art die Erde bevölkert.",
        "Ihr seid in einer gegenteiligen Lage wie das nordamerikanische Volk."
      ],
      [
        "Bedenkt, meine lieben Freunde, daß dieses nordamerikanische Volk, das Euer Gegenpol ist, von der Zeit ab begonnen hat, vom Westen allmählich gegen den Osten vorzurücken, in der in Europa das Zeitalter des Materialismus begonnen hat, und ihn weiter ausgebaut hat.",
        "Bedenkt, daß in den Wur­zeln des Amerikanertums der Materialismus waltet."
      ],
      [
        "Bedenkt einmal, daß diejenigen Menschen, die Amerika kultiviert haben, dies getan haben mit den Vorstellungen des kultivierten Europäers vor Jahrhun­derten, die so wenig weit hinter uns liegen.",
        "Was haben denn diese Men­schen gemacht?"
      ],
      [
        "Diese Menschen haben mit den materialistischen Vor­stellungen der modernen Parlamente, mit den Vorstellungen der mo­dernen Naturwissenschaft, der modernen Gesellschaftsordnung das­jenige getan, was sonst die ungebildeten Menschen machen, wenn sie Urwälder ausroden, Stück für Stück Ackerboden erobern, Land be­reiten der Kultur.",
        "Das ist alles aus Materialismus entsprungen."
      ],
      [
        "Und wenn man heute betrachtet den als ihren bedeutendsten Schriftsteller Anerkannten, den ja auch die Amerikaner durch Wahl zu ihrem Leiter bestimmt haben, Woodrow Wilson, der für die heutigen Verhältnisse wirklich ein bedeutender Schriftsteller ist, der Glänzendes an schrift­stellerischen Leistungen für die soziale Anschauung geleistet hat, wenn man ihn anschaut, seine Begriffe und Ideen, alles, was er repräsentiert als Vertreter des amerikanischen Volkes, was ist es?",
        "Ein Kartenhaus."
      ],
      [
        "Ein Kartenhaus, von einem einzigen Hauch, wenn er einmal gehaucht würde aus den spirituellen Welten heraus, vernichtet.",
        "Dann würde diese ganze Kultur umfallen.",
        "Jede Einzelheit, aus der die amerikanische Kultur stammt, kann man nachweisen aus äußeren Geschichtsbüchern,"
      ],
      [
        "aus der Kulturgeschichte der vorigen Jahrhunderte.",
        "Alles liegt offen da, alles ist Menschenwerk, woraus das entsprungen ist."
      ],
      [
        "Fragt nach, woher Euer Volkstum kommt, woher Euer Geistesleben stammt, fragt nach, woher das Beste kommt, was Ihr in Euren Seelen hegen könnt.",
        "Ihr werdet es auf der Erde nicht finden!",
        "Das ist nicht in dieser Weise zu finden, das wurzelt in der geistigen Welt selber.",
        "Das ist Organismus, Lebewesen, das ist kein Kartenhaus!",
        "Solche Dinge dür­fen wir niemals zur Veranlassung nehmen unseres Hochmutes, sondern zur Veranlassung unserer Demut, unserer Bescheidenheit, weil wir aus ihm nicht holen sollen ein waghalsiges Selbstbewußtsein, sondern Ver­antwortlichkeitsgefühl."
      ],
      [
        "Meine lieben Freunde!",
        "Ich habe gestern über die Freiheit gesprochen.",
        "Es wird viel Wasser hinunterfließen müssen die europäischen Ströme, bis eine gewisse Anzahl von Menschen voll versteht, was mit dieser Freiheit begriffen werden soll, was mit dieser Freiheit gemeint ist."
      ],
      [
        "Was ist Freiheit?",
        "Gehen wir vom Westen nach dem Osten!",
        "Was ist für den Amerikaner Freiheit?",
        "Dasjenige, was ihm das Leben am bequemsten einrichtet.",
        "Er nennt Freiheit dasjenige, was hineinverwoben werden soll in die soziale Ordnung, damit am besten ein jeder einzelne für die äu­ßere Welt vorwärtskommt."
      ],
      [
        "Wir kennen Freiheit anders - sagt Wood­row Wilson -, als der Europäer, wir kennen Freiheit, weil sie uns prak­tisch erscheint. - So sagt der Amerikaner selber.",
        "Ein Messer nimmt man zum Schneiden, eine Gabel zum Essen, weil sie praktisch sind dazu."
      ],
      [
        "Der Amerikaner nimmt die Freiheit, weil sie praktisch ist dafür, was er braucht, weil er am besten damit die Ordnung herstellen kann, die ihm angenehm ist.",
        "Freiheit ist für den Amerikaner ein Nützlichkeitspro­dukt, sie bringt ihm Nutzen."
      ],
      [
        "Meine lieben Freunde!",
        "Für den Westeuro­päer war die Freiheit etwas anderes, war Freiheit ein hohes Ideal, etwas, wozu er aufblickte.",
        "Man darf fast das Wort des Dichters auf die Freiheit anwenden.",
        "Dem Europäer ist sie die «hohe herrliche Göttin», für den Amerikaner ist sie die nützliche Melkkuh, die ihn mit Milch und Butter versorgt. ich sage das nicht, sondern derjenige, der in den nächsten Jahren verantwortlich ist für die Leitung der Amerikanischen Vereinigten Staaten, hat das gesagt."
      ],
      [
        "Es ist nun überhaupt nicht meine Aufgabe, meine Meinung vorzubringen, sondern nur der Interpret"
      ],
      [
        "zu sein für dasjenige, was in der geistigen Weit lebt.",
        "In einem hervor­ragenden Amerikaner hat sich die amerikanische Freiheit selbst charak­terisiert.",
        "Und nehmen wir all dasjenige, was in Europa geistige Heroen geleistet haben, um diese göttliche Freiheit zu schildern als die hohe, hehre Göttin, so ist das allermeiste davon so, daß man sagen muß: All unser Enthusiasmus, all unsere Begeisterung, all unsere Empfindungen, Gedanken, Gefühle, sie wenden sich hin zu dem, was den Europäern vorgeschwebt hat als höchstes Ideal der Freiheit."
      ],
      [
        "Begreift, meine lieben Freunde, daß noch etwas ganz anderes die Freiheit werden muß für die Anhänger der spirituellen Weltbetrach­tung.",
        "Ihr werdet alles schlecht verstehen, wenn Ihr nicht das Bewußt­sein habt, daß alles neu sich gestalten muß.",
        "Wir stehen vor der Forde­rung, daß Freiheit noch etwas ganz anderes werden muß, als was bisher als hohes Ideal gefühlt haben, was verstanden haben selbst die Besten der Menschheit.",
        "Denn wir wissen, daß wir in der nächsten Zeit als Menschen werden gehen dürfen zu einer göttlichen Quelle, daß wir trinker werden dürfen Geisteswasser, und daß dieses Geisteswasser in unseren Seelen leben wird, und daß wir mit ihm werden verseelischen müssen die Freiheit, so wie wir mit unserem Körper verkörperlichen die Seele.",
        "Dem einen ist die Freiheit praktisch für das äußere Leben, dem andern ist sie ein hohes geistiges, hehres Ideal, dem dritten muß die Freiheit sein dasjenige, was er verseelischen darf, was höher ist als die Seele, soviel höher als die Seele, wie die Seele höher ist als der Leib.",
        "Wir sollen lernen zu verseelischen die Freiheit.",
        "Vieles sollen wir lernen, also die Freiheit zu verseelischen, dann schreiten wir so vorwärts, wie es die ewigen, geistigen Mächte für die Menschheitsevolution haben wollen, indem sie in Eure Seelen Theosophie haben einfließen lassen."
      ],
      [
        "So, meine lieben Freunde, wollen wir einfach gesprochene Worte, die nicht zu Eurem Verständnis, sondern zu Euren Herzen gesprochen sein wollten, so wollen wir diese Worte hinnehmen in dieser Stunde, da Ihr die Möglichkeit gefunden habt, auch in äußerer Weise innerhalb Eures Landes organisatorisch Euch der Theosophie zu ergeben; so wol­len wir zum Anlaß nehmen, in diesem Augenblick uns bewußt zu wer­den der hohen Aufgabe, die uns durch spirituelle Auffassung der Welt gegeben wird.",
        "Meine lieben Freunde!",
        "Dieses Bewußtsein wird es machen,"
      ],
      [
        "daß, wenn wir in ihm leben, von jener stillen Arbeit in den theosophi­schen Zweigen ausstrahlen wird etwas, was von Heil sein wird für das ganze Land, denn der beginnt erst das spirituelle Leben zu verstehen, der da weiß, daß nicht nur dasjenige, was wir in äußerer Weise tun kön­nen zur Verbreitung der Theosophie, wirklich beiträgt zur Verbreitung der Theosophie, nein, daß auch, wenn wir zusammenarbeiten, so gut wie wir können, Verständnis zu gewinnen der Theosophie, daß auch dann unsichtbar ausstrahlen die Wirkungen unseres geistigen Strebens.",
        "Und wie wir ja wissen, daß eine Stadt, in der eine theosophische Loge ist, nach dreißig Jahren etwas ganz anderes ist, wenn auch nur wenige dort theosophisch gewirkt haben, als eine Stadt, in der sich keine theosophi­sche Loge befindet, so wird Euer Land ein ganz anderes werden, wenn Ihr mit innerem Verständnis empfindet, was Theosophie Euch geben kann."
      ],
      [
        "Ich spreche zu Euch nicht als Westeuropäer, nicht als Ange­höriger dieser oder jener Nation.",
        "Ich weiß, daß das nicht der Fall ist.",
        "Aber vielleicht gerade deshalb darf ich zu Euch sagen: Es gibt ein Heil für Rußland, es gibt ein Heil, aber dieses Heil darf nicht auf falschem Wege gesucht werden."
      ],
      [
        "Auch nicht deshalb, weil ich die Theosophie liebe, sage ich dieses, sondern deshalb, weil die ganze Menschheitsent­wickelung uns das lehren kann als die Wahrheit.",
        "Es gibt ein Heil für Rußland und dieses Heil heißt: die Theosophie."
      ],
      [
        "Für andere Gegenden der Erde wird Theosophie ein Vortreffliches, ein die Menschen Wei­terbringendes sein.",
        "Für Rußland wird Theosophie das einzige Heil sein, dasjenige, was da sein muß, damit das russische Volkstum den Anschluß findet an seine Volksseele, damit diese Volksseele nicht zu andern Auf­gaben in der Welt berufen wird als die, welche ihr vorbestimmt ist."
      ],
      [
        "Mit diesen Worten möchte ich Eure neugegründeten Zweige ein­weihen, denn ich weiß, wie in Euren Herzen aufgeht die heilige Be­deutung dieser Worte.",
        "Dann wird in Euren Seelen jene Verbindung wirken können, die zum Heile Eures Landes notwendig ist: die Ver­bindung des Mysteriums von Golgatha mit dem menschlichen Ver­ständnis dieses Mysteriums.",
        "Dann wird walten in Euren Herzen der Geist, welcher der Regenerator Eures Landes werden soll; dann wird ausstrahlen aus Euren Versammlungen dasjenige, was Euer Erdenge­biet braucht.",
        "Aus diesem Bewußtsein heraus und aufblickend zu den"
      ],
      [
        "führenden Mächten der Menschheitsevolution in Andacht und Ehr­furcht spreche ich es aus, daß ich allen Segen herabrufen möchte auf Eure Arbeit, herabrufen möchte in die Kraft Eurer Herzen, herab­rufen möchte den Segen derjenigen Mächte, die heute in Menschenher­zen das Geheimnis von Golgatha einfließen lassen, damit dieser Segen von Euren Seelen weiterwirkt in Strahlen von Eurer Arbeit ausgehend in Euer Land.",
        "Und ich weiß, daß dieser Segen immer vorhanden ist, wenn wir seiner würdig sind.",
        "So schwebe uns denn, da wir gewisser­maßen am Ausgangspunkte Eurer Arbeit stehen, so schwebe uns vor das Bild unseres Bewußtseins wie ein neuer Impuls, der spirituelle Im­puls, der sich ergießen muß in die Menschheitsentwickelung, wie hel­fend die geistigen Führer dieses Impulses überschweben unsere Arbeit, die wir in Aufrichtigkeit vollführen wollen.",
        "Dann entspringt aus die­sem Bilde das Bewußtsein, daß wir für das engere Gebiet tun, was getan werden muß, und damit auch für das ganze weite Gebiet der Mensch­heitsentwickelung, dann entspringt aus diesem Bilde unsere Pflicht.",
        "Möge in diesem Sinne der Segen der weisen Welt- und Menschheits­lenker über Eurer Arbeit walten, möge kraftvoll aufgehen in Euren Seelen dieser Segen, Licht sein in Euren Seelen, dann wird dieses Licht herausströmen können und Ihr werdet vieles tun können, was vieles Bedeutsames zum Heil, zum Fortschritt, zur wahren Menschheitsent wickelung ist."
      ]
    ]
  },
  {
    "order": 14,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Der Zusammenhang des Menschen mit der elementarischen Welt",
      "Einige Bemerkungen zu dieser Buchausgabe. Das Thema des einführenden öffentlichen Vortrages «Das Wesen der nationalen Epen mit speziellem Hinweis auf Kale­wala», der im Frühjahr 1912 in Helsingfors gehalten wurde, nahm Rudolf Steiner zwei Jahre später ins Winter 1914 in Dornach wieder auf. Jetzt hieß das Thema »Der Zusammenhang des Menschen mit der elementarischen Welt. Finnland und Kale­wala» und wurde an drei Abenden dargestellt. Am Ende des Jahres sprach Rudolf Steiner auch in Dornach über «Das Traumlied des Olaf Ästeson», nun auf diese norwegische epische Dichtung hinweisend. So war es gegeben, diesen Vortrag und die beiden 1912 und 1913 vorangegangenen Betrachtungen über das gleiche Thema in diesen Band aufzunehmen. An die drei Vorträge über Kalewala schlossen sich dann die Ausführungen über «Die Welt als Ergebnis von Gleichgewichtswirkungen» an. -In mahnenden Worten macht Rudolf Steiner - man fasse den Zeitpunkt, in welchem diese Vorträge stattfanden, ins Auge - darauf aufmerksam, »daß die Fortentwicke­lung der Menschheit davon abhängt, daß wirklich die geistigen Wahrheiten durch­dringen werden, daß wirklich die Menschen hinter die Sinneswelt sehen lernen». Inhalt und Charakter dieser Vorträge schienen daher auch geeignet zu sein, zwei Ansprachen mit diesen Darstellungen zu vereinigen, welche bisher noch nicht ver­öffentlicht wurden. Es handelt sich um die beiden in Helsingfors 1912 und 1913 gehaltenen Vorträge für russische Zuhörer, welche damals zu den in Helsingfors stattgefundenen Vortragszyklen aus Rußland hergereist kamen. Die Nachsehriften durften auf Rudolf Steiners ausdrückliche Anweisung nur in Ausnahmefällen nach­gelesen werden, und dieses wurde auch seitdem beibehalten. Die geistigen Wahrheiten, welche Rudolf Steiner damals einem nur kleinen Kreise anvertraute, müssen aber heute ins allgemeine Bewußtsein aufgenommen werden. So wurde der Entschluß zur Veröffentlichung gefaßt. Die vorangehenden Ausführungen erhellen genügend die Tiefen und Zusammenhänge der verschiedenen Volkstümer, um die Wahrheiten über das russische Volkstum so aufzunehmen, wie es von Rudolf Steiner zum Ausdruck gebracht wurde.",
      "11    Theosophische Gesellscha ft: Später Anthroposophische Gesellschaft.",
      "eine Reihe von Vorträgen: «Die geistigen Wesenheiten in den Himmelskör­pern und Naturreichen», Bibl.-Nr. 136, Gesamtausgabe 1960.",
      "zwei öffentliche Vorträge: Der zweite öffentliche Vortrag vom 12. April 1912 ist ebenfalls veröffentlicht in Bibl.-Nr. 136.",
      "12    Herman Grimm: Ilias, zweite Auflage in einem Bande, Stuttgart-Berlin 1907. Rudolf Steiner führt in seinen Notizen zu diesem Vortrag für die Ilias-Betrach­tung folgende Seiten an: 298, 307, 327 oben, 330: Vielseitigkeit, Tötung des Patroklus; 360: Thetis' Doppeldasein; 395: Nibelungen; 417.",
      "22    denkende Naturforscher: Beispielsweise Robert Wiedersheim, 1848-1923, Ana­tom.",
      "in dem 6., 7. vorchristlichen lahrhundert: Siehe »Die Geheimwissenschaft im Umriß», Bibl.-Nr. 13, Gesamtausgabe Dornach 1968. Die Weltentwickelung und der Mensch. Erste, urindische, zweite, urpersische nachatlantische Kulturepoche;",
      "dritte ägyptisch-chaldäische Kulturepoche; vierte, griechisch-lateini­sehe Kulturepoche; fünfte nachatlantische Kulturepoche: 1413-3573. Ein Kul­turzeitalter umfaßt 2160 Jahre. Viertes Zeitalter: 747 v. Chr. bis 1413 n. Chr.",
      "38    wie ein Motto: Vergl. Kalewala, 40. Rune, und Eingangsstrophe «Kanteletar» von Elias Lönnrot, 1802-1884.",
      "40    «Theosophie»: Einführung in übersinnliche Welterkenntnis und Menschenbe­stimmung, 1904. Bibl.-Nr. 9, Gesamtausgabe Dornach 1961.",
      "41    Beginn des fünften nachatlantischen Zeitraumes: Siehe Hinweis zu Seite 22.",
      "44    Skythianos: Siehe auch Vortrag vom 31. August 1909 in »Der Orient im Lichte des Okzidents. Die Kinder des Luzifer und die Brüder Christi». Bibl.­Nr.113, Gesamtausgabe Dornach 1960.",
      "46    von dem ich schon einmal gesprochen habe: Vortrag vom 9. April 1912.",
      "47    Vortrag über Kalewala: Siehe Hinweis zu S.46.",
      "50    Warägerstämme: Name der schwedischen Wikinger, die über die Ostküste des Baltischen Meeres nach Rußland vordringend das osteuropäische Tiefland bis zum Schwarzen Meer unterwarfen.",
      "52    Ralph Waldo Emerson: 1803-1882, amerikanischer Schriftsteller.",
      "54    Münchner Zyklus: »Die Geheimnisse der Schwelle». Bibl.-Nr. 147, Gesamtaus­gabe Dornach 1960.",
      "55    «Mitternacht»: Siehe »Der Seelen Erwachen», Mysteriendrama von Rudolf Steiner. 6. Bild. Bibl.-Nr. 14, Gesamtausgabe 1962.",
      "die Herrschaft des Michael: Seit 1879. Siehe »Das Initiaten-Bewußtsein», Bibl.­Nr.243, Gesamtausgabe Dornach 1969.",
      "56    Theodora: Gestalt aus dem Mysteriendrama »Die Pforte der Einweihung».",
      "60    in der Schrift: »Die Schwelle der geistigen Welt», aphoristische Ausführungen, München 1913. Bibl.-Nr. 17, Gesamtausgabe Dornach 1956.",
      "66    in unseren Architraven: Siehe »Der Baugedanke des Goetheanum», Stuttgart",
      "67    die vier Vorträge: Über »Okkultes Lesen und okkultes Hören«. Bibl.-Nr. 156; Gesamtausgabe Dornach 1967.",
      "einen Vortrag angeschlossen: Dornach, 7. Oktober 1914, «Zeiten der Erwar­tung, neue Formen der alten Schönheit». Bibl.-Nr. 287, Gesamtausgabe, in Vor­bereitung.",
      "Herman Grimm, 1828-1901.",
      "76    Emerson: Siehe Hinweis zu S.52.",
      "77    Montaigne: Michel Eyquem de Montaigne, 1533-1592, Philosoph.",
      "80    Albrecht Dürer, 1471-1528.",
      "81    Herman Grimm: Vgl. »Zwei Dürersche Kupferstiche» in »Fünfzehn Essays. Dritte Folge», Berlin 1882.",
      "93    in einer vorigen Sti'nde: Vortrag vom 9. November 1914.",
      "112    im vierten nachatlantischen Zeitalter: Siehe Hinweis zu S.22.",
      "113    in einem Vortrag: Siehe Vortrag vom 14. November1914.",
      "126    BaN: Siehe Hinweis zu S.66.",
      "131    in München: Siehe Hinweis zu S.54.",
      "136    Jupiterzeit: Siehe »Die Geheimwissenschaft im Umriß», Die Weltentwickelung und der Mensch. Bibl.-Nr. 13, Gesamtausgabe Dornach 1967.",
      "143    Kant: «Kritik der praktischen Vernunft». 1. Teil, drittes Hauptstück: Von den Triebfedern der reinen praktischen Vernunft.",
      "147    Manichäismus: Siehe Vortrag vom 26. Dezember 1914. Bibl.-Nr. 156, Gesamt­ausgabe Dornach 1967.",
      "später eininal: Siehe Gesamtausgabe 1966, Bibl.-Nr. 275.",
      "149    Olaf Asteson: Über das norwegische Traumlied vom Olaf Ästeson sprach Ru­dolf Steiner am 1. Januar 1912, am 7. Januar 1913 und am 31. Dezember 1914; seine Ausführungen waren stets von der Rezitation des Traumliedes durch Marie Steiner-von Sivers begleitet. Daß diese außergewöhnliche Volksdichtung innerhalb der anthroposophischen Bewegung einen so bedeutenden Platz ein­geräumt erhielt, ist vor allem der Initiative von Ingeborg Möller-Lindholm, der norwegischen Dichterin, zu danken, welche Rudolf Steiner auf die alte Legende aufmerksam machte. Durch das Entgegenkommen von Frau Möller, für das wir ihr herzlichst danken, sind wir in der Lage, die Notizen, welche sie sich über ihre Gespräche mit Rudolf Steiner aufzeichnete, dieser Ausgabe hin­zuzufügen. Aus einem Vortrag von Ingeborg Möller über »Das Traumlied des Olaf Ästeson», den sie uns in der Übersetzung freundlicherweise zur Verfügung stellte, haben wir einige Angaben als Hinweise aufgenommen und entsprechend gekennzeichnet.",
      "Bemerkungen über das Traumlied von Ingeborg Möller, Lillehammer",
      "Im Juni des Jahres 1910 hielt Dr. Steiner in Oslo einen Vortragszyklus: »Die Mission einzelner Volksseelen in Verbindung mit der germanisch-nordischen Mythologie.» Ich lud bei dieser Gelegenheit wohl vierzig hinzugereiste anthro­posophische Freunde zum Tee ein; damals wohnte ich in Oslo und hatte ein großes Zimmer zur Verfügung. Dr. Steiner und Frau Marie Steiner hatten sich auch bereit erklärt, zu kommen. Am Tage vorher bat ich Dr. Steiner, ob er nicht uns etwas erzählen könnte über das eigentümliche norwegische Volkslied:",
      "Das Traumlied des Olaf Ästeson. Rudolf Steiner lächelte freundlich und sagte, daß er doch das Lied erst gelesen oder gehört haben müßte. Dies sah ich ein. Er schlug dann selbst vor, am nächsten Tage eine Stunde vor den anderen Gästen zu kommen, damit ich das Lied vorlesen und für ihn vorläufig übersetzen konnte. So geschah es auch.",
      "Während des Lesens saß Dr. Steiner mit geschlossenen Augen da und hörte in­tenssv zu. Er war deutlich tief ergriffen vom eigentümlichen Inhalt des Liedes. Nachdem der Tee getrunken war, wurde das Traumlied von einem Mitglied der Gesellschaft auf norwegisch vorgelesen. Darnach hielt Dr. Steiner einen er­greifenden, aber kurzen Vortrag über das Lied. Er verweilte besonders bei der Tatsache, daß die Handlungen in der Zeit der zwölf heiligen Nächte sich ab­spielen, wo die außerirdischen Einflüsse am stärksten sind. Außerdem berührte er besonders den Namen des Olaf Ästeson. Olaf oder Oleifr = der «Geblie­bene», der »Zurückgelassene», nachdem die Vorfahren nicht mehr da sind. Er ist der, der das Blut der Väter der Generationen weiterträgt. Äst bedeutet Liebe: er ist also »Der Liebe Sohn».",
      "Dr. Steiner bat mich, das Lied ins Deutsche zu übersetzen. Er konnte selbst nicht norwegisch, geschweige denn die alte, auch für moderne Norweger schwere Mundart, in der das Traumlied niedergeschrieben ist. Ich entschuldigte mich zuerst damit, daß ich die deutsche Sprache nicht so gut beherrschte, damit ich den wunderbaren, musikalischen Rhythmus mitbekommen könnte. Dr. Stei­ner sagte, das mache nichts - ich solle das Lied nur ganz nüchtern Wort für Wort übertragen, damit er einen genaueren Überblick über den Inhalt bekom­men könne. Ich tat dieses im Laufe des Herbstes und sandte ihm die sehr pro­saische und in vielen Beziehungen sehr mangelhafte Übersetzung. Nachher brachte Rudolf Steiner das Lied in eigene Rhythmen und hielt später mehrere Vorträge darüber. Es wurde dann auch für eurythmische Darstellungen ver­wendet, besonders zur Weihnachtszeit.",
      "Im Jahre 1913 sagte Dr. Steiner zu mir, daß ich nicht die Vorstellung festhal­ten sollte, daß Olaf, der Heilige, der ursprüngliche Olaf Ästeson sei. (St. Olaf, norwegischer König, fiel 1035 n. Chr. in der Schlacht bei Stiklestad als Vor­kämpfer des Christentums.) Es habe mehrere «Olaf Ästeson» gegeben, sagte Dr. Steiner. Es war dies eine Art Mysterientitel.",
      "Nach dem Ersten Weltkrieg war Dr. Steiner 1921 und 1923 wieder in Norwe­gen. Er wohnte damals bei Ingenieur Ingerö. Frau Ragnhild Ingerö, die vor einigen Jahren starb, erzählte mir, daß Dr. Steiner mit ihr über das Traum-lied gesprochen hatte. Er hatte sich inzwischen mehr damit beschäftigt und Neues herausgefunden. Unter anderem, daß das Lied viel älter sei, als gewöhn­lich angenommen wurde. Es stammt ungefähr aus dem Jahr 400 n. Chr. Da­mals lebte ein großer, christlicher Eingeweihter hier im Lande. Er begründete eine Mysterienschule in Südnorwegen; der Ort wurde nicht genannt. Sein My­sterienname war Olaf Ästeson, und das Lied schildert seine Einweihung. Ur­sprünglich, so erzählte Dr. Steiner, war das Lied viel länger und hatte zwölf Abschnitte, einen für jedes Bild im Tierkreis. Das Lied schildert Olaf Ästesons Wanderung durch den ganzen Tierkreis, was er dort sah und erlebte. Es sind nur Reste des ursprünglichen Liedes, die wir heute haben. Die erwähnte Myste­rienschule bestand bis in das frühe Mittelalter hinein. Der Leiter wurde immer Olaf Ästeson genannt.",
      "Dr. Steiner sagte, daß er mit der Zeit diese Tatsachen öffentlich bekanntmachen würde, und auch andere wichtige Dinge in Verbindung mit dem Liede. Er wollte dies aber nicht tun, bevor er bestimmte äußere Belege für seine Mittei­lungen gefunden hatte. Er meinte diese auch finden zu können. Aber der Brand des Goetheanums, übermäßige Arbeit und zuletzt Krankheit und Tod haben auch dieses Vorhaben verhindert. Jetzt besitzen wir nur diese Andeutungen.",
      "Persönliche Bemerkungen",
      "Über diese Mitteilungen von Dr. Steiner habe ich viel nachgedacht und bin zu dem Ergebnis gekommen, daß diese Mysterienschule vielleicht in »Skiringssal» zu suchen ist. Dieser Ort liegt, oder vielmehr lag in Vestfold; einer Ortschaft im südwestlichen Norwegen. Der Ort wird in den alten Sagen immer als heilig bezeichnet. Die Wikinger, die im Ausland starben, wünschten in Skiringssal be­graben zu werden. Dort war auch ein »Kaupang» (Kaufplatz). Jetzt graben die Archäologen dort etwas aus, wovon sie annehmen, daß es der Rest dieses Handelsplatzes ist. Bis jetzt hat man aber nicht sicher aufweisen können, wo Skiringssal liegt. Damals lag es an der Küste; jetzt haben Lehmablagerungen dazu geführt, daß der Ort tiefer in das Land »hineingeschoben» ist. Skiringssal bedeutet: Saal der Reinigung. Skirn bedeutet Taufe oder Reinigung (altnor­disch).",
      "Woher kam nun der erste Olaf ÄstesonP Es ist historisch erwiesen, daß irisch-schottische Mönche hier im Lande waren, lange bevor das Christentum offiziell eingeführt wurde. Den Legenden zufolge kam Joseph von Arimathia schon im ersten nachchristlichen Jahrhundert zu den britischen Inseln und begann dort seine Missionswirksamkeit. In Irland gab es schon seit Urzeiten heilige Myste­rienstätten. Ringsum auf den andern Inseln waren die Völkerstämme heid­nisch. Aus der Wirksamkeit der christlichen Missionare, zusammenfließend mit der alten Druidenweisheit, entstand die irisch-schottische Kirche, auch die Guldeerkirche genannt. Sie blühte an vielen Orten schon zwischen 300 und 400 n. Chr. Es gab Kirchen, Schulen und Klöster, trotzdem diese immer in Mit­leidenschaft gezogen wurden durch Angriffe der mächtigen heidnischen Stam­mesnachbarn. Viele Priester und Mönche erlitten den Märtyrertod. Diese Cul­deerkirche gründete sich besonders auf das Johannes-Evangelium und die Ver­kündigungen des Apostels Johannes. Sie ähnelte den ersten christlichen Ge­meinden und stand im starken Gegensatz zu der petrinischen oder römisch-katholischen Kirche. Aber die letztere siegte. Die Guldeerkirche wurde ver­nichtet und aufgelöst im Jahre 664 n. Chr. Sowohl vor als nach dieser äußeren Vernichtung sandte sie viele Missionare in verschiedene europäische Länder. Diese Kirche war ausgesprochen esoterischer Art. Vieles spricht dafür, daß der erste Olaf Ästeson ein Vertreter dieser Geistesströmung war.",
      "»Bei diesem norwegischen Volke, das noch in seiner Volkssprache vieles hat, was hart herangeht an die Grenze der okkulten Geheimnisse, war länger die Möglichkeit vorhanden, die Seelen im Zusammenhange zu lassen mit dem, was lebt und webt hinter den äußeren materiellen Erscheinungen.» (Rudolf Steiner:",
      "Aus dem Vortrag über Olaf Ästeson, Berlin, 7. Januar 1913.)",
      "151    Neu jahrs feier: Die Feier fand als Matinee statt während des Vortragszyklus »Die Welt der Sinne und die Welt des Geistes», Hannover, 27. Dezember 1911 bis 1. Januar 1912. Dornach 1933.",
      "Weihnachtsansprache: Die Ansprache hielt Rudolf Steiner am 26. Dezember 1911; sie ist in der Wochenschrift »Das Goetheanum» 1936, Nummern 51 und",
      "52 veröffentlicht worden. Rudolf Steiner führt dort aus:",
      "»So ist es richtig, diese dreizehn Nächte als die die Menschenseelen-Seherschaft repräsentierende Zeit anzusetzen, wo man wahrnimmt alles, was der Mensch durchmachen muß durch das Leben in den Inkarnationen von Adam und Eva bis zu dem Mysterium von Golgatha.",
      "Es war mir interessant, diesen Gedanken, der Ihnen nur mit etwas anderen Worten entgegenströmt aus mancherlei Vorträgen, die über das Christus-My­sterium gehalten worden sind, diesen Gedanken bei meinem letzten vorjährigen Aufenthalt in Kristiania (Oslo) schön verkörpert zu sehen in einer Sage und Legende: der sogenannten Traumlegende, die merkwürdigerweise in den letzten zehn bis fünfzehn Jahren in Norwegen aufgetaucht ist und in das Volk sich eingelebt hat, die allerdings auf frühere Zeiten zurückführt; jener Legende, die uns in ganz wunderbarer Weise schön erzählt, wie Olaf Ästeson gleichsam ein­geweiht wird durch natürliche Kräfte, indem er einschläft am Weihnachts­abend, durch die dreizehn Tage bis zum sechsten Januar schläft und durch-macht alle die Schauer dessen, was der Mensch durchleben muß durch die In­karnationen vom Erdenbeginn bis zum Mysterium von Golgatha. Und wie er, Olaf Ästeson, dann schaut, als er sich nähert der Zeit des 6. Januar, das Ein­greifen des Christus-Geistes in der Menschheit, dem der Michael-Geist voran­gegangen war. Ich hoffe, wir werden bei einer anderen Gelegenheit noch in diesen Tagen dieses Gedicht von Olaf Ästeson Ihnen vorführen können, damit Sie sehen, wie da heute noch lebt, ja geradezu wieder auflebt das Bewußtsein solcher Seherschaft in den dreizehn Tagen. Nur die eine charakteristische Strophe vom Anfang sei angeführt:",
      "So höre meinen Sang!",
      "Ich will dir singen",
      "Von einem flinken Jüngling:",
      "Es war das Olaf Ästeson,",
      "Der einst so lange schlief.",
      "Von ihm will ich dir singen.",
      "Er ging zur Ruh' am Weihnachtsabend,",
      "Ein starker Schlaf umfing ihn bald,",
      "Und nicht konnt' er erwachen,",
      "Bevor am dreizehnten Tag",
      "Das Volk zur Kirche ging.",
      "Es war das Olaf Ästeson,",
      "Der einst so lange schlief!",
      "Von ihm will ich dir singen.",
      "Und das geht dann weiter: wie er geführt wird in seinem Traum der dreizehn Nächte durch all das, was der Mensch in der heute geschilderten Weise zu durchleben hat infolge der Versuchung des Luzifer. Anschaulich wird geschil­dert, wie Olaf Ästeson durch alle die Gefilde geht, wo die Menschen das er­leben, was wir ja so oft schilderten bei unseren Erzählungen von Kamaloka; wie hereinströmt in dieses geschaute Kamaloka der Christus-Geist, geführt von Michael. So wird sich für die Menschen immer mehr und mehr mit dem, was wir den im Geist kommenden Christus nennen, eröffnen die Möglichkeit, wirk­lich auch zu erkennen, wie die geistigen Kräfte walten und weben, wie das, was wir Feste nennen, nicht willkürlich festgesetzt worden ist, sondern fest­gesetzt worden ist durch die den Menschen so oft unbewußte, aber durch die Geschichte waltende Weltenweisheit.»",
      "152  zu einem Vortragszyklus: Siehe die Bemerkungen von Ingeborg Möller.",
      "153    Der Prediger Landstad: M. B. Landstad, bekannter norwegischer Psalmendich­ter und Herausgeber von Psalmenbüchern. Er war Pfarrer in Telemark, damals ein verstecktes Tal, wo alte Gewohnheiten und Bräuche, alte Trachten und Sprache sich durch die Zeiten ziemlich unverändert erhalten hatten. Landstad war stark von Grundtvig (dänischer Dichter und Volkserzieher: 1783-1872) beeinflußt und hatte wie die meisten Anhänger Grundtvigs viel Verständnis für Geschichte und Volkskunst. Er reiste daher im Lande herum und schrieb alte Sagen und Volksweisen nieder. Diese ließ er sich erzählen und vorsingen von alten Menschen. Auf seinen Reisen wurde Landstad oft begleitet von Olea Kröger, einer Pfarrerstochter, die sehr musikalisch war. Darüber hinaus hatte sie Fähigkeiten, ja ganz ungewöhnliche Fähigkeiten, sich in die alten Weisen und Lieder einzuleben und diese oft schwierigen Dinge - alte Tonarten - dann niederzuschreiben. Olea Kröger war geboren und aufgewachsen in Telemark und kannte Sprache und Bräuche des Landes besser als die meisten anderen. Das, was sie durch eigene Sammelarbeit sich erwarb, übergab sie bescheiden an Landstad oder an andere »Gelehrte». Ihre Arbeit ist wenig bekannt außer­halb eines engen Forscherkreises, aber ihr Einsatz kann nicht hoch genug ge­wertet werden. (I. M.)",
      "153/54 an eine musikalische Stimmung: Siehe die voranstehenden Bemerkungen",
      "154    in dieser zunächst provisorischen Einrichtung: In dieser Form wird das Traum-lied hier abgedruckt; die Fassung wird auch bei der eurythmischen Darstel­lung des Traumliedes gebraucht; ein endgültiger Text wurde von Rudolf Stei­ner nicht mehr gegeben.",
      "155    Das Traumlied: «Draumkvaedet»: Siehe die Sammlung »Norske Folkeviser», her­ausgegeben von Thorwald Lammers, Kristiania 1910, bei H. Aschehoug & Co.",
      "158    Gjallarbrücke: Diese Brücke wölbt sich über den mystischen Fluß Gjöll, der die Reiche trennt in der geistigen Welt. (I. M.)",
      "Es schlug mich die Geisterschlange: Olaf erzählt weiter, wie er über den Tier­kreis (Zodiakus) fuhr. Gerade hier ist es deutlich, daß ein großer Teil des Lie­des fehlt, wie es auch Landstad in seinen Kommentaren berichtet. Von den Sternbildern wird nur der «Hund» (Canis major) erwähnt. Dieses Sternbild liegt aber außerhalb des Tierkreises. Gleichfalls die «Schlange» (Serpens). Aber der «Stier» (Tau rus) im Tierkreis ist ihm ein wichtiges Bild. - Nachdem der Tier­kreis durchlaufen ist, bekommt Olaf die Eingebung, einen anderen Weg ein­zuschlagen; er begibt sich auf die Milchstraße (vintergaten). Es ist eine alte Vorstellung, daß die Milchstraße in das Reich der Seligen, in das Paradies führt. (I. M.)",
      "160    Brooksvalin: »Brooksvalin» ist ein altes, eigentümliches Wort, das Landstad mit »Der Bedrängnis Vorhof» übersetzt. Aus dem Liede geht hervor, daß Olaf jetzt wieder in den Tierkreis zurückkehrt und in das Zeichen der Waage kommt. (I. M.)",
      "161    Vom Höllen fürsten geleitet: Grutte Graubart - Ahriman. (I. M.)",
      "162    Dem Welt gerichte unterstehen: Nach der neunten Strophe folgen noch drei Strophen im Manuskript Rudolf Steiners, die aber weder gedruckt noch euryth­misiert wurden.",
      "Was aus dem Süden kam,",
      "Das schien nur lautre Güte.",
      "Es ritt voran Sankt Michael",
      "An Jesu Christi Seite",
      "Auf einem weißen Pferde",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Sie ritten aus dem Süden,",
      "Gar zahlreich war da ihr Gefolge.",
      "Es ritt voran Sankt Michael.",
      "Er hielt die Posaune",
      "Mit seiner Hand",
      "In Brooksvalin, wo Seelen",
      "Dem Weitgerichte unterstehen.",
      "Das war der heil'ge Michael,",
      "Der blies in die Posaune.",
      "So wurden die Geister nun gerufen",
      "In Brooksvalin, wo Seelen",
      "Dem Weltgerichte unterstehen.",
      "Und wog die Menschenseelen: Überall, wo das Christentum sich ausgebreitet hatte, gab es Bilder von Michael, der eine Waage in der einen Hand hält. In der anderen hat er oft eine Lanze oder ein Schwert, womit er den Drachen durchbohrt. So wird er auf unzähligen Kirchenmalereien und Skulpturen dar­gestellt, zum Beispiel auf dem Nordportal der Domkirche in Drontheim. -Hiermit ist im Grunde der epische Teil des Liedes zu Ende. Es folgen noch einige Verse; Olaf ermahnt seine Mitmenschen im Sinne des Wortes der Hei-ligen Schrift: «Sie sollen von ihrer Arbeit ruhen, aber ihre Taten folgen ihnen.» Landstad erzählt, er hätte gehört, daß das Lied früher bei der Leichenwache verwendet wurde für den Verstorbenen. Das Lied sollte der Seele eine Hilfe sein für ihren ersten Weg in der anderen Welt. (I. M.)",
      "167 bei meinem vorletzten Besuch: Siehe die Bemerkungen von Ingeborg Möller.",
      "176    aus dem 2. Mosesbuche, 33. Kapitel, Vers 18: In der von Rudolf Steiner ange­gebenen Übersetzung durch Dr. Hugo Bergmann heißt es wörtlich: »Und Mose sprach zu Gott: Zeige mir doch deine Herrlichkeit! Und dieser sprach: Ich werde vorüberziehen lassen all meine Güte an deinem Angesicht und will rufen den Namen Jahves vor dir und will gnädig sein dem, den ich begnade, und mich erbarmen des, dessen ich mich erbarme. Dann aber sprach er: Du kannst mein Antlitz nicht sehen, denn mich sieht kein Mensch, der dann leben bliebe. Und es sprach Jahve: Hier ist ein Ort bei mir, stelle dich auf den Fel­sen. Und wenn meine Herrlichkeit vorüberzieht, so will ich dich in eine Höh­lung des Felsens stellen und meine Hand über dich decken, bis ich vorüber bin. Wenn ich dann meine Hand entferne, so wirst du meine Rückseite sehen; aber mein Antlitz kann nicht geschaut werden.»",
      "Hugo Bergmann: geb. 1883. Philosoph, lehrt heute an der Universität in Je­rusalem.",
      "177    »Die Schwelle der geistigen Welt»: Siehe Hinweis zu S.60.",
      "184    »Die geistige Führung des Menschen und der Menschheit»: Geisteswissenschaft­liche Ergebnisse über die Menschheitsentwickelung. München 1911. Bibl.-Nr. 15, Gesamtausgabe Dornach 1963.",
      "194    Helena Petrowna Blavatsky: 1831-1891, begründete 1875 die Theosophische Gesellschaft.",
      "199    Was die Weisheit ist: I. Kor., 3, 19.",
      "214    Lasset die Toten: Matth. 8,22.",
      "216    Woodrow Wslson: l856-l924, Präsident der USA, 1912-1920."
    ],
    "sentences": [
      [
        "Der Zusammenhang des Menschen mit der elementarischen Welt"
      ],
      [
        "Einige Bemerkungen zu dieser Buchausgabe.",
        "Das Thema des einführenden öffentlichen Vortrages «Das Wesen der nationalen Epen mit speziellem Hinweis auf Kale­wala», der im Frühjahr 1912 in Helsingfors gehalten wurde, nahm Rudolf Steiner zwei Jahre später ins Winter 1914 in Dornach wieder auf.",
        "Jetzt hieß das Thema »Der Zusammenhang des Menschen mit der elementarischen Welt.",
        "Finnland und Kale­wala» und wurde an drei Abenden dargestellt.",
        "Am Ende des Jahres sprach Rudolf Steiner auch in Dornach über «Das Traumlied des Olaf Ästeson», nun auf diese norwegische epische Dichtung hinweisend.",
        "So war es gegeben, diesen Vortrag und die beiden 1912 und 1913 vorangegangenen Betrachtungen über das gleiche Thema in diesen Band aufzunehmen.",
        "An die drei Vorträge über Kalewala schlossen sich dann die Ausführungen über «Die Welt als Ergebnis von Gleichgewichtswirkungen» an. -In mahnenden Worten macht Rudolf Steiner - man fasse den Zeitpunkt, in welchem diese Vorträge stattfanden, ins Auge - darauf aufmerksam, »daß die Fortentwicke­lung der Menschheit davon abhängt, daß wirklich die geistigen Wahrheiten durch­dringen werden, daß wirklich die Menschen hinter die Sinneswelt sehen lernen».",
        "Inhalt und Charakter dieser Vorträge schienen daher auch geeignet zu sein, zwei Ansprachen mit diesen Darstellungen zu vereinigen, welche bisher noch nicht ver­öffentlicht wurden.",
        "Es handelt sich um die beiden in Helsingfors 1912 und 1913 gehaltenen Vorträge für russische Zuhörer, welche damals zu den in Helsingfors stattgefundenen Vortragszyklen aus Rußland hergereist kamen.",
        "Die Nachsehriften durften auf Rudolf Steiners ausdrückliche Anweisung nur in Ausnahmefällen nach­gelesen werden, und dieses wurde auch seitdem beibehalten.",
        "Die geistigen Wahrheiten, welche Rudolf Steiner damals einem nur kleinen Kreise anvertraute, müssen aber heute ins allgemeine Bewußtsein aufgenommen werden.",
        "So wurde der Entschluß zur Veröffentlichung gefaßt.",
        "Die vorangehenden Ausführungen erhellen genügend die Tiefen und Zusammenhänge der verschiedenen Volkstümer, um die Wahrheiten über das russische Volkstum so aufzunehmen, wie es von Rudolf Steiner zum Ausdruck gebracht wurde."
      ],
      [
        "11 Theosophische Gesellscha ft: Später Anthroposophische Gesellschaft."
      ],
      [
        "eine Reihe von Vorträgen: «Die geistigen Wesenheiten in den Himmelskör­pern und Naturreichen», Bibl.-Nr. 136, Gesamtausgabe 1960."
      ],
      [
        "zwei öffentliche Vorträge: Der zweite öffentliche Vortrag vom 12.",
        "April 1912 ist ebenfalls veröffentlicht in Bibl.-Nr. 136."
      ],
      [
        "12 Herman Grimm: Ilias, zweite Auflage in einem Bande, Stuttgart-Berlin 1907.",
        "Rudolf Steiner führt in seinen Notizen zu diesem Vortrag für die Ilias-Betrach­tung folgende Seiten an: 298, 307, 327 oben, 330: Vielseitigkeit, Tötung des Patroklus; 360: Thetis' Doppeldasein; 395: Nibelungen; 417."
      ],
      [
        "22 denkende Naturforscher: Beispielsweise Robert Wiedersheim, 1848-1923, Ana­tom."
      ],
      [
        "in dem 6., 7. vorchristlichen lahrhundert: Siehe »Die Geheimwissenschaft im Umriß», Bibl.-Nr. 13, Gesamtausgabe Dornach 1968.",
        "Die Weltentwickelung und der Mensch.",
        "Erste, urindische, zweite, urpersische nachatlantische Kulturepoche;"
      ],
      [
        "dritte ägyptisch-chaldäische Kulturepoche; vierte, griechisch-lateini­sehe Kulturepoche; fünfte nachatlantische Kulturepoche: 1413-3573.",
        "Ein Kul­turzeitalter umfaßt 2160 Jahre.",
        "Viertes Zeitalter: 747 v.",
        "Chr. bis 1413 n.",
        "Chr."
      ],
      [
        "38 wie ein Motto: Vergl.",
        "Kalewala, 40.",
        "Rune, und Eingangsstrophe «Kanteletar» von Elias Lönnrot, 1802-1884."
      ],
      [
        "40 «Theosophie»: Einführung in übersinnliche Welterkenntnis und Menschenbe­stimmung, 1904.",
        "Bibl.-Nr. 9, Gesamtausgabe Dornach 1961."
      ],
      [
        "41 Beginn des fünften nachatlantischen Zeitraumes: Siehe Hinweis zu Seite 22."
      ],
      [
        "44 Skythianos: Siehe auch Vortrag vom 31.",
        "August 1909 in »Der Orient im Lichte des Okzidents.",
        "Die Kinder des Luzifer und die Brüder Christi».",
        "Bibl.­Nr.113, Gesamtausgabe Dornach 1960."
      ],
      [
        "46 von dem ich schon einmal gesprochen habe: Vortrag vom 9.",
        "April 1912."
      ],
      [
        "47 Vortrag über Kalewala: Siehe Hinweis zu S.46."
      ],
      [
        "50 Warägerstämme: Name der schwedischen Wikinger, die über die Ostküste des Baltischen Meeres nach Rußland vordringend das osteuropäische Tiefland bis zum Schwarzen Meer unterwarfen."
      ],
      [
        "52 Ralph Waldo Emerson: 1803-1882, amerikanischer Schriftsteller."
      ],
      [
        "54 Münchner Zyklus: »Die Geheimnisse der Schwelle».",
        "Bibl.-Nr. 147, Gesamtaus­gabe Dornach 1960."
      ],
      [
        "55 «Mitternacht»: Siehe »Der Seelen Erwachen», Mysteriendrama von Rudolf Steiner. 6.",
        "Bild.",
        "Bibl.-Nr. 14, Gesamtausgabe 1962."
      ],
      [
        "die Herrschaft des Michael: Seit 1879.",
        "Siehe »Das Initiaten-Bewußtsein», Bibl.­Nr.243, Gesamtausgabe Dornach 1969."
      ],
      [
        "56 Theodora: Gestalt aus dem Mysteriendrama »Die Pforte der Einweihung»."
      ],
      [
        "60 in der Schrift: »Die Schwelle der geistigen Welt», aphoristische Ausführungen, München 1913.",
        "Bibl.-Nr. 17, Gesamtausgabe Dornach 1956."
      ],
      [
        "66 in unseren Architraven: Siehe »Der Baugedanke des Goetheanum», Stuttgart"
      ],
      [
        "67 die vier Vorträge: Über »Okkultes Lesen und okkultes Hören«.",
        "Bibl.-Nr. 156; Gesamtausgabe Dornach 1967."
      ],
      [
        "einen Vortrag angeschlossen: Dornach, 7.",
        "Oktober 1914, «Zeiten der Erwar­tung, neue Formen der alten Schönheit».",
        "Bibl.-Nr. 287, Gesamtausgabe, in Vor­bereitung."
      ],
      [
        "Herman Grimm, 1828-1901."
      ],
      [
        "76 Emerson: Siehe Hinweis zu S.52."
      ],
      [
        "77 Montaigne: Michel Eyquem de Montaigne, 1533-1592, Philosoph."
      ],
      [
        "80 Albrecht Dürer, 1471-1528."
      ],
      [
        "81 Herman Grimm: Vgl. »Zwei Dürersche Kupferstiche» in »Fünfzehn Essays.",
        "Dritte Folge», Berlin 1882."
      ],
      [
        "93 in einer vorigen Sti'nde: Vortrag vom 9.",
        "November 1914."
      ],
      [
        "112 im vierten nachatlantischen Zeitalter: Siehe Hinweis zu S.22."
      ],
      [
        "113 in einem Vortrag: Siehe Vortrag vom 14.",
        "November1914."
      ],
      [
        "126 BaN: Siehe Hinweis zu S.66."
      ],
      [
        "131 in München: Siehe Hinweis zu S.54."
      ],
      [
        "136 Jupiterzeit: Siehe »Die Geheimwissenschaft im Umriß», Die Weltentwickelung und der Mensch.",
        "Bibl.-Nr. 13, Gesamtausgabe Dornach 1967."
      ],
      [
        "143 Kant: «Kritik der praktischen Vernunft». 1.",
        "Teil, drittes Hauptstück: Von den Triebfedern der reinen praktischen Vernunft."
      ],
      [
        "147 Manichäismus: Siehe Vortrag vom 26.",
        "Dezember 1914.",
        "Bibl.-Nr. 156, Gesamt­ausgabe Dornach 1967."
      ],
      [
        "später eininal: Siehe Gesamtausgabe 1966, Bibl.-Nr. 275."
      ],
      [
        "149 Olaf Asteson: Über das norwegische Traumlied vom Olaf Ästeson sprach Ru­dolf Steiner am 1.",
        "Januar 1912, am 7.",
        "Januar 1913 und am 31.",
        "Dezember 1914; seine Ausführungen waren stets von der Rezitation des Traumliedes durch Marie Steiner-von Sivers begleitet.",
        "Daß diese außergewöhnliche Volksdichtung innerhalb der anthroposophischen Bewegung einen so bedeutenden Platz ein­geräumt erhielt, ist vor allem der Initiative von Ingeborg Möller-Lindholm, der norwegischen Dichterin, zu danken, welche Rudolf Steiner auf die alte Legende aufmerksam machte.",
        "Durch das Entgegenkommen von Frau Möller, für das wir ihr herzlichst danken, sind wir in der Lage, die Notizen, welche sie sich über ihre Gespräche mit Rudolf Steiner aufzeichnete, dieser Ausgabe hin­zuzufügen.",
        "Aus einem Vortrag von Ingeborg Möller über »Das Traumlied des Olaf Ästeson», den sie uns in der Übersetzung freundlicherweise zur Verfügung stellte, haben wir einige Angaben als Hinweise aufgenommen und entsprechend gekennzeichnet."
      ],
      [
        "Bemerkungen über das Traumlied von Ingeborg Möller, Lillehammer"
      ],
      [
        "Im Juni des Jahres 1910 hielt Dr.",
        "Steiner in Oslo einen Vortragszyklus: »Die Mission einzelner Volksseelen in Verbindung mit der germanisch-nordischen Mythologie.» Ich lud bei dieser Gelegenheit wohl vierzig hinzugereiste anthro­posophische Freunde zum Tee ein; damals wohnte ich in Oslo und hatte ein großes Zimmer zur Verfügung.",
        "Steiner und Frau Marie Steiner hatten sich auch bereit erklärt, zu kommen.",
        "Am Tage vorher bat ich Dr.",
        "Steiner, ob er nicht uns etwas erzählen könnte über das eigentümliche norwegische Volkslied:"
      ],
      [
        "Das Traumlied des Olaf Ästeson.",
        "Rudolf Steiner lächelte freundlich und sagte, daß er doch das Lied erst gelesen oder gehört haben müßte.",
        "Dies sah ich ein.",
        "Er schlug dann selbst vor, am nächsten Tage eine Stunde vor den anderen Gästen zu kommen, damit ich das Lied vorlesen und für ihn vorläufig übersetzen konnte.",
        "So geschah es auch."
      ],
      [
        "Während des Lesens saß Dr.",
        "Steiner mit geschlossenen Augen da und hörte in­tenssv zu.",
        "Er war deutlich tief ergriffen vom eigentümlichen Inhalt des Liedes.",
        "Nachdem der Tee getrunken war, wurde das Traumlied von einem Mitglied der Gesellschaft auf norwegisch vorgelesen.",
        "Darnach hielt Dr.",
        "Steiner einen er­greifenden, aber kurzen Vortrag über das Lied.",
        "Er verweilte besonders bei der Tatsache, daß die Handlungen in der Zeit der zwölf heiligen Nächte sich ab­spielen, wo die außerirdischen Einflüsse am stärksten sind.",
        "Außerdem berührte er besonders den Namen des Olaf Ästeson.",
        "Olaf oder Oleifr = der «Geblie­bene», der »Zurückgelassene», nachdem die Vorfahren nicht mehr da sind.",
        "Er ist der, der das Blut der Väter der Generationen weiterträgt.",
        "Äst bedeutet Liebe: er ist also »Der Liebe Sohn»."
      ],
      [
        "Steiner bat mich, das Lied ins Deutsche zu übersetzen.",
        "Er konnte selbst nicht norwegisch, geschweige denn die alte, auch für moderne Norweger schwere Mundart, in der das Traumlied niedergeschrieben ist.",
        "Ich entschuldigte mich zuerst damit, daß ich die deutsche Sprache nicht so gut beherrschte, damit ich den wunderbaren, musikalischen Rhythmus mitbekommen könnte.",
        "Stei­ner sagte, das mache nichts - ich solle das Lied nur ganz nüchtern Wort für Wort übertragen, damit er einen genaueren Überblick über den Inhalt bekom­men könne.",
        "Ich tat dieses im Laufe des Herbstes und sandte ihm die sehr pro­saische und in vielen Beziehungen sehr mangelhafte Übersetzung.",
        "Nachher brachte Rudolf Steiner das Lied in eigene Rhythmen und hielt später mehrere Vorträge darüber.",
        "Es wurde dann auch für eurythmische Darstellungen ver­wendet, besonders zur Weihnachtszeit."
      ],
      [
        "Im Jahre 1913 sagte Dr.",
        "Steiner zu mir, daß ich nicht die Vorstellung festhal­ten sollte, daß Olaf, der Heilige, der ursprüngliche Olaf Ästeson sei. (St.",
        "Olaf, norwegischer König, fiel 1035 n.",
        "Chr. in der Schlacht bei Stiklestad als Vor­kämpfer des Christentums.) Es habe mehrere «Olaf Ästeson» gegeben, sagte Dr.",
        "Steiner.",
        "Es war dies eine Art Mysterientitel."
      ],
      [
        "Nach dem Ersten Weltkrieg war Dr.",
        "Steiner 1921 und 1923 wieder in Norwe­gen.",
        "Er wohnte damals bei Ingenieur Ingerö.",
        "Frau Ragnhild Ingerö, die vor einigen Jahren starb, erzählte mir, daß Dr.",
        "Steiner mit ihr über das Traum-lied gesprochen hatte.",
        "Er hatte sich inzwischen mehr damit beschäftigt und Neues herausgefunden.",
        "Unter anderem, daß das Lied viel älter sei, als gewöhn­lich angenommen wurde.",
        "Es stammt ungefähr aus dem Jahr 400 n.",
        "Chr.",
        "Da­mals lebte ein großer, christlicher Eingeweihter hier im Lande.",
        "Er begründete eine Mysterienschule in Südnorwegen; der Ort wurde nicht genannt.",
        "Sein My­sterienname war Olaf Ästeson, und das Lied schildert seine Einweihung.",
        "Ur­sprünglich, so erzählte Dr.",
        "Steiner, war das Lied viel länger und hatte zwölf Abschnitte, einen für jedes Bild im Tierkreis.",
        "Das Lied schildert Olaf Ästesons Wanderung durch den ganzen Tierkreis, was er dort sah und erlebte.",
        "Es sind nur Reste des ursprünglichen Liedes, die wir heute haben.",
        "Die erwähnte Myste­rienschule bestand bis in das frühe Mittelalter hinein.",
        "Der Leiter wurde immer Olaf Ästeson genannt."
      ],
      [
        "Steiner sagte, daß er mit der Zeit diese Tatsachen öffentlich bekanntmachen würde, und auch andere wichtige Dinge in Verbindung mit dem Liede.",
        "Er wollte dies aber nicht tun, bevor er bestimmte äußere Belege für seine Mittei­lungen gefunden hatte.",
        "Er meinte diese auch finden zu können.",
        "Aber der Brand des Goetheanums, übermäßige Arbeit und zuletzt Krankheit und Tod haben auch dieses Vorhaben verhindert.",
        "Jetzt besitzen wir nur diese Andeutungen."
      ],
      [
        "Persönliche Bemerkungen"
      ],
      [
        "Über diese Mitteilungen von Dr.",
        "Steiner habe ich viel nachgedacht und bin zu dem Ergebnis gekommen, daß diese Mysterienschule vielleicht in »Skiringssal» zu suchen ist.",
        "Dieser Ort liegt, oder vielmehr lag in Vestfold; einer Ortschaft im südwestlichen Norwegen.",
        "Der Ort wird in den alten Sagen immer als heilig bezeichnet.",
        "Die Wikinger, die im Ausland starben, wünschten in Skiringssal be­graben zu werden.",
        "Dort war auch ein »Kaupang» (Kaufplatz).",
        "Jetzt graben die Archäologen dort etwas aus, wovon sie annehmen, daß es der Rest dieses Handelsplatzes ist.",
        "Bis jetzt hat man aber nicht sicher aufweisen können, wo Skiringssal liegt.",
        "Damals lag es an der Küste; jetzt haben Lehmablagerungen dazu geführt, daß der Ort tiefer in das Land »hineingeschoben» ist.",
        "Skiringssal bedeutet: Saal der Reinigung.",
        "Skirn bedeutet Taufe oder Reinigung (altnor­disch)."
      ],
      [
        "Woher kam nun der erste Olaf ÄstesonP Es ist historisch erwiesen, daß irisch-schottische Mönche hier im Lande waren, lange bevor das Christentum offiziell eingeführt wurde.",
        "Den Legenden zufolge kam Joseph von Arimathia schon im ersten nachchristlichen Jahrhundert zu den britischen Inseln und begann dort seine Missionswirksamkeit.",
        "In Irland gab es schon seit Urzeiten heilige Myste­rienstätten.",
        "Ringsum auf den andern Inseln waren die Völkerstämme heid­nisch.",
        "Aus der Wirksamkeit der christlichen Missionare, zusammenfließend mit der alten Druidenweisheit, entstand die irisch-schottische Kirche, auch die Guldeerkirche genannt.",
        "Sie blühte an vielen Orten schon zwischen 300 und 400 n.",
        "Chr.",
        "Es gab Kirchen, Schulen und Klöster, trotzdem diese immer in Mit­leidenschaft gezogen wurden durch Angriffe der mächtigen heidnischen Stam­mesnachbarn.",
        "Viele Priester und Mönche erlitten den Märtyrertod.",
        "Diese Cul­deerkirche gründete sich besonders auf das Johannes-Evangelium und die Ver­kündigungen des Apostels Johannes.",
        "Sie ähnelte den ersten christlichen Ge­meinden und stand im starken Gegensatz zu der petrinischen oder römisch-katholischen Kirche.",
        "Aber die letztere siegte.",
        "Die Guldeerkirche wurde ver­nichtet und aufgelöst im Jahre 664 n.",
        "Chr.",
        "Sowohl vor als nach dieser äußeren Vernichtung sandte sie viele Missionare in verschiedene europäische Länder.",
        "Diese Kirche war ausgesprochen esoterischer Art.",
        "Vieles spricht dafür, daß der erste Olaf Ästeson ein Vertreter dieser Geistesströmung war."
      ],
      [
        "»Bei diesem norwegischen Volke, das noch in seiner Volkssprache vieles hat, was hart herangeht an die Grenze der okkulten Geheimnisse, war länger die Möglichkeit vorhanden, die Seelen im Zusammenhange zu lassen mit dem, was lebt und webt hinter den äußeren materiellen Erscheinungen.» (Rudolf Steiner:"
      ],
      [
        "Aus dem Vortrag über Olaf Ästeson, Berlin, 7.",
        "Januar 1913.)"
      ],
      [
        "151 Neu jahrs feier: Die Feier fand als Matinee statt während des Vortragszyklus »Die Welt der Sinne und die Welt des Geistes», Hannover, 27.",
        "Dezember 1911 bis 1.",
        "Januar 1912.",
        "Dornach 1933."
      ],
      [
        "Weihnachtsansprache: Die Ansprache hielt Rudolf Steiner am 26.",
        "Dezember 1911; sie ist in der Wochenschrift »Das Goetheanum» 1936, Nummern 51 und"
      ],
      [
        "52 veröffentlicht worden.",
        "Rudolf Steiner führt dort aus:"
      ],
      [
        "»So ist es richtig, diese dreizehn Nächte als die die Menschenseelen-Seherschaft repräsentierende Zeit anzusetzen, wo man wahrnimmt alles, was der Mensch durchmachen muß durch das Leben in den Inkarnationen von Adam und Eva bis zu dem Mysterium von Golgatha."
      ],
      [
        "Es war mir interessant, diesen Gedanken, der Ihnen nur mit etwas anderen Worten entgegenströmt aus mancherlei Vorträgen, die über das Christus-My­sterium gehalten worden sind, diesen Gedanken bei meinem letzten vorjährigen Aufenthalt in Kristiania (Oslo) schön verkörpert zu sehen in einer Sage und Legende: der sogenannten Traumlegende, die merkwürdigerweise in den letzten zehn bis fünfzehn Jahren in Norwegen aufgetaucht ist und in das Volk sich eingelebt hat, die allerdings auf frühere Zeiten zurückführt; jener Legende, die uns in ganz wunderbarer Weise schön erzählt, wie Olaf Ästeson gleichsam ein­geweiht wird durch natürliche Kräfte, indem er einschläft am Weihnachts­abend, durch die dreizehn Tage bis zum sechsten Januar schläft und durch-macht alle die Schauer dessen, was der Mensch durchleben muß durch die In­karnationen vom Erdenbeginn bis zum Mysterium von Golgatha.",
        "Und wie er, Olaf Ästeson, dann schaut, als er sich nähert der Zeit des 6.",
        "Januar, das Ein­greifen des Christus-Geistes in der Menschheit, dem der Michael-Geist voran­gegangen war.",
        "Ich hoffe, wir werden bei einer anderen Gelegenheit noch in diesen Tagen dieses Gedicht von Olaf Ästeson Ihnen vorführen können, damit Sie sehen, wie da heute noch lebt, ja geradezu wieder auflebt das Bewußtsein solcher Seherschaft in den dreizehn Tagen.",
        "Nur die eine charakteristische Strophe vom Anfang sei angeführt:"
      ],
      [
        "So höre meinen Sang!"
      ],
      [
        "Ich will dir singen"
      ],
      [
        "Von einem flinken Jüngling:"
      ],
      [
        "Es war das Olaf Ästeson,"
      ],
      [
        "Der einst so lange schlief."
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Er ging zur Ruh' am Weihnachtsabend,"
      ],
      [
        "Ein starker Schlaf umfing ihn bald,"
      ],
      [
        "Und nicht konnt' er erwachen,"
      ],
      [
        "Bevor am dreizehnten Tag"
      ],
      [
        "Das Volk zur Kirche ging."
      ],
      [
        "Es war das Olaf Ästeson,"
      ],
      [
        "Der einst so lange schlief!"
      ],
      [
        "Von ihm will ich dir singen."
      ],
      [
        "Und das geht dann weiter: wie er geführt wird in seinem Traum der dreizehn Nächte durch all das, was der Mensch in der heute geschilderten Weise zu durchleben hat infolge der Versuchung des Luzifer.",
        "Anschaulich wird geschil­dert, wie Olaf Ästeson durch alle die Gefilde geht, wo die Menschen das er­leben, was wir ja so oft schilderten bei unseren Erzählungen von Kamaloka; wie hereinströmt in dieses geschaute Kamaloka der Christus-Geist, geführt von Michael.",
        "So wird sich für die Menschen immer mehr und mehr mit dem, was wir den im Geist kommenden Christus nennen, eröffnen die Möglichkeit, wirk­lich auch zu erkennen, wie die geistigen Kräfte walten und weben, wie das, was wir Feste nennen, nicht willkürlich festgesetzt worden ist, sondern fest­gesetzt worden ist durch die den Menschen so oft unbewußte, aber durch die Geschichte waltende Weltenweisheit.»"
      ],
      [
        "152 zu einem Vortragszyklus: Siehe die Bemerkungen von Ingeborg Möller."
      ],
      [
        "153 Der Prediger Landstad: M.",
        "Landstad, bekannter norwegischer Psalmendich­ter und Herausgeber von Psalmenbüchern.",
        "Er war Pfarrer in Telemark, damals ein verstecktes Tal, wo alte Gewohnheiten und Bräuche, alte Trachten und Sprache sich durch die Zeiten ziemlich unverändert erhalten hatten.",
        "Landstad war stark von Grundtvig (dänischer Dichter und Volkserzieher: 1783-1872) beeinflußt und hatte wie die meisten Anhänger Grundtvigs viel Verständnis für Geschichte und Volkskunst.",
        "Er reiste daher im Lande herum und schrieb alte Sagen und Volksweisen nieder.",
        "Diese ließ er sich erzählen und vorsingen von alten Menschen.",
        "Auf seinen Reisen wurde Landstad oft begleitet von Olea Kröger, einer Pfarrerstochter, die sehr musikalisch war.",
        "Darüber hinaus hatte sie Fähigkeiten, ja ganz ungewöhnliche Fähigkeiten, sich in die alten Weisen und Lieder einzuleben und diese oft schwierigen Dinge - alte Tonarten - dann niederzuschreiben.",
        "Olea Kröger war geboren und aufgewachsen in Telemark und kannte Sprache und Bräuche des Landes besser als die meisten anderen.",
        "Das, was sie durch eigene Sammelarbeit sich erwarb, übergab sie bescheiden an Landstad oder an andere »Gelehrte».",
        "Ihre Arbeit ist wenig bekannt außer­halb eines engen Forscherkreises, aber ihr Einsatz kann nicht hoch genug ge­wertet werden. (I."
      ],
      [
        "153/54 an eine musikalische Stimmung: Siehe die voranstehenden Bemerkungen"
      ],
      [
        "154 in dieser zunächst provisorischen Einrichtung: In dieser Form wird das Traum-lied hier abgedruckt; die Fassung wird auch bei der eurythmischen Darstel­lung des Traumliedes gebraucht; ein endgültiger Text wurde von Rudolf Stei­ner nicht mehr gegeben."
      ],
      [
        "155 Das Traumlied: «Draumkvaedet»: Siehe die Sammlung »Norske Folkeviser», her­ausgegeben von Thorwald Lammers, Kristiania 1910, bei H.",
        "Aschehoug & Co."
      ],
      [
        "158 Gjallarbrücke: Diese Brücke wölbt sich über den mystischen Fluß Gjöll, der die Reiche trennt in der geistigen Welt. (I."
      ],
      [
        "Es schlug mich die Geisterschlange: Olaf erzählt weiter, wie er über den Tier­kreis (Zodiakus) fuhr.",
        "Gerade hier ist es deutlich, daß ein großer Teil des Lie­des fehlt, wie es auch Landstad in seinen Kommentaren berichtet.",
        "Von den Sternbildern wird nur der «Hund» (Canis major) erwähnt.",
        "Dieses Sternbild liegt aber außerhalb des Tierkreises.",
        "Gleichfalls die «Schlange» (Serpens).",
        "Aber der «Stier» (Tau rus) im Tierkreis ist ihm ein wichtiges Bild. - Nachdem der Tier­kreis durchlaufen ist, bekommt Olaf die Eingebung, einen anderen Weg ein­zuschlagen; er begibt sich auf die Milchstraße (vintergaten).",
        "Es ist eine alte Vorstellung, daß die Milchstraße in das Reich der Seligen, in das Paradies führt. (I."
      ],
      [
        "160 Brooksvalin: »Brooksvalin» ist ein altes, eigentümliches Wort, das Landstad mit »Der Bedrängnis Vorhof» übersetzt.",
        "Aus dem Liede geht hervor, daß Olaf jetzt wieder in den Tierkreis zurückkehrt und in das Zeichen der Waage kommt. (I."
      ],
      [
        "161 Vom Höllen fürsten geleitet: Grutte Graubart - Ahriman. (I."
      ],
      [
        "162 Dem Welt gerichte unterstehen: Nach der neunten Strophe folgen noch drei Strophen im Manuskript Rudolf Steiners, die aber weder gedruckt noch euryth­misiert wurden."
      ],
      [
        "Was aus dem Süden kam,"
      ],
      [
        "Das schien nur lautre Güte."
      ],
      [
        "Es ritt voran Sankt Michael"
      ],
      [
        "An Jesu Christi Seite"
      ],
      [
        "Auf einem weißen Pferde"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Sie ritten aus dem Süden,"
      ],
      [
        "Gar zahlreich war da ihr Gefolge."
      ],
      [
        "Es ritt voran Sankt Michael."
      ],
      [
        "Er hielt die Posaune"
      ],
      [
        "Mit seiner Hand"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weitgerichte unterstehen."
      ],
      [
        "Das war der heil'ge Michael,"
      ],
      [
        "Der blies in die Posaune."
      ],
      [
        "So wurden die Geister nun gerufen"
      ],
      [
        "In Brooksvalin, wo Seelen"
      ],
      [
        "Dem Weltgerichte unterstehen."
      ],
      [
        "Und wog die Menschenseelen: Überall, wo das Christentum sich ausgebreitet hatte, gab es Bilder von Michael, der eine Waage in der einen Hand hält.",
        "In der anderen hat er oft eine Lanze oder ein Schwert, womit er den Drachen durchbohrt.",
        "So wird er auf unzähligen Kirchenmalereien und Skulpturen dar­gestellt, zum Beispiel auf dem Nordportal der Domkirche in Drontheim. -Hiermit ist im Grunde der epische Teil des Liedes zu Ende.",
        "Es folgen noch einige Verse; Olaf ermahnt seine Mitmenschen im Sinne des Wortes der Hei-ligen Schrift: «Sie sollen von ihrer Arbeit ruhen, aber ihre Taten folgen ihnen.» Landstad erzählt, er hätte gehört, daß das Lied früher bei der Leichenwache verwendet wurde für den Verstorbenen.",
        "Das Lied sollte der Seele eine Hilfe sein für ihren ersten Weg in der anderen Welt. (I."
      ],
      [
        "167 bei meinem vorletzten Besuch: Siehe die Bemerkungen von Ingeborg Möller."
      ],
      [
        "176 aus dem 2.",
        "Mosesbuche, 33.",
        "Kapitel, Vers 18: In der von Rudolf Steiner ange­gebenen Übersetzung durch Dr.",
        "Hugo Bergmann heißt es wörtlich: »Und Mose sprach zu Gott: Zeige mir doch deine Herrlichkeit!",
        "Und dieser sprach: Ich werde vorüberziehen lassen all meine Güte an deinem Angesicht und will rufen den Namen Jahves vor dir und will gnädig sein dem, den ich begnade, und mich erbarmen des, dessen ich mich erbarme.",
        "Dann aber sprach er: Du kannst mein Antlitz nicht sehen, denn mich sieht kein Mensch, der dann leben bliebe.",
        "Und es sprach Jahve: Hier ist ein Ort bei mir, stelle dich auf den Fel­sen.",
        "Und wenn meine Herrlichkeit vorüberzieht, so will ich dich in eine Höh­lung des Felsens stellen und meine Hand über dich decken, bis ich vorüber bin.",
        "Wenn ich dann meine Hand entferne, so wirst du meine Rückseite sehen; aber mein Antlitz kann nicht geschaut werden.»"
      ],
      [
        "Hugo Bergmann: geb. 1883.",
        "Philosoph, lehrt heute an der Universität in Je­rusalem."
      ],
      [
        "177 »Die Schwelle der geistigen Welt»: Siehe Hinweis zu S.60."
      ],
      [
        "184 »Die geistige Führung des Menschen und der Menschheit»: Geisteswissenschaft­liche Ergebnisse über die Menschheitsentwickelung.",
        "München 1911.",
        "Bibl.-Nr. 15, Gesamtausgabe Dornach 1963."
      ],
      [
        "194 Helena Petrowna Blavatsky: 1831-1891, begründete 1875 die Theosophische Gesellschaft."
      ],
      [
        "199 Was die Weisheit ist: I.",
        "Kor., 3, 19."
      ],
      [
        "214 Lasset die Toten: Matth. 8,22."
      ],
      [
        "216 Woodrow Wslson: l856-l924, Präsident der USA, 1912-1920."
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

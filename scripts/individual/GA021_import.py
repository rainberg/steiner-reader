#!/usr/bin/env python3
"""Standalone import script for GA021 — GA021 - Von Seelenrätseln (1917)"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA021 - Von Seelenrätseln (1917)"""
GA_NUMBER = "GA021"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "VORWORT",
    "paragraphs": [
      "Rudolf Steiner",
      "Von Seelenrätseln",
      "Anthropologie und Anthroposophie",
      "Max Dessoir über Anthroposophie",
      "Franz Brentano (Ein Nachruf)",
      "Skizzenhafte Erweiterungen",
      "Verlag der Rudolf Steiner-Nachlassverwaltung",
      "Dornach / Schweiz",
      "© 1960 by Rudolf Steifler-Nachläßverwaltung, Dornach/Schweiz",
      "Druck: Benteli AG  Bern-Bumpliz",
      "Printed in Switzerland",
      "Vorwort    7",
      "I. Anthropologie und Anthroposophie     11",
      "II. Max Dessoir über Anthroposophie     34",
      "III. Franz Brentano (Ein Nachruf)     78",
      "IV. Skizzenhafte Erweiterungen des Inhaltes dieser Schrift    128",
      "1. Die philosophische Rechtfertigung der Anthroposophie    128",
      "2. Das Auftreten der Erkenntnisgrenzen    135",
      "3. Von der Abstraktheit der Begriffe    138",
      "4. Ein wichtiges Merkmal der Geist-Wahr­nehmung      142",
      "5. Über die wirkliche Grundlage der intentionalen Beziehung     143",
      "6. Die physischen und die geistigen Abhängig­keiten der Menschen-Wesenheit    150",
      "7. Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano    163",
      "8. Ein oft erhobener Einwand gegen die Anthroposophie      169",
      "9. Schlußbemerkung      171",
      "Übersicht über die Rudolf Steiner Gesamtausgabe    174",
      "Die in dieser Schrift vereinigten Aufsätze sind von mir ge­schrieben, um einiges von dem vorzubringen, was ich zu einer Rechtfertigung des anthroposophischen Erkenntnisweges glaube sagen zu müssen.",
      "In dem ersten «Anthropologie und Anthroposophie» suche ich in einer kurzen Darstellung zu zeigen, wie wahre naturwissenschaftliche Betrachtung nicht nur in keinem Widerspruche steht mit demjenigen, was ich unter «An­throposophie» verstehe, sondern wie der geisteswissen­schaftliche Weg der letzteren von den Erkenntnismitteln der ersteren als etwas Notwendiges gefordert werden muß. Es muß eine anthroposophische Geisteswissenschaft geben, wenn die anthropologischen Erkenntnisse der Na­turwissenschaft das sein wollen, was zu sein sie beanspru­chen müssen. Entweder sind die Gründe für das Vorhan­densein einer Anthroposophie berechtigte, oder es ist auch den naturwissenschaftlichen Einsichten kein Wahr­heitswert zuzuerkennen. Dies bestrebe ich mich in dem ersten Aufsatze in einer Form auszusprechen, wie man sie in meinen bereits veröffentlichten Schriften ausgesprochen noch nicht, wenn auch veranlagt findet.",
      "Von dem zweiten Aufsatze «Max Dessoir über Anthro­posophie» gestehe ich, daß ich ein subjektives Verlangen, ihn zu schreiben, nicht gehabt habe. Allein er mußte ge­schrieben werden, weil durch die Unterlassung in man­chen Kreisen die mißverständliche Meinung sich bilden könnte, der Vertreter der Anthroposophie scheue davor zurück, in eine wissenschaftliche Diskussion mit Vertre­tern anderer Vorstellungsarten einzutreten. Ich lasse ja",
      "viele Angriffe auf die Anthroposophie gänzlich unbeant­wortet, nicht nur weil ich Polemik auf diesem Gebiete doch nicht als meine Aufgabe betrachte, sondern weil weit­aus die meisten dieser Angriffe des Ernstes ermangeln, der für eine fruchtbare Diskussion in diesem Bereiche nötig ist. Auch diejenigen Angreifer, welche glauben aus wis­senschaftlichen Beweggründen heraus die Anthroposophie bekämpfen zu sollen, wissen oftmals gar nicht, wie unwis­senschaftlich ihre Einwände gegenüber dem wissenschaft­lichen Denken sind, das die Anthroposophie für sich nötig hat. - Daß der Aufsatz über Max Dessoirs Angriff gegen die Anthroposophie nicht sein konnte, wozu ich ihn gerne gemacht hätte, bedauere ich außerordentlich.",
      "Ich wäre ger­ne in eine Diskussion eingetreten über die Vorstellungs­art, zu der Dessoir sich bekennt, einerseits und die anthro­posophische andrerseits. Statt dessen bin ich durch Des­soirs «Kritik» genötigt worden, zu zeigen, wie er ein Zerr­bild meiner Anschauungen vor seine Leser bringt, und dann nicht über diese, sondern über das von ihm Vorge­brachte spricht, das mit meinen Anschauungen nicht das geringste zu tun hat.",
      "Ich mußte zeigen, wie Max Dessoir die Bücher «liest», die er zu bekämpfen unternimmt. Da­durch ist mein Aufsatz mit der Besprechung von Dingen erfüllt, die kleinlich erscheinen können. Wie soll man aber anders verfahren, wenn Kleinlichkeiten nötig sind, um die Wahrheit darzustellen?",
      "Ob Max Dessoir das Recht hat, die von mir vertretene Anthroposophie dadurch herabzu­setzen, daß er sie in Geistesströmungen einreiht, von de­nen er sagt, sie seien «eine Mischung aus falschen Deutun­gen gewisser seelischer Vorgänge und falsch gewerteten Überbleibseln einer verschwundenen Weltanschauung»:",
      "das zu beurteilen, überlasse ich den Lesern meiner Schrift, die aus dieser entnehmen werden, wie viel dieser «Kriti­ker » von meinen Anschauungen hat verstehen können nach der Art, wie er meine Bücher gelesen hat.*",
      "Von dem dritten Aufsatz «Franz Brentano» (ein Nachruf) habe ich das Gegenteil zu sagen. Ihn zu schreiben, war mir tiefstes Bedürfnis. Und wenn ich in bezug auf ihn et­was bedauere, so ist es dieses, daß ich ihn nicht vor langer Zeit habe schreiben und den Versuch unternehmen kön­nen, ihn Brentano noch vor Augen treten zu lassen. Allein trotzdem ich ein eifriger Leser von Brentanos Schriften seit sehr langer Zeit bin: erst jetzt ist mir sein Lebenswerk so vor die Seele getreten, daß ich das Verhältnis desselben zur Anthroposophie in der Art darstellen kann, wie es in dieser Schrift geschieht. Der Hingang des verehrten Man­nes hat mich gedrängt, dieses Lebenswerk wieder in Ge­danken durchzuleben; und daraus sind die Ansichten über dasselbe erst zu dem vorläufigen Abschluß gekommen, welcher den Ausführungen meines Aufsatzes zugrunde liegt.",
      "Angegliedert habe ich an diese drei Aufsätze «Skizzenhafte Erweiterungen des Inhaltes dieser Schrift», die anthroposophische Forschungsergebnisse darstellen. Die Verhältnisse der Gegenwart bringen es mit sich, daß ich in diesen Darstellungen Andeutungen über Ergebnisse gebe, die eigentlich eine viel ausführlichere Besprechung notwendig",
      "* Über andere gegnerische Schriften und Aufsätze vergleiche die Schluß­bemerkung dieser Schrift. Im Grunde empfinde ich es als dem Ernste dieser Zeit nicht angemessen, solche Polemik erscheinen zu lassen, wie die mir durch Dessoirs Schrift notwendig gewordene. Allein ich durfte mich in die­sem Falle der Antwort auf die Herausforderung durch einen solchen Angriff nicht entziehen.",
      "machen, wie ich sie bisher - aber auch nur teilweise - in mündlichen Vorträgen vorgebracht habe. Ich ziehe in diesen Darstellungen einige der wissenschaftlichen Fäden, die von der Anthroposophie zur Philosophie, zur Psycho­logie und zur Physiologie gezogen werden müssen.",
      "Es könnte wohl scheinen, als ob in der gegenwärtigen Zeit die Interessen des Menschen nach anderer Richtung gehen müßten als diejenige ist, in welcher die folgenden Betrachtungen sich bewegen. Doch glaube ich, daß man nicht nur nicht abgezogen von den ernsten Pflichten die­ser unmittelbaren Gegenwart gegenüber durch solche Be­trachtungen wird, sondern daß, was in ihnen liegt, gerade dieser Gegenwart dient durch Impulse, die vielleicht weni­ger unmittelbar hervorstechende, aber dafür um so stär­kere Beziehungen zu dem Erleben dieser Gegenwart haben.",
      "Berlin, 10. September 1917                    RUDOLF STEINER"
    ],
    "sentences": [
      [
        "Rudolf Steiner"
      ],
      [
        "Von Seelenrätseln"
      ],
      [
        "Anthropologie und Anthroposophie"
      ],
      [
        "Max Dessoir über Anthroposophie"
      ],
      [
        "Franz Brentano (Ein Nachruf)"
      ],
      [
        "Skizzenhafte Erweiterungen"
      ],
      [
        "Verlag der Rudolf Steiner-Nachlassverwaltung"
      ],
      [
        "Dornach / Schweiz"
      ],
      [
        "© 1960 by Rudolf Steifler-Nachläßverwaltung, Dornach/Schweiz"
      ],
      [
        "Druck: Benteli AG Bern-Bumpliz"
      ],
      [
        "Printed in Switzerland"
      ],
      [
        "Vorwort 7"
      ],
      [
        "Anthropologie und Anthroposophie 11"
      ],
      [
        "Max Dessoir über Anthroposophie 34"
      ],
      [
        "III.",
        "Franz Brentano (Ein Nachruf) 78"
      ],
      [
        "Skizzenhafte Erweiterungen des Inhaltes dieser Schrift 128"
      ],
      [
        "Die philosophische Rechtfertigung der Anthroposophie 128"
      ],
      [
        "Das Auftreten der Erkenntnisgrenzen 135"
      ],
      [
        "Von der Abstraktheit der Begriffe 138"
      ],
      [
        "Ein wichtiges Merkmal der Geist-Wahr­nehmung 142"
      ],
      [
        "Über die wirkliche Grundlage der intentionalen Beziehung 143"
      ],
      [
        "Die physischen und die geistigen Abhängig­keiten der Menschen-Wesenheit 150"
      ],
      [
        "Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano 163"
      ],
      [
        "Ein oft erhobener Einwand gegen die Anthroposophie 169"
      ],
      [
        "Schlußbemerkung 171"
      ],
      [
        "Übersicht über die Rudolf Steiner Gesamtausgabe 174"
      ],
      [
        "Die in dieser Schrift vereinigten Aufsätze sind von mir ge­schrieben, um einiges von dem vorzubringen, was ich zu einer Rechtfertigung des anthroposophischen Erkenntnisweges glaube sagen zu müssen."
      ],
      [
        "In dem ersten «Anthropologie und Anthroposophie» suche ich in einer kurzen Darstellung zu zeigen, wie wahre naturwissenschaftliche Betrachtung nicht nur in keinem Widerspruche steht mit demjenigen, was ich unter «An­throposophie» verstehe, sondern wie der geisteswissen­schaftliche Weg der letzteren von den Erkenntnismitteln der ersteren als etwas Notwendiges gefordert werden muß.",
        "Es muß eine anthroposophische Geisteswissenschaft geben, wenn die anthropologischen Erkenntnisse der Na­turwissenschaft das sein wollen, was zu sein sie beanspru­chen müssen.",
        "Entweder sind die Gründe für das Vorhan­densein einer Anthroposophie berechtigte, oder es ist auch den naturwissenschaftlichen Einsichten kein Wahr­heitswert zuzuerkennen.",
        "Dies bestrebe ich mich in dem ersten Aufsatze in einer Form auszusprechen, wie man sie in meinen bereits veröffentlichten Schriften ausgesprochen noch nicht, wenn auch veranlagt findet."
      ],
      [
        "Von dem zweiten Aufsatze «Max Dessoir über Anthro­posophie» gestehe ich, daß ich ein subjektives Verlangen, ihn zu schreiben, nicht gehabt habe.",
        "Allein er mußte ge­schrieben werden, weil durch die Unterlassung in man­chen Kreisen die mißverständliche Meinung sich bilden könnte, der Vertreter der Anthroposophie scheue davor zurück, in eine wissenschaftliche Diskussion mit Vertre­tern anderer Vorstellungsarten einzutreten.",
        "Ich lasse ja"
      ],
      [
        "viele Angriffe auf die Anthroposophie gänzlich unbeant­wortet, nicht nur weil ich Polemik auf diesem Gebiete doch nicht als meine Aufgabe betrachte, sondern weil weit­aus die meisten dieser Angriffe des Ernstes ermangeln, der für eine fruchtbare Diskussion in diesem Bereiche nötig ist.",
        "Auch diejenigen Angreifer, welche glauben aus wis­senschaftlichen Beweggründen heraus die Anthroposophie bekämpfen zu sollen, wissen oftmals gar nicht, wie unwis­senschaftlich ihre Einwände gegenüber dem wissenschaft­lichen Denken sind, das die Anthroposophie für sich nötig hat. - Daß der Aufsatz über Max Dessoirs Angriff gegen die Anthroposophie nicht sein konnte, wozu ich ihn gerne gemacht hätte, bedauere ich außerordentlich."
      ],
      [
        "Ich wäre ger­ne in eine Diskussion eingetreten über die Vorstellungs­art, zu der Dessoir sich bekennt, einerseits und die anthro­posophische andrerseits.",
        "Statt dessen bin ich durch Des­soirs «Kritik» genötigt worden, zu zeigen, wie er ein Zerr­bild meiner Anschauungen vor seine Leser bringt, und dann nicht über diese, sondern über das von ihm Vorge­brachte spricht, das mit meinen Anschauungen nicht das geringste zu tun hat."
      ],
      [
        "Ich mußte zeigen, wie Max Dessoir die Bücher «liest», die er zu bekämpfen unternimmt.",
        "Da­durch ist mein Aufsatz mit der Besprechung von Dingen erfüllt, die kleinlich erscheinen können.",
        "Wie soll man aber anders verfahren, wenn Kleinlichkeiten nötig sind, um die Wahrheit darzustellen?"
      ],
      [
        "Ob Max Dessoir das Recht hat, die von mir vertretene Anthroposophie dadurch herabzu­setzen, daß er sie in Geistesströmungen einreiht, von de­nen er sagt, sie seien «eine Mischung aus falschen Deutun­gen gewisser seelischer Vorgänge und falsch gewerteten Überbleibseln einer verschwundenen Weltanschauung»:"
      ],
      [
        "das zu beurteilen, überlasse ich den Lesern meiner Schrift, die aus dieser entnehmen werden, wie viel dieser «Kriti­ker » von meinen Anschauungen hat verstehen können nach der Art, wie er meine Bücher gelesen hat.*"
      ],
      [
        "Von dem dritten Aufsatz «Franz Brentano» (ein Nachruf) habe ich das Gegenteil zu sagen.",
        "Ihn zu schreiben, war mir tiefstes Bedürfnis.",
        "Und wenn ich in bezug auf ihn et­was bedauere, so ist es dieses, daß ich ihn nicht vor langer Zeit habe schreiben und den Versuch unternehmen kön­nen, ihn Brentano noch vor Augen treten zu lassen.",
        "Allein trotzdem ich ein eifriger Leser von Brentanos Schriften seit sehr langer Zeit bin: erst jetzt ist mir sein Lebenswerk so vor die Seele getreten, daß ich das Verhältnis desselben zur Anthroposophie in der Art darstellen kann, wie es in dieser Schrift geschieht.",
        "Der Hingang des verehrten Man­nes hat mich gedrängt, dieses Lebenswerk wieder in Ge­danken durchzuleben; und daraus sind die Ansichten über dasselbe erst zu dem vorläufigen Abschluß gekommen, welcher den Ausführungen meines Aufsatzes zugrunde liegt."
      ],
      [
        "Angegliedert habe ich an diese drei Aufsätze «Skizzenhafte Erweiterungen des Inhaltes dieser Schrift», die anthroposophische Forschungsergebnisse darstellen.",
        "Die Verhältnisse der Gegenwart bringen es mit sich, daß ich in diesen Darstellungen Andeutungen über Ergebnisse gebe, die eigentlich eine viel ausführlichere Besprechung notwendig"
      ],
      [
        "* Über andere gegnerische Schriften und Aufsätze vergleiche die Schluß­bemerkung dieser Schrift.",
        "Im Grunde empfinde ich es als dem Ernste dieser Zeit nicht angemessen, solche Polemik erscheinen zu lassen, wie die mir durch Dessoirs Schrift notwendig gewordene.",
        "Allein ich durfte mich in die­sem Falle der Antwort auf die Herausforderung durch einen solchen Angriff nicht entziehen."
      ],
      [
        "machen, wie ich sie bisher - aber auch nur teilweise - in mündlichen Vorträgen vorgebracht habe.",
        "Ich ziehe in diesen Darstellungen einige der wissenschaftlichen Fäden, die von der Anthroposophie zur Philosophie, zur Psycho­logie und zur Physiologie gezogen werden müssen."
      ],
      [
        "Es könnte wohl scheinen, als ob in der gegenwärtigen Zeit die Interessen des Menschen nach anderer Richtung gehen müßten als diejenige ist, in welcher die folgenden Betrachtungen sich bewegen.",
        "Doch glaube ich, daß man nicht nur nicht abgezogen von den ernsten Pflichten die­ser unmittelbaren Gegenwart gegenüber durch solche Be­trachtungen wird, sondern daß, was in ihnen liegt, gerade dieser Gegenwart dient durch Impulse, die vielleicht weni­ger unmittelbar hervorstechende, aber dafür um so stär­kere Beziehungen zu dem Erleben dieser Gegenwart haben."
      ],
      [
        "Berlin, 10.",
        "September 1917 RUDOLF STEINER"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "I ANTHROPOLOGIE UND ANTHROPOSOPHIE",
    "paragraphs": [
      "Max Dessoirs Buch «Vom Jenseits der Seele» enthält einen kurzen Abschnitt, in dem die von mir vertretene anthro­posophisch orientierte Geisteswissenschaft als wissen­schaftlich unberechtigt gekennzeichnet werden soll.* Nun könnte es manchem scheinen, als ob eine Diskussion mit Persönlichkeiten, welche auf dem wissenschaftlichen Ge­sichtspunkte Dessoirs stehen, für den Vertreter der geisteswissenschaftlichen Anthroposophie unter allen Umständen unfruchtbar sein müsse. Denn der letztere muß ein rein geistiges Erfahrungsgebiet behaupten, das der erstere grundsätzlich ablehnt und in den Bereich der Phantasiegebilde verweist. Man könne also über die in Betracht kom­menden geisteswissenschaftlichen Erkenntnisse nur mit jemand sprechen, der von vorneherein Gründe zu haben glaubt dafür, daß das gemeinte geisteswissenschaftliche Gebiet eine Wirklichkeit ist. - Diese Ansicht wäre richtig, wenn der Vertreter der Anthroposophie nichts anderes vorbrächte als seine inneren persönlichen Erlebnisse, und diese sich einfach neben die Ergebnisse der auf Sinnes­beobachtung und wissenschaftliche Verarbeitung dieser Beobachtung begründeten Wissenschaft hinstellten. Dann könnte man sagen: der Bekenner der so gekennzeichneten",
      "* Vergleiche Max Dessoir: «Vom Jenseits der Seele», die Geheimwissen­schaften in kritischer Betrachtung. Der im besonderen über Anthroposophie handelnde Abschnitt umfaßt die Seiten 254-263.",
      "Wissenschaft lehne es eben ab, die Erlebnisse des Erfor­schers des Geistgebietes als Wirklichkeiten anzusehen, und dieser könne mit dem von ihm Vorgebrachten nur auf sol­che Persönlichkeiten Eindruck machen, die von vorne­herein sich auf seinen Gesichtspunkt stellen.",
      "Nun beruht aber diese Meinung doch nur auf einer mißverständlichen Auffassung dessen, was von mir Anthro­posophie genannt wird. Richtig ist, daß diese Anthroposo­phie auf seelischen Erfahrungen beruht, die unabhängig von den Eindrücken der Sinneswelt und auch unabhängig von den wissenschaftlichen Urteilen gewonnen werden, die nur auf die Sinneseindrücke sich stützen. Es muß also zugegeben werden, daß beide Arten von Erfahrungen zu­nächst wie durch eine unübersteigliche Kluft geschieden scheinen. - Doch dieses entspricht nicht der Wahrheit. Es gibt ein gemeinsames Gebiet, auf dem sich beide For­schungsrichtungen begegnen müssen, und auf dem eine Diskussion möglich ist über dasjenige, was von der einen und der anderen vorgebracht wird. Dies gemeinsame Ge­biet läßt sich auf die folgende Art kennzeichnen.",
      "Der Vertreter der Anthroposophie glaubt aus Erfahrun­gen heraus, die nicht nur seine persönlichen Erlebnisse sind, behaupten zu dürfen, daß die menschlichen Erkenntnisvorgange von dem Punkte an weiter entwickelt werden können, bei dem derjenige Forscher halt macht, der sich nur auf Sinnesbeobachtung und Verstandesurteil über die­se Sinnesbeobachtung stützen will. Ich möchte in dem Fol­genden, um fortwährenden langatmigen Umschreibungen zu entgehen, die auf Sinnesbeobachtung und verstandesge­mäße Bearbeitung der Sinnesbeobachtung gestützte Wis­senschaftsrichtung Anthropologie nennen und bitte den",
      "Leser, mir diesen nicht gewöhnlichen Gebrauch dieses Ausdruckes zu gestatten. Er soll in den folgenden Ausführungen nur für das hier Gekennzeichnete angewendet wer­den. In diesem Sinne meint Anthroposophie mit ihrer For­schung da beginnen zu können, wo Anthropologie auf­hört.*",
      "Der Vertreter der Anthropologie bleibt dabei stehen, die in der Seele erlebbaren Verstandesbegriffe auf die Sin­neserlebnisse zu beziehen. Der Vertreter der Anthroposo­phie macht die Erfahrung, daß diese Begriffe, abgesehen davon, daß sie auf die Sinneseindrücke bezogen werden sollen, noch ein eigenes Leben für sich in der Seele entfal­ten können. Und daß sie, indem sie dieses Leben innerhalb der Seele entfalten, in dieser selbst eine Entwickelung zu­stande bringen. Er wird sich bewußt, wie die Seele, wenn sie auf diese Entwickelung die notwendige Aufmerksam­keit wendet, innerhalb ihres Wesens die Entdeckung macht, daß sich in ihr Geistorgane offenbaren. (Ich gebrau­che diesen Ausdruck «Geistorgane», indem ich erweiternd den Sprachgebrauch aufnehme, dem Goethe aus seiner",
      "* Obgleich dasjenige, was von mir als «Anthroposophie» vertreten wird, in seinen Ergebnissen auf einem ganz anderen Boden steht als die Ausführungen Robert Zimmermanns in seinem 188 1 erschienenen Buche «Anthroposophie», so glaube ich doch den von Zimmermann gekenn­zeichneten Begriff des Unterschiedes von Anthroposophie und Anthropo­logie gebrauchen zu dürfen. Zimmermann faßt aber als den Inhalt seiner «Anthroposophie» nur die von der Anthropologie gelieferten Begriffe in ein abstraktes Schema. Ihm liegt das erkennende Schauen, auf dem die von mir gemeinte Anthroposophie ruht, nicht im Bereiche der wissenschaftli­chen Forschungswege. Seine Anthroposophie unterscheidet sich von der Anthropologie nur dadurch, daß die erstere die von der letzteren erhaltenen Begriffe erst einem dem Herbartschen Philosophieren ähnlichen Verfahren unterwirft, bevor sie dieselben zum Inhalte ihres rein verstandesmäßigen Ideen-Schemas macht.",
      "Weltanschauung heraus gefolgt ist, als er die Ausdrücke «Geistes-Augen», «Geistes-Ohren » anwandte.)* Solche Geistorgane stellen dann für die Seele Bildungen dar, die für sie ähnlich gedacht werden dürfen wie die Sinnesorga­ne für den Leib. Selbstverständlich dürfen sie nur seelisch gedacht werden. Jeder Versuch, sie mit irgendeiner leibli­chen Bildung zusammenzubringen, muß von der Anthro­posophie strengstens abgelehnt werden. Sie muß ihre Geistorgane so vorstellen, daß sie in keiner Weise aus dem Bereich des Seelischen heraustreten und in das Gefüge des Leiblichen übergreifen. Ihr gilt ein solches Übergreifen als krankhafte Bildung, die sie aus ihrem Bereich streng ausschließt. Die Art, wie innerhalb der Anthroposophie über die Entwickelung der Geistorgane gedacht wird, sollte für denjenigen, der sich über diese Art wirklich unterrichtet, ein genügend starker Beweis sein dafür, daß über abnorme Seelenerlebnisse, über Illusionen, Visionen, Halluzinatio­nen usw. für den Erforscher des wirklichen Geistgebietes keine anderen Vorstellungen vorhanden sind als die auch innerhalb der Anthropologie berechtigten.** Eine Ver­wechselung der anthroposophischen Ergebnisse mit ab­normen sogenannten Seelenerlebnissen beruht immer auf Mißverständnis oder ungenügender Kenntnis des in der Anthroposophie Gemeinten. Auch kann derjenige, der",
      "* Eine ausführlichere Darstellung und Rechtfertigung dieser Vorstel­lung von «Geistorganen» findet man in meinem Buche «Vom Menschen­rätsel» Seite 146 ff. und in meinen auf Goethes Weltanschauung bezüglichen Schriften.",
      "**    Die inneren Erlebnisse, welche von der Seele durchzumachen sind, um zu dem Gehrauch ihrer Geistorgane zu kommen, findet man in einer Reihe meiner Schriften geschildert, besonders in meinem Buche: «Wie er­langt man Erkenntnisse der höheren Welten?» und im zweiten Teile meiner «Geheimwissenschaft».",
      "einsichtsvoll verfolgt, wie Anthroposophie den Weg zur Entwickelung der Geistorgane darstellt, gewiß nicht auf die Meinung verfallen, dieser Weg könne zu krankhaften Bildungen oder Zuständen führen. Der Einsichtsvolle sollte vielmehr erkennen, daß alle Stufen des seelischen Er­fahrens, welche der Mensch im Sinne der Anthroposophie auf dem Wege zur Geist-Anschauung erlebt, in einem Ge­biete liegen, das ganz nur seelisch ist, und neben dem das Erleben der Sinne und die gewöhnliche Verstandestätig­keit unverändert so verlaufen, wie sie vor der Entstehung dieses Gebietes verlaufen sind.",
      "Daß gerade in bezug auf diese Seite der anthroposophischen Erkenntnis viele Mißverständnisse herrschen, rührt davon her, daß es manchen Menschen Schwierigkeiten bereitet, ein rein Seelisches in den Bereich ihrer Aufmerksamkeit zu ziehen. Solche Men­schen werden sogleich verlassen von der Kraft ihres Vorstellen, wenn dieses nicht gestützt ist durch den Hinblick auf sinnlich Wahrnehmbares.",
      "Es dämpft sich dann deren Vorstellungskraft herunter selbst unter das Maß von Stär­ke, die im Träumen herrscht, bis zu jenem niedrigen Gra­de, der für das Vorstellen im traumlosen Schlafe vorhan­den ist, und der nicht mehr bewußt wird. Man kann sagen, solche Menschen sind in ihrem Bewußtsein erfüllt von den Nachwirkungen oder der unmittelbaren Wirkung der Sin­nes-Eindrücke, und es geht neben diesem Erfüllt-Sein ein Verschlafen alles dessen einher, das als Seelisches erkannt würde, wenn es erfaßt werden könnte.",
      "Man kann sogar sagen, daß das Seelische in seiner Eigenart deshalb von vielen Menschen dem schärfsten Mißverständnis ausge­setzt wird, nur weil sie gegenüber demselben nicht in der gleichen Art aufwachen können wie gegenüber dem sinnlichen",
      "Inhalt des Bewußtseins. Daß Menschen mit nur den­jenigen Aufmerksamkeitsgraden, welche das gewöhnliche äußere Leben bewirkt, In solcher Lage sind, braucht nie­mand in Verwunderung zu versetzen, der im rechten Lich­te zum Beispiel zu sehen vermag, welche Lehre aus einem Vorwürfe zu ziehen ist, den Franz Brentano dem Philoso­phen William James mit Bezug auf diese Sache machen muß.",
      "Brentano schreibt, daß man «zwischen der empfin­denden Tätigkeit und dem, worauf sie gerichtet ist, also zwischen Empfinden und Empfundenem, zu unterschei­den» habe («und sie sind so sicher verschieden als mein gegenwärtiges Mich-Erinnern und das Ereignis, das mir dabei als vergangen vorschwebt, oder, um einen noch dra­stischeren Vergleich anzuwenden, mein Haß eines Feindes und der Gegenstand dieses Hasses verschieden sind») und er macht dazu die Bemerkung, daß man den Irrtum, gegen den sich diese Worte richten, «da und dort auftauchen» sehe. Er sagt weiter: «Unter anderen hat William James ihn sich eigen gemacht, und auf dem Internationalen Kon­greß für Psychologie, Rom 1905, in längerer Rede zu be­gründen versucht.",
      "Weil mir, wenn ich in einen Saal blicke, zugleich mit dem Saal auch mein Sehen erscheint; weil fer­ner Phantasiebilder von sinnlichen Gegenständen sich von objektiv erregten Sinnesbildern derselben nur graduell un­terscheiden; weil endlich Körper von uns schön genannt werden, der Unterschied von Schön und Häßlich aber zu dem Unterschiede von Gemütsbewegungen in Beziehung steht: so sollen psychisches und physisches Phänomen nicht mehr als zwei Klassen von Erscheinungen gelten. - Es ist mir schwer verständlich, wie sich dem Redner selbst die Schwäche dieser Argumente nicht fühlbar gemacht hat.",
      "Zugleich erscheinen heißt nicht als dasselbe erscheinen, wie zugleich sein nicht so viel ist als dasselbe sein. Und darum konnte Descartes ohne Widerspruch empfehlen, zu­nächst wenigstens zu leugnen, daß der Saal, den ich sehe, sei, und nur daran, daß das Sehen des Saales sei, als an et­was Unzweifelhaftem festzuhalten.",
      "Ist aber das erste Argu­ment hinfällig, dann offenbar auch das zweite; denn was verschlüge es, wenn ein Phantasieren von einem Sehen sich nur durch den Intensitätsgrad unterschiede, da, selbst wenn auch dieser ausgeglichen wäre, die volle Gleichheit des Phantasierens mit dem Sehen nach eben dem Gesagten nur die Gleichheit mit einem psychischen Phänomen be­deuten würde? Im dritten Argument wird von Schönheit gesprochen ...",
      "Es ist nun aber gewiß eine seltsame Logik, welche daraus, daß» das Wohlgefallen am Schönen «etwas Psychisches ist, schließen will, daß auch das, an dessen Er­scheinung es geknüpft ist, etwas Psychisches sein müsse. Wäre dies richtig, so wäre auch jedes Mißfallen identisch mit dem, woran einer ein Mißfallen hat, und man müßte sich wohl hüten, einen begangenen Fehler zu bereuen, da in dieser mit ihm identischen Reue der Fehltritt selbst sich wiederholen würde. - Bei solcher Lage der Dinge dürfte es denn doch nicht wohl zu fürchten sein, daß die Autori­tät von James, der sich leider unter den deutschen Psycho­logen die eines Mach gesellt, viele dazu verleiten werde, die augenfälligsten Unterschiede zu verkennen. »* Jedenfalls ist diese «Verkennung der augenfälligsten Unterschie­de» keine seltene Tatsache.",
      "Und sie beruht darauf, daß die Kraft des Vorstellens die nötige Aufmerksamkeit nur für",
      "* Vergleiche Franz Brentano: «Untersuchungen zur Sinnespsychologie» (Leipzig, 1907), Seite 96 f.",
      "den Sinneseindruck entfalten kann, während das eigentlich Seelische, das dabei vorgeht, dem Bewußtsein sich nicht stärker vergegenwärtigt als das im Zustand des Schlafes Erlebte. Man hat es mit zwei Strömungen von Erlebnissen zu tun, von denen die eine wachend erfaßt, die andere aber",
      "- die seelische - gleichzeitig nur mit einer der abgeschwäch­ten Vorstellungskraft des Schlafes gleichkommenden, also fast mit gar keiner Aufmerksamkeit ergriffen wird. Es darf eben durchaus nicht außer acht gelassen werden, daß wäh­rend des gewöhnlichen Wachzustandes des Menschen die seelische Verfassung des Schlafes nicht einfach aufhört, sondern neben dem Wachen fortdauert, und daß das ei­gentlich Seelische nur dann in den Bereich des Wahrneh­mens tritt, wenn der Mensch nicht bloß für die Sinneswelt erwacht, wie dies im gewöhnlichen Bewußtsein stattfindet, sondern auch für das seelische Dasein, wie das im schauenden Bewußtsein der Fall ist. Ob nun durch das im Wachen fortdauernde Schlafen für das Seelische dieses letztere - im grob materialistischen Sinne - geleugnet wird, oder ob, weil es nicht gesehen, mit dem Physischen zusammenge­worfen wird, wie im Falle James', ist fast gleichgiltig; die Ergebnisse sind fast die gleichen: beides führt zu verhäng­nisvollen Kurzsichtigkeiten. Nicht verwunderlich aber ist, daß so oft das Seelische unwahrnehmbar bleibt, wenn selbst ein Philosoph wie W. James es nicht in richtiger Art von dem Physischen zu scheiden vermag.*",
      "Wer so wenig wie W. James das wesentlich Seelenhafte von den durch die Sinne erlebten Seelen-Inhalten abson­dern",
      "* Genaueres über dieses Erwachen derjenigen seelischen Fähigkeiten, welche im gewöhnlichen Bewußtsein unerwacht sind, findet man in meinem Buche «Vom Menschenrätsel» Seite 156 ff.",
      "kann, mit dem läßt sich schwer sprechen von demje­nigen Gebiete im Seelendasein, innerhalb dessen die Ent­wickelung der Geistorgane beobachtet werden soll. Denn diese Entwickelung geht eben dort vor sich, wohin sich seine Aufmerksamkeit nicht zu wenden vermag. Sie führt von dem verstandesmäßigen zum schauenden Erkennen.* Nun ist aber durch die Fähigkeit, das wesenhaft Seeli­sche wahrzunehmen, noch nichts weiter erreicht, als eine allererste Vorbedingung, die es möglich macht, den geisti­gen Blick dahin zu lenken, wo die Anthroposophie die Entwickelung der Seelenorgane sucht. Denn, was sich zu­nächst diesem Blicke darbietet, das verhält sich zu dem, wovon Anthroposophie als von dem mit Geistorganen ausgerüsteten Seelenwesen spricht, wie eine undifferen­zierte lebendige Zelle zu einem mit Sinnesorganen ausge­statteten Lebewesen. Die einzelnen Geistorgane selbst aber werden nur in dem Maße der Seele als ihr Besitz bewußt, in dem sie dieselben zu gebrauchen vermag. Denn diese Organe sind nicht etwas Ruhendes; sie sind in fortwähren­der Beweglichkeit. Und wenn sie nicht im Gebrauche sind, kann man sich auch ihres Vorhandenseins nicht bewußt sein. Für sie fällt also Wahrnehmen und im Gebrauche Stehen zusammen. Wie die Entwickelung dieser Organe und damit auch ihre Wahrnehmbarkeit zutage tritt, das fin­det man in meinen anthroposophischen Schriften geschil­dert. Ich will hier nur auf einiges in dieser Richtung Lie­gendes hinweisen.",
      "*    Eine noch weiter gehende Begründung dieser Ausführungen findet man in den am Schlusse stehenden «Skizzenhaften Erweiterungen des In­haltes dieser Schrift»: «I. Die philosophische Rechtfertigung der Anthro­posophie.»",
      "Wer sich dem Nachdenken über die durch die Sinnes-Erscheinungen bewirkten Erlebnisse hingibt, der stößt überall auf Fragen, zu deren Beantwortung ihm dieses Nachdenken zunächst unzulänglich erscheint. Im Verfolg solchen Nachdenkens kommen die Vertreter der Anthro­pologie zur Festlegung von Erkenntnisgrenzen.",
      "Es braucht nur daran erinnert zu werden, wie Du Bois-Reymond in seiner Rede über die Grenzen des Naturerkennens davon spricht, daß man nicht wissen könne, welches das Wesen der Materie ist, und welches dasjenige der einfachsten Be­wußtseinserscheinung. Man kann nun an solchen Punkten des Nachdenkens stehen bleiben und sich der Meinung hingeben: da liegen eben für den Menschen unübersteig­liche Erkenntnisschranken.",
      "Und man kann demgemäß sich dabei beruhigen, daß der Mensch nur innerhalb des von diesen Schranken umschlossenen Gebietes ein Wissen er­langen könne und darüber hinaus nur ein Ahnen, Fühlen, Hoffen, Wünschen möglich sei, mit denen eine «Wissen­schaft» nichts zu tun haben könne. - Oder man kann in diesem Punkte anheben, Hypothesen auszubilden über ein Gebiet, das über das Sinnlich-Wahrnehmbare hinausliegt. Man bedient sich in einem solchen Falle des Verstandes, von dem man glaubt, daß er seine Urteile über ein Gebiet ausdehnen dürfe, von dem die Sinne nichts wahrnehmen.",
      "Man wird sich mit einem solchen Verfahren der Gefahr aussetzen, daß der in dieser Beziehung Ungläubige erwi­dert, der Verstand habe keine Berechtigung, über eine Wirklichkeit zu urteilen, für die ihm die Grundlage der Sinneswahrnehmungen entzogen ist. Denn diese allein gä­ben seinen Urteilen einen Inhalt.",
      "Ohne einen solchen In­halt blieben seine Begriffe leer.",
      "Die anthroposophisch orientierte Geisteswissenschaft verhält sich nicht in der einen und nicht in der andern die­ser beiden Arten zu den «Erkenntnisgrenzen». In der zweiten nicht, weil sie mit denjenigen der gleichen Ansicht sein muß, welche empfinden, daß man gewissermaßen allen Boden für das Nachdenken verliert, wenn man die Vor­stellungen so beläßt, wie man sie an den Sinneswahrneh­mungen gewonnen hat, und sie doch über dieses Gebiet hinaus anwenden will. - In der ersten Art nicht, weil sie gewahr wird, daß sich an den sogenannten Grenzen des Erkennens etwas seelisch erleben läßt, das mit dem aus der Sinneswahrnehmung gewonnenen Vorstellungs-Inhalt nichts zu tun hat.",
      "Wenn die Seele nur diesen Inhalt sich ver­gegenwärtigt, dann muß sie bei wahrer Selbstbesinnung sich sagen: dieser Inhalt kann unmittelbar nicht etwas an­deres dem Erkennen offenbaren als eine Nachbildung des sinnlich Erlebten. Anders wird die Sache, wenn die Seele dazu übergeht, sich zu fragen: was läßt sich in ihr selbst erfahren, wenn sie mit solchen Vorstellungen sich erfüllt, zu denen sie an den gewöhnlichen Erkenntnisgrenzen ge­führt wird?",
      "Sie kann sich dann bei entsprechender Selbst­besinnung sagen: erkennen im gewöhnlichen Sinne kann ich mit solchen Vorstellungen nichts; aber in dem Falle, in dem ich mir diese Ohnmacht des Erkennens recht innerlich anschaulich mache, werde ich gewahr, wie diese Vorstel­lungen in mir selbst wirken. Als gewöhnliche Erkenntnis­vorstellungen bleiben sie stumm; aber in eben dem Maße, als sich ihre Stummheit dem Bewußtsein immer mehr mit­teilt, gewinnen sie ein eigenes inneres Leben, das mit dem Leben der Seele eine Einheit wird.",
      "Und die Seele bemerkt dann, wie sie mit diesem Erleben in einer Lage ist, die sich",
      "etwa mit der Lage eines blinden Wesens vergleichen läßt, das auch noch keine besondere Ausbildung seines Tast­sinnes erfahren hat. Ein solches Wesen würde zunächst überall hin anstoßen. Es würde den Widerstand der äuße­ren Wirklichkeiten empfinden. Und aus dieser allgemeinen Empfindung könnte sich ein inneres Leben entwickeln, er­füllt von einem primitiven Bewußtsein, das nicht mehr bloß die allgemeine Empfindung hat: ich stoße an Dinge, sondern das diese Empfindung in sich vermannigfaltigt und Härte von Weichheit, Glätte von Rauhigkeit usw. un­terscheidet. - In dieser Art kann die Seele das Erlebnis in sich erfahren und vermannigfaltigen, das sie mit den an den Erkenntnisgrenzen gebildeten Vorstellungen hat. Sie lernt erfahren, daß diese Grenzen nichts anderes darstellen als dasjenige, was entsteht, wenn sie von der geistigen Welt seelisch berührt wird. Das Gewahrwerden solcher Gren­zen wird der Seele zu einem Erlebnis, das sich vergleichen läßt mit dem Tast-Erlebnis auf dem sinnlichen Gebiete.* Was sie vorher als Grenze des Erkennens bezeichnet hat, in dem sieht sie nunmehr die geistig-seelische Berührung durch eine geistige Welt. Und aus dem besonnenen Erle­ben, das sie mit den verschiedenen Grenzvorstellungen ha­ben kann, besondert sich ihr die allgemeine Empfindung einer geistigen Welt zu einem mannigfaltigen Wahrneh­men derselben. Auf solche Art wird die gewissermaßen",
      "* Erkenntnisgrenzen wie die oben besprochenen treten nicht bloß in der geringen Zahl auf, in der sie manchem zum Bewußtsein kommen; sie erge­ben sich in großer Menge auf den Wegen, die das Nachdenken durch sein inneres Wesen einschlagen muß, um in ein Verhältnis zur wahren Wirklich­keit zu kommen. Man vergleiche dazu in dem letzten Abschnitt «Skizzen­hafte Erweiterungen des Inhaltes dieser Schrift» das Kapitel: «Das Auftre­ten der Erkenntnisgrenzen.»",
      "niedrigste Art der Wahrnehmbarkeit der geistigen Welt zum Erlebnis. Es ist damit nur das erste Aufschließen der Seele für die geistige Welt gekennzeichnet. Aber es ist auch gezeigt, daß in demjenigen, was die von mir gemeinte An­throposophie als geistige Erlebnisse anstrebt, nicht auf all­gemeine nebulose gefühlsmäßige Selbsterlebnisse der Seele gedeutet wird, sondern auf etwas, das in gesetzmäßiger Art in einem wirklichen inneren Erleben entwickelt wird. Es kann hier nicht der Ort sein, zu zeigen, wie die erste primitive Geist-Wahrnehmung durch weitere seelische Verrichtungen gesteigert wird, so daß, wie von einem gei­stig-seelischen Tasten, auch von anderen gewissermaßen höheren Wahrnehmungsarten gesprochen werden kann. Es muß bezüglich der Schilderung solcher seelischer Ver­richtungen auf meine anthroposophischen Bücher und Aufsätze verwiesen werden. Hier sollte nur das Prinzipielle angedeutet werden über die geistige Wahrnehmung, von welcher die Anthroposophie spricht.",
      "Durch einen Vergleich möchte ich noch veranschauli­chen, wie anders das ganze Verhalten der Seele innerhalb der anthroposophischen Geistes-Erforschung ist als in der Anthropologie. Man stelle sich eine Anzahl von Weizen­körnern vor. Man kann diese als Nahrungsmittel verwen­den. Man kann sie aber auch in die Erde setzen, sodaß sich andere Weizenpflanzen aus ihnen entwickeln. Man kann Vorstellungen, die man durch die Sinnes-Erlebnisse ge­wonnen hat, so im Bewußtsein halten, daß man in ihnen das Nachbilden der sinnenfälligen Wirklichkeit erlebt. Und man kann sie auch so erleben, daß man die Kraft in der Seele wirksam sein läßt, die sie in derselben durch das­jenige ausüben, was sie sind, abgesehen davon, daß sie ein",
      "Sinnliches abbilden. Die erste Wirkungsweise der Vorstel­lungen in der Seele läßt sich vergleichen mit dem, was durch die Weizenkörner wird, wenn sie als Nahrungsmittel von einem Lebewesen aufgenommen werden. Die zweite mit der Hervorbringung einer neuen Weizenpflanze durch jedes Samenkorn. - Der Vergleich darf allerdings nur so gedacht werden, daß man berücksichtigt: aus dem Samenkorn wird eine der Vorfahren-Pflanze ähnliche; aus der in der Seele wirksamen Vorstellung wird innerhalb der Seele eine der Bildung von Geistorganen dienliche Kraft. Und berücksichtigt muß auch werden, daß das erste Bewußt­sein solcher inneren Kräfte nur an so stark wirksamen Vor­stellungen entzündet werden kann, wie es die gekennzeich­neten Grenzvorstellungen sind, daß aber, wenn dieses Be­wußtsein für solche Kräfte einmal erwacht ist, ihm in aller­dings geringerem Maße auch andere Vorstellungen dienst­bar sein können, um den eingeschlagenen Weg weiter zu gehen.",
      "Zugleich weist dieser Vergleich auf etwas hin, das sich der anthroposophischen Forschung über das Wesen des Vorstellungslebens ergibt. Wie das Samenkorn, wenn es zum Nahrungsmittel verarbeitet wird, aus derjenigen Ent­wickelungsströmung herausgehoben wird, die in seiner ur­eigenen Wesenheit liegt und zur Bildung einer neuen Pflan­ze führt, so wird die Vorstellung aus der ihr wesentlichen Entwickelungsrichtung abgelenkt, wenn sie von der vorstellenden Seele zur Nachbildung einer Sinneswahrneh­mung verwendet wird. Die der Vorstellung durch ihr eige­nes Wesen entsprechende Entwickelung ist die, in der Ent­wickelung der Seele als Kraft zu wirken. Ebenso wie man die der Pflanze eigenen Entwickelungsgesetze nicht findet,",
      "wenn man die Samen auf ihren Nahrungswert hin unter­sucht, ebenso wenig findet man das Wesen der Vorstel­lung, wenn man untersucht, inwiefern sie die nachbildende Erkenntnis der durch sie vermittelten Wirklichkeit hervor­bringt. Es soll damit nicht gesagt sein, daß diese Untersu­chung nicht angestellt werden könnte. Sie kann dies eben­so, wie diejenige über den Nahrungswert der Pflanzensa­men. Aber wie man durch das letztere sich über etwas an­deres auf klärt als über die Entwickelungsgesetze des Pflan­zenwachstums, so erlangt man durch eine Erkenntnistheo­rie, welche die Vorstellungen auf ihren nachbildenden Er­kenntniswert hin prüft, über etwas anderes Aufschluß als über das Wesen des Vorstellungslebens. So wenig das Sa­menkorn es in seinem Wesen vorgezeichnet hat, Nahrung zu werden, so wenig liegt es im Wesen der Vorstellung, nachbildende Erkenntnis zu liefern. Ja, man kann sagen, wie die Verwendung als Nahrungsmittel etwas für das Sa­menkorn ganz Äußerliches ist, so ist es das erkenntnismäßige Nachbilden für die Vorstellungen. In Wahrheit er­greift in den Vorstellungen die Seele ihr eigenes sich ent­wickelndes Wesen. Und erst durch die eigene Tätigkeit der Seele geschieht es, daß die Vorstellungen zu Vermittlern der Erkenntnis einer Wirklichkeit werden.*",
      "Die Frage nun, wie die Vorstellungen zu solchen Er­kenntnisvermittlern werden, muß die anthroposophische Beobachtung, welche sich der Geistorgane bedient, anders beantworten als die Erkenntnistheorien es tun, welche diese",
      "* Eine ausführlichere Begründung der in obigem gegebenen Gedanken findet man in dem letzten Abschnitt des 2. Bandes meiner «Rätsel der Philo­sophie»: «Skizzenhaft dargestellter Ausblick auf eine Anthroposophie»",
      "(Seiten 594-627).",
      "Beobachtung ablehnen. Für diese anthroposophische Be­obachtung ergibt sich das Folgende.",
      "So wie die Vorstellungen ihrem ureigenen Wesen nach sind, bilden sie zwar einen Teil des Lebens der Seele; aber sie können nicht in der Seele bewußt werden, so lange diese nicht ihre Geistorgane bewußt gebraucht. Sie bleiben, so lange sie ihrem Eigenwesen nach lebendig sind, in der Seele unbewußt. Die Seele lebt durch sie, aber sie kann nichts von ihnen wissen. Sie müssen ihr eigenes Leben her­abdämpfen, um bewußte Seelenerlebnisse des gewöhnli­chen Bewußtseins zu werden. Diese Herabdämpfung ge­schieht durch jede sinnliche Wahrnehmung. So kommt, wenn die Seele einen Sinneseindruck empfängt, eine Her­ablähmung des Vorstellungslebens zustande; und die her­abgelähmte Vorstellung erlebt die Seele bewußt als den Vermittler einer Erkenntnis der äußeren Wirklichkeit.* Alle Vorstellungen, die von der Seele auf eine äußere Sin­nes-Wirklichkeit bezogen werden, sind innere Geist-Er­lebnisse, deren Leben herabgedämpft ist. In allem, das man über eine äußere Sinneswelt denkt, hat man es mit den erstatteten Vorstellungen zu tun. Nun geht aber das Vorstel­lungsleben nicht etwa verloren, sondern es führt sein Da­sein, getrennt von dem Gebiete des Bewußtseins, in den nicht bewußten Sphären der Seele. Und da wird es von den Geistorganen wiedergefunden. So wie nun die abgetöteten Vorstellungen von der Seele auf die Sinneswelt bezogen werden können, so die mit den Geistorganen erfaßten le­bendigen Vorstellungen auf die Geisteswelt. - Die oben",
      "* Man vergleiche damit den 3. Abschnitt der am Schlusse dieser Schrift gegebenen «Skizzenhaften Erweiterungen des Inhaltes ...»: «Von der Ab­straktheit der Begriffe.»",
      "gekennzeichneten Grenzvorstellungen sind diejenigen, die sich durch ihre eigene Wesenheit nicht ablähmen lassen, daher widerstreben sie einer Beziehung zur Sinnes-Wirk­lichkeit. Eben dadurch werden sie zu Ausgangspunkten der Geistwahrnehmung.",
      "Vorstellungen, die als lebendige von der Seele erfaßt werden, habe ich in meinen anthroposophischen Schriften imaginative Vorstellungen genannt. Man verkennt, was hier als «imaginativ» gemeint ist, wenn man es verwech­selt mit der bildlichen Ausdrucksform, die angewendet wer­den muß, um solche Vorstellungen entsprechend anzudeu­ten. Was da wirklich mit «imaginativ» gemeint ist, kann etwa in der folgenden Art verdeutlicht werden. Wenn je­mand eine Sinneswahrnehmung hat, während ihn der äu­ßere Gegenstand beeindruckt, dann hat die Wahrnehmung für ihn eine gewisse innere Stärke. Wenn er sich von dem Gegenstande abwendet, dann kann er sich in einer bloßen Innenvorstellung denselben vergegenwärtigen. Aber die Vorstellung hat nur eine geringere innere Stärke. Sie ist im Verhältnis zu der bei Anwesenheit des äußeren Gegenstan­des wirksamen Vorstellung gewissermaßen schattenhaft. Wenn der Mensch für das gewöhnliche Bewußtsein schattenhaft in seiner Seele vorhandene Vorstellungen beleben will, so durchtränkt er sie mit Nachklängen an die Sinnesanschauung. Er macht die Vorstellung zum anschaulichen Bilde. Solche Bildvorstellungen sind nun gewiß nichts an­deres als Ergebnisse aus dem Zusammenwirken des Vor­stellens und des Sinneslebens. Die «imaginativen» Vor­stellungen der Anthroposophie entstehen durchaus nicht in dieser Art. Die Seele muß, um sie zustande zu bringen, so genau den inneren Vorgang der Vereinigung von Vorstellungsleben",
      "und Sinnes-Eindruck kennen, daß sie das Einfließen der Sinneseindrücke, beziehungsweise ihrer Nacherlebnisse, in das Vorstellungsleben ganz fern halten kann. Man bringt die Fernhaltung der Sinnes-Nach-Erleb­nisse nur zustande, wenn man kennen gelernt hat, wie das Vorstellen von diesen Nacherlebnissen ergriffen wird.",
      "Erst dann ist man in der Lage, die Geistorgane lebendig zu ver­binden mit dem Wesen des Vorstellens und dadurch die Eindrücke der geistigen Wirklichkeit zu empfangen. Es wird dabei das Vorstellungsleben von einer ganz anderen Seite her durchdrungen als im Sinneswahrnehmen.",
      "Die Er­lebnisse, die man dabei hat, sind wesentlich andere als die an den Sinneswahrnehmungen zu erfahrenden. Und doch gibt es eine Möglichkeit, über diese Erlebnisse sich auszu­drücken. Das kann in folgender Art geschehen. - Wenn der Mensch die Farbe Gelb wahrnimmt, so hat er in seiner Seele nicht bloß das Augenerlebnis, sondern ein gefühls­artiges Mit-Erlebnis der Seele.",
      "Dieses kann für verschie­dene Menschen eine verschiedene Stärke haben, ganz feh­len wird es niemals. Goethe hat in dem schönen Kapitel seiner Farbenlehre über «sinnlich-sittliche Wirkung der Farben» die Gefühls-Nebenwirkungen für Rot, Gelb, Grün usw. sehr eindringlich beschrieben.",
      "Nimmt nun die Seele aus einem gewissen Gebiete des Geistes etwas wahr, so kann der Fall eintreten, daß diese geistige Wahrnehmung in ihr dasselbe gefühlsmäßige Neben-Erlebnis hat, das bei der sinnlichen Wahrnehmung des Gelb auftritt. Man weiß dann, daß man dieses oder jenes geistige Erlebnis hat.",
      "Man hat dabei natürlich nicht in der Vorstellung dasselbe vor sich, was man in der sinnlichen Wahrnehmung der gelben Farbe vor sich hat. Aber man hat dasselbe Innenerlebnis",
      "als gefühlsmäßige Nebenwirkung, das man hat, wenn die gelbe Farbe vor dem Auge ist. Man sagt dann: man nehme das Geist-Erlebnis als «gelb» wahr. Vielleicht könnte man, um sich genauer auszudrücken, immer sagen: man nimmt etwas wahr, was wie «gelb» für die Seele ist. Doch sollte niemand einer so umständlichen Redeweise bedürfen, der aus der anthroposophlschen Literatur den Vorgang ken­nen gelernt hat, welcher zur geistigen Wahrnehmung führt. Diese Literatur macht genugsam darauf aufmerk­sam, daß das der Geistwahrnehmung zugängliche Wesenhafte nicht so vor dem Geistorgane steht wie ein verdünn­ter sinnlicher Gegenstand oder Vorgang, oder so, daß es wiedergegeben werden könnte durch Vorstellungen, die in gewöhnlicher Bedeutung sinnlich-anschauliche sind.*",
      "Wie die geistige Welt, die außerhalb des Menschen liegt, so lernt die Seele durch ihre Geistorgane das geistige Wesen des Menschen selbst kennen. Anthroposophie beobachtet dieses geistige Wesen als Glied der geistigen Welt. Sie schreitet von der Beobachtung eines Teiles der geistigen Welt fort zu solchen Vorstellungen über den Menschen, welche ihr vergegenwärtigen, was sich im Menschenleibe als geistiger Mensch offenbart. Die Anthropologie schrei­tet, von der entgegengesetzten Richtung kommend, eben­falls zu Vorstellungen fort über das menschliche Wesen. Bildet die Anthroposophie die in obigen Ausführungen",
      "* Eine weitere Beleuchtung findet das zuletzt hier Ausgesprochene durch das 4. Kapitel der am Schlusse dieser Schrift gegebenen «Skizzenhaf­ten Erweiterungen des Inhaltes ...»: «Ein wichtiges Merkmal der Geistwahrnehmung.»",
      "gekennzeichneten Beobachtungsarten aus, dann gelangt sie zu Anschauungen über das geistige Wesen des Men­schen, welches sich in der Sinneswelt in dem Leibe offen­bart. Die Blüte dieser Offenbarung ist das Bewußtsein, das die Sinneseindrücke in dem Vorstellungsdasein weiter be­stehen läßt. Indem die Anthroposophie fortschreitet von den Erlebnissen der außermenschlichen geistigen Welt bis zum Menschen, findet sie denselben zuletzt als im Sinnesleibe lebend, und in demselben das Bewußtsein von der sinnlichen Wirklichkeit entwickelnd. Das letzte, was sie auf ihrem Wege von dem Menschen findet, ist das leben­dige Vorstellungswesen der Seele, das sie in zusammen­hängenden imaginativen Vorstellungen auszudrücken ver­mag. Dann kann sie noch, gewissermaßen am Ende ihres geisterforschenden Weges, den Blick weiter gebrauchend, schauen, wie sich das wesenhafte Vorstellungsleben durch die wahrnehmenden Sinne ablähmt. In diesem abgelähm­ten Vorstellungsleben hat sie, von der Geistseite her be­leuchtet, den in der Sinneswelt lebenden Menschen, inso­fern er ein vorstellender ist, gekennzeichnet. Sie kommt auf diese Art zu einer Philosophie über den Menschen, als einem letzten Ergebnisse ihrer Forschungen. Was auf ih­rem Wege vorher liegt, befindet sich rein im Geistgebiete. Sie kommt mit dem, was sich ihr auf ihrem Geisteswege ergeben hat, bei einer Kennzeichnung des in der Sinneswelt lebenden Menschen an.",
      "Die Anthropologie erforscht die Reiche der Sinneswelt. Sie gelangt auf ihrem Wege fortschreitend ebenfalls bis zum Menschen. Es stellt sich ihr derselbe dar, wie er die Tatsachen der Sinneswelt in seiner Leibesorganisation so zusammenfaßt, daß aus dieser Zusammenfassung das Be­wußtsein",
      "entspringt, durch welches die äußere Wirklich­keit in Vorstellungen vergegenwärtigt wird. Die Vorstel­lungen sieht der Anthropologe aus dem menschlichen Or­ganismus entspringen. Indem er dieses beobachtet, muß er in einem gewissen Sinne Halt machen.",
      "Einen inneren ge­setzmäßigen Zusammenhang des Vorstellens kann er nicht mit der bloßen Anthropologie erfassen. Wie die Anthro­posophie am Ende ihres in geistigen Erfahrungen verlaufenden Weges noch hinblickt auf das geistige Wesen des Menschen, insofern dieses durch die Wahrnehmungen der Sinne sich offenbart, so muß die Anthropologie, wenn sie am Ende ihres im Sinnesgebiete verlaufenden Weges ist, hinblicken nach der Art, wie sich der Sinnesmensch vorstellend an den Sinneswahrnehmungen betätigt.",
      "Und in­dem sie dieses beobachtet, findet sie diese Betätigung nicht von den Gesetzen des Leibeslebens, sondern von den Denkgesetzen der Logik getragen. Die Logik aber ist kein Gebiet, das auf dieselbe Art betreten werden kann, wie die anderen Gebiete der Anthropologie.",
      "In dem von Logik beherrschten Denken walten Gesetze, die nicht mehr als diejenigen der Leibesorganisation zu kennzeichnen sind. Indem sich der Mensch in ihnen betätigt, offenbart sich in ihm dasselbe Wesen, welches die Anthroposophie am En­de ihres Weges angetroffen hat.",
      "Nur sieht der Anthropo­loge dieses Wesen so, wie es von der Sinnesseite her be­leuchtet ist. Er sieht die abgemähten Vorstellungen und gibt, indem er eine Logik zugesteht, auch das zu, daß in den Vorstellungen Gesetze aus einer Welt walten, die sich mit der sinnlichen wohl zur Einheit zusammenschließt, jedoch mit ihr nicht zusammenfällt.",
      "In dem von dem logi­schen Wesen getragenen Vorstellungsleben offenbart sich",
      "dem Anthropologen der in die Geisteswelt hineinragende Sinnesmensch. Die Anthropologie kommt auf diesem We­ge zu einer Philosophie über den Menschen, als einem letz­ten Ergebnisse ihrer Forschungen. Was auf ihrem Wege vorher liegt, befindet sich rein im Sinnesgebiete.*",
      "Sind die beiden Wege, der anthroposophische und der anthropologische, in rechtmäßiger Art durchwandelt, so treffen sie in einem Punkte zusammen. Die Anthroposo­phie bringt bei diesem Zusammentreffen das Bild des lebendigen Geistmenschen mit und zeigt, wie dieser durch das Sinnensein das zwischen Geburt und Tod bestehende Bewußtsein entwickelt, indem das übersinnliche Bewußt­seinsleben abgelähmt wird. Die Anthropologie zeigt bei dem Begegnen das Bild des im Bewußtsein sich selbst erfassenden Sinnesmenschen, der aber aufragend in das gei­stige Dasein in dem Wesen lebt, das über Geburt und Tod hinaus liegt. Bei diesem Zusammentreffen ist eine wirklich fruchtbare Verständigung zwischen Anthroposophie und Anthropologie möglich. Diese muß eintreten, wenn beide sich zur Philosophie über den Menschen fortbilden. Die aus der Anthroposophie hervorgegangene Philosophie über den Menschen wird zwar ein Bild desselben liefern, das mit ganz andern Mitteln gemalt ist als dasjenige, wel­ches die vom Menschen handelnde, aus der Anthropolo­gie hervorgegangene Philosophie gibt; aber die Betrachter der beiden Bilder werden sich mit ihren Vorstellungen in ähnlicher Übereinstimmung befinden können wie das negative",
      "* Ebenso wie die Gedanken auf Seite 19 finden auch die oben angedeu­teten nach einer gewissen Richtung hin noch eine Beleuchtung durch die im 1. Kapitel der am Ende dieser Schrift gegebenen «Skizzenhaften Erwei­terungen des Inhaltes ...»: «Die philosophische Rechtfertigung der Anthro­posophie.»",
      "Plattenbild des Photographen bei entsprechender Behandlung mit der positiven Photographie.",
      "Es scheint mit diesen Ausführungen gezeigt zu sein, in welchem Sinne die im Beginne dieser Schrift angedeutete Frage über die Möglichkeit einer fruchtbaren Diskussion zwischen Anthropologie und Anthroposophie ganz be­sonders vom anthroposophischen Gesichtspunkte aus be­jahend zu beantworten ist."
    ],
    "sentences": [
      [
        "Max Dessoirs Buch «Vom Jenseits der Seele» enthält einen kurzen Abschnitt, in dem die von mir vertretene anthro­posophisch orientierte Geisteswissenschaft als wissen­schaftlich unberechtigt gekennzeichnet werden soll.* Nun könnte es manchem scheinen, als ob eine Diskussion mit Persönlichkeiten, welche auf dem wissenschaftlichen Ge­sichtspunkte Dessoirs stehen, für den Vertreter der geisteswissenschaftlichen Anthroposophie unter allen Umständen unfruchtbar sein müsse.",
        "Denn der letztere muß ein rein geistiges Erfahrungsgebiet behaupten, das der erstere grundsätzlich ablehnt und in den Bereich der Phantasiegebilde verweist.",
        "Man könne also über die in Betracht kom­menden geisteswissenschaftlichen Erkenntnisse nur mit jemand sprechen, der von vorneherein Gründe zu haben glaubt dafür, daß das gemeinte geisteswissenschaftliche Gebiet eine Wirklichkeit ist. - Diese Ansicht wäre richtig, wenn der Vertreter der Anthroposophie nichts anderes vorbrächte als seine inneren persönlichen Erlebnisse, und diese sich einfach neben die Ergebnisse der auf Sinnes­beobachtung und wissenschaftliche Verarbeitung dieser Beobachtung begründeten Wissenschaft hinstellten.",
        "Dann könnte man sagen: der Bekenner der so gekennzeichneten"
      ],
      [
        "* Vergleiche Max Dessoir: «Vom Jenseits der Seele», die Geheimwissen­schaften in kritischer Betrachtung.",
        "Der im besonderen über Anthroposophie handelnde Abschnitt umfaßt die Seiten 254-263."
      ],
      [
        "Wissenschaft lehne es eben ab, die Erlebnisse des Erfor­schers des Geistgebietes als Wirklichkeiten anzusehen, und dieser könne mit dem von ihm Vorgebrachten nur auf sol­che Persönlichkeiten Eindruck machen, die von vorne­herein sich auf seinen Gesichtspunkt stellen."
      ],
      [
        "Nun beruht aber diese Meinung doch nur auf einer mißverständlichen Auffassung dessen, was von mir Anthro­posophie genannt wird.",
        "Richtig ist, daß diese Anthroposo­phie auf seelischen Erfahrungen beruht, die unabhängig von den Eindrücken der Sinneswelt und auch unabhängig von den wissenschaftlichen Urteilen gewonnen werden, die nur auf die Sinneseindrücke sich stützen.",
        "Es muß also zugegeben werden, daß beide Arten von Erfahrungen zu­nächst wie durch eine unübersteigliche Kluft geschieden scheinen. - Doch dieses entspricht nicht der Wahrheit.",
        "Es gibt ein gemeinsames Gebiet, auf dem sich beide For­schungsrichtungen begegnen müssen, und auf dem eine Diskussion möglich ist über dasjenige, was von der einen und der anderen vorgebracht wird.",
        "Dies gemeinsame Ge­biet läßt sich auf die folgende Art kennzeichnen."
      ],
      [
        "Der Vertreter der Anthroposophie glaubt aus Erfahrun­gen heraus, die nicht nur seine persönlichen Erlebnisse sind, behaupten zu dürfen, daß die menschlichen Erkenntnisvorgange von dem Punkte an weiter entwickelt werden können, bei dem derjenige Forscher halt macht, der sich nur auf Sinnesbeobachtung und Verstandesurteil über die­se Sinnesbeobachtung stützen will.",
        "Ich möchte in dem Fol­genden, um fortwährenden langatmigen Umschreibungen zu entgehen, die auf Sinnesbeobachtung und verstandesge­mäße Bearbeitung der Sinnesbeobachtung gestützte Wis­senschaftsrichtung Anthropologie nennen und bitte den"
      ],
      [
        "Leser, mir diesen nicht gewöhnlichen Gebrauch dieses Ausdruckes zu gestatten.",
        "Er soll in den folgenden Ausführungen nur für das hier Gekennzeichnete angewendet wer­den.",
        "In diesem Sinne meint Anthroposophie mit ihrer For­schung da beginnen zu können, wo Anthropologie auf­hört.*"
      ],
      [
        "Der Vertreter der Anthropologie bleibt dabei stehen, die in der Seele erlebbaren Verstandesbegriffe auf die Sin­neserlebnisse zu beziehen.",
        "Der Vertreter der Anthroposo­phie macht die Erfahrung, daß diese Begriffe, abgesehen davon, daß sie auf die Sinneseindrücke bezogen werden sollen, noch ein eigenes Leben für sich in der Seele entfal­ten können.",
        "Und daß sie, indem sie dieses Leben innerhalb der Seele entfalten, in dieser selbst eine Entwickelung zu­stande bringen.",
        "Er wird sich bewußt, wie die Seele, wenn sie auf diese Entwickelung die notwendige Aufmerksam­keit wendet, innerhalb ihres Wesens die Entdeckung macht, daß sich in ihr Geistorgane offenbaren. (Ich gebrau­che diesen Ausdruck «Geistorgane», indem ich erweiternd den Sprachgebrauch aufnehme, dem Goethe aus seiner"
      ],
      [
        "* Obgleich dasjenige, was von mir als «Anthroposophie» vertreten wird, in seinen Ergebnissen auf einem ganz anderen Boden steht als die Ausführungen Robert Zimmermanns in seinem 188 1 erschienenen Buche «Anthroposophie», so glaube ich doch den von Zimmermann gekenn­zeichneten Begriff des Unterschiedes von Anthroposophie und Anthropo­logie gebrauchen zu dürfen.",
        "Zimmermann faßt aber als den Inhalt seiner «Anthroposophie» nur die von der Anthropologie gelieferten Begriffe in ein abstraktes Schema.",
        "Ihm liegt das erkennende Schauen, auf dem die von mir gemeinte Anthroposophie ruht, nicht im Bereiche der wissenschaftli­chen Forschungswege.",
        "Seine Anthroposophie unterscheidet sich von der Anthropologie nur dadurch, daß die erstere die von der letzteren erhaltenen Begriffe erst einem dem Herbartschen Philosophieren ähnlichen Verfahren unterwirft, bevor sie dieselben zum Inhalte ihres rein verstandesmäßigen Ideen-Schemas macht."
      ],
      [
        "Weltanschauung heraus gefolgt ist, als er die Ausdrücke «Geistes-Augen», «Geistes-Ohren » anwandte.)* Solche Geistorgane stellen dann für die Seele Bildungen dar, die für sie ähnlich gedacht werden dürfen wie die Sinnesorga­ne für den Leib.",
        "Selbstverständlich dürfen sie nur seelisch gedacht werden.",
        "Jeder Versuch, sie mit irgendeiner leibli­chen Bildung zusammenzubringen, muß von der Anthro­posophie strengstens abgelehnt werden.",
        "Sie muß ihre Geistorgane so vorstellen, daß sie in keiner Weise aus dem Bereich des Seelischen heraustreten und in das Gefüge des Leiblichen übergreifen.",
        "Ihr gilt ein solches Übergreifen als krankhafte Bildung, die sie aus ihrem Bereich streng ausschließt.",
        "Die Art, wie innerhalb der Anthroposophie über die Entwickelung der Geistorgane gedacht wird, sollte für denjenigen, der sich über diese Art wirklich unterrichtet, ein genügend starker Beweis sein dafür, daß über abnorme Seelenerlebnisse, über Illusionen, Visionen, Halluzinatio­nen usw. für den Erforscher des wirklichen Geistgebietes keine anderen Vorstellungen vorhanden sind als die auch innerhalb der Anthropologie berechtigten.** Eine Ver­wechselung der anthroposophischen Ergebnisse mit ab­normen sogenannten Seelenerlebnissen beruht immer auf Mißverständnis oder ungenügender Kenntnis des in der Anthroposophie Gemeinten.",
        "Auch kann derjenige, der"
      ],
      [
        "* Eine ausführlichere Darstellung und Rechtfertigung dieser Vorstel­lung von «Geistorganen» findet man in meinem Buche «Vom Menschen­rätsel» Seite 146 ff. und in meinen auf Goethes Weltanschauung bezüglichen Schriften."
      ],
      [
        "** Die inneren Erlebnisse, welche von der Seele durchzumachen sind, um zu dem Gehrauch ihrer Geistorgane zu kommen, findet man in einer Reihe meiner Schriften geschildert, besonders in meinem Buche: «Wie er­langt man Erkenntnisse der höheren Welten?» und im zweiten Teile meiner «Geheimwissenschaft»."
      ],
      [
        "einsichtsvoll verfolgt, wie Anthroposophie den Weg zur Entwickelung der Geistorgane darstellt, gewiß nicht auf die Meinung verfallen, dieser Weg könne zu krankhaften Bildungen oder Zuständen führen.",
        "Der Einsichtsvolle sollte vielmehr erkennen, daß alle Stufen des seelischen Er­fahrens, welche der Mensch im Sinne der Anthroposophie auf dem Wege zur Geist-Anschauung erlebt, in einem Ge­biete liegen, das ganz nur seelisch ist, und neben dem das Erleben der Sinne und die gewöhnliche Verstandestätig­keit unverändert so verlaufen, wie sie vor der Entstehung dieses Gebietes verlaufen sind."
      ],
      [
        "Daß gerade in bezug auf diese Seite der anthroposophischen Erkenntnis viele Mißverständnisse herrschen, rührt davon her, daß es manchen Menschen Schwierigkeiten bereitet, ein rein Seelisches in den Bereich ihrer Aufmerksamkeit zu ziehen.",
        "Solche Men­schen werden sogleich verlassen von der Kraft ihres Vorstellen, wenn dieses nicht gestützt ist durch den Hinblick auf sinnlich Wahrnehmbares."
      ],
      [
        "Es dämpft sich dann deren Vorstellungskraft herunter selbst unter das Maß von Stär­ke, die im Träumen herrscht, bis zu jenem niedrigen Gra­de, der für das Vorstellen im traumlosen Schlafe vorhan­den ist, und der nicht mehr bewußt wird.",
        "Man kann sagen, solche Menschen sind in ihrem Bewußtsein erfüllt von den Nachwirkungen oder der unmittelbaren Wirkung der Sin­nes-Eindrücke, und es geht neben diesem Erfüllt-Sein ein Verschlafen alles dessen einher, das als Seelisches erkannt würde, wenn es erfaßt werden könnte."
      ],
      [
        "Man kann sogar sagen, daß das Seelische in seiner Eigenart deshalb von vielen Menschen dem schärfsten Mißverständnis ausge­setzt wird, nur weil sie gegenüber demselben nicht in der gleichen Art aufwachen können wie gegenüber dem sinnlichen"
      ],
      [
        "Inhalt des Bewußtseins.",
        "Daß Menschen mit nur den­jenigen Aufmerksamkeitsgraden, welche das gewöhnliche äußere Leben bewirkt, In solcher Lage sind, braucht nie­mand in Verwunderung zu versetzen, der im rechten Lich­te zum Beispiel zu sehen vermag, welche Lehre aus einem Vorwürfe zu ziehen ist, den Franz Brentano dem Philoso­phen William James mit Bezug auf diese Sache machen muß."
      ],
      [
        "Brentano schreibt, daß man «zwischen der empfin­denden Tätigkeit und dem, worauf sie gerichtet ist, also zwischen Empfinden und Empfundenem, zu unterschei­den» habe («und sie sind so sicher verschieden als mein gegenwärtiges Mich-Erinnern und das Ereignis, das mir dabei als vergangen vorschwebt, oder, um einen noch dra­stischeren Vergleich anzuwenden, mein Haß eines Feindes und der Gegenstand dieses Hasses verschieden sind») und er macht dazu die Bemerkung, daß man den Irrtum, gegen den sich diese Worte richten, «da und dort auftauchen» sehe.",
        "Er sagt weiter: «Unter anderen hat William James ihn sich eigen gemacht, und auf dem Internationalen Kon­greß für Psychologie, Rom 1905, in längerer Rede zu be­gründen versucht."
      ],
      [
        "Weil mir, wenn ich in einen Saal blicke, zugleich mit dem Saal auch mein Sehen erscheint; weil fer­ner Phantasiebilder von sinnlichen Gegenständen sich von objektiv erregten Sinnesbildern derselben nur graduell un­terscheiden; weil endlich Körper von uns schön genannt werden, der Unterschied von Schön und Häßlich aber zu dem Unterschiede von Gemütsbewegungen in Beziehung steht: so sollen psychisches und physisches Phänomen nicht mehr als zwei Klassen von Erscheinungen gelten. - Es ist mir schwer verständlich, wie sich dem Redner selbst die Schwäche dieser Argumente nicht fühlbar gemacht hat."
      ],
      [
        "Zugleich erscheinen heißt nicht als dasselbe erscheinen, wie zugleich sein nicht so viel ist als dasselbe sein.",
        "Und darum konnte Descartes ohne Widerspruch empfehlen, zu­nächst wenigstens zu leugnen, daß der Saal, den ich sehe, sei, und nur daran, daß das Sehen des Saales sei, als an et­was Unzweifelhaftem festzuhalten."
      ],
      [
        "Ist aber das erste Argu­ment hinfällig, dann offenbar auch das zweite; denn was verschlüge es, wenn ein Phantasieren von einem Sehen sich nur durch den Intensitätsgrad unterschiede, da, selbst wenn auch dieser ausgeglichen wäre, die volle Gleichheit des Phantasierens mit dem Sehen nach eben dem Gesagten nur die Gleichheit mit einem psychischen Phänomen be­deuten würde?",
        "Im dritten Argument wird von Schönheit gesprochen ..."
      ],
      [
        "Es ist nun aber gewiß eine seltsame Logik, welche daraus, daß» das Wohlgefallen am Schönen «etwas Psychisches ist, schließen will, daß auch das, an dessen Er­scheinung es geknüpft ist, etwas Psychisches sein müsse.",
        "Wäre dies richtig, so wäre auch jedes Mißfallen identisch mit dem, woran einer ein Mißfallen hat, und man müßte sich wohl hüten, einen begangenen Fehler zu bereuen, da in dieser mit ihm identischen Reue der Fehltritt selbst sich wiederholen würde. - Bei solcher Lage der Dinge dürfte es denn doch nicht wohl zu fürchten sein, daß die Autori­tät von James, der sich leider unter den deutschen Psycho­logen die eines Mach gesellt, viele dazu verleiten werde, die augenfälligsten Unterschiede zu verkennen. »* Jedenfalls ist diese «Verkennung der augenfälligsten Unterschie­de» keine seltene Tatsache."
      ],
      [
        "Und sie beruht darauf, daß die Kraft des Vorstellens die nötige Aufmerksamkeit nur für"
      ],
      [
        "* Vergleiche Franz Brentano: «Untersuchungen zur Sinnespsychologie» (Leipzig, 1907), Seite 96 f."
      ],
      [
        "den Sinneseindruck entfalten kann, während das eigentlich Seelische, das dabei vorgeht, dem Bewußtsein sich nicht stärker vergegenwärtigt als das im Zustand des Schlafes Erlebte.",
        "Man hat es mit zwei Strömungen von Erlebnissen zu tun, von denen die eine wachend erfaßt, die andere aber"
      ],
      [
        "- die seelische - gleichzeitig nur mit einer der abgeschwäch­ten Vorstellungskraft des Schlafes gleichkommenden, also fast mit gar keiner Aufmerksamkeit ergriffen wird.",
        "Es darf eben durchaus nicht außer acht gelassen werden, daß wäh­rend des gewöhnlichen Wachzustandes des Menschen die seelische Verfassung des Schlafes nicht einfach aufhört, sondern neben dem Wachen fortdauert, und daß das ei­gentlich Seelische nur dann in den Bereich des Wahrneh­mens tritt, wenn der Mensch nicht bloß für die Sinneswelt erwacht, wie dies im gewöhnlichen Bewußtsein stattfindet, sondern auch für das seelische Dasein, wie das im schauenden Bewußtsein der Fall ist.",
        "Ob nun durch das im Wachen fortdauernde Schlafen für das Seelische dieses letztere - im grob materialistischen Sinne - geleugnet wird, oder ob, weil es nicht gesehen, mit dem Physischen zusammenge­worfen wird, wie im Falle James', ist fast gleichgiltig; die Ergebnisse sind fast die gleichen: beides führt zu verhäng­nisvollen Kurzsichtigkeiten.",
        "Nicht verwunderlich aber ist, daß so oft das Seelische unwahrnehmbar bleibt, wenn selbst ein Philosoph wie W.",
        "James es nicht in richtiger Art von dem Physischen zu scheiden vermag.*"
      ],
      [
        "Wer so wenig wie W.",
        "James das wesentlich Seelenhafte von den durch die Sinne erlebten Seelen-Inhalten abson­dern"
      ],
      [
        "* Genaueres über dieses Erwachen derjenigen seelischen Fähigkeiten, welche im gewöhnlichen Bewußtsein unerwacht sind, findet man in meinem Buche «Vom Menschenrätsel» Seite 156 ff."
      ],
      [
        "kann, mit dem läßt sich schwer sprechen von demje­nigen Gebiete im Seelendasein, innerhalb dessen die Ent­wickelung der Geistorgane beobachtet werden soll.",
        "Denn diese Entwickelung geht eben dort vor sich, wohin sich seine Aufmerksamkeit nicht zu wenden vermag.",
        "Sie führt von dem verstandesmäßigen zum schauenden Erkennen.* Nun ist aber durch die Fähigkeit, das wesenhaft Seeli­sche wahrzunehmen, noch nichts weiter erreicht, als eine allererste Vorbedingung, die es möglich macht, den geisti­gen Blick dahin zu lenken, wo die Anthroposophie die Entwickelung der Seelenorgane sucht.",
        "Denn, was sich zu­nächst diesem Blicke darbietet, das verhält sich zu dem, wovon Anthroposophie als von dem mit Geistorganen ausgerüsteten Seelenwesen spricht, wie eine undifferen­zierte lebendige Zelle zu einem mit Sinnesorganen ausge­statteten Lebewesen.",
        "Die einzelnen Geistorgane selbst aber werden nur in dem Maße der Seele als ihr Besitz bewußt, in dem sie dieselben zu gebrauchen vermag.",
        "Denn diese Organe sind nicht etwas Ruhendes; sie sind in fortwähren­der Beweglichkeit.",
        "Und wenn sie nicht im Gebrauche sind, kann man sich auch ihres Vorhandenseins nicht bewußt sein.",
        "Für sie fällt also Wahrnehmen und im Gebrauche Stehen zusammen.",
        "Wie die Entwickelung dieser Organe und damit auch ihre Wahrnehmbarkeit zutage tritt, das fin­det man in meinen anthroposophischen Schriften geschil­dert.",
        "Ich will hier nur auf einiges in dieser Richtung Lie­gendes hinweisen."
      ],
      [
        "* Eine noch weiter gehende Begründung dieser Ausführungen findet man in den am Schlusse stehenden «Skizzenhaften Erweiterungen des In­haltes dieser Schrift»: «I.",
        "Die philosophische Rechtfertigung der Anthro­posophie.»"
      ],
      [
        "Wer sich dem Nachdenken über die durch die Sinnes-Erscheinungen bewirkten Erlebnisse hingibt, der stößt überall auf Fragen, zu deren Beantwortung ihm dieses Nachdenken zunächst unzulänglich erscheint.",
        "Im Verfolg solchen Nachdenkens kommen die Vertreter der Anthro­pologie zur Festlegung von Erkenntnisgrenzen."
      ],
      [
        "Es braucht nur daran erinnert zu werden, wie Du Bois-Reymond in seiner Rede über die Grenzen des Naturerkennens davon spricht, daß man nicht wissen könne, welches das Wesen der Materie ist, und welches dasjenige der einfachsten Be­wußtseinserscheinung.",
        "Man kann nun an solchen Punkten des Nachdenkens stehen bleiben und sich der Meinung hingeben: da liegen eben für den Menschen unübersteig­liche Erkenntnisschranken."
      ],
      [
        "Und man kann demgemäß sich dabei beruhigen, daß der Mensch nur innerhalb des von diesen Schranken umschlossenen Gebietes ein Wissen er­langen könne und darüber hinaus nur ein Ahnen, Fühlen, Hoffen, Wünschen möglich sei, mit denen eine «Wissen­schaft» nichts zu tun haben könne. - Oder man kann in diesem Punkte anheben, Hypothesen auszubilden über ein Gebiet, das über das Sinnlich-Wahrnehmbare hinausliegt.",
        "Man bedient sich in einem solchen Falle des Verstandes, von dem man glaubt, daß er seine Urteile über ein Gebiet ausdehnen dürfe, von dem die Sinne nichts wahrnehmen."
      ],
      [
        "Man wird sich mit einem solchen Verfahren der Gefahr aussetzen, daß der in dieser Beziehung Ungläubige erwi­dert, der Verstand habe keine Berechtigung, über eine Wirklichkeit zu urteilen, für die ihm die Grundlage der Sinneswahrnehmungen entzogen ist.",
        "Denn diese allein gä­ben seinen Urteilen einen Inhalt."
      ],
      [
        "Ohne einen solchen In­halt blieben seine Begriffe leer."
      ],
      [
        "Die anthroposophisch orientierte Geisteswissenschaft verhält sich nicht in der einen und nicht in der andern die­ser beiden Arten zu den «Erkenntnisgrenzen».",
        "In der zweiten nicht, weil sie mit denjenigen der gleichen Ansicht sein muß, welche empfinden, daß man gewissermaßen allen Boden für das Nachdenken verliert, wenn man die Vor­stellungen so beläßt, wie man sie an den Sinneswahrneh­mungen gewonnen hat, und sie doch über dieses Gebiet hinaus anwenden will. - In der ersten Art nicht, weil sie gewahr wird, daß sich an den sogenannten Grenzen des Erkennens etwas seelisch erleben läßt, das mit dem aus der Sinneswahrnehmung gewonnenen Vorstellungs-Inhalt nichts zu tun hat."
      ],
      [
        "Wenn die Seele nur diesen Inhalt sich ver­gegenwärtigt, dann muß sie bei wahrer Selbstbesinnung sich sagen: dieser Inhalt kann unmittelbar nicht etwas an­deres dem Erkennen offenbaren als eine Nachbildung des sinnlich Erlebten.",
        "Anders wird die Sache, wenn die Seele dazu übergeht, sich zu fragen: was läßt sich in ihr selbst erfahren, wenn sie mit solchen Vorstellungen sich erfüllt, zu denen sie an den gewöhnlichen Erkenntnisgrenzen ge­führt wird?"
      ],
      [
        "Sie kann sich dann bei entsprechender Selbst­besinnung sagen: erkennen im gewöhnlichen Sinne kann ich mit solchen Vorstellungen nichts; aber in dem Falle, in dem ich mir diese Ohnmacht des Erkennens recht innerlich anschaulich mache, werde ich gewahr, wie diese Vorstel­lungen in mir selbst wirken.",
        "Als gewöhnliche Erkenntnis­vorstellungen bleiben sie stumm; aber in eben dem Maße, als sich ihre Stummheit dem Bewußtsein immer mehr mit­teilt, gewinnen sie ein eigenes inneres Leben, das mit dem Leben der Seele eine Einheit wird."
      ],
      [
        "Und die Seele bemerkt dann, wie sie mit diesem Erleben in einer Lage ist, die sich"
      ],
      [
        "etwa mit der Lage eines blinden Wesens vergleichen läßt, das auch noch keine besondere Ausbildung seines Tast­sinnes erfahren hat.",
        "Ein solches Wesen würde zunächst überall hin anstoßen.",
        "Es würde den Widerstand der äuße­ren Wirklichkeiten empfinden.",
        "Und aus dieser allgemeinen Empfindung könnte sich ein inneres Leben entwickeln, er­füllt von einem primitiven Bewußtsein, das nicht mehr bloß die allgemeine Empfindung hat: ich stoße an Dinge, sondern das diese Empfindung in sich vermannigfaltigt und Härte von Weichheit, Glätte von Rauhigkeit usw. un­terscheidet. - In dieser Art kann die Seele das Erlebnis in sich erfahren und vermannigfaltigen, das sie mit den an den Erkenntnisgrenzen gebildeten Vorstellungen hat.",
        "Sie lernt erfahren, daß diese Grenzen nichts anderes darstellen als dasjenige, was entsteht, wenn sie von der geistigen Welt seelisch berührt wird.",
        "Das Gewahrwerden solcher Gren­zen wird der Seele zu einem Erlebnis, das sich vergleichen läßt mit dem Tast-Erlebnis auf dem sinnlichen Gebiete.* Was sie vorher als Grenze des Erkennens bezeichnet hat, in dem sieht sie nunmehr die geistig-seelische Berührung durch eine geistige Welt.",
        "Und aus dem besonnenen Erle­ben, das sie mit den verschiedenen Grenzvorstellungen ha­ben kann, besondert sich ihr die allgemeine Empfindung einer geistigen Welt zu einem mannigfaltigen Wahrneh­men derselben.",
        "Auf solche Art wird die gewissermaßen"
      ],
      [
        "* Erkenntnisgrenzen wie die oben besprochenen treten nicht bloß in der geringen Zahl auf, in der sie manchem zum Bewußtsein kommen; sie erge­ben sich in großer Menge auf den Wegen, die das Nachdenken durch sein inneres Wesen einschlagen muß, um in ein Verhältnis zur wahren Wirklich­keit zu kommen.",
        "Man vergleiche dazu in dem letzten Abschnitt «Skizzen­hafte Erweiterungen des Inhaltes dieser Schrift» das Kapitel: «Das Auftre­ten der Erkenntnisgrenzen.»"
      ],
      [
        "niedrigste Art der Wahrnehmbarkeit der geistigen Welt zum Erlebnis.",
        "Es ist damit nur das erste Aufschließen der Seele für die geistige Welt gekennzeichnet.",
        "Aber es ist auch gezeigt, daß in demjenigen, was die von mir gemeinte An­throposophie als geistige Erlebnisse anstrebt, nicht auf all­gemeine nebulose gefühlsmäßige Selbsterlebnisse der Seele gedeutet wird, sondern auf etwas, das in gesetzmäßiger Art in einem wirklichen inneren Erleben entwickelt wird.",
        "Es kann hier nicht der Ort sein, zu zeigen, wie die erste primitive Geist-Wahrnehmung durch weitere seelische Verrichtungen gesteigert wird, so daß, wie von einem gei­stig-seelischen Tasten, auch von anderen gewissermaßen höheren Wahrnehmungsarten gesprochen werden kann.",
        "Es muß bezüglich der Schilderung solcher seelischer Ver­richtungen auf meine anthroposophischen Bücher und Aufsätze verwiesen werden.",
        "Hier sollte nur das Prinzipielle angedeutet werden über die geistige Wahrnehmung, von welcher die Anthroposophie spricht."
      ],
      [
        "Durch einen Vergleich möchte ich noch veranschauli­chen, wie anders das ganze Verhalten der Seele innerhalb der anthroposophischen Geistes-Erforschung ist als in der Anthropologie.",
        "Man stelle sich eine Anzahl von Weizen­körnern vor.",
        "Man kann diese als Nahrungsmittel verwen­den.",
        "Man kann sie aber auch in die Erde setzen, sodaß sich andere Weizenpflanzen aus ihnen entwickeln.",
        "Man kann Vorstellungen, die man durch die Sinnes-Erlebnisse ge­wonnen hat, so im Bewußtsein halten, daß man in ihnen das Nachbilden der sinnenfälligen Wirklichkeit erlebt.",
        "Und man kann sie auch so erleben, daß man die Kraft in der Seele wirksam sein läßt, die sie in derselben durch das­jenige ausüben, was sie sind, abgesehen davon, daß sie ein"
      ],
      [
        "Sinnliches abbilden.",
        "Die erste Wirkungsweise der Vorstel­lungen in der Seele läßt sich vergleichen mit dem, was durch die Weizenkörner wird, wenn sie als Nahrungsmittel von einem Lebewesen aufgenommen werden.",
        "Die zweite mit der Hervorbringung einer neuen Weizenpflanze durch jedes Samenkorn. - Der Vergleich darf allerdings nur so gedacht werden, daß man berücksichtigt: aus dem Samenkorn wird eine der Vorfahren-Pflanze ähnliche; aus der in der Seele wirksamen Vorstellung wird innerhalb der Seele eine der Bildung von Geistorganen dienliche Kraft.",
        "Und berücksichtigt muß auch werden, daß das erste Bewußt­sein solcher inneren Kräfte nur an so stark wirksamen Vor­stellungen entzündet werden kann, wie es die gekennzeich­neten Grenzvorstellungen sind, daß aber, wenn dieses Be­wußtsein für solche Kräfte einmal erwacht ist, ihm in aller­dings geringerem Maße auch andere Vorstellungen dienst­bar sein können, um den eingeschlagenen Weg weiter zu gehen."
      ],
      [
        "Zugleich weist dieser Vergleich auf etwas hin, das sich der anthroposophischen Forschung über das Wesen des Vorstellungslebens ergibt.",
        "Wie das Samenkorn, wenn es zum Nahrungsmittel verarbeitet wird, aus derjenigen Ent­wickelungsströmung herausgehoben wird, die in seiner ur­eigenen Wesenheit liegt und zur Bildung einer neuen Pflan­ze führt, so wird die Vorstellung aus der ihr wesentlichen Entwickelungsrichtung abgelenkt, wenn sie von der vorstellenden Seele zur Nachbildung einer Sinneswahrneh­mung verwendet wird.",
        "Die der Vorstellung durch ihr eige­nes Wesen entsprechende Entwickelung ist die, in der Ent­wickelung der Seele als Kraft zu wirken.",
        "Ebenso wie man die der Pflanze eigenen Entwickelungsgesetze nicht findet,"
      ],
      [
        "wenn man die Samen auf ihren Nahrungswert hin unter­sucht, ebenso wenig findet man das Wesen der Vorstel­lung, wenn man untersucht, inwiefern sie die nachbildende Erkenntnis der durch sie vermittelten Wirklichkeit hervor­bringt.",
        "Es soll damit nicht gesagt sein, daß diese Untersu­chung nicht angestellt werden könnte.",
        "Sie kann dies eben­so, wie diejenige über den Nahrungswert der Pflanzensa­men.",
        "Aber wie man durch das letztere sich über etwas an­deres auf klärt als über die Entwickelungsgesetze des Pflan­zenwachstums, so erlangt man durch eine Erkenntnistheo­rie, welche die Vorstellungen auf ihren nachbildenden Er­kenntniswert hin prüft, über etwas anderes Aufschluß als über das Wesen des Vorstellungslebens.",
        "So wenig das Sa­menkorn es in seinem Wesen vorgezeichnet hat, Nahrung zu werden, so wenig liegt es im Wesen der Vorstellung, nachbildende Erkenntnis zu liefern.",
        "Ja, man kann sagen, wie die Verwendung als Nahrungsmittel etwas für das Sa­menkorn ganz Äußerliches ist, so ist es das erkenntnismäßige Nachbilden für die Vorstellungen.",
        "In Wahrheit er­greift in den Vorstellungen die Seele ihr eigenes sich ent­wickelndes Wesen.",
        "Und erst durch die eigene Tätigkeit der Seele geschieht es, daß die Vorstellungen zu Vermittlern der Erkenntnis einer Wirklichkeit werden.*"
      ],
      [
        "Die Frage nun, wie die Vorstellungen zu solchen Er­kenntnisvermittlern werden, muß die anthroposophische Beobachtung, welche sich der Geistorgane bedient, anders beantworten als die Erkenntnistheorien es tun, welche diese"
      ],
      [
        "* Eine ausführlichere Begründung der in obigem gegebenen Gedanken findet man in dem letzten Abschnitt des 2.",
        "Bandes meiner «Rätsel der Philo­sophie»: «Skizzenhaft dargestellter Ausblick auf eine Anthroposophie»"
      ],
      [
        "(Seiten 594-627)."
      ],
      [
        "Beobachtung ablehnen.",
        "Für diese anthroposophische Be­obachtung ergibt sich das Folgende."
      ],
      [
        "So wie die Vorstellungen ihrem ureigenen Wesen nach sind, bilden sie zwar einen Teil des Lebens der Seele; aber sie können nicht in der Seele bewußt werden, so lange diese nicht ihre Geistorgane bewußt gebraucht.",
        "Sie bleiben, so lange sie ihrem Eigenwesen nach lebendig sind, in der Seele unbewußt.",
        "Die Seele lebt durch sie, aber sie kann nichts von ihnen wissen.",
        "Sie müssen ihr eigenes Leben her­abdämpfen, um bewußte Seelenerlebnisse des gewöhnli­chen Bewußtseins zu werden.",
        "Diese Herabdämpfung ge­schieht durch jede sinnliche Wahrnehmung.",
        "So kommt, wenn die Seele einen Sinneseindruck empfängt, eine Her­ablähmung des Vorstellungslebens zustande; und die her­abgelähmte Vorstellung erlebt die Seele bewußt als den Vermittler einer Erkenntnis der äußeren Wirklichkeit.* Alle Vorstellungen, die von der Seele auf eine äußere Sin­nes-Wirklichkeit bezogen werden, sind innere Geist-Er­lebnisse, deren Leben herabgedämpft ist.",
        "In allem, das man über eine äußere Sinneswelt denkt, hat man es mit den erstatteten Vorstellungen zu tun.",
        "Nun geht aber das Vorstel­lungsleben nicht etwa verloren, sondern es führt sein Da­sein, getrennt von dem Gebiete des Bewußtseins, in den nicht bewußten Sphären der Seele.",
        "Und da wird es von den Geistorganen wiedergefunden.",
        "So wie nun die abgetöteten Vorstellungen von der Seele auf die Sinneswelt bezogen werden können, so die mit den Geistorganen erfaßten le­bendigen Vorstellungen auf die Geisteswelt. - Die oben"
      ],
      [
        "* Man vergleiche damit den 3.",
        "Abschnitt der am Schlusse dieser Schrift gegebenen «Skizzenhaften Erweiterungen des Inhaltes ...»: «Von der Ab­straktheit der Begriffe.»"
      ],
      [
        "gekennzeichneten Grenzvorstellungen sind diejenigen, die sich durch ihre eigene Wesenheit nicht ablähmen lassen, daher widerstreben sie einer Beziehung zur Sinnes-Wirk­lichkeit.",
        "Eben dadurch werden sie zu Ausgangspunkten der Geistwahrnehmung."
      ],
      [
        "Vorstellungen, die als lebendige von der Seele erfaßt werden, habe ich in meinen anthroposophischen Schriften imaginative Vorstellungen genannt.",
        "Man verkennt, was hier als «imaginativ» gemeint ist, wenn man es verwech­selt mit der bildlichen Ausdrucksform, die angewendet wer­den muß, um solche Vorstellungen entsprechend anzudeu­ten.",
        "Was da wirklich mit «imaginativ» gemeint ist, kann etwa in der folgenden Art verdeutlicht werden.",
        "Wenn je­mand eine Sinneswahrnehmung hat, während ihn der äu­ßere Gegenstand beeindruckt, dann hat die Wahrnehmung für ihn eine gewisse innere Stärke.",
        "Wenn er sich von dem Gegenstande abwendet, dann kann er sich in einer bloßen Innenvorstellung denselben vergegenwärtigen.",
        "Aber die Vorstellung hat nur eine geringere innere Stärke.",
        "Sie ist im Verhältnis zu der bei Anwesenheit des äußeren Gegenstan­des wirksamen Vorstellung gewissermaßen schattenhaft.",
        "Wenn der Mensch für das gewöhnliche Bewußtsein schattenhaft in seiner Seele vorhandene Vorstellungen beleben will, so durchtränkt er sie mit Nachklängen an die Sinnesanschauung.",
        "Er macht die Vorstellung zum anschaulichen Bilde.",
        "Solche Bildvorstellungen sind nun gewiß nichts an­deres als Ergebnisse aus dem Zusammenwirken des Vor­stellens und des Sinneslebens.",
        "Die «imaginativen» Vor­stellungen der Anthroposophie entstehen durchaus nicht in dieser Art.",
        "Die Seele muß, um sie zustande zu bringen, so genau den inneren Vorgang der Vereinigung von Vorstellungsleben"
      ],
      [
        "und Sinnes-Eindruck kennen, daß sie das Einfließen der Sinneseindrücke, beziehungsweise ihrer Nacherlebnisse, in das Vorstellungsleben ganz fern halten kann.",
        "Man bringt die Fernhaltung der Sinnes-Nach-Erleb­nisse nur zustande, wenn man kennen gelernt hat, wie das Vorstellen von diesen Nacherlebnissen ergriffen wird."
      ],
      [
        "Erst dann ist man in der Lage, die Geistorgane lebendig zu ver­binden mit dem Wesen des Vorstellens und dadurch die Eindrücke der geistigen Wirklichkeit zu empfangen.",
        "Es wird dabei das Vorstellungsleben von einer ganz anderen Seite her durchdrungen als im Sinneswahrnehmen."
      ],
      [
        "Die Er­lebnisse, die man dabei hat, sind wesentlich andere als die an den Sinneswahrnehmungen zu erfahrenden.",
        "Und doch gibt es eine Möglichkeit, über diese Erlebnisse sich auszu­drücken.",
        "Das kann in folgender Art geschehen. - Wenn der Mensch die Farbe Gelb wahrnimmt, so hat er in seiner Seele nicht bloß das Augenerlebnis, sondern ein gefühls­artiges Mit-Erlebnis der Seele."
      ],
      [
        "Dieses kann für verschie­dene Menschen eine verschiedene Stärke haben, ganz feh­len wird es niemals.",
        "Goethe hat in dem schönen Kapitel seiner Farbenlehre über «sinnlich-sittliche Wirkung der Farben» die Gefühls-Nebenwirkungen für Rot, Gelb, Grün usw. sehr eindringlich beschrieben."
      ],
      [
        "Nimmt nun die Seele aus einem gewissen Gebiete des Geistes etwas wahr, so kann der Fall eintreten, daß diese geistige Wahrnehmung in ihr dasselbe gefühlsmäßige Neben-Erlebnis hat, das bei der sinnlichen Wahrnehmung des Gelb auftritt.",
        "Man weiß dann, daß man dieses oder jenes geistige Erlebnis hat."
      ],
      [
        "Man hat dabei natürlich nicht in der Vorstellung dasselbe vor sich, was man in der sinnlichen Wahrnehmung der gelben Farbe vor sich hat.",
        "Aber man hat dasselbe Innenerlebnis"
      ],
      [
        "als gefühlsmäßige Nebenwirkung, das man hat, wenn die gelbe Farbe vor dem Auge ist.",
        "Man sagt dann: man nehme das Geist-Erlebnis als «gelb» wahr.",
        "Vielleicht könnte man, um sich genauer auszudrücken, immer sagen: man nimmt etwas wahr, was wie «gelb» für die Seele ist.",
        "Doch sollte niemand einer so umständlichen Redeweise bedürfen, der aus der anthroposophlschen Literatur den Vorgang ken­nen gelernt hat, welcher zur geistigen Wahrnehmung führt.",
        "Diese Literatur macht genugsam darauf aufmerk­sam, daß das der Geistwahrnehmung zugängliche Wesenhafte nicht so vor dem Geistorgane steht wie ein verdünn­ter sinnlicher Gegenstand oder Vorgang, oder so, daß es wiedergegeben werden könnte durch Vorstellungen, die in gewöhnlicher Bedeutung sinnlich-anschauliche sind.*"
      ],
      [
        "Wie die geistige Welt, die außerhalb des Menschen liegt, so lernt die Seele durch ihre Geistorgane das geistige Wesen des Menschen selbst kennen.",
        "Anthroposophie beobachtet dieses geistige Wesen als Glied der geistigen Welt.",
        "Sie schreitet von der Beobachtung eines Teiles der geistigen Welt fort zu solchen Vorstellungen über den Menschen, welche ihr vergegenwärtigen, was sich im Menschenleibe als geistiger Mensch offenbart.",
        "Die Anthropologie schrei­tet, von der entgegengesetzten Richtung kommend, eben­falls zu Vorstellungen fort über das menschliche Wesen.",
        "Bildet die Anthroposophie die in obigen Ausführungen"
      ],
      [
        "* Eine weitere Beleuchtung findet das zuletzt hier Ausgesprochene durch das 4.",
        "Kapitel der am Schlusse dieser Schrift gegebenen «Skizzenhaf­ten Erweiterungen des Inhaltes ...»: «Ein wichtiges Merkmal der Geistwahrnehmung.»"
      ],
      [
        "gekennzeichneten Beobachtungsarten aus, dann gelangt sie zu Anschauungen über das geistige Wesen des Men­schen, welches sich in der Sinneswelt in dem Leibe offen­bart.",
        "Die Blüte dieser Offenbarung ist das Bewußtsein, das die Sinneseindrücke in dem Vorstellungsdasein weiter be­stehen läßt.",
        "Indem die Anthroposophie fortschreitet von den Erlebnissen der außermenschlichen geistigen Welt bis zum Menschen, findet sie denselben zuletzt als im Sinnesleibe lebend, und in demselben das Bewußtsein von der sinnlichen Wirklichkeit entwickelnd.",
        "Das letzte, was sie auf ihrem Wege von dem Menschen findet, ist das leben­dige Vorstellungswesen der Seele, das sie in zusammen­hängenden imaginativen Vorstellungen auszudrücken ver­mag.",
        "Dann kann sie noch, gewissermaßen am Ende ihres geisterforschenden Weges, den Blick weiter gebrauchend, schauen, wie sich das wesenhafte Vorstellungsleben durch die wahrnehmenden Sinne ablähmt.",
        "In diesem abgelähm­ten Vorstellungsleben hat sie, von der Geistseite her be­leuchtet, den in der Sinneswelt lebenden Menschen, inso­fern er ein vorstellender ist, gekennzeichnet.",
        "Sie kommt auf diese Art zu einer Philosophie über den Menschen, als einem letzten Ergebnisse ihrer Forschungen.",
        "Was auf ih­rem Wege vorher liegt, befindet sich rein im Geistgebiete.",
        "Sie kommt mit dem, was sich ihr auf ihrem Geisteswege ergeben hat, bei einer Kennzeichnung des in der Sinneswelt lebenden Menschen an."
      ],
      [
        "Die Anthropologie erforscht die Reiche der Sinneswelt.",
        "Sie gelangt auf ihrem Wege fortschreitend ebenfalls bis zum Menschen.",
        "Es stellt sich ihr derselbe dar, wie er die Tatsachen der Sinneswelt in seiner Leibesorganisation so zusammenfaßt, daß aus dieser Zusammenfassung das Be­wußtsein"
      ],
      [
        "entspringt, durch welches die äußere Wirklich­keit in Vorstellungen vergegenwärtigt wird.",
        "Die Vorstel­lungen sieht der Anthropologe aus dem menschlichen Or­ganismus entspringen.",
        "Indem er dieses beobachtet, muß er in einem gewissen Sinne Halt machen."
      ],
      [
        "Einen inneren ge­setzmäßigen Zusammenhang des Vorstellens kann er nicht mit der bloßen Anthropologie erfassen.",
        "Wie die Anthro­posophie am Ende ihres in geistigen Erfahrungen verlaufenden Weges noch hinblickt auf das geistige Wesen des Menschen, insofern dieses durch die Wahrnehmungen der Sinne sich offenbart, so muß die Anthropologie, wenn sie am Ende ihres im Sinnesgebiete verlaufenden Weges ist, hinblicken nach der Art, wie sich der Sinnesmensch vorstellend an den Sinneswahrnehmungen betätigt."
      ],
      [
        "Und in­dem sie dieses beobachtet, findet sie diese Betätigung nicht von den Gesetzen des Leibeslebens, sondern von den Denkgesetzen der Logik getragen.",
        "Die Logik aber ist kein Gebiet, das auf dieselbe Art betreten werden kann, wie die anderen Gebiete der Anthropologie."
      ],
      [
        "In dem von Logik beherrschten Denken walten Gesetze, die nicht mehr als diejenigen der Leibesorganisation zu kennzeichnen sind.",
        "Indem sich der Mensch in ihnen betätigt, offenbart sich in ihm dasselbe Wesen, welches die Anthroposophie am En­de ihres Weges angetroffen hat."
      ],
      [
        "Nur sieht der Anthropo­loge dieses Wesen so, wie es von der Sinnesseite her be­leuchtet ist.",
        "Er sieht die abgemähten Vorstellungen und gibt, indem er eine Logik zugesteht, auch das zu, daß in den Vorstellungen Gesetze aus einer Welt walten, die sich mit der sinnlichen wohl zur Einheit zusammenschließt, jedoch mit ihr nicht zusammenfällt."
      ],
      [
        "In dem von dem logi­schen Wesen getragenen Vorstellungsleben offenbart sich"
      ],
      [
        "dem Anthropologen der in die Geisteswelt hineinragende Sinnesmensch.",
        "Die Anthropologie kommt auf diesem We­ge zu einer Philosophie über den Menschen, als einem letz­ten Ergebnisse ihrer Forschungen.",
        "Was auf ihrem Wege vorher liegt, befindet sich rein im Sinnesgebiete.*"
      ],
      [
        "Sind die beiden Wege, der anthroposophische und der anthropologische, in rechtmäßiger Art durchwandelt, so treffen sie in einem Punkte zusammen.",
        "Die Anthroposo­phie bringt bei diesem Zusammentreffen das Bild des lebendigen Geistmenschen mit und zeigt, wie dieser durch das Sinnensein das zwischen Geburt und Tod bestehende Bewußtsein entwickelt, indem das übersinnliche Bewußt­seinsleben abgelähmt wird.",
        "Die Anthropologie zeigt bei dem Begegnen das Bild des im Bewußtsein sich selbst erfassenden Sinnesmenschen, der aber aufragend in das gei­stige Dasein in dem Wesen lebt, das über Geburt und Tod hinaus liegt.",
        "Bei diesem Zusammentreffen ist eine wirklich fruchtbare Verständigung zwischen Anthroposophie und Anthropologie möglich.",
        "Diese muß eintreten, wenn beide sich zur Philosophie über den Menschen fortbilden.",
        "Die aus der Anthroposophie hervorgegangene Philosophie über den Menschen wird zwar ein Bild desselben liefern, das mit ganz andern Mitteln gemalt ist als dasjenige, wel­ches die vom Menschen handelnde, aus der Anthropolo­gie hervorgegangene Philosophie gibt; aber die Betrachter der beiden Bilder werden sich mit ihren Vorstellungen in ähnlicher Übereinstimmung befinden können wie das negative"
      ],
      [
        "* Ebenso wie die Gedanken auf Seite 19 finden auch die oben angedeu­teten nach einer gewissen Richtung hin noch eine Beleuchtung durch die im 1.",
        "Kapitel der am Ende dieser Schrift gegebenen «Skizzenhaften Erwei­terungen des Inhaltes ...»: «Die philosophische Rechtfertigung der Anthro­posophie.»"
      ],
      [
        "Plattenbild des Photographen bei entsprechender Behandlung mit der positiven Photographie."
      ],
      [
        "Es scheint mit diesen Ausführungen gezeigt zu sein, in welchem Sinne die im Beginne dieser Schrift angedeutete Frage über die Möglichkeit einer fruchtbaren Diskussion zwischen Anthropologie und Anthroposophie ganz be­sonders vom anthroposophischen Gesichtspunkte aus be­jahend zu beantworten ist."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "II MAX DESSOIR ÜBER ANTHROPOSOPHIE",
    "paragraphs": [
      "Aus den hier vorangehenden Darstellungen ist wohl ersicht­lich, wie erwünscht dem Vertreter der Anthroposophie eine sachliche Auseinandersetzung mit dem Anthropologen sein kann. Es wäre denkbar, daß sich an ein Buch, das solche Absichten verfolgt wie das Max Dessoirs, eine derartige Ausein­andersetzung anknüpfen ließe. Vom Gesichtspunkte der An­throposophie ist dieses Buch im Sinne der anthropologischen Wissenschaft abgefaßt. Es stützt sich auf die Ergebnisse der Sinnesbeobachtung und will diejenige Denkungsart und die­jenigen Forschungsmittel zur Geltung bringen, welche in der naturwissenschaftlichen Erkenntnisströmung im Ge­brauch sind. Das Buch ist, im Sinne der hier gemachten Ausführungen, der anthropologischen Wissenschaft zugehörig.",
      "In dem «Anthroposophie» überschriebenen Abschnitt seines Buches will Max Dessoir eine Kritik liefern der in meinen Schriften dargestellten anthroposophischen An­schauungen.* Er versucht, verschiedene Ausführungen die­ser Schriften in seiner Art wiederzugeben und daran seine kritischen Bemerkungen zu knüpfen. Das also könnte dazu führen, zu beobachten, was von den beiden Vorstellungs­kreisen für diesen oder jenen Punkt des Erkenntnisstrebens gesagt werden kann.",
      "*    Seiten 254 des Buches «Vom Jenseits der Seele», die Geheimwis­senschaften in kritischer Betrachtung von Max Dessoir. Verlag von Ferdi­nand Enke in Stuttgart, 1917.",
      "Ich will daraufhin die Ausführungen Max Dessoirs hier zur Darstellung und Besprechung bringen. - Dessoir will darauf hinweisen, daß von mir die Ansicht vertreten wird, die menschliche Seele könne es dahin bringen, durch innere Entwickelung sich ihrer Geistorgane zu bedienen, und sich dadurch zu einer Geisteswelt in ähnlicher Art in Beziehung setzen, wie sie dies durch die leiblichen Sinne zur sinnlichen tut. Man kann aus den vorangehenden Darlegungen dieser meiner Schrift ersehen, wie ich dasjenige denke, was in der Seele vorgehen muß, damit sie zur Anschauung des geistigen Lebens komme.",
      "Max Dessoir stellt in seiner Art dar, was ich in dieser Beziehung in meinen Schriften dargelegt habe. Er sagt darüber: «Durch solche Innenarbeit erreicht die Seele das, was von aller Philosophie erstrebt wird.",
      "Frei­lich muß das leibfreie Bewußtsein vor der Verwechslung mit traumhaftem Hellsehen und hypnotischen Vorgängen behütet werden. Wenn unsere Seelenkräfte gesteigert sind, kann das Ich sich oberhalb des Bewußtseins erleben, gleich­sam in einer Verdichtung und Verselbständigung des Gei­stigen, ja, es kann schon bei der Wahrnehmung von Farben und Tönen die Vermittelung des Leibes aus dem Erlebnis ausschließen.» Zu diesen seinen Sätzen fügt dann Dessoir die Anmerkung hinzu: «Es lohnt nicht, diese Behauptun­gen im einzelnen zu widerlegen.»* Dessoir bringt also meine Anschauung von geistiger Wahrnehmung damit zu­sammen, daß ich behaupte, man könne bei der Wahrneh­mung von Farben und Tönen die Vermittelung des Leibes ausschließen.",
      "Der Leser fasse ins Auge, was ich in den vor angehenden Darlegungen über die Erlebnisse gesagt habe, welche die Seele durch ihre Geistorgane macht, und wie sie",
      "* Vergleiche Seite 255 des genannten Buches.",
      "dazu kommt, sich über diese Erlebnisse in Farben- und Ton­bildern auszudrücken. Er wird dann ersehen, daß ich vom Gesichtspunkte der Anthroposophie nichts Törichteres be­haupten könnte, als die Seele könne «bei der Wahrnehmung von Farben und Tönen die Vermittelung des Leibes aus­schließen». Brächte ich eine solche Behauptung vor, so wäre allerdings richtig, zu sagen, es lohne «nicht, diese Be­hauptung im einzelnen zu widerlegen». Man steht da vor einer wirklich merkwürdigen Tatsache. Max Dessoir be­hauptet, daß ich etwas sage, was nach meinen eigenen Vor­aussetzungen von mir als töricht bezeichnet werden muß. Mit einer solchen gegnerischen Einwendung ist nun aller­dings eine Auseinandersetzung unmöglich. Man kann nur feststellen, welch ein Zerrbild dahingestellt und für die An­schauung dessen ausgegeben wird, den man bekämpfen will.",
      "Nun könnte vielleicht Dessoir einwenden: so klar, wie ich die Konsequenzen meiner Anschauungen in bezug auf den eben berührten Punkt in dem vorangehenden Kapitel dieser Schrift ausgedrückt habe, finde er sie in meinen frü­heren Schriften nicht dargestellt. Ich werde ohne weiteres zugeben, daß mit Bezug auf manche Punkte der Anthropo­sophie in späteren von mir gegebenen Darlegungen eine ge­nauere Ausführung von früher Gebotenem zu finden ist, und daß der Leser meiner früheren Schriften vielleicht da oder dort zu einer irrigen Ansicht darüber kommen kann, was ich selbst in einem gewissen Punkte für die richtige Konsequenz meiner Anschauungen notwendig halte. Ich glaube, daß dieses jeder Einsichtige für selbstverständlich halten muß. Denn Anthroposophie ist ein weites Arbeits­feld, und Veröffentlichungen können immer nur einzelne Teilgebiete umfassen.",
      "Aber kann in diesem Falle sich Max Dessoir darauf beru­fen, daß in meinen früheren Schriften der oben berührte Punkt keine Aufhellung gefunden habe? Dessoirs Buch ist 1917 erschienen. Ich habe in der fünften Auflage meiner Schrift «Wie erlangt man Erkenntnisse der höheren Wel­ten», welche 1914 erschienen ist, zu der Stelle, die über die bildhafte Darstellung geistiger Erlebnisse durch Farben handelt, die folgende Bemerkung gemacht: «Man muß bei allen folgenden Schilderungen darauf achten, daß zum Bei­spiel beim  einer Farbe geistiges Sehen (Schauen) ge­meint ist. Wenn die hellsichtige Erkenntnis davon spricht: , so bedeutet dies: . Nur weil es der hellsichtigen Erkenntnis in einem solchen Falle ganz naturgemäß ist, zu sagen: , wird dieser Ausdruck angewandt. Wer dies nicht bedenkt, kann leicht eine Far­benvision mit einem wahrhaft hellsichtigen Erlebnis ver­wechseln.»* Ich habe diese Bemerkung gemacht, nicht weil ich glaube, daß jemand, der meine früheren Darlegungen mit wahrem Verständnisse liest, zu der Meinung kommen könne, ich behaupte, man könne Farben ohne Augen sehen, sondern weil ich mir denken konnte, es möchte da oder dort jemand bei flüchtigem Lesen durch Mißverstand mir eine sol­che Behauptung unterschieben, wenn ich nicht ausdrück­lich sage, daß ich sie für unberechtigt halte. Drei Jahre spä­ter, nachdem ich diese Unterschiebung ausdrücklich abge­wehrt habe, kommt Max Dessoir und erzählt, ich behaupte, was ich in Wirklichkeit für töricht halte.",
      "* Vergleiche meine Schrift «Wie erlangt man Erkenntnisse der höheren Welten?» (19. Auflage , Seite 111, Anmerkung.",
      "Doch damit nicht genug. In der sechsten Auflage meines Buches «Theosophie », die ebenfalls 1914 erschienen ist, findet sich über die besprochene Sache das Folgende: « Man kann zu der Vorstellung kommen, als ob dasjenige, was hier als geschildert wird, vor der Seele so stünde, wie eine physische Farbe vor dem Auge steht.",
      "Eine solche wäre aber nichts als eine Halluzination. Mit Eindrücken, die sind, hat die Geisteswis­senschaft nicht das geringste zu tun. Und sie sind jedenfalls in der hier vorliegenden Schilderung nicht gemeint.",
      "Man kommt zu einer richtigen Vorstellung, wenn man sich das Folgende gegenwärtig hält. Die Seele erlebt an einer phy­sischen Farbe nicht nur den sinnlichen Eindruck, sondern sie hat an ihr ein seelisches Erlebnis.",
      "Dieses seelische Er­lebnis ist ein anderes, wenn die Seele - durch das Auge - eine gelbe, ein anderes, wenn sie eine blaue Farbe wahr­nimmt. Man nenne dieses Erlebnis das oder das . Die Seele nun, welche den Er­kenntmmispfad betreten hat, hat ein gleiches gegenüber den aktiven Seelenerlebnissen anderer Wesen; ein gegenüber den hinge­bungsvollen Seelenstimmungen.",
      "Das Wesentliche ist nicht, daß der bei einer Vorstellung einer ande­ren Seele so sieht, wie er dies in der phy­sischen Welt sieht, sondern daß er ein Erlebnis hat, das ihn berechtigt, die Vorstellung zu nennen, wie der physische Mensch einen Vorhang zum Beispiel nennt. Und weiter ist es wesentlich, daß der sich be­wußt ist, mit diesem seinem Erlebnis in einem leibfreien Er­leben zu stehen, so daß er die Möglichkeit empfängt, von dem Werte und der Bedeutung des Seelenlebens in einer",
      "Welt zu sprechen, deren Wahrnehmung nicht durch den menschlichen Leib vermittelt ist.»*",
      "Ich verzichte darauf, noch anderes aus meinen Schriften anzuführen, das in der berührten Sache meine wirkliche Ansicht darstellen kann. Und ich überlasse es jedem Leser, der noch ein sachliches Urteil über Tatsachen auch dann sich bil­den kann, wenn von Anthroposophie die Rede ist, - zu be­urteilen, was über die «Wiedergabe» meiner Darstellung durch Max Dessoir zu denken ist.",
      "Auf den Grad des Verständnisses, welchen Dessoir der von mir versuchten Schilderung des durch Geistorgane er­langten Bewußtseins entgegenbringt, wirft ein recht ver­hängnisvolles Licht, was er im weiteren seiner Darstellung über die Beziehung der «imaginativen» Vorstellung zu ei­ner ihnen entsprechenden geistigen Wirklichkeit vorbringt. Er hat vernommen, daß Anthroposophie die Entwickelung des Menschentums auf der Erde nicht allein mit den Mitteln erklärt, welche in der Anthropologie angewendet werden, sondern daß sie durch ihre Mittel diese Entwickelung in Abhängigkeit von geistigen Kräften und Wesenheiten er­schaut. In meinem Buche « Geheimwissenschaft im Umriß» habe ich versucht, diesen menschlichen Entwickelungsvor­gang anschaulich zu machen durch «imaginative» Vorstel­lungen (übrigens auch durch Erkennmisarten, die über das",
      "*    Vergleiche meine «Theosophie». Einführung in übersinnliche Welterkenntnis und Menschenbestimmung (28.Auflage 1955, Seite 154). In mei­nem Buche «Die Geheimwissenschaft im Umriß», das 1913 in 5. Auflage erschienen ist, steht eine ebensolche Ausführung über das Schauen von Far­ben auf Seite 421 f. (26. Auflage 1955, Seite 418 f.). Nun liegt das schier Un­glaubliche vor, daß Max Dessoir diese 5. Auflage auf Seite 254 seines Buches als eine der Schriften anführt, die er benützt haben will. Er behauptet also, daß jeh etwas sage, wovon in meinem von ihm selbst zitierten Buch das genaue Gegenteil steht.",
      "imaginative Anschauen hinausliegen, was aber für das hier zu Besprechende weniger in Betracht kommt). Ich habe in dem genannten Buche angedeutet, wie sich dem anthropo­sophischen Anschauen ein Bild ergibt von den Zuständen, welche die Menschheit durchlebt hat in Entwickelungsfor­men, die den gegenwärtigen schon nahe stehen, und ich habe auch hingewiesen auf solche ältere Entwickelungsfor­men, in denen der Mensch in einer Art auftritt, welche der gegenwärtigen sehr unähnlich ist, und die nicht durch die dem sinnlichen Wahrnehmen entlehnten Vorstellungen der Anthropologie, sondern durch imaginative Vorstellungen von mir geschildert werden. - Dessoir unterrichtet nun seine Leser über dasjenige, was ich über die Menschheitsentwickelung ausgeführt habe, in der folgenden Art.",
      "Meine Darstellung der Entwickelungsformen, welche der gegen­wärtigen Menschenbildung noch nahe stehen, gibt er so an , daß ich für eine bestimmte Zeitperiode in der Vergangen­heit eine altindische Kultur der Menschheit annehme und dann andere Kulturperioden darauf folgen lasse. Bei Dossier heißt es: «Alt-Indien ist nicht das jetzige Indien, wie denn überhaupt alle geographischen, astronomischen, hi­storischen Bezeichnungen sinnbildlich zu verstehen sind.",
      "Auf die indische Kultur folgte die urpersische, geführt von Zarathustra, der aber viel früher lebte als die in der Ge­schichte diesen Namen tragende Persönlichkeit. Andere Zeitabschnitte schlossen sich an.",
      "Wir stehen in der sechsten Periode.»* - Was ich über eine viel ältere Zeit der Mensch­heitsentwickelung sage, in der diese noch in Formen zutage trat, die den gegenwärtigen sehr unähnlich sind, darüber berichtet Dessoir so: «Dieser Mensch hat sich herausgebil­det",
      "*    Vergleiche Seite 258 f. des Dessoirschen Buches.",
      "in einer urfernen Vergangenheit, die Steiner das lemu­rische Zeitalter der Erde nennt - warum wohl? -, und in ei­nem Lande, das damals zwischen Australien und Indien lag (was also eine richtige Ortsbestimmung und kein Symbol ist).»* - Ich will nun hier ganz davon absehen, daß ich diese «Wiedergaben» des von mir Dargestellten auch im ganzen nur als Zerrbilder ansehen kann, die völlig unge­eignet sind, irgend einem Leser ein Bild von dem zu ge­ben, was ich meine. Ich will nur über einen Punkt dieser «Wiedergaben» sprechen. Dessoir ruft in seinem Leser den Glauben hervor, ich spreche davon, daß das im Geiste Geschaute sinnbildlich (symbolisch) zu verstehen sei, daß also Alt-Indien, wohin ich eine alte Menschheitskultur ver­lege, ein « symbolisches Land» sei. Später findet er es ta­delnswert, daß ich eine viel ältere menschliche Entwicke­lungsperiode nach Lemurien - zwischen Australien und Indien - verlege und dabei mir selbst in grausamer Weise widerspreche, da man doch aus meiner Darstellung mer­ken könne, daß ich Lemurien für eine richtige Ortsbestim­mung und kein Symbol halte.",
      "Es ist durchaus zuzugeben, daß ein Leser des Dessoir­schen Buches, der nichts von mir gelesen hat, und bloß Des­soirs Bericht entgegennimmt, zu der Ansicht kommen muß, meine Darstellung sei ganz undurchdachtes, verworrenes und in sich selbst widerspruchsvolles Zeug. - Was steht aber über das von mir als Alt-Indien gekennzeichnete Er­dengebiet wirklich in meinem Buche? Man lese die betreffen­den Ausführungen nach, und man wird finden, daß ich mit vollkommener Deutlichkeit zum Ausdruck bringe, wie Alt-Indien kein Symbol, sondern das Erdgebiet ist, das,",
      "*    Vergleiche Seite 261 des Dessoirschen Buches.",
      "wenn auch nicht ganz genau, so doch im wesentlichen mit dem zusammenfällt, das jedermann Indien nennt.* Dessoir berichtet also seinem Leser als meine Ansicht et­was, was mir auch nie eingefallen ist, vorzustellen. Und weil er findet, daß ich bei der Schilderung vom alten Le­murien wohl so spreche, wie es mit meiner wirklichen Mei­nung vom alten Indien zusammenstimmt, nicht aber mit dem Unsinn, den er mich sagen läßt, zeiht er mich des Wi­derspruches.**",
      "Man fragt sich, wie kommt das Unglaubliche zustande , daß mich Dessoir behaupten läßt, Alt-Indien sei «sinnbild­lich» zu verstehen. Mir ergibt sich darüber aus dem ganzen Zusammenhange seiner Darstellung das Folgende. Dessoir hat etwas gelesen über die Vorgänge im Seelenleben, die ich kennzeichne als den Weg zum geistigen Schauen, dessen erste Stufe das imaginative Erkennen ist. Ich schildere da, wie die Seele durch ruhige Hingabe an gewisse Gedanken aus ihren Untergründen die Fähigkeit heraus entwickelt, imaginative Vorstellungen zu bilden. Ich sage, zu diesem Ziele ruhe die Seele am besten in sinnbildlichen Vorstellun­gen. Niemand sollte durch meine Darstellung auf den Irr­tum verfallen, die sinnbildlichen Vorstellungen seien etwas anderes als das Mittel, um zum imaginativen Erkennen zu kommen. Dessoir meint nun, weil man mittels Sinnbildern zum imaginativen Vorstellen kommt, bestehe dies letztere auch nur in Sinnbildern, ja er schreibt mir die Ansicht zu , wer sich seiner Geistorgane bedient, schaue nicht durch die",
      "* Vergleiche meine «Geheimwissenschaft im Umriß», 26. Auflage, Stuttgart, 1955, Seite 275 f.",
      "** Vergleiche meine «Geheimwissenschaft im Umriß», 26. Auflage, Seite 259.",
      "imaginativen Vorstellungen auf Wirklichkeiten, sondern nur auf Sinnbilder.",
      "Meiner Darlegung gegenüber ist die Dessoirsche Be­hauptung, ich weise in solchen Fällen wie beim alten Indien auf Sinnbilder hin, nicht auf Wirklichkeiten, nur mit dem Folgenden zu vergleichen. Jemand findet aus der Beschaf­fenheit eines Stückes Erdboden, daß es in der Gegend, in der er sich befindet, vor kurzer Zeit geregnet haben müsse. Er teilt das einem anderen mit. Er kann diesem selbstver­ständlich nur seine Vorstellung davon mitteilen, daß es ge­regnet hat. Deshalb behauptet ein Dritter, der Erste sage, die Beschaffenheit des Erdbodens rühre nicht von einem wirklichen Regen her, sondern von der Vorstellung des Regens. Ich behaupte weder, daß die imaginativen Vorstellun­gen in bloßen Sinnbildern sich erschöpfen, noch daß sie selbst eine Wirklichkeit sind, sondern daß sie sich auf eine Wirklichkeit beziehen, wie das bei den Vorstellungen des gewöhnlichen Bewußtseins auch der Fall ist. Und mir un­terstellen, ich weise nur auf sinnbildliche Wirklichkeiten hin, kommt gleich der Behauptung, der Naturforscher sehe nicht in dem Wesenhaften, auf das er sich durch seine Vor­stellung bezieht, sondern in diesen selbst die Wirklichkeit.",
      "Wenn man Anschauungen, die man bekämpfen will, so darstellt, wie dies durch Dessoir geschieht, so ist der Kampf recht leicht. Und Max Dessoir macht es sich wirklich leicht, sich mit vornehmer Art auf den kritischen Richterstuhl zu setzen; aber er erreicht dies nur dadurch, daß er meine Dar­legung erst in ein Zerrbild, ja oft in eine völlige Torheit ver­kehrt, und dann diese seine eigene Schöpfung abkanzelt. Er sagt: «Es ist widerspruchsvoll, daß aus  und nur  gemeinten Sachverhalten die Tatbestände",
      "der Wirklichkeit sich entwickelt haben sollen.»* Doch ist solch widerspruchsvolle Art des Vorstellens bei mir nir­gends zu finden. Daß meine Darstellung sie enthält, ist eine Unterschiebung Dessoirs. Und wenn dieser gar sich zu der Behauptung versteigt: «Denn nicht darum handelt es sich , ob man das Geistige als Gehirntätigkeit ansieht oder nicht, sondern darum, ob das Geistige in den Formen kindlicher Vorstellungsweise oder als ein Reich eigener Gesetzmäßig­keit zu denken ist, »** so muß darauf erwidert werden: Ich bin mit ihm ganz einverstanden, daß sich alles das, was er seinen Lesern als meine Meinung auftischt, in den Formen kindlicher Vorstellungsweise hält; doch hat das von ihm also Bezeichnete nichts mit meinen wirklichen Ansichten zu tun, sondern bezieht sich restlos auf seine eigenen Vorstel­lungen, die er sich, die meinigen entstellend, gebildet hat.",
      "Wie ist es nur möglich, daß ein Gelehrter so verfährt? Ich muß, um etwas für eine Antwort auf diese Frage zu tun, den Leser für kurze Zeit in ein Gebiet führen, das diesem viel­leicht nicht kurzweilig erscheinen wird, das ich aber hier be­treten muß, um zu zeigen, auf welche Art Max Dessoir die Bü­cher liest, über die er sich zum Kritiker aufwirft. Ich muß ge­genüber den Dessoirschen Ausführungen ein wenig Philo­logie dem Leser vorführen.",
      "Meine Entwickelung der menschlichen Kulturperioden in einer gewissen Zeit schildert Dessoir, wie schon erwähnt , so: «Auf die indische Kultur folgte die urpersische ... An­dere Zeitabschnitte schlossen sich an. Wir stehen in der sechsten Periode. »*** Nun könnte es recht unbedeutend erscheinen,",
      "* Vergleiche Seite 263 des Dessoirschcn Buches.",
      "**    Seite 263 des Dessoirschen Buches.",
      "***    Vergleiche Seite 258 f. des Dessoirschen Buches.",
      "jemand vorzuwerfen, er lasse mich sagen: «Wir stehen in der sechsten Periode», während ich mit aller nur denkbaren Klarheit ausführe, daß wir in der fünften stehen. Aber in diesem Falle ist die Sache doch nicht unbedeutend.",
      "Denn wer in den ganzen Geist meiner diesbezüglichen Dar­stellung eingedrungen ist, der muß zugeben, daß jemand, dem auch nur beifällt, ich rede von der sechsten Periode als der gegenwärtigen, meine ganze Auseinandersetzung in der allergröbsten Weise mißverstanden hat. Daß ich die gegen­wärtige Periode als die fünfte bezeichne, hängt ganz inner­lich mit dem diesbezüglich von mir Auseinandergesetzten zusammen. - Wie kommt Dessoir zu seinem groben Mißverständnis?",
      "Man kann sich darüber eine Vorstellung bil­den , wenn man meine Darstellung der Sache mit seiner «Wiedergabe» vergleicht und dabei etwas nach philologi­scher Methode prüfend zu Werke geht. - Da, wo ich in mei­ner Schilderung der Kulturperioden zu der vierten komme, die ich im achten Jahrhundert v. Chr. beginnen und etwa im vierzehnten oder fünfzehnten Jahrhundert n.",
      "Chr. schließen lasse, sage ich das Folgende: «Im vierten, fünften und sech­sten Jahrhundert n. Chr. bereitete sich in Europa ein Kul­turzeitalter vor, in welchem die Gegenwart noch lebt. Es sollte das vierte, das griechlsch4ateinische allmählich ablö­sen.",
      "Es ist das fünfte nachatlantische Kulturzeitalter.»* Meine Meinung ist demnach, daß durch die Vorgänge im vierten, fünften und sechsten Jahrhundert sich Wirkungen vorbereiteten, die zu ihrem Ausreifen noch einige Jahrhun­derte brauchten, um dann im vierzehnten Jahrhundert den Übergang zum fünften Kulturzeitalter zu machen, in dem wir gegenwärtig noch leben. Die obige Stelle scheint nun",
      "* Vergleiche meine «Geheimwissenschaft im Umriß», Seite 294 f.",
      "Max Dessoir obenhin lesend so in den Bereich seiner Auf­merksamkeit hineingebracht zu haben, daß er die Aufeinan­derfolge des vierten, fünften und sechsten Jahrhunderts mit der Aufeinanderfolge der Kulturzeitalter verwechselt hat. Wenn jemand oberflächlich liest und außerdem kein Verständnis für das Gelesene hat, so kann dergleichen geschehen.",
      "Ich würde nicht ohne weiteres diese Hypothese von der Oberflächlichkeit Max Dessoirs hier aussprechen, wenn sie nicht gestützt würde durch die folgenden Entdeckungen, die man an der «Wiedergabe» meiner Anschauungen durch ihn machen kann. Ich muß, um die in Betracht kommenden Dinge zu besprechen, Vorstellungen anführen, die Erkennt­nisse der Anthroposophie betreffen, deren Verständnis kaum möglich ist, wenn sie nicht im Zusammenhang mit den zu ihnen weisenden Ausführungen meiner «Geheimwissenschaft» ins Auge gefaßt werden. Ich selbst würde sie niemals so aus allem Zusammenhang herausgerissen, einem Leser oder Zuhörer vorführen, wie dies Max Dessoit tut. Allein da er seine Kritik auf seine «Wiedergabe» der bei mir in einem weit ausholenden Zusammenhange dargestellten Ansichten begründet, muß ich hier auf diese «Wiedergabe» zu sprechen kommen. Ich muß daran zeigen, welcher Art diese «Wiedergabe » ist. Voraus bemerken muß ich, daß die Darstellung solcher Dinge deshalb grolle Schwierigkeiten macht, weil der Inhalt der geistigen Beobachtung nur dann einigermaßen klargestellt werden kann, wenn man sich ei­ner möglichst genauen Ausdrucksart befleißigt. Ich versu­che daher stets, wenn ich solche Dinge darstelle, keinen Zeitaufwand zu scheuen, um der sprachlichen Ausdrucks­form soviel als mir möglich ist, an Genauigkeit abzugewin­nen. Wer nur ein wenig in den Geist der Anthroposophie eindringt,",
      "wird Verständnis für das haben, was ich eben gesagt habe. - Demgegenüber will ich nun zeigen, wie Max Dessoir bei seiner «Wiedergabe» meiner Darstellungen verfährt.*",
      "Mit Bezug auf den Weg, den die Seele zur Erlangung des Gebrauchs der Geistorgane macht, stellt er meine An­schauung in der folgenden Art dar: « Die Schulung zur höheren Bewußtseinsverfassung beginnt - wenigstens für den Menschen der Gegenwart - damit, daß man mit aller Kraft sich in eine Vorstellung als in einen rein seelischen Tatbestand versenkt. Am besten eignet sich eine sinnbild­liche Vorstellung, etwa die eines schwarzen Kreuzes (Sym­bol",
      "* Es darf vielleicht hier auf etwas hingewiesen werden, das in den Krei­sen, in denen man oft die anthroposophischen Versuche auf ihren philoso­phisch-wissenschaftlichen Wert hin beurteilen will, nicht ins Auge gefaßt wird. Ich möchte diesen Hinweis schon aus dem Grunde nicht unterlassen, weil bei einigen leicht der Glaube entstehen könnte, meine gegen Dessoir vorgebrachten Darlegungen seien gar zu sehr ein pedantisches Pochen auf meinen Wortlaut.",
      "In der Anthroposophie hat man es zu tun mit Darstellun­gen des Geistigen. Man muß sich dabei der Worte, ja der Wortfügungen der gewöhnlichen Sprache bedienen. Man kann in diesen aber durchaus nicht immer adäquate Bezeichnungen finden für dasjenige, worauf die Seele gerichtet ist, wenn sie Geistiges schaut.",
      "Die im Geistigen herrschenden Be­ziehungen, die besondere Art desjenigen, was man da «Wesen» und Vorgänge nennen kann, ist viel komplizierter, feiner, vielgestaltiger als dasje­nige, was im gewöhnlichen Sprachgebrauch zum Ausdruck kommt. Man gelangt nur zum Ziele, wenn man die Möglichkeiten ausnutzt, die in der Sprache liegen in bezug auf Satzwendungen, Wortumstellungen; wenn man sich bemüht, dasjenige, was ein Satz nicht adäquat aussprechen kann, durch einen hinzugefügten zweiten im Zusammenhang mit dem ersten zum Ausdruck zu bringen.",
      "Zum Verständnis der Anthroposophie ist durchaus nötig, auf solche Dinge einzugehen. Es kann zum Beispiel der Fall eintreten, daß ein geistiger Tatbestand ganz schief gesehen wird, wenn man die Ausdrucksform nicht als etwas Wesentliches ansieht.",
      "Dessoir ist nicht einmal im ent­ferntesten darauf gekommen, daß so etwas zu berücksichtigen wäre. Er scheint überall vorauszusetzen, daß, was ihm unverständlich ist, auf dem kindlichen Denken, auf der primitiven Methode des andern beruht.",
      "für vernichtete niedere Triebe und Leidenschaften), dessen Schneidestelle von sieben roten Rosen umgeben ist (Symbol für geläuterte Triebe und Leidenschaften.»* Ab­gesehen davon, daß eine solche Behauptung, aus dem Zu­sammenhang gerissen, einen absonderlichen Eindruck auf einen Leser machen muß, während sie dies kaum tun wird an der Stelle der Auseinandersetzungen, an der sie in mei­nem Buche steht, muß ich sagen: läse ich das, was Max Dessoir in dem obigen Satze sagt, als die Meinung eines Menschen, ich hielte die Sache für Unsinn, oder, zum min­desten, für unsinnig ausgedrückt. Denn ich könnte keinen Zusammenhang finden zwischen den Bedeutungen des Doppelsymbols, zwischen «vernichteten niederen Trieben und Leidenschaften» und «geläuterten Trieben und Lei­denschaften».",
      "Ich mußte mir ja geradezu vorstellen: der Mensch solle seine niederen Triebe und Leidenschaften vernichten, und an der Stelle, an der die Vernichtung angerichtet worden ist, erschienen, wie aus dem Nichts her­vorgeschossen, geläuterte Triebe und Leidenschaften. Aber warum «geläutert», da doch nichts zu «läutern» war, sondern am Orte der Vernichtung etwas Neues entstanden ist.",
      "Mein Denken käme auf keinen Fall mit einem solchen Satze zurecht. Aber man lese doch den Satz in meinem Bu­che. Da steht: «Man stelle sich ein schwarzes Kreuz vor. Dieses sei Sinnbild für das vernichtete Niedere der Triebe und Leidenschaften; und da, wo sich die Balken des Kreu­zes schneiden, denke man sich sieben rote, strahlende Ro­sen im Kreise angeordnet.»** - Man sieht: ich sage nicht,",
      "*    Vergleiche Seite 255 des Dessoirschen Buches.",
      "** Vergleiche meine « Geheimwissenschaft im Umriß», 26. Auflage, Seite 311.",
      "das Kreuz sei Sinnbild für «vernichtete niedere Triebe und Leidenschaften», sondern für «das vernichtete Niedere der Triebe und Leidenschaften». Also die niederen Triebe und Leidenschaften werden nicht «vernichtet», sondern «ver­wandelt »,so daß ihr Niederes abgestreift wird, und sie selbst als geläutert auftreten. So macht sich Max Dessoir erst das zurecht, was er kritisieren will. Dann kann er es als eine «kindliche Vorstellungsweise» ausgeben. Es ist sicherlich pedantisch, wenn man in dieser Weise - schulmäßig - Kor­rektur übt an einem Wortlaute. Aber nicht ich bin der Ver­anlasser dieser schulmäßigen Korrektur. Was sie notwen­dig macht, sind die Dessoirschen Entstellungen, die nur durch solche Schulmäßigkeit zu fassen sind. Denn sie kom­men - meinetwegen unbewußten oder durch Oberfläch­lichkeit erzeugten - Fälschungen meines Wortlautes gleich. Und nur diesem gefälschten Wortlaut gegenüber ist die Dessoirsche Kritik möglich.",
      "Ein anderer Fall der Dessoirschen «Wiedergabe » ist der folgende. Ich spreche - wieder in einem Zusammenhange, der die Sache ganz anders erscheinen läßt, als wenn man sie in Dessoirscher Art aus diesem Zusammenhange her­ausreißt - von gewissen früheren Entwickelungszuständen, welche die Erde durchgemacht hat, bevor sie der Pla­net geworden ist, als welcher sie für den Menschen in sei­ner gegenwärtigen Entwickelungsform bewohnbar ist. Ich schildere durch imaginative Vorstellungen, wie der erste dieser Entwickelungszustände war. Ich habe nötig, diese Zustände zu veranschaulichen dadurch, daß ich von Wesen geistiger Art spreche, die mit der damaligen planetarischen Urform der Erde in Zusammenhang standen. Abgesehen nun davon, daß Dessoir mich behaupten läßt, durch diese",
      "geistartigen Wesen «entwickelten» sich «Nahrungs- und Ausscheidungsprozesse » auf der planetarischen Urform der Erde, sagt er weiter: «Von diesen Zuständen erfährt der Hellsichtige noch heute durch eine dem Riechen ähn­liche übersinnliche Wahrnehmung, denn die Zustände sind eigentlich immer da.»* In meinem Buche ist zu lesen, daß die gemeinten geistartigen Wesen in Wechselwirkung tre­ten mit den im Innern der planetarischen Urform «vorhan­denen, auf- und abwogenden Geschmackskräften. Da­durch kommt ihr Äther- oder Lebensleib in eine solche Tä­tigkeit, daß man diese als eine Art Stoffwechsel bezeichnen kann.»** Dann sage ich, diese Wesen bringen Leben in das Innere der planetarischen Urform.",
      "«Es geschehen dadurch Nahrungs- und Ausscheidungsprozesse.»*** Es ist selbst­verständlich, daß gegenüber einer solchen Schilderung von Seite der gegenwärtigen Wissenschaft die schärfste Ableh­nung möglich ist. Allein es sollte ebenso selbstverständ­lich sein, daß ein Kritiker es nicht so machen darf wie Max Dessoir.",
      "Er sagt, indem er den Glauben erweckt, daß er meine Darstellung wiedergibt, es entwickeln sich durch die gemeinten Wesen Nahrungs- und Ausscheidungspro­zesse. So wie bei mir die Sache dargestellt ist, steht zwi­schen der Angabe, daß die Wesen auftreten und derjeni­gen, daß Nahrungs- und Ausscheidungsprozesse entste­hen, der Zwischensatz, der besagt, daß sich eine Wechsel­wirkung entwickelt und daß durch diese in dem Äther- oder Lebensleib dieser Wesen eine Tätigkeit auftritt, die ihrerseits",
      "*    Vergleiche Seite 258 des Dessoirschen Buches.",
      "**    Vergleiche meine «Geheimwissenschaft im Umriß», 26. Auflage, Seite 166 f.",
      "***    An derselben Stelle meiner «Geheimwissenschaft» wie das vorige.",
      "nun wieder zu den Nahrungs- und Ausscheidungsprozesse der planetarischen Urform führt. Was Dessoir mit meiner Darstellung vollführt, läßt sich mit dem Fol­genden vergleichen. Jemand sagt: Ein Mann tritt in ein Zimmer, in dem sich ein Kind und dessen Vater befinden.",
      "Das Kind benimmt sich dem Eintretenden gegenüber so, daß der Vater es strafen muß. Diesen Satz entstellt nun ein anderer, indem er behauptet: durch das Eintreten des fremden Mannes entwickelt sich die Strafe des Kindes.",
      "Könnte nun jemand aus dieser Behauptung erkennen, was der erste eigentlich hat sagen wollen? Doch Dessoir läßt mich ferner sagen, der Hellsichtige erfahre von gewissen Zuständen, die in der planetarischen Urform auftreten, durch «eine dem Riechen ähnliche Wahrnehmung».* Bei mir ist aber zu lesen, daß sich in den entsprechenden Zu­ständen willensartige Kräfte offenbaren, die sich «dem hellseherischen Wahrnehmungsvermögen durch Wirkun­gen» kundgeben, welche «sich mit verglei­chen lassen ».** Also bei mir ist nichts zu finden von der Behauptung, daß die in Frage kommende geistige Wahr­nehmung eine «dem Riechen ähnliche » ist, sondern es tritt deutlich hervor, daß diese Wahrnehmung nicht dem Rie­chen ähnlich ist, daß aber dasjenige, was wahrgenommen wird, sich mit «Gerüchen» vergleichen lasse.",
      "Wie im anthro­posophischen Sinne ein solcher Vergleich aufzufassen ist, ist an anderem Orte dieser Schrift genugsam gezeigt. Doch Dessoir verschafft sich durch die Entstellung meines Wortlautes die Möglichkeit, die folgende - ihm wahrscheinlich",
      "* Vergleiche Seite 258 des Dessoirschen Buches.",
      "** Vergleiche meine «Geheimwissenschaft im Umriß», 26. Auflage, Seite 168.",
      "geistreich dünkende - Bemerkung anzubringen: «Mich wundert, daß hiermit der  und der  nicht in Verbindung gebracht wird.» Ich könnte nun noch andere ähnliche Beispiele von Des­soirschen «Wiedergaben» meiner Darlegungen genauer anführen, zum Beispiel wie er mich «durch Abtrennung des Ätherleibes vom physischen Leib» das «Einschlafen» eines Beines erklären läßt, während ich nicht den objektiven Tatbestand des sogenannten Einschlafen dadurch erkläre, sondern sage, daß das subjektive «eigentümliche Gefühl, das man empfindet, von dem Abtrennen des Ätherleibes» herrührt.* Nur dann, wenn man den Wortlaut meiner Darstellung so nimmt, wie ich ihn gegeben habe, kann man sich eine Meinung darüber bilden, Weiche Tragweite meiner Behauptung zukommt, und wie sie durchaus den durch die Naturwissenschaft festzustellenden objektiven Tatbestand nicht ausschließt, so wenig sie ausgeschlossen zu werden braucht von demjenigen, der die anthropologische Meinung vertritt. Das letztere aber will Dessoir seinen Lesern glauben machen. Doch ich will darauf verzichten, den Leser weiter mit derlei Korrekturen zu ermüden. Die vorgebrachten soll­ten nur zeigen, in welchem Grade oberflächlich Max Dessoir dasjenige liest, über das er sich zum Richter aufwirft.",
      "Ich will aber zeigen, wozu die Seelenverfassung führen kann, die aus solcher Oberflächlichkeit heraus zu Gericht sitzt. In meiner Schrift «Die geistige Führung des Men­schen und der Menschheit »** versuche ich darzulegen, wie",
      "* Vergleiche meine «Geheimwissenschaft im Umriß», 26. Auflage, Seite 96.",
      "** «Die geistige Führung des Menschen und der Menschheit.» Geisteswissenschaftliche Ergebnisse über die Menschheits-Entwickelung von Ru­dolf Steiner (1911). 7. Auflage. Freiburg i.Br., 1956.",
      "die Kräfte des Vorstellungslebens, die nicht gleich bei der Geburt, sondern erst in späterem Lebensalter in das Bewußtsein des Kindes treten, schon tätig sind vor diesem be­wußten Aufleben, und wie in deren unbewußter Tätigkeit zum Beispiel bei dem Fortbilden des Nervensystems und anderem diese Kräfte in einer Art weisheitsvoll wirken, gegen welche das spätere bewußte Wirken von einem ge­ringeren Weisheitsgrade erscheint. Aus Gründen, deren Darlegung hier zu weit führen würde, komme ich zu der Ansicht, daß das bewußte Vorstellungsleben zwar die Weisheit fortentwickelt, welche in gewissen Bildungen des organischen Leibes in früher Kindheit tätig ist, daß sich aber dieses bewußte Vorstellungsleben zu jenem unbewuß­ten Weisheitswirken verhält wie zum Beispiel der Bau ei­nes von bewußter menschlicher Weisheit herrührenden Werkzeuges zu dem Wunderbau des menschlichen Gehir­nes.* Der Leser der oben genannten Schrift könnte wohl aus derselben ersehen, daß ich eine solche Behauptung nicht ausspreche als das Ergebnis eines «Einfalles», son­dern daß sie der Abschluß ist eines im Sinne der Anthro­posophie vorangegangenen Forschungsweges; auch wenn ich, wie natürlich ist, nicht in jeder meiner Schriften die Einzelheiten dieses Weges darstellen kann.",
      "In dieser Be­ziehung bin ich nun schon einmal darauf angewiesen, daß meine Schriften so genommen werden wie Teile eines Gan­zen, die sich gegenseitig stützen und tragen. Doch nicht darauf kommt es mir jetzt an, die Berechtigung dieser mei­ner Behauptung über unbewußte und bewußte Weisheit darzulegen, sondern auf etwas anderes, das sich Dessoir leistet, indem er die diesbezügliche Ausführung meines",
      "* Vergleiche meine Schrift «Geistige Führung», 7. Auflage, Seite 20 ff.",
      "Buches in der folgenden Art seinen Lesern zurechtschnei­det: «Am engsten, heißt es, ist der Zusammenhang mit höheren Welten in den drei ersten Lebensjahren, in die kei­ne Erinnerung zurückreicht. Besonders ein Mensch, der selber Weisheit lehrt - so bekennt Herr Rudolf Steiner -, wird sich sagen: * - Man darf wohl fragen: welche Vorstellung mag sich in einem Leser des Dessoirschen Buches festsetzen, dem diese Sätze vor Augen treten? Kaum eine andere, als daß ich in derjenigen Schrift, die Veranlassung zu diesen Sätzen gegeben hat, von einer Beziehung der geistigen Welt zum erkennenden Menschen spreche, und dafür mich selbst als Beispiel anführe. Es ist selbstverständlich nicht schwierig, einen Menschen der Lächerlichkeit preiszuge­ben, dem man eine solche Geschmacklosigkeit vorwerfen kann. Wie aber ist die Sache wirklich? In meiner Schrift steht: «Man nehme an, ein Mensch habe Schüler gefun­den, einige Leute, die sich zu ihm bekennen. Ein solcher wird durch echte Selbsterkenntnis leicht gewahr werden , daß ihm gerade die Tatsache, daß er Bekenner gefunden hat, das Gefühl gibt: was er zu sagen habe, rühre nicht von ihm her. Es sei vielmehr so, daß sich geistige Kräfte aus höheren Welten den Bekennern mitteilen wollen, und diese finden in dem Lehrer das geeignete Werkzeug, um sich zu offenbaren. - Einem solchen Menschen wird der Gedanke nahetreten: Als ich ein Kind war, habe ich an mir durch",
      "* Vergleiche Seite 260 des Dessoirschen Buches.",
      "Kräfte gearbeitet, die aus der geistigen Welt hereinwirk­ten, und das, was ich jetzt als mein Bestes geben kann, muß auch aus höheren Welten hereinwirken; ich darf es nicht als meinem gewöhnlichen Bewußtsein angehörig betrachten. Ja, ein solcher Mensch darf sagen: etwas Dämonisches, et­was wie ein Dämon - aber das Wort im Sinne einer guten geistigen Macht genommen - wirkt aus einer geistigen Welt durch mich auf die Bekenner. - So etwas empfand Sokrates ...",
      "Viel hat man versucht, um diesen des Sokrates zu erklären. Aber man kann ihn nur erklären, wenn man sich dem Gedanken hingeben will, daß Sokrates so etwas empfinden konnte, wie aus obiger Be­trachtung sich ergibt. »* Man sieht, mir handelt es sich um eine Auffassung des Sokratischen Dämonions vom Ge­sichtspunkte der Anthroposophie.",
      "Über diesen Sokrati­schen «Dämon» gibt es viele Auffassungen. Man kann sich, wie gegen andere, so auch gegen die meinige sachlich wenden. Was aber macht Max Dessoir? Wo ich von So­krates spreche, wendet er die Sache so, als ob ich von mir selbst spreche, indem er den Satz prägt: « so bekennt Herr Rudolf Steiner» und die letzten zwei Worte sogar in Sperr­druck setzt.",
      "Womit hat man es hier zu tun? Doch mit nichts Geringerem als mit einer objektiven Unwahrheit. Ich überlasse es jedem billig Denkenden, sich selbst ein Urteil zu bilden über einen Kritiker, der sich solcher Mittel bedient.",
      "Aber die Sache ist damit nicht erschöpft. Denn, nach­dem Dessoir meine Auffassung des Sokratischen Dämo­nions in der angedeuteten Art gewendet hat, schreibt er weiter: «Die Tatsache also, daß der einzelne ein Träger",
      "* Vergleiche meine genannte Schrift «Die geistige Führung...», 7. Auf­lage, Seite 30 f.",
      "überindividueller Wahrheiten ist, vergröbert sich hier zu der Vorstellung, daß eine dinglich gedachte Geisteswelt gleichsam durch Röhren oder Drähte mit dem Individuum verbunden sei: Hegels objektiver Geist verwandelt sich in eine Gruppe von Dämonen, und alle Schattengestalten ei­nes ungeläuterten religiösen Denkens treten wieder auf. Die Richtung im ganzen kennzeichnet sich als materialisti­sche Vergröberung seelischer Vorgänge und personifizie­rende Verflachung der geistigen Werte.»* - Solcher «Kri­tik» gegenüber hört wirklich jede Möglichkeit auf, sich mit dem Kritiker ernsthaft auseinanderzusetzen. Man be­denke doch, was hier eigentlich vorliegt. Ich spreche von dem Dämonion des Sokrates, von dem doch dieser selbst",
      "- nach historischer Überlieferung - gesprochen hat. Max Dessoir legt mir unter, daß, wenn man so vom Dämonischen spricht, dann «verwandelt sich Hegels objektiver Geist in eine Gruppe von Dämonen ... »* Dessoir benutzt also seine sonderbare Abschwenkung von dem in Wahr­heit gemeinten Gedanken, um seinem Leser die Ansicht beizubringen, jemand sei berechtigt, von mir anzunehmen, ich sehe in Hegels objektivem Geist «eine Gruppe von Dä­monen». - Man stelle neben diese Dessoirsche Behaup­tung, was ich in meinem Buche «Die Rätsel der Philoso­phie» alles vorbringe, um von Hegels Ansicht über den «objektiven Geist» alles fernzuhalten, was diesem irgend­wie den Charakter des Dämonischen aufdrücken könnte.** Wer gegenüber dem von mir über Hegel Vorgebrachten",
      "*    Vergleiche Seite 260 des Dessoirschen Buches.",
      "** Vergleiche im ersten Band meines Buches «Die Rätsel der Philoso­phie», 7. Auflage, die auf Seiten 234 gegebene Darstellung der Hegelschen Philosophie.",
      "sagt: der Vertreter der Anthroposophie habe Vorstellun­gen, durch die sich Hegels «objektiver Geist» in eine Gruppe von Dämonen verwandle, der behauptet eben eine objektive Unwahrheit. Denn selbst hinter der Ausrede kann er sich nicht verschanzen: ja, zwar stellt es Steiner anders dar, aber ich kann mir nur vorstellen, daß die Stei­nerschen anthroposophischen Voraussetzungen zu den von mir angegebenen Folgerungen führen. Er würde damit eben nur zeigen, daß er meine Ausführungen über He­gels «objektiven Geist» nicht in der Lage ist, zu verste­hen. Nachdem er seinen Sprung von Sokrates zu Hegel ge­macht hat, urteilt dann Max Dessoir weiter: «Aus der Un­fähigkeit zu sachlich angemessenem Verständnis entsprin­gen die durch keine wissenschaftlichen Bedenken gehemm­ten Phantasien ... »* - Wer meine Schriften liest und dann Dessoirs Darstellung meiner Anschauungen betrachtet, dürfte vielleicht doch einem solchen Satze gegenüber emp­finden, daß ich schon einiges Recht dazu habe, ihn so zu wenden: bei Max Dessoir entspringen aus der Unfähigkeit zu sachlich angemessenem Verständnis des in meinen Schriften Gesagten die oberflächlichsten, objektiv unwah­ren Phantasien über die Vorstellungen der Anthroposo­phie.",
      "Max Dessoir teilt seinen Lesern mit, daß er außer mei­ner «Geheimwissenschaft im Umriß, 5 . Auflage» noch «eine lange Reihe anderer Schriften benutzt» habe.** Bei seiner hier charakterisierten Art, sich «auszudrücken», kann man ja kaum feststellen, was er darunter versteht, er habe «eine lange Reihe» meiner Schriften «benutzt».",
      "*    Vergleiche Seite 26o des Dessoirschen Buches.",
      "**    Vergleiche Seite 254 des Dessoirschen Buches.",
      "Ich habe mir den Abschnitt «Anthroposophie» seines Bu­ches daraufhin angesehen, von welchen meiner Schriften - außer der «Geheimwissenschaft im Umriß» - noch Spuren der Benutzung auftreten. Ich kann nur entdecken, daß die­se «lange Reihe» aus drei kleinen Schriften besteht: dem 64 Seiten umfassenden Büchlein «Die geistige Führung des Menschen und der Menschheit», dem 48 kleine Seiten umfassenden Abdruck meines Vortrages «Blut ist ein ganz besonderer Saft» und dem 46 Seiten umfassenden Schrift­chen «Reinkarnation und Karma».",
      "Dazu erwähnt er noch in einer Anmerkung meine 1894 erschienene «Philosophie der Freiheit».* So sehr es mir widerstrebt, zu dieser An­merkung auch einige rein Persönliches betreffende Sätze zu sagen: ich muß es tun, weil auch in dieser Nebensache der Grad von wissenschaftlicher Genauigkeit, der Max Des­soir eigen ist, zum Ausdruck kommt. Er sagt: «In Steiners Erstling, der (Berlin 1894) fin­den sich nur Ansätze zur eigentlichen Lehre ...» Diese «Philosophie der Freiheit » nennt also Max Dessoir meinen « Erstling».",
      "Die Wahrheit ist, daß meine schriftstellerische Tätigkeit mit meinen Einführungen in Goethes naturwissenschaftliche Schriften beginnt, deren erster Band 1883 erschienen ist, elf Jahre, bevor Dessoir meinen «Erstling» ansetzt. Diesem «Erstling» gehen voran: die ausführli­chen Einführungen zu drei Bänden von Goethes naturwissenschaftlichen Schriften, meine «Grundlinien einer Erkenntnistheorie der Goetheschen Weltanschauung» (1886), meine Schrift «Goethe als Vater einer neuen Ästhe­tik»(1889), meine für meine ganze Weltanschauung grundlegende Schrift «Wahrheit und Wissenschaft» (1892).",
      "* Vergleiche Seite 254 des Dessoirschen Buches.",
      "hätte dieses Falles von Dessoirs sonderbarer Kenntnisnah­me dessen, worüber er schreibt, doch nicht Erwähnung getan, wenn nicht die Sache so läge, daß alle in meiner « Philosophie der Freiheit» vorgebrachten Grundanschau­ungen bereits in meinen früheren Schriften ausgesprochen und in dem genannten Buche nur in einer zusammenfas­senden und sich mit den philosophisch-erkenntnistheoretischen Ansichten vom Ende des neunzehnten Jahrhun­derts auseinandersetzenden Art vorgetragen sind. Ich wollte in dieser «Philosophie der Freiheit » in systematisch-organischer Gliederung zur Darstellung bringen, was ich in den früheren, fast ein ganzes Jahrzehnt umfassenden Veröffentlichungen an erkenntnistheoretischer Grundle­gung und an ethisch-philosophischen Folgerungen für eine auf die Erfassung der geistigen Welt zielende Anschauung niedergelegt hatte.",
      "Nachdem Max Dessoir in der angeführten Art über mei­nen «Erstling» gesprochen hat, fahrt er über denselben fort: «Es wird dort gesagt, daß der Mensch etwas aus der Natur in sich herübergenommen hat und daher durch die Erkenntnis des eigenen Wesens das Rätsel der Natur lösen kann; daß im Denken eine Schaffenstätigkeit dem Erken­nen vorangeht, während wir am Zustandekommen der Natur unbeteiligt und auf nachträgliches Erkennen ange­wiesen sind. Intuition gilt hier bloß als die Form, in der ein Gedankeninhalt zunächst hervortritt.» Man sehe nach, ob sich in meiner «Philosophie der Freiheit» etwas findet, das sich in diese ein Ungeheuerliches von Trivialität dar­stellenden Sätze zusammenfassen läßt. Ich habe in meinem Buche den Versuch gemacht, nach einer ausführlichen Auseinandersetzung mit andren philosophischen Richtungen,",
      "zu zeigen, daß dem Menschen in der Sinnesbeobach­tung nicht die volle Wirklichkeit vorliegt, daß also das von den Sinnen gegebene Weltbild eine unvollständige Wirklich­keit ist. Ich habe mich bestrebt, darzulegen, daß die menschliche Organisation diese Unvollständigkeit notwendig macht.",
      "Nicht die Natur i>erbirgt dem Menschen dasjenige, was zu ihrem Wesen dem Sinnesbilde fehlt, son­dern der Mensch ist so geartet, daß er durch diese Artung auf der Stufe des bloß beobachtenden Erkennens sich selbst die geistige Seite des Weltbildes verhüllt. Im aktiven Denken beginnt dann die Erschließung dieser geistigen Seite.",
      "Es ist - im Sinne meiner Weltauffassung - im akti­ven Denken ein Wirkliches (Geistiges) unmittelbar gegen­wärtig' das im bloßen Beobachten noch nicht gegeben sein kann. Das ist gerade das Charakteristische dieser meiner erkenntnistheoretischen Grundlegung einer Geisteswis­senschaft, daß ich nicht in der Intuition - insoferne diese im Denken zum Ausdruck kommt - «bloß die Form» sehe, «in der ein Gedankeninhalt zunächst hervortritt».",
      "Max Dessoir beliebt also seinen Lesern das Gegenteil von dem vorzusetzen, was in meiner «Philosophie der Freiheit» wirklich dargestellt ist. - Man sehe, um das zu bemerken , nur auf die folgenden meiner Gedanken: «In dem Denken haben wir das Element gegeben, das unsere besondere In­dividualität mit dem Kosmos zu einem Ganzen zusammenschließt. Indem wir empfinden und fühlen (auch wahrneh­men), sind wir einzelne, indem wir denken, sind wir das All-Eine Wesen, das alles durchdringt...» «Die Wahrneh­mung ist also nichts Fertiges, Abgeschlossenes, sondern die eine Seite der totalen Wirklichkeit.",
      "Die andre Seite ist der Begriff. Der Erkenntnisakt ist die Synthese von Wahrnehmung",
      "und Begriff . . . »* «Im Gegensatz zum Wahrneh­mungsinhalte, der uns von außen gegeben ist, erscheint der Gedankeninhalt im Innern. Die Form, in der er zu­nächst auftritt, wollen wir als Intuition bezeichnen. Sie ist für das Denken, was die Beobachtung für die Wahrnehmung ist. Intuition und Beobachtung sind die Quellen unserer Erkenntnis.»** Ich sage also hier: Intuition wolle ich als Ausdruck für die Form gebrauchen, in der die im Gedan­keninhalt verankerte geistige Wirklichkeit zunächst in der menschlichen Seele auftritt, bevor diese erkannt hat, daß in dieser gedanklichen Innenerfahrung die in der Wahrneh­mung noch nicht gegebene Seite der Wirklichkeit enthal­ten ist. Deshalb sage ich: Intuition ist «für das Denken, was die Beobachtung für die Wahrnehmung ist». Also selbst, wenn Max Dessoir scheinbar wörtlich eines Andern Gedan­ken anführt, ist er imstande, das was dieser Andere meint, in das Gegenteil zu verkehren. Dessoir läßt mich sagen:",
      "«Intuition gilt hier bloß als die Form, in der ein Gedankeninhalt zunächst hervortritt.»*** Den folgenden meiner Sät­ze, durch den dieses von ihm gebrauchte «bloß» zum Un­sinn wird, läßt er weg. Mir gilt eben Intuition nicht «bloß» als die «Form, in der ein Gedankeninhalt zunächst her­vortritt», sondern als die Offenbarung eines Geistig-Wirk­lichen, wie die Wahrnehmung als diejenige des Stofflich-Wirklichen. Wenn ich sage: die Uhr tritt zunächst als der Inhalt meiner Westentasche auf; sie ist für mich der Messer der Zeit; so darf nicht ein anderer behaupten, ich",
      "* Vergleiche zu diesen Gedanken meine «Philosophie der Freiheit», 11. Auflage, Seiten 93 und 94.",
      "** Vergleiche «Philosophie der Freiheit», Seite 98.",
      "*** Vergleiche Seite 254 des Dessoirschen Buches.",
      "hätte gesagt: die Uhr ist «bloß» der Inhalt meiner Westen­tasche.",
      "Im Zusammenhange meiner Veröffentlichungen ist meine «Philosophie der Freiheit » die erkenntnistheoretischer Grundlegung für die von mir vertretene anthroposo­phisch orientierte Geisteswissenschaft. Ich habe dies in ei­nem besonderen Abschnitt meines Buches «Die Rätsel der Philosophie» dargelegt.* Ich habe in diesem Abschnitt ge­zeigt, wie ein gerader Weg von meiner Schrift «Wahrheit und Wissenschaft» und meinem Buche «Philosophie der Freiheit», nach meiner Auffassung, zur «Anthroposophie» führt.",
      "Doch Max Dessoir schafft sich die Möglichkeit, durch Nicht-Benutzung meines zweibändigen Buches über die «Rätsel der Philosophie» seinen Lesern allerlei leicht Mißzuverstehendes über die « lange Reihe» meiner drei kleinen Schriften «Die geistige Führung...», «Blut ist ein ganz be­sonderer Saft» und «Reinkarnation und Karma» zu erzäh­len. In der ersteren kleinen Schrift mache ich den Versuch, im geistigen Entwickelungsgange der Menschheit konkrete geistige Wesenskräfte als wirksam zu erkennen.",
      "Ich habe für den Leser nach meinen Vorstellungen klar gemacht, daß ich mir wohl bewußt bin, wie leicht gerade der Inhalt dieser Schrift mißverstanden werden kann. In der Vorrede sage ich ausdrücklich, daß jemand, der diese Schrift in die Hand bekommt, ohne deren Voraussetzungen zu kennen, sie «als kuriosen Ausfluß einer bloßen Phantastik ansehen» müßte.",
      "Ich bezeichne allerdings in dieser Vorrede nur das in meinen beiden Schriften «Theosophie» und «Geheimwissen­schaft» Enthaltene als diese Voraussetzungen. Das ist 1911",
      "*    Vergleiche das Schlußkapitel des zweiten Bandes meiner «Rätsel der Philosophie».",
      "geschehen. 1914 ist mein Buch «Die Rätsel der Philosophie» als zweite Auflage meiner 1900 und 1901 erschienenen «Welt- und Lebensanschauungen im neunzehnten Jahrhun­dert» veröffentlicht worden. In diesen «Rätseln der Philo­sophie» habe ich auch dargestellt, wie die Atomenlehre ent­standen ist, wie sich Forscher wie Galilei in den geistigen Entwickelungsgang der Menschheit - nach meinen Vor­stellungen - eingliedern, ohne daß ich bei dieser Darstellung auf etwas anderes mich beziehe, als was mit Bezug auf die Entstehung der Atomenlehre oder auf die Stellung Galileis in der Wissenschaftsgeschichte «vor jedermanns Augen ... klar zutage» liegt.* Meine Darstellung ist zwar in meiner Art gehalten; aber ich beziehe mich bei dieser Darstellung auf nichts anderes, als was für einen gewöhnlichen Darstel­ler eines Abrisses der Philosophiegeschichte üblich ist.",
      "In meiner Schrift «Die geistige Führung ...» wird der Versuch gemacht, das, was ich selbst in einem anderen Buche so dar­zustellen bestrebt bin, wie es «vor jedermanns Augen» liegt, als Ergebnis konkreter geistiger Wesenskräfte, die im menschlichen Entwickelungsgange wirksam sind, darzu­stellen. Aus dem Zusammenhang, in dem diese Darstellung in meiner Schrift «Die geistige Führung ...» auftritt, heraus­gerissen, läßt sich - meiner Meinung nach - der bezügliche Gedanke nur in folgender Art wiedergeben: In der Geistes­geschichte der Menschheit wirken außer den Kräften, die sich für die gewöhnlichen historischen Methoden als für «jedermanns Augen . . . klar zutage» liegend ergeben, noch",
      "* Vergleiche meine Darstellung der Atomenlehre in ihrer Entwickelung zum Beispiel «Die Rätsel der Philosophie». 1. Band, 7. Auflage, Seite 62 f. , meine Auffassung über Galilei zum Beispiel in demselben Band, Seite 104 f. Doch habe ich auch in meinen Einführungen und Anmerkungen zu Goe­thes «Naturwissenschaftlichen Schriften» von Galilei gesprochen.",
      "andere, nur der geisteswissenschaftlichen Forschung zu­gängliche (übersinnliche) Wesenskräfte. Und diese Wesenskräfte wirken nach bestimmten erkennbaren Gesetzen. In der Art, wie in derjenigen Entwickelungsperiode der Menschheit, die ich die ägyptisch-chaldäische nenne (vom vierten bis zum ersten vorchristlichen Jahrtausend), die Erkenntniskräfte wirken, sind solche Wesenskräfte erkenn­bar, die in dem Zeitalter, in dem die Atomenlehre entsteht, wieder, aber in einer anderen Tätigkeitsform, auftreten.",
      "In der Entstehung und Fortbildung des Atomismus sehe ich wirksam solche geistige Wesenskräfte, die in der Denkungsart des ägyptisch-chaldäischen Zeitalters in andrer Art schon wirksam waren.* - Wer auch nur ganz flüchtig auf meine Ausführungen eingeht, kann finden, daß die Geltend­machung geistiger Wirkenskräfte im Verfolg der Mensch­heitsentwickelung durch meine anthroposophischen Ge­sichtspunkte von mir nicht dazu getrieben wird, das rein historisch Beobachtbare durch allerlei Anthropomorphis­men oder Analogien zu vernebeln, oder in das Dämmerdun­kel einer falschen Mystik zu rücken. Max Dessoir findet möglich, mit Bezug auf das hier in Frage Kommende seinen Lesern die Worte vorzusetzen: «Nein - hier kann der ge­duldigste Berichterstatter seine Ruhe nicht länger bewah­ren.",
      "Vor jedermanns Augen liegt klar zutage, wie die Ato­menlehre entstanden ist und sich seit dem Altertum folgerecht entwickelt hat, und da kommt jemand und ruft den geheimnisvollen großen Unbekannten zu Hilfe ! »** - Wer meine «Rätsel der Philosophie» liest, sieht, daß, was vor jedermanns",
      "* Vergleiche meine Schrift «Die geistige Führung...», 7. Auflage, Seite 65 f.",
      "** Vergleiche Seite 259 des Dessoirschen Buches.",
      "Auge liegt, auch von mir in dem Sinne dargestellt wird, wie es eben vor jedermanns Auge liegt; und daß ich für diejenigen Menschen, die verstehen können, daß das vor jedermanns Augen Liegende ein nicht vor Augen Liegen­des birgt, auf dieses dem geistigen Schauen Zugängliche hinweise. Und mein Hinweis ist nicht der auf einen «ge­heimnisvollen Unbekannten», sondern eben auf etwas, das durch die anthroposophischen Gesichtspunkte erkannt wird.*",
      "Daß das, was ich in einem oben angeführten Beispiele von Sokrates sage, Max Dessoir so wendet, als ob ich von mir selbst spreche, habe ich als unzulässig nachgewiesen. Daß aber die Bemerkung, die Max Dessoir auf Seite 34 seines Buches macht, auf niemand andern als auf ihn selbst zu be­ziehen ist, geht wohl aus dem Zusammenhange hervor. Um diese Bemerkung zu verstehen, muß man ins Auge fassen, daß Dessoir im Bewußtseinsaugenblick zwei Gebiete unter­scheidet, ein Mittelfeld und die Randzone. Die Bewußt­seinsinhalte bewegen sich, so führt er aus, immerwährend von einem dieser Gebiete in das andere. Nur erhalten diese Inhalte, wenn sie in die Randzone eintreten, ein besonderes Aussehen. Sie entbehren der Schärfe, haben weniger Eigen­schaften als sonst, werden unbestimmt. Die Randzone führt ein Nebendasein. Doch gibt es zwei Wege, auf denen sie zu",
      "* Man verzeihe mir hier ein aus der Mathematik entlehntes Gleichnis für die Dessoirsche «Kritik». Angenommen: Jemand sage innerhalb der Logarithmenlehre: zwei Zahlen werden multipliziert, wenn man deren Lo­garithmen addiert und zur Summe dieser die Grundzahl, als das Produkt, sucht. Wenn nun jemand käme und sagte: Nein - jedermann weiß doch, wie Zahlen multipliziert werden und da spricht einer vom Addieren ! In dieser Art aber ist Max Dessoirs Kritik mit Bezug auf den oben berührten Punkt.",
      "selbständigerer Wirksamkeit gelangt. Der erste dieser Wege kommt für das hier Anzuführende nicht in Betracht. Über den zweiten äußert sich Dessoir in der folgenden Art: «Der andere Weg der Verselbständigung verläuft so, daß die Randzone zwar als Mitbewußtsein neben dem Hauptbewußtsein bestehen bleibt, sich aber zu einer größeren Bestimmtheit und Verknüpfung ihrer Inhalte erhebt und dadurch in ein ganz neues Verhältnis zur gleichzeitigen vollbewußten See­lentätigkeit tritt.",
      "Um wiederum ein leicht verständliches Bild zu gebrauchen: aus dem Mittelpunkt des Kreises glei­tet ein Komplex an die Peripherie, versinkt dort aber nicht ins Nebelhafte, sondern bewahrt teilweise seine Bestimmt­heit und seinen Zusammenhang.»* Im Anschluß an diese Ausführung sagt dann Dessoir: «Ein Beispiel: Beim Vor­tragen sehr geläufiger Gedankengänge geraten mir gele­gentlich Begriffe und Worte in jene Region, und die Auf­merksamkeit beschäftigt sich mit anderen Dingen. Trotz­dem spreche ich weiter, gewissermaßen ohne Anteil des Be­wußtseins.",
      "Dabei ist es vorgekommen, daß ich von einer plötzlich eingetretenen Stille im Saal überrascht wurde und mir erst klar gemacht werden mußte, daß sie die Folge mei­nes eigenen Verstummens war ! Gewohnte Vorstellungs­verknüpfungen und Urteile können also auch vollzogen werden, zumal solche, die sich im Unan­schaulichen bewegen; die mit ihnen verbundenen Sprachbewegungen laufen gleichfalls ohne Schwierigkeit in den eingeübten Bahnen.» Allerdings, wenn ich diese Stelle in ihrer vollen Tragweite nehme, möchte ich doch lieber nicht annehmen, daß sie auf eine Eigenerfahrung Dessoirs ver­weist, sondern daß er von etwas spricht, was er an andern",
      "* Vergleiche Seite 32 ff. des Dessoirschen Buches.",
      "verträumten Rednern bemerkt hat, und daß er «mir» und «ich» nur gebraucht in dem Sinne, wie man es tut, wenn man sich stilistisch so ausdrückt, als ob man sich an die Stelle des Andern versetze. Der Zusammenhang, in dem die Sätze stehen, macht diese Erklärung allerdings schwierig, und nur möglich, wenn man annimmt, Dessoir sei stilistisch da­bei etwas unterlaufen, was in unserer hastenden Zeit vielen Schriftstellern geschieht. - Doch, wie dem auch sei, wesent­lich liegt die Sache so, daß eine Seelenverfassung, in welcher das «Unterbewußte» eine solche Rolle spielt, wie in dem von Dessoir für einen Redner gekennzeichneten Fall, zu dem allerersten gehört, was seelisch überwunden werden muß, wenn man in das Verständnis der anthroposophischen Erkenntnis eindringen will. Das völlige Gegenteil: die rest­lose Durchdringung der Begriffe mit Bewußtheit, ist not­wendig, wenn diese Begriffe ein Verhältnis haben sollen zur wirklichen geistigen Welt. Auf dem Gebiete der Anthropo­sophie ist ein Redner unmöglich, der weiterredet, wenn «die Aufmerksamkeit» sich « mit anderen Dingen» beschäftigt. Denn wer Anthroposophie erfassen will, muß sich daran ge­wöhnt haben, die Richtung seiner Aufmerksamkeit nicht zu trennen von der Richtung eines durch ihn hervorgerufe­nen Vorstellungsverlaufes. Er wird nicht weiter sprechen von Dingen, von denen sich seine Aufmerksamkeit abwen­det, weil er nicht weiter über solche Dinge denken wird.",
      "Sehe ich mir nun an, wie Max Dessoir über meine kleine Schrift «Blut ist ein ganz besonderer Saft» seinen Lesern berichtet, so drängt sich mir allerdings der Gedanke auf, daß er nicht nur weiter redet, wenn seine Aufmerksamkeit sich «anderen Dingen» zuwendet, sondern daß er in einem solchen Falle sogar weiter schreibt. In diesem Bericht findet",
      "man das Folgende. Es wird mein Satz angeführt: «Das Blut nimmt die durch das Gehirn verinnerlichten Bilder der Au­ßenwelt auf»,* und dazu macht Dessoir die Bemerkung: «Eine solche ungeheuerliche Mißachtung aller Tatsachen verbindet sich mit der ebenso unbeweisbaren wie unver­ständlichen Behauptung, der vorgeschichtliche Mensch habe in den , auch die Erleb­nisse seiner Vorfahren erinnert. »** Man lese doch diese Sät­ze, die Dessoir anführt, einmal in dem Zusammenhange nach, in dem sie in meiner Schrift stehen, und man nehme dazu meine Bemerkung auf Seite 24 derselben Schrift: «Ich muß im Gleichnisse sprechen, wenn ich die hier in Betracht kommenden komplizierten Vorgänge darstellen will», so wird man vielleicht doch einsehen, was es bedeutet, wenn jemand in der Dessoirschen Art berichtet. - Man stelle sich doch nur vor, was es hieße, wenn ich über Max Dessoirs «Jenseits der Seele» schriebe und meinen Lesern erzählte: da kommt jemand, der behauptet, das Blut, das «in unseren Adern» rinnt, ist «das Blut vieler Jahrtausende » .",
      "Und es sei dies eine ebenso unbeweisbare wie unverständliche Behaup­tung, die sich als gleichwertig zu der andern verhält: «Doch unterliegt es keinem Zweifel, daß es hinter der Oberfläche des Bewußtseins einen dunklen, reich gefüllten Raum gibt, durch dessen Veränderungen auch die Krümmung der Oberfläche verändert wird.» Die beiden Sätze finden sich in dem Dessoirschen Buche, der letzte Seite 1, der erste, von dem «Blute der Jahrtausende» auf Seite 12. Beide Sätze sind natürlich voll berechtigt, weil sich Max Dessoir «im Gleich­nisse» ausspricht.",
      "Wo ich dasselbe tun muß, und dies ausdrücklich",
      "*    Vergleiche meine Schrift «Blut ist ein ganz besonderer Saft», Seite 24.",
      "** Vergleiche Seite 261 des Dessoirschen Buches.",
      "bemerke, schmiedet Dessoir sich zur Widerlegung eine kritische Waffe aus hölzernem Eisen. - Dessoir spricht davon, daß mein Hinweis auf geistig Wesenhaftes sich «im ganzen kennzeichnet als materialistische Vergrö­berung seelischer Vorgänge und personifizierende Verfla­chung der geistigen Werte ».* Diese Behauptung ist gegen­über den Ausführungen meiner Schriften ebenso sinnvoll, wie wenn ich das Folgende sagte: Ein Denker, der imstande ist, zu sagen: «Man darf- in einer freilich sehr unvollkom­menen Vergleichung - den Bewußtseinsaugenblick einen Kreis nennen, dessen Peripherie schwarz, dessen Mittel­punkt weiß und dessen dazwischen liegende Teile abge­stuftes Grau sind», dessen Ansicht kennzeichne sich «im ganzen . . . als materialistische Vergröberung seelischer Vor­gänge». Und dieser Denker, der solch Groteskes macht, den Bewußtseinsaugenblick mit einem Kreise vergleicht, von weiß, grau, schwarz spricht, ist Max Dessoir.** ES kann mir natürlich nicht beifallen, dergleichen so hinzureden, denn ich weiß, Max Dessoir vergröbert in diesem Falle nicht in materialistischer Art seelische Vorgänge. Was er aber mir gegenüber vollbringt, ist von der eben gekennzeichneten Art.",
      "Man wird es begreiflich finden, daß es völlig unmöglich ist, mit einer Kritik, die auf Voraussetzungen ruht wie die Dessoirsche, sich auseinanderzusetzen über den Sinn des Schicksalsgesetzes vom anthroposophischen Gesichts­punkte aus; ich müßte ganze Kapitel meiner Schriften hier abschreiben, wenn ich zeigen wollte, wie haarsträubend ver­schoben wird, was ich an Vorstellungen über das menschli­che Schicksal vertrete durch die Dessoirsche Behauptung:",
      "*    Vergleiche Seite 260 des Dessoirschen Buches.",
      "** Vergleiche Seite 32 des Dessoirschen Buches.",
      "«Hiermit wird angeblich ein Zusammenhang von Ursache und Wirkung in der geistigen Welt enthüllt (die Kausalität gilt demnach nicht nur in der verstandesmäßig aufgefaßten Erfahrungswelt). Der Mensch, der sich durch eine Reihe von Lebensläufen hindurch vervollkommnet, untersteht dem Karma-Gesetz, wonach jede Tat ihre Folgen unaus­bleiblich nach sich zieht, also zum Beispiel die gegenwärtige Not von der Präexistenz her selbstverschuldet ist. »* Ich habe 1887 in meiner Einführung zum zweiten Bande von Goethes Naturwissenschaftlichen Schriften die Sätze nieder­geschrieben: «Das Erklären eines Vorganges in der Natur ist ein Zurückgehen auf die Bedingungen desselben: ein Aufsuchen des Produzenten zu dem gegebenen Produkte.",
      "Wenn ich eine Wirkung wahrnehme und dazu die Ursache suche, so genügen diese zwei Wahrnehmungen keineswegs meinem Erklärungsbedürfnisse. Ich muß zu den Gesetzen zurückgehen, nach denen diese Ursache diese Wirkung her­vorbringt.",
      "Beim menschlichen Handeln ist das nun anders. Da tritt die eine Erscheinung bedingende Gesetzlichkeit selbst in Aktion; was ein Produkt konstituiert, tritt selbst auf den Schauplatz des Wirkens. Wir haben es mit einem er­scheinenden Dasein zu tun, bei dem wir stehen bleiben kön­nen, bei dem wir nicht nach den tiefer liegenden Bedingun­gen zu fragen brauchen.»** Es ist wohl klar, was ich meine: das Fragen nach Bedingungen einer menschlichen Handlung kann nicht in derselben Weise erfolgen wie einem Vorgange der Natur gegenüber.",
      "Es muß also anders sein. Meine Anschauungen über den Schicksalszusammenhang, die eng",
      "*    Vergleiche Seite 265 des Dessoirschen Buches.",
      "** Vergleiche meine Einleitungen zu Goethes Naturwissenschaftlichen Schriften, Dornach 1926, Seite 149, Freiburg i. Br. 1949, Seite 183 f.",
      "verwandt sind mit denen nach den Willens quellen des Men­schen, können also nicht auf dasjenige Verhältnis von Ur­sache und Wirkung weisen, von dem man in der Naturwis­senschaft spricht. Ich gab mir deshalb in meinem Buche «Theosophie» alle Mühe, verständlich zu machen, daß ich weit davon entfernt bin, das Übergreifen der Erlebnisse des einen Menschenlebens in die folgenden im Sinne des natür­lichen Kausalzusammenhanges zu denken.",
      "Max Dessoir entstellt meine Schicksalsvorstellung in gröbster Weise, in­dem er in deren Mitteilung den Satz verflicht: «Die Kausa­lität gilt demnach nicht nur in der verstandesmäßig aufge­faßten Erfahrungswelt.» - Eine Möglichkeit, diese Bemer­kung anzubringen, schafft er sich nur dadurch, daß er aus meiner kleinen Schrift «Reinkarnation und Karma» einen Satz heraushebt, der in dieser Schrift eine längere Ausfüh­rung zusammenfaßt. Durch diese Ausführung wird dem Satze aber erst die rechte Bedeutung gegeben.",
      "So wie ihn Dessoir (isoliert) hinstellt, kann man in einer recht wohlfeilen Art seine Kritik daran üben. Der Satz heißt: «Alles, was ich in meinem gegenwärtigen Leben kann und tue, steht nicht abgesondert für sich allein da als Wunder, sondern hängt als Wirkung mit den früheren Daseinsformen meiner Seele zusammen, und als Ursache mit den späteren.»* Wer sich darauf einläßt, den Satz im Zusammenhang mit den Ausführungen zu lesen, die er zusammenfaßt, der wird fin­den, ich verstehe das Hinübergreifen von einer Lebensform in die andere so, daß auf dasselbe die im bloßen Naturbe­trachten übliche Kategorie der Kausalität nicht anwendbar ist.",
      "Man kann nur in abgekürzter Redewendung von Kau­salität",
      "*    Vergleiche meine Schrift «Reinkarnation und Karma» und Seite 261 f. von Dessoirs Buch.",
      "sprechen, wenn man eben die genauere Bestimmung mitgibt oder beim Leser als bekannt voraussetzen darf. In meinem zusammenfassenden Satz läßt aber das Vorange­hende gar nicht zu, daß man ihn anders als in der folgenden Art auffaßt: Alles, was ich in meinem gegenwärtigen Leben kann und tue, hängt als Wirkung mit den früheren Daseinsformen meiner Seele insofern zusammen, als die im gegenwär­tigen Leben liegenden Ursachen meines Könnens und Han­delns mit anderen Lebensformen in einer Beziehung stehen, welche nicht eine solche der gewöhnlichen Kausalität ist; und alles, was ich kann und tue hängt mit späteren Daseinsformen meiner Seele insofern zusammen, als dieses Ge­konnte und Getane Ursache von Wirkungen im gegenwär­tigen Leben ist, die nun ihrerseits mit dem Inhalt späterer Lebensformen in einer Beziehung stehen, welche wieder nicht eine solche der gewöhnlichen Kausalität ist. - Wer meine Schriften verfolgt, wird ersehen, daß ich nie einen Karma-Begriff vertreten habe, der mit der Vorstellung des freien Menschenwesens unvereinbar ist.",
      "Dessoir hätte das bemerken können, wenn er auch nichts anderes von mir Ge­schriebene «benutzt» hätte, als was in meiner «Geheimwissenschaft» steht: «Wer da meint, daß die menschliche Freiheit mit dem ... Vorausbestimmtsein der zukünftigen Gestaltung der Dinge nicht vereinbar sei, der sollte beden­ken, daß des Menschen freies Handeln in der Zukunft eben­sowenig davon abhängt, wie die vorausbestimmten Dinge sein werden, wie diese Freiheit davon abhängt, daß er sich vornimmt, nach einem Jahre in einem Hause zu wohnen, dessen Plan er gegenwärtig feststellt. »* Denn wenn auch",
      "* Vergleiche meine «Geheimwissenschaft im Umriß», 26. Auflage, Seite 413 f.",
      "diese Sätze sich nicht unmittelbar auf die Zusammenhänge der menschlichen Erdenleben beziehen, so könnte sie doch nicht jemand schreiben, welcher der Meinung ist, die Schicksale dieser Erdenleben hängen so zusammen, wie es dem Gesetze der naturwissenschaftlichen Kausalität ent­spricht.",
      "Dessoir läßt nirgends merken, daß er sich die Mühe ge­nommen habe, zu prüfen, in welcher Art ich erkenntnistheoretisch und allgemein-philosophisch, sowie in Gemäß­heit naturwissenschaftlicher Vorstellungen die von mir ver­tretene Anthroposophie begründe. Dafür stellt er Behaup­tungen auf, für die sich auch nicht einmal ein entfernter An­haltspunkt in meinen Schriften vorfindet. So Seite 296 f. sei­nes Buches: «Erfahren wir, daß die noch ganz in diesem Bann stehende Medizin des Mittelalters den Menschen nach dem Tierkreis einteilte und in der Hand mit ihren Fingern Unterabteilungen der Himmelsmaße sah, oder lesen wir bei Rudolf Steiner, daß vor der Befruchtung die Pflanze in einer solchen Lage ist wie die ganze Erde vor der Sonnentren­nung war, so haben wir Beispiele für den Grundsatz, im kleinen das Abbild großer Weltvorgänge zu sehen.»* Wäre, was Max Dessoir mit diesem Satze meint, ebenso richtig wie es unrichtig ist, so genügte es, meinen anthroposophischen Gesichtspunkt zusammenzuwerfen mit allem möglichen dilettantischen",
      "* Max Dessoir schreibt dieses mit Bezug auf die Ausführungen meiner «Geheimwissenschaft im Umriß», 26. Auflage, Seite 335 ff. Er ist einem Verständnis des von mir Gesagten nicht einmal nahe gekommen, sonst hätte er auf den Gedanken gar nicht verfallen können, daß diese Sache ir­gend etwas mit der von ihm angeführten dilettantischen Methode zu tun haben kann, «Entsprechungen» aufzusuchen zwischen weit voneinander entfernten Tatsachen. Ein Unbefangener muß sehen, daß, was ich über Erde und Sonnentrennung einerseits und über die Befruchtung der Pflanze andrerseits sage, in ganz selbständiger Weise gefunden wird, ohne von der ­Absicht auszugehen, eine «Entsprechung» aufzufinden. Mit demselben Rechte könnte man sagen, der Physiker suche nach «Entsprechungen», wenn er die polarisch zu einander stehenden Tatsachen, die an der Anode und der Kathode zutage treten, in die Untersuchung zieht. Aber Dessoir ist eher weit entfernt davon, zu verstehen , daß die von mir angewandte Methode nichts zu tun hat mit dem, was er treffen will, sondern daß sie völlig die ins Geistgebiet gewendete naturwissenschaftliche Denkweise ist.",
      "Treiben, das sich gegenwärtig als Mystik, Theosophie und dergleichen geltend macht. In Wirklich­keit ist diese Behauptung Dessoirs nur - schon allein für sich - ein voller Beweis dafür, daß dieser Kritiker meiner Anthroposophie ohne jedes Verständnis gegenübersteht, sowohl, was deren philosophische Grundlage wie deren Methode, ja auch sogar was die Ausdrucksform für ihre Er­gebnisse betrifft. Im Grunde ist Dessoirs Kritik nichts ande­res als viele «Entgegnungen», denen die von mir vertretene Anthroposophie ausgesetzt ist. Mit ihnen sind Auseinan­dersetzungen unfruchtbar, weil sie nicht dasjenige kritisie­ren, was sie zu beurteilen vorgeben, sondern ein von ihnen willkürlich geformtes Zerrbild, gegenüber dem dann ihnen die Kritik recht leicht wird. Mir erscheint es ganz unmög­lich, daß jemand, der einsieht, worauf es mir bei dem an­kommt, was mir Anthroposophie ist, dieses zusammenstellt - wie es Dessoir tut - mit einer literarischen unwillkürlichen Burleske wie den Faustbüchern von J.A. Louvier, mit der absonderlichen Rassenmystik Guido Lists, mit der Chri­stian Science - ja selbst mit alledem, was Dessoir als «Neu-­Buddhismus» bezeichnet. - Ob es berechtigt ist, daß Max Dessoir von meinen Ausführungen sagt: «Es verrät eine Anspruchslosigkeit des Denkens, wenn bloß verlangt wird, das Vorgebrachte als nicht widersinnig anzuerkennen (denn im weiteren Sinn möglich ist gar vieles, was unwahrscheinlich",
      "und fruchtlos bleibt); wenn nirgends untersucht und gefragt, gezweifelt und abgewogen, sondern von oben her bestimmt wird: .»* - dies zu beurteilen überlasse ich denjenigen, die meine Schriften wirklich kennen lernen mögen. Gar ein Satz wie dieser: «Harmlose Leser lassen sich vielleicht durch die eingestreuten Beispiele und die angebliche Aufklärung gewisser Erfahrungen bestechen . . . »* kann mich höch­stens dazu veranlassen, zu denken, wie «harmlose Leser» des Dessoirschen Buches sich vielleicht durch die einge­streuten, aber sinnlos interpretierten Zitate aus meinen Schriften und die gefällige Umsetzung meiner Gedanken ins Triviale bestechen lassen. - Wenn ich trotz der Unfrucht­barkeit, zu der eine Auseinandersetzung mit diesem Kriti­ker von vorneherein verurteilt ist, diese doch hier vorbringe, so geschieht es, weil ich wieder einmal an einem Beispiele zei­gen mußte, welcher Art von Beurteilung das, was ich An­throposophie nenne, begegnet; und weil es gar zu viele «harmlose Leser» gibt, die sich ihr Urteil über eine solche geistige Bestrebung nach Büchern wie das Dessoirsche bil­den, ohne Kenntnis zu nehmen von dem, was beurteilt wird, und ohne auch nur zu ahnen, wie das in Wirklichkeit aussieht, von dem ihnen ein Zerrbild vor Augen gestellt wird.",
      "Ob es eine Bedeutung hat, wenn jemand, der so ferne ist vom Verständnisse dessen, was ich anstrebe, der so von ihm beurteilte Schriften liest, wie Max Dessoir, - «von oben her» behauptet, ich lasse mir «gewisse Beziehungen zur Wissenschaft angelegen sein», besitze aber «kein inneres Verhältnis zum Geist der Wissenschaft»**, darüber urteile",
      "*    Vergleiche Seite 263 des Dessoirschen Buches.",
      "** Vergleiche Seite 254 des Dessoirschen Buches.",
      "ich auch nicht selbst, sondern überlasse dieses den Lesern meiner Bücher. - Fast ein Wunder wäre es, wenn die ganze Geistesart Max Dessoirs zu allem übrigen nicht auch noch den Satz fügte: «Gar nun die Masse seiner Anhänger ver­zichtet völlig auf eigene Denkarbeit.»* Wie oft müssen sich dieses diejenigen sagen lassen, die man als meine «Anhän­ger» zu bezeichnen beliebt ! Gewiß, «Anhänger» von zwei­felhaften Eigenschaften gibt es bei jeder geistigen Bestre­bung. Es kommt aber darauf an, ob diese und nicht vielleicht andere für die Bestrebung die Charakteristischen sind. Was weiß Max Dessoir von meinen «Anhängern»? Was weiß er darüber, wie viele es unter ihnen gibt, die nicht nur weit ent­fernt davon sind, auf eigene Denkarbeit zu verzichten, son­dern die, nachdem sie durch ihre Denkarbeit das wissen­schaftlich Ungenügende der Weltanschauungen vom Schla­ge der Dessoirschen durchschaut haben, es nicht verschmä­hen, sich Anregungen zu holen bei den Bestrebungen, durch welche ich, so gut ich es vermag, einen methodischen Weg suche, um ein kleines Stück in die geistige Welt einzudrin­gen. Vielleicht kommt doch die Zeit auch einmal heran, in der man gerechter urteilen wird über solche Menschen in der Gegenwart, die genug Denkarbeit zu verrichten imstande sind, um nicht zu den «harmlosen Lesern» Max Dessoirs zu gehören.**",
      "*    Vergleiche Seite 254 des Dessoirschen Buches.",
      "** Nur die Tatsache, daß Dessoir nicht in der Lage ist, sich wirklich ent­sprechende Vorstellungen über die anthroposophischen Versuche zu ma­chen, läßt es erklärlich erscheinen, daß er nicht einmal da mit irgendeinem Verständnisse dieser Versuche einsetzt, wo sein eigener Gedankengang ihm dies so nahe wie möglich legt. Solch ein Fall liegt in dem vor, worauf er mit zwei Sätzen auf Seite 322 f. seines Buches weist: «Es gibt kein Jenseits der Seele im Sinne einer unsichtbaren Wirklichkeit, weil geistige Sachverhalte des dinghaften wie des personenhaften Daseins überhoben sind.",
      "Das objektive Seelenjenseits darf als ein Überbewußtsein, niemals aber als ein räumlich außerhalb der Seele Existierendes betrachtet werden.» Dessoir sieht nicht, daß er mit einem solchen Satze nicht eine Widerlegung, sondern gerade den Beweis für die Notwendigkeit der Anthroposophie liefert. Er sieht nicht, daß in meinen Schriften überall der Versuch unternommen wird, die in Be­tracht kommenden Fragen als Bewußtseinsfragen zu behandeln.",
      "Man wolle nur bemerken, wie dieser Versuch zum Beispiel gerade in meiner «Geheim­wissenschaft im Umriß» durchgeführt ist. Nur kann eben Dessoir nicht sehen, daß dadurch der ganze Erkenntnisvorgang gegenüber der geistigen Welt zu einer inneren Verrichtung des Bewußtseins gemacht wird, daß innerhalb des Bewußtseins selbst andere Bewußtseinsformen erlebend auf­gesucht werden müssen, die es dann allerdings nicht mit einem «räumlich außerhalb der Seele Existierenden» zu tun haben, sondern mit einem Inne­sein der Seele in einem solchen Existierenden, das in ebendemselben Sinne unräumlich ist wie die Erlebnisse des gewöhnlichen Bewußtseins es selbst schon sind.",
      "Allerdings müßte derjenige, der dieses einsehen will, im anthro­posophischen Sinne zurecht gekommen sein mit einem solchen Satz wie derjenige ist, den Friedrich Theodor Vischer im 1. Teil seines «Altes und Neues», Seite 194, niedergeschrieben hat: «Die Seele, als oberste Einheit aller Vorgänge, kann allerdings nicht im Leibe lokalisiert sein, obwohl sie anderswo als im Leibe nicht ist ...» Dieser Satz gehört zu denjenigen, die an die Grenzorte des gewöhnlichen Erkennens führen im Sinne des I.",
      "Abschnit­tes dieser Schrift und im Sinne des I. Kapitels der am Ende derselben ste­henden «Skizzenhaften Erweiterungen des Inhaltes dieser Schrift»."
    ],
    "sentences": [
      [
        "Aus den hier vorangehenden Darstellungen ist wohl ersicht­lich, wie erwünscht dem Vertreter der Anthroposophie eine sachliche Auseinandersetzung mit dem Anthropologen sein kann.",
        "Es wäre denkbar, daß sich an ein Buch, das solche Absichten verfolgt wie das Max Dessoirs, eine derartige Ausein­andersetzung anknüpfen ließe.",
        "Vom Gesichtspunkte der An­throposophie ist dieses Buch im Sinne der anthropologischen Wissenschaft abgefaßt.",
        "Es stützt sich auf die Ergebnisse der Sinnesbeobachtung und will diejenige Denkungsart und die­jenigen Forschungsmittel zur Geltung bringen, welche in der naturwissenschaftlichen Erkenntnisströmung im Ge­brauch sind.",
        "Das Buch ist, im Sinne der hier gemachten Ausführungen, der anthropologischen Wissenschaft zugehörig."
      ],
      [
        "In dem «Anthroposophie» überschriebenen Abschnitt seines Buches will Max Dessoir eine Kritik liefern der in meinen Schriften dargestellten anthroposophischen An­schauungen.* Er versucht, verschiedene Ausführungen die­ser Schriften in seiner Art wiederzugeben und daran seine kritischen Bemerkungen zu knüpfen.",
        "Das also könnte dazu führen, zu beobachten, was von den beiden Vorstellungs­kreisen für diesen oder jenen Punkt des Erkenntnisstrebens gesagt werden kann."
      ],
      [
        "* Seiten 254 des Buches «Vom Jenseits der Seele», die Geheimwis­senschaften in kritischer Betrachtung von Max Dessoir.",
        "Verlag von Ferdi­nand Enke in Stuttgart, 1917."
      ],
      [
        "Ich will daraufhin die Ausführungen Max Dessoirs hier zur Darstellung und Besprechung bringen. - Dessoir will darauf hinweisen, daß von mir die Ansicht vertreten wird, die menschliche Seele könne es dahin bringen, durch innere Entwickelung sich ihrer Geistorgane zu bedienen, und sich dadurch zu einer Geisteswelt in ähnlicher Art in Beziehung setzen, wie sie dies durch die leiblichen Sinne zur sinnlichen tut.",
        "Man kann aus den vorangehenden Darlegungen dieser meiner Schrift ersehen, wie ich dasjenige denke, was in der Seele vorgehen muß, damit sie zur Anschauung des geistigen Lebens komme."
      ],
      [
        "Max Dessoir stellt in seiner Art dar, was ich in dieser Beziehung in meinen Schriften dargelegt habe.",
        "Er sagt darüber: «Durch solche Innenarbeit erreicht die Seele das, was von aller Philosophie erstrebt wird."
      ],
      [
        "Frei­lich muß das leibfreie Bewußtsein vor der Verwechslung mit traumhaftem Hellsehen und hypnotischen Vorgängen behütet werden.",
        "Wenn unsere Seelenkräfte gesteigert sind, kann das Ich sich oberhalb des Bewußtseins erleben, gleich­sam in einer Verdichtung und Verselbständigung des Gei­stigen, ja, es kann schon bei der Wahrnehmung von Farben und Tönen die Vermittelung des Leibes aus dem Erlebnis ausschließen.» Zu diesen seinen Sätzen fügt dann Dessoir die Anmerkung hinzu: «Es lohnt nicht, diese Behauptun­gen im einzelnen zu widerlegen.»* Dessoir bringt also meine Anschauung von geistiger Wahrnehmung damit zu­sammen, daß ich behaupte, man könne bei der Wahrneh­mung von Farben und Tönen die Vermittelung des Leibes ausschließen."
      ],
      [
        "Der Leser fasse ins Auge, was ich in den vor angehenden Darlegungen über die Erlebnisse gesagt habe, welche die Seele durch ihre Geistorgane macht, und wie sie"
      ],
      [
        "* Vergleiche Seite 255 des genannten Buches."
      ],
      [
        "dazu kommt, sich über diese Erlebnisse in Farben- und Ton­bildern auszudrücken.",
        "Er wird dann ersehen, daß ich vom Gesichtspunkte der Anthroposophie nichts Törichteres be­haupten könnte, als die Seele könne «bei der Wahrnehmung von Farben und Tönen die Vermittelung des Leibes aus­schließen».",
        "Brächte ich eine solche Behauptung vor, so wäre allerdings richtig, zu sagen, es lohne «nicht, diese Be­hauptung im einzelnen zu widerlegen».",
        "Man steht da vor einer wirklich merkwürdigen Tatsache.",
        "Max Dessoir be­hauptet, daß ich etwas sage, was nach meinen eigenen Vor­aussetzungen von mir als töricht bezeichnet werden muß.",
        "Mit einer solchen gegnerischen Einwendung ist nun aller­dings eine Auseinandersetzung unmöglich.",
        "Man kann nur feststellen, welch ein Zerrbild dahingestellt und für die An­schauung dessen ausgegeben wird, den man bekämpfen will."
      ],
      [
        "Nun könnte vielleicht Dessoir einwenden: so klar, wie ich die Konsequenzen meiner Anschauungen in bezug auf den eben berührten Punkt in dem vorangehenden Kapitel dieser Schrift ausgedrückt habe, finde er sie in meinen frü­heren Schriften nicht dargestellt.",
        "Ich werde ohne weiteres zugeben, daß mit Bezug auf manche Punkte der Anthropo­sophie in späteren von mir gegebenen Darlegungen eine ge­nauere Ausführung von früher Gebotenem zu finden ist, und daß der Leser meiner früheren Schriften vielleicht da oder dort zu einer irrigen Ansicht darüber kommen kann, was ich selbst in einem gewissen Punkte für die richtige Konsequenz meiner Anschauungen notwendig halte.",
        "Ich glaube, daß dieses jeder Einsichtige für selbstverständlich halten muß.",
        "Denn Anthroposophie ist ein weites Arbeits­feld, und Veröffentlichungen können immer nur einzelne Teilgebiete umfassen."
      ],
      [
        "Aber kann in diesem Falle sich Max Dessoir darauf beru­fen, daß in meinen früheren Schriften der oben berührte Punkt keine Aufhellung gefunden habe?",
        "Dessoirs Buch ist 1917 erschienen.",
        "Ich habe in der fünften Auflage meiner Schrift «Wie erlangt man Erkenntnisse der höheren Wel­ten», welche 1914 erschienen ist, zu der Stelle, die über die bildhafte Darstellung geistiger Erlebnisse durch Farben handelt, die folgende Bemerkung gemacht: «Man muß bei allen folgenden Schilderungen darauf achten, daß zum Bei­spiel beim einer Farbe geistiges Sehen (Schauen) ge­meint ist.",
        "Wenn die hellsichtige Erkenntnis davon spricht: , so bedeutet dies: .",
        "Nur weil es der hellsichtigen Erkenntnis in einem solchen Falle ganz naturgemäß ist, zu sagen: , wird dieser Ausdruck angewandt.",
        "Wer dies nicht bedenkt, kann leicht eine Far­benvision mit einem wahrhaft hellsichtigen Erlebnis ver­wechseln.»* Ich habe diese Bemerkung gemacht, nicht weil ich glaube, daß jemand, der meine früheren Darlegungen mit wahrem Verständnisse liest, zu der Meinung kommen könne, ich behaupte, man könne Farben ohne Augen sehen, sondern weil ich mir denken konnte, es möchte da oder dort jemand bei flüchtigem Lesen durch Mißverstand mir eine sol­che Behauptung unterschieben, wenn ich nicht ausdrück­lich sage, daß ich sie für unberechtigt halte.",
        "Drei Jahre spä­ter, nachdem ich diese Unterschiebung ausdrücklich abge­wehrt habe, kommt Max Dessoir und erzählt, ich behaupte, was ich in Wirklichkeit für töricht halte."
      ],
      [
        "* Vergleiche meine Schrift «Wie erlangt man Erkenntnisse der höheren Welten?» (19.",
        "Auflage , Seite 111, Anmerkung."
      ],
      [
        "Doch damit nicht genug.",
        "In der sechsten Auflage meines Buches «Theosophie », die ebenfalls 1914 erschienen ist, findet sich über die besprochene Sache das Folgende: « Man kann zu der Vorstellung kommen, als ob dasjenige, was hier als geschildert wird, vor der Seele so stünde, wie eine physische Farbe vor dem Auge steht."
      ],
      [
        "Eine solche wäre aber nichts als eine Halluzination.",
        "Mit Eindrücken, die sind, hat die Geisteswis­senschaft nicht das geringste zu tun.",
        "Und sie sind jedenfalls in der hier vorliegenden Schilderung nicht gemeint."
      ],
      [
        "Man kommt zu einer richtigen Vorstellung, wenn man sich das Folgende gegenwärtig hält.",
        "Die Seele erlebt an einer phy­sischen Farbe nicht nur den sinnlichen Eindruck, sondern sie hat an ihr ein seelisches Erlebnis."
      ],
      [
        "Dieses seelische Er­lebnis ist ein anderes, wenn die Seele - durch das Auge - eine gelbe, ein anderes, wenn sie eine blaue Farbe wahr­nimmt.",
        "Man nenne dieses Erlebnis das oder das .",
        "Die Seele nun, welche den Er­kenntmmispfad betreten hat, hat ein gleiches gegenüber den aktiven Seelenerlebnissen anderer Wesen; ein gegenüber den hinge­bungsvollen Seelenstimmungen."
      ],
      [
        "Das Wesentliche ist nicht, daß der bei einer Vorstellung einer ande­ren Seele so sieht, wie er dies in der phy­sischen Welt sieht, sondern daß er ein Erlebnis hat, das ihn berechtigt, die Vorstellung zu nennen, wie der physische Mensch einen Vorhang zum Beispiel nennt.",
        "Und weiter ist es wesentlich, daß der sich be­wußt ist, mit diesem seinem Erlebnis in einem leibfreien Er­leben zu stehen, so daß er die Möglichkeit empfängt, von dem Werte und der Bedeutung des Seelenlebens in einer"
      ],
      [
        "Welt zu sprechen, deren Wahrnehmung nicht durch den menschlichen Leib vermittelt ist.»*"
      ],
      [
        "Ich verzichte darauf, noch anderes aus meinen Schriften anzuführen, das in der berührten Sache meine wirkliche Ansicht darstellen kann.",
        "Und ich überlasse es jedem Leser, der noch ein sachliches Urteil über Tatsachen auch dann sich bil­den kann, wenn von Anthroposophie die Rede ist, - zu be­urteilen, was über die «Wiedergabe» meiner Darstellung durch Max Dessoir zu denken ist."
      ],
      [
        "Auf den Grad des Verständnisses, welchen Dessoir der von mir versuchten Schilderung des durch Geistorgane er­langten Bewußtseins entgegenbringt, wirft ein recht ver­hängnisvolles Licht, was er im weiteren seiner Darstellung über die Beziehung der «imaginativen» Vorstellung zu ei­ner ihnen entsprechenden geistigen Wirklichkeit vorbringt.",
        "Er hat vernommen, daß Anthroposophie die Entwickelung des Menschentums auf der Erde nicht allein mit den Mitteln erklärt, welche in der Anthropologie angewendet werden, sondern daß sie durch ihre Mittel diese Entwickelung in Abhängigkeit von geistigen Kräften und Wesenheiten er­schaut.",
        "In meinem Buche « Geheimwissenschaft im Umriß» habe ich versucht, diesen menschlichen Entwickelungsvor­gang anschaulich zu machen durch «imaginative» Vorstel­lungen (übrigens auch durch Erkennmisarten, die über das"
      ],
      [
        "* Vergleiche meine «Theosophie».",
        "Einführung in übersinnliche Welterkenntnis und Menschenbestimmung (28.Auflage 1955, Seite 154).",
        "In mei­nem Buche «Die Geheimwissenschaft im Umriß», das 1913 in 5.",
        "Auflage erschienen ist, steht eine ebensolche Ausführung über das Schauen von Far­ben auf Seite 421 f. (26.",
        "Auflage 1955, Seite 418 f.).",
        "Nun liegt das schier Un­glaubliche vor, daß Max Dessoir diese 5.",
        "Auflage auf Seite 254 seines Buches als eine der Schriften anführt, die er benützt haben will.",
        "Er behauptet also, daß jeh etwas sage, wovon in meinem von ihm selbst zitierten Buch das genaue Gegenteil steht."
      ],
      [
        "imaginative Anschauen hinausliegen, was aber für das hier zu Besprechende weniger in Betracht kommt).",
        "Ich habe in dem genannten Buche angedeutet, wie sich dem anthropo­sophischen Anschauen ein Bild ergibt von den Zuständen, welche die Menschheit durchlebt hat in Entwickelungsfor­men, die den gegenwärtigen schon nahe stehen, und ich habe auch hingewiesen auf solche ältere Entwickelungsfor­men, in denen der Mensch in einer Art auftritt, welche der gegenwärtigen sehr unähnlich ist, und die nicht durch die dem sinnlichen Wahrnehmen entlehnten Vorstellungen der Anthropologie, sondern durch imaginative Vorstellungen von mir geschildert werden. - Dessoir unterrichtet nun seine Leser über dasjenige, was ich über die Menschheitsentwickelung ausgeführt habe, in der folgenden Art."
      ],
      [
        "Meine Darstellung der Entwickelungsformen, welche der gegen­wärtigen Menschenbildung noch nahe stehen, gibt er so an , daß ich für eine bestimmte Zeitperiode in der Vergangen­heit eine altindische Kultur der Menschheit annehme und dann andere Kulturperioden darauf folgen lasse.",
        "Bei Dossier heißt es: «Alt-Indien ist nicht das jetzige Indien, wie denn überhaupt alle geographischen, astronomischen, hi­storischen Bezeichnungen sinnbildlich zu verstehen sind."
      ],
      [
        "Auf die indische Kultur folgte die urpersische, geführt von Zarathustra, der aber viel früher lebte als die in der Ge­schichte diesen Namen tragende Persönlichkeit.",
        "Andere Zeitabschnitte schlossen sich an."
      ],
      [
        "Wir stehen in der sechsten Periode.»* - Was ich über eine viel ältere Zeit der Mensch­heitsentwickelung sage, in der diese noch in Formen zutage trat, die den gegenwärtigen sehr unähnlich sind, darüber berichtet Dessoir so: «Dieser Mensch hat sich herausgebil­det"
      ],
      [
        "* Vergleiche Seite 258 f. des Dessoirschen Buches."
      ],
      [
        "in einer urfernen Vergangenheit, die Steiner das lemu­rische Zeitalter der Erde nennt - warum wohl? -, und in ei­nem Lande, das damals zwischen Australien und Indien lag (was also eine richtige Ortsbestimmung und kein Symbol ist).»* - Ich will nun hier ganz davon absehen, daß ich diese «Wiedergaben» des von mir Dargestellten auch im ganzen nur als Zerrbilder ansehen kann, die völlig unge­eignet sind, irgend einem Leser ein Bild von dem zu ge­ben, was ich meine.",
        "Ich will nur über einen Punkt dieser «Wiedergaben» sprechen.",
        "Dessoir ruft in seinem Leser den Glauben hervor, ich spreche davon, daß das im Geiste Geschaute sinnbildlich (symbolisch) zu verstehen sei, daß also Alt-Indien, wohin ich eine alte Menschheitskultur ver­lege, ein « symbolisches Land» sei.",
        "Später findet er es ta­delnswert, daß ich eine viel ältere menschliche Entwicke­lungsperiode nach Lemurien - zwischen Australien und Indien - verlege und dabei mir selbst in grausamer Weise widerspreche, da man doch aus meiner Darstellung mer­ken könne, daß ich Lemurien für eine richtige Ortsbestim­mung und kein Symbol halte."
      ],
      [
        "Es ist durchaus zuzugeben, daß ein Leser des Dessoir­schen Buches, der nichts von mir gelesen hat, und bloß Des­soirs Bericht entgegennimmt, zu der Ansicht kommen muß, meine Darstellung sei ganz undurchdachtes, verworrenes und in sich selbst widerspruchsvolles Zeug. - Was steht aber über das von mir als Alt-Indien gekennzeichnete Er­dengebiet wirklich in meinem Buche?",
        "Man lese die betreffen­den Ausführungen nach, und man wird finden, daß ich mit vollkommener Deutlichkeit zum Ausdruck bringe, wie Alt-Indien kein Symbol, sondern das Erdgebiet ist, das,"
      ],
      [
        "* Vergleiche Seite 261 des Dessoirschen Buches."
      ],
      [
        "wenn auch nicht ganz genau, so doch im wesentlichen mit dem zusammenfällt, das jedermann Indien nennt.* Dessoir berichtet also seinem Leser als meine Ansicht et­was, was mir auch nie eingefallen ist, vorzustellen.",
        "Und weil er findet, daß ich bei der Schilderung vom alten Le­murien wohl so spreche, wie es mit meiner wirklichen Mei­nung vom alten Indien zusammenstimmt, nicht aber mit dem Unsinn, den er mich sagen läßt, zeiht er mich des Wi­derspruches.**"
      ],
      [
        "Man fragt sich, wie kommt das Unglaubliche zustande , daß mich Dessoir behaupten läßt, Alt-Indien sei «sinnbild­lich» zu verstehen.",
        "Mir ergibt sich darüber aus dem ganzen Zusammenhange seiner Darstellung das Folgende.",
        "Dessoir hat etwas gelesen über die Vorgänge im Seelenleben, die ich kennzeichne als den Weg zum geistigen Schauen, dessen erste Stufe das imaginative Erkennen ist.",
        "Ich schildere da, wie die Seele durch ruhige Hingabe an gewisse Gedanken aus ihren Untergründen die Fähigkeit heraus entwickelt, imaginative Vorstellungen zu bilden.",
        "Ich sage, zu diesem Ziele ruhe die Seele am besten in sinnbildlichen Vorstellun­gen.",
        "Niemand sollte durch meine Darstellung auf den Irr­tum verfallen, die sinnbildlichen Vorstellungen seien etwas anderes als das Mittel, um zum imaginativen Erkennen zu kommen.",
        "Dessoir meint nun, weil man mittels Sinnbildern zum imaginativen Vorstellen kommt, bestehe dies letztere auch nur in Sinnbildern, ja er schreibt mir die Ansicht zu , wer sich seiner Geistorgane bedient, schaue nicht durch die"
      ],
      [
        "* Vergleiche meine «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Stuttgart, 1955, Seite 275 f."
      ],
      [
        "** Vergleiche meine «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 259."
      ],
      [
        "imaginativen Vorstellungen auf Wirklichkeiten, sondern nur auf Sinnbilder."
      ],
      [
        "Meiner Darlegung gegenüber ist die Dessoirsche Be­hauptung, ich weise in solchen Fällen wie beim alten Indien auf Sinnbilder hin, nicht auf Wirklichkeiten, nur mit dem Folgenden zu vergleichen.",
        "Jemand findet aus der Beschaf­fenheit eines Stückes Erdboden, daß es in der Gegend, in der er sich befindet, vor kurzer Zeit geregnet haben müsse.",
        "Er teilt das einem anderen mit.",
        "Er kann diesem selbstver­ständlich nur seine Vorstellung davon mitteilen, daß es ge­regnet hat.",
        "Deshalb behauptet ein Dritter, der Erste sage, die Beschaffenheit des Erdbodens rühre nicht von einem wirklichen Regen her, sondern von der Vorstellung des Regens.",
        "Ich behaupte weder, daß die imaginativen Vorstellun­gen in bloßen Sinnbildern sich erschöpfen, noch daß sie selbst eine Wirklichkeit sind, sondern daß sie sich auf eine Wirklichkeit beziehen, wie das bei den Vorstellungen des gewöhnlichen Bewußtseins auch der Fall ist.",
        "Und mir un­terstellen, ich weise nur auf sinnbildliche Wirklichkeiten hin, kommt gleich der Behauptung, der Naturforscher sehe nicht in dem Wesenhaften, auf das er sich durch seine Vor­stellung bezieht, sondern in diesen selbst die Wirklichkeit."
      ],
      [
        "Wenn man Anschauungen, die man bekämpfen will, so darstellt, wie dies durch Dessoir geschieht, so ist der Kampf recht leicht.",
        "Und Max Dessoir macht es sich wirklich leicht, sich mit vornehmer Art auf den kritischen Richterstuhl zu setzen; aber er erreicht dies nur dadurch, daß er meine Dar­legung erst in ein Zerrbild, ja oft in eine völlige Torheit ver­kehrt, und dann diese seine eigene Schöpfung abkanzelt.",
        "Er sagt: «Es ist widerspruchsvoll, daß aus und nur gemeinten Sachverhalten die Tatbestände"
      ],
      [
        "der Wirklichkeit sich entwickelt haben sollen.»* Doch ist solch widerspruchsvolle Art des Vorstellens bei mir nir­gends zu finden.",
        "Daß meine Darstellung sie enthält, ist eine Unterschiebung Dessoirs.",
        "Und wenn dieser gar sich zu der Behauptung versteigt: «Denn nicht darum handelt es sich , ob man das Geistige als Gehirntätigkeit ansieht oder nicht, sondern darum, ob das Geistige in den Formen kindlicher Vorstellungsweise oder als ein Reich eigener Gesetzmäßig­keit zu denken ist, »** so muß darauf erwidert werden: Ich bin mit ihm ganz einverstanden, daß sich alles das, was er seinen Lesern als meine Meinung auftischt, in den Formen kindlicher Vorstellungsweise hält; doch hat das von ihm also Bezeichnete nichts mit meinen wirklichen Ansichten zu tun, sondern bezieht sich restlos auf seine eigenen Vorstel­lungen, die er sich, die meinigen entstellend, gebildet hat."
      ],
      [
        "Wie ist es nur möglich, daß ein Gelehrter so verfährt?",
        "Ich muß, um etwas für eine Antwort auf diese Frage zu tun, den Leser für kurze Zeit in ein Gebiet führen, das diesem viel­leicht nicht kurzweilig erscheinen wird, das ich aber hier be­treten muß, um zu zeigen, auf welche Art Max Dessoir die Bü­cher liest, über die er sich zum Kritiker aufwirft.",
        "Ich muß ge­genüber den Dessoirschen Ausführungen ein wenig Philo­logie dem Leser vorführen."
      ],
      [
        "Meine Entwickelung der menschlichen Kulturperioden in einer gewissen Zeit schildert Dessoir, wie schon erwähnt , so: «Auf die indische Kultur folgte die urpersische ...",
        "An­dere Zeitabschnitte schlossen sich an.",
        "Wir stehen in der sechsten Periode. »*** Nun könnte es recht unbedeutend erscheinen,"
      ],
      [
        "* Vergleiche Seite 263 des Dessoirschcn Buches."
      ],
      [
        "** Seite 263 des Dessoirschen Buches."
      ],
      [
        "*** Vergleiche Seite 258 f. des Dessoirschen Buches."
      ],
      [
        "jemand vorzuwerfen, er lasse mich sagen: «Wir stehen in der sechsten Periode», während ich mit aller nur denkbaren Klarheit ausführe, daß wir in der fünften stehen.",
        "Aber in diesem Falle ist die Sache doch nicht unbedeutend."
      ],
      [
        "Denn wer in den ganzen Geist meiner diesbezüglichen Dar­stellung eingedrungen ist, der muß zugeben, daß jemand, dem auch nur beifällt, ich rede von der sechsten Periode als der gegenwärtigen, meine ganze Auseinandersetzung in der allergröbsten Weise mißverstanden hat.",
        "Daß ich die gegen­wärtige Periode als die fünfte bezeichne, hängt ganz inner­lich mit dem diesbezüglich von mir Auseinandergesetzten zusammen. - Wie kommt Dessoir zu seinem groben Mißverständnis?"
      ],
      [
        "Man kann sich darüber eine Vorstellung bil­den , wenn man meine Darstellung der Sache mit seiner «Wiedergabe» vergleicht und dabei etwas nach philologi­scher Methode prüfend zu Werke geht. - Da, wo ich in mei­ner Schilderung der Kulturperioden zu der vierten komme, die ich im achten Jahrhundert v.",
        "Chr. beginnen und etwa im vierzehnten oder fünfzehnten Jahrhundert n."
      ],
      [
        "Chr. schließen lasse, sage ich das Folgende: «Im vierten, fünften und sech­sten Jahrhundert n.",
        "Chr. bereitete sich in Europa ein Kul­turzeitalter vor, in welchem die Gegenwart noch lebt.",
        "Es sollte das vierte, das griechlsch4ateinische allmählich ablö­sen."
      ],
      [
        "Es ist das fünfte nachatlantische Kulturzeitalter.»* Meine Meinung ist demnach, daß durch die Vorgänge im vierten, fünften und sechsten Jahrhundert sich Wirkungen vorbereiteten, die zu ihrem Ausreifen noch einige Jahrhun­derte brauchten, um dann im vierzehnten Jahrhundert den Übergang zum fünften Kulturzeitalter zu machen, in dem wir gegenwärtig noch leben.",
        "Die obige Stelle scheint nun"
      ],
      [
        "* Vergleiche meine «Geheimwissenschaft im Umriß», Seite 294 f."
      ],
      [
        "Max Dessoir obenhin lesend so in den Bereich seiner Auf­merksamkeit hineingebracht zu haben, daß er die Aufeinan­derfolge des vierten, fünften und sechsten Jahrhunderts mit der Aufeinanderfolge der Kulturzeitalter verwechselt hat.",
        "Wenn jemand oberflächlich liest und außerdem kein Verständnis für das Gelesene hat, so kann dergleichen geschehen."
      ],
      [
        "Ich würde nicht ohne weiteres diese Hypothese von der Oberflächlichkeit Max Dessoirs hier aussprechen, wenn sie nicht gestützt würde durch die folgenden Entdeckungen, die man an der «Wiedergabe» meiner Anschauungen durch ihn machen kann.",
        "Ich muß, um die in Betracht kommenden Dinge zu besprechen, Vorstellungen anführen, die Erkennt­nisse der Anthroposophie betreffen, deren Verständnis kaum möglich ist, wenn sie nicht im Zusammenhang mit den zu ihnen weisenden Ausführungen meiner «Geheimwissenschaft» ins Auge gefaßt werden.",
        "Ich selbst würde sie niemals so aus allem Zusammenhang herausgerissen, einem Leser oder Zuhörer vorführen, wie dies Max Dessoit tut.",
        "Allein da er seine Kritik auf seine «Wiedergabe» der bei mir in einem weit ausholenden Zusammenhange dargestellten Ansichten begründet, muß ich hier auf diese «Wiedergabe» zu sprechen kommen.",
        "Ich muß daran zeigen, welcher Art diese «Wiedergabe » ist.",
        "Voraus bemerken muß ich, daß die Darstellung solcher Dinge deshalb grolle Schwierigkeiten macht, weil der Inhalt der geistigen Beobachtung nur dann einigermaßen klargestellt werden kann, wenn man sich ei­ner möglichst genauen Ausdrucksart befleißigt.",
        "Ich versu­che daher stets, wenn ich solche Dinge darstelle, keinen Zeitaufwand zu scheuen, um der sprachlichen Ausdrucks­form soviel als mir möglich ist, an Genauigkeit abzugewin­nen.",
        "Wer nur ein wenig in den Geist der Anthroposophie eindringt,"
      ],
      [
        "wird Verständnis für das haben, was ich eben gesagt habe. - Demgegenüber will ich nun zeigen, wie Max Dessoir bei seiner «Wiedergabe» meiner Darstellungen verfährt.*"
      ],
      [
        "Mit Bezug auf den Weg, den die Seele zur Erlangung des Gebrauchs der Geistorgane macht, stellt er meine An­schauung in der folgenden Art dar: « Die Schulung zur höheren Bewußtseinsverfassung beginnt - wenigstens für den Menschen der Gegenwart - damit, daß man mit aller Kraft sich in eine Vorstellung als in einen rein seelischen Tatbestand versenkt.",
        "Am besten eignet sich eine sinnbild­liche Vorstellung, etwa die eines schwarzen Kreuzes (Sym­bol"
      ],
      [
        "* Es darf vielleicht hier auf etwas hingewiesen werden, das in den Krei­sen, in denen man oft die anthroposophischen Versuche auf ihren philoso­phisch-wissenschaftlichen Wert hin beurteilen will, nicht ins Auge gefaßt wird.",
        "Ich möchte diesen Hinweis schon aus dem Grunde nicht unterlassen, weil bei einigen leicht der Glaube entstehen könnte, meine gegen Dessoir vorgebrachten Darlegungen seien gar zu sehr ein pedantisches Pochen auf meinen Wortlaut."
      ],
      [
        "In der Anthroposophie hat man es zu tun mit Darstellun­gen des Geistigen.",
        "Man muß sich dabei der Worte, ja der Wortfügungen der gewöhnlichen Sprache bedienen.",
        "Man kann in diesen aber durchaus nicht immer adäquate Bezeichnungen finden für dasjenige, worauf die Seele gerichtet ist, wenn sie Geistiges schaut."
      ],
      [
        "Die im Geistigen herrschenden Be­ziehungen, die besondere Art desjenigen, was man da «Wesen» und Vorgänge nennen kann, ist viel komplizierter, feiner, vielgestaltiger als dasje­nige, was im gewöhnlichen Sprachgebrauch zum Ausdruck kommt.",
        "Man gelangt nur zum Ziele, wenn man die Möglichkeiten ausnutzt, die in der Sprache liegen in bezug auf Satzwendungen, Wortumstellungen; wenn man sich bemüht, dasjenige, was ein Satz nicht adäquat aussprechen kann, durch einen hinzugefügten zweiten im Zusammenhang mit dem ersten zum Ausdruck zu bringen."
      ],
      [
        "Zum Verständnis der Anthroposophie ist durchaus nötig, auf solche Dinge einzugehen.",
        "Es kann zum Beispiel der Fall eintreten, daß ein geistiger Tatbestand ganz schief gesehen wird, wenn man die Ausdrucksform nicht als etwas Wesentliches ansieht."
      ],
      [
        "Dessoir ist nicht einmal im ent­ferntesten darauf gekommen, daß so etwas zu berücksichtigen wäre.",
        "Er scheint überall vorauszusetzen, daß, was ihm unverständlich ist, auf dem kindlichen Denken, auf der primitiven Methode des andern beruht."
      ],
      [
        "für vernichtete niedere Triebe und Leidenschaften), dessen Schneidestelle von sieben roten Rosen umgeben ist (Symbol für geläuterte Triebe und Leidenschaften.»* Ab­gesehen davon, daß eine solche Behauptung, aus dem Zu­sammenhang gerissen, einen absonderlichen Eindruck auf einen Leser machen muß, während sie dies kaum tun wird an der Stelle der Auseinandersetzungen, an der sie in mei­nem Buche steht, muß ich sagen: läse ich das, was Max Dessoir in dem obigen Satze sagt, als die Meinung eines Menschen, ich hielte die Sache für Unsinn, oder, zum min­desten, für unsinnig ausgedrückt.",
        "Denn ich könnte keinen Zusammenhang finden zwischen den Bedeutungen des Doppelsymbols, zwischen «vernichteten niederen Trieben und Leidenschaften» und «geläuterten Trieben und Lei­denschaften»."
      ],
      [
        "Ich mußte mir ja geradezu vorstellen: der Mensch solle seine niederen Triebe und Leidenschaften vernichten, und an der Stelle, an der die Vernichtung angerichtet worden ist, erschienen, wie aus dem Nichts her­vorgeschossen, geläuterte Triebe und Leidenschaften.",
        "Aber warum «geläutert», da doch nichts zu «läutern» war, sondern am Orte der Vernichtung etwas Neues entstanden ist."
      ],
      [
        "Mein Denken käme auf keinen Fall mit einem solchen Satze zurecht.",
        "Aber man lese doch den Satz in meinem Bu­che.",
        "Da steht: «Man stelle sich ein schwarzes Kreuz vor.",
        "Dieses sei Sinnbild für das vernichtete Niedere der Triebe und Leidenschaften; und da, wo sich die Balken des Kreu­zes schneiden, denke man sich sieben rote, strahlende Ro­sen im Kreise angeordnet.»** - Man sieht: ich sage nicht,"
      ],
      [
        "* Vergleiche Seite 255 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche meine « Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 311."
      ],
      [
        "das Kreuz sei Sinnbild für «vernichtete niedere Triebe und Leidenschaften», sondern für «das vernichtete Niedere der Triebe und Leidenschaften».",
        "Also die niederen Triebe und Leidenschaften werden nicht «vernichtet», sondern «ver­wandelt »,so daß ihr Niederes abgestreift wird, und sie selbst als geläutert auftreten.",
        "So macht sich Max Dessoir erst das zurecht, was er kritisieren will.",
        "Dann kann er es als eine «kindliche Vorstellungsweise» ausgeben.",
        "Es ist sicherlich pedantisch, wenn man in dieser Weise - schulmäßig - Kor­rektur übt an einem Wortlaute.",
        "Aber nicht ich bin der Ver­anlasser dieser schulmäßigen Korrektur.",
        "Was sie notwen­dig macht, sind die Dessoirschen Entstellungen, die nur durch solche Schulmäßigkeit zu fassen sind.",
        "Denn sie kom­men - meinetwegen unbewußten oder durch Oberfläch­lichkeit erzeugten - Fälschungen meines Wortlautes gleich.",
        "Und nur diesem gefälschten Wortlaut gegenüber ist die Dessoirsche Kritik möglich."
      ],
      [
        "Ein anderer Fall der Dessoirschen «Wiedergabe » ist der folgende.",
        "Ich spreche - wieder in einem Zusammenhange, der die Sache ganz anders erscheinen läßt, als wenn man sie in Dessoirscher Art aus diesem Zusammenhange her­ausreißt - von gewissen früheren Entwickelungszuständen, welche die Erde durchgemacht hat, bevor sie der Pla­net geworden ist, als welcher sie für den Menschen in sei­ner gegenwärtigen Entwickelungsform bewohnbar ist.",
        "Ich schildere durch imaginative Vorstellungen, wie der erste dieser Entwickelungszustände war.",
        "Ich habe nötig, diese Zustände zu veranschaulichen dadurch, daß ich von Wesen geistiger Art spreche, die mit der damaligen planetarischen Urform der Erde in Zusammenhang standen.",
        "Abgesehen nun davon, daß Dessoir mich behaupten läßt, durch diese"
      ],
      [
        "geistartigen Wesen «entwickelten» sich «Nahrungs- und Ausscheidungsprozesse » auf der planetarischen Urform der Erde, sagt er weiter: «Von diesen Zuständen erfährt der Hellsichtige noch heute durch eine dem Riechen ähn­liche übersinnliche Wahrnehmung, denn die Zustände sind eigentlich immer da.»* In meinem Buche ist zu lesen, daß die gemeinten geistartigen Wesen in Wechselwirkung tre­ten mit den im Innern der planetarischen Urform «vorhan­denen, auf- und abwogenden Geschmackskräften.",
        "Da­durch kommt ihr Äther- oder Lebensleib in eine solche Tä­tigkeit, daß man diese als eine Art Stoffwechsel bezeichnen kann.»** Dann sage ich, diese Wesen bringen Leben in das Innere der planetarischen Urform."
      ],
      [
        "«Es geschehen dadurch Nahrungs- und Ausscheidungsprozesse.»*** Es ist selbst­verständlich, daß gegenüber einer solchen Schilderung von Seite der gegenwärtigen Wissenschaft die schärfste Ableh­nung möglich ist.",
        "Allein es sollte ebenso selbstverständ­lich sein, daß ein Kritiker es nicht so machen darf wie Max Dessoir."
      ],
      [
        "Er sagt, indem er den Glauben erweckt, daß er meine Darstellung wiedergibt, es entwickeln sich durch die gemeinten Wesen Nahrungs- und Ausscheidungspro­zesse.",
        "So wie bei mir die Sache dargestellt ist, steht zwi­schen der Angabe, daß die Wesen auftreten und derjeni­gen, daß Nahrungs- und Ausscheidungsprozesse entste­hen, der Zwischensatz, der besagt, daß sich eine Wechsel­wirkung entwickelt und daß durch diese in dem Äther- oder Lebensleib dieser Wesen eine Tätigkeit auftritt, die ihrerseits"
      ],
      [
        "* Vergleiche Seite 258 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche meine «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 166 f."
      ],
      [
        "*** An derselben Stelle meiner «Geheimwissenschaft» wie das vorige."
      ],
      [
        "nun wieder zu den Nahrungs- und Ausscheidungsprozesse der planetarischen Urform führt.",
        "Was Dessoir mit meiner Darstellung vollführt, läßt sich mit dem Fol­genden vergleichen.",
        "Jemand sagt: Ein Mann tritt in ein Zimmer, in dem sich ein Kind und dessen Vater befinden."
      ],
      [
        "Das Kind benimmt sich dem Eintretenden gegenüber so, daß der Vater es strafen muß.",
        "Diesen Satz entstellt nun ein anderer, indem er behauptet: durch das Eintreten des fremden Mannes entwickelt sich die Strafe des Kindes."
      ],
      [
        "Könnte nun jemand aus dieser Behauptung erkennen, was der erste eigentlich hat sagen wollen?",
        "Doch Dessoir läßt mich ferner sagen, der Hellsichtige erfahre von gewissen Zuständen, die in der planetarischen Urform auftreten, durch «eine dem Riechen ähnliche Wahrnehmung».* Bei mir ist aber zu lesen, daß sich in den entsprechenden Zu­ständen willensartige Kräfte offenbaren, die sich «dem hellseherischen Wahrnehmungsvermögen durch Wirkun­gen» kundgeben, welche «sich mit verglei­chen lassen ».** Also bei mir ist nichts zu finden von der Behauptung, daß die in Frage kommende geistige Wahr­nehmung eine «dem Riechen ähnliche » ist, sondern es tritt deutlich hervor, daß diese Wahrnehmung nicht dem Rie­chen ähnlich ist, daß aber dasjenige, was wahrgenommen wird, sich mit «Gerüchen» vergleichen lasse."
      ],
      [
        "Wie im anthro­posophischen Sinne ein solcher Vergleich aufzufassen ist, ist an anderem Orte dieser Schrift genugsam gezeigt.",
        "Doch Dessoir verschafft sich durch die Entstellung meines Wortlautes die Möglichkeit, die folgende - ihm wahrscheinlich"
      ],
      [
        "* Vergleiche Seite 258 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche meine «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 168."
      ],
      [
        "geistreich dünkende - Bemerkung anzubringen: «Mich wundert, daß hiermit der und der nicht in Verbindung gebracht wird.» Ich könnte nun noch andere ähnliche Beispiele von Des­soirschen «Wiedergaben» meiner Darlegungen genauer anführen, zum Beispiel wie er mich «durch Abtrennung des Ätherleibes vom physischen Leib» das «Einschlafen» eines Beines erklären läßt, während ich nicht den objektiven Tatbestand des sogenannten Einschlafen dadurch erkläre, sondern sage, daß das subjektive «eigentümliche Gefühl, das man empfindet, von dem Abtrennen des Ätherleibes» herrührt.* Nur dann, wenn man den Wortlaut meiner Darstellung so nimmt, wie ich ihn gegeben habe, kann man sich eine Meinung darüber bilden, Weiche Tragweite meiner Behauptung zukommt, und wie sie durchaus den durch die Naturwissenschaft festzustellenden objektiven Tatbestand nicht ausschließt, so wenig sie ausgeschlossen zu werden braucht von demjenigen, der die anthropologische Meinung vertritt.",
        "Das letztere aber will Dessoir seinen Lesern glauben machen.",
        "Doch ich will darauf verzichten, den Leser weiter mit derlei Korrekturen zu ermüden.",
        "Die vorgebrachten soll­ten nur zeigen, in welchem Grade oberflächlich Max Dessoir dasjenige liest, über das er sich zum Richter aufwirft."
      ],
      [
        "Ich will aber zeigen, wozu die Seelenverfassung führen kann, die aus solcher Oberflächlichkeit heraus zu Gericht sitzt.",
        "In meiner Schrift «Die geistige Führung des Men­schen und der Menschheit »** versuche ich darzulegen, wie"
      ],
      [
        "* Vergleiche meine «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 96."
      ],
      [
        "** «Die geistige Führung des Menschen und der Menschheit.» Geisteswissenschaftliche Ergebnisse über die Menschheits-Entwickelung von Ru­dolf Steiner (1911). 7.",
        "Auflage.",
        "Freiburg i.Br., 1956."
      ],
      [
        "die Kräfte des Vorstellungslebens, die nicht gleich bei der Geburt, sondern erst in späterem Lebensalter in das Bewußtsein des Kindes treten, schon tätig sind vor diesem be­wußten Aufleben, und wie in deren unbewußter Tätigkeit zum Beispiel bei dem Fortbilden des Nervensystems und anderem diese Kräfte in einer Art weisheitsvoll wirken, gegen welche das spätere bewußte Wirken von einem ge­ringeren Weisheitsgrade erscheint.",
        "Aus Gründen, deren Darlegung hier zu weit führen würde, komme ich zu der Ansicht, daß das bewußte Vorstellungsleben zwar die Weisheit fortentwickelt, welche in gewissen Bildungen des organischen Leibes in früher Kindheit tätig ist, daß sich aber dieses bewußte Vorstellungsleben zu jenem unbewuß­ten Weisheitswirken verhält wie zum Beispiel der Bau ei­nes von bewußter menschlicher Weisheit herrührenden Werkzeuges zu dem Wunderbau des menschlichen Gehir­nes.* Der Leser der oben genannten Schrift könnte wohl aus derselben ersehen, daß ich eine solche Behauptung nicht ausspreche als das Ergebnis eines «Einfalles», son­dern daß sie der Abschluß ist eines im Sinne der Anthro­posophie vorangegangenen Forschungsweges; auch wenn ich, wie natürlich ist, nicht in jeder meiner Schriften die Einzelheiten dieses Weges darstellen kann."
      ],
      [
        "In dieser Be­ziehung bin ich nun schon einmal darauf angewiesen, daß meine Schriften so genommen werden wie Teile eines Gan­zen, die sich gegenseitig stützen und tragen.",
        "Doch nicht darauf kommt es mir jetzt an, die Berechtigung dieser mei­ner Behauptung über unbewußte und bewußte Weisheit darzulegen, sondern auf etwas anderes, das sich Dessoir leistet, indem er die diesbezügliche Ausführung meines"
      ],
      [
        "* Vergleiche meine Schrift «Geistige Führung», 7.",
        "Auflage, Seite 20 ff."
      ],
      [
        "Buches in der folgenden Art seinen Lesern zurechtschnei­det: «Am engsten, heißt es, ist der Zusammenhang mit höheren Welten in den drei ersten Lebensjahren, in die kei­ne Erinnerung zurückreicht.",
        "Besonders ein Mensch, der selber Weisheit lehrt - so bekennt Herr Rudolf Steiner -, wird sich sagen: * - Man darf wohl fragen: welche Vorstellung mag sich in einem Leser des Dessoirschen Buches festsetzen, dem diese Sätze vor Augen treten?",
        "Kaum eine andere, als daß ich in derjenigen Schrift, die Veranlassung zu diesen Sätzen gegeben hat, von einer Beziehung der geistigen Welt zum erkennenden Menschen spreche, und dafür mich selbst als Beispiel anführe.",
        "Es ist selbstverständlich nicht schwierig, einen Menschen der Lächerlichkeit preiszuge­ben, dem man eine solche Geschmacklosigkeit vorwerfen kann.",
        "Wie aber ist die Sache wirklich?",
        "In meiner Schrift steht: «Man nehme an, ein Mensch habe Schüler gefun­den, einige Leute, die sich zu ihm bekennen.",
        "Ein solcher wird durch echte Selbsterkenntnis leicht gewahr werden , daß ihm gerade die Tatsache, daß er Bekenner gefunden hat, das Gefühl gibt: was er zu sagen habe, rühre nicht von ihm her.",
        "Es sei vielmehr so, daß sich geistige Kräfte aus höheren Welten den Bekennern mitteilen wollen, und diese finden in dem Lehrer das geeignete Werkzeug, um sich zu offenbaren. - Einem solchen Menschen wird der Gedanke nahetreten: Als ich ein Kind war, habe ich an mir durch"
      ],
      [
        "* Vergleiche Seite 260 des Dessoirschen Buches."
      ],
      [
        "Kräfte gearbeitet, die aus der geistigen Welt hereinwirk­ten, und das, was ich jetzt als mein Bestes geben kann, muß auch aus höheren Welten hereinwirken; ich darf es nicht als meinem gewöhnlichen Bewußtsein angehörig betrachten.",
        "Ja, ein solcher Mensch darf sagen: etwas Dämonisches, et­was wie ein Dämon - aber das Wort im Sinne einer guten geistigen Macht genommen - wirkt aus einer geistigen Welt durch mich auf die Bekenner. - So etwas empfand Sokrates ..."
      ],
      [
        "Viel hat man versucht, um diesen des Sokrates zu erklären.",
        "Aber man kann ihn nur erklären, wenn man sich dem Gedanken hingeben will, daß Sokrates so etwas empfinden konnte, wie aus obiger Be­trachtung sich ergibt. »* Man sieht, mir handelt es sich um eine Auffassung des Sokratischen Dämonions vom Ge­sichtspunkte der Anthroposophie."
      ],
      [
        "Über diesen Sokrati­schen «Dämon» gibt es viele Auffassungen.",
        "Man kann sich, wie gegen andere, so auch gegen die meinige sachlich wenden.",
        "Was aber macht Max Dessoir?",
        "Wo ich von So­krates spreche, wendet er die Sache so, als ob ich von mir selbst spreche, indem er den Satz prägt: « so bekennt Herr Rudolf Steiner» und die letzten zwei Worte sogar in Sperr­druck setzt."
      ],
      [
        "Womit hat man es hier zu tun?",
        "Doch mit nichts Geringerem als mit einer objektiven Unwahrheit.",
        "Ich überlasse es jedem billig Denkenden, sich selbst ein Urteil zu bilden über einen Kritiker, der sich solcher Mittel bedient."
      ],
      [
        "Aber die Sache ist damit nicht erschöpft.",
        "Denn, nach­dem Dessoir meine Auffassung des Sokratischen Dämo­nions in der angedeuteten Art gewendet hat, schreibt er weiter: «Die Tatsache also, daß der einzelne ein Träger"
      ],
      [
        "* Vergleiche meine genannte Schrift «Die geistige Führung...», 7.",
        "Auf­lage, Seite 30 f."
      ],
      [
        "überindividueller Wahrheiten ist, vergröbert sich hier zu der Vorstellung, daß eine dinglich gedachte Geisteswelt gleichsam durch Röhren oder Drähte mit dem Individuum verbunden sei: Hegels objektiver Geist verwandelt sich in eine Gruppe von Dämonen, und alle Schattengestalten ei­nes ungeläuterten religiösen Denkens treten wieder auf.",
        "Die Richtung im ganzen kennzeichnet sich als materialisti­sche Vergröberung seelischer Vorgänge und personifizie­rende Verflachung der geistigen Werte.»* - Solcher «Kri­tik» gegenüber hört wirklich jede Möglichkeit auf, sich mit dem Kritiker ernsthaft auseinanderzusetzen.",
        "Man be­denke doch, was hier eigentlich vorliegt.",
        "Ich spreche von dem Dämonion des Sokrates, von dem doch dieser selbst"
      ],
      [
        "- nach historischer Überlieferung - gesprochen hat.",
        "Max Dessoir legt mir unter, daß, wenn man so vom Dämonischen spricht, dann «verwandelt sich Hegels objektiver Geist in eine Gruppe von Dämonen ... »* Dessoir benutzt also seine sonderbare Abschwenkung von dem in Wahr­heit gemeinten Gedanken, um seinem Leser die Ansicht beizubringen, jemand sei berechtigt, von mir anzunehmen, ich sehe in Hegels objektivem Geist «eine Gruppe von Dä­monen». - Man stelle neben diese Dessoirsche Behaup­tung, was ich in meinem Buche «Die Rätsel der Philoso­phie» alles vorbringe, um von Hegels Ansicht über den «objektiven Geist» alles fernzuhalten, was diesem irgend­wie den Charakter des Dämonischen aufdrücken könnte.** Wer gegenüber dem von mir über Hegel Vorgebrachten"
      ],
      [
        "* Vergleiche Seite 260 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche im ersten Band meines Buches «Die Rätsel der Philoso­phie», 7.",
        "Auflage, die auf Seiten 234 gegebene Darstellung der Hegelschen Philosophie."
      ],
      [
        "sagt: der Vertreter der Anthroposophie habe Vorstellun­gen, durch die sich Hegels «objektiver Geist» in eine Gruppe von Dämonen verwandle, der behauptet eben eine objektive Unwahrheit.",
        "Denn selbst hinter der Ausrede kann er sich nicht verschanzen: ja, zwar stellt es Steiner anders dar, aber ich kann mir nur vorstellen, daß die Stei­nerschen anthroposophischen Voraussetzungen zu den von mir angegebenen Folgerungen führen.",
        "Er würde damit eben nur zeigen, daß er meine Ausführungen über He­gels «objektiven Geist» nicht in der Lage ist, zu verste­hen.",
        "Nachdem er seinen Sprung von Sokrates zu Hegel ge­macht hat, urteilt dann Max Dessoir weiter: «Aus der Un­fähigkeit zu sachlich angemessenem Verständnis entsprin­gen die durch keine wissenschaftlichen Bedenken gehemm­ten Phantasien ... »* - Wer meine Schriften liest und dann Dessoirs Darstellung meiner Anschauungen betrachtet, dürfte vielleicht doch einem solchen Satze gegenüber emp­finden, daß ich schon einiges Recht dazu habe, ihn so zu wenden: bei Max Dessoir entspringen aus der Unfähigkeit zu sachlich angemessenem Verständnis des in meinen Schriften Gesagten die oberflächlichsten, objektiv unwah­ren Phantasien über die Vorstellungen der Anthroposo­phie."
      ],
      [
        "Max Dessoir teilt seinen Lesern mit, daß er außer mei­ner «Geheimwissenschaft im Umriß, 5 .",
        "Auflage» noch «eine lange Reihe anderer Schriften benutzt» habe.** Bei seiner hier charakterisierten Art, sich «auszudrücken», kann man ja kaum feststellen, was er darunter versteht, er habe «eine lange Reihe» meiner Schriften «benutzt»."
      ],
      [
        "* Vergleiche Seite 26o des Dessoirschen Buches."
      ],
      [
        "** Vergleiche Seite 254 des Dessoirschen Buches."
      ],
      [
        "Ich habe mir den Abschnitt «Anthroposophie» seines Bu­ches daraufhin angesehen, von welchen meiner Schriften - außer der «Geheimwissenschaft im Umriß» - noch Spuren der Benutzung auftreten.",
        "Ich kann nur entdecken, daß die­se «lange Reihe» aus drei kleinen Schriften besteht: dem 64 Seiten umfassenden Büchlein «Die geistige Führung des Menschen und der Menschheit», dem 48 kleine Seiten umfassenden Abdruck meines Vortrages «Blut ist ein ganz besonderer Saft» und dem 46 Seiten umfassenden Schrift­chen «Reinkarnation und Karma»."
      ],
      [
        "Dazu erwähnt er noch in einer Anmerkung meine 1894 erschienene «Philosophie der Freiheit».* So sehr es mir widerstrebt, zu dieser An­merkung auch einige rein Persönliches betreffende Sätze zu sagen: ich muß es tun, weil auch in dieser Nebensache der Grad von wissenschaftlicher Genauigkeit, der Max Des­soir eigen ist, zum Ausdruck kommt.",
        "Er sagt: «In Steiners Erstling, der (Berlin 1894) fin­den sich nur Ansätze zur eigentlichen Lehre ...» Diese «Philosophie der Freiheit » nennt also Max Dessoir meinen « Erstling»."
      ],
      [
        "Die Wahrheit ist, daß meine schriftstellerische Tätigkeit mit meinen Einführungen in Goethes naturwissenschaftliche Schriften beginnt, deren erster Band 1883 erschienen ist, elf Jahre, bevor Dessoir meinen «Erstling» ansetzt.",
        "Diesem «Erstling» gehen voran: die ausführli­chen Einführungen zu drei Bänden von Goethes naturwissenschaftlichen Schriften, meine «Grundlinien einer Erkenntnistheorie der Goetheschen Weltanschauung» (1886), meine Schrift «Goethe als Vater einer neuen Ästhe­tik»(1889), meine für meine ganze Weltanschauung grundlegende Schrift «Wahrheit und Wissenschaft» (1892)."
      ],
      [
        "* Vergleiche Seite 254 des Dessoirschen Buches."
      ],
      [
        "hätte dieses Falles von Dessoirs sonderbarer Kenntnisnah­me dessen, worüber er schreibt, doch nicht Erwähnung getan, wenn nicht die Sache so läge, daß alle in meiner « Philosophie der Freiheit» vorgebrachten Grundanschau­ungen bereits in meinen früheren Schriften ausgesprochen und in dem genannten Buche nur in einer zusammenfas­senden und sich mit den philosophisch-erkenntnistheoretischen Ansichten vom Ende des neunzehnten Jahrhun­derts auseinandersetzenden Art vorgetragen sind.",
        "Ich wollte in dieser «Philosophie der Freiheit » in systematisch-organischer Gliederung zur Darstellung bringen, was ich in den früheren, fast ein ganzes Jahrzehnt umfassenden Veröffentlichungen an erkenntnistheoretischer Grundle­gung und an ethisch-philosophischen Folgerungen für eine auf die Erfassung der geistigen Welt zielende Anschauung niedergelegt hatte."
      ],
      [
        "Nachdem Max Dessoir in der angeführten Art über mei­nen «Erstling» gesprochen hat, fahrt er über denselben fort: «Es wird dort gesagt, daß der Mensch etwas aus der Natur in sich herübergenommen hat und daher durch die Erkenntnis des eigenen Wesens das Rätsel der Natur lösen kann; daß im Denken eine Schaffenstätigkeit dem Erken­nen vorangeht, während wir am Zustandekommen der Natur unbeteiligt und auf nachträgliches Erkennen ange­wiesen sind.",
        "Intuition gilt hier bloß als die Form, in der ein Gedankeninhalt zunächst hervortritt.» Man sehe nach, ob sich in meiner «Philosophie der Freiheit» etwas findet, das sich in diese ein Ungeheuerliches von Trivialität dar­stellenden Sätze zusammenfassen läßt.",
        "Ich habe in meinem Buche den Versuch gemacht, nach einer ausführlichen Auseinandersetzung mit andren philosophischen Richtungen,"
      ],
      [
        "zu zeigen, daß dem Menschen in der Sinnesbeobach­tung nicht die volle Wirklichkeit vorliegt, daß also das von den Sinnen gegebene Weltbild eine unvollständige Wirklich­keit ist.",
        "Ich habe mich bestrebt, darzulegen, daß die menschliche Organisation diese Unvollständigkeit notwendig macht."
      ],
      [
        "Nicht die Natur i>erbirgt dem Menschen dasjenige, was zu ihrem Wesen dem Sinnesbilde fehlt, son­dern der Mensch ist so geartet, daß er durch diese Artung auf der Stufe des bloß beobachtenden Erkennens sich selbst die geistige Seite des Weltbildes verhüllt.",
        "Im aktiven Denken beginnt dann die Erschließung dieser geistigen Seite."
      ],
      [
        "Es ist - im Sinne meiner Weltauffassung - im akti­ven Denken ein Wirkliches (Geistiges) unmittelbar gegen­wärtig' das im bloßen Beobachten noch nicht gegeben sein kann.",
        "Das ist gerade das Charakteristische dieser meiner erkenntnistheoretischen Grundlegung einer Geisteswis­senschaft, daß ich nicht in der Intuition - insoferne diese im Denken zum Ausdruck kommt - «bloß die Form» sehe, «in der ein Gedankeninhalt zunächst hervortritt»."
      ],
      [
        "Max Dessoir beliebt also seinen Lesern das Gegenteil von dem vorzusetzen, was in meiner «Philosophie der Freiheit» wirklich dargestellt ist. - Man sehe, um das zu bemerken , nur auf die folgenden meiner Gedanken: «In dem Denken haben wir das Element gegeben, das unsere besondere In­dividualität mit dem Kosmos zu einem Ganzen zusammenschließt.",
        "Indem wir empfinden und fühlen (auch wahrneh­men), sind wir einzelne, indem wir denken, sind wir das All-Eine Wesen, das alles durchdringt...» «Die Wahrneh­mung ist also nichts Fertiges, Abgeschlossenes, sondern die eine Seite der totalen Wirklichkeit."
      ],
      [
        "Die andre Seite ist der Begriff.",
        "Der Erkenntnisakt ist die Synthese von Wahrnehmung"
      ],
      [
        "und Begriff . . . »* «Im Gegensatz zum Wahrneh­mungsinhalte, der uns von außen gegeben ist, erscheint der Gedankeninhalt im Innern.",
        "Die Form, in der er zu­nächst auftritt, wollen wir als Intuition bezeichnen.",
        "Sie ist für das Denken, was die Beobachtung für die Wahrnehmung ist.",
        "Intuition und Beobachtung sind die Quellen unserer Erkenntnis.»** Ich sage also hier: Intuition wolle ich als Ausdruck für die Form gebrauchen, in der die im Gedan­keninhalt verankerte geistige Wirklichkeit zunächst in der menschlichen Seele auftritt, bevor diese erkannt hat, daß in dieser gedanklichen Innenerfahrung die in der Wahrneh­mung noch nicht gegebene Seite der Wirklichkeit enthal­ten ist.",
        "Deshalb sage ich: Intuition ist «für das Denken, was die Beobachtung für die Wahrnehmung ist».",
        "Also selbst, wenn Max Dessoir scheinbar wörtlich eines Andern Gedan­ken anführt, ist er imstande, das was dieser Andere meint, in das Gegenteil zu verkehren.",
        "Dessoir läßt mich sagen:"
      ],
      [
        "«Intuition gilt hier bloß als die Form, in der ein Gedankeninhalt zunächst hervortritt.»*** Den folgenden meiner Sät­ze, durch den dieses von ihm gebrauchte «bloß» zum Un­sinn wird, läßt er weg.",
        "Mir gilt eben Intuition nicht «bloß» als die «Form, in der ein Gedankeninhalt zunächst her­vortritt», sondern als die Offenbarung eines Geistig-Wirk­lichen, wie die Wahrnehmung als diejenige des Stofflich-Wirklichen.",
        "Wenn ich sage: die Uhr tritt zunächst als der Inhalt meiner Westentasche auf; sie ist für mich der Messer der Zeit; so darf nicht ein anderer behaupten, ich"
      ],
      [
        "* Vergleiche zu diesen Gedanken meine «Philosophie der Freiheit», 11.",
        "Auflage, Seiten 93 und 94."
      ],
      [
        "** Vergleiche «Philosophie der Freiheit», Seite 98."
      ],
      [
        "*** Vergleiche Seite 254 des Dessoirschen Buches."
      ],
      [
        "hätte gesagt: die Uhr ist «bloß» der Inhalt meiner Westen­tasche."
      ],
      [
        "Im Zusammenhange meiner Veröffentlichungen ist meine «Philosophie der Freiheit » die erkenntnistheoretischer Grundlegung für die von mir vertretene anthroposo­phisch orientierte Geisteswissenschaft.",
        "Ich habe dies in ei­nem besonderen Abschnitt meines Buches «Die Rätsel der Philosophie» dargelegt.* Ich habe in diesem Abschnitt ge­zeigt, wie ein gerader Weg von meiner Schrift «Wahrheit und Wissenschaft» und meinem Buche «Philosophie der Freiheit», nach meiner Auffassung, zur «Anthroposophie» führt."
      ],
      [
        "Doch Max Dessoir schafft sich die Möglichkeit, durch Nicht-Benutzung meines zweibändigen Buches über die «Rätsel der Philosophie» seinen Lesern allerlei leicht Mißzuverstehendes über die « lange Reihe» meiner drei kleinen Schriften «Die geistige Führung...», «Blut ist ein ganz be­sonderer Saft» und «Reinkarnation und Karma» zu erzäh­len.",
        "In der ersteren kleinen Schrift mache ich den Versuch, im geistigen Entwickelungsgange der Menschheit konkrete geistige Wesenskräfte als wirksam zu erkennen."
      ],
      [
        "Ich habe für den Leser nach meinen Vorstellungen klar gemacht, daß ich mir wohl bewußt bin, wie leicht gerade der Inhalt dieser Schrift mißverstanden werden kann.",
        "In der Vorrede sage ich ausdrücklich, daß jemand, der diese Schrift in die Hand bekommt, ohne deren Voraussetzungen zu kennen, sie «als kuriosen Ausfluß einer bloßen Phantastik ansehen» müßte."
      ],
      [
        "Ich bezeichne allerdings in dieser Vorrede nur das in meinen beiden Schriften «Theosophie» und «Geheimwissen­schaft» Enthaltene als diese Voraussetzungen.",
        "Das ist 1911"
      ],
      [
        "* Vergleiche das Schlußkapitel des zweiten Bandes meiner «Rätsel der Philosophie»."
      ],
      [
        "geschehen. 1914 ist mein Buch «Die Rätsel der Philosophie» als zweite Auflage meiner 1900 und 1901 erschienenen «Welt- und Lebensanschauungen im neunzehnten Jahrhun­dert» veröffentlicht worden.",
        "In diesen «Rätseln der Philo­sophie» habe ich auch dargestellt, wie die Atomenlehre ent­standen ist, wie sich Forscher wie Galilei in den geistigen Entwickelungsgang der Menschheit - nach meinen Vor­stellungen - eingliedern, ohne daß ich bei dieser Darstellung auf etwas anderes mich beziehe, als was mit Bezug auf die Entstehung der Atomenlehre oder auf die Stellung Galileis in der Wissenschaftsgeschichte «vor jedermanns Augen ... klar zutage» liegt.* Meine Darstellung ist zwar in meiner Art gehalten; aber ich beziehe mich bei dieser Darstellung auf nichts anderes, als was für einen gewöhnlichen Darstel­ler eines Abrisses der Philosophiegeschichte üblich ist."
      ],
      [
        "In meiner Schrift «Die geistige Führung ...» wird der Versuch gemacht, das, was ich selbst in einem anderen Buche so dar­zustellen bestrebt bin, wie es «vor jedermanns Augen» liegt, als Ergebnis konkreter geistiger Wesenskräfte, die im menschlichen Entwickelungsgange wirksam sind, darzu­stellen.",
        "Aus dem Zusammenhang, in dem diese Darstellung in meiner Schrift «Die geistige Führung ...» auftritt, heraus­gerissen, läßt sich - meiner Meinung nach - der bezügliche Gedanke nur in folgender Art wiedergeben: In der Geistes­geschichte der Menschheit wirken außer den Kräften, die sich für die gewöhnlichen historischen Methoden als für «jedermanns Augen . . . klar zutage» liegend ergeben, noch"
      ],
      [
        "* Vergleiche meine Darstellung der Atomenlehre in ihrer Entwickelung zum Beispiel «Die Rätsel der Philosophie». 1.",
        "Band, 7.",
        "Auflage, Seite 62 f. , meine Auffassung über Galilei zum Beispiel in demselben Band, Seite 104 f.",
        "Doch habe ich auch in meinen Einführungen und Anmerkungen zu Goe­thes «Naturwissenschaftlichen Schriften» von Galilei gesprochen."
      ],
      [
        "andere, nur der geisteswissenschaftlichen Forschung zu­gängliche (übersinnliche) Wesenskräfte.",
        "Und diese Wesenskräfte wirken nach bestimmten erkennbaren Gesetzen.",
        "In der Art, wie in derjenigen Entwickelungsperiode der Menschheit, die ich die ägyptisch-chaldäische nenne (vom vierten bis zum ersten vorchristlichen Jahrtausend), die Erkenntniskräfte wirken, sind solche Wesenskräfte erkenn­bar, die in dem Zeitalter, in dem die Atomenlehre entsteht, wieder, aber in einer anderen Tätigkeitsform, auftreten."
      ],
      [
        "In der Entstehung und Fortbildung des Atomismus sehe ich wirksam solche geistige Wesenskräfte, die in der Denkungsart des ägyptisch-chaldäischen Zeitalters in andrer Art schon wirksam waren.* - Wer auch nur ganz flüchtig auf meine Ausführungen eingeht, kann finden, daß die Geltend­machung geistiger Wirkenskräfte im Verfolg der Mensch­heitsentwickelung durch meine anthroposophischen Ge­sichtspunkte von mir nicht dazu getrieben wird, das rein historisch Beobachtbare durch allerlei Anthropomorphis­men oder Analogien zu vernebeln, oder in das Dämmerdun­kel einer falschen Mystik zu rücken.",
        "Max Dessoir findet möglich, mit Bezug auf das hier in Frage Kommende seinen Lesern die Worte vorzusetzen: «Nein - hier kann der ge­duldigste Berichterstatter seine Ruhe nicht länger bewah­ren."
      ],
      [
        "Vor jedermanns Augen liegt klar zutage, wie die Ato­menlehre entstanden ist und sich seit dem Altertum folgerecht entwickelt hat, und da kommt jemand und ruft den geheimnisvollen großen Unbekannten zu Hilfe ! »** - Wer meine «Rätsel der Philosophie» liest, sieht, daß, was vor jedermanns"
      ],
      [
        "* Vergleiche meine Schrift «Die geistige Führung...», 7.",
        "Auflage, Seite 65 f."
      ],
      [
        "** Vergleiche Seite 259 des Dessoirschen Buches."
      ],
      [
        "Auge liegt, auch von mir in dem Sinne dargestellt wird, wie es eben vor jedermanns Auge liegt; und daß ich für diejenigen Menschen, die verstehen können, daß das vor jedermanns Augen Liegende ein nicht vor Augen Liegen­des birgt, auf dieses dem geistigen Schauen Zugängliche hinweise.",
        "Und mein Hinweis ist nicht der auf einen «ge­heimnisvollen Unbekannten», sondern eben auf etwas, das durch die anthroposophischen Gesichtspunkte erkannt wird.*"
      ],
      [
        "Daß das, was ich in einem oben angeführten Beispiele von Sokrates sage, Max Dessoir so wendet, als ob ich von mir selbst spreche, habe ich als unzulässig nachgewiesen.",
        "Daß aber die Bemerkung, die Max Dessoir auf Seite 34 seines Buches macht, auf niemand andern als auf ihn selbst zu be­ziehen ist, geht wohl aus dem Zusammenhange hervor.",
        "Um diese Bemerkung zu verstehen, muß man ins Auge fassen, daß Dessoir im Bewußtseinsaugenblick zwei Gebiete unter­scheidet, ein Mittelfeld und die Randzone.",
        "Die Bewußt­seinsinhalte bewegen sich, so führt er aus, immerwährend von einem dieser Gebiete in das andere.",
        "Nur erhalten diese Inhalte, wenn sie in die Randzone eintreten, ein besonderes Aussehen.",
        "Sie entbehren der Schärfe, haben weniger Eigen­schaften als sonst, werden unbestimmt.",
        "Die Randzone führt ein Nebendasein.",
        "Doch gibt es zwei Wege, auf denen sie zu"
      ],
      [
        "* Man verzeihe mir hier ein aus der Mathematik entlehntes Gleichnis für die Dessoirsche «Kritik».",
        "Angenommen: Jemand sage innerhalb der Logarithmenlehre: zwei Zahlen werden multipliziert, wenn man deren Lo­garithmen addiert und zur Summe dieser die Grundzahl, als das Produkt, sucht.",
        "Wenn nun jemand käme und sagte: Nein - jedermann weiß doch, wie Zahlen multipliziert werden und da spricht einer vom Addieren !",
        "In dieser Art aber ist Max Dessoirs Kritik mit Bezug auf den oben berührten Punkt."
      ],
      [
        "selbständigerer Wirksamkeit gelangt.",
        "Der erste dieser Wege kommt für das hier Anzuführende nicht in Betracht.",
        "Über den zweiten äußert sich Dessoir in der folgenden Art: «Der andere Weg der Verselbständigung verläuft so, daß die Randzone zwar als Mitbewußtsein neben dem Hauptbewußtsein bestehen bleibt, sich aber zu einer größeren Bestimmtheit und Verknüpfung ihrer Inhalte erhebt und dadurch in ein ganz neues Verhältnis zur gleichzeitigen vollbewußten See­lentätigkeit tritt."
      ],
      [
        "Um wiederum ein leicht verständliches Bild zu gebrauchen: aus dem Mittelpunkt des Kreises glei­tet ein Komplex an die Peripherie, versinkt dort aber nicht ins Nebelhafte, sondern bewahrt teilweise seine Bestimmt­heit und seinen Zusammenhang.»* Im Anschluß an diese Ausführung sagt dann Dessoir: «Ein Beispiel: Beim Vor­tragen sehr geläufiger Gedankengänge geraten mir gele­gentlich Begriffe und Worte in jene Region, und die Auf­merksamkeit beschäftigt sich mit anderen Dingen.",
        "Trotz­dem spreche ich weiter, gewissermaßen ohne Anteil des Be­wußtseins."
      ],
      [
        "Dabei ist es vorgekommen, daß ich von einer plötzlich eingetretenen Stille im Saal überrascht wurde und mir erst klar gemacht werden mußte, daß sie die Folge mei­nes eigenen Verstummens war !",
        "Gewohnte Vorstellungs­verknüpfungen und Urteile können also auch vollzogen werden, zumal solche, die sich im Unan­schaulichen bewegen; die mit ihnen verbundenen Sprachbewegungen laufen gleichfalls ohne Schwierigkeit in den eingeübten Bahnen.» Allerdings, wenn ich diese Stelle in ihrer vollen Tragweite nehme, möchte ich doch lieber nicht annehmen, daß sie auf eine Eigenerfahrung Dessoirs ver­weist, sondern daß er von etwas spricht, was er an andern"
      ],
      [
        "* Vergleiche Seite 32 ff. des Dessoirschen Buches."
      ],
      [
        "verträumten Rednern bemerkt hat, und daß er «mir» und «ich» nur gebraucht in dem Sinne, wie man es tut, wenn man sich stilistisch so ausdrückt, als ob man sich an die Stelle des Andern versetze.",
        "Der Zusammenhang, in dem die Sätze stehen, macht diese Erklärung allerdings schwierig, und nur möglich, wenn man annimmt, Dessoir sei stilistisch da­bei etwas unterlaufen, was in unserer hastenden Zeit vielen Schriftstellern geschieht. - Doch, wie dem auch sei, wesent­lich liegt die Sache so, daß eine Seelenverfassung, in welcher das «Unterbewußte» eine solche Rolle spielt, wie in dem von Dessoir für einen Redner gekennzeichneten Fall, zu dem allerersten gehört, was seelisch überwunden werden muß, wenn man in das Verständnis der anthroposophischen Erkenntnis eindringen will.",
        "Das völlige Gegenteil: die rest­lose Durchdringung der Begriffe mit Bewußtheit, ist not­wendig, wenn diese Begriffe ein Verhältnis haben sollen zur wirklichen geistigen Welt.",
        "Auf dem Gebiete der Anthropo­sophie ist ein Redner unmöglich, der weiterredet, wenn «die Aufmerksamkeit» sich « mit anderen Dingen» beschäftigt.",
        "Denn wer Anthroposophie erfassen will, muß sich daran ge­wöhnt haben, die Richtung seiner Aufmerksamkeit nicht zu trennen von der Richtung eines durch ihn hervorgerufe­nen Vorstellungsverlaufes.",
        "Er wird nicht weiter sprechen von Dingen, von denen sich seine Aufmerksamkeit abwen­det, weil er nicht weiter über solche Dinge denken wird."
      ],
      [
        "Sehe ich mir nun an, wie Max Dessoir über meine kleine Schrift «Blut ist ein ganz besonderer Saft» seinen Lesern berichtet, so drängt sich mir allerdings der Gedanke auf, daß er nicht nur weiter redet, wenn seine Aufmerksamkeit sich «anderen Dingen» zuwendet, sondern daß er in einem solchen Falle sogar weiter schreibt.",
        "In diesem Bericht findet"
      ],
      [
        "man das Folgende.",
        "Es wird mein Satz angeführt: «Das Blut nimmt die durch das Gehirn verinnerlichten Bilder der Au­ßenwelt auf»,* und dazu macht Dessoir die Bemerkung: «Eine solche ungeheuerliche Mißachtung aller Tatsachen verbindet sich mit der ebenso unbeweisbaren wie unver­ständlichen Behauptung, der vorgeschichtliche Mensch habe in den , auch die Erleb­nisse seiner Vorfahren erinnert. »** Man lese doch diese Sät­ze, die Dessoir anführt, einmal in dem Zusammenhange nach, in dem sie in meiner Schrift stehen, und man nehme dazu meine Bemerkung auf Seite 24 derselben Schrift: «Ich muß im Gleichnisse sprechen, wenn ich die hier in Betracht kommenden komplizierten Vorgänge darstellen will», so wird man vielleicht doch einsehen, was es bedeutet, wenn jemand in der Dessoirschen Art berichtet. - Man stelle sich doch nur vor, was es hieße, wenn ich über Max Dessoirs «Jenseits der Seele» schriebe und meinen Lesern erzählte: da kommt jemand, der behauptet, das Blut, das «in unseren Adern» rinnt, ist «das Blut vieler Jahrtausende » ."
      ],
      [
        "Und es sei dies eine ebenso unbeweisbare wie unverständliche Behaup­tung, die sich als gleichwertig zu der andern verhält: «Doch unterliegt es keinem Zweifel, daß es hinter der Oberfläche des Bewußtseins einen dunklen, reich gefüllten Raum gibt, durch dessen Veränderungen auch die Krümmung der Oberfläche verändert wird.» Die beiden Sätze finden sich in dem Dessoirschen Buche, der letzte Seite 1, der erste, von dem «Blute der Jahrtausende» auf Seite 12.",
        "Beide Sätze sind natürlich voll berechtigt, weil sich Max Dessoir «im Gleich­nisse» ausspricht."
      ],
      [
        "Wo ich dasselbe tun muß, und dies ausdrücklich"
      ],
      [
        "* Vergleiche meine Schrift «Blut ist ein ganz besonderer Saft», Seite 24."
      ],
      [
        "** Vergleiche Seite 261 des Dessoirschen Buches."
      ],
      [
        "bemerke, schmiedet Dessoir sich zur Widerlegung eine kritische Waffe aus hölzernem Eisen. - Dessoir spricht davon, daß mein Hinweis auf geistig Wesenhaftes sich «im ganzen kennzeichnet als materialistische Vergrö­berung seelischer Vorgänge und personifizierende Verfla­chung der geistigen Werte ».* Diese Behauptung ist gegen­über den Ausführungen meiner Schriften ebenso sinnvoll, wie wenn ich das Folgende sagte: Ein Denker, der imstande ist, zu sagen: «Man darf- in einer freilich sehr unvollkom­menen Vergleichung - den Bewußtseinsaugenblick einen Kreis nennen, dessen Peripherie schwarz, dessen Mittel­punkt weiß und dessen dazwischen liegende Teile abge­stuftes Grau sind», dessen Ansicht kennzeichne sich «im ganzen . . . als materialistische Vergröberung seelischer Vor­gänge».",
        "Und dieser Denker, der solch Groteskes macht, den Bewußtseinsaugenblick mit einem Kreise vergleicht, von weiß, grau, schwarz spricht, ist Max Dessoir.** ES kann mir natürlich nicht beifallen, dergleichen so hinzureden, denn ich weiß, Max Dessoir vergröbert in diesem Falle nicht in materialistischer Art seelische Vorgänge.",
        "Was er aber mir gegenüber vollbringt, ist von der eben gekennzeichneten Art."
      ],
      [
        "Man wird es begreiflich finden, daß es völlig unmöglich ist, mit einer Kritik, die auf Voraussetzungen ruht wie die Dessoirsche, sich auseinanderzusetzen über den Sinn des Schicksalsgesetzes vom anthroposophischen Gesichts­punkte aus; ich müßte ganze Kapitel meiner Schriften hier abschreiben, wenn ich zeigen wollte, wie haarsträubend ver­schoben wird, was ich an Vorstellungen über das menschli­che Schicksal vertrete durch die Dessoirsche Behauptung:"
      ],
      [
        "* Vergleiche Seite 260 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche Seite 32 des Dessoirschen Buches."
      ],
      [
        "«Hiermit wird angeblich ein Zusammenhang von Ursache und Wirkung in der geistigen Welt enthüllt (die Kausalität gilt demnach nicht nur in der verstandesmäßig aufgefaßten Erfahrungswelt).",
        "Der Mensch, der sich durch eine Reihe von Lebensläufen hindurch vervollkommnet, untersteht dem Karma-Gesetz, wonach jede Tat ihre Folgen unaus­bleiblich nach sich zieht, also zum Beispiel die gegenwärtige Not von der Präexistenz her selbstverschuldet ist. »* Ich habe 1887 in meiner Einführung zum zweiten Bande von Goethes Naturwissenschaftlichen Schriften die Sätze nieder­geschrieben: «Das Erklären eines Vorganges in der Natur ist ein Zurückgehen auf die Bedingungen desselben: ein Aufsuchen des Produzenten zu dem gegebenen Produkte."
      ],
      [
        "Wenn ich eine Wirkung wahrnehme und dazu die Ursache suche, so genügen diese zwei Wahrnehmungen keineswegs meinem Erklärungsbedürfnisse.",
        "Ich muß zu den Gesetzen zurückgehen, nach denen diese Ursache diese Wirkung her­vorbringt."
      ],
      [
        "Beim menschlichen Handeln ist das nun anders.",
        "Da tritt die eine Erscheinung bedingende Gesetzlichkeit selbst in Aktion; was ein Produkt konstituiert, tritt selbst auf den Schauplatz des Wirkens.",
        "Wir haben es mit einem er­scheinenden Dasein zu tun, bei dem wir stehen bleiben kön­nen, bei dem wir nicht nach den tiefer liegenden Bedingun­gen zu fragen brauchen.»** Es ist wohl klar, was ich meine: das Fragen nach Bedingungen einer menschlichen Handlung kann nicht in derselben Weise erfolgen wie einem Vorgange der Natur gegenüber."
      ],
      [
        "Es muß also anders sein.",
        "Meine Anschauungen über den Schicksalszusammenhang, die eng"
      ],
      [
        "* Vergleiche Seite 265 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche meine Einleitungen zu Goethes Naturwissenschaftlichen Schriften, Dornach 1926, Seite 149, Freiburg i.",
        "Br. 1949, Seite 183 f."
      ],
      [
        "verwandt sind mit denen nach den Willens quellen des Men­schen, können also nicht auf dasjenige Verhältnis von Ur­sache und Wirkung weisen, von dem man in der Naturwis­senschaft spricht.",
        "Ich gab mir deshalb in meinem Buche «Theosophie» alle Mühe, verständlich zu machen, daß ich weit davon entfernt bin, das Übergreifen der Erlebnisse des einen Menschenlebens in die folgenden im Sinne des natür­lichen Kausalzusammenhanges zu denken."
      ],
      [
        "Max Dessoir entstellt meine Schicksalsvorstellung in gröbster Weise, in­dem er in deren Mitteilung den Satz verflicht: «Die Kausa­lität gilt demnach nicht nur in der verstandesmäßig aufge­faßten Erfahrungswelt.» - Eine Möglichkeit, diese Bemer­kung anzubringen, schafft er sich nur dadurch, daß er aus meiner kleinen Schrift «Reinkarnation und Karma» einen Satz heraushebt, der in dieser Schrift eine längere Ausfüh­rung zusammenfaßt.",
        "Durch diese Ausführung wird dem Satze aber erst die rechte Bedeutung gegeben."
      ],
      [
        "So wie ihn Dessoir (isoliert) hinstellt, kann man in einer recht wohlfeilen Art seine Kritik daran üben.",
        "Der Satz heißt: «Alles, was ich in meinem gegenwärtigen Leben kann und tue, steht nicht abgesondert für sich allein da als Wunder, sondern hängt als Wirkung mit den früheren Daseinsformen meiner Seele zusammen, und als Ursache mit den späteren.»* Wer sich darauf einläßt, den Satz im Zusammenhang mit den Ausführungen zu lesen, die er zusammenfaßt, der wird fin­den, ich verstehe das Hinübergreifen von einer Lebensform in die andere so, daß auf dasselbe die im bloßen Naturbe­trachten übliche Kategorie der Kausalität nicht anwendbar ist."
      ],
      [
        "Man kann nur in abgekürzter Redewendung von Kau­salität"
      ],
      [
        "* Vergleiche meine Schrift «Reinkarnation und Karma» und Seite 261 f. von Dessoirs Buch."
      ],
      [
        "sprechen, wenn man eben die genauere Bestimmung mitgibt oder beim Leser als bekannt voraussetzen darf.",
        "In meinem zusammenfassenden Satz läßt aber das Vorange­hende gar nicht zu, daß man ihn anders als in der folgenden Art auffaßt: Alles, was ich in meinem gegenwärtigen Leben kann und tue, hängt als Wirkung mit den früheren Daseinsformen meiner Seele insofern zusammen, als die im gegenwär­tigen Leben liegenden Ursachen meines Könnens und Han­delns mit anderen Lebensformen in einer Beziehung stehen, welche nicht eine solche der gewöhnlichen Kausalität ist; und alles, was ich kann und tue hängt mit späteren Daseinsformen meiner Seele insofern zusammen, als dieses Ge­konnte und Getane Ursache von Wirkungen im gegenwär­tigen Leben ist, die nun ihrerseits mit dem Inhalt späterer Lebensformen in einer Beziehung stehen, welche wieder nicht eine solche der gewöhnlichen Kausalität ist. - Wer meine Schriften verfolgt, wird ersehen, daß ich nie einen Karma-Begriff vertreten habe, der mit der Vorstellung des freien Menschenwesens unvereinbar ist."
      ],
      [
        "Dessoir hätte das bemerken können, wenn er auch nichts anderes von mir Ge­schriebene «benutzt» hätte, als was in meiner «Geheimwissenschaft» steht: «Wer da meint, daß die menschliche Freiheit mit dem ...",
        "Vorausbestimmtsein der zukünftigen Gestaltung der Dinge nicht vereinbar sei, der sollte beden­ken, daß des Menschen freies Handeln in der Zukunft eben­sowenig davon abhängt, wie die vorausbestimmten Dinge sein werden, wie diese Freiheit davon abhängt, daß er sich vornimmt, nach einem Jahre in einem Hause zu wohnen, dessen Plan er gegenwärtig feststellt. »* Denn wenn auch"
      ],
      [
        "* Vergleiche meine «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 413 f."
      ],
      [
        "diese Sätze sich nicht unmittelbar auf die Zusammenhänge der menschlichen Erdenleben beziehen, so könnte sie doch nicht jemand schreiben, welcher der Meinung ist, die Schicksale dieser Erdenleben hängen so zusammen, wie es dem Gesetze der naturwissenschaftlichen Kausalität ent­spricht."
      ],
      [
        "Dessoir läßt nirgends merken, daß er sich die Mühe ge­nommen habe, zu prüfen, in welcher Art ich erkenntnistheoretisch und allgemein-philosophisch, sowie in Gemäß­heit naturwissenschaftlicher Vorstellungen die von mir ver­tretene Anthroposophie begründe.",
        "Dafür stellt er Behaup­tungen auf, für die sich auch nicht einmal ein entfernter An­haltspunkt in meinen Schriften vorfindet.",
        "So Seite 296 f. sei­nes Buches: «Erfahren wir, daß die noch ganz in diesem Bann stehende Medizin des Mittelalters den Menschen nach dem Tierkreis einteilte und in der Hand mit ihren Fingern Unterabteilungen der Himmelsmaße sah, oder lesen wir bei Rudolf Steiner, daß vor der Befruchtung die Pflanze in einer solchen Lage ist wie die ganze Erde vor der Sonnentren­nung war, so haben wir Beispiele für den Grundsatz, im kleinen das Abbild großer Weltvorgänge zu sehen.»* Wäre, was Max Dessoir mit diesem Satze meint, ebenso richtig wie es unrichtig ist, so genügte es, meinen anthroposophischen Gesichtspunkt zusammenzuwerfen mit allem möglichen dilettantischen"
      ],
      [
        "* Max Dessoir schreibt dieses mit Bezug auf die Ausführungen meiner «Geheimwissenschaft im Umriß», 26.",
        "Auflage, Seite 335 ff.",
        "Er ist einem Verständnis des von mir Gesagten nicht einmal nahe gekommen, sonst hätte er auf den Gedanken gar nicht verfallen können, daß diese Sache ir­gend etwas mit der von ihm angeführten dilettantischen Methode zu tun haben kann, «Entsprechungen» aufzusuchen zwischen weit voneinander entfernten Tatsachen.",
        "Ein Unbefangener muß sehen, daß, was ich über Erde und Sonnentrennung einerseits und über die Befruchtung der Pflanze andrerseits sage, in ganz selbständiger Weise gefunden wird, ohne von der ­Absicht auszugehen, eine «Entsprechung» aufzufinden.",
        "Mit demselben Rechte könnte man sagen, der Physiker suche nach «Entsprechungen», wenn er die polarisch zu einander stehenden Tatsachen, die an der Anode und der Kathode zutage treten, in die Untersuchung zieht.",
        "Aber Dessoir ist eher weit entfernt davon, zu verstehen , daß die von mir angewandte Methode nichts zu tun hat mit dem, was er treffen will, sondern daß sie völlig die ins Geistgebiet gewendete naturwissenschaftliche Denkweise ist."
      ],
      [
        "Treiben, das sich gegenwärtig als Mystik, Theosophie und dergleichen geltend macht.",
        "In Wirklich­keit ist diese Behauptung Dessoirs nur - schon allein für sich - ein voller Beweis dafür, daß dieser Kritiker meiner Anthroposophie ohne jedes Verständnis gegenübersteht, sowohl, was deren philosophische Grundlage wie deren Methode, ja auch sogar was die Ausdrucksform für ihre Er­gebnisse betrifft.",
        "Im Grunde ist Dessoirs Kritik nichts ande­res als viele «Entgegnungen», denen die von mir vertretene Anthroposophie ausgesetzt ist.",
        "Mit ihnen sind Auseinan­dersetzungen unfruchtbar, weil sie nicht dasjenige kritisie­ren, was sie zu beurteilen vorgeben, sondern ein von ihnen willkürlich geformtes Zerrbild, gegenüber dem dann ihnen die Kritik recht leicht wird.",
        "Mir erscheint es ganz unmög­lich, daß jemand, der einsieht, worauf es mir bei dem an­kommt, was mir Anthroposophie ist, dieses zusammenstellt - wie es Dessoir tut - mit einer literarischen unwillkürlichen Burleske wie den Faustbüchern von J.A.",
        "Louvier, mit der absonderlichen Rassenmystik Guido Lists, mit der Chri­stian Science - ja selbst mit alledem, was Dessoir als «Neu-­Buddhismus» bezeichnet. - Ob es berechtigt ist, daß Max Dessoir von meinen Ausführungen sagt: «Es verrät eine Anspruchslosigkeit des Denkens, wenn bloß verlangt wird, das Vorgebrachte als nicht widersinnig anzuerkennen (denn im weiteren Sinn möglich ist gar vieles, was unwahrscheinlich"
      ],
      [
        "und fruchtlos bleibt); wenn nirgends untersucht und gefragt, gezweifelt und abgewogen, sondern von oben her bestimmt wird: .»* - dies zu beurteilen überlasse ich denjenigen, die meine Schriften wirklich kennen lernen mögen.",
        "Gar ein Satz wie dieser: «Harmlose Leser lassen sich vielleicht durch die eingestreuten Beispiele und die angebliche Aufklärung gewisser Erfahrungen bestechen . . . »* kann mich höch­stens dazu veranlassen, zu denken, wie «harmlose Leser» des Dessoirschen Buches sich vielleicht durch die einge­streuten, aber sinnlos interpretierten Zitate aus meinen Schriften und die gefällige Umsetzung meiner Gedanken ins Triviale bestechen lassen. - Wenn ich trotz der Unfrucht­barkeit, zu der eine Auseinandersetzung mit diesem Kriti­ker von vorneherein verurteilt ist, diese doch hier vorbringe, so geschieht es, weil ich wieder einmal an einem Beispiele zei­gen mußte, welcher Art von Beurteilung das, was ich An­throposophie nenne, begegnet; und weil es gar zu viele «harmlose Leser» gibt, die sich ihr Urteil über eine solche geistige Bestrebung nach Büchern wie das Dessoirsche bil­den, ohne Kenntnis zu nehmen von dem, was beurteilt wird, und ohne auch nur zu ahnen, wie das in Wirklichkeit aussieht, von dem ihnen ein Zerrbild vor Augen gestellt wird."
      ],
      [
        "Ob es eine Bedeutung hat, wenn jemand, der so ferne ist vom Verständnisse dessen, was ich anstrebe, der so von ihm beurteilte Schriften liest, wie Max Dessoir, - «von oben her» behauptet, ich lasse mir «gewisse Beziehungen zur Wissenschaft angelegen sein», besitze aber «kein inneres Verhältnis zum Geist der Wissenschaft»**, darüber urteile"
      ],
      [
        "* Vergleiche Seite 263 des Dessoirschen Buches."
      ],
      [
        "** Vergleiche Seite 254 des Dessoirschen Buches."
      ],
      [
        "ich auch nicht selbst, sondern überlasse dieses den Lesern meiner Bücher. - Fast ein Wunder wäre es, wenn die ganze Geistesart Max Dessoirs zu allem übrigen nicht auch noch den Satz fügte: «Gar nun die Masse seiner Anhänger ver­zichtet völlig auf eigene Denkarbeit.»* Wie oft müssen sich dieses diejenigen sagen lassen, die man als meine «Anhän­ger» zu bezeichnen beliebt !",
        "Gewiß, «Anhänger» von zwei­felhaften Eigenschaften gibt es bei jeder geistigen Bestre­bung.",
        "Es kommt aber darauf an, ob diese und nicht vielleicht andere für die Bestrebung die Charakteristischen sind.",
        "Was weiß Max Dessoir von meinen «Anhängern»?",
        "Was weiß er darüber, wie viele es unter ihnen gibt, die nicht nur weit ent­fernt davon sind, auf eigene Denkarbeit zu verzichten, son­dern die, nachdem sie durch ihre Denkarbeit das wissen­schaftlich Ungenügende der Weltanschauungen vom Schla­ge der Dessoirschen durchschaut haben, es nicht verschmä­hen, sich Anregungen zu holen bei den Bestrebungen, durch welche ich, so gut ich es vermag, einen methodischen Weg suche, um ein kleines Stück in die geistige Welt einzudrin­gen.",
        "Vielleicht kommt doch die Zeit auch einmal heran, in der man gerechter urteilen wird über solche Menschen in der Gegenwart, die genug Denkarbeit zu verrichten imstande sind, um nicht zu den «harmlosen Lesern» Max Dessoirs zu gehören.**"
      ],
      [
        "* Vergleiche Seite 254 des Dessoirschen Buches."
      ],
      [
        "** Nur die Tatsache, daß Dessoir nicht in der Lage ist, sich wirklich ent­sprechende Vorstellungen über die anthroposophischen Versuche zu ma­chen, läßt es erklärlich erscheinen, daß er nicht einmal da mit irgendeinem Verständnisse dieser Versuche einsetzt, wo sein eigener Gedankengang ihm dies so nahe wie möglich legt.",
        "Solch ein Fall liegt in dem vor, worauf er mit zwei Sätzen auf Seite 322 f. seines Buches weist: «Es gibt kein Jenseits der Seele im Sinne einer unsichtbaren Wirklichkeit, weil geistige Sachverhalte des dinghaften wie des personenhaften Daseins überhoben sind."
      ],
      [
        "Das objektive Seelenjenseits darf als ein Überbewußtsein, niemals aber als ein räumlich außerhalb der Seele Existierendes betrachtet werden.» Dessoir sieht nicht, daß er mit einem solchen Satze nicht eine Widerlegung, sondern gerade den Beweis für die Notwendigkeit der Anthroposophie liefert.",
        "Er sieht nicht, daß in meinen Schriften überall der Versuch unternommen wird, die in Be­tracht kommenden Fragen als Bewußtseinsfragen zu behandeln."
      ],
      [
        "Man wolle nur bemerken, wie dieser Versuch zum Beispiel gerade in meiner «Geheim­wissenschaft im Umriß» durchgeführt ist.",
        "Nur kann eben Dessoir nicht sehen, daß dadurch der ganze Erkenntnisvorgang gegenüber der geistigen Welt zu einer inneren Verrichtung des Bewußtseins gemacht wird, daß innerhalb des Bewußtseins selbst andere Bewußtseinsformen erlebend auf­gesucht werden müssen, die es dann allerdings nicht mit einem «räumlich außerhalb der Seele Existierenden» zu tun haben, sondern mit einem Inne­sein der Seele in einem solchen Existierenden, das in ebendemselben Sinne unräumlich ist wie die Erlebnisse des gewöhnlichen Bewußtseins es selbst schon sind."
      ],
      [
        "Allerdings müßte derjenige, der dieses einsehen will, im anthro­posophischen Sinne zurecht gekommen sein mit einem solchen Satz wie derjenige ist, den Friedrich Theodor Vischer im 1.",
        "Teil seines «Altes und Neues», Seite 194, niedergeschrieben hat: «Die Seele, als oberste Einheit aller Vorgänge, kann allerdings nicht im Leibe lokalisiert sein, obwohl sie anderswo als im Leibe nicht ist ...» Dieser Satz gehört zu denjenigen, die an die Grenzorte des gewöhnlichen Erkennens führen im Sinne des I."
      ],
      [
        "Abschnit­tes dieser Schrift und im Sinne des I.",
        "Kapitels der am Ende derselben ste­henden «Skizzenhaften Erweiterungen des Inhaltes dieser Schrift»."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "III FRANZ BRENTANO",
    "paragraphs": [
      "III FRANZ BRENTANO",
      "Ein Nachruf",
      "Über das Verhältnis von Anthropologie und Anthroposophie in genügender Form zu sprechen ist aus den im vorigen Abschnitt dieser Schrift angeführten Gründen in Anknüp­fung an Max Dessoirs Buch «Vom Jenseits der Seele» nicht möglich. Ich glaube nun aber, daß dieses Verhältnis an­schaulich werden kann, wenn ich an diese Stelle die Ausfüh­rungen setze, die ich in andrer Absicht niedergeschrieben habe, nämlich als Nachruf für den im März 1917 in Zürich verstorbenen Philosophen Franz Brentano. Der Hingang des von mir aufs höchste verehrten Mannes hat bei mir be­wirkt, daß dessen bedeutungsvolles Lebenswerk erneut mir vor die Seele getreten ist; er hat mich bestimmt, das Fol­gende auszusprechen.",
      "Es scheint mir, daß ich den Versuch machen darf, vom an­throposophischen Gesichtspunkte aus zu einer Ansicht über Franz Brentanos philosophisches Lebenswerk zu gelangen in diesem Augenblick, da der Tod der verehrten Persönlich­keit die Fortsetzung dieses Werkes unterbrochen hat. Ich glaube, daß der anthroposophische Gesichtspunkt mich nicht in eine einseitige Schätzung der Brentanoschen Weltanschauung verfallen lassen kann. Dies nehme ich aus zwei",
      "Gründen an. Erstens kann die Vorstellungsart Brentanos von niemand beschuldigt werden, daß sie selbst auch nur die geringste Hinneigung zu einer anthroposophischen Richtung habe. Ihr Träger hätte diese, wenn er selbst zu einem Urteile über sie Veranlassung gehabt hätte, wohl mit aller Entschiedenheit abgelehnt. Zweitens bin ich, von mei­nem anthroposophischen Gesichtspunkte aus, in der Lage, der Philosophie Franz Brentanos rückhaltlose Verehrung entgegenzubringen.",
      "Was das erste betrifft, so glaube ich nicht zu irren, wenn ich sage, Brentano hätte, wenn er über die von mir gemeinte Anthroposophie zu einem Urteil gekommen wäre, dies so gestaltet, wie dasjenige, das er sich über Plotins Philosophie gebildet hat. Wie dieser gegenüber würde er wohl auch von der Anthroposophie gesagt haben: «Mystisches Dunkel und ein freies Schweifen der Phantasie in unbekannten Re­gionen.»* Wie dem Neuplatonismus würde er auch gegen­über der Anthroposophie zur Vorsicht gemahnt haben, «damit man nicht, von eitlem Scheine verlockt, in den laby­rinthischen Gängen einer Pseudophilosophie sich verlie­re».** Ja, er hätte vielleicht die Denkweise der Anthropo­sophie für zu dilettantisch befunden, um sie auch nur für würdig zu halten, sie den Philosophien beizuzählen, über die er so urteilte wie über die Fichte-Schelling-Hegelsche. In seiner Wiener Antrittsrede sagt er über diese : «Vielleicht ist auch die jüngstvergangene Zeit eine... Epoche des Verfalles gewesen, in der alle Begriffe trüb ineinander schwammen, und von sachentsprechender Methode nicht eine Spur mehr",
      "*    Vergleiche Brentanos Schrift: «Was für ein Philosoph manchrnal Epoche macht» (Wien, Pest, Leipzig, Hartlebens Verlag, 1876), Seite 14.",
      "**    Vergleiche Seite 23 der ehen angeführten Schrift Brentanos.",
      "zu finden war.»* Ich glaube, daß Brentano so geurteilt hätte, wenn ich auch selbstverständlich nicht nur dieses Ur­teil für völlig grundlos, sondern auch jede Zusammenstel­lung der Anthroposophie mit den Philosophien, mit denen sie dieser Philosoph wahrscheinlich zusammengestellt hätte, für unberechtigt halte.",
      "Was nun den zweiten der oben angegebenen Gründe, mich mit der Brentanoschen Philosophie auseinanderzu­setzen, betrifft, so darf ich bekennen, daß sie für mich zu den anziehendsten Leistungen der Seelenforschung in der Gegenwart gehört. Ich konnte zwar nur wenige der Wie­ner Vorlesungen Brentanos vor etwa sechsunddreißig Jah­ren hören; aber von diesem Zeitraum an habe ich seine schriftstellerische Tätigkeit mit wärmstem Anteile ver­folgt. Leider erschienen seine Veröffentlichungen, gemes­sen an meinem Wunsche, von ihm zu vernehmen, in viel zu großen Zeitabständen. Und sie sind zumeist so gehal­ten, daß man durch sie nur wie durch kleine Öffnungen in einen Raum mit einer Fülle von Schätzen, so durch gelegentliche Veröffentlichungen auf ein weites Reich un­veröffentlichter Gedanken blickte, das der hervorragende Mann in sich trug. So in sich trug, daß es in fortwäh­render Ausgestaltung hohen Erkenntniszielen zustrebte. Als nach langer Pause 1911 Brentanos Buch über «Aristo­teles», seine glänzende Schrift «Aristoteles' Lehre vom Ursprung des menschlichen Geistes» und sein Wiederab­druck des wichtigsten Teiles seiner Psychologie mit den so scharfsinnigen «Nachträgen» erschienen waren, da war",
      "* Vergleiche den Abdruck der 1874 heim Antritt seiner Wiener Profes­sur gehaltenen Antrittsrede : «Über die Gründe der Entmutigung auf philosophischem Gebiete» (Wien 1874), Seite 18.",
      "das Lesen dieser Schriften für mich eine Reihe von Festes­freuden.*",
      "Ich fühle mich Franz Brentano gegenüber von einer sol­chen Gesinnung durchdrungen, von der ich glaube sagen zu dürfen, daß man sie erwirbt, wenn die vom anthroposo­phischen Gesichtspunkte aus gewonnene wissenschaftliche Überzeugung - eben die Gesinnung ergreift. Ich bestrebe mich, seine Anschauungen in ihrem Werte zu durch­schauen, wenn ich mich auch keiner Täuschung darüber hingebe, daß er in dem oben angedeuteten Sinne über Anthroposophie hätte denken können, ja wohl, müssen. Dies bringe ich hier wahrlich nicht vor, um in alberner Art über meine Gesinnung gegenüber gegnerischen oder abwei­chenden Anschauungen in eine eitle Selbstkritik zu ver­fallen, sondern weil ich weiß, wie viel Mißverständnisse meiner Urteile über andere Geistesrichtungen es mir ge­bracht hat, daß ich mich in meinen Veröffentlichungen oft so ausgesprochen habe, wie es eine Folge dieser Ge­sinnung ist.",
      "Die ganze Brentanosche Seelenforschung methodisch durchdringend erscheinen mir die Grundgedanken, welche ihn 1868 zur Aufstellung seines Leitsatzes führten. Als er damals in Würzburg seine philosophische Professur antrat, rückte er seine Vorstellungsart in das Licht der These : es könne die wahre philosophische Forschungsart keine an­dere sein als die in dem naturwissenschaftlichen Erkennen berechtigte. «Vera philosophiae methodus nulla alia nisi",
      "* Vergleiche Brentano : «Aristoteles und seine Weltanschauung » (1911, Verlag von Quelle und Meyer in Leipzig); Brentano : «Aristoteles' Lehre vom Ursprung des menschlichen Geistes» (Leipzig, Verlag von Veit und Comp., 1911); Brentano: «Von der Klassifiltation der psychischen Phäno­mene» (Leipzig, Verlag von Duneker und Humblot, 1911).",
      "scientiae naturalis est.»* Als er dann den ersten Band seiner « Psychologie vom empirischen Standpunkte » 1874 erschei­nen ließ - in der Zeit, als er seine Wiener Professur antrat -, suchte er die Seelenerscheinungen in Gemäßheit des ange­führten Leitsatzes wissenschaftlich darzulegen.** Für mich bildet, was Brentano mit diesem Buche gewollt hat, und was von diesem Wollen während seiner Lebenszeit durch seine Veröffentlichungen zutage getreten ist, ein bedeutsames wissenschaftliches Problem. Brentano hatte - das geht aus seinem Buche hervor- seine Psychologie auf eine Reihe von Büchern berechnet. Das zweite hatte er versprochen, kurze Zeit nach dem ersten erscheinen zu lassen. Es ist keine Fort­setzung des nur die Anfangsvorstellungen seiner Psycholo­gie enthaltenden ersten Teiles erschienen. Als er 1889 seinen in der Wiener Juristischen Gesellschaft gehaltenen Vortrag «Vom Ursprung sittlicher Erkenntnis» abdrucken ließ, schrieb er in der Vorrede : «Man würde irren, wenn man um des zufälligen Anstoßes willen den Vortrag für ein flüchti­ges Werk der Gelegenheit hielte. Er bietet Früchte von jah­relangem Nachdenken. Unter allem, was ich bisher veröf­fentlicht, sind seine Erörterungen wohl das gereifteste Er­zeugnis. - Sie gehören zum Gedankenkreise einer , den ich, wie ich nunmehr zu hoffen wage, in nicht ferner Zeit seinem ganzen Umfange nach der Öffentlichkeit erschließen kann. Man wird dann an weiten",
      "*    Später sprach er sich über die Aufstellung dieser These aus in dem Vortrage, den er 1892 in der Wiener Philosophischen Gesellschaft gehalten hat und der abgedruckt ist als Schrift : «Über die Zukunft der Philosophie» (Wien, Alfred Hölder, 1893). Da findet man Seite 3 den hier gemeinten spä­teren Hinweis Brentanos auf seine These.",
      "** Vergleiche Brentano : «Psychologie vom empirischen Standpunkte», 1. Band (Leipzig, Verlag von Duneker und Humblot, 1874)",
      "Abständen von allem Hergebrachten, und insbesondere auch an wesentlichen Fortbildungen eigener, in der  vertretener An­schauungen genugsam erkennen, daß ich in meiner langen literarischen Zurückgezogenheit nicht eben müßig gewesen bin.»* Auch diese «Deskriptive Psychologie» ist nicht er­schienen. Die Verehrer der Brentanoschen Philosophie kön­nen ermessen, welchen Gewinn sie ihnen gebracht hätte, wenn sie die ein enges Gebiet umfassenden 1907 erschiene­nen «Untersuchungen zur Sinnespsychologie» studieren.**",
      "Man muß sich die Frage stellen: was hat Brentano dazu gebracht, in der Fortsetzung seiner Veröffentlichungen im­mer wieder inne zu halten, ja, das als in kurzer Zeit fertig Geglaubte dann doch nicht zu veröffentlichen? Ich bekenne, daß ich mit innerlichster Erschütterung in dem Nachruf für Franz Brentano, den Alois Höfler im Mai 1917 hat erschei­nen lassen, die Worte las : «Wie er an seinem Hauptproblem, dem Gottesbeweis, so zuversichtlich weiterarbeitete, daß mir noch vor wenigen Jahren ein mit Brentano innig befreundeter, ausgezeichneter Wiener Arzt erzählte, Brentano habe ihm kürzlich versichert, nun habe er den Gottesbeweis binnen wenigen Wochen fertig ... »*** Ebenso empfand ich, als ich aus einem andern Nachruf (von Utitz)**** vernahm :",
      "« Das Werk, das er am heißesten geliebt, an dem er sein gan­zes Leben lang geschaffen, ist unveröffentlicht geblieben.»",
      "* Vergleiche Brentanos Schrift «Vom Ursprung sittlicher Erkenntnis» (Leipzig, Verlag Daneker und Humblot, 1889), Seite Vf.",
      "**    Brentano : «Untersuchungen zur Sinnespsychologie» (Leipzig, Ver­lag Duncker und Humblot, 1907).",
      "***    Süddeutsche Monatshefte, Mai 1917, in dem Aufsatz : «Franz Bren­tano in Wien», Seite 319 ff.",
      "****    Erschienen in der Vossischen Zeitung.",
      "Mir scheint, daß Brentanos Schicksale mit seinen geplan­ten Veröffentlichungen ein schwerwiegendes geisteswissen­schaftliches Problem darstellen. Nähern wird man sich die­sem wohl nur, wenn man dasjenige in seiner Eigenart be­trachten will, was er der Welt hat mitteilen können.",
      "Ich halte für wichtig, ins Auge zu fassen, daß Brentano in seiner psychologischen Forschung in scharfsinniger Weise eine reine Vorstellung des wirklich Seelischen zugrunde le­gen will. Er fragt sich : was ist Charakteristisches in allen Vorkommnissen, die man als seelische ansprechen muß. Und er fand, was er in den Nachträgen zur Psychologie 1911 so ausdrückte : «Das Charakteristische für jede psychische Tätigkeit besteht, wie ich gezeigt zu haben glaube, in der Beziehung zu etwas als Objekt.»* Vorstellen ist eine psychi­sche Tätigkeit. Das Charakteristische ist, daß ich nicht nur vorstelle, sondern daß ich etwas vorstelle, daß meine Vor­stellung sich auf etwas bezieht. Mit einem der mittelalterli­chen Philosophie entlehnten Ausdruck bezeichnet Brentano diese Eigenheit der seelischen Erscheinungen als «intentio­nale Beziehung». «Der gemeinsame Charakterzug» - so führt er an einem andern One aus - «alles Psychischen be­steht in dem, was man häufig mit einem leider sehr mißver­ständlichen Ausdruck Bewußtsein genannt hat, das heißt in einem subjektischen Verhalten, in einer, wie man sie bezeich­nete, intentionalen Beziehung zu etwas, was vielleicht nicht wirklich, aber doch innerlich gegenständlich gegeben ist. Kein Hören ohne Gehörtes, kein Glauben ohne Geglaub­tes, kein Hoffen ohne Gehofftes, kein Streben ohne Erstreb­tes, keine Freude ohne etwas, worüber man sich freut, und",
      "* Vergleiche Brentano : «Von der Klassifikation der psychischen Phäno­mene», Seite 122.",
      "so im übrigen.»* Dieses intentionale  Innesein ist nun in der Tat etwas, was wie ein Leitmotiv so führt, daß man alles, dem man es beilegen kann, eben dadurch in seiner seelischen Eigenart erkennt.",
      "Den psychischen Erscheinungen stellt Brentano die phy­sischen gegenüber: Farben, Schall, Raum und viele andere. Er findet, daß sich diese von jenen eben dadurch unterschei­den, daß ihnen eine intentionale Beziehung nicht eigen ist. Und er beschränkt sich darauf, diese Beziehung den psychi­schen Erscheinungen zu-, den physischen abzusprechen. Nun wird aber gerade, wenn man Brentanos Ansicht über die intentionale Beziehung kennen lernt, die Vorstellung zu der Frage hingeführt : macht ein solcher Gesichtspunkt nicht notwendig, auch das Physische von ihm aus anzuse­hen? Wer nun in diesem Sinne wie Brentano das Psychische so, das Physische auf ein Gemeinsames hin prüft, der findet, daß jede Erscheinung dieses Gebietes durch etwas anderes ist. Löst sich ein Körper in einer Flüssigkeit auf, so tritt diese Erscheinung am gelösten Körper durch die Beziehung der lösenden Flüssigkeit zu ihm auf. Wenn Phosphor seine Farbe durch die Einwirkung der Sonne ändert, so weist dies in dieselbe Richtung. Alle Eigenschaften in der physischen Welt sind durch die Verhältnisse der Dinge zu einander. Es ist für physisches Sein richtig, wenn Moleschott sagt: «Al­les Sein ist ein Sein durch Eigenschaften. Aber es gibt keine Eigenschaft, die nicht durch ein Verhältnis besteht.»** Wie",
      "*    Vergleiche Brentano : «Vom Ursprung sittlicher Erkenntnis», Seite 14. Und über den Grundrug des Intentionellen «Psychologie vom empiri­schen Standpunkte», Seite 115 ff.",
      "** Besonders prägnant hat dieses dargestellt Richard Wallascheck in einem bedeutenden Aufsatz der Wiener Wochensehrift «Die Zeit», Nr.96 und 97 des Jahrganges 1896 (vom 1. und 8. August).",
      "alles Psychische in sich etwas enthält, wodurch es auf ein außer ihm Befindliches weist, so ist umgekehrt ein Physi­sches so geartet, daß das, was es ist, es durch die Beziehung eines Äußeren auf es ist. Muß nicht jemand, der in so scharf­sinniger Weise wie Brentano die intentionale Beziehung alles Seelischen betont, die Aufmerksamkeit auch auf das Charakteristische der physischen Erscheinungen richten, das sich durch den gleichen Gedankenvorgang ergibt? Si­cher scheint zum mindesten, daß eine solche Betrachtung des Seelischen die Beziehung desselben zur physischen Welt nur finden kann, wenn sie dieses Charakteristische in Erwä­gung zieht.*",
      "Brentano findet nun drei Arten von intentionalen Bezie­hungen im seelischen Leben. Die erste ist das Vorstellen von etwas; die zweite die Anerkennung oder Verwerfung, die sich im Urteilen aussprechen; die dritte die des Liebens oder Hassens, welche im Fühlen erlebt werden. Wenn ich sage: Gott ist gerecht, so stelle ich etwas vor; aber ich anerkenne oder verwerfe das Vorgestellte noch nicht; wenn ich aber sage: es gibt einen Gott, so anerkenne ich das Vorgestellte durch ein Urteil Sage ich: die Freude ist mir lieb, so urteile ich nicht bloß, sondern ich erlebe ein Gefühl. Brentano un­terscheidet aus solchen Voraussetzungen heraus drei Grundklassen der psychischen Erlebnisse: Vorstellen, Ur­teilen, Fühlen (oder die Erscheinungen des Liebens und Hassens). Diese drei Grundklassen setzt er an die Stelle der von anderen anerkannten Teilung der psychischen Erschei­nungen",
      "* Man vergleiche damit den Schluß des 7. Kapitels der am Ende dieser Schtift gegebenen «Skizzenhaften Erweiterungen des Inhaltes...». «7. Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano.»",
      "in: Vorstellen, Fühlen und Wollen.* Während näm­lich Vorstellen und Urteilen viele in eine Klasse zusammenfassen, trennt Brentano die beiden. Er ist mit der Zusam­menfassung nicht einverstanden, weil er nicht wie andere in dem Urteil nur eine Verbindung von Vorstellungen sieht, sondern eben eineAnerkennung oder einVerwerfen des Vor-gestellten, was beim bloßen Vorstellen nicht vollzogen wird. Gefühl und Wille hinwiederum, welche andere trennen, fal­len für Brentano, ihrem seelischen Gehalte nach, in eins zu­sammen. Was seelisch erlebt wird, indem man sich zum Ver­richten einer Handlung hingezogen oder davon abgestoßen fühlt, ist dasselbe, was man erlebt, wenn man zur Freude sich hingezogen oder vom Schmerze abgestoßen fühlt.",
      "Es ist aus Brentanos Schriften ersichtlich, daß er einen großen Wert darauf legt, die von ihm vorgefundene Gliede­rung des seelischen Erlebens in Denken, Fühlen und Wol­len durch die andere ersetzt zu haben, in Vorstellen, Urtei­len und in Lieben und Hassen. Von dieser Gliederung aus sucht er sich einen Weg zu bahnen zum Verständnis dessen, was die Wahrheit auf der einen Seite, die sittliche Güte auf der anderen Seite ist. Die Wahrheit stützt sich ihm auf das richtige Urteilen; die sittliche Güte auf das richtige Lieben. Er findet: «Wir nennen etwas wahr, wenn die daraufbezüg­liche Anerkennung richtig ist. Wir nennen etwas gut, wenn die darauf bezügliche Liebe richtig ist.»**",
      "Man kann in Brentanos Ausführungen finden, daß er mit der richtigen Anerkennung im Urteile bei der Wahrheit, mit",
      "* Vergleiche Brentano : «Psychologie vom empirischen Standpunkte» Seite 233 ff., und seine Schrift : «Von der Klassifikation der psychischen Phä­nomene.»",
      "** Vergleiche Brentano: «Vom Ursprung sittlicher Erkenntnis». Seite 17.",
      "dem richtigen Erleben der Liebe bei der sittlichen Güte einen seelischen Tatbestand scharf ins Auge faßt und um­schreibt. Allein man kann innerhalb seines Vorstellungs­bereiches nichts finden, was genügen würde, um von dem seelischen Erlebnis des Vorstellens zu dem des Urteilens den Übergang zu finden. Wo man auch hinblickt in diesem Vorstellensbereich: man sucht vergebens nach der Beant­wortung der Frage: was liegt denn vor, wenn sich die Seele bewußt ist, sie stelle nicht bloß vor, sondern sie finde sich veranlaßt, den Gegenstand des Vorstellens durch ein Urteil anzuerkennen? - Ebenso wenig kann man eine Frage ver­meiden bei dem richtigen Lieben für die sittliche Güte. Innerhalb desjenigen Bereiches, welchen Brentano als « Seelisches » umschreibt, ist für das sittliche Verhalten aller­dings kein anderer Tatbestand vorhanden als das richtige Lieben. Aber ist denn einer sittlichen Handlung nicht auch eine Beziehung zu der äußeren Welt eigen? Kann dieses, was eine solche Handlung für die Welt charakterisiert, erschöpft werden dadurch, daß man sagt : sie ist eine Handlung, die richtig geliebt wird? *",
      "Man hat beim Verfolgen Brentanoscher Gedankengänge zumeist das Gefühl : sie seien immer fruchtbringend, weil sie ein Problem nach einer Richtung hin scharfsinnig und mit wissenschaftlicher Besonnenheit in Angriff nehmen; aber man empfindet auch, Brentano führt mit solchen Gedan­kengängen nicht zu dem Ziel, das seine Ausgangspunkte ver­sprechen. Solch eine Empfindung kann sich auch aufdrän­gen, wenn man seine Dreiteilung des Seelenlebens in Vorstellen,",
      "* Man vergleiche hiermit das 5. Kapitel in den am Ende dieser Schrift ge­gebenen «Skizzenhaften Erweiterungen des Inhaltes...»: «5. Über die wirk­liche Grundlage der intentionalen Beziehung.»",
      "Urteilen, Lieben und Hassen vergleicht mit der an­dern in Vorstellen, Fühlen und Wollen. Man folgt mit einer gewissen Zustimmung dem, was er für seine Meinung bei­zubringen weiß; und man kann zuletzt doch wohl kaum die Überzeugung gewinnen, daß er alle Gründe hinreichend würdigt, die für die andere sprechen.",
      "Man nehme nur als besonderes Beispiel die Folgerung, die Brentano aus seiner Gliederung für die Kennzeichnung des Wahren, Schönen und Guten zieht. Wer das Seelenleben nach erkennendem Vorstellen, Fühlen und Wollen gliedert, wird kaum anders können, als das Streben nach Wahrheit mit dem Vorstellen, das Erleben der Schönheit mit dem Fühlen, das Vollbringen des Guten mit dem Wollen in einen näheren Zusammen­hang zu bringen.",
      "Im Lichte der Brentanoschen Gedanken erscheint die Sache anders. Da haben die Vorstellungen als solche keine Beziehung zu einander, durch die sich als sol­che schon die Wahrheit offenbaren könnte. Strebt die Seele nach einem Vollkommenen in der Beziehung von Vorstel­lungen, so kann daher ihr Ideal dabei nicht die Wahrheit sein; es ist vielmehr die Schönheit.",
      "Die Wahrheit liegt nicht auf dem Wege des bloßen Vorstellens, sondern des Urtei­lens. Und das sittlich Gute findet sich nicht als ein dem Wol­len Wesentliches, sondern ist Inhalt eines Fühlens; denn richtig zu lieben, ist Gefühls-Erlebnis.* - Nun kann aber die Wahrheit für das gewöhnliche Bewußtsein doch nur im vorstellenden Erkennen gesucht werden.",
      "Denn, wenn auch das Urteil, das zur Wahrheit führt, nicht in einer bloßen",
      "* Vergleiche Brentano : «Psychologie vom empirischen Standpunkte», Seite 340 ff., und seine Schrift : «Von der Klassifikation der psychischen Phä­nomene», Seite 110 ff., sowie auch das von ihm in seiner Schrift «Vom Ur­sprung sittlicher Erkenntnis», Seite 17 ff., Gesagte.",
      "Verbindung von Vorstellungen sich erschöpft, sondern auf einer Anerkennung oder Verwerfung von Vorstellungen beruht, so kann diese Anerkennung oder Verwerfung von diesem Bewußtsein nur in Vorstellungen erlebt werden. - Und wenn auch die Vorstellungen, durch die ein Schönes dem Bewußtsein sich darstellt, in gewissen innerhalb des Vorstellungslebens gelegenen Verhältnissen sich offenba­ren: erlebt wird die Schönheit doch durch das Gefühl. - Und obgleich ein sittlich Gutes in der Seele ein richtiges Lieben hervorrufen soll : sein Wesentliches ist doch die Verwirkli­chung des richtig Geliebten durch das Wollen.",
      "Man erkennt erst, was in Brentanos Gedanken über die Dreigliederung des Seelenlebens vorliegt, wenn man durch­schaut, daß er von etwas ganz anderem spricht als diejeni­gen, welche diese Gliederung nach Vorstellen, Fühlen und Wollen vollziehen. Diese wollen einfach die Erfahrung des gewöhnlichen Bewußtseins beschreiben. Und dieses erfährt von sich selbst in den von einander unterschiedenen Ver­richtungen des Vorstellens, Fühlens und Wollens. Was wird da eigentlich erfahren? In meinem Buche «Vom Menschenrätsel» habe ich versucht, diese Frage zu beantworten. Die dort vorgebrachten Ergebnisse habe ich in der folgenden Art zusammengefaßt. «Zunächst ist das seelische Erleben des Menschen, wie es sich im Denken, Fühlen und Wollen offenbart, an die leiblichen Werkzeuge gebunden. Und es gestaltet sich so, wie es durch diese Werkzeuge bedingt ist. Wer aber meint, er sehe das wirkliche Seelenleben, wenn er die Äußerungen der Seele durch den Leib beobachtet, der ist in demselben Fehler befangen, wie einer, der glaubt, seine Gestalt werde von dem Spiegel hervorgebracht, vor dem er steht, weil der Spiegel die notwendigen Bedingungen ent­halte,",
      "durch die sein Bild erscheint. Dieses Bild ist sogar in gewissen Grenzen als Bild von der Form des Spiegels usw. abhängig: was es aber darstellt, das hat mit dem Spiegel nichts zu tun. Das menschliche Seelenleben muß, um innerhalb der Sinneswelt sein Wesen voll zu erfüllen, ein Bild seines We­sens haben. Dieses Bild muß es im Bewußtsein haben; sonst würde es zwar ein Dasein haben; aber von diesem Dasein keine Vorstellung, kein Wissen. Dieses Bild, das im ge­wöhnlichen Bewußtsein der Seele lebt, ist nun völlig be­dingt durch die leiblichen Werkzeuge. Ohne diese würde es nicht da sein, wie das Spiegelbild nicht ohne den Spiegel. Was aber durch dieses Bild erscheint, das Seelische selbst, ist sei­nem Wesen nach von den Leibeswerkzeugen nicht abhän­giger als der vor dem Spiegel stehende Beschauer von dem Spiegel. Nicht die Seele ist von den Leibeswerkzeugen abhängig, sondern allein das gewöhnliche Bewußtsein der See­le.»* - Schildert man diesen von der Leibesorganisation ab­hängigen Bewußtseinsbereich, so gliedert man richtig nach Vorstellen, Fühlen und Wollen.** Aber Brentano schildert etwas anderes. Man fasse zunächst ins Auge, daß er unter dem «Urteilen» ein Anerkennen oder Abweisen eines Vor­stellungsinhaltes versteht. Das Urteilen betätigt sich inner­halb des Vorstellungslebens; aber es nimmt die Vorstellungen,",
      "* Vergleiche hierzu mein Buch «Vom Menschenrätsel», 4. Auflage, Seite 156. Ich möchte die für viele gewiß überflüssige Bemerkung hier anfügen, daß ich - aus der Wesenheit der Sache heraus - bei meinem Verglei­che des Bewußtseins mit einem Spiegelbilde nicht im Auge habe, was man gewöhnlich tut, die Vorstellungswelt ein Spiegelbild der Außenwelt zu nennen, sondeen daß ich, was die Seele im gewöhnlichen Bewußtsein er­lebt, als ein Spiegelbild des wahrhaft Seelischen bezeichne.",
      "**    Man vergleiche damit das 6. Kapitel der am Ende dieser Schrift gege­benen «Skizzenhaften Erweiterungen des Inhaltes...» : «6. Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit.»",
      "die in der Seele auftreten, nicht einfach hin, sondern es setzt sie durch Anerkennung oder Ablehnung in Beziehung zu einer Wirklichkeit. Sieht man genauer zu, so kann diese Beziehung der Vorstellungen auf eine Wirklichkeit nur in einer Tätigkeit der Seele gefunden werden, welche in dieser selbst sich vollzieht.",
      "Dem entspricht aber niemals restlos, was die Seele bewirkt, wenn sie eine Vorstellung umteilend auf eine Sinneswahmehmung bezieht. Denn da ist es der Zwang des äußeren Eindruckes, der nicht rein innerlich er­lebt, sondern nur nacherlebt wird, und so als vorgestelltes Nach-Erlebnis zur Anerkennung oder zum Verwerfen führt.",
      "Dagegen entspricht, was Brentano beschreibt, in die­ser Beziehung vollkommen demjenigen Erkennen, das im ersten Abschnitt dieser Schrift das imaginative genannt wird. In diesem wird das Vorstellen des gewöhnlichen Be­wußtseins nicht einfach hingenommen, sondern in innerem Seelen-Erleben weiter gebildet, so daß aus ihm sich die Kraft auslöst, das seelisch Erfahrene auf eine geistige Wirk­lichkeit so zu beziehen, daß diese anerkannt oder verworfen wird.",
      "Brentanos Urteilsbegriff wird also nicht im gewöhnli­chen Bewußtsein vollkommen verwirklicht, sondern in der Seele, die in imaginativem Erkenntnis sich betätigt. - Des weiteren ist klar, daß durch Brentanos vollständige Ablö­sung des Vorstellungs- von dem Urteilsbegriff, von ihm das Vorstellen als bloßes Bild gefaßt wird. So aber lebt das ge­wöhnliche Vorstellen in der imaginativen Erkenntnis.",
      "Auch diese zweite Eigenschaft, welche die Anthroposophie dem imaginativen Erkennen beilegt, findet sich also in Brenta­nos Charakteristik der psychischen Erscheinungen. - Fer­ner: Brentano spricht die Erlebnisse des Fühlens als Erscheinungen der Liebe und des Hasses an. Wer zum imagi­nativen",
      "Erkennen aufsteigt, der muß in der Tat diejenige Art des seelischen Erlebens, die für das gewöhnliche Bewußtsein als Lieben und Hassen - im Brentanoschen Sinn -sich offenbart, für das übersinnliche Schauen so umwan­deln, daß er sich gewissen Eigenarten der geistigen Wirk­lichkeit gegenübersetzen kann, welche in meiner «Theoso­phie» zum Beispiel in der folgenden Art geschildert wer­den : «Es gehört zu dem ersten, was man sich für die Orien­tierung in der seelischen Welt aneignen muß, daß man die verschiedenen Arten ihrer Gebilde in ähnlicher Weise un­terscheidet, wie man in der physischen Welt feste, flüssige und luft- oder gasförmige Körper unterscheidet. Um dazu zu kommen, muß man die beiden Grundkräfte kennen, die hier vor allem wichtig sind. Man kann sie Sympathie und An­tipathie nennen. Wie diese Grundkräfte in einem seelischen Gebilde wirken, danach bestimmt sich dessen Art.»* Wäh­rend Lieben und Hassen für das Leben der Seele in der Sin­neswelt etwas Subjektives bleibt, erlebt das imaginative Er­kennen das objektive Verhalten in der Seelenwelt mit durch innere Erfahrungen, die dem Lieben und Hassen gleich­kommen. Brentano beschreibt auch da, indem er von Seelenerscheinungen spricht, eine Eigenheit des imaginativen Erkennens (durch die dasselbe aber schon in den Bereich einer noch höheren Erkenntnisart** hineinreicht). Und daß",
      "* Vergleiche meine «Theosophie», 28. Auflage, Seite 96.",
      "** Die erste Form des «schauenden Erkennens», die imaginative, geht uber in die zweite, die in meinen Schriften die inspirierte genannt wird. Wie eigentlich in der Brentanoschen Definition des Liebens und Hassens schon die in die Inspiration übergegangene Imagination lebt, das findet man dar­gestellt in den Schlußausfiihrungen des 6. Kapitels der am Ende dieser Schrift gegebenen «Skizzenhaften Erweiterungen des Inhaltes...» : «6. Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit.»",
      "er von der objektiven Art des Liebens und Hassens im Gegen­satz zur subjektiven Gefühlsweise des gewöhnlichen Be­wußtseins eine Vorstellung hat, das ersieht man daraus, daß er die sittliche Güte als ein richtiges Lieben darstellt. - Zu­letzt muß ganz besonders in Betracht gezogen werden, daß für Brentano das Wollen aus dem Kreise der Seelenerschei­nungen herausfällt. Nun gehört das aus dem gewöhnlichen Bewußtsein erfließende Wollen ganz der physischen Welt an. Es verwirklicht sich in der Gestalt, wie es von diesem Bewußtsein gedacht werden kann, restlos in der physischen Welt, obwohl es ein in der physischen Welt sich offenbaren des rein geistig-Wesenhaftes an sich ist. Schildert man das in der physischen Welt vorhandene gewöhnliche Bewußtsein, so kann in dieser Schilderung das Wollen nicht fehlen. Schildert man das schauende Bewußtsein, so kann in diese Schilderung nichts von den Vorstellungen über das ge­wöhnliche Wollen übergehen. Denn in der seelischen Welt, auf welche das imaginative Bewußtsein sich bezieht, erfolgt das Geschehen auf einen seelischen Impuls hin anders als durch Akte des Wollens, wie solche der physischen Welt ei­gen sind. Indem also Brentano die seelischen Erscheinun­gen in dem Gebiete ins Auge faßt, in dem die imaginative Er­kenntnis sich betätigt, muß ihm der Begriff des Wollens sich verflüchtigen.",
      "Es scheint wirklich einleuchtend zu sein, daß Brentano dazu getrieben worden ist, indem er das Wesen der psychi­schen Erscheinungen beschrieben hat, eigentlich das Wesen der schauenden Erkenntnis zu schildern. Selbst aus Einzel­heiten seiner Darstellung geht dies klar hervor. Man nehme ein Beispiel für viele, die angeführt werden könnten. Er sagt : «Der gemeinsame Charakterzug alles Psychischen be­steht",
      "in dem, was man häufig mit einem leider sehr mißver­ständlichen Ausdruck Bewußtsein genannt hat ... ».* Aber wenn man nur diejenigen Seelenerscheinungen schildert, welche als dem gewöhnlichen Bewußtsein angehörig von der Leibesorganisation bedingt sind, so ist der Ausdruck gar nicht mißverständlich. Brentano hat eine Empfindung davon, daß die wirkliche Seele aber in diesem gewöhnlichen Bewußtsein nicht lebt, und er fühlt sich veranlaßt, von dem Wesen dieser wirklichen Seele in Vorstellungen zu sprechen, die allerdings mißverstanden werden müssen, wenn man auf sie den gewöhnlichen Bewußtseinsbegriff anwenden will.",
      "Brentano geht in seiner Forschung so vor, daß er die Er­scheinungen des anthropologischen Gebietes bis dahin ver­folgt, wo sie den Unbefangenen dazu zwingen, Vorstellun­gen über die Seele zu bilden, welche zusammentreffen mit dem, was die Anthroposophie auf ihren Wegen über die Seele findet. Und die Ergebnisse der beiden Wege zeigen sich gerade durch Brentanos Psychologie im vollsten Ein­klange. Brentano selbst wollte aber den anthropologischen Weg nicht verlassen. Daran hinderte ihn seine Auslegung des von ihm aufgestellten Leitsatzes: «Es kann die wahre Forschungsart der Philosophie keine andere sein als die in der naturwissenschaftlichen Erkenntnisart anerkannte.»** Eine andere Auffassung dieses Leitsatzes hätte ihn dazu füh­ren können, anzuerkennen, daß man gerade dann die natur­wissenschaftliche Vorstellungsart in dem rechten Lichte sieht, wenn man sich bewußt ist, daß diese für das geistige Gebiet sich ihrem eigenen Wesen gemäß wandeln muß. Brentano hat die wahren Seelenerschenningen, welche er",
      "* Vergleiche Brentano : «Vom Ursprung sittlicher Erkenntnis», Seite 14.",
      "** Vergleiche oben Seite 81 f. dieser Schrift.",
      "als solche kennzeichnet, niemals zum Gegenstande eines ausgesprochenen Bewußtseins machen wollen. Hätte er die­ses getan, so wäre er von der Anthropologie zur Anthropo­sophie fortgeschritten. Er fürchtete diesen Weg, weil er ihn nur als ein Abirren in «mystisches Dunkel und ein freies Schweifen der Phantasie in unbekannte Regionen» anzuse­hen vermochte.* Er ließ sich auf eine Prüfung dessen gar nicht ein, was seine eigene psychologische Auffassung not­wendig machte. Jedesmal, wenn er vor der Notwendigkeit stand, seinen eigenen Weg fortzusetzen in das anthroposo­phische Gebiet hinein, blieb er stehen. Er wollte die Fragen, welche sich nur anthroposophisch beantworten lassen, an­thropologisch lösen. Diese Lösung mußte scheitern. Weil sie scheitern mußte, konnte er seine angefangenen Darstel­lungen nicht so fortsetzen, daß die Fortsetzung für ihn hätte befriedigend werden können. Hätte er die «Psychologie vom empirischen Standpunkt »fortgesetzt : sie hätte nach dem Er­gebnisse des ersten Bandes eine Anthroposophie werden müssen. Hätte er seine «Deskriptive Psychologie»wirklich geliefert : Anthroposophie müßte aus ihr überall herausleuchten. Hätte er entsprechend seinem Ausgangspunkte die Ethik seiner Schrift «Vom Ursprung sittlicher Erkenntnis» weiter geführt: er hätte auf Anthroposophie stoßen müssen.",
      "Vor Brentanos Seele stand die Möglichkeit einer Psycho­logie, die nicht wie die rein anthropologische gestaltet sein kann. Die letztere kann an die Fragen gar nicht denken, welche als die bedeutungsvollsten über das Seelenleben auf­geworfen werden müssen. Die neuere Psychologie will nur anthropologisch sein, weil sie alles darüber Hinausgehende für unwissenschaftlich hält. Brentano aber sagt : «Für die",
      "* Vergleiche oben Seite 79 dieser Schrift.",
      "Hoffnungen eines Platon und Aristoteles, über das Fortle­ben unseres besseren Teiles nach der Auflösung des Leibes Sicherheit zu gewinnen, würden dagegen die Gesetze der Assoziation von Vorstellungen, der Entwickelung von Überzeugungen und Meinungen und des Keimens und Trei­bens von Lust und Liebe alles andere, nur nicht ein wahre Entschädigung sein... Und wenn wirklich der Unterschied der beiden Anschauungen die Aufnahme oder den Ausschluß der Frage nach der Unsterblichkeit besagte, so wäre er für die Psychologie ein überaus bedeutender zu nennen, und ein Eingehen in die metaphysische Untersuchung über die Substanz als Trägerin der Zustände unvermeidlich.»* Anthroposophie zeigt, wie nicht durch metaphysische Spe­kulationen in das von Brentano bezeichnete Gebiet einge­treten werden kann, sondern allein durch Betätigung sol­cher Seelenkräfte, welche nicht in das gewöhnliche Bewußt­sein fallen können. Indem Brentano in seiner Philosophie das Wesen der Seele so schildert, daß in seiner Schilderung das Wesen der schauenden Erkenntnis deutlich zum Aus­drucke kommt, ist diese Philosophie eine vollkommene Rechtfertigung der Anthroposophie. Und man darf in Bren­tano sehen den philosophischen Forscher, der auf seinem Wege bis zur Pforte der Anthroposophie gelangt, diese Pforte aber nicht aufschließen will, weil das Bild von naturwissenschaftlicher Denkart, das er sich macht, ihm den Glauben erzeugt, er gelange durch dieses Aufschließen in den Abgrund der Unwissenschaft.",
      "* Vergleiche Brentano : «Psychologie vom empirischen Standpunkte», Seite 20.",
      "Die Schwierigkeiten, vor die sich Brentano oft gestellt sieht, wenn er seine Vorstellungen fortsetzen will, rühren davon her, daß er diese Vorstellungen über das Wesen des Seeli­schen auf dasjenige bezieht, was im gewöhnlichen Bewußt­sein vorliegt. Dazu wird er veranlaßt, weil er innerhalb der Auffassung stehen bleiben will, die ihm als die naturwissen­schaftlich berechtigte erscheint.",
      "Aber diese Auffassung kann durch ihre Erkenntuismittel eben nur zu dem gelan­gen, was von dem Seelischen als der Inhalt des gewöhnli­chen Bewußtseins vorliegt. Dieser Inhalt ist aber nicht die Wirklichkeit des Seelischen, sondern dessen Spiegelbild.",
      "Dies durchschaut Brentano nur von der einen Seite des be­greifenden Verstehens, aber nicht von der andern, der Be­obachtung. In seinen Begriffen entwirft er ein Bild seeli­scher Erscheinungen, die sich in der Wirklichkeit der Seele abspielen; wenn er beobachtet, glaubt er in dem Spiegelbild des Seelischen eine Wirklichkeit zu haben.* - Eine andere philosophische Richtung, der Brentano die schärfste Abnei­gung entgegengebracht hat, diejenige Eduard von Hartmanns, ist auch von einer naturwissenschaftlichen Vorstel­lungsart ausgegangen.",
      "Eduard von Hartmann hat den Spie­gelbild-Charakter des gewöhnlichen Bewußtseins durch­schaut. Er sieht daher in diesem Bewußtsein keine Wirklich­keit. Aber er lehnt es auch entschieden ab, die entsprechende Wirklichkeit überhaupt in ein menschliches Bewußtsein hereinzuholen.",
      "Er verweist diese Wirklichkeit in das Gebiet des Unbewußten. Über dieses zu reden, gestattet er nur der hypothetischen Anwendung der durch gewöhnliches Be­wußtsein",
      "* Vergleiche hiertnit das 7. Kapitel der am Ende dieser Schrift gegehenen «Skizzenhaften Erweiterungen des Inhaltes...» : «7. Die Sonderung des See­lischen von dem Außer-Seelischen durch Franz Brentano.»",
      "gebildeten Begriffe über dieses Gebiet hinaus.* Die Anthroposophie behauptet, daß über dieses Gebiet hin­aus geistige Beobachtung möglich ist. Und daß dieser gei­stigen Beobachtung auch Begriffe zugänglich seien, die so wenig bloß hypothetisch sein dürfen wie die im sinnlichen Felde gewonnenen. - Eduard von Hartmanns Übersinnli­ches soll kein unmittelbar Erkanntes, sondern ein aus dem unmittelbar Erkannten Erschlossenes sein. Hartmann ge­hört zu denjenigen Philosophen der neueren Zeit, die Be­griffe nicht bilden wollen, wenn sie zum Ausgangspunkte dieser Begriffsbildung nicht die Aussagen der sinnlichen Beobachtung und des Erlebens im gewöhnlichen Bewußt­sein haben. Brentano bildet solche Begriffe. Aber er täuscht sich über die Wirklichkeit, in der sie durch Beobachtung gebildet werden können. Sein Geist erweist sich als merk­würdig zwiespältig. Er möchte ganz Naturforscher in dem Sinne sein, wie sich die naturwissenschaftliche Vor­stellungsart in der neueren Zeit herausgebildet hat. Und er muß doch Begriffe bilden, welche sich vor dieser Vorstellungsart nur dann rechifertigen lassen, wenn man dieselbe nicht als die einzig geltende hinnimmt. Dieser Zwiespalt in Brentanos Forschergeist wird dem erklär­lich, der sich in die ersten Schriften Brentanos vertieft : in sein Buch : «Von der mannigfachen Bedeutung des Seien­den nach Aristoteles » (186z); in seine «Psychologie des Aristoteles» (1 867) und in seinen « Creatinismus des Aristo­teles»",
      "* Die in bezug auf obiges zielenden Anschauungen Eduard von Hartmanns findet man in übersichtlicher Art dargestellt in dessen zwei Büchern: «Die moderne Psychologie» (Leipzig 1901, Hermann Haackes Verlag) und «Grundriß der Psychologie» (Band 3 von E.v. Hartmanns System der Philosophie im Grnndriß, Bad Sachsa im Harz 1908, Hermann Haacke, Verlagsbuchhandlung).",
      "(1882).* - In diesen Schriften geht Brentano mit mu­stergiltiger Gelehrsamkeit den Gedankengängen des Aristoteles nach. Und in diesem Nachgehen eignet er sich ein Den­ken an, das sich nicht in den Begriffen erschöpfen lassen kann, die in der Anthropologie geltend sind.",
      "In diesen Schriften hat er einen Seelenbegriff im Bereiche seiner Auf­merksamkeit, welcher das Seelische aus dem Geistigen her­leitet. Dieses aus dem Geiste herstammende Seelische be­dient sich des aus physischen Vorgängen gebildeten Orga­nismus, um innerhalb des sinnlichen Daseins sich Vorstellun­gen zu bilden.",
      "Was in der Seele sich Vorstellungen bildet, ist geistiger Natur, ist der «Nus» des Aristoteles. Aber dieser «Nus» ist von zweifacher Wesenheit, als «Nus pathetikos» ist er rein leidend; er läßt sich von den durch den Organismus ihm gegebenen Eindrücken zu seinen Vorstellungen anre­gen.",
      "Damit aber diese Vorstellungen so in die Erscheinung treten, wie sie in der tätigen Seele sind, muß diese Tätigkeit als «Nus poietikos»wirken. Was der «Nus pathetikos » lie­fert, wären bloß Erscheinungen in einem finsteren Seelen-sein; sie werden beleuchtet durch den «Nus poietikos».",
      "Brentano sagt darüber : Der Nus poietikos ist das Licht, wel­ches die Phantasmen erleuchtet und das Geistige im Sinnli­chen für unser Geistesauge sichtbar macht.** - Es kommt, wenn man Brentano verstehen will, nicht allein darauf an, in­wieweit er die aristotellschen Vorstellungen in seine eigene Überzeugung aufgenommen hat, sondern vor allem darauf, daß er sich mit dem eigenen Denken in diesen Vorstellungen",
      "* Franz Brentano : «Von der mannigfachen Bedeutung des Seienden nach Aristoteles» (Freiburg im Breisgau, Herdersche Verlagshandlung); dessen «Die Psychologie des Aristoteles» (Mainz, Verlag von Franz Kirch­heim); dessen «Über den Creatinismus des Aristoteles » (Wien, Tempsky).",
      "** Vergleiche Brentano : «Die Psychologie des Aristoteles», Seite 172 ff.",
      "hingebungsvoll bewegt hat. Dadurch aber betätigte sich die­ses Denken in einem Bereiche, in dem der Ausgangspunkt der Sinnesanschauung, und damit die anthropologische Grundlage für die Begriffsbildung nicht vorhanden sind.",
      "Und dieser Grundzug des Denkens ist in Brentanos For­schung geblieben. Er will zwar nur gelten lassen, was nach dem Muster der gegenwärtigen naturwissenschaftlichen Vorstellungsart anerkannt werden kann; aber er muß Ge­danken bilden, die nicht in dieses Bereich gehören.",
      "Nun läßt sich nach rein naturwissenschaftlicher Methode über die See­lenerscheinungen nur etwas sagen, insoferne diese das durch die Leibesorganisation bedingte Spiegelbild des wirklich Wesenhaften der Seele sind, das heißt, insoferne sie in ihrem Spiegelbild-Charakter mit der Leibesorganisation entstehen und vergehen. Was aber Brentano über die Wirklichkeit des Seelischen denken muß, ist ein Geistiges, von der Leibesor­ganisation Unabhängiges, das sogar durch den «Nus poieti­kos» sich das Geistige im Sinnlichen durch unser Geistes­auge sichtbar macht. - Daß Brentano sich mit seinem Den­ken in solchen Bereichen bewegen kann, verbietet ihm, das Seelensein durch die Leibes organisation entstehend und mit der Leibesorganisation vergehend zu denken.",
      "Weil er aber eine übersinnliche Beobachtung ablehnt, so kann ihm in diesem Seelensein kein Inhalt beobachtbar sein, der über das physische Sein hinausreicht. Sobald er der Seele einen In­halt zuschreiben soll, den diese ohne die Mithilfe der Leibes-organisation entfalten könnte, fühlt sich Brentano in einer Welt, für die er keine Vorstellungen findet.",
      "In solcher Gei­stesverfassung wendet er sich an Aristoteles und findet auch bei ihm Seelenvorstellungen, die für ein außerleibliches Da­sein keinen anderen Inhalt ergeben, als den im leiblichen",
      "Dasein erworbenen. Charakteristisch in seiner Einseitig­keit ist, was in dieser Beziehung Brentano in seiner «Psychologie des Aristoteles» vorbringt : «Wie nun der Mensch, wenn ihm ein Fuß oder ein anderes Glied entrissen wird, keine vollendete Substanz mehr ist, so ist er natürlich noch viel weniger eine vollendete Substanz, wenn der ganze leib­liche Teil dem Tode anheimgefallen ist. Der geistige Teil besteht zwar noch fort, allein die irren gar sehr, die wie Plato glauben, daß die Trennung vom Leibe für ihn eine Förde­rung und gleichsam eine Befreiung aus drückendem Ge­fängnisse sei; muß ja doch die Seele nunmehr auf alle die zahlreichen Dienste verzichten, welche die Kräfte des Lei­bes ihr geleistet haben.»* - Über die Auffassung des Aristo­teles vom Wesen der Seele war Brentano in einen außeror­dentlich interessanten Streit mit dem Philosophen Eduard Zeller gekommen. Dieser behauptete, die Meinung des Aristoteles gehe dahin, eine Präexistenz der Seele vor ihrer Verbindung mit der Leibesorganisation anzunehmen, wäh­rend Brentano dem Aristoteles eine solche Ansicht ab­sprach, und ihn nur denken ließ, die Seele werde erst in die Leibesorganisation hinein geschaffen; sie habe also keine Präexistenz, wohl aber nach der Auflösung des Leibes eine Postexistenz.** Brentano meinte, eine Präexistenz nehme nur Plato, nicht aber Aristoteles an. Es ist nicht zu leugnen, daß die Gründe, welche Brentano für seine Meinung und",
      "* Vergleiche Brentano: «Psychologie des Aristoteles», Seite 196.",
      "**    Über den Inhalt des wissenschaftlichen Streites zwischen Brentano und Zeller vergleiche Brentano: «Offener Brief an Herrn Professor Dr. Eduard Zeller aus Anlaß meiner Schrift über die Lehre des Aristoteles von der Ewigkeit des Geistes» (Leipzig 1883, Duneker und Humblot) und des­sen : «Aristoteles' Lehre vom Ursprung des menschlichen Geistes» (Leip­zig 1911, Veit und Comp.).",
      "gegen die Zellersche vorbringt, viel Gewicht haben. Abge­sehen von der Brentanoschen geistvollen Interpretation entsprechender aristotelischer Behauptungen bietet es ja eine Schwierigkeit, dem Aristoteles die Ansicht von der Präexistenz der Seele zuzuschreiben, weil eine solche einem Grundsatz der aristotelischen Metaphysik zu widerspre­chen scheint. Aristoteles sagt nämlich, daß niemals eine «Form» vor dem «Stoffe» existieren könne, der die Form trägt. Die Kugelgestalt existiere niemals ohne das sie erfül­lende Stoffliche. Da aber Aristoteles das Seelische als die «Form»der Leibesorganisation faßt, so scheint es, daß man ihm nicht zuschreiben dürfe : er habe gedacht, die Seele könne vor der Entstehung der Leibesorganisation existieren.",
      "Brentano hat sich nun mit seinem Seelenbegriff in der aristotelischen Vorstellung von der Unmöglichkeit einer Präexistenz so verfangen, daß er nicht bemerken kann, wie diese aristotelische Vorstellung selbst in einem wichtigen Punkte versagt. Kann man denn wirklich «Form» und «Materie» so denken, daß man nur annimmt : die Form könne nicht vor der sie erfüllenden Materie bestehen? Die Kugelgestalt sei doch nicht vorhanden vor der sie erfül­lenden Stoffmasse? So wie sie an der Stoffmasse erscheint, ist die Kugelform gewiß nicht vor der Zusammenballung des Stoffes vorhanden. Allein bevor dieser zusammenschießt, sind die Kräfte vorhanden, welche an diesen Stoff herankommen, und deren Ergebnis für ihn sich in seiner Kugelgestalt offenbart. Und in diesen Kräften lebt vor dem Auftreten der Kugelgestalt diese schon gewiß in andrer Art.* Hätte Brentano sich nicht durch seine Auslegung",
      "* Die Täuschung über eine Berechtigung zu der oben gekennzeichneten Behauptung von Form und Materie kann nur im Hinblick auf die Bildung von Kristallen etwa entstehen, weil da die Form unmittelbar aus den der Materie innewohnenden Kräften hervorzugehen scheint. Doch wird ein unbefangenes Denken nicht anders können als die Formkräfte innerhalb des Materiellen vorauszusetzen, bevor die geformte Materie wirklich ent­steht. Völlig unhaltbar ist die aristotelische Vorstellung aber schon bei der Pflanze, deren formende Kräfte man gewiß nicht allein in den Verhältnissen im Keime suchen muß, sondern in Wirksamkeiten von der Außenwelt her, die unbegrenzt lange vor der Bildung der sinnlichen Pflanze vorhanden sind.",
      "der naturwissenschaftlichen Vorstellungsart für den Inhalt des Seelenbegriffs durch die Anschauungen über die körper­liche Organisation gebunden gefühlt, so hätte er vielleicht bemerkt, daß der aristotelische Seelenbegriff selbst mit einem inneren Widerspruch behaftet ist. So hat er denn an der Be­trachtung der Weltanschauung des Aristoteles nur die Mög­lichkeit gewonnen, über die Seele Vorstellungen zu denken, welche diese aus dem Gebiete der Leibesorganisation her­aus heben, ihr aber nicht einen solchen Inhalt zuweisen, der gestattet, daß man sie bei unbefangenem Denken wirklich von der Leibesorganisation unabhängig vorstellen kann.",
      "Neben Aristoteles ist für Brentano auch Leibniz ein Phi­losoph, dem er besondere Anerkennung zuwendet. Beson­ders die Art der Leibnizischen Seelenbetrachtung scheint ihn angezogen zu haben. Man kann nun sagen, daß Leib­niz auf diesem Gebiete eine Vorstellungsweise hat, welche wie eine wesentliche Erweiterung der Meinung des Ari­stoteles erscheint. Während dieser den wesenhaften Inhalt des menschlichen Denkens abhängig macht von der Sin­nesbeobachtung, löst Leibniz diesen Inhalt von der sinnli­chen Grundlage los. Dem Aristoteles folgend wird man den Satz anerkennen : es ist nichts im Denken, was nicht vorher in den Sinnen war (nihil est in intellectu, quod non fuerit in sensu); Leibniz aber ist der Meinung, daß nichts",
      "im Denken sei, was nicht vorher in den Sinnen war, außer das Denken selbst (nihil est in intellectu, quod non fuerit in sensu, nisi ipse intellectus). Es wäre unrichtig, dem Aristo­teles die Ansicht zuzuschreiben, daß das im Denken sich betätigende Wesenhafte ein Ergebnis der leiblichen Wir­kenskräfte sei.",
      "Aber indem er den Nus pathetikos zum lei­denden Empfänger der Sinneseindrücke, den Nus poieti­kos zum Beleuchter dieser Eindrücke machte, blieb inner­halb seiner Philosophie nichts, das Inhalt eines von dem Sinnessein unabhängigen Seelenlebens werden könnte. In dieser Beziehung erweist sich der Leibnizische Satz frucht­barer.",
      "Durch ihn wird die Aufmerksamkeit besonders hin-gelenkt auf das von der Leibesorganisation unabhängige Seelenwesen. Allerdings wird diese Aufmerksamkeit ein­geschränkt auf den bloß intellektiven Teil dieses Wesens.",
      "Und insofern ist Leibnizens Satz einseitig. Dennoch ist er eine Richtlinie, die im gegenwärtigen naturwissenschaftlichen Zeitalter zu etwas führen kann, zu dem Leibniz zu ge­langen noch nicht möglich war.",
      "Dazu waren in seiner Epo­che die Vorstellungen über den rein naturgemäßen Ur­sprung von Eigenschaften der Leibesorganisation noch zu unvollkommen. Gegenwärtig ist dies anders. Man kann heute bis zu einem gewissen Grade naturwissenschaftlich erkennen, wie sich die organischen Leibeskräfte von den Vorfahren vererben, und wie innerhalb dieser vererbten Kräfte des Organismus die Seele wirkt.",
      "Was von vielen, die glauben, auf dem rechten «naturwissenschaftlichen Stand­punkte » zu stehen, allerdings nicht zugegeben wird, erweist sich doch beim richtigen Erfassen der naturwissenschaftli­chen Erkenntnisse als notwendige Ansicht : daß alles, wo­durch die Seele im physischen Leben wirkt, bedingt ist durch",
      "die Leibeskräfte, die in der physischen Vererbung slinie von den Vorfahren auf die Nachkommen übergehen, außer dem Inhalt des Seelischen selbst. So etwa kann man gegenwärtig den Leibnizischen Satz erweitern. Dann aber ist er die an­thropologische Rechtfertigung der anthroposophischen Be­trachtungsart. Dann verweist er die Seele darauf, ihren we­senhaften Inhalt in einer geistigen Welt zu suchen, und zwar durch eine andere Erkenntnisart als die in der Anthropologie übliche. Denn dieser ist nur zugänglich, was im gewöhnli­chen Bewußtsein durch die Leibesorganisation erlebt wird.* Man kann der Ansicht sein, Brentano hätte alle Vorbedingungen gehabt, um, von Leibniz ausgehend, sich den Blick auf das im Geiste verankerte Wesenhafte der Seele zu eröffnen, und das sich diesem Blick Ergebende durch die naturwissenschaftlichen Erkenntnisse der neueren Zeit zu erkräftigen. Wer seinen Ausführungen folgt, sieht den Weg, der vor ihm gelegen war. Es hätte der Weg zu einem rein geistig erkennbaren Seelenwesen vor ihm offenbar",
      "* Es gibt Denker, welche die Ansicht, daß des Menschen seelischer We­senskern nicht von den Vorfahren ererbt ist, sondern aus der geistigen Welt kommt, abstoßend finden, weil sie dadurch den Fortpflanzungsvorgang herabgewürdigt sehen. Zu diesen Denkern gehört der Philosoph J. Frobschamaner (man vergleiche dessen Schrift «Über den Ursprung der menschlichen Seelen», Seite 98 ff.). Dieser meint, es müsse angenommen werden, daß auch die Seelen der Kinder von den Eltern stammen, da «diese lebendigen Menschen nicht etwa bloße Leiber oder gar Tiere zeugen» (ver­gleiche Frohschammers Schrift über «Die Philosophie des Thomas von Aquino», Leipzig, Brockhaus 1889, Seite VIII). Von einem aus dieser Mei­nung kommenden Einwand kann die Anschauung, die in den Ausführun­gen der vorliegenden Schrift zur Darstellung kommt, nicht betroffen wer­den. Denn man braucht den Seelenkern, der, aus der geistigen Welt kom­mend, sich mit dem von den Vorfahren Vererbten verbindet, vor der Empfängnis nicht ohne Beziehung zu den Seelen der Eltern zu denken, wenn man ihn auch nicht durch den Fortpflanzungsakt entstehend denkt.",
      "werden können, wenn er ausgebildet hätte, was im Berei­che seiner Aufmerksamkeit lag, als er solche Sätze nieder­schrieb wie diesen: «Aber wie ist» das «Eingreifen der Gottheit» beim Erscheinen einer menschlichen Seele in ei­nem Leib «zu denken? Hat sie, nachdem sie den geistigen Teil des Menschen von Ewigkeit schöpferisch hervorge­bracht hatte, ihn nun mit einem Embryo in der Art ver­bunden, daß er, der bisher als besondere geistige Substanz für sich bestand, nun aufhörte, ein wirkliches Wesen für sich zu sein, und Teil einer menschlichen Natur wurde, oder hat sie ihn erst jetzt schöpferisch hervorgebracht? -Wenn Aristoteles das erste annahm, so mußte er glauben, daß derselbe Geist wieder und wieder mit anderen und an­deren Embryonen verbunden werde; denn das Menschengeschlecht erhält sich nach ihm fortzeugend ins Unendli­che, die Menge der von Ewigkeit bestehenden Geister kann aber nur eine endliche sein.",
      "Alle Ausleger sind nun darin einig, daß Aristoteles in der reiferen Zeit seines Phi­losophierens die Palingenese verworfen hat. Also ist diese Möglichkeit ausgeschiossen.»* Was nicht in der Gedan­kenfolge des Aristoteles liegt, die Rechtfertigung des gei­stigen Blickes auf die wiederholten Leben der Menschenseele durch Palingenese : für Brentano hätte es sich ergeben können aus der Verbindung der an Aristoteles verfeiner­ten Begriffe über die Seele mit den Erkennmissen der neue­ren Naturwissenschaft. - Er hätte diesen Weg um so mehr gehen können, als er empfänglichen Sinn hatte für die Er­kermtuislehre der mittelalterlichen Philosophie.",
      "Wer diese Erkenntnislehre wirklich erfaßt, der eignet sich eine Sum­me",
      "* Vergleiche Brentano: «Aristoteles und seine Weltanschauung» (1911), Seite 134.",
      "von Ideen an, die geeignet sind, die neueren naturwis­senschaftlichen Ergebnisse zur geistigen Welt in eine Be­ziehung zu setzen, welche durch die Ideen der rein natur­wissenschaftlich-anthropologischen Forschung nicht zu durchschauen ist. Was eine Vorstellungsart wie diejenige des Thomas von Aquino für die Vertiefung der Naturwis­senschaft nach der geistigen Seite zu leisten vermag, das wird gegenwärtig in vielen Kreisen ganz verkannt.",
      "Man glaubt in solchen Kreisen, die neueren naturwissenschaft­lichen Erkenntnisse bedingten eine Abkehr von dieser Vor­stellungsart. Die Wahrheit ist, daß man zunächst das na­turwissenschaftlich erkannte Wesenhafte der Welt mit Ge­danken umspannen will, welche bei genauerem Zusehen in sich unvollendet bleiben.",
      "Ihre Vollendung wäre, sie selbst als ein solches Wesenhaftes in der Seele zu denken, wie sie in der Vorstellungsart des Thomas von Aquino gedacht werden. Brentano befand sich auch auf dem Wege, ein rechtes Verhältnis zu dieser Vorstellungsart zu gewinnen.",
      "Schreibt er doch : «Als ich meine Abhandlung und später meine schrieb, wollte ich in einer zweifachen Weise das Verständnis sei­ner Lehre fördern; einmal und vorzüglich direkt durch Aufhellung einiger der wichtigsten Lehrpunkte, dann in­direkt, aber in allgemeinerer Weise, indem ich der Erklä­rung neue Hiifsquellen eröffnete. Ich machte auf die scharfsinnigen Kommentare des Thomas von Aquino auf­merksam und zeigte, wie man in ihnen manche Lehre rich­tiger als bei späteren Erklärern dargestellt findet.»* - Brentano",
      "* Vergleiche Brentano : «Aristoteles' Lehre vom Ursprung des menach­lichen Geistes» (1911), Seite 1.",
      "verlegte sich den Weg, der sich ihm durch solche Stu­dien hätte darbieten können, durch seine Hinneigung zu der Vorstellungsart von Bacon, Locke und allem, was mit solch einer Vors tellungsart philosophisch zusammenhängt. Er hielt diese Vorstellungsart vor allem für die der natur-wissenschaftlichen Forschungsweise gemäße.* Doch eben diese Vorstellungsart führt dazu, den Inhalt des Seelenle­bens in völliger Abhängigkeit von der Sinneswelt zu den­ken.",
      "Und weil diese Denkweise nur anthropologisch vor­gehen will, so kommt nur dasjenige als psychologisches Ergebnis in ihren Bereich, was in Wahrheit keine seelische Wirklichkeit ist, sondern nur ein Spiegelbild dieser Wirk­lichkeit, nämlich der Inhalt des gewöhnlichen Bewußt­seins. - Hätte Brentano die Spiegelbild-Natur des gewöhn­lichen Bewußtseins durchschaut : er hätte im Verfolg der anthropologischen Forschung nicht haltmachen können vor dem Tore, das in die Anthroposophie führt. - Es wird gewiß dieser meiner Anschauung gegenüber die Meinung geltend gemacht werden können, Brentano habe eben der Gabe des geistigen Schauens ermangelt; deshalb habe er nicht den Übergang von Anthropologie zur Anthroposo­phie gesucht, wenn er auch durch seine besondere geistige Eigenart dazu getrieben worden ist, in interessanter Form die Seelenerscheinungen so verstandesgemäß zu charak­terisieren, daß sich diese Form durch die Anthroposophie rechifertigen läßt. Ich habe aber diese Meinung nicht.",
      "Ich bin nicht der Anschauung, daß geistiges Schauen nur als",
      "* Vergleiche unter anderem Brentano: «Die vier Phasen der Philosophie» (1895), Seite 22, und die ganze Haltung seiner Wiener Antrittsrede «Über die Gründe der Entmutigung auf philosophischem Gebiete» (Wien 1874, W. Braumüller).",
      "eine besondere Gabe für Ausnahmepersönlichkeiten er­reichbar ist. Ich muß dieses Schauen für eine Fähigkeit der Menschenseele halten, die jeder sich aneignen kann, wenn er die zu ihr führenden seelischen Erlebnisse in sich wach­ruft. Und Brentanos Natur erscheint mir zu solchem Wach-Rufen ganz besonders geeignet.* Ich halte aber dafür, daß man solches Wach-Rufen durch Theorien, die ihm wider­streben, verhindern kann. Daß man das Schauen nicht auf­kommen läßt, wenn man sich in Ideen verstrickt, welche dessen Berechtigung von vorneherein in Frage stellen. Und Brentano hat das Schauen in seiner Seele dadurch nicht aufkommen lassen, daß bei ihm die Ideen, welche es in so schöner Art rechifertigten, stets unterlagen denen, die es verwerfen, und die befürchten lassen, daß man durch dasselbe in « den labyrinthischen Gängen einer Pseudo­philosophie sich verliere».**",
      "1895 hat Brentano den Abdruck eines Vortrages erschei­nen lassen, den er in der « Literarischen Gesellschaft in Wien» mit Rücksicht auf H.Lorms Buch «Der grundlose Optimismus» gehalten hat.*** Dieser enthält seine Ansicht über «die vier Phasen der Philosophie und ihren augen­blicklichen Stand». Brentano vertritt in diesen Ausführun­gen die Meinung, daß sich der Entwickelungsgang des philosophischen Forschens in einer gewissen Beziehung",
      "*    Man vergleiche Herzu das 8. Kapitel der am Ende dieser Schrift gege­benen «Skizzenhaften Erweiterungen des Inhaltes...» : «8. Ein oft erhobener Einwand gegen die Anthroposophie.»",
      "** Vergleiche oben Seite 79.",
      "*** Brentano : «Die vier Phasen der Philosophie und ihr augenblicklicher Stand» (Stuttgart 1895, J. G.Cottasche Buchhandlung Nachfolger).",
      "vergleichen lasse mit der Geschichte der schönen Künste. «Während andere Wissenschaften, so lange sie überhaupt betrieben werden, einen stetigen Fortschritt aufweisen, der nur einmal durch eine Zeit des Stillstandes unterbrochen wird, zeigt die Philosophie, wie die schöne Kunst, neben den Zeiten aufsteigender Entwickelung Zeiten der Deca­dence, die oft nicht minder reich, ja reicher an epochema­chenden Erscheinungen sind als die Zeiten gesunder Fruchtbarkeit.»* Drei solcher Perioden, die von gesunder Fruchtbarkeit zur Decadence fortlaufen, unterscheidet Brentano im verflossenen Entwickelungsgang der Philo­sophie.",
      "Eine jede beginnt damit, daß aus dem reinen philo­sophischen Staunen über die Rätsel der Welt sich wahr­haft wissenschaftliches Interesse regt, und dieses Interesse eme Erkenntnis aus echtem, reinem Wissenstrieb sucht. Auf diese gesunde Epoche folgt dann eine andere, in der das erste Stadium des Verfalls erscheint.",
      "Da tritt das reine wissenschaftliche Interesse zurück, und man sucht nach Gedanken, durch die man das soziale und persönliche Le­ben regeln und sich in denselben zurechtfinden kann. Die Philosophie will da nicht mehr dem reinen Erkenntnisstre­ben, sondern den Interessen des Lebens dienen.",
      "Ein wei­terer Verfall tritt in der dritten Epoche ein, Man wird durch die Unsicherheit der Gedanken, die einem nicht rei­nen wissenschaftlichen Interesse entsprungen sind, an der Möglichkeit wahrer Erkenntnis irre und verfällt in Skep­tizismus. Die vierte Epoche ist dann diejenige des völligen Niederganges.",
      "Der Zweifel der dritten Epoche hat alle wissenschaftliche Grundlage der Philosophie unterhöhlt. Man sucht aus unwissenschaftlichen Untergründen in",
      "* Vergleiche «Vier Phasen», Seite 9.",
      "phantastischen, verschwimmenden Begriffen, durch my­stisches Erleben zur Wahrheit zu kommen. Den ersten Entwickelungskreis denkt sich Brentano mit der griechi­schen Naturphilosophie beginnend; und mit Aristoteles, meint er, schließe die gesunde Phase ab.",
      "Anaxagoras schätzt er innerhalb dieser Phase besonders hoch ein. Er ist der Ansicht, daß, trotzdem in dieser Zeit die Griechen in bezug auf viele wissenschaftliche Fragen, ganz im Anfange standen, die Art ihres Forschens doch einen solchen Charakter hatte, der vor einer strengen naturwissenschaft­lichen Denkungsart seine Rechtfertigung findet.",
      "Auf diese erste Phase folgen die Stoiker, die Epikuräer. Sie bringen schon einen Verfall. Sie wollen Ideen, die im Dienste des Lebens stehen. In der Neueren Akademie, besonders aber durch Aenesidemus, Agrippa, Sextus Empirikus sieht man den Skeptizismus allen Glauben an sichergestellte wissen­schaftliche Wahrheiten austilgen.",
      "Und im Neuplatonismus, bei Ammonius Sakkas, Plotin, Porphyrius, Jamblichus, Proklus tritt an die Stelle des wissenschaftlichen Forschens das in den labyrinthischen Gängen einer Pseudophiloso­phie sich ergehende mystische Erleben. - Im Mittelalter sieht man, wenn auch vielleicht nicht mit solcher Deutlich­keit, diese vier Phasen sich wiederholen. Mit Thomas von Aquino hebt eine philosophisch gesunde Vorstellungsart an, die den Aristotelismus in einer neuen Form aufleben läßt.",
      "In der darauf folgenden Zeit, deren Repräsentant Duns Scotus ist, herrscht durch eine ins Ungeheuerliche getriebene Disputierkunst, eine Art Analogon zur ersten griechischen Verfallsperiode. Auf sie folgt der Nominalis­mus, der einen skeptischen Charakter trägt.",
      "Wilhelm von Occam verwirft die Ansicht, daß sich die allgemeinen",
      "Ideen auf etwas Wirkliches beziehen, und gibt dadurch dem Inhalte der menschlichen Wahrheit nur den Wert einer außer der Wirklichkeit stehenden begrifflichen Zu­sammenfassung; während die Wirklichkeit nur in den individuellen Einzeldingen liegen soll. Dieses Analogon der Skepsis wird abgelöst durch die nicht in wissenschaftlichen Bahnen strebende Mystik der Eckhardt, Tauler, Heinrich Suso, des Verfassers der Deutschen Theologie und ande­rer.",
      "Dies sind die vier Phasen der philosophischen Ent­wickelung im Mittelalter. - In der Neuzeit beginnt mit Bacon von Verulam wieder eine gesunde, auf naturwissen­schaftlichem Denken ruhende Entwickelung, in welcher dann Descartes, Locke, Leibniz fruchtbringend weiter wir­ken. Auf sie folgt die französische und englische Aufklä­rungsphilosophie, in denen Grundsätze, wie man sie für das Leben sympathisch fand, die Haltung des philosophi­schen Gedankenganges beherrschten.",
      "Darauf tritt mit Da­vid Hume die Skepsis ein; und auf sie folgt die Phase des Niedergangs, die in England mit Thomas Reid, in Deutsch­land mit Kant einsetzt. Brentano betrachtet an Kants Phi­losophie eine Seite, die ihm gestattet, diese zusammenzubringen mit der Plotinschen Verfallsperiode der griechi­schen Philosophie.",
      "Er tadelt an Kant, daß dieser nicht wie ein wissenschaftlicher Forscher die Wahrheit in einer Übereinstimmung der Vorstellungen mit den wirklichen Ge­genständen suche, sondern vielmehr darin, daß sich die Gegenstände nach dem menschlichen Vorstellungsvermö­gen richten sollen. Damit glaubt Brentano der Kantschen Philosophie eine Art mystischen Grundzuges zuschreiben zu müssen, der sich dann in der Verfallsphilosophie Fich­tes, Schellings und Hegels in völliger Unwissenschaftlichkeit",
      "offenbart. - Einen neuen Aufschwung der Philosophie erhofft Brentano von einer wissenschaftlichen Arbeit innerhalb ihres Gebietes nach dem Muster der in der neue­ren Zeit herrschend gewordenen naturwissenschaftlichen Denkungsart. Zur Einleitung einer solchen Philosophie hat er seine These aufgestellt : die wahre philosophische Forschungsart sei keine andere als die in der naturwissen­schaftlichen Erkennntisart anerkannte.* Ihr wollte er seine Lebensarbeit widmen.",
      "Brentano sagt in der Vorrede zu dem Abdruck des Vor­trages, in dem er diese Ansicht von den « vier Phasen der Philosophie» gegeben hat: diese «seine Auffassung der Geschichte der Philosophie mag manchen als neu befrem­den; mir selbst steht sie seit Jahren fest und wurde auch seit mehr als zwei Dezennien, wie von mir, so von einigen Schülern den akademischen Vorlesungen über Geschichte der Philsophie zugrunde gelegt. Daß sie Vorurteilen be­gegnen, und daß diese vielleicht zu mächtig sein werden, um beim ersten Anprall zu weichen, darüber ergebe ich mich keiner Täuschung. Immerhin hoffe ich von den vor­geführten Tatsachen und Erwägungen, daß sie bei dem, welcher denkend folgt, nicht ohne Eindruck bleiben kön­nen.»** - Daß man von diesen Ausführungen Brentanos einen be­deutenden Eindruck empfangen kann, ist durchaus meine Meinung. Insofern sie eine Klassifikation der im Laufe der philosophischen Entwickelung auftretenden Erscheinun­gen von einem gewissen Gesichtspunkte aus darbieten, be­ruhen sie auf gut begründeten Einsichten in diesen Entwickelungsgang.",
      "*    Vergleiche oben Seite 81 f. dieser Schrift.",
      "**    Vergleiche Brentano: «Die vier Phasen der Philosophie...», Seite 5 f.",
      "Die vier Phasen der Philosophie bieten Un­terschiede, die in der Wirklichkeit begründet sind. - Sobald man aber in eine Betrachtung der in den einzelnen Phasen treibenden Kräfte eintritt, kann man nicht finden, daß Bren­tano diese Kräfte zutreffend charakterisiert. Sogleich bei sei­ner Ansicht über die erste Phase der Philosophie des Alter­tums tritt das zutage. Die Grundzüge der griechischen Phi­losophie von den jonischen Anfängen bis zu Aristoteles weisen gewiß viele Züge auf, welche Brentano das Recht geben, in ihnen eine naturwissenschaftliche Denkart in sei­nem Sinne zu sehen. Aber kommt denn diese Denkart wirk­lich durch dasjenige zustande, was Brentano die naturwis­senschaftliche Methode nennt? Sind die Gedanken dieser griechischen Philosophen nicht vielmehr ein Ergebnis des­sen, was sie als das Wesen des Menschen und dessen Stel­lung zum Weltall in der eigenen Seele erlebten ?* Wer sich diese Frage sachgemäß beantwortet, wird finden, daß die inneren Impulse für den Gedankengehalt dieser Philoso­phie gerade im Stoizismus, im Epikuräismus, in der ganzen praktischen Lebensphilosophie der späteren Griechenzeit zum unmittelbaren Ausdruck kamen. Man kann bemerken, wie in den Seelenkräften, welche Brentano in der zweiten Phase wirksam findet, der Ausgangspunkt liegt für die erste Phase der Philosophie des Altertums. Diese Kräfte waren",
      "* Im ersten Bande meines Buches «Die Rätsel der Philosophie » habe ich den Versuch gemacht, diese Frage im bejahenden Sinne zu beantworten. Ich bestrebe mich da, zu zeigen, wie die ersten griechischen Philosophen nicht aus der Naturbeobachtung heraus zu ihren Ideen kommen, sondern weil sie die äußere Natur von dem Erlebnisse ihres Seelen-Innern aus beur­teilten. Thales sprach davon, daß alles aus dem Wasser stamme, weil er die­sen Wasser-Entstehungs-Prozeß als das Wesen des eigenen menschlichen Inneren erlebte. Und so die ihm verwandten Philosophen. Vergleiche meine «Rätsel der Philosophie», Seite 52 ff.",
      "der sinnlichen und sozialen Erscheinungsform des Weltalls zugewendet und konnten daher in der Phase des Skeptizis­mus, der zum Zweifel an der unmittelbaren Wirklichkeit dieser Erscheinungsform getrieben wird, und in der folgen­den Phase des schauenden Erkennens, das über diese Form hinausgehen muß, nur unvollkommen auftreten. Aus die­sem Grunde zeigen sich diese Phasen innerhalb der Philoso­phie des Altertums als solche des Verfalls. - Und welche Seelenkräfte wirken im philosophischen Entwickelungsgang des Mittelalters?",
      "Daß im Thomismus die Höhe dieses Entwickelungsganges liegt in bezug auf diejenigen Verhält­nisse, die Brentano ins Auge faßt, wird niemand bezweifeln können, der die in Betracht kommenden Tatsachen wirklich kennt. Aber man kann doch nicht verkennen, daß durch den christlichen Standpunkt des Thomas von Aquino die in der griechischen Lebensphilosophie wirksamen Seelenkräfte nicht mehr bloß aus philosophischen Impulsen heraus wir­ken, sondern einen überphilosophischen Charakter ange­nommen haben.",
      "Welche Impulse aber wirken bei Thomas von Aquino, insoferne er Philosoph ist? Man braucht keine Neigung für die Schwächen der nominalistischen Philoso­phen des Mittelalters zu haben; aber man wird doch finden können, daß die im Nominalismus wirkenden Seelenim­pulse die subjektive Grundlage bilden auch für den thomi­stischen Realismus.",
      "Wenn Thomas die Allgemeinbegriffe, welche die Erscheinungen der Sinneswahrnehmungen zu­sammenfassen, als dasjenige erkennt, was sich auf ein geistig Wirkliches bezieht, so gewinnt er die Kraft zu dieser seiner realistischen Vorstellungsart aus dem Gefühl desjenigen heraus, was diese Begriffe abgesehen davon, daß sie sich auf Sinneserscheinungen beziehen, in dem Dasein der Seele",
      "selbst bedeuten. Gerade weil Thomas die Allgemeinbegriffe nicht unmittelbar auf die Vorkommnisse des Sinnesdaseins bezog, empfand er, wie in sie eine andere Wirklichkeit hereinleuchtet, und wie sie eigentlich für die Erscheinungen des Sinnenlebens nur Zeichen sind.",
      "Als dann im Nominalis­mus dieser Unterton des Thomismus als selbständige Philo­sophie auftrat, mußte er naturgemäß seine Einseitigkeit of­fenbaren. Das Gefühl, daß die in der Seele erlebten Begriffe einen ins Geistige gewandten Realismus begründen, mußte schwinden, und das andere vorherrschend werden, daß die Allgemeinbegriffe bloße zusammenfassende Namen sind.",
      "Wenn man die Wesenheit des Nominalismus so auffaßt, ver­steht man auch die ihm vorangehende zweite Phase der mit­telalterlichen Philosophie, den Skotismus, als einen Über­gang zum Nominalismus. Man wird aber doch nicht umhin können, die ganze Kraft der mittelalterlichen Denkarbeit, insoferne sie Philosophie ist, aus der Grundauffassung heraus zu verstehen, die sich in einseitiger Art im Nominalismus gezeigt hat.",
      "Dann aber wird man zu der Ansicht kommen, daß die wirklich treibenden Kräfte dieser Philosophie in den Seelenimpulsen liegen, welche man im Sinne der Brentano­schen Klassifikation als der dritten Phase angehörig bezeich­nen muß. Und in derjenigen Epoche, welche Brentano als die mystische Phase des Mittelalters kennzeichnet, tritt dann auch klar hervor, wie die ihr angehörigen Mystiker, durch die nominalistische Natur des begreifenden Erkennens be­wogen, sich nicht an dieses, sondern an andere Seelenkräfte wenden, um zum Kerne der Welterscheinungen vorzudrin­gen. - Verfolgt man nun für die Philosophie der neueren Zeit die Wirksamkeit der treibenden Seelenkräfte an dem Faden der Brentanoschen Klassifikation, so findet man, daß",
      "die inneren Wesenszüge dieser Epoche ganz andere sind, als diejenigen, welche von Brentano verzeichnet werden. Die Phase der naturwissenschaftlichen Denkart, welche Brentano durch Bacon von Verulam, Descartes, Locke, Leibniz verwirklicht findet, will sich gewisser ihr eigener Charakterzüge wegen durchaus nicht als rein naturwissen­schaftlich im Brentanoschen Sinne denken lassen.",
      "Wie soll man dem Grundgedanken Descartes' «Ich denke, also bin ich» rein naturwissenschaftlich beikommen; wie soll man Leibnizens Monadologie, oder dessen «vorbestimmte Har­monie » in die naturwissenschaftliche Vorstellungsart Bren­tanos hineinbringen? Auch die Brentanosche Auffassung der zweiten Phase, welcher er die französische und englische Aufklärungsphilosophie zuteilt, macht Schwierigkeiten, wenn man bei seinen Vorstellungen stehen bleiben will.",
      "Man wird dieser Epoche gewiß den Charakter einer Ver­fallszeit der Philosophie nicht absprechen wollen; aber man kann sie verstehen aus der Tatsache heraus, daß in ihren Trägern die in der christlichen Lebensanschauung ener­gisch wirksamen außerphilosophlschen Seelenimpulse ge­lähmt waren, so daß ein Verhältnis zu den übersinnlichen Weltkräften philosophisch nicht gefunden werden konnte. Zugleich wirkte die nominalistische Skepsis des Mittelal­ters noch nach, wodurch verhindert wurde, daß eine Bezie­hung des seelisch erlebten Erkennmis-Inhaltes zu einem geistig Wirklichen gesucht wurde. - Und schreitet man dann zu dem neuzeitlichen Skeptizismus und derjenigen Vorstellungsweise fort, die Brentano einer mystischen Phase zueignet, dann verliert man die Möglichkeit, seiner Klassifikation noch zuzustimmen.",
      "Gewiß muß man die skeptische Phase mit David Hume beginnen lassen. Aber",
      "Kant, den Kritiker, als Mystiker kennzeichnen, erweist sich denn doch als stark einseitige Charakteristik. Und die Philo­sophien Fichtes, Schellings, Hegels und anderer Denker der auf Kant folgenden Zeit lassen sich nicht als mystische fas­sen, besonders, wenn man den Brentanoschen Begriff der Mystik zugrunde legt.",
      "Man wird vielmehr gerade im Sinne der Brentanoschen Klassifikation von David Hume über Kant, bis zu Hegel einen gemeinsamen Grundzug finden. Dieser besteht in der Ablehnung, auf Grund derjenigen Vorstellungen, die aus der Sinneswelt gewonnen sind, das philosophische Weltbild einer wahren Wirklichkeit zu zeichnen.",
      "So paradox es scheint, Hegel einen Skeptiker zu nennen : er Ist es doch in dem Sinne, daß er den Vorstellun­gen, welche der Natur entnommen sind, keinen unmittelba­ren Wirklichkeitswert zuschreibt. Man weicht von dem Brentanoschen Begriff des Skeptizismus nicht ab, wenn man die Entwickelung der Philosophie von Hume bis Hegel als die Phase des neuzeitlichen Skeptizismus auffaßt.",
      "Die vierte neuzeitliche Phase kann man erst nach Hegel beginnen las­sen. Was in ihr als naturwissenschaftliche Vorstellungsart auftritt, wird aber Brentano sicherlich nicht in die Nähe des Mystizismus bringen wollen.",
      "Doch man fasse ins Auge, in welcher Art Brentano selbst sich mit seinem Philosophieren in diese Epoche hineinstellen will. Mit einer kaum zu über­bietenden Energie fordert er für die Philosophie eine natur­wissenschaftliche Methode.",
      "In seiner psychologischen For­schung strebt er die Innehaltung dieser Methode an. Und was er zutage fördert, ist eine Rechtfertigung der Anthropo­sophie. Was als Fortsetzung seines anthropologischen Stre­bens auftreten müßte, wenn er im Sinne des von ihm Vorge­stellten weiter schritte, wäre Anthroposophie.",
      "eine Anthroposophie, welche mit der naturwissenschaftli­chen Denkungsart in voller Harmonie steht. - Ist nicht Brentanos Lebensarbeit selbst der vollgültigste Beweis dafür, daß die vierte Phase der neuzeitlichen Philosophie ihre Impulse aus denjenigen Seelenkräften ziehen muß, welche der Neuplatonismus ebenso wie die Mystik des Mittelalters betätigen wollten, aber nicht konnten, weil sie mit dem inneren Seelenwirken nicht bis zu einem solchen Erleben der geisti­gen Wirklichkeit zu kommen vermochten, das in völliger bewußter Klarheit des Denkens (oder der Begriffe) sich vollzieht? Wie die griechische Philosophie ihre Kraft aus den Seelenimpulsen schöpfte, welche Brentano in der zwei­ten philosophischen Phase sich verwirklichen sieht, aus der praktischen Lebensphilosophie; wie die mittelalterliche Philosophie den Impulsen der dritten Phase, dem Skeptizis­mus ihre Stärke verdankt; so muß die neuzeitliche Philoso­phie ihre Impulse aus den Grund-Kräften der vierten Phase holen, aus dem erkennenden Schauen. Darf also Brentano in dem Neuplatonismus und in der mittelalterlichen Mystik Verfallsphilosophien in Gemäßheit seiner Vorstellungsart annehmen, so könnte man in der die Anthropologie ergän­zenden Anthroposophie die fruchtbare Phase der neueren Philosophie anerkennen, wenn man dieses Philosophen ei­gene Ideen über Philosophie-Entwickelung zu den Konse­quenzen führt, die er nicht selbst gezogen hat, die aber ganz ungezwungen sich aus ihnen ergeben.",
      "In dem gekennzeichneten Verhältnis Brentanos zu den Er­kenntnis-Forderungen der Gegenwart ist es wohl gelegen, daß man beim Lesen seiner Schriften Eindrücke empfängt,",
      "welche sich nicht in dem erschöpfen, was der unmittelbare Inhalt der von ihm vorgebrachten Begriffe enthält. Es klin­gen in dieses Lesen überall Untertöne hinein. Diese kom­men aus einem Seelenleben, das hinter den ausgesprochenen Ideen weit zurückliegt. Was Brentano im Geiste des Lesers anregt, ist oft stärker in diesem wirksam, als das von dem Verfasser in scharf umrissenen Vorstellungen Gesagte. Man fühlt sich auch veranlaßt, oftmals zum Lesen einer Brenta­noschen Schrift zurückzukehren. Man kann vieles von dem durchdacht haben, was gegenwärtig über das Verhältnis der Philosophie zu andern Erkenntnisvorstellungen gesagt wird; Brentanos Schrift «Über die Zukunft der Philoso­phie» wird bei solchem Durchdenken fast immer in der Er­innerung auftauchen. Diese Schrift gibt einen Vortrag wie­der, den er in der «Philosophischen Gesellschaft» in Wien 1892 gehalten hat, um seine Auffassung über die Zukunft der Philosophie den hierauf bezüglichen Ansichten entge­genzuhalten, welche der Rechtsgelehrte Adolf Exner in ei­ner Inaugurationsrede über «politische Bildung» (1 891) vorgebracht hatte.* Der Abdruck des Vortrages ist mit «Anmerkungen» versehen, die weitweisende geschichtli­che Ausblicke in den geistigen Entwickelungsgang der Menschheit geben. - In dieser Schrift klingt alles an, was sich dem Betrachter der gegenwärtigen naturwissenschaft­lichen Vorstellungsart über die Notwendigkeit ergeben kann, von dieser Vorstellungsart aus zu einer anthroposo­phischen fortzuschreiten.",
      "* Brentano : «Über die Zukunft der Philosophie». Mit apologetisch-kritischer Berücksichtigung der Inaugurationsrede von Adolf Exner «Über politische Bildung» als Rektor der Wiener Universität (Wien, Alfred Höl­der, 1893).",
      "Die Träger dieser naturwissenschaftlichen Vorstellungsart leben zumeist in dem Glauben, daß sie ihnen von dem wirklichen Sein der Dinge selbst aufgedrängt ist. Sie sind der Meinung, daß sie ihre Erkenntnisse so einrichten, wie die Wirklichkeit sich offenbart.",
      "Doch dieser Glaube ist eine Täuschung. Die Wahrheit ist, daß in der neueren Zeit die menschliche Seele aus ihrer eigenen, im Laufe der Jahrtau­sende tätigen, Entwickelung heraus Bedürfnisse nach sol­chen Vorstellungen entfaltet hat, welche das naturwissen­schaftliche Weltbild ausmachen.",
      "Helmholtz. Weisman, Huxiey und andere sind zu ihren Vorstellungen nicht des­halb gekommen, weil die Wirklichkeit ihnen diese als die absolute Wahrheit gegeben hat, sondern weil sie in sich diese Vorstellungen bilden mußten, um durch sie auf die ihnen entgegentretende Wirklichkeit ein gewisses Licht zu werfen.",
      "Man formt sich ein mathematisches oder mechani­sches Weltbild nicht, weil eine außerseelische Wirklichkeit dazu zwingt, sondern weil man in seiner Seele die mathema­tischen und mechanischen Vorstellungen ausgebildet und sich dadurch eine innere Beleuchtungsquelle für das eröffnet hat, was in der Außenwelt auf mathematische und mechani­sche Art sich offenbart. - Obgleich nun im allgemeinen das eben Gekennzeichnete für jede Entwickelungsstufe der menschlichen Seele gilt : es erscheint an den neueren natur-wissenschaftlichen Vorstellungen noch auf eine besondere Weise. Diese Vorstellungen vernichten, wenn sie folgerecht von einer Seite durchdacht werden, die Begriffe über das Seelische.",
      "An dem durchaus nicht unerheblichen aber höchst fragwürdigen Begriffe einer «Seelenlehre ohne Seele», der nicht von philosophischen Dilettanten allein, sondern von sehr ernsten Denkern gebildet worden ist,",
      "zeigt sich dieses.* Solche Vorstellungen bringen dazu, die Erscheinungen des gewöhnlichen Bewußtseins in ihrer Ab­hängigkeit von der Leibesorganisation immer mehr zu durchschauen. Wird damit nicht zugleich erkannt, daß in dem, was in dieser Art als Seelisches auftritt, nicht dieses selbst, sondern nur dessen Spiegelbild sich offenbart, dann entwindet sich der Betrachtung die wirkliche Idee des See­lischen, und die Schein-Idee tritt auf, die in dem Seelischen nur sieht, was Ergebnis der Leibesorganisation ist.",
      "Nun läßt sich andrerseits für das unbefangene Denken die letz­tere Ansicht aber doch nicht halten. Die Ideen, welche die Naturwissenschaft über die Natur bildet, erweisen vor die­sem unbefangenen Denken ihren seelischen Zusammen­hang mit einer hinter der Natur liegenden Wirklichkeit, der in diesen Ideen selbst sich nicht offenbart.",
      "Keine anthropo­logische Betrachtungsart kann von sich aus zu erschöpfen­den Vorstellungen über diesen Zusammenhang kommen. Denn er tritt nicht in das gewöhnliche Bewußtsein herein. - Diese Tatsache tritt bei den gegenwärtigen naturwissen­schaftlichen Vorstellungen stärker zutage als bei geschicht­lich vergangenen Erkenntnisstufen.",
      "Die letzteren bildeten bei der Beobachtung der Außenwelt noch Begriffe, welche in ihren Inhalt etwas von der geistigen Unterlage dieser Außenwelt hereinnahmen. Und die Seele fühlte sich in ihrer eigenen Geistigkeit mit dem Geiste der Außenwelt als in einer Einheit.",
      "Die neuere Naturwissenschaft muß, ihrem Wesen nach, die Natur eben rein naturgemäß denken. Dadurch",
      "* Auch diese Vorstellung «Seelenlehre ohne Seele» gehört in den Be­reich der in dieser Schrift gekennzeichneten Rätsel an den «Grenzorten des Erkennens»; und wird sie nicht so durchlebt, daß sie als Ausgangspunkt für das schauende Bewußtsein genommen wird, so vermauert sie den Zugang zu dem wahren Seelen-Erkennen, Statt einen Weg zu ihm zu zeigen.",
      "gewinnt sie die Möglichkeit, wohl den Inhalt ihrer Ideen durch die Naturbeobachtung zu rechtfertigen, nicht aber das Dasein dieser Ideen, als inneres Seelisch-Wesenhaf­tes, selbst. - Aus diesem Grunde ist gerade die echt naturwissenschaftliche Vorstellungsart ohne allen Boden, wenn sie ihr eigenes Dasein nicht rechtfertigen kann durch eine anthroposophische Beobachtung. Mit Anthroposophie kann man in uneingeschränkter Art sich zu der naturwis­senschaftlichen Vorstellungsweise bekennen; ohne Anthro­posophie wird man immer aufs neue den vergeblichen Ver­such machen wollen, aus naturwissenschaftlichen Beobach­tungsergebnis sen heraus selbst den Geist zu entdecken. Die naturwissenschaftlichen Ideen der neueren Zeit sind eben Erzeugnisse des Zusammenlebens der Seele mit einer geisti­gen Welt; aber wissen kann die Seele von diesem Zusammen­leben nur in lebendiger Geistbetrachtung.*",
      "Man könnte leicht auf die Frage kommen: Warum sucht denn die Seele naturwissenschaftliche Vorstellungen auszu­bilden, wenn sie sich dadurch geradezu einen Inhalt schafft, der sie von ihrer Geist-Grundlage abschneidet? Vom Stand­punkte einer solchen Meinung, welche die naturwissen­schaftlichen Vorstellungen deshalb gebildet glaubt, weil die Welt nun einmal ihnen gemäß sich offenbart, läßt sich auf diese Frage keine Antwort finden. Wohl aber ergibt sich eine solche, wenn man auf die Bedürfnisse des seelischen Le­bens",
      "* Wohin eine echte natutwissenschaftliche Bettachtungsart kommt, das zeigt in einleuchtender Art das in vielen Beziehungen hervotragende Buch Oskar Hertwigs: «Das Werden des Organismen, Widerlegung von Darwins Zufallstheorie» (1916). Gerade wenn eine Arbeit, wie die dieser Schrift zugrund liegende, in so mustergiltiger Art naturwissenschaftlich-methodiseh gehalten ist, führt sie zu unzähligen Seelen-Erlebnissen an den «Grenzorten des Erkennens».",
      "selbst sieht. Mit Vorstellungen, wie sie eine vornatur­wissenschaftliche Zeit allein ausgebildet hat, könnte das see­lische Erleben niemals zum vollen Bewußtsein seiner selbst gelangen. Es würde zwar in den Natur-Ideen, die Geistiges mitenthalten, einen unbestimmten Zusammenhang mit dem Geiste erfühlen, nicht aber des Geistes volle, unabhängige Eigenart erleben können. Es strebt daher das Seelische im Entwickelungsgang der Menschheit nach der Aufstellung solcher Ideen, welche dieses Seelische selbst nicht enthalten, um an ihnen, sich selbst unabhängig vom Naturdasein zu wis­sen. Der Zusammenhang mit dem Geiste muß aber dann nicht durch diese Natur-Ideen, sondern durch geistiges Schauen erkennend gesucht werden. Die Ausbildung der neueren Naturwissenschaft ist eine notwendige Stufe im Seelen-Entwickelungsgange der Menschheit. Man erkennt ihre Grundlage, wenn man einsieht, wie die Seele ihrer be­darf, um sich selbst zu finden. Man erkennt auf der andern Seite ihre erkenntnistheoretische Tragweite, wenn man durchschaut, wie gerade sie das geistige Schauen zu einer Notwendigkeit macht.*",
      "Adolf Exner, gegen dessen Meinung Brentanos Schrift «Die Zukunft der Philosophie» gerichtet ist, stand einer Naturwissenschaft gegenüber, welche zwar die Natur-Ideen rein ausbilden will, die aber nicht bereit ist, zur Anthropo­sophie fortzuschreiten, wenn es sich um die Erfassung der seelischen Wirklichkeit handelt. Er fand die «naturwissen­schaftliche Bildung» unfruchtbar für die Ausgestaltung der",
      "* Das oben Ausgesprochene findet man im einzelnen dargestellt in mei­nem Buche: «Die Rätsel der Philosophie.» Zu zeigen, wie das naturwissen­schaftliche Erkennen im Seelenfortschritt der Menschheit seine Kraft be­währt, bildet einen der Grundgedanken dieses Buches.",
      "Ideen, die im gesellschaftlichen Zusammenleben der Men­schen wirken müssen. Er fordert daher eine Denkungsart für die Lösung der dem kommenden Zeitalter bevorstehen­den Fragen des Gesellschaftslebens, die nicht auf naturwis­senschaftlicher Grundlage ruht.",
      "Er findet, daß die großen juristischen Fragen, welchen das Römertum gegenüber­stand, von diesem gerade deshalb so fruchtbringend gelöst worden sind, weil die Römer für naturwissenschaftliche Vorstellungsart wenig Begabung hatten. Und er versucht, zu zeigen, daß das achtzehnte Jahrhundert trotz seiner Nei­gung zu naturwissenschaftlicher Denkungsart sich der Be­zwingung der Gesellschaftsfragen wenig gewachsen ge­zeigt hat.",
      "Exner richtet seinen Blick auf eine naturwissen­schaftliche Vorstellungsart, die nicht um ihre eigenen Grundlagen wissenschaftlich bemüht ist. Man kann verste­hen, daß er einer solchen gegenüber zu seinen Ansichten ge­kommen ist.",
      "Denn sie muß ihre Ideen so ausgestalten, daß diese das Naturgemäße in seiner Reinheit vor die Seele füh­ren. Aus ihnen läßt sich kein Impuls für Gedanken gewin­nen, die im Gesellschaftsleben fruchtbar sind.",
      "Denn inner­halb dieses Lebens stehen Seelen den Seelen als solchen ge­genüber. Ein solcher Impuls kann sich nur ergeben, wenn das Seelische in seiner geistigen Art durch erkennendes Schauen erlebt wird, wenn die naturwissenschaftlich-an­thropologische Betrachtung in der anthroposophischen ihre Ergänzung findet. - Brentano trug in seiner Seele Ideen, die durchaus in das anthroposophische Gebiet mün­den, trotzdem er nur im Anthropologischen bleiben wollte.",
      "Deshalb sind seine Ausführungen gegen Exner von durch­schlagender Kraft, auch wenn Brentano den Übergang zur Anthroposophie nicht selbst machen will. Sie zeigen, wie",
      "Exner gar nicht von dem spricht, was eine sich selbst ver­stehende naturwissenschaftliche Vorstellungsart wirklich vermag, sondern wie er einen Windmühlenkampf führt ge­gen eine sich selbst mißverstehende Denkart. Man kann Brentanos Schrift lesen und überall durchfühlen, wie be­rechtigt alles ist, was durch seine Ideen in diese oder jene Richtung weist, ohne daß man findet, er spreche restlos aus, worauf er verweist.",
      "Mit Franz Brentano ist eine Persönlichkeit hinweggegan­gen, welche in ihrem Werke zu erleben einen unermeßlichen Gewinn bedeutet. Dieser Gewinn ist völlig unabhängig von dem Grade der verstandesgemäßen Übereinstimmung, die man diesem Werke entgegenbringen kann. Denn er ent­springt aus den Offenbarungen einer Menschenseele, die viel tiefer in der Welt-Wirklichkeit ihren Ursprung haben, als die Sphäre ist, in welcher im gewöhnlichen Leben sich Verstandes-Übereinstimmungen finden. Und Brentano ist eine Persönlichkeit, bestimmt fortzuwirken im geistigen Entwickelungsgang der Menschheit, durch Impulse, die sich nicht in der Fortführung der von ihm entwickelten Ideen erschöpfen. Ich kann mir gut vorstellen, wie jemand durchaus nicht mit dem einverstanden ist, was ich über Brentanos Verhältnis zur Anthroposophie hier ausgeführt habe; daß man aber, auf welchem wissenschaftlichen Standpunkte man auch stehe, zu weniger verehrenden Empfindungen dem Werte von Brentanos Persönlichkeit gegenüber kommen kann als die sind, welche den Absichten meiner Ausführungen zugrunde liegen, scheint mir unmöglich, wenn man den philosophischen Geist auf sich wirken läßt, der durch die Schriften dieses Mannes weht."
    ],
    "sentences": [
      [
        "III FRANZ BRENTANO"
      ],
      [
        "Ein Nachruf"
      ],
      [
        "Über das Verhältnis von Anthropologie und Anthroposophie in genügender Form zu sprechen ist aus den im vorigen Abschnitt dieser Schrift angeführten Gründen in Anknüp­fung an Max Dessoirs Buch «Vom Jenseits der Seele» nicht möglich.",
        "Ich glaube nun aber, daß dieses Verhältnis an­schaulich werden kann, wenn ich an diese Stelle die Ausfüh­rungen setze, die ich in andrer Absicht niedergeschrieben habe, nämlich als Nachruf für den im März 1917 in Zürich verstorbenen Philosophen Franz Brentano.",
        "Der Hingang des von mir aufs höchste verehrten Mannes hat bei mir be­wirkt, daß dessen bedeutungsvolles Lebenswerk erneut mir vor die Seele getreten ist; er hat mich bestimmt, das Fol­gende auszusprechen."
      ],
      [
        "Es scheint mir, daß ich den Versuch machen darf, vom an­throposophischen Gesichtspunkte aus zu einer Ansicht über Franz Brentanos philosophisches Lebenswerk zu gelangen in diesem Augenblick, da der Tod der verehrten Persönlich­keit die Fortsetzung dieses Werkes unterbrochen hat.",
        "Ich glaube, daß der anthroposophische Gesichtspunkt mich nicht in eine einseitige Schätzung der Brentanoschen Weltanschauung verfallen lassen kann.",
        "Dies nehme ich aus zwei"
      ],
      [
        "Gründen an.",
        "Erstens kann die Vorstellungsart Brentanos von niemand beschuldigt werden, daß sie selbst auch nur die geringste Hinneigung zu einer anthroposophischen Richtung habe.",
        "Ihr Träger hätte diese, wenn er selbst zu einem Urteile über sie Veranlassung gehabt hätte, wohl mit aller Entschiedenheit abgelehnt.",
        "Zweitens bin ich, von mei­nem anthroposophischen Gesichtspunkte aus, in der Lage, der Philosophie Franz Brentanos rückhaltlose Verehrung entgegenzubringen."
      ],
      [
        "Was das erste betrifft, so glaube ich nicht zu irren, wenn ich sage, Brentano hätte, wenn er über die von mir gemeinte Anthroposophie zu einem Urteil gekommen wäre, dies so gestaltet, wie dasjenige, das er sich über Plotins Philosophie gebildet hat.",
        "Wie dieser gegenüber würde er wohl auch von der Anthroposophie gesagt haben: «Mystisches Dunkel und ein freies Schweifen der Phantasie in unbekannten Re­gionen.»* Wie dem Neuplatonismus würde er auch gegen­über der Anthroposophie zur Vorsicht gemahnt haben, «damit man nicht, von eitlem Scheine verlockt, in den laby­rinthischen Gängen einer Pseudophilosophie sich verlie­re».** Ja, er hätte vielleicht die Denkweise der Anthropo­sophie für zu dilettantisch befunden, um sie auch nur für würdig zu halten, sie den Philosophien beizuzählen, über die er so urteilte wie über die Fichte-Schelling-Hegelsche.",
        "In seiner Wiener Antrittsrede sagt er über diese : «Vielleicht ist auch die jüngstvergangene Zeit eine...",
        "Epoche des Verfalles gewesen, in der alle Begriffe trüb ineinander schwammen, und von sachentsprechender Methode nicht eine Spur mehr"
      ],
      [
        "* Vergleiche Brentanos Schrift: «Was für ein Philosoph manchrnal Epoche macht» (Wien, Pest, Leipzig, Hartlebens Verlag, 1876), Seite 14."
      ],
      [
        "** Vergleiche Seite 23 der ehen angeführten Schrift Brentanos."
      ],
      [
        "zu finden war.»* Ich glaube, daß Brentano so geurteilt hätte, wenn ich auch selbstverständlich nicht nur dieses Ur­teil für völlig grundlos, sondern auch jede Zusammenstel­lung der Anthroposophie mit den Philosophien, mit denen sie dieser Philosoph wahrscheinlich zusammengestellt hätte, für unberechtigt halte."
      ],
      [
        "Was nun den zweiten der oben angegebenen Gründe, mich mit der Brentanoschen Philosophie auseinanderzu­setzen, betrifft, so darf ich bekennen, daß sie für mich zu den anziehendsten Leistungen der Seelenforschung in der Gegenwart gehört.",
        "Ich konnte zwar nur wenige der Wie­ner Vorlesungen Brentanos vor etwa sechsunddreißig Jah­ren hören; aber von diesem Zeitraum an habe ich seine schriftstellerische Tätigkeit mit wärmstem Anteile ver­folgt.",
        "Leider erschienen seine Veröffentlichungen, gemes­sen an meinem Wunsche, von ihm zu vernehmen, in viel zu großen Zeitabständen.",
        "Und sie sind zumeist so gehal­ten, daß man durch sie nur wie durch kleine Öffnungen in einen Raum mit einer Fülle von Schätzen, so durch gelegentliche Veröffentlichungen auf ein weites Reich un­veröffentlichter Gedanken blickte, das der hervorragende Mann in sich trug.",
        "So in sich trug, daß es in fortwäh­render Ausgestaltung hohen Erkenntniszielen zustrebte.",
        "Als nach langer Pause 1911 Brentanos Buch über «Aristo­teles», seine glänzende Schrift «Aristoteles' Lehre vom Ursprung des menschlichen Geistes» und sein Wiederab­druck des wichtigsten Teiles seiner Psychologie mit den so scharfsinnigen «Nachträgen» erschienen waren, da war"
      ],
      [
        "* Vergleiche den Abdruck der 1874 heim Antritt seiner Wiener Profes­sur gehaltenen Antrittsrede : «Über die Gründe der Entmutigung auf philosophischem Gebiete» (Wien 1874), Seite 18."
      ],
      [
        "das Lesen dieser Schriften für mich eine Reihe von Festes­freuden.*"
      ],
      [
        "Ich fühle mich Franz Brentano gegenüber von einer sol­chen Gesinnung durchdrungen, von der ich glaube sagen zu dürfen, daß man sie erwirbt, wenn die vom anthroposo­phischen Gesichtspunkte aus gewonnene wissenschaftliche Überzeugung - eben die Gesinnung ergreift.",
        "Ich bestrebe mich, seine Anschauungen in ihrem Werte zu durch­schauen, wenn ich mich auch keiner Täuschung darüber hingebe, daß er in dem oben angedeuteten Sinne über Anthroposophie hätte denken können, ja wohl, müssen.",
        "Dies bringe ich hier wahrlich nicht vor, um in alberner Art über meine Gesinnung gegenüber gegnerischen oder abwei­chenden Anschauungen in eine eitle Selbstkritik zu ver­fallen, sondern weil ich weiß, wie viel Mißverständnisse meiner Urteile über andere Geistesrichtungen es mir ge­bracht hat, daß ich mich in meinen Veröffentlichungen oft so ausgesprochen habe, wie es eine Folge dieser Ge­sinnung ist."
      ],
      [
        "Die ganze Brentanosche Seelenforschung methodisch durchdringend erscheinen mir die Grundgedanken, welche ihn 1868 zur Aufstellung seines Leitsatzes führten.",
        "Als er damals in Würzburg seine philosophische Professur antrat, rückte er seine Vorstellungsart in das Licht der These : es könne die wahre philosophische Forschungsart keine an­dere sein als die in dem naturwissenschaftlichen Erkennen berechtigte.",
        "«Vera philosophiae methodus nulla alia nisi"
      ],
      [
        "* Vergleiche Brentano : «Aristoteles und seine Weltanschauung » (1911, Verlag von Quelle und Meyer in Leipzig); Brentano : «Aristoteles' Lehre vom Ursprung des menschlichen Geistes» (Leipzig, Verlag von Veit und Comp., 1911); Brentano: «Von der Klassifiltation der psychischen Phäno­mene» (Leipzig, Verlag von Duneker und Humblot, 1911)."
      ],
      [
        "scientiae naturalis est.»* Als er dann den ersten Band seiner « Psychologie vom empirischen Standpunkte » 1874 erschei­nen ließ - in der Zeit, als er seine Wiener Professur antrat -, suchte er die Seelenerscheinungen in Gemäßheit des ange­führten Leitsatzes wissenschaftlich darzulegen.** Für mich bildet, was Brentano mit diesem Buche gewollt hat, und was von diesem Wollen während seiner Lebenszeit durch seine Veröffentlichungen zutage getreten ist, ein bedeutsames wissenschaftliches Problem.",
        "Brentano hatte - das geht aus seinem Buche hervor- seine Psychologie auf eine Reihe von Büchern berechnet.",
        "Das zweite hatte er versprochen, kurze Zeit nach dem ersten erscheinen zu lassen.",
        "Es ist keine Fort­setzung des nur die Anfangsvorstellungen seiner Psycholo­gie enthaltenden ersten Teiles erschienen.",
        "Als er 1889 seinen in der Wiener Juristischen Gesellschaft gehaltenen Vortrag «Vom Ursprung sittlicher Erkenntnis» abdrucken ließ, schrieb er in der Vorrede : «Man würde irren, wenn man um des zufälligen Anstoßes willen den Vortrag für ein flüchti­ges Werk der Gelegenheit hielte.",
        "Er bietet Früchte von jah­relangem Nachdenken.",
        "Unter allem, was ich bisher veröf­fentlicht, sind seine Erörterungen wohl das gereifteste Er­zeugnis. - Sie gehören zum Gedankenkreise einer , den ich, wie ich nunmehr zu hoffen wage, in nicht ferner Zeit seinem ganzen Umfange nach der Öffentlichkeit erschließen kann.",
        "Man wird dann an weiten"
      ],
      [
        "* Später sprach er sich über die Aufstellung dieser These aus in dem Vortrage, den er 1892 in der Wiener Philosophischen Gesellschaft gehalten hat und der abgedruckt ist als Schrift : «Über die Zukunft der Philosophie» (Wien, Alfred Hölder, 1893).",
        "Da findet man Seite 3 den hier gemeinten spä­teren Hinweis Brentanos auf seine These."
      ],
      [
        "** Vergleiche Brentano : «Psychologie vom empirischen Standpunkte», 1.",
        "Band (Leipzig, Verlag von Duneker und Humblot, 1874)"
      ],
      [
        "Abständen von allem Hergebrachten, und insbesondere auch an wesentlichen Fortbildungen eigener, in der vertretener An­schauungen genugsam erkennen, daß ich in meiner langen literarischen Zurückgezogenheit nicht eben müßig gewesen bin.»* Auch diese «Deskriptive Psychologie» ist nicht er­schienen.",
        "Die Verehrer der Brentanoschen Philosophie kön­nen ermessen, welchen Gewinn sie ihnen gebracht hätte, wenn sie die ein enges Gebiet umfassenden 1907 erschiene­nen «Untersuchungen zur Sinnespsychologie» studieren.**"
      ],
      [
        "Man muß sich die Frage stellen: was hat Brentano dazu gebracht, in der Fortsetzung seiner Veröffentlichungen im­mer wieder inne zu halten, ja, das als in kurzer Zeit fertig Geglaubte dann doch nicht zu veröffentlichen?",
        "Ich bekenne, daß ich mit innerlichster Erschütterung in dem Nachruf für Franz Brentano, den Alois Höfler im Mai 1917 hat erschei­nen lassen, die Worte las : «Wie er an seinem Hauptproblem, dem Gottesbeweis, so zuversichtlich weiterarbeitete, daß mir noch vor wenigen Jahren ein mit Brentano innig befreundeter, ausgezeichneter Wiener Arzt erzählte, Brentano habe ihm kürzlich versichert, nun habe er den Gottesbeweis binnen wenigen Wochen fertig ... »*** Ebenso empfand ich, als ich aus einem andern Nachruf (von Utitz)**** vernahm :"
      ],
      [
        "« Das Werk, das er am heißesten geliebt, an dem er sein gan­zes Leben lang geschaffen, ist unveröffentlicht geblieben.»"
      ],
      [
        "* Vergleiche Brentanos Schrift «Vom Ursprung sittlicher Erkenntnis» (Leipzig, Verlag Daneker und Humblot, 1889), Seite Vf."
      ],
      [
        "** Brentano : «Untersuchungen zur Sinnespsychologie» (Leipzig, Ver­lag Duncker und Humblot, 1907)."
      ],
      [
        "*** Süddeutsche Monatshefte, Mai 1917, in dem Aufsatz : «Franz Bren­tano in Wien», Seite 319 ff."
      ],
      [
        "**** Erschienen in der Vossischen Zeitung."
      ],
      [
        "Mir scheint, daß Brentanos Schicksale mit seinen geplan­ten Veröffentlichungen ein schwerwiegendes geisteswissen­schaftliches Problem darstellen.",
        "Nähern wird man sich die­sem wohl nur, wenn man dasjenige in seiner Eigenart be­trachten will, was er der Welt hat mitteilen können."
      ],
      [
        "Ich halte für wichtig, ins Auge zu fassen, daß Brentano in seiner psychologischen Forschung in scharfsinniger Weise eine reine Vorstellung des wirklich Seelischen zugrunde le­gen will.",
        "Er fragt sich : was ist Charakteristisches in allen Vorkommnissen, die man als seelische ansprechen muß.",
        "Und er fand, was er in den Nachträgen zur Psychologie 1911 so ausdrückte : «Das Charakteristische für jede psychische Tätigkeit besteht, wie ich gezeigt zu haben glaube, in der Beziehung zu etwas als Objekt.»* Vorstellen ist eine psychi­sche Tätigkeit.",
        "Das Charakteristische ist, daß ich nicht nur vorstelle, sondern daß ich etwas vorstelle, daß meine Vor­stellung sich auf etwas bezieht.",
        "Mit einem der mittelalterli­chen Philosophie entlehnten Ausdruck bezeichnet Brentano diese Eigenheit der seelischen Erscheinungen als «intentio­nale Beziehung».",
        "«Der gemeinsame Charakterzug» - so führt er an einem andern One aus - «alles Psychischen be­steht in dem, was man häufig mit einem leider sehr mißver­ständlichen Ausdruck Bewußtsein genannt hat, das heißt in einem subjektischen Verhalten, in einer, wie man sie bezeich­nete, intentionalen Beziehung zu etwas, was vielleicht nicht wirklich, aber doch innerlich gegenständlich gegeben ist.",
        "Kein Hören ohne Gehörtes, kein Glauben ohne Geglaub­tes, kein Hoffen ohne Gehofftes, kein Streben ohne Erstreb­tes, keine Freude ohne etwas, worüber man sich freut, und"
      ],
      [
        "* Vergleiche Brentano : «Von der Klassifikation der psychischen Phäno­mene», Seite 122."
      ],
      [
        "so im übrigen.»* Dieses intentionale Innesein ist nun in der Tat etwas, was wie ein Leitmotiv so führt, daß man alles, dem man es beilegen kann, eben dadurch in seiner seelischen Eigenart erkennt."
      ],
      [
        "Den psychischen Erscheinungen stellt Brentano die phy­sischen gegenüber: Farben, Schall, Raum und viele andere.",
        "Er findet, daß sich diese von jenen eben dadurch unterschei­den, daß ihnen eine intentionale Beziehung nicht eigen ist.",
        "Und er beschränkt sich darauf, diese Beziehung den psychi­schen Erscheinungen zu-, den physischen abzusprechen.",
        "Nun wird aber gerade, wenn man Brentanos Ansicht über die intentionale Beziehung kennen lernt, die Vorstellung zu der Frage hingeführt : macht ein solcher Gesichtspunkt nicht notwendig, auch das Physische von ihm aus anzuse­hen?",
        "Wer nun in diesem Sinne wie Brentano das Psychische so, das Physische auf ein Gemeinsames hin prüft, der findet, daß jede Erscheinung dieses Gebietes durch etwas anderes ist.",
        "Löst sich ein Körper in einer Flüssigkeit auf, so tritt diese Erscheinung am gelösten Körper durch die Beziehung der lösenden Flüssigkeit zu ihm auf.",
        "Wenn Phosphor seine Farbe durch die Einwirkung der Sonne ändert, so weist dies in dieselbe Richtung.",
        "Alle Eigenschaften in der physischen Welt sind durch die Verhältnisse der Dinge zu einander.",
        "Es ist für physisches Sein richtig, wenn Moleschott sagt: «Al­les Sein ist ein Sein durch Eigenschaften.",
        "Aber es gibt keine Eigenschaft, die nicht durch ein Verhältnis besteht.»** Wie"
      ],
      [
        "* Vergleiche Brentano : «Vom Ursprung sittlicher Erkenntnis», Seite 14.",
        "Und über den Grundrug des Intentionellen «Psychologie vom empiri­schen Standpunkte», Seite 115 ff."
      ],
      [
        "** Besonders prägnant hat dieses dargestellt Richard Wallascheck in einem bedeutenden Aufsatz der Wiener Wochensehrift «Die Zeit», Nr.96 und 97 des Jahrganges 1896 (vom 1. und 8.",
        "August)."
      ],
      [
        "alles Psychische in sich etwas enthält, wodurch es auf ein außer ihm Befindliches weist, so ist umgekehrt ein Physi­sches so geartet, daß das, was es ist, es durch die Beziehung eines Äußeren auf es ist.",
        "Muß nicht jemand, der in so scharf­sinniger Weise wie Brentano die intentionale Beziehung alles Seelischen betont, die Aufmerksamkeit auch auf das Charakteristische der physischen Erscheinungen richten, das sich durch den gleichen Gedankenvorgang ergibt?",
        "Si­cher scheint zum mindesten, daß eine solche Betrachtung des Seelischen die Beziehung desselben zur physischen Welt nur finden kann, wenn sie dieses Charakteristische in Erwä­gung zieht.*"
      ],
      [
        "Brentano findet nun drei Arten von intentionalen Bezie­hungen im seelischen Leben.",
        "Die erste ist das Vorstellen von etwas; die zweite die Anerkennung oder Verwerfung, die sich im Urteilen aussprechen; die dritte die des Liebens oder Hassens, welche im Fühlen erlebt werden.",
        "Wenn ich sage: Gott ist gerecht, so stelle ich etwas vor; aber ich anerkenne oder verwerfe das Vorgestellte noch nicht; wenn ich aber sage: es gibt einen Gott, so anerkenne ich das Vorgestellte durch ein Urteil Sage ich: die Freude ist mir lieb, so urteile ich nicht bloß, sondern ich erlebe ein Gefühl.",
        "Brentano un­terscheidet aus solchen Voraussetzungen heraus drei Grundklassen der psychischen Erlebnisse: Vorstellen, Ur­teilen, Fühlen (oder die Erscheinungen des Liebens und Hassens).",
        "Diese drei Grundklassen setzt er an die Stelle der von anderen anerkannten Teilung der psychischen Erschei­nungen"
      ],
      [
        "* Man vergleiche damit den Schluß des 7.",
        "Kapitels der am Ende dieser Schtift gegebenen «Skizzenhaften Erweiterungen des Inhaltes...».",
        "Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano.»"
      ],
      [
        "in: Vorstellen, Fühlen und Wollen.* Während näm­lich Vorstellen und Urteilen viele in eine Klasse zusammenfassen, trennt Brentano die beiden.",
        "Er ist mit der Zusam­menfassung nicht einverstanden, weil er nicht wie andere in dem Urteil nur eine Verbindung von Vorstellungen sieht, sondern eben eineAnerkennung oder einVerwerfen des Vor-gestellten, was beim bloßen Vorstellen nicht vollzogen wird.",
        "Gefühl und Wille hinwiederum, welche andere trennen, fal­len für Brentano, ihrem seelischen Gehalte nach, in eins zu­sammen.",
        "Was seelisch erlebt wird, indem man sich zum Ver­richten einer Handlung hingezogen oder davon abgestoßen fühlt, ist dasselbe, was man erlebt, wenn man zur Freude sich hingezogen oder vom Schmerze abgestoßen fühlt."
      ],
      [
        "Es ist aus Brentanos Schriften ersichtlich, daß er einen großen Wert darauf legt, die von ihm vorgefundene Gliede­rung des seelischen Erlebens in Denken, Fühlen und Wol­len durch die andere ersetzt zu haben, in Vorstellen, Urtei­len und in Lieben und Hassen.",
        "Von dieser Gliederung aus sucht er sich einen Weg zu bahnen zum Verständnis dessen, was die Wahrheit auf der einen Seite, die sittliche Güte auf der anderen Seite ist.",
        "Die Wahrheit stützt sich ihm auf das richtige Urteilen; die sittliche Güte auf das richtige Lieben.",
        "Er findet: «Wir nennen etwas wahr, wenn die daraufbezüg­liche Anerkennung richtig ist.",
        "Wir nennen etwas gut, wenn die darauf bezügliche Liebe richtig ist.»**"
      ],
      [
        "Man kann in Brentanos Ausführungen finden, daß er mit der richtigen Anerkennung im Urteile bei der Wahrheit, mit"
      ],
      [
        "* Vergleiche Brentano : «Psychologie vom empirischen Standpunkte» Seite 233 ff., und seine Schrift : «Von der Klassifikation der psychischen Phä­nomene.»"
      ],
      [
        "** Vergleiche Brentano: «Vom Ursprung sittlicher Erkenntnis».",
        "Seite 17."
      ],
      [
        "dem richtigen Erleben der Liebe bei der sittlichen Güte einen seelischen Tatbestand scharf ins Auge faßt und um­schreibt.",
        "Allein man kann innerhalb seines Vorstellungs­bereiches nichts finden, was genügen würde, um von dem seelischen Erlebnis des Vorstellens zu dem des Urteilens den Übergang zu finden.",
        "Wo man auch hinblickt in diesem Vorstellensbereich: man sucht vergebens nach der Beant­wortung der Frage: was liegt denn vor, wenn sich die Seele bewußt ist, sie stelle nicht bloß vor, sondern sie finde sich veranlaßt, den Gegenstand des Vorstellens durch ein Urteil anzuerkennen? - Ebenso wenig kann man eine Frage ver­meiden bei dem richtigen Lieben für die sittliche Güte.",
        "Innerhalb desjenigen Bereiches, welchen Brentano als « Seelisches » umschreibt, ist für das sittliche Verhalten aller­dings kein anderer Tatbestand vorhanden als das richtige Lieben.",
        "Aber ist denn einer sittlichen Handlung nicht auch eine Beziehung zu der äußeren Welt eigen?",
        "Kann dieses, was eine solche Handlung für die Welt charakterisiert, erschöpft werden dadurch, daß man sagt : sie ist eine Handlung, die richtig geliebt wird? *"
      ],
      [
        "Man hat beim Verfolgen Brentanoscher Gedankengänge zumeist das Gefühl : sie seien immer fruchtbringend, weil sie ein Problem nach einer Richtung hin scharfsinnig und mit wissenschaftlicher Besonnenheit in Angriff nehmen; aber man empfindet auch, Brentano führt mit solchen Gedan­kengängen nicht zu dem Ziel, das seine Ausgangspunkte ver­sprechen.",
        "Solch eine Empfindung kann sich auch aufdrän­gen, wenn man seine Dreiteilung des Seelenlebens in Vorstellen,"
      ],
      [
        "* Man vergleiche hiermit das 5.",
        "Kapitel in den am Ende dieser Schrift ge­gebenen «Skizzenhaften Erweiterungen des Inhaltes...»: «5.",
        "Über die wirk­liche Grundlage der intentionalen Beziehung.»"
      ],
      [
        "Urteilen, Lieben und Hassen vergleicht mit der an­dern in Vorstellen, Fühlen und Wollen.",
        "Man folgt mit einer gewissen Zustimmung dem, was er für seine Meinung bei­zubringen weiß; und man kann zuletzt doch wohl kaum die Überzeugung gewinnen, daß er alle Gründe hinreichend würdigt, die für die andere sprechen."
      ],
      [
        "Man nehme nur als besonderes Beispiel die Folgerung, die Brentano aus seiner Gliederung für die Kennzeichnung des Wahren, Schönen und Guten zieht.",
        "Wer das Seelenleben nach erkennendem Vorstellen, Fühlen und Wollen gliedert, wird kaum anders können, als das Streben nach Wahrheit mit dem Vorstellen, das Erleben der Schönheit mit dem Fühlen, das Vollbringen des Guten mit dem Wollen in einen näheren Zusammen­hang zu bringen."
      ],
      [
        "Im Lichte der Brentanoschen Gedanken erscheint die Sache anders.",
        "Da haben die Vorstellungen als solche keine Beziehung zu einander, durch die sich als sol­che schon die Wahrheit offenbaren könnte.",
        "Strebt die Seele nach einem Vollkommenen in der Beziehung von Vorstel­lungen, so kann daher ihr Ideal dabei nicht die Wahrheit sein; es ist vielmehr die Schönheit."
      ],
      [
        "Die Wahrheit liegt nicht auf dem Wege des bloßen Vorstellens, sondern des Urtei­lens.",
        "Und das sittlich Gute findet sich nicht als ein dem Wol­len Wesentliches, sondern ist Inhalt eines Fühlens; denn richtig zu lieben, ist Gefühls-Erlebnis.* - Nun kann aber die Wahrheit für das gewöhnliche Bewußtsein doch nur im vorstellenden Erkennen gesucht werden."
      ],
      [
        "Denn, wenn auch das Urteil, das zur Wahrheit führt, nicht in einer bloßen"
      ],
      [
        "* Vergleiche Brentano : «Psychologie vom empirischen Standpunkte», Seite 340 ff., und seine Schrift : «Von der Klassifikation der psychischen Phä­nomene», Seite 110 ff., sowie auch das von ihm in seiner Schrift «Vom Ur­sprung sittlicher Erkenntnis», Seite 17 ff., Gesagte."
      ],
      [
        "Verbindung von Vorstellungen sich erschöpft, sondern auf einer Anerkennung oder Verwerfung von Vorstellungen beruht, so kann diese Anerkennung oder Verwerfung von diesem Bewußtsein nur in Vorstellungen erlebt werden. - Und wenn auch die Vorstellungen, durch die ein Schönes dem Bewußtsein sich darstellt, in gewissen innerhalb des Vorstellungslebens gelegenen Verhältnissen sich offenba­ren: erlebt wird die Schönheit doch durch das Gefühl. - Und obgleich ein sittlich Gutes in der Seele ein richtiges Lieben hervorrufen soll : sein Wesentliches ist doch die Verwirkli­chung des richtig Geliebten durch das Wollen."
      ],
      [
        "Man erkennt erst, was in Brentanos Gedanken über die Dreigliederung des Seelenlebens vorliegt, wenn man durch­schaut, daß er von etwas ganz anderem spricht als diejeni­gen, welche diese Gliederung nach Vorstellen, Fühlen und Wollen vollziehen.",
        "Diese wollen einfach die Erfahrung des gewöhnlichen Bewußtseins beschreiben.",
        "Und dieses erfährt von sich selbst in den von einander unterschiedenen Ver­richtungen des Vorstellens, Fühlens und Wollens.",
        "Was wird da eigentlich erfahren?",
        "In meinem Buche «Vom Menschenrätsel» habe ich versucht, diese Frage zu beantworten.",
        "Die dort vorgebrachten Ergebnisse habe ich in der folgenden Art zusammengefaßt.",
        "«Zunächst ist das seelische Erleben des Menschen, wie es sich im Denken, Fühlen und Wollen offenbart, an die leiblichen Werkzeuge gebunden.",
        "Und es gestaltet sich so, wie es durch diese Werkzeuge bedingt ist.",
        "Wer aber meint, er sehe das wirkliche Seelenleben, wenn er die Äußerungen der Seele durch den Leib beobachtet, der ist in demselben Fehler befangen, wie einer, der glaubt, seine Gestalt werde von dem Spiegel hervorgebracht, vor dem er steht, weil der Spiegel die notwendigen Bedingungen ent­halte,"
      ],
      [
        "durch die sein Bild erscheint.",
        "Dieses Bild ist sogar in gewissen Grenzen als Bild von der Form des Spiegels usw. abhängig: was es aber darstellt, das hat mit dem Spiegel nichts zu tun.",
        "Das menschliche Seelenleben muß, um innerhalb der Sinneswelt sein Wesen voll zu erfüllen, ein Bild seines We­sens haben.",
        "Dieses Bild muß es im Bewußtsein haben; sonst würde es zwar ein Dasein haben; aber von diesem Dasein keine Vorstellung, kein Wissen.",
        "Dieses Bild, das im ge­wöhnlichen Bewußtsein der Seele lebt, ist nun völlig be­dingt durch die leiblichen Werkzeuge.",
        "Ohne diese würde es nicht da sein, wie das Spiegelbild nicht ohne den Spiegel.",
        "Was aber durch dieses Bild erscheint, das Seelische selbst, ist sei­nem Wesen nach von den Leibeswerkzeugen nicht abhän­giger als der vor dem Spiegel stehende Beschauer von dem Spiegel.",
        "Nicht die Seele ist von den Leibeswerkzeugen abhängig, sondern allein das gewöhnliche Bewußtsein der See­le.»* - Schildert man diesen von der Leibesorganisation ab­hängigen Bewußtseinsbereich, so gliedert man richtig nach Vorstellen, Fühlen und Wollen.** Aber Brentano schildert etwas anderes.",
        "Man fasse zunächst ins Auge, daß er unter dem «Urteilen» ein Anerkennen oder Abweisen eines Vor­stellungsinhaltes versteht.",
        "Das Urteilen betätigt sich inner­halb des Vorstellungslebens; aber es nimmt die Vorstellungen,"
      ],
      [
        "* Vergleiche hierzu mein Buch «Vom Menschenrätsel», 4.",
        "Auflage, Seite 156.",
        "Ich möchte die für viele gewiß überflüssige Bemerkung hier anfügen, daß ich - aus der Wesenheit der Sache heraus - bei meinem Verglei­che des Bewußtseins mit einem Spiegelbilde nicht im Auge habe, was man gewöhnlich tut, die Vorstellungswelt ein Spiegelbild der Außenwelt zu nennen, sondeen daß ich, was die Seele im gewöhnlichen Bewußtsein er­lebt, als ein Spiegelbild des wahrhaft Seelischen bezeichne."
      ],
      [
        "** Man vergleiche damit das 6.",
        "Kapitel der am Ende dieser Schrift gege­benen «Skizzenhaften Erweiterungen des Inhaltes...» : «6.",
        "Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit.»"
      ],
      [
        "die in der Seele auftreten, nicht einfach hin, sondern es setzt sie durch Anerkennung oder Ablehnung in Beziehung zu einer Wirklichkeit.",
        "Sieht man genauer zu, so kann diese Beziehung der Vorstellungen auf eine Wirklichkeit nur in einer Tätigkeit der Seele gefunden werden, welche in dieser selbst sich vollzieht."
      ],
      [
        "Dem entspricht aber niemals restlos, was die Seele bewirkt, wenn sie eine Vorstellung umteilend auf eine Sinneswahmehmung bezieht.",
        "Denn da ist es der Zwang des äußeren Eindruckes, der nicht rein innerlich er­lebt, sondern nur nacherlebt wird, und so als vorgestelltes Nach-Erlebnis zur Anerkennung oder zum Verwerfen führt."
      ],
      [
        "Dagegen entspricht, was Brentano beschreibt, in die­ser Beziehung vollkommen demjenigen Erkennen, das im ersten Abschnitt dieser Schrift das imaginative genannt wird.",
        "In diesem wird das Vorstellen des gewöhnlichen Be­wußtseins nicht einfach hingenommen, sondern in innerem Seelen-Erleben weiter gebildet, so daß aus ihm sich die Kraft auslöst, das seelisch Erfahrene auf eine geistige Wirk­lichkeit so zu beziehen, daß diese anerkannt oder verworfen wird."
      ],
      [
        "Brentanos Urteilsbegriff wird also nicht im gewöhnli­chen Bewußtsein vollkommen verwirklicht, sondern in der Seele, die in imaginativem Erkenntnis sich betätigt. - Des weiteren ist klar, daß durch Brentanos vollständige Ablö­sung des Vorstellungs- von dem Urteilsbegriff, von ihm das Vorstellen als bloßes Bild gefaßt wird.",
        "So aber lebt das ge­wöhnliche Vorstellen in der imaginativen Erkenntnis."
      ],
      [
        "Auch diese zweite Eigenschaft, welche die Anthroposophie dem imaginativen Erkennen beilegt, findet sich also in Brenta­nos Charakteristik der psychischen Erscheinungen. - Fer­ner: Brentano spricht die Erlebnisse des Fühlens als Erscheinungen der Liebe und des Hasses an.",
        "Wer zum imagi­nativen"
      ],
      [
        "Erkennen aufsteigt, der muß in der Tat diejenige Art des seelischen Erlebens, die für das gewöhnliche Bewußtsein als Lieben und Hassen - im Brentanoschen Sinn -sich offenbart, für das übersinnliche Schauen so umwan­deln, daß er sich gewissen Eigenarten der geistigen Wirk­lichkeit gegenübersetzen kann, welche in meiner «Theoso­phie» zum Beispiel in der folgenden Art geschildert wer­den : «Es gehört zu dem ersten, was man sich für die Orien­tierung in der seelischen Welt aneignen muß, daß man die verschiedenen Arten ihrer Gebilde in ähnlicher Weise un­terscheidet, wie man in der physischen Welt feste, flüssige und luft- oder gasförmige Körper unterscheidet.",
        "Um dazu zu kommen, muß man die beiden Grundkräfte kennen, die hier vor allem wichtig sind.",
        "Man kann sie Sympathie und An­tipathie nennen.",
        "Wie diese Grundkräfte in einem seelischen Gebilde wirken, danach bestimmt sich dessen Art.»* Wäh­rend Lieben und Hassen für das Leben der Seele in der Sin­neswelt etwas Subjektives bleibt, erlebt das imaginative Er­kennen das objektive Verhalten in der Seelenwelt mit durch innere Erfahrungen, die dem Lieben und Hassen gleich­kommen.",
        "Brentano beschreibt auch da, indem er von Seelenerscheinungen spricht, eine Eigenheit des imaginativen Erkennens (durch die dasselbe aber schon in den Bereich einer noch höheren Erkenntnisart** hineinreicht).",
        "Und daß"
      ],
      [
        "* Vergleiche meine «Theosophie», 28.",
        "Auflage, Seite 96."
      ],
      [
        "** Die erste Form des «schauenden Erkennens», die imaginative, geht uber in die zweite, die in meinen Schriften die inspirierte genannt wird.",
        "Wie eigentlich in der Brentanoschen Definition des Liebens und Hassens schon die in die Inspiration übergegangene Imagination lebt, das findet man dar­gestellt in den Schlußausfiihrungen des 6.",
        "Kapitels der am Ende dieser Schrift gegebenen «Skizzenhaften Erweiterungen des Inhaltes...» : «6.",
        "Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit.»"
      ],
      [
        "er von der objektiven Art des Liebens und Hassens im Gegen­satz zur subjektiven Gefühlsweise des gewöhnlichen Be­wußtseins eine Vorstellung hat, das ersieht man daraus, daß er die sittliche Güte als ein richtiges Lieben darstellt. - Zu­letzt muß ganz besonders in Betracht gezogen werden, daß für Brentano das Wollen aus dem Kreise der Seelenerschei­nungen herausfällt.",
        "Nun gehört das aus dem gewöhnlichen Bewußtsein erfließende Wollen ganz der physischen Welt an.",
        "Es verwirklicht sich in der Gestalt, wie es von diesem Bewußtsein gedacht werden kann, restlos in der physischen Welt, obwohl es ein in der physischen Welt sich offenbaren des rein geistig-Wesenhaftes an sich ist.",
        "Schildert man das in der physischen Welt vorhandene gewöhnliche Bewußtsein, so kann in dieser Schilderung das Wollen nicht fehlen.",
        "Schildert man das schauende Bewußtsein, so kann in diese Schilderung nichts von den Vorstellungen über das ge­wöhnliche Wollen übergehen.",
        "Denn in der seelischen Welt, auf welche das imaginative Bewußtsein sich bezieht, erfolgt das Geschehen auf einen seelischen Impuls hin anders als durch Akte des Wollens, wie solche der physischen Welt ei­gen sind.",
        "Indem also Brentano die seelischen Erscheinun­gen in dem Gebiete ins Auge faßt, in dem die imaginative Er­kenntnis sich betätigt, muß ihm der Begriff des Wollens sich verflüchtigen."
      ],
      [
        "Es scheint wirklich einleuchtend zu sein, daß Brentano dazu getrieben worden ist, indem er das Wesen der psychi­schen Erscheinungen beschrieben hat, eigentlich das Wesen der schauenden Erkenntnis zu schildern.",
        "Selbst aus Einzel­heiten seiner Darstellung geht dies klar hervor.",
        "Man nehme ein Beispiel für viele, die angeführt werden könnten.",
        "Er sagt : «Der gemeinsame Charakterzug alles Psychischen be­steht"
      ],
      [
        "in dem, was man häufig mit einem leider sehr mißver­ständlichen Ausdruck Bewußtsein genannt hat ... ».* Aber wenn man nur diejenigen Seelenerscheinungen schildert, welche als dem gewöhnlichen Bewußtsein angehörig von der Leibesorganisation bedingt sind, so ist der Ausdruck gar nicht mißverständlich.",
        "Brentano hat eine Empfindung davon, daß die wirkliche Seele aber in diesem gewöhnlichen Bewußtsein nicht lebt, und er fühlt sich veranlaßt, von dem Wesen dieser wirklichen Seele in Vorstellungen zu sprechen, die allerdings mißverstanden werden müssen, wenn man auf sie den gewöhnlichen Bewußtseinsbegriff anwenden will."
      ],
      [
        "Brentano geht in seiner Forschung so vor, daß er die Er­scheinungen des anthropologischen Gebietes bis dahin ver­folgt, wo sie den Unbefangenen dazu zwingen, Vorstellun­gen über die Seele zu bilden, welche zusammentreffen mit dem, was die Anthroposophie auf ihren Wegen über die Seele findet.",
        "Und die Ergebnisse der beiden Wege zeigen sich gerade durch Brentanos Psychologie im vollsten Ein­klange.",
        "Brentano selbst wollte aber den anthropologischen Weg nicht verlassen.",
        "Daran hinderte ihn seine Auslegung des von ihm aufgestellten Leitsatzes: «Es kann die wahre Forschungsart der Philosophie keine andere sein als die in der naturwissenschaftlichen Erkenntnisart anerkannte.»** Eine andere Auffassung dieses Leitsatzes hätte ihn dazu füh­ren können, anzuerkennen, daß man gerade dann die natur­wissenschaftliche Vorstellungsart in dem rechten Lichte sieht, wenn man sich bewußt ist, daß diese für das geistige Gebiet sich ihrem eigenen Wesen gemäß wandeln muß.",
        "Brentano hat die wahren Seelenerschenningen, welche er"
      ],
      [
        "* Vergleiche Brentano : «Vom Ursprung sittlicher Erkenntnis», Seite 14."
      ],
      [
        "** Vergleiche oben Seite 81 f. dieser Schrift."
      ],
      [
        "als solche kennzeichnet, niemals zum Gegenstande eines ausgesprochenen Bewußtseins machen wollen.",
        "Hätte er die­ses getan, so wäre er von der Anthropologie zur Anthropo­sophie fortgeschritten.",
        "Er fürchtete diesen Weg, weil er ihn nur als ein Abirren in «mystisches Dunkel und ein freies Schweifen der Phantasie in unbekannte Regionen» anzuse­hen vermochte.* Er ließ sich auf eine Prüfung dessen gar nicht ein, was seine eigene psychologische Auffassung not­wendig machte.",
        "Jedesmal, wenn er vor der Notwendigkeit stand, seinen eigenen Weg fortzusetzen in das anthroposo­phische Gebiet hinein, blieb er stehen.",
        "Er wollte die Fragen, welche sich nur anthroposophisch beantworten lassen, an­thropologisch lösen.",
        "Diese Lösung mußte scheitern.",
        "Weil sie scheitern mußte, konnte er seine angefangenen Darstel­lungen nicht so fortsetzen, daß die Fortsetzung für ihn hätte befriedigend werden können.",
        "Hätte er die «Psychologie vom empirischen Standpunkt »fortgesetzt : sie hätte nach dem Er­gebnisse des ersten Bandes eine Anthroposophie werden müssen.",
        "Hätte er seine «Deskriptive Psychologie»wirklich geliefert : Anthroposophie müßte aus ihr überall herausleuchten.",
        "Hätte er entsprechend seinem Ausgangspunkte die Ethik seiner Schrift «Vom Ursprung sittlicher Erkenntnis» weiter geführt: er hätte auf Anthroposophie stoßen müssen."
      ],
      [
        "Vor Brentanos Seele stand die Möglichkeit einer Psycho­logie, die nicht wie die rein anthropologische gestaltet sein kann.",
        "Die letztere kann an die Fragen gar nicht denken, welche als die bedeutungsvollsten über das Seelenleben auf­geworfen werden müssen.",
        "Die neuere Psychologie will nur anthropologisch sein, weil sie alles darüber Hinausgehende für unwissenschaftlich hält.",
        "Brentano aber sagt : «Für die"
      ],
      [
        "* Vergleiche oben Seite 79 dieser Schrift."
      ],
      [
        "Hoffnungen eines Platon und Aristoteles, über das Fortle­ben unseres besseren Teiles nach der Auflösung des Leibes Sicherheit zu gewinnen, würden dagegen die Gesetze der Assoziation von Vorstellungen, der Entwickelung von Überzeugungen und Meinungen und des Keimens und Trei­bens von Lust und Liebe alles andere, nur nicht ein wahre Entschädigung sein...",
        "Und wenn wirklich der Unterschied der beiden Anschauungen die Aufnahme oder den Ausschluß der Frage nach der Unsterblichkeit besagte, so wäre er für die Psychologie ein überaus bedeutender zu nennen, und ein Eingehen in die metaphysische Untersuchung über die Substanz als Trägerin der Zustände unvermeidlich.»* Anthroposophie zeigt, wie nicht durch metaphysische Spe­kulationen in das von Brentano bezeichnete Gebiet einge­treten werden kann, sondern allein durch Betätigung sol­cher Seelenkräfte, welche nicht in das gewöhnliche Bewußt­sein fallen können.",
        "Indem Brentano in seiner Philosophie das Wesen der Seele so schildert, daß in seiner Schilderung das Wesen der schauenden Erkenntnis deutlich zum Aus­drucke kommt, ist diese Philosophie eine vollkommene Rechtfertigung der Anthroposophie.",
        "Und man darf in Bren­tano sehen den philosophischen Forscher, der auf seinem Wege bis zur Pforte der Anthroposophie gelangt, diese Pforte aber nicht aufschließen will, weil das Bild von naturwissenschaftlicher Denkart, das er sich macht, ihm den Glauben erzeugt, er gelange durch dieses Aufschließen in den Abgrund der Unwissenschaft."
      ],
      [
        "* Vergleiche Brentano : «Psychologie vom empirischen Standpunkte», Seite 20."
      ],
      [
        "Die Schwierigkeiten, vor die sich Brentano oft gestellt sieht, wenn er seine Vorstellungen fortsetzen will, rühren davon her, daß er diese Vorstellungen über das Wesen des Seeli­schen auf dasjenige bezieht, was im gewöhnlichen Bewußt­sein vorliegt.",
        "Dazu wird er veranlaßt, weil er innerhalb der Auffassung stehen bleiben will, die ihm als die naturwissen­schaftlich berechtigte erscheint."
      ],
      [
        "Aber diese Auffassung kann durch ihre Erkenntuismittel eben nur zu dem gelan­gen, was von dem Seelischen als der Inhalt des gewöhnli­chen Bewußtseins vorliegt.",
        "Dieser Inhalt ist aber nicht die Wirklichkeit des Seelischen, sondern dessen Spiegelbild."
      ],
      [
        "Dies durchschaut Brentano nur von der einen Seite des be­greifenden Verstehens, aber nicht von der andern, der Be­obachtung.",
        "In seinen Begriffen entwirft er ein Bild seeli­scher Erscheinungen, die sich in der Wirklichkeit der Seele abspielen; wenn er beobachtet, glaubt er in dem Spiegelbild des Seelischen eine Wirklichkeit zu haben.* - Eine andere philosophische Richtung, der Brentano die schärfste Abnei­gung entgegengebracht hat, diejenige Eduard von Hartmanns, ist auch von einer naturwissenschaftlichen Vorstel­lungsart ausgegangen."
      ],
      [
        "Eduard von Hartmann hat den Spie­gelbild-Charakter des gewöhnlichen Bewußtseins durch­schaut.",
        "Er sieht daher in diesem Bewußtsein keine Wirklich­keit.",
        "Aber er lehnt es auch entschieden ab, die entsprechende Wirklichkeit überhaupt in ein menschliches Bewußtsein hereinzuholen."
      ],
      [
        "Er verweist diese Wirklichkeit in das Gebiet des Unbewußten.",
        "Über dieses zu reden, gestattet er nur der hypothetischen Anwendung der durch gewöhnliches Be­wußtsein"
      ],
      [
        "* Vergleiche hiertnit das 7.",
        "Kapitel der am Ende dieser Schrift gegehenen «Skizzenhaften Erweiterungen des Inhaltes...» : «7.",
        "Die Sonderung des See­lischen von dem Außer-Seelischen durch Franz Brentano.»"
      ],
      [
        "gebildeten Begriffe über dieses Gebiet hinaus.* Die Anthroposophie behauptet, daß über dieses Gebiet hin­aus geistige Beobachtung möglich ist.",
        "Und daß dieser gei­stigen Beobachtung auch Begriffe zugänglich seien, die so wenig bloß hypothetisch sein dürfen wie die im sinnlichen Felde gewonnenen. - Eduard von Hartmanns Übersinnli­ches soll kein unmittelbar Erkanntes, sondern ein aus dem unmittelbar Erkannten Erschlossenes sein.",
        "Hartmann ge­hört zu denjenigen Philosophen der neueren Zeit, die Be­griffe nicht bilden wollen, wenn sie zum Ausgangspunkte dieser Begriffsbildung nicht die Aussagen der sinnlichen Beobachtung und des Erlebens im gewöhnlichen Bewußt­sein haben.",
        "Brentano bildet solche Begriffe.",
        "Aber er täuscht sich über die Wirklichkeit, in der sie durch Beobachtung gebildet werden können.",
        "Sein Geist erweist sich als merk­würdig zwiespältig.",
        "Er möchte ganz Naturforscher in dem Sinne sein, wie sich die naturwissenschaftliche Vor­stellungsart in der neueren Zeit herausgebildet hat.",
        "Und er muß doch Begriffe bilden, welche sich vor dieser Vorstellungsart nur dann rechifertigen lassen, wenn man dieselbe nicht als die einzig geltende hinnimmt.",
        "Dieser Zwiespalt in Brentanos Forschergeist wird dem erklär­lich, der sich in die ersten Schriften Brentanos vertieft : in sein Buch : «Von der mannigfachen Bedeutung des Seien­den nach Aristoteles » (186z); in seine «Psychologie des Aristoteles» (1 867) und in seinen « Creatinismus des Aristo­teles»"
      ],
      [
        "* Die in bezug auf obiges zielenden Anschauungen Eduard von Hartmanns findet man in übersichtlicher Art dargestellt in dessen zwei Büchern: «Die moderne Psychologie» (Leipzig 1901, Hermann Haackes Verlag) und «Grundriß der Psychologie» (Band 3 von E.v.",
        "Hartmanns System der Philosophie im Grnndriß, Bad Sachsa im Harz 1908, Hermann Haacke, Verlagsbuchhandlung)."
      ],
      [
        "(1882).* - In diesen Schriften geht Brentano mit mu­stergiltiger Gelehrsamkeit den Gedankengängen des Aristoteles nach.",
        "Und in diesem Nachgehen eignet er sich ein Den­ken an, das sich nicht in den Begriffen erschöpfen lassen kann, die in der Anthropologie geltend sind."
      ],
      [
        "In diesen Schriften hat er einen Seelenbegriff im Bereiche seiner Auf­merksamkeit, welcher das Seelische aus dem Geistigen her­leitet.",
        "Dieses aus dem Geiste herstammende Seelische be­dient sich des aus physischen Vorgängen gebildeten Orga­nismus, um innerhalb des sinnlichen Daseins sich Vorstellun­gen zu bilden."
      ],
      [
        "Was in der Seele sich Vorstellungen bildet, ist geistiger Natur, ist der «Nus» des Aristoteles.",
        "Aber dieser «Nus» ist von zweifacher Wesenheit, als «Nus pathetikos» ist er rein leidend; er läßt sich von den durch den Organismus ihm gegebenen Eindrücken zu seinen Vorstellungen anre­gen."
      ],
      [
        "Damit aber diese Vorstellungen so in die Erscheinung treten, wie sie in der tätigen Seele sind, muß diese Tätigkeit als «Nus poietikos»wirken.",
        "Was der «Nus pathetikos » lie­fert, wären bloß Erscheinungen in einem finsteren Seelen-sein; sie werden beleuchtet durch den «Nus poietikos»."
      ],
      [
        "Brentano sagt darüber : Der Nus poietikos ist das Licht, wel­ches die Phantasmen erleuchtet und das Geistige im Sinnli­chen für unser Geistesauge sichtbar macht.** - Es kommt, wenn man Brentano verstehen will, nicht allein darauf an, in­wieweit er die aristotellschen Vorstellungen in seine eigene Überzeugung aufgenommen hat, sondern vor allem darauf, daß er sich mit dem eigenen Denken in diesen Vorstellungen"
      ],
      [
        "* Franz Brentano : «Von der mannigfachen Bedeutung des Seienden nach Aristoteles» (Freiburg im Breisgau, Herdersche Verlagshandlung); dessen «Die Psychologie des Aristoteles» (Mainz, Verlag von Franz Kirch­heim); dessen «Über den Creatinismus des Aristoteles » (Wien, Tempsky)."
      ],
      [
        "** Vergleiche Brentano : «Die Psychologie des Aristoteles», Seite 172 ff."
      ],
      [
        "hingebungsvoll bewegt hat.",
        "Dadurch aber betätigte sich die­ses Denken in einem Bereiche, in dem der Ausgangspunkt der Sinnesanschauung, und damit die anthropologische Grundlage für die Begriffsbildung nicht vorhanden sind."
      ],
      [
        "Und dieser Grundzug des Denkens ist in Brentanos For­schung geblieben.",
        "Er will zwar nur gelten lassen, was nach dem Muster der gegenwärtigen naturwissenschaftlichen Vorstellungsart anerkannt werden kann; aber er muß Ge­danken bilden, die nicht in dieses Bereich gehören."
      ],
      [
        "Nun läßt sich nach rein naturwissenschaftlicher Methode über die See­lenerscheinungen nur etwas sagen, insoferne diese das durch die Leibesorganisation bedingte Spiegelbild des wirklich Wesenhaften der Seele sind, das heißt, insoferne sie in ihrem Spiegelbild-Charakter mit der Leibesorganisation entstehen und vergehen.",
        "Was aber Brentano über die Wirklichkeit des Seelischen denken muß, ist ein Geistiges, von der Leibesor­ganisation Unabhängiges, das sogar durch den «Nus poieti­kos» sich das Geistige im Sinnlichen durch unser Geistes­auge sichtbar macht. - Daß Brentano sich mit seinem Den­ken in solchen Bereichen bewegen kann, verbietet ihm, das Seelensein durch die Leibes organisation entstehend und mit der Leibesorganisation vergehend zu denken."
      ],
      [
        "Weil er aber eine übersinnliche Beobachtung ablehnt, so kann ihm in diesem Seelensein kein Inhalt beobachtbar sein, der über das physische Sein hinausreicht.",
        "Sobald er der Seele einen In­halt zuschreiben soll, den diese ohne die Mithilfe der Leibes-organisation entfalten könnte, fühlt sich Brentano in einer Welt, für die er keine Vorstellungen findet."
      ],
      [
        "In solcher Gei­stesverfassung wendet er sich an Aristoteles und findet auch bei ihm Seelenvorstellungen, die für ein außerleibliches Da­sein keinen anderen Inhalt ergeben, als den im leiblichen"
      ],
      [
        "Dasein erworbenen.",
        "Charakteristisch in seiner Einseitig­keit ist, was in dieser Beziehung Brentano in seiner «Psychologie des Aristoteles» vorbringt : «Wie nun der Mensch, wenn ihm ein Fuß oder ein anderes Glied entrissen wird, keine vollendete Substanz mehr ist, so ist er natürlich noch viel weniger eine vollendete Substanz, wenn der ganze leib­liche Teil dem Tode anheimgefallen ist.",
        "Der geistige Teil besteht zwar noch fort, allein die irren gar sehr, die wie Plato glauben, daß die Trennung vom Leibe für ihn eine Förde­rung und gleichsam eine Befreiung aus drückendem Ge­fängnisse sei; muß ja doch die Seele nunmehr auf alle die zahlreichen Dienste verzichten, welche die Kräfte des Lei­bes ihr geleistet haben.»* - Über die Auffassung des Aristo­teles vom Wesen der Seele war Brentano in einen außeror­dentlich interessanten Streit mit dem Philosophen Eduard Zeller gekommen.",
        "Dieser behauptete, die Meinung des Aristoteles gehe dahin, eine Präexistenz der Seele vor ihrer Verbindung mit der Leibesorganisation anzunehmen, wäh­rend Brentano dem Aristoteles eine solche Ansicht ab­sprach, und ihn nur denken ließ, die Seele werde erst in die Leibesorganisation hinein geschaffen; sie habe also keine Präexistenz, wohl aber nach der Auflösung des Leibes eine Postexistenz.** Brentano meinte, eine Präexistenz nehme nur Plato, nicht aber Aristoteles an.",
        "Es ist nicht zu leugnen, daß die Gründe, welche Brentano für seine Meinung und"
      ],
      [
        "* Vergleiche Brentano: «Psychologie des Aristoteles», Seite 196."
      ],
      [
        "** Über den Inhalt des wissenschaftlichen Streites zwischen Brentano und Zeller vergleiche Brentano: «Offener Brief an Herrn Professor Dr.",
        "Eduard Zeller aus Anlaß meiner Schrift über die Lehre des Aristoteles von der Ewigkeit des Geistes» (Leipzig 1883, Duneker und Humblot) und des­sen : «Aristoteles' Lehre vom Ursprung des menschlichen Geistes» (Leip­zig 1911, Veit und Comp.)."
      ],
      [
        "gegen die Zellersche vorbringt, viel Gewicht haben.",
        "Abge­sehen von der Brentanoschen geistvollen Interpretation entsprechender aristotelischer Behauptungen bietet es ja eine Schwierigkeit, dem Aristoteles die Ansicht von der Präexistenz der Seele zuzuschreiben, weil eine solche einem Grundsatz der aristotelischen Metaphysik zu widerspre­chen scheint.",
        "Aristoteles sagt nämlich, daß niemals eine «Form» vor dem «Stoffe» existieren könne, der die Form trägt.",
        "Die Kugelgestalt existiere niemals ohne das sie erfül­lende Stoffliche.",
        "Da aber Aristoteles das Seelische als die «Form»der Leibesorganisation faßt, so scheint es, daß man ihm nicht zuschreiben dürfe : er habe gedacht, die Seele könne vor der Entstehung der Leibesorganisation existieren."
      ],
      [
        "Brentano hat sich nun mit seinem Seelenbegriff in der aristotelischen Vorstellung von der Unmöglichkeit einer Präexistenz so verfangen, daß er nicht bemerken kann, wie diese aristotelische Vorstellung selbst in einem wichtigen Punkte versagt.",
        "Kann man denn wirklich «Form» und «Materie» so denken, daß man nur annimmt : die Form könne nicht vor der sie erfüllenden Materie bestehen?",
        "Die Kugelgestalt sei doch nicht vorhanden vor der sie erfül­lenden Stoffmasse?",
        "So wie sie an der Stoffmasse erscheint, ist die Kugelform gewiß nicht vor der Zusammenballung des Stoffes vorhanden.",
        "Allein bevor dieser zusammenschießt, sind die Kräfte vorhanden, welche an diesen Stoff herankommen, und deren Ergebnis für ihn sich in seiner Kugelgestalt offenbart.",
        "Und in diesen Kräften lebt vor dem Auftreten der Kugelgestalt diese schon gewiß in andrer Art.* Hätte Brentano sich nicht durch seine Auslegung"
      ],
      [
        "* Die Täuschung über eine Berechtigung zu der oben gekennzeichneten Behauptung von Form und Materie kann nur im Hinblick auf die Bildung von Kristallen etwa entstehen, weil da die Form unmittelbar aus den der Materie innewohnenden Kräften hervorzugehen scheint.",
        "Doch wird ein unbefangenes Denken nicht anders können als die Formkräfte innerhalb des Materiellen vorauszusetzen, bevor die geformte Materie wirklich ent­steht.",
        "Völlig unhaltbar ist die aristotelische Vorstellung aber schon bei der Pflanze, deren formende Kräfte man gewiß nicht allein in den Verhältnissen im Keime suchen muß, sondern in Wirksamkeiten von der Außenwelt her, die unbegrenzt lange vor der Bildung der sinnlichen Pflanze vorhanden sind."
      ],
      [
        "der naturwissenschaftlichen Vorstellungsart für den Inhalt des Seelenbegriffs durch die Anschauungen über die körper­liche Organisation gebunden gefühlt, so hätte er vielleicht bemerkt, daß der aristotelische Seelenbegriff selbst mit einem inneren Widerspruch behaftet ist.",
        "So hat er denn an der Be­trachtung der Weltanschauung des Aristoteles nur die Mög­lichkeit gewonnen, über die Seele Vorstellungen zu denken, welche diese aus dem Gebiete der Leibesorganisation her­aus heben, ihr aber nicht einen solchen Inhalt zuweisen, der gestattet, daß man sie bei unbefangenem Denken wirklich von der Leibesorganisation unabhängig vorstellen kann."
      ],
      [
        "Neben Aristoteles ist für Brentano auch Leibniz ein Phi­losoph, dem er besondere Anerkennung zuwendet.",
        "Beson­ders die Art der Leibnizischen Seelenbetrachtung scheint ihn angezogen zu haben.",
        "Man kann nun sagen, daß Leib­niz auf diesem Gebiete eine Vorstellungsweise hat, welche wie eine wesentliche Erweiterung der Meinung des Ari­stoteles erscheint.",
        "Während dieser den wesenhaften Inhalt des menschlichen Denkens abhängig macht von der Sin­nesbeobachtung, löst Leibniz diesen Inhalt von der sinnli­chen Grundlage los.",
        "Dem Aristoteles folgend wird man den Satz anerkennen : es ist nichts im Denken, was nicht vorher in den Sinnen war (nihil est in intellectu, quod non fuerit in sensu); Leibniz aber ist der Meinung, daß nichts"
      ],
      [
        "im Denken sei, was nicht vorher in den Sinnen war, außer das Denken selbst (nihil est in intellectu, quod non fuerit in sensu, nisi ipse intellectus).",
        "Es wäre unrichtig, dem Aristo­teles die Ansicht zuzuschreiben, daß das im Denken sich betätigende Wesenhafte ein Ergebnis der leiblichen Wir­kenskräfte sei."
      ],
      [
        "Aber indem er den Nus pathetikos zum lei­denden Empfänger der Sinneseindrücke, den Nus poieti­kos zum Beleuchter dieser Eindrücke machte, blieb inner­halb seiner Philosophie nichts, das Inhalt eines von dem Sinnessein unabhängigen Seelenlebens werden könnte.",
        "In dieser Beziehung erweist sich der Leibnizische Satz frucht­barer."
      ],
      [
        "Durch ihn wird die Aufmerksamkeit besonders hin-gelenkt auf das von der Leibesorganisation unabhängige Seelenwesen.",
        "Allerdings wird diese Aufmerksamkeit ein­geschränkt auf den bloß intellektiven Teil dieses Wesens."
      ],
      [
        "Und insofern ist Leibnizens Satz einseitig.",
        "Dennoch ist er eine Richtlinie, die im gegenwärtigen naturwissenschaftlichen Zeitalter zu etwas führen kann, zu dem Leibniz zu ge­langen noch nicht möglich war."
      ],
      [
        "Dazu waren in seiner Epo­che die Vorstellungen über den rein naturgemäßen Ur­sprung von Eigenschaften der Leibesorganisation noch zu unvollkommen.",
        "Gegenwärtig ist dies anders.",
        "Man kann heute bis zu einem gewissen Grade naturwissenschaftlich erkennen, wie sich die organischen Leibeskräfte von den Vorfahren vererben, und wie innerhalb dieser vererbten Kräfte des Organismus die Seele wirkt."
      ],
      [
        "Was von vielen, die glauben, auf dem rechten «naturwissenschaftlichen Stand­punkte » zu stehen, allerdings nicht zugegeben wird, erweist sich doch beim richtigen Erfassen der naturwissenschaftli­chen Erkenntnisse als notwendige Ansicht : daß alles, wo­durch die Seele im physischen Leben wirkt, bedingt ist durch"
      ],
      [
        "die Leibeskräfte, die in der physischen Vererbung slinie von den Vorfahren auf die Nachkommen übergehen, außer dem Inhalt des Seelischen selbst.",
        "So etwa kann man gegenwärtig den Leibnizischen Satz erweitern.",
        "Dann aber ist er die an­thropologische Rechtfertigung der anthroposophischen Be­trachtungsart.",
        "Dann verweist er die Seele darauf, ihren we­senhaften Inhalt in einer geistigen Welt zu suchen, und zwar durch eine andere Erkenntnisart als die in der Anthropologie übliche.",
        "Denn dieser ist nur zugänglich, was im gewöhnli­chen Bewußtsein durch die Leibesorganisation erlebt wird.* Man kann der Ansicht sein, Brentano hätte alle Vorbedingungen gehabt, um, von Leibniz ausgehend, sich den Blick auf das im Geiste verankerte Wesenhafte der Seele zu eröffnen, und das sich diesem Blick Ergebende durch die naturwissenschaftlichen Erkenntnisse der neueren Zeit zu erkräftigen.",
        "Wer seinen Ausführungen folgt, sieht den Weg, der vor ihm gelegen war.",
        "Es hätte der Weg zu einem rein geistig erkennbaren Seelenwesen vor ihm offenbar"
      ],
      [
        "* Es gibt Denker, welche die Ansicht, daß des Menschen seelischer We­senskern nicht von den Vorfahren ererbt ist, sondern aus der geistigen Welt kommt, abstoßend finden, weil sie dadurch den Fortpflanzungsvorgang herabgewürdigt sehen.",
        "Zu diesen Denkern gehört der Philosoph J.",
        "Frobschamaner (man vergleiche dessen Schrift «Über den Ursprung der menschlichen Seelen», Seite 98 ff.).",
        "Dieser meint, es müsse angenommen werden, daß auch die Seelen der Kinder von den Eltern stammen, da «diese lebendigen Menschen nicht etwa bloße Leiber oder gar Tiere zeugen» (ver­gleiche Frohschammers Schrift über «Die Philosophie des Thomas von Aquino», Leipzig, Brockhaus 1889, Seite VIII).",
        "Von einem aus dieser Mei­nung kommenden Einwand kann die Anschauung, die in den Ausführun­gen der vorliegenden Schrift zur Darstellung kommt, nicht betroffen wer­den.",
        "Denn man braucht den Seelenkern, der, aus der geistigen Welt kom­mend, sich mit dem von den Vorfahren Vererbten verbindet, vor der Empfängnis nicht ohne Beziehung zu den Seelen der Eltern zu denken, wenn man ihn auch nicht durch den Fortpflanzungsakt entstehend denkt."
      ],
      [
        "werden können, wenn er ausgebildet hätte, was im Berei­che seiner Aufmerksamkeit lag, als er solche Sätze nieder­schrieb wie diesen: «Aber wie ist» das «Eingreifen der Gottheit» beim Erscheinen einer menschlichen Seele in ei­nem Leib «zu denken?",
        "Hat sie, nachdem sie den geistigen Teil des Menschen von Ewigkeit schöpferisch hervorge­bracht hatte, ihn nun mit einem Embryo in der Art ver­bunden, daß er, der bisher als besondere geistige Substanz für sich bestand, nun aufhörte, ein wirkliches Wesen für sich zu sein, und Teil einer menschlichen Natur wurde, oder hat sie ihn erst jetzt schöpferisch hervorgebracht? -Wenn Aristoteles das erste annahm, so mußte er glauben, daß derselbe Geist wieder und wieder mit anderen und an­deren Embryonen verbunden werde; denn das Menschengeschlecht erhält sich nach ihm fortzeugend ins Unendli­che, die Menge der von Ewigkeit bestehenden Geister kann aber nur eine endliche sein."
      ],
      [
        "Alle Ausleger sind nun darin einig, daß Aristoteles in der reiferen Zeit seines Phi­losophierens die Palingenese verworfen hat.",
        "Also ist diese Möglichkeit ausgeschiossen.»* Was nicht in der Gedan­kenfolge des Aristoteles liegt, die Rechtfertigung des gei­stigen Blickes auf die wiederholten Leben der Menschenseele durch Palingenese : für Brentano hätte es sich ergeben können aus der Verbindung der an Aristoteles verfeiner­ten Begriffe über die Seele mit den Erkennmissen der neue­ren Naturwissenschaft. - Er hätte diesen Weg um so mehr gehen können, als er empfänglichen Sinn hatte für die Er­kermtuislehre der mittelalterlichen Philosophie."
      ],
      [
        "Wer diese Erkenntnislehre wirklich erfaßt, der eignet sich eine Sum­me"
      ],
      [
        "* Vergleiche Brentano: «Aristoteles und seine Weltanschauung» (1911), Seite 134."
      ],
      [
        "von Ideen an, die geeignet sind, die neueren naturwis­senschaftlichen Ergebnisse zur geistigen Welt in eine Be­ziehung zu setzen, welche durch die Ideen der rein natur­wissenschaftlich-anthropologischen Forschung nicht zu durchschauen ist.",
        "Was eine Vorstellungsart wie diejenige des Thomas von Aquino für die Vertiefung der Naturwis­senschaft nach der geistigen Seite zu leisten vermag, das wird gegenwärtig in vielen Kreisen ganz verkannt."
      ],
      [
        "Man glaubt in solchen Kreisen, die neueren naturwissenschaft­lichen Erkenntnisse bedingten eine Abkehr von dieser Vor­stellungsart.",
        "Die Wahrheit ist, daß man zunächst das na­turwissenschaftlich erkannte Wesenhafte der Welt mit Ge­danken umspannen will, welche bei genauerem Zusehen in sich unvollendet bleiben."
      ],
      [
        "Ihre Vollendung wäre, sie selbst als ein solches Wesenhaftes in der Seele zu denken, wie sie in der Vorstellungsart des Thomas von Aquino gedacht werden.",
        "Brentano befand sich auch auf dem Wege, ein rechtes Verhältnis zu dieser Vorstellungsart zu gewinnen."
      ],
      [
        "Schreibt er doch : «Als ich meine Abhandlung und später meine schrieb, wollte ich in einer zweifachen Weise das Verständnis sei­ner Lehre fördern; einmal und vorzüglich direkt durch Aufhellung einiger der wichtigsten Lehrpunkte, dann in­direkt, aber in allgemeinerer Weise, indem ich der Erklä­rung neue Hiifsquellen eröffnete.",
        "Ich machte auf die scharfsinnigen Kommentare des Thomas von Aquino auf­merksam und zeigte, wie man in ihnen manche Lehre rich­tiger als bei späteren Erklärern dargestellt findet.»* - Brentano"
      ],
      [
        "* Vergleiche Brentano : «Aristoteles' Lehre vom Ursprung des menach­lichen Geistes» (1911), Seite 1."
      ],
      [
        "verlegte sich den Weg, der sich ihm durch solche Stu­dien hätte darbieten können, durch seine Hinneigung zu der Vorstellungsart von Bacon, Locke und allem, was mit solch einer Vors tellungsart philosophisch zusammenhängt.",
        "Er hielt diese Vorstellungsart vor allem für die der natur-wissenschaftlichen Forschungsweise gemäße.* Doch eben diese Vorstellungsart führt dazu, den Inhalt des Seelenle­bens in völliger Abhängigkeit von der Sinneswelt zu den­ken."
      ],
      [
        "Und weil diese Denkweise nur anthropologisch vor­gehen will, so kommt nur dasjenige als psychologisches Ergebnis in ihren Bereich, was in Wahrheit keine seelische Wirklichkeit ist, sondern nur ein Spiegelbild dieser Wirk­lichkeit, nämlich der Inhalt des gewöhnlichen Bewußt­seins. - Hätte Brentano die Spiegelbild-Natur des gewöhn­lichen Bewußtseins durchschaut : er hätte im Verfolg der anthropologischen Forschung nicht haltmachen können vor dem Tore, das in die Anthroposophie führt. - Es wird gewiß dieser meiner Anschauung gegenüber die Meinung geltend gemacht werden können, Brentano habe eben der Gabe des geistigen Schauens ermangelt; deshalb habe er nicht den Übergang von Anthropologie zur Anthroposo­phie gesucht, wenn er auch durch seine besondere geistige Eigenart dazu getrieben worden ist, in interessanter Form die Seelenerscheinungen so verstandesgemäß zu charak­terisieren, daß sich diese Form durch die Anthroposophie rechifertigen läßt.",
        "Ich habe aber diese Meinung nicht."
      ],
      [
        "Ich bin nicht der Anschauung, daß geistiges Schauen nur als"
      ],
      [
        "* Vergleiche unter anderem Brentano: «Die vier Phasen der Philosophie» (1895), Seite 22, und die ganze Haltung seiner Wiener Antrittsrede «Über die Gründe der Entmutigung auf philosophischem Gebiete» (Wien 1874, W.",
        "Braumüller)."
      ],
      [
        "eine besondere Gabe für Ausnahmepersönlichkeiten er­reichbar ist.",
        "Ich muß dieses Schauen für eine Fähigkeit der Menschenseele halten, die jeder sich aneignen kann, wenn er die zu ihr führenden seelischen Erlebnisse in sich wach­ruft.",
        "Und Brentanos Natur erscheint mir zu solchem Wach-Rufen ganz besonders geeignet.* Ich halte aber dafür, daß man solches Wach-Rufen durch Theorien, die ihm wider­streben, verhindern kann.",
        "Daß man das Schauen nicht auf­kommen läßt, wenn man sich in Ideen verstrickt, welche dessen Berechtigung von vorneherein in Frage stellen.",
        "Und Brentano hat das Schauen in seiner Seele dadurch nicht aufkommen lassen, daß bei ihm die Ideen, welche es in so schöner Art rechifertigten, stets unterlagen denen, die es verwerfen, und die befürchten lassen, daß man durch dasselbe in « den labyrinthischen Gängen einer Pseudo­philosophie sich verliere».**"
      ],
      [
        "1895 hat Brentano den Abdruck eines Vortrages erschei­nen lassen, den er in der « Literarischen Gesellschaft in Wien» mit Rücksicht auf H.Lorms Buch «Der grundlose Optimismus» gehalten hat.*** Dieser enthält seine Ansicht über «die vier Phasen der Philosophie und ihren augen­blicklichen Stand».",
        "Brentano vertritt in diesen Ausführun­gen die Meinung, daß sich der Entwickelungsgang des philosophischen Forschens in einer gewissen Beziehung"
      ],
      [
        "* Man vergleiche Herzu das 8.",
        "Kapitel der am Ende dieser Schrift gege­benen «Skizzenhaften Erweiterungen des Inhaltes...» : «8.",
        "Ein oft erhobener Einwand gegen die Anthroposophie.»"
      ],
      [
        "** Vergleiche oben Seite 79."
      ],
      [
        "*** Brentano : «Die vier Phasen der Philosophie und ihr augenblicklicher Stand» (Stuttgart 1895, J.",
        "G.Cottasche Buchhandlung Nachfolger)."
      ],
      [
        "vergleichen lasse mit der Geschichte der schönen Künste.",
        "«Während andere Wissenschaften, so lange sie überhaupt betrieben werden, einen stetigen Fortschritt aufweisen, der nur einmal durch eine Zeit des Stillstandes unterbrochen wird, zeigt die Philosophie, wie die schöne Kunst, neben den Zeiten aufsteigender Entwickelung Zeiten der Deca­dence, die oft nicht minder reich, ja reicher an epochema­chenden Erscheinungen sind als die Zeiten gesunder Fruchtbarkeit.»* Drei solcher Perioden, die von gesunder Fruchtbarkeit zur Decadence fortlaufen, unterscheidet Brentano im verflossenen Entwickelungsgang der Philo­sophie."
      ],
      [
        "Eine jede beginnt damit, daß aus dem reinen philo­sophischen Staunen über die Rätsel der Welt sich wahr­haft wissenschaftliches Interesse regt, und dieses Interesse eme Erkenntnis aus echtem, reinem Wissenstrieb sucht.",
        "Auf diese gesunde Epoche folgt dann eine andere, in der das erste Stadium des Verfalls erscheint."
      ],
      [
        "Da tritt das reine wissenschaftliche Interesse zurück, und man sucht nach Gedanken, durch die man das soziale und persönliche Le­ben regeln und sich in denselben zurechtfinden kann.",
        "Die Philosophie will da nicht mehr dem reinen Erkenntnisstre­ben, sondern den Interessen des Lebens dienen."
      ],
      [
        "Ein wei­terer Verfall tritt in der dritten Epoche ein, Man wird durch die Unsicherheit der Gedanken, die einem nicht rei­nen wissenschaftlichen Interesse entsprungen sind, an der Möglichkeit wahrer Erkenntnis irre und verfällt in Skep­tizismus.",
        "Die vierte Epoche ist dann diejenige des völligen Niederganges."
      ],
      [
        "Der Zweifel der dritten Epoche hat alle wissenschaftliche Grundlage der Philosophie unterhöhlt.",
        "Man sucht aus unwissenschaftlichen Untergründen in"
      ],
      [
        "* Vergleiche «Vier Phasen», Seite 9."
      ],
      [
        "phantastischen, verschwimmenden Begriffen, durch my­stisches Erleben zur Wahrheit zu kommen.",
        "Den ersten Entwickelungskreis denkt sich Brentano mit der griechi­schen Naturphilosophie beginnend; und mit Aristoteles, meint er, schließe die gesunde Phase ab."
      ],
      [
        "Anaxagoras schätzt er innerhalb dieser Phase besonders hoch ein.",
        "Er ist der Ansicht, daß, trotzdem in dieser Zeit die Griechen in bezug auf viele wissenschaftliche Fragen, ganz im Anfange standen, die Art ihres Forschens doch einen solchen Charakter hatte, der vor einer strengen naturwissenschaft­lichen Denkungsart seine Rechtfertigung findet."
      ],
      [
        "Auf diese erste Phase folgen die Stoiker, die Epikuräer.",
        "Sie bringen schon einen Verfall.",
        "Sie wollen Ideen, die im Dienste des Lebens stehen.",
        "In der Neueren Akademie, besonders aber durch Aenesidemus, Agrippa, Sextus Empirikus sieht man den Skeptizismus allen Glauben an sichergestellte wissen­schaftliche Wahrheiten austilgen."
      ],
      [
        "Und im Neuplatonismus, bei Ammonius Sakkas, Plotin, Porphyrius, Jamblichus, Proklus tritt an die Stelle des wissenschaftlichen Forschens das in den labyrinthischen Gängen einer Pseudophiloso­phie sich ergehende mystische Erleben. - Im Mittelalter sieht man, wenn auch vielleicht nicht mit solcher Deutlich­keit, diese vier Phasen sich wiederholen.",
        "Mit Thomas von Aquino hebt eine philosophisch gesunde Vorstellungsart an, die den Aristotelismus in einer neuen Form aufleben läßt."
      ],
      [
        "In der darauf folgenden Zeit, deren Repräsentant Duns Scotus ist, herrscht durch eine ins Ungeheuerliche getriebene Disputierkunst, eine Art Analogon zur ersten griechischen Verfallsperiode.",
        "Auf sie folgt der Nominalis­mus, der einen skeptischen Charakter trägt."
      ],
      [
        "Wilhelm von Occam verwirft die Ansicht, daß sich die allgemeinen"
      ],
      [
        "Ideen auf etwas Wirkliches beziehen, und gibt dadurch dem Inhalte der menschlichen Wahrheit nur den Wert einer außer der Wirklichkeit stehenden begrifflichen Zu­sammenfassung; während die Wirklichkeit nur in den individuellen Einzeldingen liegen soll.",
        "Dieses Analogon der Skepsis wird abgelöst durch die nicht in wissenschaftlichen Bahnen strebende Mystik der Eckhardt, Tauler, Heinrich Suso, des Verfassers der Deutschen Theologie und ande­rer."
      ],
      [
        "Dies sind die vier Phasen der philosophischen Ent­wickelung im Mittelalter. - In der Neuzeit beginnt mit Bacon von Verulam wieder eine gesunde, auf naturwissen­schaftlichem Denken ruhende Entwickelung, in welcher dann Descartes, Locke, Leibniz fruchtbringend weiter wir­ken.",
        "Auf sie folgt die französische und englische Aufklä­rungsphilosophie, in denen Grundsätze, wie man sie für das Leben sympathisch fand, die Haltung des philosophi­schen Gedankenganges beherrschten."
      ],
      [
        "Darauf tritt mit Da­vid Hume die Skepsis ein; und auf sie folgt die Phase des Niedergangs, die in England mit Thomas Reid, in Deutsch­land mit Kant einsetzt.",
        "Brentano betrachtet an Kants Phi­losophie eine Seite, die ihm gestattet, diese zusammenzubringen mit der Plotinschen Verfallsperiode der griechi­schen Philosophie."
      ],
      [
        "Er tadelt an Kant, daß dieser nicht wie ein wissenschaftlicher Forscher die Wahrheit in einer Übereinstimmung der Vorstellungen mit den wirklichen Ge­genständen suche, sondern vielmehr darin, daß sich die Gegenstände nach dem menschlichen Vorstellungsvermö­gen richten sollen.",
        "Damit glaubt Brentano der Kantschen Philosophie eine Art mystischen Grundzuges zuschreiben zu müssen, der sich dann in der Verfallsphilosophie Fich­tes, Schellings und Hegels in völliger Unwissenschaftlichkeit"
      ],
      [
        "offenbart. - Einen neuen Aufschwung der Philosophie erhofft Brentano von einer wissenschaftlichen Arbeit innerhalb ihres Gebietes nach dem Muster der in der neue­ren Zeit herrschend gewordenen naturwissenschaftlichen Denkungsart.",
        "Zur Einleitung einer solchen Philosophie hat er seine These aufgestellt : die wahre philosophische Forschungsart sei keine andere als die in der naturwissen­schaftlichen Erkennntisart anerkannte.* Ihr wollte er seine Lebensarbeit widmen."
      ],
      [
        "Brentano sagt in der Vorrede zu dem Abdruck des Vor­trages, in dem er diese Ansicht von den « vier Phasen der Philosophie» gegeben hat: diese «seine Auffassung der Geschichte der Philosophie mag manchen als neu befrem­den; mir selbst steht sie seit Jahren fest und wurde auch seit mehr als zwei Dezennien, wie von mir, so von einigen Schülern den akademischen Vorlesungen über Geschichte der Philsophie zugrunde gelegt.",
        "Daß sie Vorurteilen be­gegnen, und daß diese vielleicht zu mächtig sein werden, um beim ersten Anprall zu weichen, darüber ergebe ich mich keiner Täuschung.",
        "Immerhin hoffe ich von den vor­geführten Tatsachen und Erwägungen, daß sie bei dem, welcher denkend folgt, nicht ohne Eindruck bleiben kön­nen.»** - Daß man von diesen Ausführungen Brentanos einen be­deutenden Eindruck empfangen kann, ist durchaus meine Meinung.",
        "Insofern sie eine Klassifikation der im Laufe der philosophischen Entwickelung auftretenden Erscheinun­gen von einem gewissen Gesichtspunkte aus darbieten, be­ruhen sie auf gut begründeten Einsichten in diesen Entwickelungsgang."
      ],
      [
        "* Vergleiche oben Seite 81 f. dieser Schrift."
      ],
      [
        "** Vergleiche Brentano: «Die vier Phasen der Philosophie...», Seite 5 f."
      ],
      [
        "Die vier Phasen der Philosophie bieten Un­terschiede, die in der Wirklichkeit begründet sind. - Sobald man aber in eine Betrachtung der in den einzelnen Phasen treibenden Kräfte eintritt, kann man nicht finden, daß Bren­tano diese Kräfte zutreffend charakterisiert.",
        "Sogleich bei sei­ner Ansicht über die erste Phase der Philosophie des Alter­tums tritt das zutage.",
        "Die Grundzüge der griechischen Phi­losophie von den jonischen Anfängen bis zu Aristoteles weisen gewiß viele Züge auf, welche Brentano das Recht geben, in ihnen eine naturwissenschaftliche Denkart in sei­nem Sinne zu sehen.",
        "Aber kommt denn diese Denkart wirk­lich durch dasjenige zustande, was Brentano die naturwis­senschaftliche Methode nennt?",
        "Sind die Gedanken dieser griechischen Philosophen nicht vielmehr ein Ergebnis des­sen, was sie als das Wesen des Menschen und dessen Stel­lung zum Weltall in der eigenen Seele erlebten ?* Wer sich diese Frage sachgemäß beantwortet, wird finden, daß die inneren Impulse für den Gedankengehalt dieser Philoso­phie gerade im Stoizismus, im Epikuräismus, in der ganzen praktischen Lebensphilosophie der späteren Griechenzeit zum unmittelbaren Ausdruck kamen.",
        "Man kann bemerken, wie in den Seelenkräften, welche Brentano in der zweiten Phase wirksam findet, der Ausgangspunkt liegt für die erste Phase der Philosophie des Altertums.",
        "Diese Kräfte waren"
      ],
      [
        "* Im ersten Bande meines Buches «Die Rätsel der Philosophie » habe ich den Versuch gemacht, diese Frage im bejahenden Sinne zu beantworten.",
        "Ich bestrebe mich da, zu zeigen, wie die ersten griechischen Philosophen nicht aus der Naturbeobachtung heraus zu ihren Ideen kommen, sondern weil sie die äußere Natur von dem Erlebnisse ihres Seelen-Innern aus beur­teilten.",
        "Thales sprach davon, daß alles aus dem Wasser stamme, weil er die­sen Wasser-Entstehungs-Prozeß als das Wesen des eigenen menschlichen Inneren erlebte.",
        "Und so die ihm verwandten Philosophen.",
        "Vergleiche meine «Rätsel der Philosophie», Seite 52 ff."
      ],
      [
        "der sinnlichen und sozialen Erscheinungsform des Weltalls zugewendet und konnten daher in der Phase des Skeptizis­mus, der zum Zweifel an der unmittelbaren Wirklichkeit dieser Erscheinungsform getrieben wird, und in der folgen­den Phase des schauenden Erkennens, das über diese Form hinausgehen muß, nur unvollkommen auftreten.",
        "Aus die­sem Grunde zeigen sich diese Phasen innerhalb der Philoso­phie des Altertums als solche des Verfalls. - Und welche Seelenkräfte wirken im philosophischen Entwickelungsgang des Mittelalters?"
      ],
      [
        "Daß im Thomismus die Höhe dieses Entwickelungsganges liegt in bezug auf diejenigen Verhält­nisse, die Brentano ins Auge faßt, wird niemand bezweifeln können, der die in Betracht kommenden Tatsachen wirklich kennt.",
        "Aber man kann doch nicht verkennen, daß durch den christlichen Standpunkt des Thomas von Aquino die in der griechischen Lebensphilosophie wirksamen Seelenkräfte nicht mehr bloß aus philosophischen Impulsen heraus wir­ken, sondern einen überphilosophischen Charakter ange­nommen haben."
      ],
      [
        "Welche Impulse aber wirken bei Thomas von Aquino, insoferne er Philosoph ist?",
        "Man braucht keine Neigung für die Schwächen der nominalistischen Philoso­phen des Mittelalters zu haben; aber man wird doch finden können, daß die im Nominalismus wirkenden Seelenim­pulse die subjektive Grundlage bilden auch für den thomi­stischen Realismus."
      ],
      [
        "Wenn Thomas die Allgemeinbegriffe, welche die Erscheinungen der Sinneswahrnehmungen zu­sammenfassen, als dasjenige erkennt, was sich auf ein geistig Wirkliches bezieht, so gewinnt er die Kraft zu dieser seiner realistischen Vorstellungsart aus dem Gefühl desjenigen heraus, was diese Begriffe abgesehen davon, daß sie sich auf Sinneserscheinungen beziehen, in dem Dasein der Seele"
      ],
      [
        "selbst bedeuten.",
        "Gerade weil Thomas die Allgemeinbegriffe nicht unmittelbar auf die Vorkommnisse des Sinnesdaseins bezog, empfand er, wie in sie eine andere Wirklichkeit hereinleuchtet, und wie sie eigentlich für die Erscheinungen des Sinnenlebens nur Zeichen sind."
      ],
      [
        "Als dann im Nominalis­mus dieser Unterton des Thomismus als selbständige Philo­sophie auftrat, mußte er naturgemäß seine Einseitigkeit of­fenbaren.",
        "Das Gefühl, daß die in der Seele erlebten Begriffe einen ins Geistige gewandten Realismus begründen, mußte schwinden, und das andere vorherrschend werden, daß die Allgemeinbegriffe bloße zusammenfassende Namen sind."
      ],
      [
        "Wenn man die Wesenheit des Nominalismus so auffaßt, ver­steht man auch die ihm vorangehende zweite Phase der mit­telalterlichen Philosophie, den Skotismus, als einen Über­gang zum Nominalismus.",
        "Man wird aber doch nicht umhin können, die ganze Kraft der mittelalterlichen Denkarbeit, insoferne sie Philosophie ist, aus der Grundauffassung heraus zu verstehen, die sich in einseitiger Art im Nominalismus gezeigt hat."
      ],
      [
        "Dann aber wird man zu der Ansicht kommen, daß die wirklich treibenden Kräfte dieser Philosophie in den Seelenimpulsen liegen, welche man im Sinne der Brentano­schen Klassifikation als der dritten Phase angehörig bezeich­nen muß.",
        "Und in derjenigen Epoche, welche Brentano als die mystische Phase des Mittelalters kennzeichnet, tritt dann auch klar hervor, wie die ihr angehörigen Mystiker, durch die nominalistische Natur des begreifenden Erkennens be­wogen, sich nicht an dieses, sondern an andere Seelenkräfte wenden, um zum Kerne der Welterscheinungen vorzudrin­gen. - Verfolgt man nun für die Philosophie der neueren Zeit die Wirksamkeit der treibenden Seelenkräfte an dem Faden der Brentanoschen Klassifikation, so findet man, daß"
      ],
      [
        "die inneren Wesenszüge dieser Epoche ganz andere sind, als diejenigen, welche von Brentano verzeichnet werden.",
        "Die Phase der naturwissenschaftlichen Denkart, welche Brentano durch Bacon von Verulam, Descartes, Locke, Leibniz verwirklicht findet, will sich gewisser ihr eigener Charakterzüge wegen durchaus nicht als rein naturwissen­schaftlich im Brentanoschen Sinne denken lassen."
      ],
      [
        "Wie soll man dem Grundgedanken Descartes' «Ich denke, also bin ich» rein naturwissenschaftlich beikommen; wie soll man Leibnizens Monadologie, oder dessen «vorbestimmte Har­monie » in die naturwissenschaftliche Vorstellungsart Bren­tanos hineinbringen?",
        "Auch die Brentanosche Auffassung der zweiten Phase, welcher er die französische und englische Aufklärungsphilosophie zuteilt, macht Schwierigkeiten, wenn man bei seinen Vorstellungen stehen bleiben will."
      ],
      [
        "Man wird dieser Epoche gewiß den Charakter einer Ver­fallszeit der Philosophie nicht absprechen wollen; aber man kann sie verstehen aus der Tatsache heraus, daß in ihren Trägern die in der christlichen Lebensanschauung ener­gisch wirksamen außerphilosophlschen Seelenimpulse ge­lähmt waren, so daß ein Verhältnis zu den übersinnlichen Weltkräften philosophisch nicht gefunden werden konnte.",
        "Zugleich wirkte die nominalistische Skepsis des Mittelal­ters noch nach, wodurch verhindert wurde, daß eine Bezie­hung des seelisch erlebten Erkennmis-Inhaltes zu einem geistig Wirklichen gesucht wurde. - Und schreitet man dann zu dem neuzeitlichen Skeptizismus und derjenigen Vorstellungsweise fort, die Brentano einer mystischen Phase zueignet, dann verliert man die Möglichkeit, seiner Klassifikation noch zuzustimmen."
      ],
      [
        "Gewiß muß man die skeptische Phase mit David Hume beginnen lassen.",
        "Aber"
      ],
      [
        "Kant, den Kritiker, als Mystiker kennzeichnen, erweist sich denn doch als stark einseitige Charakteristik.",
        "Und die Philo­sophien Fichtes, Schellings, Hegels und anderer Denker der auf Kant folgenden Zeit lassen sich nicht als mystische fas­sen, besonders, wenn man den Brentanoschen Begriff der Mystik zugrunde legt."
      ],
      [
        "Man wird vielmehr gerade im Sinne der Brentanoschen Klassifikation von David Hume über Kant, bis zu Hegel einen gemeinsamen Grundzug finden.",
        "Dieser besteht in der Ablehnung, auf Grund derjenigen Vorstellungen, die aus der Sinneswelt gewonnen sind, das philosophische Weltbild einer wahren Wirklichkeit zu zeichnen."
      ],
      [
        "So paradox es scheint, Hegel einen Skeptiker zu nennen : er Ist es doch in dem Sinne, daß er den Vorstellun­gen, welche der Natur entnommen sind, keinen unmittelba­ren Wirklichkeitswert zuschreibt.",
        "Man weicht von dem Brentanoschen Begriff des Skeptizismus nicht ab, wenn man die Entwickelung der Philosophie von Hume bis Hegel als die Phase des neuzeitlichen Skeptizismus auffaßt."
      ],
      [
        "Die vierte neuzeitliche Phase kann man erst nach Hegel beginnen las­sen.",
        "Was in ihr als naturwissenschaftliche Vorstellungsart auftritt, wird aber Brentano sicherlich nicht in die Nähe des Mystizismus bringen wollen."
      ],
      [
        "Doch man fasse ins Auge, in welcher Art Brentano selbst sich mit seinem Philosophieren in diese Epoche hineinstellen will.",
        "Mit einer kaum zu über­bietenden Energie fordert er für die Philosophie eine natur­wissenschaftliche Methode."
      ],
      [
        "In seiner psychologischen For­schung strebt er die Innehaltung dieser Methode an.",
        "Und was er zutage fördert, ist eine Rechtfertigung der Anthropo­sophie.",
        "Was als Fortsetzung seines anthropologischen Stre­bens auftreten müßte, wenn er im Sinne des von ihm Vorge­stellten weiter schritte, wäre Anthroposophie."
      ],
      [
        "eine Anthroposophie, welche mit der naturwissenschaftli­chen Denkungsart in voller Harmonie steht. - Ist nicht Brentanos Lebensarbeit selbst der vollgültigste Beweis dafür, daß die vierte Phase der neuzeitlichen Philosophie ihre Impulse aus denjenigen Seelenkräften ziehen muß, welche der Neuplatonismus ebenso wie die Mystik des Mittelalters betätigen wollten, aber nicht konnten, weil sie mit dem inneren Seelenwirken nicht bis zu einem solchen Erleben der geisti­gen Wirklichkeit zu kommen vermochten, das in völliger bewußter Klarheit des Denkens (oder der Begriffe) sich vollzieht?",
        "Wie die griechische Philosophie ihre Kraft aus den Seelenimpulsen schöpfte, welche Brentano in der zwei­ten philosophischen Phase sich verwirklichen sieht, aus der praktischen Lebensphilosophie; wie die mittelalterliche Philosophie den Impulsen der dritten Phase, dem Skeptizis­mus ihre Stärke verdankt; so muß die neuzeitliche Philoso­phie ihre Impulse aus den Grund-Kräften der vierten Phase holen, aus dem erkennenden Schauen.",
        "Darf also Brentano in dem Neuplatonismus und in der mittelalterlichen Mystik Verfallsphilosophien in Gemäßheit seiner Vorstellungsart annehmen, so könnte man in der die Anthropologie ergän­zenden Anthroposophie die fruchtbare Phase der neueren Philosophie anerkennen, wenn man dieses Philosophen ei­gene Ideen über Philosophie-Entwickelung zu den Konse­quenzen führt, die er nicht selbst gezogen hat, die aber ganz ungezwungen sich aus ihnen ergeben."
      ],
      [
        "In dem gekennzeichneten Verhältnis Brentanos zu den Er­kenntnis-Forderungen der Gegenwart ist es wohl gelegen, daß man beim Lesen seiner Schriften Eindrücke empfängt,"
      ],
      [
        "welche sich nicht in dem erschöpfen, was der unmittelbare Inhalt der von ihm vorgebrachten Begriffe enthält.",
        "Es klin­gen in dieses Lesen überall Untertöne hinein.",
        "Diese kom­men aus einem Seelenleben, das hinter den ausgesprochenen Ideen weit zurückliegt.",
        "Was Brentano im Geiste des Lesers anregt, ist oft stärker in diesem wirksam, als das von dem Verfasser in scharf umrissenen Vorstellungen Gesagte.",
        "Man fühlt sich auch veranlaßt, oftmals zum Lesen einer Brenta­noschen Schrift zurückzukehren.",
        "Man kann vieles von dem durchdacht haben, was gegenwärtig über das Verhältnis der Philosophie zu andern Erkenntnisvorstellungen gesagt wird; Brentanos Schrift «Über die Zukunft der Philoso­phie» wird bei solchem Durchdenken fast immer in der Er­innerung auftauchen.",
        "Diese Schrift gibt einen Vortrag wie­der, den er in der «Philosophischen Gesellschaft» in Wien 1892 gehalten hat, um seine Auffassung über die Zukunft der Philosophie den hierauf bezüglichen Ansichten entge­genzuhalten, welche der Rechtsgelehrte Adolf Exner in ei­ner Inaugurationsrede über «politische Bildung» (1 891) vorgebracht hatte.* Der Abdruck des Vortrages ist mit «Anmerkungen» versehen, die weitweisende geschichtli­che Ausblicke in den geistigen Entwickelungsgang der Menschheit geben. - In dieser Schrift klingt alles an, was sich dem Betrachter der gegenwärtigen naturwissenschaft­lichen Vorstellungsart über die Notwendigkeit ergeben kann, von dieser Vorstellungsart aus zu einer anthroposo­phischen fortzuschreiten."
      ],
      [
        "* Brentano : «Über die Zukunft der Philosophie».",
        "Mit apologetisch-kritischer Berücksichtigung der Inaugurationsrede von Adolf Exner «Über politische Bildung» als Rektor der Wiener Universität (Wien, Alfred Höl­der, 1893)."
      ],
      [
        "Die Träger dieser naturwissenschaftlichen Vorstellungsart leben zumeist in dem Glauben, daß sie ihnen von dem wirklichen Sein der Dinge selbst aufgedrängt ist.",
        "Sie sind der Meinung, daß sie ihre Erkenntnisse so einrichten, wie die Wirklichkeit sich offenbart."
      ],
      [
        "Doch dieser Glaube ist eine Täuschung.",
        "Die Wahrheit ist, daß in der neueren Zeit die menschliche Seele aus ihrer eigenen, im Laufe der Jahrtau­sende tätigen, Entwickelung heraus Bedürfnisse nach sol­chen Vorstellungen entfaltet hat, welche das naturwissen­schaftliche Weltbild ausmachen."
      ],
      [
        "Helmholtz.",
        "Weisman, Huxiey und andere sind zu ihren Vorstellungen nicht des­halb gekommen, weil die Wirklichkeit ihnen diese als die absolute Wahrheit gegeben hat, sondern weil sie in sich diese Vorstellungen bilden mußten, um durch sie auf die ihnen entgegentretende Wirklichkeit ein gewisses Licht zu werfen."
      ],
      [
        "Man formt sich ein mathematisches oder mechani­sches Weltbild nicht, weil eine außerseelische Wirklichkeit dazu zwingt, sondern weil man in seiner Seele die mathema­tischen und mechanischen Vorstellungen ausgebildet und sich dadurch eine innere Beleuchtungsquelle für das eröffnet hat, was in der Außenwelt auf mathematische und mechani­sche Art sich offenbart. - Obgleich nun im allgemeinen das eben Gekennzeichnete für jede Entwickelungsstufe der menschlichen Seele gilt : es erscheint an den neueren natur-wissenschaftlichen Vorstellungen noch auf eine besondere Weise.",
        "Diese Vorstellungen vernichten, wenn sie folgerecht von einer Seite durchdacht werden, die Begriffe über das Seelische."
      ],
      [
        "An dem durchaus nicht unerheblichen aber höchst fragwürdigen Begriffe einer «Seelenlehre ohne Seele», der nicht von philosophischen Dilettanten allein, sondern von sehr ernsten Denkern gebildet worden ist,"
      ],
      [
        "zeigt sich dieses.* Solche Vorstellungen bringen dazu, die Erscheinungen des gewöhnlichen Bewußtseins in ihrer Ab­hängigkeit von der Leibesorganisation immer mehr zu durchschauen.",
        "Wird damit nicht zugleich erkannt, daß in dem, was in dieser Art als Seelisches auftritt, nicht dieses selbst, sondern nur dessen Spiegelbild sich offenbart, dann entwindet sich der Betrachtung die wirkliche Idee des See­lischen, und die Schein-Idee tritt auf, die in dem Seelischen nur sieht, was Ergebnis der Leibesorganisation ist."
      ],
      [
        "Nun läßt sich andrerseits für das unbefangene Denken die letz­tere Ansicht aber doch nicht halten.",
        "Die Ideen, welche die Naturwissenschaft über die Natur bildet, erweisen vor die­sem unbefangenen Denken ihren seelischen Zusammen­hang mit einer hinter der Natur liegenden Wirklichkeit, der in diesen Ideen selbst sich nicht offenbart."
      ],
      [
        "Keine anthropo­logische Betrachtungsart kann von sich aus zu erschöpfen­den Vorstellungen über diesen Zusammenhang kommen.",
        "Denn er tritt nicht in das gewöhnliche Bewußtsein herein. - Diese Tatsache tritt bei den gegenwärtigen naturwissen­schaftlichen Vorstellungen stärker zutage als bei geschicht­lich vergangenen Erkenntnisstufen."
      ],
      [
        "Die letzteren bildeten bei der Beobachtung der Außenwelt noch Begriffe, welche in ihren Inhalt etwas von der geistigen Unterlage dieser Außenwelt hereinnahmen.",
        "Und die Seele fühlte sich in ihrer eigenen Geistigkeit mit dem Geiste der Außenwelt als in einer Einheit."
      ],
      [
        "Die neuere Naturwissenschaft muß, ihrem Wesen nach, die Natur eben rein naturgemäß denken.",
        "Dadurch"
      ],
      [
        "* Auch diese Vorstellung «Seelenlehre ohne Seele» gehört in den Be­reich der in dieser Schrift gekennzeichneten Rätsel an den «Grenzorten des Erkennens»; und wird sie nicht so durchlebt, daß sie als Ausgangspunkt für das schauende Bewußtsein genommen wird, so vermauert sie den Zugang zu dem wahren Seelen-Erkennen, Statt einen Weg zu ihm zu zeigen."
      ],
      [
        "gewinnt sie die Möglichkeit, wohl den Inhalt ihrer Ideen durch die Naturbeobachtung zu rechtfertigen, nicht aber das Dasein dieser Ideen, als inneres Seelisch-Wesenhaf­tes, selbst. - Aus diesem Grunde ist gerade die echt naturwissenschaftliche Vorstellungsart ohne allen Boden, wenn sie ihr eigenes Dasein nicht rechtfertigen kann durch eine anthroposophische Beobachtung.",
        "Mit Anthroposophie kann man in uneingeschränkter Art sich zu der naturwis­senschaftlichen Vorstellungsweise bekennen; ohne Anthro­posophie wird man immer aufs neue den vergeblichen Ver­such machen wollen, aus naturwissenschaftlichen Beobach­tungsergebnis sen heraus selbst den Geist zu entdecken.",
        "Die naturwissenschaftlichen Ideen der neueren Zeit sind eben Erzeugnisse des Zusammenlebens der Seele mit einer geisti­gen Welt; aber wissen kann die Seele von diesem Zusammen­leben nur in lebendiger Geistbetrachtung.*"
      ],
      [
        "Man könnte leicht auf die Frage kommen: Warum sucht denn die Seele naturwissenschaftliche Vorstellungen auszu­bilden, wenn sie sich dadurch geradezu einen Inhalt schafft, der sie von ihrer Geist-Grundlage abschneidet?",
        "Vom Stand­punkte einer solchen Meinung, welche die naturwissen­schaftlichen Vorstellungen deshalb gebildet glaubt, weil die Welt nun einmal ihnen gemäß sich offenbart, läßt sich auf diese Frage keine Antwort finden.",
        "Wohl aber ergibt sich eine solche, wenn man auf die Bedürfnisse des seelischen Le­bens"
      ],
      [
        "* Wohin eine echte natutwissenschaftliche Bettachtungsart kommt, das zeigt in einleuchtender Art das in vielen Beziehungen hervotragende Buch Oskar Hertwigs: «Das Werden des Organismen, Widerlegung von Darwins Zufallstheorie» (1916).",
        "Gerade wenn eine Arbeit, wie die dieser Schrift zugrund liegende, in so mustergiltiger Art naturwissenschaftlich-methodiseh gehalten ist, führt sie zu unzähligen Seelen-Erlebnissen an den «Grenzorten des Erkennens»."
      ],
      [
        "selbst sieht.",
        "Mit Vorstellungen, wie sie eine vornatur­wissenschaftliche Zeit allein ausgebildet hat, könnte das see­lische Erleben niemals zum vollen Bewußtsein seiner selbst gelangen.",
        "Es würde zwar in den Natur-Ideen, die Geistiges mitenthalten, einen unbestimmten Zusammenhang mit dem Geiste erfühlen, nicht aber des Geistes volle, unabhängige Eigenart erleben können.",
        "Es strebt daher das Seelische im Entwickelungsgang der Menschheit nach der Aufstellung solcher Ideen, welche dieses Seelische selbst nicht enthalten, um an ihnen, sich selbst unabhängig vom Naturdasein zu wis­sen.",
        "Der Zusammenhang mit dem Geiste muß aber dann nicht durch diese Natur-Ideen, sondern durch geistiges Schauen erkennend gesucht werden.",
        "Die Ausbildung der neueren Naturwissenschaft ist eine notwendige Stufe im Seelen-Entwickelungsgange der Menschheit.",
        "Man erkennt ihre Grundlage, wenn man einsieht, wie die Seele ihrer be­darf, um sich selbst zu finden.",
        "Man erkennt auf der andern Seite ihre erkenntnistheoretische Tragweite, wenn man durchschaut, wie gerade sie das geistige Schauen zu einer Notwendigkeit macht.*"
      ],
      [
        "Adolf Exner, gegen dessen Meinung Brentanos Schrift «Die Zukunft der Philosophie» gerichtet ist, stand einer Naturwissenschaft gegenüber, welche zwar die Natur-Ideen rein ausbilden will, die aber nicht bereit ist, zur Anthropo­sophie fortzuschreiten, wenn es sich um die Erfassung der seelischen Wirklichkeit handelt.",
        "Er fand die «naturwissen­schaftliche Bildung» unfruchtbar für die Ausgestaltung der"
      ],
      [
        "* Das oben Ausgesprochene findet man im einzelnen dargestellt in mei­nem Buche: «Die Rätsel der Philosophie.» Zu zeigen, wie das naturwissen­schaftliche Erkennen im Seelenfortschritt der Menschheit seine Kraft be­währt, bildet einen der Grundgedanken dieses Buches."
      ],
      [
        "Ideen, die im gesellschaftlichen Zusammenleben der Men­schen wirken müssen.",
        "Er fordert daher eine Denkungsart für die Lösung der dem kommenden Zeitalter bevorstehen­den Fragen des Gesellschaftslebens, die nicht auf naturwis­senschaftlicher Grundlage ruht."
      ],
      [
        "Er findet, daß die großen juristischen Fragen, welchen das Römertum gegenüber­stand, von diesem gerade deshalb so fruchtbringend gelöst worden sind, weil die Römer für naturwissenschaftliche Vorstellungsart wenig Begabung hatten.",
        "Und er versucht, zu zeigen, daß das achtzehnte Jahrhundert trotz seiner Nei­gung zu naturwissenschaftlicher Denkungsart sich der Be­zwingung der Gesellschaftsfragen wenig gewachsen ge­zeigt hat."
      ],
      [
        "Exner richtet seinen Blick auf eine naturwissen­schaftliche Vorstellungsart, die nicht um ihre eigenen Grundlagen wissenschaftlich bemüht ist.",
        "Man kann verste­hen, daß er einer solchen gegenüber zu seinen Ansichten ge­kommen ist."
      ],
      [
        "Denn sie muß ihre Ideen so ausgestalten, daß diese das Naturgemäße in seiner Reinheit vor die Seele füh­ren.",
        "Aus ihnen läßt sich kein Impuls für Gedanken gewin­nen, die im Gesellschaftsleben fruchtbar sind."
      ],
      [
        "Denn inner­halb dieses Lebens stehen Seelen den Seelen als solchen ge­genüber.",
        "Ein solcher Impuls kann sich nur ergeben, wenn das Seelische in seiner geistigen Art durch erkennendes Schauen erlebt wird, wenn die naturwissenschaftlich-an­thropologische Betrachtung in der anthroposophischen ihre Ergänzung findet. - Brentano trug in seiner Seele Ideen, die durchaus in das anthroposophische Gebiet mün­den, trotzdem er nur im Anthropologischen bleiben wollte."
      ],
      [
        "Deshalb sind seine Ausführungen gegen Exner von durch­schlagender Kraft, auch wenn Brentano den Übergang zur Anthroposophie nicht selbst machen will.",
        "Sie zeigen, wie"
      ],
      [
        "Exner gar nicht von dem spricht, was eine sich selbst ver­stehende naturwissenschaftliche Vorstellungsart wirklich vermag, sondern wie er einen Windmühlenkampf führt ge­gen eine sich selbst mißverstehende Denkart.",
        "Man kann Brentanos Schrift lesen und überall durchfühlen, wie be­rechtigt alles ist, was durch seine Ideen in diese oder jene Richtung weist, ohne daß man findet, er spreche restlos aus, worauf er verweist."
      ],
      [
        "Mit Franz Brentano ist eine Persönlichkeit hinweggegan­gen, welche in ihrem Werke zu erleben einen unermeßlichen Gewinn bedeutet.",
        "Dieser Gewinn ist völlig unabhängig von dem Grade der verstandesgemäßen Übereinstimmung, die man diesem Werke entgegenbringen kann.",
        "Denn er ent­springt aus den Offenbarungen einer Menschenseele, die viel tiefer in der Welt-Wirklichkeit ihren Ursprung haben, als die Sphäre ist, in welcher im gewöhnlichen Leben sich Verstandes-Übereinstimmungen finden.",
        "Und Brentano ist eine Persönlichkeit, bestimmt fortzuwirken im geistigen Entwickelungsgang der Menschheit, durch Impulse, die sich nicht in der Fortführung der von ihm entwickelten Ideen erschöpfen.",
        "Ich kann mir gut vorstellen, wie jemand durchaus nicht mit dem einverstanden ist, was ich über Brentanos Verhältnis zur Anthroposophie hier ausgeführt habe; daß man aber, auf welchem wissenschaftlichen Standpunkte man auch stehe, zu weniger verehrenden Empfindungen dem Werte von Brentanos Persönlichkeit gegenüber kommen kann als die sind, welche den Absichten meiner Ausführungen zugrunde liegen, scheint mir unmöglich, wenn man den philosophischen Geist auf sich wirken läßt, der durch die Schriften dieses Mannes weht."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "SKIZZENHAFTE ERWEITERUNGEN DESINHALTES DIESER SCHRIFT",
    "paragraphs": [
      "SKIZZENHAFTE ERWEITERUNGEN DESINHALTES DIESER SCHRIFT",
      "I. Die philosophische Rechtfertigung der Anthroposophie",
      "Zu Seite19 , Anmerkung zu Zeile 6 von oben",
      "Wer mit seiner Vorstellungsart in dem philosophischen Denken der Gegenwart wurzeln will, der hat nötig, erkenntnistheoretisch das Wesenhaft-Seelische, von dem der erste Abschnitt dieser Schrift spricht, vor sich selbst und vor diesem Denken zu rechtfertigen. Nach einer solchen Rechtfertigung verlangen viele Menschen nicht, die das wirklich Seelische aus unmittelbaren innerem Erleben ken­nen und es zu unterscheiden wissen von dem durch die Sinne bewirkten seelischen Erfahren. Diesen erscheint die Rechtfertigung oftmals als unnötige, ja unbequeme Begriffsspalterei. Ihrer so gearteten Abneigung steht der Un­wille der philosophisch Denkenden gegenüber. Sie wollen die inneren Erlebnisse des Seelischen nur als subjektive Erfahrungen gelten lassen, denen ein Erkenntniswert nicht zuzuschreiben ist. Sie sind daher wenig geneigt, im Bereiche ihrer philosophischen Begriffe die Elemente auf­zusuchen, durch die man an die anthroposophischen Ideen herankommt. Durch diese von beiden Seiten kommenden Abneigungen wird eine Verständigung außerordentlich er­schwert. Sie ist aber notwendig. Denn in unserer Zeit kann einer Vorstellungsart nur dann Erkenntniswert zugeschrieben",
      "werden, wenn sie ihre Anschauungen vor eben dersel­ben Kritik zur Geltung bringen kann, vor welcher die na­turwissenschaftlichen Gesetze ihre Rechtfertigung suchen. - Für eine erkenntnistheoretische Rechtfertigung der an­throposophischen Ideen handelt es sich vor allem darum, die Art, wie sie erlebt werden, möglichst genau in Begrif­fen zu fassen. Man kann dieses in der verschiedensten Wei­se tun.",
      "Es seien hier zwei von diesen Weisen zu schildern versucht. Für die Schilderung der einen sei ausgegangen von der Betrachtung der Erinnerung. Man wird allerdings dabei sogleich an einen mißlichen Punkt der gegenwärti­gen philosophischen Wissenschaft getrieben.",
      "Denn über das Wesen der Erinnerung herrschen in derselben wenig geklärte Begriffe. Ich werde hier von Vorstellungen aus­gehen, die ich zwar auf den Wegen der Anthroposophie gefunden, die aber durchaus philosophisch und physiolo­gisch zu begründen sind.",
      "Der Raum, den ich mir in dieser Schrift zumessen muß, reicht allerdings nicht aus, diese letztere Begründung hier zu geben. Ich hoffe sie in einer zukünftig erscheinenden Schrift zu liefern. Ich meine aber, was ich über die Erinnerung sagen werde, kann jeder be­gründet finden, der auf die heute vorhandenen Ergebnisse der physiologischen und psychologischen Wissenschaft mit richtigem Blicke zu sehen vermag. - Die durch Sinnes­eindrücke angeregten Vorstellungen treten in den Bereich des unbewußten menschlichen Erlebens.",
      "Sie können aus demselben wieder heraufgeholt, erinnert werden. Vorstellungen sind ein rein seelisch Wesenhaftos; ihr Bewußtsein im gewöhnlichen Wachleben ist leiblich bedingt. Auch kann sie die an den Leib gebundene Seele nicht durch ihre eigenen Kräfte aus dem unbewußten Zustande in den bewußten",
      "heraufheben. Sie bedarf dazu der Kräfte des Lei­bes. Für die gewöhnliche Erinnerung muß der Leib tätig sein, geradeso wie er für die Entstehung der Sinnesvor­stellungen in den Vorgängen der Sinnesorgane tätig sein muß.",
      "Stelle ich einen Sinnesvorgang vor, so muß sich zu­erst eine leibliche Tätigkeit in den Sinnesorganen entwik­keIn; in der Seele tritt als deren Ergebnis die Vorstellung auf. Erinnere ich eine Vorstellung, so muß eine der Sinnestätigkeit polar entgegengesetzte innere Leibestätigkeit (in feinen Organen) stattfinden, und in der Seele tritt als Er­gebnis die erinnerte Vorstellung auf.",
      "Diese Vorstellung bezieht sich auf einen Sinnesvorgang, der vor Zeiten vor meiner Seele gestanden hat. Ich stelle ihn vor durch ein in­neres Erlebnis, zu dem mich die Leibesorganisation befä­higt. Man vergegenwärtige sich nun das Wesen einer sol­chen Erinnerungsvorstellung.",
      "Denn man kommt durch diese Vergegenwärtigung auf das Wesen dessen, was die anthroposophischen Ideen sind. Sie sind keine Erinne­rungsvorstellungen; aber sie treten in der Seele so auf wie Erinnerungsvorstellungen.",
      "Dies ist für viele Menschen, die sich gerne in einer gröberen Art Vorstellungen über die geistige Welt verschaffen möchten, eine Enttäuschung. Aber man kann die geistige Welt auf keine derbere Weise erleben als in der Erinnerung ein in der Sinneswelt vor Zeiten erfahrenes, nicht mehr vor Augen stehendes Ereig­nis.",
      "Nun aber kommt die Fähigkeit, ein solches Ereignis zu erinnern, aus der Kraft der Leibesorganisation. Diese darf beim Erleben des Wesenhaft-Seelischen nicht mitwir­ken. Die Seele muß vielmehr in sich selbst die Fähigkeit er­wecken, das mit Vorstellungen zu vollbringen, was der Leib mit den Sinnesvorstellungen vollbringt, wenn er deren",
      "Erinnerung vermittelt. Solche Vorstellungen, die aus den Tiefen der Seele heraufgeholt werden allein durch die Ktaft der Seele, wie aus den Tiefen der Menschennatur durch die Leibesorganisation die Erinnerungsvorstellun­gen: dies sind Vorstellungen, welche sich auf die geistige Welt beziehen.",
      "Sie sind in jeder Seele vorhanden. Was er­worben werden muß, um dieses Vorhandensein gewahr zu werden, ist die Kraft, durch rein seelische Betätigung, diese Vorstellungen aus den Seelentiefen heraufzuholen.",
      "Wie die erinnerten Sinnesvorstellungen sich auf einen ver­gangenen Sinnes-Eindruck beziehen, so diese Vorstellun­gen auf einen nicht in der Sinneswelt vorhandenen Zusam­menhang der Seele mit der Geisteswelt. Die Menschenseele steht der geistigen Welt so gegenüber wie der Mensch im allgemeinen einem vergessenen Dasein gegenübersteht; und sie kommt zur Erkenntnis dieser Welt, wenn sie in sich Kräfte zum Erwachen bringt, welche jenen Leibeskräften ähnlich sind, die der Erinnerung dienen. - Es kommt also für die philosophische Rechtfertigung der Ideen vom wahrhaft Seelischen darauf an, das Innenleben so zu erforschen, daß man in demselben eine Betätigang findet, welche rein seelisch ist und doch in gewisser Bezie­hung gleichartig der beim Erinnern geübten Betätigung. - Eine zweite Weise, vom rein Seelischen einen Begriff zu bilden, kann die folgende sein.",
      "Man kann ins Auge fassen, was durch anthropologische Beobachtang über den wol­lenden (handelnden) Menschen auszumachen ist. Einem auszuführenden Willensimpuls liegt zunächst die Vorstel­lung von dem zu Wollenden zugrunde.",
      "Diese Vorstellung kann physiologisch in ihrer Bedingtheit von der Leibesorganisation (dem Nervensystem) erkannt werden. An die",
      "Vorstellung gebunden ist ein Gefühlston, ein fühlendes Sympathisieren mit dem Vorgestellten, das bewirkt, daß diese Vorstellung den Impuls für ein Wollen liefert. Dann aber verliert sich das seelische Erleben in die Tiefen, und bewußt tritt erst wieder der Erfolg auf.",
      "Der Mensch stellt vor , wie er sich bewegt, um das Vorgestellte auszuführen (Th. Ziehen hat in seiner physiologischen Psychologie be­sonders klar dieses alles dargestellt). - Man kann nun er­sehen, wie das bewußte Vorstellungsleben, wenn ein Wil­lensakt in Frage kommt, in bezug auf das Zwischenglied des Wollens aussetzt.",
      "Was seelisch im Wollen einer durch den Leib ausgeführten Handlung erlebt wird, tritt nicht in das gewöhnliche bewußte Vorstellen ein. Aber es ist auch einleuchtend, daß sich ein solches Wollen durch eine Tä­tigkeit des Leibes verwirklicht.",
      "Unschwer wird man aber auch erkennen, daß die Seele, indem sie, logischen Geset­zen folgend, durch Verknüpfung von Vorstellungen die Wahrheit sucht, ein Wollen entwickelt. Ein Wollen, das nicht in physiologischen Gesetzen zu umfassen ist.",
      "Sonst würde sich eine unlogische Vorstellungsverknüpfung - oder auch nur eine alogische - nicht sondern lassen von einer, die in den Bahnen der logischen Gesetzmäßigkeit verläuft. (Auf dilettantenhaftes Gerede, als ob logische Folgerung nur in einer von der Seele durch Anpassung an die Außenwelt erworbenen Eigenschaft bestünde, braucht man wohl nicht im Ernste Rücksicht zu nehmen.) In die­sem Wollen, das rein innerhalb der Seele verläuft, und das zu logisch gegründeten Überzeugungen führt, kann man ein Durchdrungensein der Seele mit einer rein geistigen Tätigkeit sehen. Von dem, was im Wollen nach außen vorgeht, weiß das gewöhnliche Vorstellen so wenig, wie der",
      "Mensch im Schlafe von sich weiß. Von dem logischen Be­stimmtsein beim Bilden von Überzeugungen hat er aber auch nicht ein so volles Bewußtsein wie von dem Inhalte der Überzeugungen selbst. Wer innerlich wenn auch nur anthropologisch zu beobachten versteht, der wird über die Anwesenheit des logischen Bestimmtseins im gewöhnli­chen Bewußtsein doch einen Begriff bilden können.",
      "Er wird erkennen, daß der Mensch von diesem Bestimmtsein so weiß wie er träumend weiß. Man kann durchaus die Rich­tigkeit des Paradoxons behaupten: das gewöhnliche Be­wußtsein kennt den Inhalt seiner Überzeugungen; aber es träumt nur von der logischen Gesetzmäßigkeit, die in dem Suchen nach diesen Überzeugungen lebt.",
      "Man sieht: im gewöhnlichen Bewußtsein verschläft man das Wollen, wenn man durch den Leib ein Wollen nach außen entwickelt; man verträumt das Wollen, wenn man im Denken nach Überzeugungen sucht. Doch erkennt man, daß in letzterem Falle dasjenige, wovon man träumt, kein Leibliches sein kann, denn sonst müßten die logischen Gesetze mit den physiologischen zusammenfallen.",
      "Faßt man den Begriff des im denkenden Suchen nach der Wahrheit lebenden Wollens, so ist dieser Begriff der eines seelisch Wesenhaf­ten. - Man kann aus den beiden Weisen (neben denen an­dere möglich sind), erkenntnistheoretisch sich dem Be­griffe des Seelisch-Wesenhaften, im Sinne der Anthroposo­phie, zu nähern, ersehen, wie scharf dieses Seelisch-Wesenhafte sich absondert von allem, was abnorme Seelentätig­keit ist, wie das visionäre, halluzinatorische, mediale usw. Wesen.",
      "Denn von all diesem Abnormen muß der Ursprung im physiologisch Bestimmbaren gesucht werden. Das See­lische der Anthroposophie ist aber nicht nur ein solches,",
      "das seelisch nach Art des gewöhnlichen gesunden Bewußt­seins erlebt wird, sondern ein solches, an dem in voller wacher Bewußtheit beim Vorstellung-Bilden so erlebt wird, wie man erlebt, wenn man sich an erfahrene Tatsa­chen des Lebens erinnert, oder wie man erlebt beim lo­gisch bedingten Bilden von Überzeugungen. Man sieht wohl, daß das erkennende Erleben der Anthroposophie in Vorstellungen verläuft, welche den Charakter des gewöhn­lichen von der Außenwelt mit der Wirklichkeit begabten Bewußtseins beibehalten, und zu diesem Fähigkeiten hin­zufügen, die in das Geistgebiet hineinführen; während al­les Visionäre, Halluzinatorische usw. in einem Bewußtsein lebt, das zu dem gewöhnlichen nichts hinzufügt, sondern von ihm Fähigkeiten wegnimmt, so daß der Bewußtseinsstatus unter den Grad heruntersinkt, der in dem bewußten Sinneswahrnehmen vorhanden ist.",
      "Für die Leser meiner Schriften, welche dasjenige kennen, was ich an andern Or­ten über das Gedächtnis und die Erinnerung ausgeführt habe, bemerke ich das Folgende. Die in das Unbewußte gegangenen Vorstellungen, welche später erinnert werden, hat man, während sie unbewußt bleiben, als Vorstellungen in dem Gliede der menschlichen Wesenheit zu suchen, das in diesen Schriften als Lebensleib (Ätherleib) bezeichnet wird.",
      "Die Tätigkeit aber, durch welche die im Lebensleib verankerten Vorstellungen erinnert werden, gehört dem physischen Leib an. Ich mache diese Bemerkung, damit nicht mancher «schnellfertig mit dem Urteil» einen Wider­spruch da konstruiert, wo eine durch die Natur der Sache geforderte Unterscheidung notwendig ist."
    ],
    "sentences": [
      [
        "SKIZZENHAFTE ERWEITERUNGEN DESINHALTES DIESER SCHRIFT"
      ],
      [
        "Die philosophische Rechtfertigung der Anthroposophie"
      ],
      [
        "Zu Seite19 , Anmerkung zu Zeile 6 von oben"
      ],
      [
        "Wer mit seiner Vorstellungsart in dem philosophischen Denken der Gegenwart wurzeln will, der hat nötig, erkenntnistheoretisch das Wesenhaft-Seelische, von dem der erste Abschnitt dieser Schrift spricht, vor sich selbst und vor diesem Denken zu rechtfertigen.",
        "Nach einer solchen Rechtfertigung verlangen viele Menschen nicht, die das wirklich Seelische aus unmittelbaren innerem Erleben ken­nen und es zu unterscheiden wissen von dem durch die Sinne bewirkten seelischen Erfahren.",
        "Diesen erscheint die Rechtfertigung oftmals als unnötige, ja unbequeme Begriffsspalterei.",
        "Ihrer so gearteten Abneigung steht der Un­wille der philosophisch Denkenden gegenüber.",
        "Sie wollen die inneren Erlebnisse des Seelischen nur als subjektive Erfahrungen gelten lassen, denen ein Erkenntniswert nicht zuzuschreiben ist.",
        "Sie sind daher wenig geneigt, im Bereiche ihrer philosophischen Begriffe die Elemente auf­zusuchen, durch die man an die anthroposophischen Ideen herankommt.",
        "Durch diese von beiden Seiten kommenden Abneigungen wird eine Verständigung außerordentlich er­schwert.",
        "Sie ist aber notwendig.",
        "Denn in unserer Zeit kann einer Vorstellungsart nur dann Erkenntniswert zugeschrieben"
      ],
      [
        "werden, wenn sie ihre Anschauungen vor eben dersel­ben Kritik zur Geltung bringen kann, vor welcher die na­turwissenschaftlichen Gesetze ihre Rechtfertigung suchen. - Für eine erkenntnistheoretische Rechtfertigung der an­throposophischen Ideen handelt es sich vor allem darum, die Art, wie sie erlebt werden, möglichst genau in Begrif­fen zu fassen.",
        "Man kann dieses in der verschiedensten Wei­se tun."
      ],
      [
        "Es seien hier zwei von diesen Weisen zu schildern versucht.",
        "Für die Schilderung der einen sei ausgegangen von der Betrachtung der Erinnerung.",
        "Man wird allerdings dabei sogleich an einen mißlichen Punkt der gegenwärti­gen philosophischen Wissenschaft getrieben."
      ],
      [
        "Denn über das Wesen der Erinnerung herrschen in derselben wenig geklärte Begriffe.",
        "Ich werde hier von Vorstellungen aus­gehen, die ich zwar auf den Wegen der Anthroposophie gefunden, die aber durchaus philosophisch und physiolo­gisch zu begründen sind."
      ],
      [
        "Der Raum, den ich mir in dieser Schrift zumessen muß, reicht allerdings nicht aus, diese letztere Begründung hier zu geben.",
        "Ich hoffe sie in einer zukünftig erscheinenden Schrift zu liefern.",
        "Ich meine aber, was ich über die Erinnerung sagen werde, kann jeder be­gründet finden, der auf die heute vorhandenen Ergebnisse der physiologischen und psychologischen Wissenschaft mit richtigem Blicke zu sehen vermag. - Die durch Sinnes­eindrücke angeregten Vorstellungen treten in den Bereich des unbewußten menschlichen Erlebens."
      ],
      [
        "Sie können aus demselben wieder heraufgeholt, erinnert werden.",
        "Vorstellungen sind ein rein seelisch Wesenhaftos; ihr Bewußtsein im gewöhnlichen Wachleben ist leiblich bedingt.",
        "Auch kann sie die an den Leib gebundene Seele nicht durch ihre eigenen Kräfte aus dem unbewußten Zustande in den bewußten"
      ],
      [
        "heraufheben.",
        "Sie bedarf dazu der Kräfte des Lei­bes.",
        "Für die gewöhnliche Erinnerung muß der Leib tätig sein, geradeso wie er für die Entstehung der Sinnesvor­stellungen in den Vorgängen der Sinnesorgane tätig sein muß."
      ],
      [
        "Stelle ich einen Sinnesvorgang vor, so muß sich zu­erst eine leibliche Tätigkeit in den Sinnesorganen entwik­keIn; in der Seele tritt als deren Ergebnis die Vorstellung auf.",
        "Erinnere ich eine Vorstellung, so muß eine der Sinnestätigkeit polar entgegengesetzte innere Leibestätigkeit (in feinen Organen) stattfinden, und in der Seele tritt als Er­gebnis die erinnerte Vorstellung auf."
      ],
      [
        "Diese Vorstellung bezieht sich auf einen Sinnesvorgang, der vor Zeiten vor meiner Seele gestanden hat.",
        "Ich stelle ihn vor durch ein in­neres Erlebnis, zu dem mich die Leibesorganisation befä­higt.",
        "Man vergegenwärtige sich nun das Wesen einer sol­chen Erinnerungsvorstellung."
      ],
      [
        "Denn man kommt durch diese Vergegenwärtigung auf das Wesen dessen, was die anthroposophischen Ideen sind.",
        "Sie sind keine Erinne­rungsvorstellungen; aber sie treten in der Seele so auf wie Erinnerungsvorstellungen."
      ],
      [
        "Dies ist für viele Menschen, die sich gerne in einer gröberen Art Vorstellungen über die geistige Welt verschaffen möchten, eine Enttäuschung.",
        "Aber man kann die geistige Welt auf keine derbere Weise erleben als in der Erinnerung ein in der Sinneswelt vor Zeiten erfahrenes, nicht mehr vor Augen stehendes Ereig­nis."
      ],
      [
        "Nun aber kommt die Fähigkeit, ein solches Ereignis zu erinnern, aus der Kraft der Leibesorganisation.",
        "Diese darf beim Erleben des Wesenhaft-Seelischen nicht mitwir­ken.",
        "Die Seele muß vielmehr in sich selbst die Fähigkeit er­wecken, das mit Vorstellungen zu vollbringen, was der Leib mit den Sinnesvorstellungen vollbringt, wenn er deren"
      ],
      [
        "Erinnerung vermittelt.",
        "Solche Vorstellungen, die aus den Tiefen der Seele heraufgeholt werden allein durch die Ktaft der Seele, wie aus den Tiefen der Menschennatur durch die Leibesorganisation die Erinnerungsvorstellun­gen: dies sind Vorstellungen, welche sich auf die geistige Welt beziehen."
      ],
      [
        "Sie sind in jeder Seele vorhanden.",
        "Was er­worben werden muß, um dieses Vorhandensein gewahr zu werden, ist die Kraft, durch rein seelische Betätigung, diese Vorstellungen aus den Seelentiefen heraufzuholen."
      ],
      [
        "Wie die erinnerten Sinnesvorstellungen sich auf einen ver­gangenen Sinnes-Eindruck beziehen, so diese Vorstellun­gen auf einen nicht in der Sinneswelt vorhandenen Zusam­menhang der Seele mit der Geisteswelt.",
        "Die Menschenseele steht der geistigen Welt so gegenüber wie der Mensch im allgemeinen einem vergessenen Dasein gegenübersteht; und sie kommt zur Erkenntnis dieser Welt, wenn sie in sich Kräfte zum Erwachen bringt, welche jenen Leibeskräften ähnlich sind, die der Erinnerung dienen. - Es kommt also für die philosophische Rechtfertigung der Ideen vom wahrhaft Seelischen darauf an, das Innenleben so zu erforschen, daß man in demselben eine Betätigang findet, welche rein seelisch ist und doch in gewisser Bezie­hung gleichartig der beim Erinnern geübten Betätigung. - Eine zweite Weise, vom rein Seelischen einen Begriff zu bilden, kann die folgende sein."
      ],
      [
        "Man kann ins Auge fassen, was durch anthropologische Beobachtang über den wol­lenden (handelnden) Menschen auszumachen ist.",
        "Einem auszuführenden Willensimpuls liegt zunächst die Vorstel­lung von dem zu Wollenden zugrunde."
      ],
      [
        "Diese Vorstellung kann physiologisch in ihrer Bedingtheit von der Leibesorganisation (dem Nervensystem) erkannt werden.",
        "An die"
      ],
      [
        "Vorstellung gebunden ist ein Gefühlston, ein fühlendes Sympathisieren mit dem Vorgestellten, das bewirkt, daß diese Vorstellung den Impuls für ein Wollen liefert.",
        "Dann aber verliert sich das seelische Erleben in die Tiefen, und bewußt tritt erst wieder der Erfolg auf."
      ],
      [
        "Der Mensch stellt vor , wie er sich bewegt, um das Vorgestellte auszuführen (Th.",
        "Ziehen hat in seiner physiologischen Psychologie be­sonders klar dieses alles dargestellt). - Man kann nun er­sehen, wie das bewußte Vorstellungsleben, wenn ein Wil­lensakt in Frage kommt, in bezug auf das Zwischenglied des Wollens aussetzt."
      ],
      [
        "Was seelisch im Wollen einer durch den Leib ausgeführten Handlung erlebt wird, tritt nicht in das gewöhnliche bewußte Vorstellen ein.",
        "Aber es ist auch einleuchtend, daß sich ein solches Wollen durch eine Tä­tigkeit des Leibes verwirklicht."
      ],
      [
        "Unschwer wird man aber auch erkennen, daß die Seele, indem sie, logischen Geset­zen folgend, durch Verknüpfung von Vorstellungen die Wahrheit sucht, ein Wollen entwickelt.",
        "Ein Wollen, das nicht in physiologischen Gesetzen zu umfassen ist."
      ],
      [
        "Sonst würde sich eine unlogische Vorstellungsverknüpfung - oder auch nur eine alogische - nicht sondern lassen von einer, die in den Bahnen der logischen Gesetzmäßigkeit verläuft. (Auf dilettantenhaftes Gerede, als ob logische Folgerung nur in einer von der Seele durch Anpassung an die Außenwelt erworbenen Eigenschaft bestünde, braucht man wohl nicht im Ernste Rücksicht zu nehmen.) In die­sem Wollen, das rein innerhalb der Seele verläuft, und das zu logisch gegründeten Überzeugungen führt, kann man ein Durchdrungensein der Seele mit einer rein geistigen Tätigkeit sehen.",
        "Von dem, was im Wollen nach außen vorgeht, weiß das gewöhnliche Vorstellen so wenig, wie der"
      ],
      [
        "Mensch im Schlafe von sich weiß.",
        "Von dem logischen Be­stimmtsein beim Bilden von Überzeugungen hat er aber auch nicht ein so volles Bewußtsein wie von dem Inhalte der Überzeugungen selbst.",
        "Wer innerlich wenn auch nur anthropologisch zu beobachten versteht, der wird über die Anwesenheit des logischen Bestimmtseins im gewöhnli­chen Bewußtsein doch einen Begriff bilden können."
      ],
      [
        "Er wird erkennen, daß der Mensch von diesem Bestimmtsein so weiß wie er träumend weiß.",
        "Man kann durchaus die Rich­tigkeit des Paradoxons behaupten: das gewöhnliche Be­wußtsein kennt den Inhalt seiner Überzeugungen; aber es träumt nur von der logischen Gesetzmäßigkeit, die in dem Suchen nach diesen Überzeugungen lebt."
      ],
      [
        "Man sieht: im gewöhnlichen Bewußtsein verschläft man das Wollen, wenn man durch den Leib ein Wollen nach außen entwickelt; man verträumt das Wollen, wenn man im Denken nach Überzeugungen sucht.",
        "Doch erkennt man, daß in letzterem Falle dasjenige, wovon man träumt, kein Leibliches sein kann, denn sonst müßten die logischen Gesetze mit den physiologischen zusammenfallen."
      ],
      [
        "Faßt man den Begriff des im denkenden Suchen nach der Wahrheit lebenden Wollens, so ist dieser Begriff der eines seelisch Wesenhaf­ten. - Man kann aus den beiden Weisen (neben denen an­dere möglich sind), erkenntnistheoretisch sich dem Be­griffe des Seelisch-Wesenhaften, im Sinne der Anthroposo­phie, zu nähern, ersehen, wie scharf dieses Seelisch-Wesenhafte sich absondert von allem, was abnorme Seelentätig­keit ist, wie das visionäre, halluzinatorische, mediale usw.",
        "Wesen."
      ],
      [
        "Denn von all diesem Abnormen muß der Ursprung im physiologisch Bestimmbaren gesucht werden.",
        "Das See­lische der Anthroposophie ist aber nicht nur ein solches,"
      ],
      [
        "das seelisch nach Art des gewöhnlichen gesunden Bewußt­seins erlebt wird, sondern ein solches, an dem in voller wacher Bewußtheit beim Vorstellung-Bilden so erlebt wird, wie man erlebt, wenn man sich an erfahrene Tatsa­chen des Lebens erinnert, oder wie man erlebt beim lo­gisch bedingten Bilden von Überzeugungen.",
        "Man sieht wohl, daß das erkennende Erleben der Anthroposophie in Vorstellungen verläuft, welche den Charakter des gewöhn­lichen von der Außenwelt mit der Wirklichkeit begabten Bewußtseins beibehalten, und zu diesem Fähigkeiten hin­zufügen, die in das Geistgebiet hineinführen; während al­les Visionäre, Halluzinatorische usw. in einem Bewußtsein lebt, das zu dem gewöhnlichen nichts hinzufügt, sondern von ihm Fähigkeiten wegnimmt, so daß der Bewußtseinsstatus unter den Grad heruntersinkt, der in dem bewußten Sinneswahrnehmen vorhanden ist."
      ],
      [
        "Für die Leser meiner Schriften, welche dasjenige kennen, was ich an andern Or­ten über das Gedächtnis und die Erinnerung ausgeführt habe, bemerke ich das Folgende.",
        "Die in das Unbewußte gegangenen Vorstellungen, welche später erinnert werden, hat man, während sie unbewußt bleiben, als Vorstellungen in dem Gliede der menschlichen Wesenheit zu suchen, das in diesen Schriften als Lebensleib (Ätherleib) bezeichnet wird."
      ],
      [
        "Die Tätigkeit aber, durch welche die im Lebensleib verankerten Vorstellungen erinnert werden, gehört dem physischen Leib an.",
        "Ich mache diese Bemerkung, damit nicht mancher «schnellfertig mit dem Urteil» einen Wider­spruch da konstruiert, wo eine durch die Natur der Sache geforderte Unterscheidung notwendig ist."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "2. Das Auftreten der «Erkenntnisgrenzen»",
    "paragraphs": [
      "2. Das Auftreten der «Erkenntnisgrenzen»",
      "Zu Seite 22, Anmerkung zu Zeile 18 von oben",
      "Bei den Denkern, welche mit voller Kraft nach einem Ver­hältnis zur wahren Wirklichkeit streben, wie ein solches durch die innere Natur des Menschen gefordert wird, fin­det man in großer Menge die auf Seite 22 ff. dieser Schrift besprochenen Erkenntnisgrenzen besprochen; und man kann, wenn man die Art dieser Besprechungen ins Auge faßt, sehr wohl bemerken, wie der Anstoß, den echte Den­ker an solchen «Grenzen» erleben, zu der Richtung von innerer Seelenerfahrung drängt, von welcher im ersten Abschnitt dieser Schrift die Rede ist. Man sehe, wie der geistvolle Friedrich Theodor Vischer in dem gehaltvollen Aufsatz, den er über Johannes Volkelts Buch die «Traumphantasie» geschrieben hat, das Erkenntnis-Erlebnis schil­dert, das er an solch einer Grenze empfand: «Kein Geist, wo kein Nerven-Zentrum, wo kein Gehirn, sagen die Geg­ner.",
      "Kein Nerven-Zentrum, kein Gehirn, sagen wir, wenn es nicht von unten auf unzähligen Stufen vorbereitet wäre; es ist leicht, spöttlich von einem Umrumoren des Geistes in Granit und Kalk zu reden, - nicht schwerer, als es uns wäre, spottweise zu fragen, wie sich das Eiweiß im Ge­hirn zu Ideen aufschwinge. Der menschlichen Erkenntnis schwindet die Messung der Stufenunterschiede.",
      "Es wird Geheimnis bleiben, wie es kommt und zugeht, daß die Na­tur, unter welcher doch der Geist schlummern muß, als so vollkommener Gegenschlag des Geistes dasteht, daß wir uns Beulen daran stoßen; es ist eine Diremtion von sol­chem Schein der Absolutheit, daß mit Hegels Anderssein und Außersichsein, so geistreich die Formel, doch so gut",
      "wie nichts gesagt, die Schroffheit der scheinbaren Scheide­wand einfach verdeckt ist. Die richtige Anerkennung der Schneide und des Stoßes in diesem Gegenschlag findet man bei Fichte, aber keine Erklärung dafür» (vergleiche Friedr.",
      "Theodor Vischer: «Altes und Neues», 1881, Erste Abteilung Seite 229 f.). Friedrich Theodor Vischer weist scharf auf einen solchen Punkt hin, wie diejenigen sind, auf die auch Anthroposophie verweisen muß.",
      "Doch ihm kommt nicht zum Bewußtsein, daß in einem solchen Grenzorte des Erkennens eine andere Form des Erkennens eintreten kann. Er möchte mit derselben Art des Erken­nens auch an diesen Grenzen leben, mit der er vor densel­ben auskommt.",
      "Anthroposophie versucht zu zeigen, daß Wissenschaft nicht aufhört, wo sich das gewöhnliche Er­kennen «Beulen» schlägt, wo dieses «Schneiden» und « Stöße» im Gegenschlag der Wirklichkeit findet; sondern daß die Erlebnisse infolge dieser «Beulen», «Schneiden und Stöße» zur Entwickelung eines andersartigen Er­kennens führen, welches den Gegenstoß der Wirklichkeit zur Geistwahrnehmung umbildet, die sich zunächst, auf ihrer ersten Stufe, mit der Tastwahrnehmung des Sinnengebietes vergleichen läßt. - Im dritten Teil von «Altes und Neues» (Seite z24) sagt Friedrich Theodor Vischer: «Gut, eine Seele neben dem Körper gibt es nicht (Vischer meint für den Materialisten); eben das, was wir Materie nennen, wird also auf der uns bekannten höchsten Stufe seiner For­mung, im Gehirn, zu Seele und die Seele entwickelt sich zu Geist. Es gilt, einen Begriff zu vollziehen, der für den tren­nenden Verstand ein reiner Widerspruch ist.» Gegenüber der Vischerschen Ausführung muß wieder die Anthropo­sophie sagen: Gut, für den trennenden Verstand liegt ein",
      "Widerspruch vor; aber für die Seele wird der Widerspruch zum Ausgangspunkt eines Erkennens, vor dem der tren­nende Verstand Halt macht, weil er den «Gegenschlag» der geistigen Wirklichkeit erlebt.",
      "Gideon Spicker, der außer einer Reihe scharfsinniger Schriften auch (1910) das «Philosophische Bekenntnis ei­nes ehemaligen Kapuziners» geschrieben hat, weist mit Worten, die wahrlich eindringlich genug sind, auf einen der Grenzpunkte des gewöhnlichen Erkennens hin (siehe Seite 30 dieses Bekenntnisses): «Zu welcher Philosophie man sich bekenne: ob zur dogmatischen oder skeptischen, empirischen oder transzendentalen, kritischen oder eklek­tischen: alle ohne Ausnahme gehen von einem unbewiese­nen und unbeweisbaren Satz aus, nämlich von der Notwendigkeit des Denkens. Hinter diese Notwendigkeit kommt keine Untersuchung, so tief sie auch schürfen mag, jemals zurück. Sie muß unbedingt angenommen werden und läßt sich durch nichts begründen; jeder Versuch, ihre Richtig­keit beweisen zu wollen, setzt sie immer schon voraus. Un­ter ihr gähnt ein bodenloser Abgrund, eine schauerliche, von keinem Lichtstrahl erhellte Finsternis. Wir wissen also nicht, woher sie kommt, noch auch wohin sie führt. Ob ein gnädiger Gott oder ein böser Dämon sie in die Ver­nunft gelegt, beides ist ungewiß.» Also auch die Betrach­tung des Denkens selbst führt den Denker an einen Grenzort des gewöhnlichen Erkennens. Anthroposophie setzt mit ihrem Erkennen an dem Grenzorte ein; sie weiß, vor der Kunst des verstandesmäßigen Denkens steht die Not­wendigkeit wie eine undurchdringliche Wand. Für das er­lebte Denken schwindet die Undurchdringlichkeit der Wand; dieses erlebte Denken findet ein Licht, um die «von",
      "keinem Lichtstrahl» des nur verstandmäßigen Denkens «erhellte Finsternis» schauend zu erhellen; und der «boden­lose Abgrund» ist ein solcher nur für das Reich des Sinnenseins; wer an diesem Abgrund nicht stehen bleibt, sondern das Wagnis unternimmt, mit dem Denken auch dann wei­ter zu schreiten, wenn dieses ablegen muß, was ihm die Sinneswelt eingefügt hat, der findet in «dem bodenlosen Abgrund» die geistige Wirklichkeit.",
      "Und so könnte fortgefahren werden, ohne absehbares Ende, in der Aufzeigung der Erlebnisse, welche ernste Denker an den «Erkenntnisgrenzen» haben. - Man würde aus solcher Aufzeigung ersehen, daß Anthroposophie als sachgemäßes Ergebnis der Gedanken-Entwickelung der neueren Zeit sich einstellt. Vieles weist auf sie hin, wenn dieses Viele in rechtem Lichte gesehen wird."
    ],
    "sentences": [
      [
        "Das Auftreten der «Erkenntnisgrenzen»"
      ],
      [
        "Zu Seite 22, Anmerkung zu Zeile 18 von oben"
      ],
      [
        "Bei den Denkern, welche mit voller Kraft nach einem Ver­hältnis zur wahren Wirklichkeit streben, wie ein solches durch die innere Natur des Menschen gefordert wird, fin­det man in großer Menge die auf Seite 22 ff. dieser Schrift besprochenen Erkenntnisgrenzen besprochen; und man kann, wenn man die Art dieser Besprechungen ins Auge faßt, sehr wohl bemerken, wie der Anstoß, den echte Den­ker an solchen «Grenzen» erleben, zu der Richtung von innerer Seelenerfahrung drängt, von welcher im ersten Abschnitt dieser Schrift die Rede ist.",
        "Man sehe, wie der geistvolle Friedrich Theodor Vischer in dem gehaltvollen Aufsatz, den er über Johannes Volkelts Buch die «Traumphantasie» geschrieben hat, das Erkenntnis-Erlebnis schil­dert, das er an solch einer Grenze empfand: «Kein Geist, wo kein Nerven-Zentrum, wo kein Gehirn, sagen die Geg­ner."
      ],
      [
        "Kein Nerven-Zentrum, kein Gehirn, sagen wir, wenn es nicht von unten auf unzähligen Stufen vorbereitet wäre; es ist leicht, spöttlich von einem Umrumoren des Geistes in Granit und Kalk zu reden, - nicht schwerer, als es uns wäre, spottweise zu fragen, wie sich das Eiweiß im Ge­hirn zu Ideen aufschwinge.",
        "Der menschlichen Erkenntnis schwindet die Messung der Stufenunterschiede."
      ],
      [
        "Es wird Geheimnis bleiben, wie es kommt und zugeht, daß die Na­tur, unter welcher doch der Geist schlummern muß, als so vollkommener Gegenschlag des Geistes dasteht, daß wir uns Beulen daran stoßen; es ist eine Diremtion von sol­chem Schein der Absolutheit, daß mit Hegels Anderssein und Außersichsein, so geistreich die Formel, doch so gut"
      ],
      [
        "wie nichts gesagt, die Schroffheit der scheinbaren Scheide­wand einfach verdeckt ist.",
        "Die richtige Anerkennung der Schneide und des Stoßes in diesem Gegenschlag findet man bei Fichte, aber keine Erklärung dafür» (vergleiche Friedr."
      ],
      [
        "Theodor Vischer: «Altes und Neues», 1881, Erste Abteilung Seite 229 f.).",
        "Friedrich Theodor Vischer weist scharf auf einen solchen Punkt hin, wie diejenigen sind, auf die auch Anthroposophie verweisen muß."
      ],
      [
        "Doch ihm kommt nicht zum Bewußtsein, daß in einem solchen Grenzorte des Erkennens eine andere Form des Erkennens eintreten kann.",
        "Er möchte mit derselben Art des Erken­nens auch an diesen Grenzen leben, mit der er vor densel­ben auskommt."
      ],
      [
        "Anthroposophie versucht zu zeigen, daß Wissenschaft nicht aufhört, wo sich das gewöhnliche Er­kennen «Beulen» schlägt, wo dieses «Schneiden» und « Stöße» im Gegenschlag der Wirklichkeit findet; sondern daß die Erlebnisse infolge dieser «Beulen», «Schneiden und Stöße» zur Entwickelung eines andersartigen Er­kennens führen, welches den Gegenstoß der Wirklichkeit zur Geistwahrnehmung umbildet, die sich zunächst, auf ihrer ersten Stufe, mit der Tastwahrnehmung des Sinnengebietes vergleichen läßt. - Im dritten Teil von «Altes und Neues» (Seite z24) sagt Friedrich Theodor Vischer: «Gut, eine Seele neben dem Körper gibt es nicht (Vischer meint für den Materialisten); eben das, was wir Materie nennen, wird also auf der uns bekannten höchsten Stufe seiner For­mung, im Gehirn, zu Seele und die Seele entwickelt sich zu Geist.",
        "Es gilt, einen Begriff zu vollziehen, der für den tren­nenden Verstand ein reiner Widerspruch ist.» Gegenüber der Vischerschen Ausführung muß wieder die Anthropo­sophie sagen: Gut, für den trennenden Verstand liegt ein"
      ],
      [
        "Widerspruch vor; aber für die Seele wird der Widerspruch zum Ausgangspunkt eines Erkennens, vor dem der tren­nende Verstand Halt macht, weil er den «Gegenschlag» der geistigen Wirklichkeit erlebt."
      ],
      [
        "Gideon Spicker, der außer einer Reihe scharfsinniger Schriften auch (1910) das «Philosophische Bekenntnis ei­nes ehemaligen Kapuziners» geschrieben hat, weist mit Worten, die wahrlich eindringlich genug sind, auf einen der Grenzpunkte des gewöhnlichen Erkennens hin (siehe Seite 30 dieses Bekenntnisses): «Zu welcher Philosophie man sich bekenne: ob zur dogmatischen oder skeptischen, empirischen oder transzendentalen, kritischen oder eklek­tischen: alle ohne Ausnahme gehen von einem unbewiese­nen und unbeweisbaren Satz aus, nämlich von der Notwendigkeit des Denkens.",
        "Hinter diese Notwendigkeit kommt keine Untersuchung, so tief sie auch schürfen mag, jemals zurück.",
        "Sie muß unbedingt angenommen werden und läßt sich durch nichts begründen; jeder Versuch, ihre Richtig­keit beweisen zu wollen, setzt sie immer schon voraus.",
        "Un­ter ihr gähnt ein bodenloser Abgrund, eine schauerliche, von keinem Lichtstrahl erhellte Finsternis.",
        "Wir wissen also nicht, woher sie kommt, noch auch wohin sie führt.",
        "Ob ein gnädiger Gott oder ein böser Dämon sie in die Ver­nunft gelegt, beides ist ungewiß.» Also auch die Betrach­tung des Denkens selbst führt den Denker an einen Grenzort des gewöhnlichen Erkennens.",
        "Anthroposophie setzt mit ihrem Erkennen an dem Grenzorte ein; sie weiß, vor der Kunst des verstandesmäßigen Denkens steht die Not­wendigkeit wie eine undurchdringliche Wand.",
        "Für das er­lebte Denken schwindet die Undurchdringlichkeit der Wand; dieses erlebte Denken findet ein Licht, um die «von"
      ],
      [
        "keinem Lichtstrahl» des nur verstandmäßigen Denkens «erhellte Finsternis» schauend zu erhellen; und der «boden­lose Abgrund» ist ein solcher nur für das Reich des Sinnenseins; wer an diesem Abgrund nicht stehen bleibt, sondern das Wagnis unternimmt, mit dem Denken auch dann wei­ter zu schreiten, wenn dieses ablegen muß, was ihm die Sinneswelt eingefügt hat, der findet in «dem bodenlosen Abgrund» die geistige Wirklichkeit."
      ],
      [
        "Und so könnte fortgefahren werden, ohne absehbares Ende, in der Aufzeigung der Erlebnisse, welche ernste Denker an den «Erkenntnisgrenzen» haben. - Man würde aus solcher Aufzeigung ersehen, daß Anthroposophie als sachgemäßes Ergebnis der Gedanken-Entwickelung der neueren Zeit sich einstellt.",
        "Vieles weist auf sie hin, wenn dieses Viele in rechtem Lichte gesehen wird."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "3. Von der Abstraktheit der Begriffe",
    "paragraphs": [
      "3. Von der Abstraktheit der Begriffe",
      "Zu Seite 26, Anmerkung zu Zeile 16 von oben",
      "Auf Seite 26 dieser Schrift spreche ich von der «Herablähmung» der Vorstellungen, wenn diese zu Nachbildnern einer sinnenfälligen Wirklichkeit werden. - In dieser «Her­ablähmung» ist die wirkliche Tatsache zu suchen, die dem Verfahren der Abstraktion im Erkenntnisprozeß zugrunde liegt. Der Mensch bildet sich über die sinnenfällige Wirk­lichkeit Begriffe. Für die Erkenntnistheorie entsteht die Frage, wie sich dasjenige, das der Mensch als Begriff von einem wirklichen Wesen oder Vorgang in seiner Seele zu­rückbehält, zu diesem wirklichen Wesen oder Vorgang verhält. Hat dasjenige, was ich in mir als den Begriff eines",
      "Wolfes herumtrage, irgend eine Beziehung zu einer Wirk­lichkeit, oder ist es bloß ein von meiner Seele geformtes Schema, das ich mir gebildet habe, indem ich von demjeni­gen absehe (abstrahiere), was diesem oder jenem Wolfe ei­gentümlich ist, dem aber in der Welt des Wirklichen nichts entspricht. Eine ausgedehnte Betrachtung erfuhr diese Frage in dem mittelalterlichen Streite zwischen Nomina­listen und Realisten.",
      "Für den Nominalisten ist an dem Wolf nur wirklich die an diesem als einzelnem Individuum vor­handenen sichtbaren Stoffe, Fleisch, Blut, Knochen usw. Der Begriff «Wolf» ist «bloß» eine gedankliche Zusam­menfassung der verschiedenen Wölfen gemeinsamen Merkmale.",
      "Der Realist erwidert darauf: irgend ein Stoff, den man am einzelnen Wolf findet, den trifft man auch bei andern Tieren an. Es muß etwas geben, das den Stoff in den lebendigen Zusammenhang hineinordnet, in dem er sich im Wolfe findet.",
      "Dieses ordnende Wirkliche ist durch den Begriff gegeben. - Man wird nun zugeben müssen, daß Vincenz Knauer, der hervorragende Kenner des Aristote­les und der mittelalterlichen Philosophie, in seinem Buche «Die Hauptprobleme der Philosophie» (Wien 1892) bei Besprechung der aristotelischen Erkenntnistheorie (Seite 137) etwas Vortreffliches sagt mit den Worten: «Der Wolf zum Beispiel besteht aus keinen andern materiellen Be­standteilen als das Lamm; seine materielle Leiblichkeit baut sich aus assimiliertem Lammfleisch auf; aber der Wolf wird doch kein Lamm, auch wenn er zeitlebens nichts als Lämmer frißt. Was ihn also zum Wolf macht, das muß selbstverständlich etwas anderes sein als die Hyle, die sinnfällige Mate­rie, und zwar kein bloßes Gedankending muß und kann es sein, obwohl es nur dem Denken, nicht dem Sinne zugängig ist, sondern ein",
      "Wirkendes, also Wirkliches, ein sehr Reales.» Doch wie will man im Sinne einer bloß anthropologischen Betrachtung der Wirklichkeit beikommen, auf die hiemit gedeutet wird? Was durch die Sinne der Seele vermittelt wird, das ergibt nicht den Begriff «Wolf».",
      "Was aber im gewöhnli­chen Bewußtsein als dieser Begriff vorliegt, das ist sicher kein «Wirkendes». Aus der Kraft dieses Begriffes konnte doch gewiß nicht die Zusammenordnung der im Wolfe vereinigten «sinnfälligen» Materien entstehen.",
      "Die Wahr­heit ist, daß Anthropologie mit dieser Frage an einem der Grenzorte ihres Erkennens ist. Anthroposophie zeigt, daß außer der Beziehung des Menschen zum Wolfe, die im «Sinnfälligen» vorhanden ist, noch eine andere besteht.",
      "Diese tritt in ihrer unmittelbaren Eigenart nicht in das ge­wöhnliche Bewußtsein ein. Aber sie besteht als ein lebendi­ger übersinnlicher Zusammenhang zwischen dem Men­schen und dem sinnlich angeschauten Objekte.",
      "Das Lebendige, das im Menschen durch diesen Zusammenhang be­steht, wird durch seine Verstandesorgarisation herabge­lähmt zum «Begriff». Die abstrakte Vorstellung ist das zur Vergegenwärtigung im gewöhnlichen Bewußtsein erstor­bene Wirkliche, in dem der Mensch zwar lebt bei der Sin­neswahrnehmung, das aber in seinem Leben nicht bewußt wird.",
      "Die Abstraktheit von Vorstellungen wird bewirkt durch eine innere Notwendigkeit der Seele. Die Wirklich­keit gibt dem Menschen ein Lebendiges. Er ertötet von diesem Lebendigen denjenigen Teil, der in sein gewöhnli­ches Bewußtsein fällt.",
      "Er vollbringt dieses, weil er an der Außenwelt nicht zum Selbstbewußtsein kommen könnte, wenn er den entsprechenden Zusammenhang mit dieser Außenwelt in seiner vollen Lebendigkeit erfahren müßte.",
      "Ohne die Ablähmung dieser vollen Lebendigkeit müßte sich der Mensch als Glied innerhalb einer über seine menschlichen Grenzen hinausreichenden Einheit erken­nen; er würde Organ eines größeren Organismus sein. Die Art, wie der Mensch seinen Erkenntnisvorgang nach in­nen in die Abstraktheit der Begriffe auslaufen läßt, ist nicht bedingt durch ein außer ihm liegendes Wirkliches, sondern durch die Entwickelungsbedingungen seines eigenen We­sens, welche erfordern, daß er im Wahrnehmungsprozeß den lebendigen Zusammenhang mit der Außenwelt ab­dämpft zu diesen abstrakten Begriffen, welche die Grund­lage bilden, auf der das Selbstbewußtsein erwächst.",
      "Daß dieses so ist, das zeigt sich der Seele nach der Entwicke­lung ihrer Geistorgane. Durch diese wird der lebendige Zusammenhang (in dem Sinne, wie das Seite z6 dieser Schrift dargestellt ist) mit einer außer dem Menschen lie­genden Geist-Wirklichkeit wieder hergestellt; wenn aber das Selbstbewußtsein nicht bereits ein Erworbenes wäre vom gewöhnlichen Bewußtsein her: es könnte im schauen­den Bewußtsein nicht ausgebildet werden.",
      "Man kann hieraus begreifen, daß das gesunde gewöhnliche Bewußtsein die notwendige Voraussetzung für das schauende Bewußt­sein ist. Wer glaubt, ein schauendes Bewußtsein ohne das tätige gesunde gewöhnliche Bewußtsein entwickeln zu können, der irrt gar sehr.",
      "Es muß sogar das gewöhnliche normale Bewußtsein in jedem Augenblicke das schauende Bewußtsein begleiten, weil sonst dies letztere Unordnung in die menschliche Selbstbewußtheit und damit in das Ver­hältnis des Menschen zur Wirklichkeit brächte. Anthropo­sophie kann es bei ihrer schauenden Erkenntnis nur mit einem solchen Bewußtsein, nicht aber mit irgend einer",
      "Herabstimmung des gewöhnlichen Bewußtseins zu tun haben."
    ],
    "sentences": [
      [
        "Von der Abstraktheit der Begriffe"
      ],
      [
        "Zu Seite 26, Anmerkung zu Zeile 16 von oben"
      ],
      [
        "Auf Seite 26 dieser Schrift spreche ich von der «Herablähmung» der Vorstellungen, wenn diese zu Nachbildnern einer sinnenfälligen Wirklichkeit werden. - In dieser «Her­ablähmung» ist die wirkliche Tatsache zu suchen, die dem Verfahren der Abstraktion im Erkenntnisprozeß zugrunde liegt.",
        "Der Mensch bildet sich über die sinnenfällige Wirk­lichkeit Begriffe.",
        "Für die Erkenntnistheorie entsteht die Frage, wie sich dasjenige, das der Mensch als Begriff von einem wirklichen Wesen oder Vorgang in seiner Seele zu­rückbehält, zu diesem wirklichen Wesen oder Vorgang verhält.",
        "Hat dasjenige, was ich in mir als den Begriff eines"
      ],
      [
        "Wolfes herumtrage, irgend eine Beziehung zu einer Wirk­lichkeit, oder ist es bloß ein von meiner Seele geformtes Schema, das ich mir gebildet habe, indem ich von demjeni­gen absehe (abstrahiere), was diesem oder jenem Wolfe ei­gentümlich ist, dem aber in der Welt des Wirklichen nichts entspricht.",
        "Eine ausgedehnte Betrachtung erfuhr diese Frage in dem mittelalterlichen Streite zwischen Nomina­listen und Realisten."
      ],
      [
        "Für den Nominalisten ist an dem Wolf nur wirklich die an diesem als einzelnem Individuum vor­handenen sichtbaren Stoffe, Fleisch, Blut, Knochen usw.",
        "Der Begriff «Wolf» ist «bloß» eine gedankliche Zusam­menfassung der verschiedenen Wölfen gemeinsamen Merkmale."
      ],
      [
        "Der Realist erwidert darauf: irgend ein Stoff, den man am einzelnen Wolf findet, den trifft man auch bei andern Tieren an.",
        "Es muß etwas geben, das den Stoff in den lebendigen Zusammenhang hineinordnet, in dem er sich im Wolfe findet."
      ],
      [
        "Dieses ordnende Wirkliche ist durch den Begriff gegeben. - Man wird nun zugeben müssen, daß Vincenz Knauer, der hervorragende Kenner des Aristote­les und der mittelalterlichen Philosophie, in seinem Buche «Die Hauptprobleme der Philosophie» (Wien 1892) bei Besprechung der aristotelischen Erkenntnistheorie (Seite 137) etwas Vortreffliches sagt mit den Worten: «Der Wolf zum Beispiel besteht aus keinen andern materiellen Be­standteilen als das Lamm; seine materielle Leiblichkeit baut sich aus assimiliertem Lammfleisch auf; aber der Wolf wird doch kein Lamm, auch wenn er zeitlebens nichts als Lämmer frißt.",
        "Was ihn also zum Wolf macht, das muß selbstverständlich etwas anderes sein als die Hyle, die sinnfällige Mate­rie, und zwar kein bloßes Gedankending muß und kann es sein, obwohl es nur dem Denken, nicht dem Sinne zugängig ist, sondern ein"
      ],
      [
        "Wirkendes, also Wirkliches, ein sehr Reales.» Doch wie will man im Sinne einer bloß anthropologischen Betrachtung der Wirklichkeit beikommen, auf die hiemit gedeutet wird?",
        "Was durch die Sinne der Seele vermittelt wird, das ergibt nicht den Begriff «Wolf»."
      ],
      [
        "Was aber im gewöhnli­chen Bewußtsein als dieser Begriff vorliegt, das ist sicher kein «Wirkendes».",
        "Aus der Kraft dieses Begriffes konnte doch gewiß nicht die Zusammenordnung der im Wolfe vereinigten «sinnfälligen» Materien entstehen."
      ],
      [
        "Die Wahr­heit ist, daß Anthropologie mit dieser Frage an einem der Grenzorte ihres Erkennens ist.",
        "Anthroposophie zeigt, daß außer der Beziehung des Menschen zum Wolfe, die im «Sinnfälligen» vorhanden ist, noch eine andere besteht."
      ],
      [
        "Diese tritt in ihrer unmittelbaren Eigenart nicht in das ge­wöhnliche Bewußtsein ein.",
        "Aber sie besteht als ein lebendi­ger übersinnlicher Zusammenhang zwischen dem Men­schen und dem sinnlich angeschauten Objekte."
      ],
      [
        "Das Lebendige, das im Menschen durch diesen Zusammenhang be­steht, wird durch seine Verstandesorgarisation herabge­lähmt zum «Begriff».",
        "Die abstrakte Vorstellung ist das zur Vergegenwärtigung im gewöhnlichen Bewußtsein erstor­bene Wirkliche, in dem der Mensch zwar lebt bei der Sin­neswahrnehmung, das aber in seinem Leben nicht bewußt wird."
      ],
      [
        "Die Abstraktheit von Vorstellungen wird bewirkt durch eine innere Notwendigkeit der Seele.",
        "Die Wirklich­keit gibt dem Menschen ein Lebendiges.",
        "Er ertötet von diesem Lebendigen denjenigen Teil, der in sein gewöhnli­ches Bewußtsein fällt."
      ],
      [
        "Er vollbringt dieses, weil er an der Außenwelt nicht zum Selbstbewußtsein kommen könnte, wenn er den entsprechenden Zusammenhang mit dieser Außenwelt in seiner vollen Lebendigkeit erfahren müßte."
      ],
      [
        "Ohne die Ablähmung dieser vollen Lebendigkeit müßte sich der Mensch als Glied innerhalb einer über seine menschlichen Grenzen hinausreichenden Einheit erken­nen; er würde Organ eines größeren Organismus sein.",
        "Die Art, wie der Mensch seinen Erkenntnisvorgang nach in­nen in die Abstraktheit der Begriffe auslaufen läßt, ist nicht bedingt durch ein außer ihm liegendes Wirkliches, sondern durch die Entwickelungsbedingungen seines eigenen We­sens, welche erfordern, daß er im Wahrnehmungsprozeß den lebendigen Zusammenhang mit der Außenwelt ab­dämpft zu diesen abstrakten Begriffen, welche die Grund­lage bilden, auf der das Selbstbewußtsein erwächst."
      ],
      [
        "Daß dieses so ist, das zeigt sich der Seele nach der Entwicke­lung ihrer Geistorgane.",
        "Durch diese wird der lebendige Zusammenhang (in dem Sinne, wie das Seite z6 dieser Schrift dargestellt ist) mit einer außer dem Menschen lie­genden Geist-Wirklichkeit wieder hergestellt; wenn aber das Selbstbewußtsein nicht bereits ein Erworbenes wäre vom gewöhnlichen Bewußtsein her: es könnte im schauen­den Bewußtsein nicht ausgebildet werden."
      ],
      [
        "Man kann hieraus begreifen, daß das gesunde gewöhnliche Bewußtsein die notwendige Voraussetzung für das schauende Bewußt­sein ist.",
        "Wer glaubt, ein schauendes Bewußtsein ohne das tätige gesunde gewöhnliche Bewußtsein entwickeln zu können, der irrt gar sehr."
      ],
      [
        "Es muß sogar das gewöhnliche normale Bewußtsein in jedem Augenblicke das schauende Bewußtsein begleiten, weil sonst dies letztere Unordnung in die menschliche Selbstbewußtheit und damit in das Ver­hältnis des Menschen zur Wirklichkeit brächte.",
        "Anthropo­sophie kann es bei ihrer schauenden Erkenntnis nur mit einem solchen Bewußtsein, nicht aber mit irgend einer"
      ],
      [
        "Herabstimmung des gewöhnlichen Bewußtseins zu tun haben."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "4. Ein wichtiges Merkmal der Geist-Wahrnebmung",
    "paragraphs": [
      "4. Ein wichtiges Merkmal der Geist-Wahrnebmung",
      "Zu Seite 29, Anmerkung zu Zelle 14 von oben",
      "Die Wahrnehmungen, welche die Seele im Bereiche der gei­stigen Wirklichkeit macht, leben in dieser nicht in der glei­chen Art fort wie die Vorstellungen, die an sinnlichen Wahr­nehmungen gewonnen werden. Obgleich im Sinne des er­sten Kapitels dieser «Skizzenhaften Erweiterungen des In­haltes dieser Schrift» ein Vergleich dieser Wahrnehmungen mit den Erinnerungsvorstellungen möglich ist, so verhal­ten sich die ersteren in der Seele doch nicht wie die letzteren. Was als geistige Wahrnehmung erlebt wird, kann nämlich in dieser seiner unmittelbaren Gestalt nicht wie eine Erinne­rungsvorstellung in der Seele behalten werden. Soll man dieselbe geistige Wahrnehmung erneut wieder haben, so muß sie auch erneut in der Seele wieder hergestellt werden. Das heißt, es muß die Beziehung der Seele zu der entspre­chenden geistigen Wirklichkeit wieder gesucht werden. Und diese Wieder-Erneuerung läßt sich nicht mit einem Er­innern an einen Sinneseindruck vergleichen, sondern nur mit dem Vor-Augen-Führen desselben sinnenfälligen Ob­jektes, das man bei einem früheren Eindruck gehabt hat. Was von der realen geistigen Wahrnehmung unmittelbar in der Erinnerung behalten werden kann, ist nicht diese selbst, sondern die Verrichtung der Seele, durch die man zu der entsprechenden Wahrnehmung gelangt. Strebe ich danach, eine geistige Wahrnehmung, die ich vor einiger Zeit gehabt",
      "habe, wieder zu haben, so sollte ich nicht nach der Erinne­rung dieser Wahrnehmung suchen, sondern nach der Erin­nerung, die mir die Vorbereitungen meiner Seele zurück­ruft, welche mich zu der Wahrnehmung geführt haben. Die Wahrnehmung stellt sich dann durch einen von mir unab­hängigen Vorgang ein. Es ist wichtig, vollbewußt sich zu sein dieser Zweiheit des Vorganges, weil man nur dadurch eine richtige Erkenntnis von dem erlangt, was wirklich geistig objektiv ist. - In der Praxis ist aber das Wesen dieser Zweiheit dadurch modifiziert, daß der Inhalt des geistigen Wahrnehmens aus dem schauenden Bewußtsein in das gewöhnliche Bewußtsein übertragen werden kann. Dann wird er in dem letztern zu einer abstrakten Vorstellung. Und diese kann in der gewöhnlichen Art erinnert werden. - Man kann aber gerade dadurch für ein richtiges bewußtes Verhältnis der Seele zur geistigen Welt viel gewinnen, daß man sich sorgfältig übt für die Erkenntnis der innerhalb des See­lenlebens mit einer gewissen Feinheit auftretenden Unter­schiede: 1. Seelenvorgänge, welche zu einer geistigen Wahrnehmung führen; 2. geistige Wahrnehmungen selbst; 3. in Begriffe des gewöhnlichen Bewußtseins umgesetzte geistige Wahrnehmungen."
    ],
    "sentences": [
      [
        "Ein wichtiges Merkmal der Geist-Wahrnebmung"
      ],
      [
        "Zu Seite 29, Anmerkung zu Zelle 14 von oben"
      ],
      [
        "Die Wahrnehmungen, welche die Seele im Bereiche der gei­stigen Wirklichkeit macht, leben in dieser nicht in der glei­chen Art fort wie die Vorstellungen, die an sinnlichen Wahr­nehmungen gewonnen werden.",
        "Obgleich im Sinne des er­sten Kapitels dieser «Skizzenhaften Erweiterungen des In­haltes dieser Schrift» ein Vergleich dieser Wahrnehmungen mit den Erinnerungsvorstellungen möglich ist, so verhal­ten sich die ersteren in der Seele doch nicht wie die letzteren.",
        "Was als geistige Wahrnehmung erlebt wird, kann nämlich in dieser seiner unmittelbaren Gestalt nicht wie eine Erinne­rungsvorstellung in der Seele behalten werden.",
        "Soll man dieselbe geistige Wahrnehmung erneut wieder haben, so muß sie auch erneut in der Seele wieder hergestellt werden.",
        "Das heißt, es muß die Beziehung der Seele zu der entspre­chenden geistigen Wirklichkeit wieder gesucht werden.",
        "Und diese Wieder-Erneuerung läßt sich nicht mit einem Er­innern an einen Sinneseindruck vergleichen, sondern nur mit dem Vor-Augen-Führen desselben sinnenfälligen Ob­jektes, das man bei einem früheren Eindruck gehabt hat.",
        "Was von der realen geistigen Wahrnehmung unmittelbar in der Erinnerung behalten werden kann, ist nicht diese selbst, sondern die Verrichtung der Seele, durch die man zu der entsprechenden Wahrnehmung gelangt.",
        "Strebe ich danach, eine geistige Wahrnehmung, die ich vor einiger Zeit gehabt"
      ],
      [
        "habe, wieder zu haben, so sollte ich nicht nach der Erinne­rung dieser Wahrnehmung suchen, sondern nach der Erin­nerung, die mir die Vorbereitungen meiner Seele zurück­ruft, welche mich zu der Wahrnehmung geführt haben.",
        "Die Wahrnehmung stellt sich dann durch einen von mir unab­hängigen Vorgang ein.",
        "Es ist wichtig, vollbewußt sich zu sein dieser Zweiheit des Vorganges, weil man nur dadurch eine richtige Erkenntnis von dem erlangt, was wirklich geistig objektiv ist. - In der Praxis ist aber das Wesen dieser Zweiheit dadurch modifiziert, daß der Inhalt des geistigen Wahrnehmens aus dem schauenden Bewußtsein in das gewöhnliche Bewußtsein übertragen werden kann.",
        "Dann wird er in dem letztern zu einer abstrakten Vorstellung.",
        "Und diese kann in der gewöhnlichen Art erinnert werden. - Man kann aber gerade dadurch für ein richtiges bewußtes Verhältnis der Seele zur geistigen Welt viel gewinnen, daß man sich sorgfältig übt für die Erkenntnis der innerhalb des See­lenlebens mit einer gewissen Feinheit auftretenden Unter­schiede: 1.",
        "Seelenvorgänge, welche zu einer geistigen Wahrnehmung führen; 2. geistige Wahrnehmungen selbst; 3. in Begriffe des gewöhnlichen Bewußtseins umgesetzte geistige Wahrnehmungen."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "5.    Über die wirkliche Grundlage der intenlionalen Beziehung",
    "paragraphs": [
      "5.    Über die wirkliche Grundlage der intenlionalen Beziehung",
      "Zu Seile 88, Anmerkung zu Zeile 20 von oben",
      "Mit der in der vorliegenden Schrift (3. Kapitel über Franz Brentano) charakterisierten «intentionalen Beziehung» tritt in Brentanos Psychologie ein Seelisches nur als Tatbestand des gewöhnlichen Bewußtseins auf, ohne daß dieser Tatbestand",
      "weiter in das seelische Erleben erklärend eingeglie­dert wird. Ich möchte mir nun hier gestatten, über diesen Tatbestand einiges skizzenhaft vorzubringen, das bei mir in durchgearbeiteten Anschauungen nach den verschiedensten Richtungen hin begründet ist. Diese Anschauungen verlangen allerdings, daß sie auch noch in ausführlicherer Gestalt - mit allen Begründungen - gegeben werden. Doch haben mir die Verhältnisse bisher nur möglich gemacht, manches Einschlägige in mündlichen Vorträgen vorzubrin­gen. Was ich hier anführen kann, sind Ergebnisse in kurzer skizzenhafter Darstellung. Und ich bitte den Leser, sie vor­läufig als solche aufzunehmen. Es handelt sich nicht um «Einfälle», sondern um etwas, dessen Begründung mit den wissenschaftlichen Mitteln der Gegenwart von mir in jahre­langer Arbeit versucht worden ist.",
      "Bei demjenigen Seelen-Erleben, das von Franz Brentano als Urteilen bezeichnet wird, kommt zu dem bloßen Vorstel­len, das in einem inneren Bildgestalten besteht, ein Aner­kennen oder Verwerfen der Vorstellungsbilder hinzu. Es entsteht für den Seelenforscher die Frage: was ist im seeli­schen Erleben dasjenige, wodurch nicht bloß das Vorstel­lungsbild: «grüner Baum», sondern das Urteil: «es ist ein grüner Baum» zustande kommt? Innerhalb des engeren Kreises des Vorstellungslebens, den man im gewöhnlichen Bewußtsein umschreibt, kann dieses «Etwas» nicht liegen. Daß man es hier nicht finden kann, hat zu denjenigen er­kenntnistheoretischen Gedanken geführt, welche ich im zweiten Bande meiner «Rätsel der Philosophie» in dem Abschnitte: «Die Welt als Illusion» dargestellt habe. Es han­delt sich dabei um ein Erlebnis, das außerhalb dieses Kreises liegt. Es kommt darauf an, das «Wo» im Bereich der seeli­schen",
      "Erlebnisse zu finden. - Steht der Mensch in wahrneh­mender Tätigkeit einem Sinnesobjekt gegenüber, so kann dieses «Etwas»in alledem nicht gefunden werden, was der Mensch in dem Wahrnehmungsvorgange so empfängt, daß dieses Empfangen durch die physiologischen und psycho­logischen Vorstellungen erfaßt wird, welche sich auf das äußere Objekt einerseits und den unmittelbar in Betracht kommenden Sinn anderseits beziehen. Hat jemand die Seh-­Wahrnehmung «grüner Baum», so kann der Tatbestand des Urteiles «es ist ein grüner Baum» nicht in der physiolo­gisch oder psychologisch unmittelbar aufzeigbaren Bezie­hung zwischen «Baum» und «Auge» gefunden werden.",
      "Was in der Seele als solcher innerer Tatbestand des Urteilens erlebt wird, ist eben noch eine andere Beziehung zwischen dem «Menschen» und «dem Baum» als diejenige ist zwi­schen dem «Baum» und dem «Auge». Doch wird nur die letztere Beziehung in dem gewöhnlichen Bewußtsein mit voller Schärfe erlebt.",
      "Die andere Beziehung bleibt in einem dumpfen Unterbewußtsein und tritt nur in dem Ergebnis zu­tage, das in der Anerkennung des «grünen Baumes» als eines Seienden liegt. Man hat es bei jeder Wahrnehmung, die auf ein Urteil sich zuspitzt, mit einer Doppelbeziehung des Men­schen zu der Objektivität zu tun. - Einsicht in diese Doppelbeziehung gewinnt man nur, wenn man die gegenwärtig vorhandene fragmentarische Sinnes-Lehre durch eine voll­ständige ersetzt.",
      "Wer alles in Betracht zieht, was zur Charak­teristik eines menschlichen Sinnes in Betracht kommt, der findet, daß man noch anderes «Sinne» nennen muß als was man gewöhnlich so bezeichnet. Was das «Auge» zum «Sinn» macht, ist zum Beispiel auch dann vorhanden, wenn man den Tatbestand erlebt: «es wird ein anderes beobachtet»,",
      "oder «es wird ein menschlicher Gedanke eines an­deren als solcher erkannt». Man macht gegenüber solchen Tatbeständen gewöhnlich den Fehler, daß man eine durch­aus berechtigte und notwendige Unterscheidung nicht voll­zieht.",
      "Man glaubt zum Beispiel, man käme damit aus, wenn man die Worte eines anderen hört, nur insoferne von «Sinn» zu sprechen, daß als solcher nur das «Gehör» in Frage kommt, und alles andere einer nicht-sinnlichen inneren Tä­tigkeit zuzuschreiben sei. So liegt aber die Sache nicht.",
      "Beim Hören menschlicher Worte und deren Verstehen als Gedan­ken kommt eine dreifache Tätigkeit in Betracht. Und jedes Glied dieser dreifachen Tätigkeit muß für sich betrachtet werden, wenn eine berechtigte wissenschaftliche Auffas­sung zustande kommen soll.",
      "Das «Hören»ist die eine Tä­tigkeit. Allein das «Hören»ist für sich ebenso wenig ein «Vernehmen von Worten» wie das «Tasten» ein «Sehen» ist. Und wie man sachgemäß unterscheiden muß zwischen dem Sinn des «Tastens» und demjenigen des «Sehens», so zwischen dem des «Hörens» und dem des «Vernehmens von Worten» und dem weiteren des «Erfassens von Gedan­ken».",
      "Es führt zu einer mangelhaften Psychologie und auch zu einer mangelhaften Erkenntnistheorie, wenn man das «Erfassen von Gedanken» nicht scharf von der Denktätig­keit absondert und den sinnesgemäßen Charakter des er­steren erkennt. Man begeht diesen Fehler nur deshalb, weil das Organ des «Vernehmens von Worten» und dasjenige des «Erfassens von Gedanken» nicht so äußerlich wahr­nehmbar sind als das Ohr für das «Hören».",
      "In Wirklichkeit sind für die beiden Wahrnehmungstätigkeiten ebenso «Or­gane» vorhanden, wie für das «Hören» das Ohr. - Führt man durch, was Physiologie und Psychologie bei einer vollständigen",
      "Betrachtung in dieser Beziehung ergeben, so ge­langt man zur folgenden Anschauung über die menschliche Sinnes-Organisation. Man muß unterscheiden: den Sinn für die «Ich-Wahrnehmung» des andern Menschen; den Sinn für «Gedanken-Erfassung»; den Sinn für «Verneh­men von Worten»; den Gehörsinn; den Wärmesinn; den Sehsinn; den Geschmacksinn; den Geruchsinn; den Gleich­gewichtssinn (das wahrnehmende Erleben des sich in einer gewissen Gleichgewichtslage-Befindens gegenüber der Au­ßenwelt); den Bewegungssinn (das wahrnehmende Erleben der Ruhe und Bewegung der eigenen Glieder einerseits, oder des Ruhens oder sich Bewegens gegenüber der Außenwelt andrerseits); den Lebenssinn (das Erleben der Verfas­sung im Organismus; Gefühl von dem subjektiven Sich-Befinden); den Tastsinn.",
      "Alle diese «Sinne» tragen die Merkmale in sich, wegen deren man «Auge» und «Ohr» in Wahrheit «Sinne» nennt. - Wer die Berechtigung einer sol­chen Unterscheidung nicht anerkennt, der gerät mit seiner Erkenntnis gegenüber der Wirklichkeit in Unordnung. Er verfällt mit seinen Vorstellungen dem Schicksal, daß sie ihn kein wahrhaft Wirkliches erleben lassen.",
      "Wer zum Beispiel das «Auge» einen «Sinn» nennt und keinen «Sinn» annimmt für das «Vernehmen von Worten», für den bleibt auch die Vorstellung, die er sich vom «Auge» bildet, ein unwirkliches Gebilde. - Ich bin der Meinung, daß Fritz Mauthner in seiner geistreichen Art - in seinen sprachkriti­schen Werken - nur deshalb von «Zufallssinnen» spricht, weil er bloß eine fragmentarische Sinnes-Lehre im Auge hat. Wäre dies nicht der Fall, so würde er bemerken, wie der «Sinn» sich in die «Wirklichkeit» hineinstellt. - Nun liegt, wenn der Mensch einem Sinnes-Objekte gegenübersteht,",
      "die Sache so, daß er niemals bloß durch einen Sinn einen Ein­druck erhält, sondern außerdem immer noch durch wenig­stens einen andern aus der Reihe der oben angeführten. Die Be­ziehung zu einem Sinne tritt mit besonderer Schärfe in das gewöhnliche Bewußtsein; die andere bleibt dumpfer.",
      "Es be­steht aber zwischen den Sinnen der Unterschied, daß eine Anzahl der selben die Beziehung zur Außenwelt mehr als eine äußerliche erleben läßt; die andere mehr als etwas, was mit dem Eigen-Sein in engster Verknüpfung ist. Sinne, die mit dem Eigensein in engster Verknüpfung sich befinden, sind zum Beispiel der Gleichgewichtssinn, der Bewegungssinn, der Lebenssinn, ja auch der Tastsinn.",
      "In den Wahrneh­mungen solcher Sinne gegenüber der Außenwelt wird stets das eigene Sein dumpf mitempfunden. Ja, man kann sagen, es tritt eine Dumpfheit des bewußten Wahrnehmens eben deshalb ein, weil die Beziehung nach außen von dem Erle­ben des Eigen-Seins übertönt wird.",
      "Ereignet sich zum Bei­spiel, daß ein Gegenstand gesehen wird, und zugleich der Gleichgewichtssinn einen Eindruck vermittelt, so wird scharf wahrgenommen das Gesehene. Dieses Gesehene führt zu der Vorstellung des Gegenstandes.",
      "Das Erlebnis durch den Gleichgewichtssinn bleibt als Wahrnehmung dumpf; jedoch es lebt auf in dem Urteile: «das Gesehene ist» oder «es ist das Gesehene». - Im Wirklichen stehen die Dinge nicht in abstrakten Unterschieden nebeneinander, sondern sie gehen mit ihren Merkmalen in einander über. So kommt es, daß in der vollständigen Reihe der «Sinne» solche sind, die weniger die Beziehung zur Außenwelt, son­dern mehr das Erleben des Eigen-Seins vermitteln.",
      "Diese letzteren tauchen mehr in das innere seelische Leben ein als zum Beispiel Auge und Ohr; dadurch erscheint das Ergebnis",
      "ihrer Wahrnehmungs-Vermittelung als inneres seeli­sches Erlebnis. Aber man sollte auch bei ihnen das eigent­lich Seelische von dem Wahrnehmungselemente so unter­scheiden, wie man zum Beispiel beim Gesehenen den äuße­ren Tatbestand von dem an ihm gemachten inneren Seelen-Erlebnisse unterscheidet. - Für denjenigen, der sich auf den anthroposophischen Gesichtspunkt stellt, darf kein Zu­rückschrecken bestehen vor solchen feinen Vorstellungs-Unterscheidungen, wie sie hier gemacht werden.",
      "Er muß das «Vernehmen der Worte» von dem Gehör einerseits, und dieses «Vernehmen der Worte» von dem durch die ei­genen Gedanken vermittelten «Verstehen der Worte» so unterscheiden können, wie das gewöhnliche Bewußtsein unterscheidet zwischen einem Baum und einem Felsblock. Würde dies mehr berücksichtigt, so würde man erkennen, daß die Anthroposophie nicht nur die eine Seite hat, welche man gewöhnlich als eine mystische bezeichnet, sondern auch die andere, durch die sie nicht zu einer weniger wissen­schaftlichen Forschung führt als die Naturwissenschaft, sondern zu einer mehr wissenschaftlichen, die eine feinere, methodischere Ausarbeitung des Vorstellenslebens nötig macht als selbst die gewöhnliche Philosophie.",
      "Ich glaube, daß Wilhelm Dilthey mit seinen philosophischen Forschun­gen auf dem Wege war zu derjenigen Sinnes-Lehre, die ich hier skizziert habe, daß er aber nicht zu einem Ziele kom­men konnte, weil er nicht durchdrang bis zu einer völligen Ausarbeitung der in Frage kommenden Vorstellungen. Vergleiche auch, was ich darüber im zweiten Bande meiner «Rätsel der Philosophie» gesagt habe, 7.",
      "Auflage, Seiten 567-572.)"
    ],
    "sentences": [
      [
        "Über die wirkliche Grundlage der intenlionalen Beziehung"
      ],
      [
        "Zu Seile 88, Anmerkung zu Zeile 20 von oben"
      ],
      [
        "Mit der in der vorliegenden Schrift (3.",
        "Kapitel über Franz Brentano) charakterisierten «intentionalen Beziehung» tritt in Brentanos Psychologie ein Seelisches nur als Tatbestand des gewöhnlichen Bewußtseins auf, ohne daß dieser Tatbestand"
      ],
      [
        "weiter in das seelische Erleben erklärend eingeglie­dert wird.",
        "Ich möchte mir nun hier gestatten, über diesen Tatbestand einiges skizzenhaft vorzubringen, das bei mir in durchgearbeiteten Anschauungen nach den verschiedensten Richtungen hin begründet ist.",
        "Diese Anschauungen verlangen allerdings, daß sie auch noch in ausführlicherer Gestalt - mit allen Begründungen - gegeben werden.",
        "Doch haben mir die Verhältnisse bisher nur möglich gemacht, manches Einschlägige in mündlichen Vorträgen vorzubrin­gen.",
        "Was ich hier anführen kann, sind Ergebnisse in kurzer skizzenhafter Darstellung.",
        "Und ich bitte den Leser, sie vor­läufig als solche aufzunehmen.",
        "Es handelt sich nicht um «Einfälle», sondern um etwas, dessen Begründung mit den wissenschaftlichen Mitteln der Gegenwart von mir in jahre­langer Arbeit versucht worden ist."
      ],
      [
        "Bei demjenigen Seelen-Erleben, das von Franz Brentano als Urteilen bezeichnet wird, kommt zu dem bloßen Vorstel­len, das in einem inneren Bildgestalten besteht, ein Aner­kennen oder Verwerfen der Vorstellungsbilder hinzu.",
        "Es entsteht für den Seelenforscher die Frage: was ist im seeli­schen Erleben dasjenige, wodurch nicht bloß das Vorstel­lungsbild: «grüner Baum», sondern das Urteil: «es ist ein grüner Baum» zustande kommt?",
        "Innerhalb des engeren Kreises des Vorstellungslebens, den man im gewöhnlichen Bewußtsein umschreibt, kann dieses «Etwas» nicht liegen.",
        "Daß man es hier nicht finden kann, hat zu denjenigen er­kenntnistheoretischen Gedanken geführt, welche ich im zweiten Bande meiner «Rätsel der Philosophie» in dem Abschnitte: «Die Welt als Illusion» dargestellt habe.",
        "Es han­delt sich dabei um ein Erlebnis, das außerhalb dieses Kreises liegt.",
        "Es kommt darauf an, das «Wo» im Bereich der seeli­schen"
      ],
      [
        "Erlebnisse zu finden. - Steht der Mensch in wahrneh­mender Tätigkeit einem Sinnesobjekt gegenüber, so kann dieses «Etwas»in alledem nicht gefunden werden, was der Mensch in dem Wahrnehmungsvorgange so empfängt, daß dieses Empfangen durch die physiologischen und psycho­logischen Vorstellungen erfaßt wird, welche sich auf das äußere Objekt einerseits und den unmittelbar in Betracht kommenden Sinn anderseits beziehen.",
        "Hat jemand die Seh-­Wahrnehmung «grüner Baum», so kann der Tatbestand des Urteiles «es ist ein grüner Baum» nicht in der physiolo­gisch oder psychologisch unmittelbar aufzeigbaren Bezie­hung zwischen «Baum» und «Auge» gefunden werden."
      ],
      [
        "Was in der Seele als solcher innerer Tatbestand des Urteilens erlebt wird, ist eben noch eine andere Beziehung zwischen dem «Menschen» und «dem Baum» als diejenige ist zwi­schen dem «Baum» und dem «Auge».",
        "Doch wird nur die letztere Beziehung in dem gewöhnlichen Bewußtsein mit voller Schärfe erlebt."
      ],
      [
        "Die andere Beziehung bleibt in einem dumpfen Unterbewußtsein und tritt nur in dem Ergebnis zu­tage, das in der Anerkennung des «grünen Baumes» als eines Seienden liegt.",
        "Man hat es bei jeder Wahrnehmung, die auf ein Urteil sich zuspitzt, mit einer Doppelbeziehung des Men­schen zu der Objektivität zu tun. - Einsicht in diese Doppelbeziehung gewinnt man nur, wenn man die gegenwärtig vorhandene fragmentarische Sinnes-Lehre durch eine voll­ständige ersetzt."
      ],
      [
        "Wer alles in Betracht zieht, was zur Charak­teristik eines menschlichen Sinnes in Betracht kommt, der findet, daß man noch anderes «Sinne» nennen muß als was man gewöhnlich so bezeichnet.",
        "Was das «Auge» zum «Sinn» macht, ist zum Beispiel auch dann vorhanden, wenn man den Tatbestand erlebt: «es wird ein anderes beobachtet»,"
      ],
      [
        "oder «es wird ein menschlicher Gedanke eines an­deren als solcher erkannt».",
        "Man macht gegenüber solchen Tatbeständen gewöhnlich den Fehler, daß man eine durch­aus berechtigte und notwendige Unterscheidung nicht voll­zieht."
      ],
      [
        "Man glaubt zum Beispiel, man käme damit aus, wenn man die Worte eines anderen hört, nur insoferne von «Sinn» zu sprechen, daß als solcher nur das «Gehör» in Frage kommt, und alles andere einer nicht-sinnlichen inneren Tä­tigkeit zuzuschreiben sei.",
        "So liegt aber die Sache nicht."
      ],
      [
        "Beim Hören menschlicher Worte und deren Verstehen als Gedan­ken kommt eine dreifache Tätigkeit in Betracht.",
        "Und jedes Glied dieser dreifachen Tätigkeit muß für sich betrachtet werden, wenn eine berechtigte wissenschaftliche Auffas­sung zustande kommen soll."
      ],
      [
        "Das «Hören»ist die eine Tä­tigkeit.",
        "Allein das «Hören»ist für sich ebenso wenig ein «Vernehmen von Worten» wie das «Tasten» ein «Sehen» ist.",
        "Und wie man sachgemäß unterscheiden muß zwischen dem Sinn des «Tastens» und demjenigen des «Sehens», so zwischen dem des «Hörens» und dem des «Vernehmens von Worten» und dem weiteren des «Erfassens von Gedan­ken»."
      ],
      [
        "Es führt zu einer mangelhaften Psychologie und auch zu einer mangelhaften Erkenntnistheorie, wenn man das «Erfassen von Gedanken» nicht scharf von der Denktätig­keit absondert und den sinnesgemäßen Charakter des er­steren erkennt.",
        "Man begeht diesen Fehler nur deshalb, weil das Organ des «Vernehmens von Worten» und dasjenige des «Erfassens von Gedanken» nicht so äußerlich wahr­nehmbar sind als das Ohr für das «Hören»."
      ],
      [
        "In Wirklichkeit sind für die beiden Wahrnehmungstätigkeiten ebenso «Or­gane» vorhanden, wie für das «Hören» das Ohr. - Führt man durch, was Physiologie und Psychologie bei einer vollständigen"
      ],
      [
        "Betrachtung in dieser Beziehung ergeben, so ge­langt man zur folgenden Anschauung über die menschliche Sinnes-Organisation.",
        "Man muß unterscheiden: den Sinn für die «Ich-Wahrnehmung» des andern Menschen; den Sinn für «Gedanken-Erfassung»; den Sinn für «Verneh­men von Worten»; den Gehörsinn; den Wärmesinn; den Sehsinn; den Geschmacksinn; den Geruchsinn; den Gleich­gewichtssinn (das wahrnehmende Erleben des sich in einer gewissen Gleichgewichtslage-Befindens gegenüber der Au­ßenwelt); den Bewegungssinn (das wahrnehmende Erleben der Ruhe und Bewegung der eigenen Glieder einerseits, oder des Ruhens oder sich Bewegens gegenüber der Außenwelt andrerseits); den Lebenssinn (das Erleben der Verfas­sung im Organismus; Gefühl von dem subjektiven Sich-Befinden); den Tastsinn."
      ],
      [
        "Alle diese «Sinne» tragen die Merkmale in sich, wegen deren man «Auge» und «Ohr» in Wahrheit «Sinne» nennt. - Wer die Berechtigung einer sol­chen Unterscheidung nicht anerkennt, der gerät mit seiner Erkenntnis gegenüber der Wirklichkeit in Unordnung.",
        "Er verfällt mit seinen Vorstellungen dem Schicksal, daß sie ihn kein wahrhaft Wirkliches erleben lassen."
      ],
      [
        "Wer zum Beispiel das «Auge» einen «Sinn» nennt und keinen «Sinn» annimmt für das «Vernehmen von Worten», für den bleibt auch die Vorstellung, die er sich vom «Auge» bildet, ein unwirkliches Gebilde. - Ich bin der Meinung, daß Fritz Mauthner in seiner geistreichen Art - in seinen sprachkriti­schen Werken - nur deshalb von «Zufallssinnen» spricht, weil er bloß eine fragmentarische Sinnes-Lehre im Auge hat.",
        "Wäre dies nicht der Fall, so würde er bemerken, wie der «Sinn» sich in die «Wirklichkeit» hineinstellt. - Nun liegt, wenn der Mensch einem Sinnes-Objekte gegenübersteht,"
      ],
      [
        "die Sache so, daß er niemals bloß durch einen Sinn einen Ein­druck erhält, sondern außerdem immer noch durch wenig­stens einen andern aus der Reihe der oben angeführten.",
        "Die Be­ziehung zu einem Sinne tritt mit besonderer Schärfe in das gewöhnliche Bewußtsein; die andere bleibt dumpfer."
      ],
      [
        "Es be­steht aber zwischen den Sinnen der Unterschied, daß eine Anzahl der selben die Beziehung zur Außenwelt mehr als eine äußerliche erleben läßt; die andere mehr als etwas, was mit dem Eigen-Sein in engster Verknüpfung ist.",
        "Sinne, die mit dem Eigensein in engster Verknüpfung sich befinden, sind zum Beispiel der Gleichgewichtssinn, der Bewegungssinn, der Lebenssinn, ja auch der Tastsinn."
      ],
      [
        "In den Wahrneh­mungen solcher Sinne gegenüber der Außenwelt wird stets das eigene Sein dumpf mitempfunden.",
        "Ja, man kann sagen, es tritt eine Dumpfheit des bewußten Wahrnehmens eben deshalb ein, weil die Beziehung nach außen von dem Erle­ben des Eigen-Seins übertönt wird."
      ],
      [
        "Ereignet sich zum Bei­spiel, daß ein Gegenstand gesehen wird, und zugleich der Gleichgewichtssinn einen Eindruck vermittelt, so wird scharf wahrgenommen das Gesehene.",
        "Dieses Gesehene führt zu der Vorstellung des Gegenstandes."
      ],
      [
        "Das Erlebnis durch den Gleichgewichtssinn bleibt als Wahrnehmung dumpf; jedoch es lebt auf in dem Urteile: «das Gesehene ist» oder «es ist das Gesehene». - Im Wirklichen stehen die Dinge nicht in abstrakten Unterschieden nebeneinander, sondern sie gehen mit ihren Merkmalen in einander über.",
        "So kommt es, daß in der vollständigen Reihe der «Sinne» solche sind, die weniger die Beziehung zur Außenwelt, son­dern mehr das Erleben des Eigen-Seins vermitteln."
      ],
      [
        "Diese letzteren tauchen mehr in das innere seelische Leben ein als zum Beispiel Auge und Ohr; dadurch erscheint das Ergebnis"
      ],
      [
        "ihrer Wahrnehmungs-Vermittelung als inneres seeli­sches Erlebnis.",
        "Aber man sollte auch bei ihnen das eigent­lich Seelische von dem Wahrnehmungselemente so unter­scheiden, wie man zum Beispiel beim Gesehenen den äuße­ren Tatbestand von dem an ihm gemachten inneren Seelen-Erlebnisse unterscheidet. - Für denjenigen, der sich auf den anthroposophischen Gesichtspunkt stellt, darf kein Zu­rückschrecken bestehen vor solchen feinen Vorstellungs-Unterscheidungen, wie sie hier gemacht werden."
      ],
      [
        "Er muß das «Vernehmen der Worte» von dem Gehör einerseits, und dieses «Vernehmen der Worte» von dem durch die ei­genen Gedanken vermittelten «Verstehen der Worte» so unterscheiden können, wie das gewöhnliche Bewußtsein unterscheidet zwischen einem Baum und einem Felsblock.",
        "Würde dies mehr berücksichtigt, so würde man erkennen, daß die Anthroposophie nicht nur die eine Seite hat, welche man gewöhnlich als eine mystische bezeichnet, sondern auch die andere, durch die sie nicht zu einer weniger wissen­schaftlichen Forschung führt als die Naturwissenschaft, sondern zu einer mehr wissenschaftlichen, die eine feinere, methodischere Ausarbeitung des Vorstellenslebens nötig macht als selbst die gewöhnliche Philosophie."
      ],
      [
        "Ich glaube, daß Wilhelm Dilthey mit seinen philosophischen Forschun­gen auf dem Wege war zu derjenigen Sinnes-Lehre, die ich hier skizziert habe, daß er aber nicht zu einem Ziele kom­men konnte, weil er nicht durchdrang bis zu einer völligen Ausarbeitung der in Frage kommenden Vorstellungen.",
        "Vergleiche auch, was ich darüber im zweiten Bande meiner «Rätsel der Philosophie» gesagt habe, 7."
      ],
      [
        "Auflage, Seiten 567-572.)"
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "6. Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit",
    "paragraphs": [
      "6. Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit",
      "Zu Seite 91, Anmerkung zu Zeile 19 von oben",
      "Skizzenhaft möchte ich nun auch darstellen, was sich mir ergeben hat über die Beziehungen des Seelischen zu dem Phy­sisch-Leiblichen. Ich darf wohl sagen, daß ich damit die Er­gebnisse einer dreißig Jahre währenden geisteswissen­schaftlichen Forschung verzeichne. Erst in den letzten Jah­ren ist es mir möglich geworden, das in Frage Kommende so in durch Worte ausdrückbare Gedanken zu fassen, daß ich das Erstrebte zu einer Art vorläufigen Abschlusses bringen konnte Auch davon möchte ich mir gestatten, die Ergeb­nisse hier nur andeutend darzulegen. Ihre Begründung kann durchaus mit den heute vorhandenen wissenschaftlichen Mitteln gegeben werden. Dies würde der Gegenstand eines umfangreichen Buches sein, das in diesem Augenblicke zu schreiben, mir die Verhältnisse nicht gestatten.",
      "Sucht man nach der Beziehung des Seelischen zum Leib­lichen, dann kann man nicht die von Brentano gegebene auf Seite 86 ff. dieser Schrift gekennzeichnete Gliederung des seelischen Erlebens in Vorstellen, Urteilen und in die Er­scheinungen des Liebens und Hassens zugrunde legen. Diese Gliederung führt beim Aufsuchen dieser Beziehun­gen zu einer solchen Verschiebung aller in Betracht kom­menden Verhältnisse, daß man nicht zu sachgemäßen Er­gebnissen gelangen kann. Man muß bei einer derartigen Betrachtung von der von Brentano abgewiesenen Gliede­rung in Vorstellen, Fühlen und Wollen ausgehen. Faßt man nun zusammen alles dasjenige Seelische, das als Vorstellen erlebt wird und sucht man nach den leiblichen Vorgängen,",
      "mit denen dieses Seelische in Beziehung zu setzen ist, so fin­det man den entsprechenden Zusammenhang, indem man dabei in weitgehendem Maße den Ergebnissen der gegen­wärtigen physiologischen Psychologie sich anschließen kann. Die körperlichen Gegenstücke zum Seelischen des Vorstellens hat man in den Vorgängen des Nervensystems mit ihrem Auslaufen in die Sinnesorgane einerseits und in die leibliche Innenorganisation andrerseits zu sehen.",
      "So sehr man vom anthroposophischen Gesichtspunkte aus manches wird anders zu denken haben, als es die gegenwärtige Wis­senschaft tut: eine Grundlage vorzüglicher Art ist in dieser Wissenschaft vorhanden. Nicht so steht es, wenn man die leiblichen Gegenstücke für das Fühlen und Wollen bestim­men will.",
      "In bezug darauf muß man sich innerhalb der Er­gebnisse gegenwärtiger Physiologie erst den richtigen Weg bahnen. Ist man auf denselben gelangt, so findet man, daß man wie das Vorstellen zur Nerventätigkeit so das Fühlen in Beziehung bringen muß zu demjenigen Lebensrhythmus, der in der Atmungstätigkeit seine Mitte hat und mit ihr zu­sammenhängt.",
      "Man hat dabei zu berücksichtigen, daß man zu dem angestrebten Ziele den Atmungsrhythmus mit al­lem, was mit ihm zusammenhängt, bis in die äußersten peri­pherischen Teile der Organisation verfolgen muß. Um auf diesem Gebiete zu konkreten Ergebnissen zu gelangen, müssen die Erfahrungen der physiologischen Forschung in einer Richtung verfolgt werden, welche heute noch vielfach ungewohnt ist.",
      "Erst wenn man dies vollbringt, werden alle Widersprüche verschwinden, die sich zunächst ergeben, wenn Fühlen und Atmungsrhythmus zusammengebracht werden. Was zunächst zum Widerspruch herausfordert, wird bei näherem Eingehen zum Beweise für diese Beziehung.",
      "Aus dem weiten Gebiet, das hier verfolgt werden muß, sei nur ein einziges Beispiel herausgehoben. Das Er­leben des Musikalischen beruht auf einem Fühlen. Der In­halt des musikalischen Gebildes aber lebt in dem Vorstellen, das durch die Wahrnehmungen des Gehörs vermittelt wird.",
      "Wodurch entsteht das musikalische Gefühls-Erlebnis? Die Vorstellung des Tongebildes, die auf Gehörorgan und Nervenvorgang beruht, ist noch nicht dieses musikalische Erlebnis. Das letztere entsteht, indem im Gehirn der At­mungsrhythmus in seiner Fortsetzung bis in dieses Organ hinein, sich begegnet mit dem, was durch Ohr und Nerven­system vollbracht wird.",
      "Und die Seele lebt nun nicht in dem bloß Gehörten und Vorgestellten, sondern sie lebt in dem Atmungsrhythmus; sie erlebt dasjenige, was im Atmungs­rhythmus ausgelöst wird dadurch, daß gewissermaßen das im Nervensystem Vorgehende heranstößt an dieses rhyth­mische Leben. Man muß nur die Physiologie des Atmungs­rhythmus im rechten Lichte sehen, so wird man umfänglich zur Anerkennung des Satzes kommen: die Seele erlebt füh­lend, indem sie sich dabei ähnlich auf den Atmungsrhyth­mus stützt wie im Vorstellen auf die Nervenvorgänge. - Und bezüglich des Wollens findet man, daß dieses sich in ähnlicher Art stützt auf Stoffwechselvorgänge.",
      "Wieder muß da in Betracht gezogen werden, was alles an Verzweigungen und Ausläufern der Stoffwechselvorgänge im ganzen Orga­nismus in Betracht kommt. Wie dann, wenn etwas «vorge­stellt» wird, sich ein Nervenvorgang abspielt, auf Grund dessen die Seele sich ihres Vorgestellten bewußt wird, wie ferner dann, wenn etwas «gefühlt» wird, eine Modifikation des Atmungsrhythmus verläuft, durch die der Seele ein Ge­fühl auflebt: so geht, wenn etwas «gewollt» wird, ein Stoffwechselvorgang",
      "vor sich, der die leibliche Grundlage ist für das als Wollen in der Seele Erlebte. - Nun ist in der Seele ein vollbewußtes waches Erleben nur für das vom Nervensy­stem vermittelte Vorstellen vorhanden. Was durch den At­mungsrhythmus vermittelt wird, das lebt im gewöhnlichen Bewußtsein in jener Stärke, welche die Traumvorstellungen haben.",
      "Dazu gehört alles Gefühlsartige, auch alle Affekte, alle Leidenschaften und so weiter. Das Wollen, das auf Stoff­wechselvorgänge gestützt ist, wird in keinem höheren Grade bewußt erlebt als in jenem ganz dumpfen, der im Schlafe vorhanden ist.",
      "Man wird bei genauer Betrachtung des hier in Frage Kommenden bemerken, daß man das Wol­len ganz anders erlebt als das Vorstellen. Das letztere erlebt man wie man etwa eine von Farbe bestrichene Fläche sieht; das Wollen so, wie eine schwarze Fläche innerhalb eines farbigen Feldes.",
      "Man «sieht» innerhalb der Fläche, auf der keine Farbe ist, eben deshalb etwas, weil im Gegensatz zu der Umgebung, von der Farben-Eindrücke ausgehen, von dieser Fläche keine solchen Eindrücke kommen: man «stellt das Wollen vor», weil innerhalb der Vorstellungs-Erleb­nisse der Seele an gewissen Stellen sich ein Nicht-Vorstellen einfügt, das sich in das vollbewußte Erleben hineinstellt ähnlich wie die im Schlafe zugebrachten Unterbrechungen des Bewußtseins in den bewußten Lebenslauf. Aus diesen verschiedenen Arten des bewußten Erlebens ergibt sich die Mannigfaltigkeit des seelischen Erfahrens in Vorstellen, Fühlen und Wollen. - Theodor Ziehen wird in seinem Bu­che «Leitfaden der physiologischen Psychologie» zu bedeutungsvollen Kennzeichnungen des Gefühls und des Wollens geführt.",
      "Dies Buch ist in mancher Beziehung mu­stergiltig für die gegenwärtige naturwissenschaftliche Betrachtungsart",
      "des Zusammenhanges von Physischem und Psychischem. Das Vorstellen in seinen verschiedenen Ge­staltungen wird zu dem Nervenleben in die Beziehung ge­setzt, die man auch vom anthroposophischen Gesichts­punkte anerkennen muß.",
      "Doch über das Gefühl sagt Zie­hen (vergleiche 9. Vorlesung in seinem genannten Buche): «Die ältere Psychologie betrachtet fast ausnahmslos die Af­fekte als die Kundgebungen eines besonderen, selbständi­gen Seelenvermögens.",
      "Kant stellte das Gefühl der Lust und Unlust als besondere Seelenfähigkeit zwischen das Erkennt­nisvermögen und das Begehrungsvermögen und betonte ausdrücklich, daß eine weitere Ableitung dieser drei Seelenvermögen aus einem gemeinschaftlichen Grunde nicht möglich sei. Demgegenüber haben unsere bisherigen Erör­terungen uns bereits gelehrt, daß die Gefühle der Lust und Unlust in dieser Selbständigkeit gar nicht existieren, daß sie vielmehr nur als Eigenschaften oder Merkmale von Emp­findungen und Vorstellungen als sogenannte Gefühlstöne auftreten.» - Diese Denkungsart gesteht also dem Fühlen keine Selbständigkeit im Seelenleben zu; sie sieht in ihm nur eine Eigenschaft des Vorstellens.",
      "Die Folge davon ist, daß sie nicht nur das Vorstellungsleben, sondern auch das Ge­fühlsleben von den Nervenvorgängen gestützt sein läßt. Für sie ist das Nervenleben das Leibliche, dem das gesamte Seelische zugeeignet wird.",
      "Doch beruht diese Denkungsart im Grunde darauf, daß sie in unbewußter Art schon das vorausdenkt, was sie finden will. Sie läßt als Seelisches nur dasjenige gelten, was zu Nervenvorgängen in Beziehung steht, und muß aus diesem Grunde dasjenige, was nicht dem Nervenleben sich zueignen läßt, das Fühlen, als nicht selb­ständig existierend ansehen, als bloßes Merkmal des Vorstellens.",
      "Wer sich nicht in dieser Weise mit seinen Begriffen in eine falsche Richtung bringt, dem wird erstens eine unbe­fangene Seelenbeobachtung die Selbständigkeit des Gefühls­lebens in der bestimmtesten Art ergeben, zweitens wird ihm die vorurteilslose Verwertung der physiologischen Erkenntnisse die Einsicht verschaffen, daß das Fühlen in der oben angedeuteten Weise dem Atmungsrhythmus zuzueig­nen ist. - Dem Wollen spricht die naturwissenschaftliche Denkungsart alles selbständig Wesenhafte im Seelenleben ab. Dieses gilt ihr nicht einmal wie das Fühlen als Merkmal des Vorstellens.",
      "Aber dieses Absprechen beruht auch nur darauf, daß man alles Wesenhaft-Seelische den Nervenvor­gängen zueignen will (vergleiche die 15. Vorlesung in Theo­dor Ziehens «Physiologischer Psychologie»). Nun kann man aber das Wollen in seiner besonderen Eigenart nicht auf eigentliche Nervenvorgänge beziehen.",
      "Gerade wenn man dies mit der musterhaften Klarheit herausarbeitet, wie es Theodor Ziehen tut, kann man zu der Ansicht hingedrängt werden, die Analyse der Seelenvorgänge in ihrer Be­ziehung zum Leibesleben «ergibt keinen Anlaß zur An­nahme eines besonderen Willensvermögens». Und doch: die unbefangene Seelenbetrachtung erzwingt die Anerken­nung des selbständigen Willenlebens; und die sachgemäße Einsicht in die physiologischen Ergebnisse zeigt, daß das Wollen als solches nicht zu Nervenvorgängen, sondern zu Stoffwechselvorgängen in Beziehung gesetzt werden muß. - Wenn man auf diesem Gebiete klare Begriffe schaffen will, dann muß man die physiologischen und psychologischen Ergebnisse in dem Lichte sehen, das durch die Wirklichkeit gefordert wird; nicht aber so, wie es in der gegenwärtigen Physiologie und Psychologie vielfach geschieht, in einer",
      "Beleuchtung, welche aus vorgefaßten Meinungen, Defini­tionen, ja sogar theoretischen Sympathien und Antipathien stammt. Vor allem ist scharf ins Auge zu fassen das Verhält­nis von Nerventätigkeit, Atmungsrhythinus und Stoff­wechseltätigkeit.",
      "Denn diese Tätigkeitsformen liegen nicht neben-, sondern ineinander, durchdringen sich, gehen inein­ander über. Stoffwechseltätigkeit ist im ganzen Organismus vorhanden; sie durchdringt die Organe des Rhythmus und diejenigen der Nerventätigkeit.",
      "Aber im Rhythmus ist sie nicht die leibliche Grundlage des Fühlens, in der Nerventä­tigkeit nicht diejenige des Vorstellens; sondern in beiden ist ihr die den Rhythmus und die Nerven durchdringende Wil­lenswirksamkeit zuzueignen. Was im Nerv als Stoffwechsel­tätigkeit existiert, kann nur ein materialistisches Vorurteil mit dem Vorstellen in eine Beziehung setzen.",
      "Die in der Wirklichkeit wurzelnde Betrachtung sagt etwas ganz ande­res. Sie muß anerkennen, daß im Nerv Stoffwechsel vorhan­den ist, insofern ihn das Wollen durchdringt. Ebenso ist es in dem leiblichen Apparat für den Rhythmus.",
      "Was in ihm Stoffwechseltätigkeit ist, hat mit dem in diesem Organ vor­handenen Wollen zu tun. Man muß mit der Stoffwechseltä­tigkeit das Wollen, mit dem rhythmischen Geschehen das Fühlen in Zusammenhang bringen, gleichgiltig, in welchen Organen sich Stoffwechsel oder Rhythmus offenbaren.",
      "In den Nerven aber geht noch etwas ganz anderes vor sich als Stoffwechsel und Rhythmus. Die leiblichen Vorgänge im Nervensystem, welche dem Vorstellen die Grundlage ge­ben, sind physiologisch schwer zu fassen.",
      "Denn, wo Nerventätigkeit stattfindet, da ist Vorstellen des gewöhnlichen Bewußtseins vorhanden. Der Satz gilt aber auch umge­kehrt: wo nicht vorgestellt wird, da kann nie Nerventätig­keit",
      "gefunden werden, sondern nur Stoffwechseltätigkeit im Nerven, und andeutungsweise rhythmisches Geschehen. Die Physiologie wird nie zu Begriffen kommen, die für die Nervenlehre wirklichkeitsgemäß sind, solange sie nicht ein­sieht, daß die wahrhaftige Nerventätigkeit überhaupt nicht Gegenstand der physiologischen Sinnesbeobachtung sein kann.",
      "Anatomie und Physiologie müssen zu der Erkenntnis kommen, daß sie die Nerventätigkeit nur durch eine Methode der Ausschließung finden können. Was im Nervenleben nicht sinnlich beobachtbar ist, wovon aber das Sinnesgemäße die Notwendigkeit seines Vorhandenseins ergibt und auch die Eigenheit seiner Wirksamkeit, das ist Nerventätigkeit.",
      "Zu einer positiven Vorstellung über die Nerventätigkeit kommt man, wenn man in ihr dasjenige materielle Gesche­hen sieht, durch das im Sinne des ersten Kapitels dieser Schrift die rein geistig-seelische Wesenhaftigkeit des leben­digen Vorstellungsinhaltes zu dem unlebendigen Vorstel­len des gewöhnlichen Bewußtseins herabgelähmt wird. Ohne diesen Begriff, den man in die Physiologie einführen muß, wird in dieser keine Möglichkeit bestehen, zu sagen, was Nerventätigkeit ist.",
      "Die Physiologie hat Methoden sich ausgebildet, welche gegenwärtig diesen Begriff eher ver­decken als ihn offenbaren. Und auch die Psychologie hat sich auf diesem Gebiete den Weg versperrt. Man sehe nur, wie zum Beispiel die Herbartsche Psychologie in dieser Richtung gewirkt hat.",
      "Sie hat den Blick nur auf das Vorstel­lungsleben geworfen, und sieht in Fühlen und Wollen nur Wirksamkeiten des Vorstellungslebens. Aber diese Wirk­samkeiten zerrinnen vor der Erkenntnis, wenn man nicht zu gleicher Zeit den Blick unbefangen auf die Wirklichkeit des Fühlens und Wollens richtet.",
      "Man kommt durch solches",
      "Zerrinnen zu keiner wirklichkeitsgemäßen Zuordnung des Fühlens und Wollens zu den leiblichen Vorgängen. - Der Leib als Ganzes, nicht bloß die in ihm eingeschlossene Ner­ventätigkeit ist physische Grundlage des Seelenlebens. Und wie das letztere für das gewöhnliche Bewußtsein sich um­schreiben läßt durch Vorstellen, Fühlen und Wollen, so das leibliche Leben durch Nerventätigkeit, rhythmisches Ge­schehen und Stoffwechselvorgänge. - Sogleich entsteht da die Frage: wie ordnen sich in den Organismus ein auf der einen Seite die eigentliche Sinneswahrnehmung, in welche die Nerventätigkeit nur ausläuft, und wie die Bewegungs­fähigkeit auf der andern Seite, in welche das Wollen mün­det?",
      "Unbefangene Beobachtung zeigt, daß beides nicht in demselben Sinne zum Organismus gehört wie Nerventätig­keit, rhythmisches Geschehen und Stoffwechselvorgänge. Was im Sinn geschieht ist etwas, das gar nicht unmittelbar dem Organismus angehört.",
      "In die Sinne erstreckt sich die Außenwelt wie in Golfen hinein in das Wesen des Organis­mus. Indem die Seele das im Sinne vor sich gehende Ge­schehen umspannt, nimmt sie nicht an einem inneren orga­nischen Geschehen teil, sondern an der Fortsetzung des äu­ßeren Geschehens in den Organismus hinein. (Ich habe diese Verhältnisse erkenntnis kritisch in einem Vortrag für den Bologner Philosophen-Kongreß des Jahres 1911 erör­tert.) - Und in einem Bewegungsvorgang hat man es phy­sisch auch nicht mit etwas zu tun, dessen Wesenhaftes inner­halb des Organismus liegt, sondern mit einer Wirksamkeit des Organismus in den Gleichgewichts- und Kräfteverhältnissen, in die der Organismus gegenüber der Außenwelt hineingestellt ist.",
      "Innerhalb des Organismus ist dem Wollen nur ein Stoffwechselvorgang zuzueignen; aber das durch",
      "diesen Vorgang ausgelöste Geschehen ist zugleich ein We­senhaftes innerhalb der Gleichgewichts- und Kräfteverhältnisse der Außenwelt; und die Seele übergreift, indem sie sich wollend betätigt, den Bereich des Organismus und lebt mit ihrem Tun das Geschehen der Außenwelt mit. Eine große Verwirrung hat für die Betrachtung aller dieser Dinge die Gliederung der Nerven in Empfindungs- und motori­sche Nerven angerichtet. So fest verankert diese Gliederung in den gegenwärtigen physiologischen Vorstellungen er­scheint: sie ist nicht in der unbefangenen Beobachtung be­gründet. Was die Physiologie vorbringt auf Grund der Zer­schneidung der Nerven, oder der krankhaften Ausschal­tung gewisser Nerven beweist nicht, was auf Grundlage des Versuches oder der Erfahrung sich ergibt, sondern etwas ganz anderes. Es beweist, daß der Unterschied gar nicht be­steht, den man zwischen Empfindungs- und motorischen Nerven annimmt. Beide Nervenarten sind vielmehr Wesens­gleich. Der sogenannte motorische Nerv dient nicht in dem Sinne der Bewegung wie die Lehre von dieser Gliederung es annimmt, sondern als Träger der Nerventätigkeit dient er der inneren Wahrnehmung desjenigen Stoffwechselvorganges, der dem Wollen zugrunde liegt, geradeso wie der Empfin­dungsnerv der Wahrnehmung desjenigen dient, was im Sin­nesorgan sich abspielt. Bevor die Nervenlehre in dieser Be­ziehung mit klaren Begriffen arbeitet, wird eine richtige Zu­ordnung des Seelenlebens zum Leibesleben nicht zustande",
      "In ähnlicher Art, wie man psycho-physiologisch die Bezie­hungen des in Vorstellen, Fühlen und Wollen verlaufenden Seelenlebens zum Leibesleben suchen kann, so kann man",
      "anthroposophisch nach Erkenntnis der Beziehungen stre­ben, welche das Seelische des gewöhnlichen Bewußtseins zum Geistesleben hat. Und da findet man durch die in dieser und in meinen anderen Schriften geschilderten anthroposo­phischen Methoden, daß sich für das Vorstellen wie im Leibe die Nerventätigkeit, so im Geistigen eine Grundlage findet.",
      "Die Seele steht nach der anderen, vom Leibe abge­wandten, Seite in Beziehung zu einem geistig Wesenhaften, das die Grundlage ist für das Vorstellen des gewöhnlichen Bewußtseins. Dieses geistig Wesenhafte kann aber nur durch schauendes Erkennen erlebt werden.",
      "Und es wird so erlebt, indem sich sein Inhalt als gegliederte Imaginationen dem schauenden Bewußtsein darstellt. Wie nach dem Leibe hin das Vorstellen auf der Nerventätigkeit ruht, so strömt es von der andern Seite her aus einem geistig Wesenhaften, das in Imaginationen sich enthüllt.",
      "Dieses geistig Wesenhafte ist, was in meinen Schriften der Äther- oder Lebensleib ge­nannt wird. (Wobei, wenn ich es bespreche, ich immer dar­auf aufmerksam mache, daß man sich an dem Ausdruck «Leib» ebensowenig wie an dem andern «Äther» stoßen solle, denn, was ich ausführe, zeigt klar, daß man das Ge­meinte nicht im materialistischen Sinne deuten soll.) Und dieser Lebensleib (in dem 4. Buch des 1.",
      "Jahrganges der Zeit­schrift «Das Reich» habe ich auch den Ausdruck «Bilde­kräfteleib» gebraucht) ist das Geistige, aus dem das Vor­stellungsleben des gewöhnlichen Bewußtseins von der Ge­burt (beziehungsweise Empfängnis) bis zum Tode erfließt. -Das Fühlen des gewöhnlichen Bewußtseins ruht nach der Leibesseite hin auf dem rhythmischen Geschehen. Von der geistigen Seite her erfließt es aus einem Geistig-Wesenhaf­ten, das innerhalb der anthroposophischen Forschung",
      "durch Methoden gefunden wird, welche ich in meinen Schriften als diejenigen der Inspiration kennzeichne. (Wo­bei man wieder berücksichtigen möge, daß ich innerhalb dieses Begriffes nur das von mir Umschriebene verstehe, so daß man meine Bezeichnung nicht verwechseln sollte mit dem, was oft vom Laien bei diesem Worte verstanden wird.) Dem schauenden Bewußtsein offenbart sich in dem der Seele zugrunde liegenden, durch Inspirationen zu erfassen­den geistig Wesenhaften dasjenige, was dem Menschen als Geistwesen eigen ist über Geburt und Tod hinaus. Auf die­sem Gebiete ist es, wo die Anthroposophie ihre geisteswis­senschaftlichen Untersuchungen über die Unsterblichkeits­frage anstellt.",
      "So wie im Leibe durch das rhythmische Geschehen sich der sterbliche Teil des fühlenden Menschenwesens offenbart, so in dem Inspirations-Inhalt des schauenden Bewußtseins der unsterbli­che geistige Seelenwesenskern. - Das Wollen, das nach dem Leibe hin auf den Stoffwechselvorgängen beruht, erströmt aus dem Geiste für das schauende Bewußtsein durch dasjenige, was ich in meinen Schriften die wahrhaftigen Intuitionen nenne. Was im Leibe durch die gewissermaßen niederste Be­tätigung des Stoffwechsels sich offenbart, dem entspricht im Geiste ein Höchstes: dasjenige, was durch Intuitionen sich ausspricht.",
      "Daher kommt das Vorstellen, das auf der Ner­ventätigkeit beruht, leiblich fast vollkommen zur Darstel­lung; das Wollen hat in den ihm leiblich zugeordneten Stoff­wechselvorgängen nur einen schwachen Abglanz. Das wirkliche Vorstellen ist das lebendige; das leiblich bedingte ist das abgelähmte.",
      "Der Inhalt ist derselbe. Das wirkliche Wollen, auch das in der physischen Welt sich verwirkli­chende, verläuft in den Regionen, die nur dem intuitiven Schauen zugänglich sind; sein leibliches Gegenstück hat mit",
      "seinem Inhalte fast gar nichts zu tun. In demjenigen geistig Wesenhaften, das der Intuition sich offenbart, ist enthalten, was sich aus vorangegangenen Erdenleben in die folgenden hinübererstreckt. Und auf dem hier in Betracht kommenden Gebiet ist es, wo die Anthroposophie sich den Fragen der wiederholten Erdenleben und der Schicksalsfrage nähert.",
      "Wie der Leib in Nerventätigkeit, rhythmischem Geschehen und Stoffwechselvorgängen sich auslebt, so der Geist des Menschen in demjenigen, was in Imaginationen, Inspiratio­nen, Intuitionen sich offenbart. Und wie der Leib in sei­nem Bereich nach zwei Seiten das Wesen seiner Außenwelt miterleben läßt, nämlich in den Sinnes- und den Bewe­gungsvorgängen, so der Geist nach der einen Seite hin, in­dem er das vorstellende Seelenleben auch im gewöhnlichen Bewußtsein imaginativ erlebt; und nach der andern Seite hin, indem er im Wollen intuitive Impulse ausgestaltet, die sich durch Stoffwechselvorgänge verwirklichen.",
      "Sieht man nach dem Leibe hin, so findet man die Nerventätigkeit, die als Vorstellungswesen lebt; sieht man nach dem Geiste hin, so gewahrt man den Geist-Inhalt der Imaginationen, der in eben dieses Vorstellungswesen einfließt. Brentano empfin­det zunächst die geistige Seite am vorstellenden Seelenle­ben; daher charakterisiert er dieses Leben als Bildleben (imaginatives Geschehen).",
      "Aber wenn nicht bloß ein eige­nes Seelen-Inneres erlebt wird, sondern durch das Urteil ein Anzuerkennendes oder zu Verwerfendes, so kommt zum Vorstellen hinzu ein aus dem Geiste fließendes Seelenerleb­nis, dessen Inhalt unbewußt bleibt, so lange es sich nur um das gewöhnliche Bewußtsein handelt, weil er in den Imaginationen von einer dem physischen Objekte zugrunde lie­genden geistigen Wesenhaftigkeit besteht, die zu der Vorstellung",
      "nur das hinzufügen, daß deren Inhalt existiert. Aus diesem Grunde ist es, daß Brentano das Vorstellungsleben in seiner Klassifikation spaltet, in das bloße Vorstellen, das nur innerlich Daseiendes imaginativ erlebt; und in das Urteilen, das von außen Gegebenes imaginativ erlebt, aber das Erleb­nis nur als Anerkennung oder Verwerfung sich zum Be­wußtsein bringt. Gegenüber dem Fühlen blickt Brentano gar nicht nach der Leibes-Grundlage, dem rhythmischen Geschehen hin, sondern er versetzt nur dasjenige in den Be­reich seiner Aufmerksamkeit, was aus unbewußt bleiben­den Inspirationen im Gebiet des gewöhnlichen Bewußt­seins als Lieben und Hassen auftritt. Das Wollen aber entfällt ganz seiner Aufmerksamkeit, weil dieses sich nur auf Er­scheinungen in der Seele richten will, in dem Wollen aber et­was liegt, was nicht in der Seele beschlossen ist, sondern mit dem die Seele eine Außenwelt miterlebt. Die Brentanosche Klassifikation der Seelenphänomene beruht also darauf, daß er diese nach Gesichtspunkten gliedert, die ihre wahre Be­leuchtung erfahren, wenn man den Blick nach dem Geist-Kerne der Seele lenkt, und daß er doch damit treffen will die Phänomene des gewöhnlichen Bewußtseins. Mit dem hier über Brentano Gesagten habe ich noch ergänzen wollen das oben Seite 90 ff. in dieser Beziehung über ihn Ausgespro­chene."
    ],
    "sentences": [
      [
        "Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit"
      ],
      [
        "Zu Seite 91, Anmerkung zu Zeile 19 von oben"
      ],
      [
        "Skizzenhaft möchte ich nun auch darstellen, was sich mir ergeben hat über die Beziehungen des Seelischen zu dem Phy­sisch-Leiblichen.",
        "Ich darf wohl sagen, daß ich damit die Er­gebnisse einer dreißig Jahre währenden geisteswissen­schaftlichen Forschung verzeichne.",
        "Erst in den letzten Jah­ren ist es mir möglich geworden, das in Frage Kommende so in durch Worte ausdrückbare Gedanken zu fassen, daß ich das Erstrebte zu einer Art vorläufigen Abschlusses bringen konnte Auch davon möchte ich mir gestatten, die Ergeb­nisse hier nur andeutend darzulegen.",
        "Ihre Begründung kann durchaus mit den heute vorhandenen wissenschaftlichen Mitteln gegeben werden.",
        "Dies würde der Gegenstand eines umfangreichen Buches sein, das in diesem Augenblicke zu schreiben, mir die Verhältnisse nicht gestatten."
      ],
      [
        "Sucht man nach der Beziehung des Seelischen zum Leib­lichen, dann kann man nicht die von Brentano gegebene auf Seite 86 ff. dieser Schrift gekennzeichnete Gliederung des seelischen Erlebens in Vorstellen, Urteilen und in die Er­scheinungen des Liebens und Hassens zugrunde legen.",
        "Diese Gliederung führt beim Aufsuchen dieser Beziehun­gen zu einer solchen Verschiebung aller in Betracht kom­menden Verhältnisse, daß man nicht zu sachgemäßen Er­gebnissen gelangen kann.",
        "Man muß bei einer derartigen Betrachtung von der von Brentano abgewiesenen Gliede­rung in Vorstellen, Fühlen und Wollen ausgehen.",
        "Faßt man nun zusammen alles dasjenige Seelische, das als Vorstellen erlebt wird und sucht man nach den leiblichen Vorgängen,"
      ],
      [
        "mit denen dieses Seelische in Beziehung zu setzen ist, so fin­det man den entsprechenden Zusammenhang, indem man dabei in weitgehendem Maße den Ergebnissen der gegen­wärtigen physiologischen Psychologie sich anschließen kann.",
        "Die körperlichen Gegenstücke zum Seelischen des Vorstellens hat man in den Vorgängen des Nervensystems mit ihrem Auslaufen in die Sinnesorgane einerseits und in die leibliche Innenorganisation andrerseits zu sehen."
      ],
      [
        "So sehr man vom anthroposophischen Gesichtspunkte aus manches wird anders zu denken haben, als es die gegenwärtige Wis­senschaft tut: eine Grundlage vorzüglicher Art ist in dieser Wissenschaft vorhanden.",
        "Nicht so steht es, wenn man die leiblichen Gegenstücke für das Fühlen und Wollen bestim­men will."
      ],
      [
        "In bezug darauf muß man sich innerhalb der Er­gebnisse gegenwärtiger Physiologie erst den richtigen Weg bahnen.",
        "Ist man auf denselben gelangt, so findet man, daß man wie das Vorstellen zur Nerventätigkeit so das Fühlen in Beziehung bringen muß zu demjenigen Lebensrhythmus, der in der Atmungstätigkeit seine Mitte hat und mit ihr zu­sammenhängt."
      ],
      [
        "Man hat dabei zu berücksichtigen, daß man zu dem angestrebten Ziele den Atmungsrhythmus mit al­lem, was mit ihm zusammenhängt, bis in die äußersten peri­pherischen Teile der Organisation verfolgen muß.",
        "Um auf diesem Gebiete zu konkreten Ergebnissen zu gelangen, müssen die Erfahrungen der physiologischen Forschung in einer Richtung verfolgt werden, welche heute noch vielfach ungewohnt ist."
      ],
      [
        "Erst wenn man dies vollbringt, werden alle Widersprüche verschwinden, die sich zunächst ergeben, wenn Fühlen und Atmungsrhythmus zusammengebracht werden.",
        "Was zunächst zum Widerspruch herausfordert, wird bei näherem Eingehen zum Beweise für diese Beziehung."
      ],
      [
        "Aus dem weiten Gebiet, das hier verfolgt werden muß, sei nur ein einziges Beispiel herausgehoben.",
        "Das Er­leben des Musikalischen beruht auf einem Fühlen.",
        "Der In­halt des musikalischen Gebildes aber lebt in dem Vorstellen, das durch die Wahrnehmungen des Gehörs vermittelt wird."
      ],
      [
        "Wodurch entsteht das musikalische Gefühls-Erlebnis?",
        "Die Vorstellung des Tongebildes, die auf Gehörorgan und Nervenvorgang beruht, ist noch nicht dieses musikalische Erlebnis.",
        "Das letztere entsteht, indem im Gehirn der At­mungsrhythmus in seiner Fortsetzung bis in dieses Organ hinein, sich begegnet mit dem, was durch Ohr und Nerven­system vollbracht wird."
      ],
      [
        "Und die Seele lebt nun nicht in dem bloß Gehörten und Vorgestellten, sondern sie lebt in dem Atmungsrhythmus; sie erlebt dasjenige, was im Atmungs­rhythmus ausgelöst wird dadurch, daß gewissermaßen das im Nervensystem Vorgehende heranstößt an dieses rhyth­mische Leben.",
        "Man muß nur die Physiologie des Atmungs­rhythmus im rechten Lichte sehen, so wird man umfänglich zur Anerkennung des Satzes kommen: die Seele erlebt füh­lend, indem sie sich dabei ähnlich auf den Atmungsrhyth­mus stützt wie im Vorstellen auf die Nervenvorgänge. - Und bezüglich des Wollens findet man, daß dieses sich in ähnlicher Art stützt auf Stoffwechselvorgänge."
      ],
      [
        "Wieder muß da in Betracht gezogen werden, was alles an Verzweigungen und Ausläufern der Stoffwechselvorgänge im ganzen Orga­nismus in Betracht kommt.",
        "Wie dann, wenn etwas «vorge­stellt» wird, sich ein Nervenvorgang abspielt, auf Grund dessen die Seele sich ihres Vorgestellten bewußt wird, wie ferner dann, wenn etwas «gefühlt» wird, eine Modifikation des Atmungsrhythmus verläuft, durch die der Seele ein Ge­fühl auflebt: so geht, wenn etwas «gewollt» wird, ein Stoffwechselvorgang"
      ],
      [
        "vor sich, der die leibliche Grundlage ist für das als Wollen in der Seele Erlebte. - Nun ist in der Seele ein vollbewußtes waches Erleben nur für das vom Nervensy­stem vermittelte Vorstellen vorhanden.",
        "Was durch den At­mungsrhythmus vermittelt wird, das lebt im gewöhnlichen Bewußtsein in jener Stärke, welche die Traumvorstellungen haben."
      ],
      [
        "Dazu gehört alles Gefühlsartige, auch alle Affekte, alle Leidenschaften und so weiter.",
        "Das Wollen, das auf Stoff­wechselvorgänge gestützt ist, wird in keinem höheren Grade bewußt erlebt als in jenem ganz dumpfen, der im Schlafe vorhanden ist."
      ],
      [
        "Man wird bei genauer Betrachtung des hier in Frage Kommenden bemerken, daß man das Wol­len ganz anders erlebt als das Vorstellen.",
        "Das letztere erlebt man wie man etwa eine von Farbe bestrichene Fläche sieht; das Wollen so, wie eine schwarze Fläche innerhalb eines farbigen Feldes."
      ],
      [
        "Man «sieht» innerhalb der Fläche, auf der keine Farbe ist, eben deshalb etwas, weil im Gegensatz zu der Umgebung, von der Farben-Eindrücke ausgehen, von dieser Fläche keine solchen Eindrücke kommen: man «stellt das Wollen vor», weil innerhalb der Vorstellungs-Erleb­nisse der Seele an gewissen Stellen sich ein Nicht-Vorstellen einfügt, das sich in das vollbewußte Erleben hineinstellt ähnlich wie die im Schlafe zugebrachten Unterbrechungen des Bewußtseins in den bewußten Lebenslauf.",
        "Aus diesen verschiedenen Arten des bewußten Erlebens ergibt sich die Mannigfaltigkeit des seelischen Erfahrens in Vorstellen, Fühlen und Wollen. - Theodor Ziehen wird in seinem Bu­che «Leitfaden der physiologischen Psychologie» zu bedeutungsvollen Kennzeichnungen des Gefühls und des Wollens geführt."
      ],
      [
        "Dies Buch ist in mancher Beziehung mu­stergiltig für die gegenwärtige naturwissenschaftliche Betrachtungsart"
      ],
      [
        "des Zusammenhanges von Physischem und Psychischem.",
        "Das Vorstellen in seinen verschiedenen Ge­staltungen wird zu dem Nervenleben in die Beziehung ge­setzt, die man auch vom anthroposophischen Gesichts­punkte anerkennen muß."
      ],
      [
        "Doch über das Gefühl sagt Zie­hen (vergleiche 9.",
        "Vorlesung in seinem genannten Buche): «Die ältere Psychologie betrachtet fast ausnahmslos die Af­fekte als die Kundgebungen eines besonderen, selbständi­gen Seelenvermögens."
      ],
      [
        "Kant stellte das Gefühl der Lust und Unlust als besondere Seelenfähigkeit zwischen das Erkennt­nisvermögen und das Begehrungsvermögen und betonte ausdrücklich, daß eine weitere Ableitung dieser drei Seelenvermögen aus einem gemeinschaftlichen Grunde nicht möglich sei.",
        "Demgegenüber haben unsere bisherigen Erör­terungen uns bereits gelehrt, daß die Gefühle der Lust und Unlust in dieser Selbständigkeit gar nicht existieren, daß sie vielmehr nur als Eigenschaften oder Merkmale von Emp­findungen und Vorstellungen als sogenannte Gefühlstöne auftreten.» - Diese Denkungsart gesteht also dem Fühlen keine Selbständigkeit im Seelenleben zu; sie sieht in ihm nur eine Eigenschaft des Vorstellens."
      ],
      [
        "Die Folge davon ist, daß sie nicht nur das Vorstellungsleben, sondern auch das Ge­fühlsleben von den Nervenvorgängen gestützt sein läßt.",
        "Für sie ist das Nervenleben das Leibliche, dem das gesamte Seelische zugeeignet wird."
      ],
      [
        "Doch beruht diese Denkungsart im Grunde darauf, daß sie in unbewußter Art schon das vorausdenkt, was sie finden will.",
        "Sie läßt als Seelisches nur dasjenige gelten, was zu Nervenvorgängen in Beziehung steht, und muß aus diesem Grunde dasjenige, was nicht dem Nervenleben sich zueignen läßt, das Fühlen, als nicht selb­ständig existierend ansehen, als bloßes Merkmal des Vorstellens."
      ],
      [
        "Wer sich nicht in dieser Weise mit seinen Begriffen in eine falsche Richtung bringt, dem wird erstens eine unbe­fangene Seelenbeobachtung die Selbständigkeit des Gefühls­lebens in der bestimmtesten Art ergeben, zweitens wird ihm die vorurteilslose Verwertung der physiologischen Erkenntnisse die Einsicht verschaffen, daß das Fühlen in der oben angedeuteten Weise dem Atmungsrhythmus zuzueig­nen ist. - Dem Wollen spricht die naturwissenschaftliche Denkungsart alles selbständig Wesenhafte im Seelenleben ab.",
        "Dieses gilt ihr nicht einmal wie das Fühlen als Merkmal des Vorstellens."
      ],
      [
        "Aber dieses Absprechen beruht auch nur darauf, daß man alles Wesenhaft-Seelische den Nervenvor­gängen zueignen will (vergleiche die 15.",
        "Vorlesung in Theo­dor Ziehens «Physiologischer Psychologie»).",
        "Nun kann man aber das Wollen in seiner besonderen Eigenart nicht auf eigentliche Nervenvorgänge beziehen."
      ],
      [
        "Gerade wenn man dies mit der musterhaften Klarheit herausarbeitet, wie es Theodor Ziehen tut, kann man zu der Ansicht hingedrängt werden, die Analyse der Seelenvorgänge in ihrer Be­ziehung zum Leibesleben «ergibt keinen Anlaß zur An­nahme eines besonderen Willensvermögens».",
        "Und doch: die unbefangene Seelenbetrachtung erzwingt die Anerken­nung des selbständigen Willenlebens; und die sachgemäße Einsicht in die physiologischen Ergebnisse zeigt, daß das Wollen als solches nicht zu Nervenvorgängen, sondern zu Stoffwechselvorgängen in Beziehung gesetzt werden muß. - Wenn man auf diesem Gebiete klare Begriffe schaffen will, dann muß man die physiologischen und psychologischen Ergebnisse in dem Lichte sehen, das durch die Wirklichkeit gefordert wird; nicht aber so, wie es in der gegenwärtigen Physiologie und Psychologie vielfach geschieht, in einer"
      ],
      [
        "Beleuchtung, welche aus vorgefaßten Meinungen, Defini­tionen, ja sogar theoretischen Sympathien und Antipathien stammt.",
        "Vor allem ist scharf ins Auge zu fassen das Verhält­nis von Nerventätigkeit, Atmungsrhythinus und Stoff­wechseltätigkeit."
      ],
      [
        "Denn diese Tätigkeitsformen liegen nicht neben-, sondern ineinander, durchdringen sich, gehen inein­ander über.",
        "Stoffwechseltätigkeit ist im ganzen Organismus vorhanden; sie durchdringt die Organe des Rhythmus und diejenigen der Nerventätigkeit."
      ],
      [
        "Aber im Rhythmus ist sie nicht die leibliche Grundlage des Fühlens, in der Nerventä­tigkeit nicht diejenige des Vorstellens; sondern in beiden ist ihr die den Rhythmus und die Nerven durchdringende Wil­lenswirksamkeit zuzueignen.",
        "Was im Nerv als Stoffwechsel­tätigkeit existiert, kann nur ein materialistisches Vorurteil mit dem Vorstellen in eine Beziehung setzen."
      ],
      [
        "Die in der Wirklichkeit wurzelnde Betrachtung sagt etwas ganz ande­res.",
        "Sie muß anerkennen, daß im Nerv Stoffwechsel vorhan­den ist, insofern ihn das Wollen durchdringt.",
        "Ebenso ist es in dem leiblichen Apparat für den Rhythmus."
      ],
      [
        "Was in ihm Stoffwechseltätigkeit ist, hat mit dem in diesem Organ vor­handenen Wollen zu tun.",
        "Man muß mit der Stoffwechseltä­tigkeit das Wollen, mit dem rhythmischen Geschehen das Fühlen in Zusammenhang bringen, gleichgiltig, in welchen Organen sich Stoffwechsel oder Rhythmus offenbaren."
      ],
      [
        "In den Nerven aber geht noch etwas ganz anderes vor sich als Stoffwechsel und Rhythmus.",
        "Die leiblichen Vorgänge im Nervensystem, welche dem Vorstellen die Grundlage ge­ben, sind physiologisch schwer zu fassen."
      ],
      [
        "Denn, wo Nerventätigkeit stattfindet, da ist Vorstellen des gewöhnlichen Bewußtseins vorhanden.",
        "Der Satz gilt aber auch umge­kehrt: wo nicht vorgestellt wird, da kann nie Nerventätig­keit"
      ],
      [
        "gefunden werden, sondern nur Stoffwechseltätigkeit im Nerven, und andeutungsweise rhythmisches Geschehen.",
        "Die Physiologie wird nie zu Begriffen kommen, die für die Nervenlehre wirklichkeitsgemäß sind, solange sie nicht ein­sieht, daß die wahrhaftige Nerventätigkeit überhaupt nicht Gegenstand der physiologischen Sinnesbeobachtung sein kann."
      ],
      [
        "Anatomie und Physiologie müssen zu der Erkenntnis kommen, daß sie die Nerventätigkeit nur durch eine Methode der Ausschließung finden können.",
        "Was im Nervenleben nicht sinnlich beobachtbar ist, wovon aber das Sinnesgemäße die Notwendigkeit seines Vorhandenseins ergibt und auch die Eigenheit seiner Wirksamkeit, das ist Nerventätigkeit."
      ],
      [
        "Zu einer positiven Vorstellung über die Nerventätigkeit kommt man, wenn man in ihr dasjenige materielle Gesche­hen sieht, durch das im Sinne des ersten Kapitels dieser Schrift die rein geistig-seelische Wesenhaftigkeit des leben­digen Vorstellungsinhaltes zu dem unlebendigen Vorstel­len des gewöhnlichen Bewußtseins herabgelähmt wird.",
        "Ohne diesen Begriff, den man in die Physiologie einführen muß, wird in dieser keine Möglichkeit bestehen, zu sagen, was Nerventätigkeit ist."
      ],
      [
        "Die Physiologie hat Methoden sich ausgebildet, welche gegenwärtig diesen Begriff eher ver­decken als ihn offenbaren.",
        "Und auch die Psychologie hat sich auf diesem Gebiete den Weg versperrt.",
        "Man sehe nur, wie zum Beispiel die Herbartsche Psychologie in dieser Richtung gewirkt hat."
      ],
      [
        "Sie hat den Blick nur auf das Vorstel­lungsleben geworfen, und sieht in Fühlen und Wollen nur Wirksamkeiten des Vorstellungslebens.",
        "Aber diese Wirk­samkeiten zerrinnen vor der Erkenntnis, wenn man nicht zu gleicher Zeit den Blick unbefangen auf die Wirklichkeit des Fühlens und Wollens richtet."
      ],
      [
        "Man kommt durch solches"
      ],
      [
        "Zerrinnen zu keiner wirklichkeitsgemäßen Zuordnung des Fühlens und Wollens zu den leiblichen Vorgängen. - Der Leib als Ganzes, nicht bloß die in ihm eingeschlossene Ner­ventätigkeit ist physische Grundlage des Seelenlebens.",
        "Und wie das letztere für das gewöhnliche Bewußtsein sich um­schreiben läßt durch Vorstellen, Fühlen und Wollen, so das leibliche Leben durch Nerventätigkeit, rhythmisches Ge­schehen und Stoffwechselvorgänge. - Sogleich entsteht da die Frage: wie ordnen sich in den Organismus ein auf der einen Seite die eigentliche Sinneswahrnehmung, in welche die Nerventätigkeit nur ausläuft, und wie die Bewegungs­fähigkeit auf der andern Seite, in welche das Wollen mün­det?"
      ],
      [
        "Unbefangene Beobachtung zeigt, daß beides nicht in demselben Sinne zum Organismus gehört wie Nerventätig­keit, rhythmisches Geschehen und Stoffwechselvorgänge.",
        "Was im Sinn geschieht ist etwas, das gar nicht unmittelbar dem Organismus angehört."
      ],
      [
        "In die Sinne erstreckt sich die Außenwelt wie in Golfen hinein in das Wesen des Organis­mus.",
        "Indem die Seele das im Sinne vor sich gehende Ge­schehen umspannt, nimmt sie nicht an einem inneren orga­nischen Geschehen teil, sondern an der Fortsetzung des äu­ßeren Geschehens in den Organismus hinein. (Ich habe diese Verhältnisse erkenntnis kritisch in einem Vortrag für den Bologner Philosophen-Kongreß des Jahres 1911 erör­tert.) - Und in einem Bewegungsvorgang hat man es phy­sisch auch nicht mit etwas zu tun, dessen Wesenhaftes inner­halb des Organismus liegt, sondern mit einer Wirksamkeit des Organismus in den Gleichgewichts- und Kräfteverhältnissen, in die der Organismus gegenüber der Außenwelt hineingestellt ist."
      ],
      [
        "Innerhalb des Organismus ist dem Wollen nur ein Stoffwechselvorgang zuzueignen; aber das durch"
      ],
      [
        "diesen Vorgang ausgelöste Geschehen ist zugleich ein We­senhaftes innerhalb der Gleichgewichts- und Kräfteverhältnisse der Außenwelt; und die Seele übergreift, indem sie sich wollend betätigt, den Bereich des Organismus und lebt mit ihrem Tun das Geschehen der Außenwelt mit.",
        "Eine große Verwirrung hat für die Betrachtung aller dieser Dinge die Gliederung der Nerven in Empfindungs- und motori­sche Nerven angerichtet.",
        "So fest verankert diese Gliederung in den gegenwärtigen physiologischen Vorstellungen er­scheint: sie ist nicht in der unbefangenen Beobachtung be­gründet.",
        "Was die Physiologie vorbringt auf Grund der Zer­schneidung der Nerven, oder der krankhaften Ausschal­tung gewisser Nerven beweist nicht, was auf Grundlage des Versuches oder der Erfahrung sich ergibt, sondern etwas ganz anderes.",
        "Es beweist, daß der Unterschied gar nicht be­steht, den man zwischen Empfindungs- und motorischen Nerven annimmt.",
        "Beide Nervenarten sind vielmehr Wesens­gleich.",
        "Der sogenannte motorische Nerv dient nicht in dem Sinne der Bewegung wie die Lehre von dieser Gliederung es annimmt, sondern als Träger der Nerventätigkeit dient er der inneren Wahrnehmung desjenigen Stoffwechselvorganges, der dem Wollen zugrunde liegt, geradeso wie der Empfin­dungsnerv der Wahrnehmung desjenigen dient, was im Sin­nesorgan sich abspielt.",
        "Bevor die Nervenlehre in dieser Be­ziehung mit klaren Begriffen arbeitet, wird eine richtige Zu­ordnung des Seelenlebens zum Leibesleben nicht zustande"
      ],
      [
        "In ähnlicher Art, wie man psycho-physiologisch die Bezie­hungen des in Vorstellen, Fühlen und Wollen verlaufenden Seelenlebens zum Leibesleben suchen kann, so kann man"
      ],
      [
        "anthroposophisch nach Erkenntnis der Beziehungen stre­ben, welche das Seelische des gewöhnlichen Bewußtseins zum Geistesleben hat.",
        "Und da findet man durch die in dieser und in meinen anderen Schriften geschilderten anthroposo­phischen Methoden, daß sich für das Vorstellen wie im Leibe die Nerventätigkeit, so im Geistigen eine Grundlage findet."
      ],
      [
        "Die Seele steht nach der anderen, vom Leibe abge­wandten, Seite in Beziehung zu einem geistig Wesenhaften, das die Grundlage ist für das Vorstellen des gewöhnlichen Bewußtseins.",
        "Dieses geistig Wesenhafte kann aber nur durch schauendes Erkennen erlebt werden."
      ],
      [
        "Und es wird so erlebt, indem sich sein Inhalt als gegliederte Imaginationen dem schauenden Bewußtsein darstellt.",
        "Wie nach dem Leibe hin das Vorstellen auf der Nerventätigkeit ruht, so strömt es von der andern Seite her aus einem geistig Wesenhaften, das in Imaginationen sich enthüllt."
      ],
      [
        "Dieses geistig Wesenhafte ist, was in meinen Schriften der Äther- oder Lebensleib ge­nannt wird. (Wobei, wenn ich es bespreche, ich immer dar­auf aufmerksam mache, daß man sich an dem Ausdruck «Leib» ebensowenig wie an dem andern «Äther» stoßen solle, denn, was ich ausführe, zeigt klar, daß man das Ge­meinte nicht im materialistischen Sinne deuten soll.) Und dieser Lebensleib (in dem 4.",
        "Buch des 1."
      ],
      [
        "Jahrganges der Zeit­schrift «Das Reich» habe ich auch den Ausdruck «Bilde­kräfteleib» gebraucht) ist das Geistige, aus dem das Vor­stellungsleben des gewöhnlichen Bewußtseins von der Ge­burt (beziehungsweise Empfängnis) bis zum Tode erfließt. -Das Fühlen des gewöhnlichen Bewußtseins ruht nach der Leibesseite hin auf dem rhythmischen Geschehen.",
        "Von der geistigen Seite her erfließt es aus einem Geistig-Wesenhaf­ten, das innerhalb der anthroposophischen Forschung"
      ],
      [
        "durch Methoden gefunden wird, welche ich in meinen Schriften als diejenigen der Inspiration kennzeichne. (Wo­bei man wieder berücksichtigen möge, daß ich innerhalb dieses Begriffes nur das von mir Umschriebene verstehe, so daß man meine Bezeichnung nicht verwechseln sollte mit dem, was oft vom Laien bei diesem Worte verstanden wird.) Dem schauenden Bewußtsein offenbart sich in dem der Seele zugrunde liegenden, durch Inspirationen zu erfassen­den geistig Wesenhaften dasjenige, was dem Menschen als Geistwesen eigen ist über Geburt und Tod hinaus.",
        "Auf die­sem Gebiete ist es, wo die Anthroposophie ihre geisteswis­senschaftlichen Untersuchungen über die Unsterblichkeits­frage anstellt."
      ],
      [
        "So wie im Leibe durch das rhythmische Geschehen sich der sterbliche Teil des fühlenden Menschenwesens offenbart, so in dem Inspirations-Inhalt des schauenden Bewußtseins der unsterbli­che geistige Seelenwesenskern. - Das Wollen, das nach dem Leibe hin auf den Stoffwechselvorgängen beruht, erströmt aus dem Geiste für das schauende Bewußtsein durch dasjenige, was ich in meinen Schriften die wahrhaftigen Intuitionen nenne.",
        "Was im Leibe durch die gewissermaßen niederste Be­tätigung des Stoffwechsels sich offenbart, dem entspricht im Geiste ein Höchstes: dasjenige, was durch Intuitionen sich ausspricht."
      ],
      [
        "Daher kommt das Vorstellen, das auf der Ner­ventätigkeit beruht, leiblich fast vollkommen zur Darstel­lung; das Wollen hat in den ihm leiblich zugeordneten Stoff­wechselvorgängen nur einen schwachen Abglanz.",
        "Das wirkliche Vorstellen ist das lebendige; das leiblich bedingte ist das abgelähmte."
      ],
      [
        "Der Inhalt ist derselbe.",
        "Das wirkliche Wollen, auch das in der physischen Welt sich verwirkli­chende, verläuft in den Regionen, die nur dem intuitiven Schauen zugänglich sind; sein leibliches Gegenstück hat mit"
      ],
      [
        "seinem Inhalte fast gar nichts zu tun.",
        "In demjenigen geistig Wesenhaften, das der Intuition sich offenbart, ist enthalten, was sich aus vorangegangenen Erdenleben in die folgenden hinübererstreckt.",
        "Und auf dem hier in Betracht kommenden Gebiet ist es, wo die Anthroposophie sich den Fragen der wiederholten Erdenleben und der Schicksalsfrage nähert."
      ],
      [
        "Wie der Leib in Nerventätigkeit, rhythmischem Geschehen und Stoffwechselvorgängen sich auslebt, so der Geist des Menschen in demjenigen, was in Imaginationen, Inspiratio­nen, Intuitionen sich offenbart.",
        "Und wie der Leib in sei­nem Bereich nach zwei Seiten das Wesen seiner Außenwelt miterleben läßt, nämlich in den Sinnes- und den Bewe­gungsvorgängen, so der Geist nach der einen Seite hin, in­dem er das vorstellende Seelenleben auch im gewöhnlichen Bewußtsein imaginativ erlebt; und nach der andern Seite hin, indem er im Wollen intuitive Impulse ausgestaltet, die sich durch Stoffwechselvorgänge verwirklichen."
      ],
      [
        "Sieht man nach dem Leibe hin, so findet man die Nerventätigkeit, die als Vorstellungswesen lebt; sieht man nach dem Geiste hin, so gewahrt man den Geist-Inhalt der Imaginationen, der in eben dieses Vorstellungswesen einfließt.",
        "Brentano empfin­det zunächst die geistige Seite am vorstellenden Seelenle­ben; daher charakterisiert er dieses Leben als Bildleben (imaginatives Geschehen)."
      ],
      [
        "Aber wenn nicht bloß ein eige­nes Seelen-Inneres erlebt wird, sondern durch das Urteil ein Anzuerkennendes oder zu Verwerfendes, so kommt zum Vorstellen hinzu ein aus dem Geiste fließendes Seelenerleb­nis, dessen Inhalt unbewußt bleibt, so lange es sich nur um das gewöhnliche Bewußtsein handelt, weil er in den Imaginationen von einer dem physischen Objekte zugrunde lie­genden geistigen Wesenhaftigkeit besteht, die zu der Vorstellung"
      ],
      [
        "nur das hinzufügen, daß deren Inhalt existiert.",
        "Aus diesem Grunde ist es, daß Brentano das Vorstellungsleben in seiner Klassifikation spaltet, in das bloße Vorstellen, das nur innerlich Daseiendes imaginativ erlebt; und in das Urteilen, das von außen Gegebenes imaginativ erlebt, aber das Erleb­nis nur als Anerkennung oder Verwerfung sich zum Be­wußtsein bringt.",
        "Gegenüber dem Fühlen blickt Brentano gar nicht nach der Leibes-Grundlage, dem rhythmischen Geschehen hin, sondern er versetzt nur dasjenige in den Be­reich seiner Aufmerksamkeit, was aus unbewußt bleiben­den Inspirationen im Gebiet des gewöhnlichen Bewußt­seins als Lieben und Hassen auftritt.",
        "Das Wollen aber entfällt ganz seiner Aufmerksamkeit, weil dieses sich nur auf Er­scheinungen in der Seele richten will, in dem Wollen aber et­was liegt, was nicht in der Seele beschlossen ist, sondern mit dem die Seele eine Außenwelt miterlebt.",
        "Die Brentanosche Klassifikation der Seelenphänomene beruht also darauf, daß er diese nach Gesichtspunkten gliedert, die ihre wahre Be­leuchtung erfahren, wenn man den Blick nach dem Geist-Kerne der Seele lenkt, und daß er doch damit treffen will die Phänomene des gewöhnlichen Bewußtseins.",
        "Mit dem hier über Brentano Gesagten habe ich noch ergänzen wollen das oben Seite 90 ff. in dieser Beziehung über ihn Ausgespro­chene."
      ]
    ]
  },
  {
    "order": 11,
    "title_de": "7.    Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano",
    "paragraphs": [
      "7.    Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano",
      "Zu Seite 86, Anmerkung zu Zeile 12 von oben",
      "Brentano zeigt durch verschiedene Ausführungen, wie stark er nach einer klaren Sonderung des Seelischen von dem",
      "Außer-Seelischen strebte. Der in dieser Schriftgekennzeich­nete Seelenbegriff, den er hat, zwingt ihn dazu. Man richte, um das zu sehen, den Blick auf die Art, wie er das Seelen-Erlebnis zu umschreiben versucht, das in dem Bilden der Überzeugung von einer Wahrheit vorliegt.",
      "Er fragt sich: woher rührt, was die Seele als Überzeugung erlebt, die sie an einen Vorstellungs-Inhalt knüpft? Einige Denker glau­ben, daß der Überzeugungsgrad einer Wahrheit gegenüber in einer gefühlten Intensität bestehe, mit der man den ent­sprechenden Vorstellungs-Inhalt erlebt.",
      "Brentano sagt darüber: «Es ist falsch, aber ein Irrtum, dem fast allgemein ge­huldigt wird, und von dem auch ich, als ich den ersten Band der Psychologie schrieb, mich noch nicht befreit hatte, daß der sogenannte Grad der Überzeugung eine Intensitätsstufe des Urteilens sei, welche mit der Intensität von Lust und Schmerz in Analogie gebracht werden könnte. Hätte Win­delband diesen Irrtum mir vorgehalten, so würde ich ihm ganz und vollkommen recht geben.",
      "Nun aber tadelt er mich, weil ich eine Intensität nur in analogem, nicht aber in glei­chem Sinne bei der Überzeugung anerkennen wollte, und weil ich die angebliche Intensität der Überzeugung und die wahrhafte Intensität des Gefühls der Größe nach für unver­gleichbar erklärte. Da haben wir eine der Folgen seiner ver­besserten Auffassung des Urteils. - Wäre der Überzeu­gungsgrad meines Glaubens, daß 2+1 = 3 sei, eine Intensi­tät, wie mächtig müßte diese dann sein!",
      "Und wenn nun gar dieser Glaube mit Windelband zu einem Gefühl gemacht, nicht bloß dem Gefühl analog gedacht werden dürfte, wie zerstörend für unser Nervensystem müßte die Heftigkeit der Gefühlserschütterung werden! Jeder Arzt würde vor dem Studium der Mathematik als etwas Gesundheitszerrüttendem",
      "warnen müssen» (Seite 57 f. von Brentanos «Vom Ursprung sittlicher Erkenntnis»). Hätte Brentano weiter durchleben können, was in diesem Streben nach dem Wesen der Überzeugung in ihm wirkte, er hätte die Sonderung er­blickt, die sich zwischen dem vorstellenden Seelischen er­gibt, das in sich selbst keine Intensität erlebt, wenn eine Überzeugung gebildet wird, und dem Außer-Seelischen, das in den Inhalt des Seelischen eingeht, und das in der In­tensität des Überzeugungsgrades auch in der Seele ein Au­ßerseelisches bleibt, so daß das Innenleben den Überzeu­gungsgrad zwar anschaut, aber nicht mit ihm lebt.",
      "Auf ein ähnliches Gebiet einer scharfen Sonderung des Seelischen vom Außer-Seelischen gehört, was Brentano in seiner Abhandlung «Über Individuation, multiple Qualität und Intensität sinnlicher Erscheinungen» (Seite 5 1ff. seiner Schrift «Untersuchungen zur Sinnespsychologie») vorbringt. Er bemüht sich da, zu zeigen, wie dem eigentlich Seelischen eine Intensität nicht innewohnend ist, und wie der Intensitätsgrad der seelischen Empfindung ein Leben des außerseelischen Empfundenen auf dem Schauplatze des Seelischen ist. Daß man durchaus nicht ins «mystische Dun­kel» der Unwissenschaftlichkeit kommen muß, wenn man sich bemüht, die in solchen elementarischen Einsichten ge­legenen Keime erkennend weiter zu entwickeln, empfindet Brentano. Deshalb schreibt er am Ende der genannten Ab­handlung (Seite 77f.): «Was das dann weiter bedeuten wer­de, ist wohl leicht ersichtlich. - Wie viel hatte nicht die Her­bartsche Psychologie, wie viel nicht auch die Psychophysik auf dieses Dogma (er meint das Dogma von der Intensität im Seelischen) gebaut! Alles das wird im Sturze mitgerissen werden. Und wir sehen so, wie die Berichtigung eines kleinen",
      "Punktes der Empfindungslehre einen weittragenden re­formatorischen Einfluß üben wird. - Selbst die Hypothesen, welche man über das Weltganze aufgestellt hat, werden davon nicht unberührt bleiben. - Man hat für die beiden Gebiete des Psychischen und Physischen vielfach eine durchgängige Analogie behauptet; den Nachweis dafür freilich nicht er­bracht oder auch nur ernstlich zu erbringen versucht. Man hielt sich ganz im allgemeinen und da konnte denn der Ge­danke an die Intensität als eine Art Größe, die jedem Psychi­schen, wie die räumliche jedem Körperlichen eigen sei, der ihm zugedachten Rolle genügen. - Behauptete man aber einmal durchgängige Analogie von Psychischem und Phy­sischem, warum nicht lieber geradezu ihre Identität behaup­ten oder das eine dem anderen einfach substituieren? - In allem dem Physischen analog und in sich selbst allein durch evidente Wahrnehmung gewährleistet, muß das Psychische jede hypothetische Annahme eines Physischen überflüssig erscheinen lassen. - So klingt denn unter anderem auch die Wundtsche Psychologie in dem Gedanken aus, daß man die Annahme einer physischen Welt, nachdem man ihn eine zeitlang heuristisch verwertet, schließlich wie ein Gerüst fallen lassen könne, wo dann das Ganze der echten Wahr­heit als rein psychisches Weltgebäude sich enthülle. - Dieser Gedanke hatte wohl auch bisher wenig Aussicht, jemals eine greifbare Gestalt und eine Durchbildung ins einzelne zu gewinnen.",
      "Die neue Auffassung der Intensität aber mit ihrem klaren Nachweis, daß eine intensive Größe nichts we­niger als universell den psychischen Tätigkeiten eigen ge­nannt werden kann, macht die Hoffnung, daß es einmal zu einer solchen kommen werde, vollends zunichte. - Den Glauben an den wahren Bestand einer Körperwelt werden wir uns",
      "also nicht nehmen lassen, und er wird für die Naturwissenschaft immer die Hypothese aller Hypothesen bleiben.» Nach einer durchgängigen Analogie von Psychischem und Physischem, die Brentano ablehnt, sucht nur derjenige, welcher nicht danach strebt, das Psychische auf der einen Seite, das Phy­sische auf der andern in klarer Weise vorzustellen, sondern der dafür, sich mit seinen Begriffen am Physischen fortta­stend, dem Psychischen solche Erlebnisse wie das der Inten­sität zuschiebt, während im rein Seelischen nichts davon ge­funden werden kann. Mir scheint, daß dieser oben ange­führte Brentanosche Gedanke noch genauer zum Vorschein gekommen wäre, wenn sein Träger im Sinne des in dieser Schrift Seite 85 f.",
      "Dargestellten die Aufmerksamkeit ge­lenkt hätte auf das Merkmal des Physischen, das dem Inten­tionellen im Psychischen an Bedeutung gleichkommt. - Doch ist schon bedeutsam, daß Brentano den Ausblick wagt von den elementaren Einsichten zu Anschauungen über weiter gehende Welträtsel. Denn die Denkungsart der neueren Zeit ist solchen Ausblicken abgeneigt.",
      "Ich gebe ein Beispiel für viele. Der bedeutende Psychologe Fortlage zeigt an einer Stelle seiner «Acht psychologischen Vorträge» (Jena 1869), wie nahe er mit seinem ahnenden Erkennen ei­nem gewissen Gebiete des schauenden Bewußtseins war, nämlich der Erkennmis von der ablähmenden Kraft des im gewöhnlichen Bewußtsein lebenden Seelendaseins.",
      "Er schreibt (Seite 35 der genannten Schrift): «Wenn wir uns lebendige Wesen nennen, und so uns eine Eigenschaft beile­gen, die wir mit Tieren und Pflanzen teilen, so verstehen wir unter dem lebendigen Zustand notwendig etwas, das uns nie verläßt, und sowohl im Schlaf als im Wachen stets in uns fortdauert. Dies ist das vegetative Leben der Ernährung unseres",
      "Organismus, ein unbewußtes Leben, ein Leben des Schlafs. Das Gehirn macht hier dadurch eine Ausnahme, daß dieses Leben der Ernährung, dieses Schlafleben bei ihm in den Pausen des Wachens überwogen wird von dem Le­ben der Verzehrung» (von mir in dieser Schrift «Herabläh­mung» genannt).",
      "«In diesen Pausen steht das Gehirn einer überwiegenden Verzehrung preisgegeben, und gerät folg­lich in einen Zustand, welcher, wenn er sich auf die übrigen Organe miterstreckte, die absolute Entkräftigung des Lei­bes oder den Tod zu Wege bringen würde.» Und diesen Ge­danken zu Ende führend, sagt Fortlage (Seite 39):« Das Be­wußtsein ist ein kleiner und partieller Tod, der Tod ist ein großes und totales Bewußtsein, ein Erwachen des ganzen We­sens in seinen innersten Tiefen.» Man kann nur sagen: Fortlage steht mit solchen Gedanken am Ausgangspunkte der An­throposophie, auch wenn er - wie Brentano - in sie nicht eintritt. Doch selbst wegen dieses Stehens am Ausgangspunkte findet der im Banne der neueren Vorstellungsart ste­hende Eduard von Hartmann, daß solch ein Ausblick von elementarischer Erkennmis zu dem großen Welträtsel der Unsterblichkeit wissenschaftlich unstatthaft ist.",
      "Eduard von Hartmann schreibt über Fortlage: «Er überschreitet aber die Grenzen der Psychologie, wenn er das Bewußtsein als kleinen und partiellen Tod, den Tod als großes und tota­les Bewußtsein, als ein helleres, gänzliches Erwachen der Seele in ihren Tiefen bezeichnet ...» (Vergleiche Eduard von Hartmann, «Die moderne Psychologie», Leipzig, 1901, Hermann Haackes Verlag, Seite 48 f.)"
    ],
    "sentences": [
      [
        "Die Sonderung des Seelischen von dem Außer-Seelischen durch Franz Brentano"
      ],
      [
        "Zu Seite 86, Anmerkung zu Zeile 12 von oben"
      ],
      [
        "Brentano zeigt durch verschiedene Ausführungen, wie stark er nach einer klaren Sonderung des Seelischen von dem"
      ],
      [
        "Außer-Seelischen strebte.",
        "Der in dieser Schriftgekennzeich­nete Seelenbegriff, den er hat, zwingt ihn dazu.",
        "Man richte, um das zu sehen, den Blick auf die Art, wie er das Seelen-Erlebnis zu umschreiben versucht, das in dem Bilden der Überzeugung von einer Wahrheit vorliegt."
      ],
      [
        "Er fragt sich: woher rührt, was die Seele als Überzeugung erlebt, die sie an einen Vorstellungs-Inhalt knüpft?",
        "Einige Denker glau­ben, daß der Überzeugungsgrad einer Wahrheit gegenüber in einer gefühlten Intensität bestehe, mit der man den ent­sprechenden Vorstellungs-Inhalt erlebt."
      ],
      [
        "Brentano sagt darüber: «Es ist falsch, aber ein Irrtum, dem fast allgemein ge­huldigt wird, und von dem auch ich, als ich den ersten Band der Psychologie schrieb, mich noch nicht befreit hatte, daß der sogenannte Grad der Überzeugung eine Intensitätsstufe des Urteilens sei, welche mit der Intensität von Lust und Schmerz in Analogie gebracht werden könnte.",
        "Hätte Win­delband diesen Irrtum mir vorgehalten, so würde ich ihm ganz und vollkommen recht geben."
      ],
      [
        "Nun aber tadelt er mich, weil ich eine Intensität nur in analogem, nicht aber in glei­chem Sinne bei der Überzeugung anerkennen wollte, und weil ich die angebliche Intensität der Überzeugung und die wahrhafte Intensität des Gefühls der Größe nach für unver­gleichbar erklärte.",
        "Da haben wir eine der Folgen seiner ver­besserten Auffassung des Urteils. - Wäre der Überzeu­gungsgrad meines Glaubens, daß 2+1 = 3 sei, eine Intensi­tät, wie mächtig müßte diese dann sein!"
      ],
      [
        "Und wenn nun gar dieser Glaube mit Windelband zu einem Gefühl gemacht, nicht bloß dem Gefühl analog gedacht werden dürfte, wie zerstörend für unser Nervensystem müßte die Heftigkeit der Gefühlserschütterung werden!",
        "Jeder Arzt würde vor dem Studium der Mathematik als etwas Gesundheitszerrüttendem"
      ],
      [
        "warnen müssen» (Seite 57 f. von Brentanos «Vom Ursprung sittlicher Erkenntnis»).",
        "Hätte Brentano weiter durchleben können, was in diesem Streben nach dem Wesen der Überzeugung in ihm wirkte, er hätte die Sonderung er­blickt, die sich zwischen dem vorstellenden Seelischen er­gibt, das in sich selbst keine Intensität erlebt, wenn eine Überzeugung gebildet wird, und dem Außer-Seelischen, das in den Inhalt des Seelischen eingeht, und das in der In­tensität des Überzeugungsgrades auch in der Seele ein Au­ßerseelisches bleibt, so daß das Innenleben den Überzeu­gungsgrad zwar anschaut, aber nicht mit ihm lebt."
      ],
      [
        "Auf ein ähnliches Gebiet einer scharfen Sonderung des Seelischen vom Außer-Seelischen gehört, was Brentano in seiner Abhandlung «Über Individuation, multiple Qualität und Intensität sinnlicher Erscheinungen» (Seite 5 1ff. seiner Schrift «Untersuchungen zur Sinnespsychologie») vorbringt.",
        "Er bemüht sich da, zu zeigen, wie dem eigentlich Seelischen eine Intensität nicht innewohnend ist, und wie der Intensitätsgrad der seelischen Empfindung ein Leben des außerseelischen Empfundenen auf dem Schauplatze des Seelischen ist.",
        "Daß man durchaus nicht ins «mystische Dun­kel» der Unwissenschaftlichkeit kommen muß, wenn man sich bemüht, die in solchen elementarischen Einsichten ge­legenen Keime erkennend weiter zu entwickeln, empfindet Brentano.",
        "Deshalb schreibt er am Ende der genannten Ab­handlung (Seite 77f.): «Was das dann weiter bedeuten wer­de, ist wohl leicht ersichtlich. - Wie viel hatte nicht die Her­bartsche Psychologie, wie viel nicht auch die Psychophysik auf dieses Dogma (er meint das Dogma von der Intensität im Seelischen) gebaut!",
        "Alles das wird im Sturze mitgerissen werden.",
        "Und wir sehen so, wie die Berichtigung eines kleinen"
      ],
      [
        "Punktes der Empfindungslehre einen weittragenden re­formatorischen Einfluß üben wird. - Selbst die Hypothesen, welche man über das Weltganze aufgestellt hat, werden davon nicht unberührt bleiben. - Man hat für die beiden Gebiete des Psychischen und Physischen vielfach eine durchgängige Analogie behauptet; den Nachweis dafür freilich nicht er­bracht oder auch nur ernstlich zu erbringen versucht.",
        "Man hielt sich ganz im allgemeinen und da konnte denn der Ge­danke an die Intensität als eine Art Größe, die jedem Psychi­schen, wie die räumliche jedem Körperlichen eigen sei, der ihm zugedachten Rolle genügen. - Behauptete man aber einmal durchgängige Analogie von Psychischem und Phy­sischem, warum nicht lieber geradezu ihre Identität behaup­ten oder das eine dem anderen einfach substituieren? - In allem dem Physischen analog und in sich selbst allein durch evidente Wahrnehmung gewährleistet, muß das Psychische jede hypothetische Annahme eines Physischen überflüssig erscheinen lassen. - So klingt denn unter anderem auch die Wundtsche Psychologie in dem Gedanken aus, daß man die Annahme einer physischen Welt, nachdem man ihn eine zeitlang heuristisch verwertet, schließlich wie ein Gerüst fallen lassen könne, wo dann das Ganze der echten Wahr­heit als rein psychisches Weltgebäude sich enthülle. - Dieser Gedanke hatte wohl auch bisher wenig Aussicht, jemals eine greifbare Gestalt und eine Durchbildung ins einzelne zu gewinnen."
      ],
      [
        "Die neue Auffassung der Intensität aber mit ihrem klaren Nachweis, daß eine intensive Größe nichts we­niger als universell den psychischen Tätigkeiten eigen ge­nannt werden kann, macht die Hoffnung, daß es einmal zu einer solchen kommen werde, vollends zunichte. - Den Glauben an den wahren Bestand einer Körperwelt werden wir uns"
      ],
      [
        "also nicht nehmen lassen, und er wird für die Naturwissenschaft immer die Hypothese aller Hypothesen bleiben.» Nach einer durchgängigen Analogie von Psychischem und Physischem, die Brentano ablehnt, sucht nur derjenige, welcher nicht danach strebt, das Psychische auf der einen Seite, das Phy­sische auf der andern in klarer Weise vorzustellen, sondern der dafür, sich mit seinen Begriffen am Physischen fortta­stend, dem Psychischen solche Erlebnisse wie das der Inten­sität zuschiebt, während im rein Seelischen nichts davon ge­funden werden kann.",
        "Mir scheint, daß dieser oben ange­führte Brentanosche Gedanke noch genauer zum Vorschein gekommen wäre, wenn sein Träger im Sinne des in dieser Schrift Seite 85 f."
      ],
      [
        "Dargestellten die Aufmerksamkeit ge­lenkt hätte auf das Merkmal des Physischen, das dem Inten­tionellen im Psychischen an Bedeutung gleichkommt. - Doch ist schon bedeutsam, daß Brentano den Ausblick wagt von den elementaren Einsichten zu Anschauungen über weiter gehende Welträtsel.",
        "Denn die Denkungsart der neueren Zeit ist solchen Ausblicken abgeneigt."
      ],
      [
        "Ich gebe ein Beispiel für viele.",
        "Der bedeutende Psychologe Fortlage zeigt an einer Stelle seiner «Acht psychologischen Vorträge» (Jena 1869), wie nahe er mit seinem ahnenden Erkennen ei­nem gewissen Gebiete des schauenden Bewußtseins war, nämlich der Erkennmis von der ablähmenden Kraft des im gewöhnlichen Bewußtsein lebenden Seelendaseins."
      ],
      [
        "Er schreibt (Seite 35 der genannten Schrift): «Wenn wir uns lebendige Wesen nennen, und so uns eine Eigenschaft beile­gen, die wir mit Tieren und Pflanzen teilen, so verstehen wir unter dem lebendigen Zustand notwendig etwas, das uns nie verläßt, und sowohl im Schlaf als im Wachen stets in uns fortdauert.",
        "Dies ist das vegetative Leben der Ernährung unseres"
      ],
      [
        "Organismus, ein unbewußtes Leben, ein Leben des Schlafs.",
        "Das Gehirn macht hier dadurch eine Ausnahme, daß dieses Leben der Ernährung, dieses Schlafleben bei ihm in den Pausen des Wachens überwogen wird von dem Le­ben der Verzehrung» (von mir in dieser Schrift «Herabläh­mung» genannt)."
      ],
      [
        "«In diesen Pausen steht das Gehirn einer überwiegenden Verzehrung preisgegeben, und gerät folg­lich in einen Zustand, welcher, wenn er sich auf die übrigen Organe miterstreckte, die absolute Entkräftigung des Lei­bes oder den Tod zu Wege bringen würde.» Und diesen Ge­danken zu Ende führend, sagt Fortlage (Seite 39):« Das Be­wußtsein ist ein kleiner und partieller Tod, der Tod ist ein großes und totales Bewußtsein, ein Erwachen des ganzen We­sens in seinen innersten Tiefen.» Man kann nur sagen: Fortlage steht mit solchen Gedanken am Ausgangspunkte der An­throposophie, auch wenn er - wie Brentano - in sie nicht eintritt.",
        "Doch selbst wegen dieses Stehens am Ausgangspunkte findet der im Banne der neueren Vorstellungsart ste­hende Eduard von Hartmann, daß solch ein Ausblick von elementarischer Erkennmis zu dem großen Welträtsel der Unsterblichkeit wissenschaftlich unstatthaft ist."
      ],
      [
        "Eduard von Hartmann schreibt über Fortlage: «Er überschreitet aber die Grenzen der Psychologie, wenn er das Bewußtsein als kleinen und partiellen Tod, den Tod als großes und tota­les Bewußtsein, als ein helleres, gänzliches Erwachen der Seele in ihren Tiefen bezeichnet ...» (Vergleiche Eduard von Hartmann, «Die moderne Psychologie», Leipzig, 1901, Hermann Haackes Verlag, Seite 48 f.)"
      ]
    ]
  },
  {
    "order": 12,
    "title_de": "8. Ein oft erhobener Einwand gegen die Anthroposophie",
    "paragraphs": [
      "8. Ein oft erhobener Einwand gegen die Anthroposophie",
      "Zu Seite 110, Anmerkung zu Zeile 6 von oben",
      "Es wird oft ein Einwand gegen die Anthroposophie erho­ben, der ebenso begreiflich aus der Seelenstimmung der Persönlichkeiten heraus ist, von denen er kommt, wie er unberechtigt ist gegenüber dem Geiste, aus dem heraus das anthroposophische Forschen angestellt wird. Mir erscheint er deshalb ganz unbeträchtlich, weil die Widerlegung für je­den nahe liegt, der mit wirklichem Verständnisse den vom anthroposophischen Gesichtspunkte gegebenen Darstel­lungen folgt.",
      "Nur weil er immer von neuem auftritt, sage ich hier einiges über ihn, wie ich es auch schon in der 6. Auflage meiner «Theosophie», am Schlusse, 1914 getan habe. - Es wird, um diesen Einwand aufzustellen, gefordert, daß die geistigen Beobachtungsergebnisse, die von der Anthropo-sophie vorgebracht werden, im Sinne der rein naturwissen­schaftlichen Experimentiermethode «bewiesen» werden sollen.",
      "Man stellt sich etwa vor, einige Personen, die be­haupten, sie können zu solchen Ergebnissen kommen, wer­den einer Anzahl anderer Personen in einem regelrecht an­geordneten Experiment gegenübergesetzt, und die «Gei­stesforscher» hätten dann anzugeben, was sie an den zu un­tersuchenden Personen «geschaut» haben. Ihre Angaben müßten dann übereinstimmen, oder doch wenigstens in ei­nem genügend großen Prozentsatze sich ähnlich sein.",
      "Man kann begreifen, daß, wer Anthroposophie nur kennt, ohne sie verstanden zu haben, eine solche Forderung immer wie­der erhebt, denn durch deren Erfüllung würde ihm erspart, sich zu dem richtigen Beweiswege durchzuarbeiten, der in der Aneignung des jedem erreichbaren eigenen Schauens be­steht.",
      "Wer aber Anthroposophie wirklich verstanden hat, der hat auch die Einsicht, daß ein in der angedeuteten Art angestelltes Experiment zur Gewinnung wahrhaft geistiger Anschauungsergebnisse ungefähr ebenso geeignet ist wie zur Beobachtung der Zeit an einer Uhr die Stillesetzung der Zeiger. Denn zur Herbeiführung der Bedingungen, unter denen Geistiges geschaut werden kann, führen Wege, die aus den Verhältnissen des seelischen Lebens selbst sich her­aus ergeben müssen. Äußere Veranstaltungen, wie sie zu einem naturwissenschaftlichen Experiment führen, sind nicht aus solchen Verhältnissen heraus gebildet. Innerhalb dieser Verhältnisse muß zum Beispiel gelegen sein, daß der Willensimpuls, der zum Schauen führt, nur aus dem ureige­nen inneren Impuls desjenigen restlos hervorgeht, der schauen soll. Und daß nicht in künstlichen äußeren Maß-nahmen etwas gegeben ist, was gestaltend in diesen inneren Impuls einfließt. - Es ist eigentlich zu verwundern, daß so wenig berücksichtigt wird, wie doch jedermann sich die Be­weise für die Anthroposophie unmittelbar durch die eigene entsprechende Seelenverfassung verschaffen kann; daß also diese «Beweise»jedermann zugänglich sind. So wenig man dieses wird eingestehen wollen: der Grund des Verlangens nach «äußeren Beweisen» liegt doch nur darinnen, daß diese letztern auf bequemerem Wege zu erreichen wären als auf dem mühsamen, unbequemen, aber wahrhaft geisteswissenschaftlichen.",
      "Auf einem ganz anderen Felde als diese Forderung nach bequemen Experimentalbeweisen für die anthroposophi­schen Wahrheiten liegt, was Brentano wollte, indem er im­mer wieder darnach strebte, in einem psychologischen La­boratorium arbeiten zu können. Die Sehnsucht, ein solches",
      "zur Verfügung zu haben, tritt in seinen Schriften oft zutage. Die Umstände haben tragisch in sein Leben eingegriffen, die ihm ein solches versagt haben. Er würde gerade durch. seine Stellung zu den psychologischen Fragen Wichtigstes durch ein solches Laboratorium geleistet haben. Will man nämlich die beste Grundlage schaffen zu anthropologisch-psycholo­gischen Ergebnissen, die bis an die «Erkenntnis-Grenz­orte» gehen, an denen sich Anthropologie mit Anthroposo­phie treffen muß, so kann dieses durch ein psychologisches Laboratorium geschehen, wie ein solches Brentano in Ge­danken vorgeschwebt hat. Um die Tatsachen des «schauen­den Bewußtseins» herbeizuführen, brauchten in einem sol­chen Laboratorium keine Experimentalmethoden gesucht zu werden; aber durch diejenigen Experimentalmethoden, die gesucht werden, würde sich offenbaren, wie die mensch­liche Wesenheit zu diesem Schauen veranlagt ist, und wie von dem gewöhnlichen das schauende Bewußtsein gefor­dert wird. Jeder, der auf dem anthroposophischen Gesichts­punkt steht, sehnt sich ebenso wie Brentano, in einem ech­ten psychologischen Laboratorium arbeiten zu können, was durch die heute noch gegen die Anthroposophie herrschen­den Vorurteile unmöglich ist."
    ],
    "sentences": [
      [
        "Ein oft erhobener Einwand gegen die Anthroposophie"
      ],
      [
        "Zu Seite 110, Anmerkung zu Zeile 6 von oben"
      ],
      [
        "Es wird oft ein Einwand gegen die Anthroposophie erho­ben, der ebenso begreiflich aus der Seelenstimmung der Persönlichkeiten heraus ist, von denen er kommt, wie er unberechtigt ist gegenüber dem Geiste, aus dem heraus das anthroposophische Forschen angestellt wird.",
        "Mir erscheint er deshalb ganz unbeträchtlich, weil die Widerlegung für je­den nahe liegt, der mit wirklichem Verständnisse den vom anthroposophischen Gesichtspunkte gegebenen Darstel­lungen folgt."
      ],
      [
        "Nur weil er immer von neuem auftritt, sage ich hier einiges über ihn, wie ich es auch schon in der 6.",
        "Auflage meiner «Theosophie», am Schlusse, 1914 getan habe. - Es wird, um diesen Einwand aufzustellen, gefordert, daß die geistigen Beobachtungsergebnisse, die von der Anthropo-sophie vorgebracht werden, im Sinne der rein naturwissen­schaftlichen Experimentiermethode «bewiesen» werden sollen."
      ],
      [
        "Man stellt sich etwa vor, einige Personen, die be­haupten, sie können zu solchen Ergebnissen kommen, wer­den einer Anzahl anderer Personen in einem regelrecht an­geordneten Experiment gegenübergesetzt, und die «Gei­stesforscher» hätten dann anzugeben, was sie an den zu un­tersuchenden Personen «geschaut» haben.",
        "Ihre Angaben müßten dann übereinstimmen, oder doch wenigstens in ei­nem genügend großen Prozentsatze sich ähnlich sein."
      ],
      [
        "Man kann begreifen, daß, wer Anthroposophie nur kennt, ohne sie verstanden zu haben, eine solche Forderung immer wie­der erhebt, denn durch deren Erfüllung würde ihm erspart, sich zu dem richtigen Beweiswege durchzuarbeiten, der in der Aneignung des jedem erreichbaren eigenen Schauens be­steht."
      ],
      [
        "Wer aber Anthroposophie wirklich verstanden hat, der hat auch die Einsicht, daß ein in der angedeuteten Art angestelltes Experiment zur Gewinnung wahrhaft geistiger Anschauungsergebnisse ungefähr ebenso geeignet ist wie zur Beobachtung der Zeit an einer Uhr die Stillesetzung der Zeiger.",
        "Denn zur Herbeiführung der Bedingungen, unter denen Geistiges geschaut werden kann, führen Wege, die aus den Verhältnissen des seelischen Lebens selbst sich her­aus ergeben müssen.",
        "Äußere Veranstaltungen, wie sie zu einem naturwissenschaftlichen Experiment führen, sind nicht aus solchen Verhältnissen heraus gebildet.",
        "Innerhalb dieser Verhältnisse muß zum Beispiel gelegen sein, daß der Willensimpuls, der zum Schauen führt, nur aus dem ureige­nen inneren Impuls desjenigen restlos hervorgeht, der schauen soll.",
        "Und daß nicht in künstlichen äußeren Maß-nahmen etwas gegeben ist, was gestaltend in diesen inneren Impuls einfließt. - Es ist eigentlich zu verwundern, daß so wenig berücksichtigt wird, wie doch jedermann sich die Be­weise für die Anthroposophie unmittelbar durch die eigene entsprechende Seelenverfassung verschaffen kann; daß also diese «Beweise»jedermann zugänglich sind.",
        "So wenig man dieses wird eingestehen wollen: der Grund des Verlangens nach «äußeren Beweisen» liegt doch nur darinnen, daß diese letztern auf bequemerem Wege zu erreichen wären als auf dem mühsamen, unbequemen, aber wahrhaft geisteswissenschaftlichen."
      ],
      [
        "Auf einem ganz anderen Felde als diese Forderung nach bequemen Experimentalbeweisen für die anthroposophi­schen Wahrheiten liegt, was Brentano wollte, indem er im­mer wieder darnach strebte, in einem psychologischen La­boratorium arbeiten zu können.",
        "Die Sehnsucht, ein solches"
      ],
      [
        "zur Verfügung zu haben, tritt in seinen Schriften oft zutage.",
        "Die Umstände haben tragisch in sein Leben eingegriffen, die ihm ein solches versagt haben.",
        "Er würde gerade durch. seine Stellung zu den psychologischen Fragen Wichtigstes durch ein solches Laboratorium geleistet haben.",
        "Will man nämlich die beste Grundlage schaffen zu anthropologisch-psycholo­gischen Ergebnissen, die bis an die «Erkenntnis-Grenz­orte» gehen, an denen sich Anthropologie mit Anthroposo­phie treffen muß, so kann dieses durch ein psychologisches Laboratorium geschehen, wie ein solches Brentano in Ge­danken vorgeschwebt hat.",
        "Um die Tatsachen des «schauen­den Bewußtseins» herbeizuführen, brauchten in einem sol­chen Laboratorium keine Experimentalmethoden gesucht zu werden; aber durch diejenigen Experimentalmethoden, die gesucht werden, würde sich offenbaren, wie die mensch­liche Wesenheit zu diesem Schauen veranlagt ist, und wie von dem gewöhnlichen das schauende Bewußtsein gefor­dert wird.",
        "Jeder, der auf dem anthroposophischen Gesichts­punkt steht, sehnt sich ebenso wie Brentano, in einem ech­ten psychologischen Laboratorium arbeiten zu können, was durch die heute noch gegen die Anthroposophie herrschen­den Vorurteile unmöglich ist."
      ]
    ]
  },
  {
    "order": 13,
    "title_de": "9. Schlußbemerkung",
    "paragraphs": [
      "9. Schlußbemerkung",
      "Auf allerlei «Angriffe», die in letzter Zeit nicht auf die An­throposophie, sondern auf meine Person gemacht worden sind, gehe ich hier nicht ein. Zum Teil ist dies deshalb hier nicht angängig, weil diese «Angriffe» eines wahren wissen­schaftlichen Charakters entbehren; zum Teil sind sie rein",
      "persönlicher Art, beruhen nicht auf sachlichen Grundlagen, sondern auf Gehässigkeit, und in den weitaus meisten Fäl­len wissen die Angreifer ganz gut, daß, was sie behaupten, objektive Unwahrheiten sind."
    ],
    "sentences": [
      [
        "Schlußbemerkung"
      ],
      [
        "Auf allerlei «Angriffe», die in letzter Zeit nicht auf die An­throposophie, sondern auf meine Person gemacht worden sind, gehe ich hier nicht ein.",
        "Zum Teil ist dies deshalb hier nicht angängig, weil diese «Angriffe» eines wahren wissen­schaftlichen Charakters entbehren; zum Teil sind sie rein"
      ],
      [
        "persönlicher Art, beruhen nicht auf sachlichen Grundlagen, sondern auf Gehässigkeit, und in den weitaus meisten Fäl­len wissen die Angreifer ganz gut, daß, was sie behaupten, objektive Unwahrheiten sind."
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

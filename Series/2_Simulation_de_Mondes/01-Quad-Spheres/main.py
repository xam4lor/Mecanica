from manim import *
import math
import random

# Main parameters : (manim main.py MainScene -[flags])
#  -p : open file directly after loading
#  -f : show file in explorer
#  -q {l, m, h, p, k} : low, medium, high, production, 4k

# Default export  command : manim main.py GenerateScenes -f -qk
# Default preview command : manim main.py GenerateScenes -p -lq

# Scenes List : OtherSpheresScene, QuadSphere, Generate3DQuadSphere



class GenerateScenes(ThreeDScene):
    def construct(self):
        # self.Scene2GeneratePointsAndJoinTheme()
        # self.Scene3TransformTrianglesToOther()
        # self.Scene4UVSphere()
        # self.Scene5IcoSphere()
        # self.Scene6QuadSphereText()
        # [pointsInter, textInter] = self.Scene7DrawQuads()
        # self.Scene8moveToArray(pointsInter, textInter)
        # self.Scene9SquareToSphere()
        # self.Scene10DrawCircle()
        # self.Scene11MethodFromSquareToSphere()
        # self.Scene13DrawSurfaceNormals3DTo2D()
        # self.Scene14DrawSpheresNormals()
        self.Scene15DrawQuadTreeText()


    def generateLinesPolygon(self, lod, translation, maxDist1):
        pointsInter = []
        for i in range(0, lod):
            x = (-lod / 2 + lod / (lod - 1) * i) / lod * maxDist1

            for j in range(0, lod):
                y = (-lod / 2 + lod / (lod - 1) * j) / lod * maxDist1
                pointsInter.append([x, y, 0])

        triangList = []

        def drawNextLine(i):
            for j in range(0, lod - 1):
                triangFirst = Polygon(pointsInter[i + j * lod], pointsInter[i + 1 + j * lod],
                                      pointsInter[i + (j + 1) * lod], fill_color=BLUE_D, fill_opacity=0.4,
                                      shade_in_3d=True)
                triangSecon = Polygon(pointsInter[i + (j + 1) * lod], pointsInter[i + 1 + j * lod],
                                      pointsInter[i + 1 + (j + 1) * lod], fill_color=BLUE_E, fill_opacity=0.4,
                                      shade_in_3d=True)

                triangFirst.set_fill(BLUE_D)
                triangSecon.set_fill(BLUE_E)

                triangFirst.move_to([triangFirst.get_x() + translation[0], triangFirst.get_y() + translation[1],
                                     triangFirst.get_z() + translation[2]])
                triangSecon.move_to([triangSecon.get_x() + translation[0], triangSecon.get_y() + translation[1],
                                     triangSecon.get_z() + translation[2]])

                triangList.append(triangFirst)
                triangList.append(triangSecon)

        currentLineID = 0
        for i in range(0, lod - 1):  # 5
            drawNextLine(currentLineID)
            currentLineID += 1

        return triangList


    # Scene 2
    def Scene2GeneratePointsAndJoinTheme(self):
        maxDist1 = 7

        def generatePointsPolygon2(lod, translation):
            pointsInter = []
            for i in range(0, lod):
                x = (-lod / 2 + lod / (lod-1) * i) / lod * maxDist1

                for j in range(0, lod):
                    y = (-lod / 2 + lod / (lod-1) * j) / lod * maxDist1
                    pointsInter.append([x, y, 0])


            pointList = []
            def drawNextLine(i):
                for j in range(0, lod):
                    point = Dot(pointsInter[i + j * lod], color=GREEN_B)
                    point.move_to([point.get_x() + translation[0], point.get_y() + translation[1], point.get_z() + translation[2]])
                    pointList.append(point)

            currentLineID = 0
            for i in range(0, lod):  # 5
                drawNextLine(currentLineID)
                currentLineID += 1

            return pointList

        triangList1 = generatePointsPolygon2(6, [0, 0, -maxDist1])
        self.play(*(DrawBorderThenFill(triangList1[i], run_time=1) for i in range(0, len(triangList1))))

        triangList2 = self.generateLinesPolygon(6, [0, 0, -maxDist1], 7)
        self.play(*(DrawBorderThenFill(triangList2[i], run_time=1.5) for i in range(0, len(triangList2))))
        self.wait(1)
        self.play(
            *(Uncreate(triangList1[i], run_time=2) for i in range(0, len(triangList1))),
            *(Uncreate(triangList2[i], run_time=2) for i in range(0, len(triangList2)))
        )
        self.wait(2)


    # Scene 3
    def Scene3TransformTrianglesToOther(self):
        maxDist2 = 7

        triangList1 = self.generateLinesPolygon(6, [0, 0, -maxDist2], maxDist2)
        self.play(*(DrawBorderThenFill(triangList1[i], run_time=1) for i in range(0, len(triangList1))))
        self.wait(4)

        triangList2 = self.generateLinesPolygon(11, [0, 0, -maxDist2], maxDist2)
        self.play(
            *(Transform(triangList1[i], triangList2[i], run_time=1) for i in range(0, len(triangList1))),
            *(DrawBorderThenFill(triangList2[i], run_time=1) for i in range(len(triangList1), len(triangList2)))
        )
        self.wait(2)

        triangList3 = self.generateLinesPolygon(16, [0, 0, -maxDist2], maxDist2)
        self.play(
            *(Uncreate(triangList1[i], run_time=0.01) for i in range(0, len(triangList1))),
            *(Transform(triangList2[i], triangList3[i], run_time=1) for i in range(0, len(triangList2))),
            *(Create(triangList3[i], run_time=1) for i in range(len(triangList2), len(triangList3)))
        )
        self.wait(2)

        triangList4 = self.generateLinesPolygon(4, [0, 0, -maxDist2], maxDist2)
        self.play(
            *(Uncreate(triangList2[i], run_time=0.01) for i in range(0, len(triangList2))),
            *(Transform(triangList3[i], triangList4[i], run_time=1) for i in range(0, len(triangList4))),
            *(Uncreate(triangList3[i], run_time=1) for i in range(len(triangList4), len(triangList3)))
        )
        self.wait(2)

        self.play(
            *(Uncreate(triangList3[i], run_time=1) for i in range(0, len(triangList3))),
            *(Uncreate(triangList4[i], run_time=1) for i in range(0, len(triangList4)))
        )
        self.wait(2)


    # Scene 4
    def Scene4UVSphere(self):
        uvText = Text("UV-SPHERE", color=YELLOW_D)
        self.play(Write(uvText, run_time=1))
        self.wait(1)

        uvText.generate_target()
        uvText.target.move_to(3*UP)
        uvText.target.scale(0.7)
        lineUVText = Line(LEFT*5 + 2.5*UP, RIGHT*5 + 2.5*UP, color=LIGHT_GRAY)
        self.play(
            MoveToTarget(uvText),
            Create(lineUVText)
        )
        self.wait(1)

        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        nb = 15
        self.begin_ambient_camera_rotation(rate=0.1)

        # Draw latitudes
        curves1 = []
        for i in range(0, nb):
            vS = 2 * i * PI / nb
            curve = ParametricFunction(
                lambda u: np.array([
                    2 * np.cos(vS) * np.cos(u),
                    2 * np.cos(vS) * np.sin(u),
                    2 * np.sin(vS)
                ]), t_min=-PI, t_max=PI, color=BLUE_D
            ).scale(1.1).set_shade_in_3d(True)
            curves1.append(curve)

        self.play(*(
            Create(curves1[i], run_time=0.7)
            for i in range(0, len(curves1))
        ))

        # Draw longitudes
        curves2 = []
        for i in range(0, nb):
            vS = 2 * i * PI / nb
            curve = ParametricFunction(
                lambda u: np.array([
                    2 * np.cos(u) * np.cos(vS),
                    2 * np.cos(u) * np.sin(vS),
                    2 * np.sin(u)
                ]), t_min=-PI, t_max=PI, color=BLUE_D
            ).scale(1.1).set_shade_in_3d(True)
            curves2.append(curve)

        self.play(*(
            Create(curves2[i], run_time=0.7)
            for i in range(0, len(curves2))
        ))

        self.wait(0.5)
        self.move_camera(phi=0.4)

        # Dots at intersections
        dotsList = []
        for i in range(0, nb):
            u = -PI + (2 * PI) / nb * i

            for j in range(0, nb):
                v = -PI + (2 * PI) / nb * j

                dot = Dot([
                    2 * np.cos(u) * np.cos(v),
                    2 * np.cos(u) * np.sin(v),
                    2 * np.sin(u)
                ], color=YELLOW_D, radius=0.05)
                dotsList.append(dot)

        self.play(
            *(
                GrowFromCenter(dotsList[i], run_time=1)
                for i in range(0, len(dotsList))
            ),
            *(
                FadeOut(curves1[i], run_time=1.5)
                for i in range(0, len(curves1))
            ),
            *(
                FadeOut(curves2[i], run_time=1.5)
                for i in range(0, len(curves2))
            )
        )

        self.wait(10.5)
        self.play(
            *(Uncreate(dotsList[i], run_time=1) for i in range(0, len(dotsList))),
            Uncreate(lineUVText),
            Uncreate(uvText)
        )
        self.stop_ambient_camera_rotation()
        self.wait()


    # Scene 5
    def Scene5IcoSphere(self):
        textIco = Text("ICO-SPHERE", color=YELLOW_D)
        self.play(Write(textIco, run_time=1))
        self.wait(1)

        textIco.generate_target()
        textIco.target.move_to(3 * UP)
        textIco.target.scale(0.7)
        lineUVText = Line(LEFT * 5 + 2.5 * UP, RIGHT * 5 + 2.5 * UP, color=LIGHT_GRAY)
        self.play(
            MoveToTarget(textIco),
            Create(lineUVText)
        )
        self.wait(12)

        self.play(
            Uncreate(lineUVText),
            Uncreate(textIco)
        )
        self.wait(2)


    # Scene 6
    def Scene6QuadSphereText(self):
        textQuad = Text("QUAD-SPHERE", color=YELLOW_D)
        self.play(Write(textQuad, run_time=1))
        self.wait(1)

        textQuad.generate_target()
        textQuad.target.move_to(3 * UP)
        textQuad.target.scale(0.7)
        lineUVText = Line(LEFT * 5 + 2.5 * UP, RIGHT * 5 + 2.5 * UP, color=LIGHT_GRAY)
        self.play(
            MoveToTarget(textQuad),
            Create(lineUVText)
        )
        self.wait(12)

        self.play(
            Uncreate(lineUVText),
            Uncreate(textQuad)
        )
        self.wait(2)


    # Scene 7
    def Scene7DrawQuads(self):
        size = 6

        # Quad
        square = Square(size, fill_color=BLUE_A)
        square.set_fill(BLUE_C, opacity=0.6)
        self.play(DrawBorderThenFill(square))
        self.wait(1)

        n = 5
        # Horizontal lines
        lines2 = []
        for j in range(0, n):
            y = -size / 2 + size / n * j
            line = Line([-size / 2, y, 0], [size / 2, y, 0])
            line.set_stroke(color=WHITE)
            lines2.append(line)

        self.play(*(
            Create(lines2[i], run_time=1)
            for i in range(0, len(lines2))
        ))

        # Vertical lines
        lines1 = []
        for i in range(0, n):
            x = -size / 2 + size / n * i
            line = Line([x, -size / 2, 0], [x, size / 2, 0])
            line.set_stroke(color=WHITE)
            lines1.append(line)

        self.play(*(
            Create(lines1[i], run_time=1)
            for i in range(0, len(lines1))
        ))
        self.wait(1.5)

        # Draw intersection points
        pointsInter = []
        for i in range(0, n + 1):
            x = -size / 2 + size / n * i
            for j in range(0, n + 1):
                y = -size / 2 + size / n * j
                point = Dot([x, y, 0], color=WHITE)
                point.stroke_color = WHITE
                point.stroke_width = 0.05
                pointsInter.append(point)

        self.play(*(
            GrowFromCenter(pointsInter[i], run_time=1)
            for i in range(0, len(pointsInter))
        ))
        self.wait(2)

        # Remove separation lines
        self.play(
            *(
                FadeOut(lines1[i], run_time=1)
                for i in range(0, len(lines1))
            ),
            *(
                FadeOut(lines2[i], run_time=1)
                for i in range(0, len(lines2))
            ),
            FadeOut(square)
        )

        # Draw positions
        textInter = []
        for j in range(0, n + 1):
            y = -size / 2 + size / n * j
            for i in range(0, n + 1):
                x = -size / 2 + size / n * i
                text = Tex("$(" + str(i) + ", " + str(j) + ")$").scale(0.5)
                text.move_to([x, y + 0.2, 0])
                textInter.append(text)
        self.play(
            *(
                Write(textInter[i], run_time=1)
                for i in range(0, len(textInter))
            )
        )
        self.wait(1)

        return [pointsInter, textInter]


    # Scene 8
    def Scene8moveToArray(self, pointsInter, textInter):
        # Move points to bottom
        for i in range(0, len(pointsInter)):
            x = pointsInter[i].get_x() / 1.3
            y = pointsInter[i].get_y() / 1.3 - 0.7

            pointsInter[i].generate_target()
            pointsInter[i].target.move_to([x, y, 0])

        # Move texts to array
        positionsArrayPoints = []
        for i in range(0, len(textInter)):
            x = -0.4 * i * 2 + 23
            y = 3
            textInter[i].generate_target()
            textInter[i].target.move_to([x, y, 0])
            positionsArrayPoints.append([x, y, 0])
        positionsArrayPoints.reverse()
        arrayVertexText = Text("vertex = [").scale(0.4)
        arrayVertexText.move_to(LEFT * 6.2 + UP * 3)

        self.play(
            *(
                 MoveToTarget(pointsInter[i], run_time=1)
                 for i in range(0, len(pointsInter))
             ),
            *(
                MoveToTarget(textInter[i], run_time=1)
                for i in range(0, len(textInter))
            ),
            Write(arrayVertexText)
        )
        self.wait(2)


        # Label each position
        labelDotsArray = []
        for i in range(0, len(positionsArrayPoints)):
            dotLabel = Text(str(i), color=GREEN_C).scale(0.4)
            dotLabel.move_to([positionsArrayPoints[i][0], positionsArrayPoints[i][1] - 0.3, 0])
            labelDotsArray.append(dotLabel)

        self.play(
            *(
                Write(labelDotsArray[i], run_time=1)
                for i in range(0, len(labelDotsArray))
            )
        )

        self.wait(1)

        # Move to dots array
        labelDotsArray.reverse()
        newDotsPosition = []
        for i in range(0, len(pointsInter)):
            labelDotsArray[i].generate_target()
            labelDotsArray[i].target.move_to([
                -pointsInter[i].get_y() - 1.2 + 0.5,
                pointsInter[i].get_x() - 0.4 - 1 + 0.4,
                0
            ])
            newDotsPosition.append([-pointsInter[i].get_y() - 1.2 + 0.5, pointsInter[i].get_x() - 0.8 - 0.4 + 0.5, 0])
        self.play(
            *(
                MoveToTarget(labelDotsArray[i], run_time=1)
                for i in range(0, len(labelDotsArray))
            )
        )
        self.wait(1)


        # Draw Triangles
        triangLines = []
        def drawNextLine(i):
            triangFirstList = []
            triangSeconList = []

            for j in range(0, 5):
                triangFirst = Polygon(newDotsPosition[i + j*6], newDotsPosition[i + 1 + j*6]  , newDotsPosition[i + (j + 1)*6], fill_color=BLUE_D, fill_opacity=0.4)
                triangSecon = Polygon(newDotsPosition[i + (j + 1)*6], newDotsPosition[i + 1 + j*6], newDotsPosition[i + 1 + (j + 1)*6], fill_color=BLUE_E, fill_opacity=0.4)

                triangFirst.set_fill(BLUE_D)
                triangSecon.set_fill(BLUE_E)

                triangFirstList.append(triangFirst)
                triangSeconList.append(triangSecon)

                triangLines.append(triangFirst)
                triangLines.append(triangSecon)


            self.play(
                *(
                     DrawBorderThenFill(triangFirstList[i], run_time=0.5)
                     for i in range(0, len(triangFirstList))
                )
            )
            self.play(
                *(
                    DrawBorderThenFill(triangSeconList[i], run_time=0.5)
                    for i in range(0, len(triangSeconList))
                )
            )

        currentLineID = 0
        for i in range(0, 5): # 5
            drawNextLine(currentLineID)
            self.wait(0.1)
            currentLineID += 1
        self.wait(2)


        # Braces
        square = Square(4.5)
        square.move_to([0, -0.7, 0])
        square.stroke_opacity = 0
        square.fill_opacity = 0

        braceSize = Brace(square, direction=UP)
        label = Tex(r'$n = 6$').scale(0.9)
        always(label.next_to, braceSize, UP)

        self.play(
            Create(braceSize),
            Write(label),
            *(
                FadeOut(triangLines[i], run_time=0.5)
                for i in range(0, len(triangLines))
            )
        )


        # Zoom points
        for i in range(0, len(pointsInter)):
            x = pointsInter[i].get_x() * 1.1
            y = (pointsInter[i].get_y() + 0.6) * 1.1

            pointsInter[i].generate_target()
            pointsInter[i].target.move_to([x, y, 0])

        for i in range(0, len(pointsInter)):
            labelDotsArray[i].generate_target()
            labelDotsArray[i].target.move_to([
                labelDotsArray[i].get_x() * 1.1,
                (labelDotsArray[i].get_y() + 0.6) * 1.1,
                0
            ])

        braceSize.generate_target()
        braceSize.target.scale(1.3)
        braceSize.target.move_to([braceSize.get_x(), braceSize.get_y() + 0.6 * 1.1 + 0.4, 0])


        self.play(
            *(
                MoveToTarget(pointsInter[i], run_time=1)
                for i in range(0, len(pointsInter))
            ),
            *(
                MoveToTarget(labelDotsArray[i], run_time=1)
                for i in range(0, len(labelDotsArray))
            ),
            MoveToTarget(braceSize),
            Unwrite(arrayVertexText),
            *(
                FadeOut(textInter[i], run_time=1)
                for i in range(0, len(textInter))
            )
        )

        self.wait(0.5)


        # Text surronding
        texXY1 = Tex(r'$(x,\,y)$').scale(0.8)
        texXY1.move_to(LEFT * 5.5 + UP * 1.5)
        texXY2 = Tex(r'$(x,\,y - 1)$').scale(0.8)
        texXY2.move_to(LEFT * 5.5 + DOWN * 1.5)
        arrow = Arrow(start=[texXY1.get_x(), texXY1.get_y() - 0.7, 0], end=[texXY2.get_x(), texXY2.get_y() + 0.7, 0], color=YELLOW_C)
        texXY3 = Tex(r'$x + (y - 1) \times n$', color=BLUE_E).scale(0.7)
        texXY3.next_to(texXY2, DOWN)

        # Coordinates of below point
        selectedDot = pointsInter[21]
        pointCoord = Tex(r'$(3, 2)$').scale(0.5)
        pointCoord.move_to([selectedDot.get_x(), selectedDot.get_y() + 0.2, 0])
        oldCopyOfText = labelDotsArray[14].copy()
        self.play(
            Write(pointCoord),
            Unwrite(labelDotsArray[14]),
            Write(texXY1)
        )
        self.wait(1)

        # Move coord to below point
        pointCoordNew = Tex(r'$(3, 1)$').scale(0.5)
        pointCoordNew.move_to([selectedDot.get_x(), pointsInter[21+5].get_y() + 0.2, 0])
        idOld = labelDotsArray[20].copy()
        pointCoord.generate_target()
        pointCoord.target.move_to([selectedDot.get_x(), pointsInter[21+5].get_y() + 0.2, 0])
        isNew = oldCopyOfText

        self.play(DrawBorderThenFill(arrow))
        self.play(Transform(pointCoord, pointCoordNew), Transform(idOld, isNew), Write(texXY2), Write(texXY3))
        self.wait(2)


        # Unwrite and make it small again
        for i in range(0, len(pointsInter)):
            x = pointsInter[i].get_x() / 1.1
            y = pointsInter[i].get_y() / 1.1 - 0.6

            pointsInter[i].generate_target()
            pointsInter[i].target.move_to([x, y, 0])
        isNew.generate_target()
        isNew.target.move_to([isNew.get_x() / 1.1, isNew.get_y() / 1.1 - 0.6, 0])

        for i in range(0, len(pointsInter)):
            labelDotsArray[i].generate_target()
            labelDotsArray[i].target.move_to([
                labelDotsArray[i].get_x() / 1.1,
                labelDotsArray[i].get_y() / 1.1 - 0.6,
                0
            ])

        braceSize.generate_target()
        braceSize.target.scale(1/1.3)
        braceSize.target.move_to([braceSize.get_x(), braceSize.get_y() - 0.6 * 1.1 - 0.4, 0])
        arrayVertexText2 = Text("vertex = [").scale(0.4)
        arrayVertexText2.move_to(LEFT * 6.2 + UP * 3)

        self.play(
            *(
                MoveToTarget(pointsInter[i], run_time=1)
                for i in range(0, len(pointsInter))
            ),
            *(
                MoveToTarget(labelDotsArray[i], run_time=1)
                for i in range(0, len(labelDotsArray))
            ),
            MoveToTarget(braceSize),
            Unwrite(pointCoord),
            Write(arrayVertexText2),
            MoveToTarget(isNew),
            Unwrite(idOld, run_time=0.1),
            *(
                Write(textInter[i], run_time=1)
                for i in range(0, len(textInter))
            )
        )
        self.wait(1)


        # Redraw triangles
        triangLines = []
        labelList = []

        def drawNextLine2(i, xInit):
            xLab = xInit
            yLab = 3.5
            xIncrem = 0.7

            for j in range(0, 5):
                triangFirstList = []
                triangSeconList = []
                dotsArrayFirst = []
                dotsArraySecon = []

                triangFirst = Polygon(newDotsPosition[i + j * 6], newDotsPosition[i + 1 + j * 6],
                                      newDotsPosition[i + (j + 1) * 6], fill_color=BLUE_D, fill_opacity=0.4)
                triangSecon = Polygon(newDotsPosition[i + (j + 1) * 6], newDotsPosition[i + 1 + j * 6],
                                      newDotsPosition[i + 1 + (j + 1) * 6], fill_color=BLUE_E, fill_opacity=0.4)

                triangFirst.set_fill(BLUE_D)
                triangSecon.set_fill(BLUE_E)

                triangFirstList.append(triangFirst)
                triangSeconList.append(triangSecon)

                triangLines.append(triangFirst)
                triangLines.append(triangSecon)

                # Move points id to array
                label11 = labelDotsArray[i + j * 6].copy()
                label11.generate_target()
                label11.target.move_to([xLab, yLab, 0])
                dotsArrayFirst.append(label11)
                xLab += xIncrem

                label12 = labelDotsArray[i + 1 + j * 6].copy()
                label12.generate_target()
                label12.target.move_to([xLab, yLab, 0])
                dotsArrayFirst.append(label12)
                xLab += xIncrem

                label13 = labelDotsArray[i + (j + 1) * 6].copy()
                label13.generate_target()
                label13.target.move_to([xLab, yLab, 0])
                dotsArrayFirst.append(label13)
                xLab += xIncrem

                label21 = labelDotsArray[i + (j + 1) * 6].copy()
                label21.generate_target()
                label21.target.move_to([xLab, yLab, 0])
                dotsArraySecon.append(label21)
                xLab += xIncrem

                label22 = labelDotsArray[i + 1 + j * 6].copy()
                label22.generate_target()
                label22.target.move_to([xLab, yLab, 0])
                dotsArraySecon.append(label22)
                xLab += xIncrem

                label23 = labelDotsArray[i + 1 + (j + 1) * 6].copy()
                label23.generate_target()
                label23.target.move_to([xLab, yLab, 0])
                dotsArraySecon.append(label23)
                xLab += xIncrem

                labelList.append(label11)
                labelList.append(label12)
                labelList.append(label13)
                labelList.append(label21)
                labelList.append(label22)
                labelList.append(label23)

                self.play(
                    *(
                        DrawBorderThenFill(triangFirstList[i], run_time=1.5)
                        for i in range(0, len(triangFirstList))
                    ),
                    *(
                        MoveToTarget(dotsArrayFirst[i], run_time=1.5)
                        for i in range(0, len(dotsArrayFirst))
                    )
                )
                self.play(
                    *(
                        DrawBorderThenFill(triangSeconList[i], run_time=1.5)
                        for i in range(0, len(triangSeconList))
                    ),
                    *(
                        MoveToTarget(dotsArraySecon[i], run_time=1.5)
                        for i in range(0, len(dotsArraySecon))
                    )
                )
            return xLab + xIncrem

        arrayTrianglesText = Text("triangles = [").scale(0.4)
        arrayTrianglesText.move_to(LEFT * 5.8 + UP * 3.5)
        self.play(Write(arrayTrianglesText))

        currentLineID = 0
        xLab = -4.5
        for i in range(0, 5):  # 5
            xLab = drawNextLine2(currentLineID, xLab)
            self.wait(1.5)
            currentLineID += 1
        self.wait(2)


        # Fade out everything but square
        self.play(
            Unwrite(arrayTrianglesText),
            Unwrite(arrayVertexText2),
            *(
                Uncreate(pointsInter[i], run_time=1)
                for i in range(0, len(pointsInter))
            ),
            *(
                Uncreate(labelDotsArray[i], run_time=1)
                for i in range(0, len(labelDotsArray))
            ),
            *(
                Unwrite(labelList[i], run_time=1)
                for i in range(0, len(labelList))
            ),
            *(
                Unwrite(textInter[i], run_time=1)
                for i in range(0, len(textInter))
            ),
            Unwrite(texXY1),
            Unwrite(texXY2),
            Unwrite(texXY3),
            Uncreate(arrow),
            Unwrite(isNew)
        )
        self.wait(1)

    def generatePolygon(self, lod, translation, direction, maxDist1):
        pointsInter = []
        for i in range(0, lod):
            x = (-lod / 2 + lod / (lod - 1) * i) / lod * maxDist1

            for j in range(0, lod):
                y = (-lod / 2 + lod / (lod - 1) * j) / lod * maxDist1

                if direction == 0 or direction == 1:
                    pointsInter.append([x, 0, y])
                elif direction == 2 or direction == 3:
                    pointsInter.append([0, y, x])
                elif direction == 4 or direction == 5:
                    pointsInter.append([x, y, 0])

        triangList = []

        def drawNextLine(i):
            for j in range(0, lod - 1):
                triangFirst = Polygon(pointsInter[i + j * lod], pointsInter[i + 1 + j * lod],
                                      pointsInter[i + 1 + (j + 1) * lod], fill_color=BLUE_D, fill_opacity=0.4,
                                      shade_in_3d=True)
                triangSecon = Polygon(pointsInter[i + j * lod], pointsInter[i + 1 + (j + 1) * lod],
                                      pointsInter[i + (j + 1) * lod], fill_color=BLUE_E, fill_opacity=0.4,
                                      shade_in_3d=True)

                triangFirst.set_fill(BLUE_D)
                triangSecon.set_fill(BLUE_E)

                triangFirst.move_to([triangFirst.get_x() + translation[0], triangFirst.get_y() + translation[1],
                                     triangFirst.get_z() + translation[2]])
                triangSecon.move_to([triangSecon.get_x() + translation[0], triangSecon.get_y() + translation[1],
                                     triangSecon.get_z() + translation[2]])

                triangList.append(triangFirst)
                triangList.append(triangSecon)

        currentLineID = 0
        for i in range(0, lod - 1):  # 5
            drawNextLine(currentLineID)
            currentLineID += 1

        return triangList


    # Scene 9
    def Scene9SquareToSphere(self):
        self.set_camera_orientation(phi=PI, theta=0, distance=400000)

        maxDist1 = 3
        maxDist2 = 1.5

        # Draw Triangles
        triangList1 = self.generatePolygon(6, [0, 0, -maxDist2], 5, maxDist1)
        self.play(*(DrawBorderThenFill(triangList1[i], run_time=0.5) for i in range(0, len(triangList1))))
        self.wait(2)

        # Morph into other polygon
        triangList2 = self.generatePolygon(9, [0, 0, -maxDist2], 5, maxDist1)
        self.play(
            *(Transform(triangList1[i], triangList2[i], run_time=0.5) for i in range(0, len(triangList1))),
            *(DrawBorderThenFill(triangList2[i], run_time=0.5) for i in range(len(triangList1), len(triangList2)))
        )
        self.wait(1)

        triangList3 = self.generatePolygon(18, [0, 0, -maxDist2], 5, maxDist1)
        self.play(
            *(Uncreate(triangList1[i], run_time=0.01) for i in range(0, len(triangList1))),
            *(Transform(triangList2[i], triangList3[i], run_time=0.5) for i in range(0, len(triangList2))),
            *(DrawBorderThenFill(triangList3[i], run_time=0.5) for i in range(len(triangList2), len(triangList3)))
        )
        self.wait(1)

        triangList4 = self.generatePolygon(4, [0, 0, -maxDist2], 5, maxDist1)
        self.play(
            *(Uncreate(triangList2[i], run_time=0.01) for i in range(0, len(triangList2))),
            *(Transform(triangList3[i], triangList4[i], run_time=0.5) for i in range(0, len(triangList4))),
            *(Uncreate(triangList3[i], run_time=0.5) for i in range(len(triangList4), len(triangList3)))
        )
        self.wait(1)

        triangList5 = self.generatePolygon(6, [0, 0, -maxDist2], 5, maxDist1)
        self.play(
            *(Uncreate(triangList3[i], run_time=0.01) for i in range(0, len(triangList3))),
            *(Transform(triangList4[i], triangList5[i], run_time=0.5) for i in range(0, len(triangList4))),
            *(DrawBorderThenFill(triangList5[i], run_time=0.5) for i in range(len(triangList4), len(triangList5)))
        )
        self.wait(1)

        self.move_camera(phi=110 * DEGREES, theta=30 * DEGREES, distance=400000)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Add other quads
        triang1 = triangList5
        triang2 = self.generatePolygon(6, [0, -maxDist2, 0], 1, maxDist1)
        triang3 = self.generatePolygon(6, [maxDist2, 0, 0], 2, maxDist1)
        triang4 = self.generatePolygon(6, [-maxDist2, 0, 0], 3, maxDist1)
        triang5 = self.generatePolygon(6, [0, 0, maxDist2], 4, maxDist1)
        triang6 = self.generatePolygon(6, [0, maxDist2, 0], 0, maxDist1)
        self.play(
            *(DrawBorderThenFill(triang2[i], run_time=0.5) for i in range(0, len(triang2))),
            *(DrawBorderThenFill(triang3[i], run_time=0.5) for i in range(0, len(triang3))),
            *(DrawBorderThenFill(triang4[i], run_time=0.5) for i in range(0, len(triang4))),
            *(DrawBorderThenFill(triang5[i], run_time=0.5) for i in range(0, len(triang5))),
            *(DrawBorderThenFill(triang6[i], run_time=0.5) for i in range(0, len(triang6)))
        )
        self.wait(2)

        # To Sphere
        def applyFunctionSphere(v, transformid):
            if transformid == 0:
                return v / math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
            elif transformid == 1:
                return v * 3.5
            elif transformid == 2:
                return v / math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]) * 3.5

        self.play(
            *(Uncreate(triangList4[i], run_time=0.01) for i in range(0, len(triangList4))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 2), triang1[i]) for i in range(0, len(triang1))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 2), triang2[i]) for i in range(0, len(triang2))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 2), triang3[i]) for i in range(0, len(triang3))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 2), triang4[i]) for i in range(0, len(triang4))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 2), triang5[i]) for i in range(0, len(triang5))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 2), triang6[i]) for i in range(0, len(triang6)))
        )
        self.wait(8)
        self.stop_ambient_camera_rotation()


    # Scene 10
    def Scene10DrawCircle(self):
        circle = Circle(RED_C, fill_opacity=0, stroke_width=6, stroke_color=RED_C, radius=3)
        self.play(Create(circle))

        self.wait(1)

        self.play(Uncreate(circle))
        self.wait(1)


    # Scene 11
    def Scene11MethodFromSquareToSphere(self):
        self.set_camera_orientation(phi=PI, theta=0, distance=400000)

        maxDist1 = 3
        maxDist2 = 1.5

        # Draw Triangles
        triangList1 = self.generatePolygon(6, [0, 0, -maxDist2], 5, maxDist1)
        self.play(*(DrawBorderThenFill(triangList1[i], run_time=0.5) for i in range(0, len(triangList1))))
        self.wait(2)

        self.move_camera(phi=110 * DEGREES, theta=20 * DEGREES, distance=400000)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Add other quads
        triang1 = triangList1
        triang2 = self.generatePolygon(6, [0, -maxDist2, 0], 1, maxDist1)
        triang3 = self.generatePolygon(6, [maxDist2, 0, 0], 2, maxDist1)
        triang4 = self.generatePolygon(6, [-maxDist2, 0, 0], 3, maxDist1)
        triang5 = self.generatePolygon(6, [0, 0, maxDist2], 4, maxDist1)
        triang6 = self.generatePolygon(6, [0, maxDist2, 0], 0, maxDist1)
        self.play(
            *(DrawBorderThenFill(triang2[i], run_time=0.5) for i in range(0, len(triang2))),
            *(DrawBorderThenFill(triang3[i], run_time=0.5) for i in range(0, len(triang3))),
            *(DrawBorderThenFill(triang4[i], run_time=0.5) for i in range(0, len(triang4))),
            *(DrawBorderThenFill(triang5[i], run_time=0.5) for i in range(0, len(triang5))),
            *(DrawBorderThenFill(triang6[i], run_time=0.5) for i in range(0, len(triang6)))
        )
        self.wait(2)

        # Vectors from center to points
        points = triang2[8].get_vertices()
        pointEl = points[0]
        vectorNew = Arrow3D([0, 0, 0], [pointEl[0], pointEl[1], pointEl[2]], color=RED_C, stroke_width=0.5)
        self.play(Create(vectorNew, run_time=0.5))
        self.wait(5)

        self.play(Uncreate(vectorNew, run_time=0.5))
        self.wait(2.5)

        # To Sphere
        def applyFunctionSphere(v, transformid):
            if transformid == 0:
                return v / math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
            elif transformid == 1:
                return v * 3.5

        self.play(
            *(Uncreate(triangList1[i], run_time=0.01) for i in range(0, len(triangList1))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 0), triang1[i]) for i in range(0, len(triang1))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 0), triang2[i]) for i in range(0, len(triang2))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 0), triang3[i]) for i in range(0, len(triang3))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 0), triang4[i]) for i in range(0, len(triang4))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 0), triang5[i]) for i in range(0, len(triang5))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 0), triang6[i]) for i in range(0, len(triang6)))
        )
        self.wait(3)

        self.play(
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 1), triang1[i]) for i in range(0, len(triang1))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 1), triang2[i]) for i in range(0, len(triang2))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 1), triang3[i]) for i in range(0, len(triang3))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 1), triang4[i]) for i in range(0, len(triang4))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 1), triang5[i]) for i in range(0, len(triang5))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v, 1), triang6[i]) for i in range(0, len(triang6)))
        )

        self.wait(1.5)

        self.play(
            *(Uncreate(triang1[i]) for i in range(0, len(triang1))),
            *(Uncreate(triang2[i]) for i in range(0, len(triang2))),
            *(Uncreate(triang3[i]) for i in range(0, len(triang3))),
            *(Uncreate(triang4[i]) for i in range(0, len(triang4))),
            *(Uncreate(triang5[i]) for i in range(0, len(triang5))),
            *(Uncreate(triang6[i]) for i in range(0, len(triang6)))
        )

        self.stop_ambient_camera_rotation()
        self.wait(2)


    # Scene 13
    def Scene13DrawSurfaceNormals3DTo2D(self):
        self.move_camera(phi=-(110+180) * DEGREES, theta=(20-70) * DEGREES, distance=400000)
        self.begin_ambient_camera_rotation(rate=0.1)

        surface3D = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                3*u/6*0.3*np.cos(u+2*v*np.abs(np.cos(u/3)))
            ]), v_min = -6, v_max = 6, u_min = -4, u_max = 4, checkerboard_colors=[GREEN_D, GREEN_A]
        )
        self.play(DrawBorderThenFill(surface3D))

        self.wait(9)

        self.move_camera(phi=-180*1.5 * DEGREES)
        self.stop_ambient_camera_rotation()
        self.wait(2)

        self.play(Uncreate(surface3D))
        self.wait(1)


    # Scene 14
    def Scene14DrawSpheresNormals(self):
        maxDist1 = 3
        maxDist2 = 1.5

        # Draw Triangles
        self.move_camera(phi=110 * DEGREES, theta=20 * DEGREES, distance=400000)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Add other quads
        triang1 = self.generatePolygon(6, [0, 0, -maxDist2], 5, maxDist1)
        triang2 = self.generatePolygon(6, [0, -maxDist2, 0], 1, maxDist1)
        triang3 = self.generatePolygon(6, [maxDist2, 0, 0], 2, maxDist1)
        triang4 = self.generatePolygon(6, [-maxDist2, 0, 0], 3, maxDist1)
        triang5 = self.generatePolygon(6, [0, 0, maxDist2], 4, maxDist1)
        triang6 = self.generatePolygon(6, [0, maxDist2, 0], 0, maxDist1)

        # Vectors from center to points
        theta = 0.3
        phi = 0.7+PI/2
        r = 3.5
        vectorNew = Arrow3D([0, 0, 0], [r*np.cos(theta), r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.cos(phi)], color=RED_C, stroke_width=0.5)

        # To Sphere
        def applyFunctionSphere(v):
            return v / math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]) * 3.5

        self.play(
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v), triang1[i], run_time=0.5) for i in range(0, len(triang1))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v), triang2[i], run_time=0.5) for i in range(0, len(triang2))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v), triang3[i], run_time=0.5) for i in range(0, len(triang3))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v), triang4[i], run_time=0.5) for i in range(0, len(triang4))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v), triang5[i], run_time=0.5) for i in range(0, len(triang5))),
            *(ApplyPointwiseFunction(lambda v: applyFunctionSphere(v), triang6[i], run_time=0.5) for i in range(0, len(triang6))),
            Create(vectorNew, run_time=0.5)
        )
        self.wait(8)

        vectorNew.generate_target()
        sl = 1.5
        vectorNew.target.move_to([r*np.cos(theta)*sl, r*np.sin(theta)*np.cos(phi)*sl, r*np.sin(theta)*np.cos(phi)*sl])
        self.play(MoveToTarget(vectorNew))
        self.wait(2)

        self.play(
            *(Uncreate(triang1[i]) for i in range(0, len(triang1))),
            *(Uncreate(triang2[i]) for i in range(0, len(triang2))),
            *(Uncreate(triang3[i]) for i in range(0, len(triang3))),
            *(Uncreate(triang4[i]) for i in range(0, len(triang4))),
            *(Uncreate(triang5[i]) for i in range(0, len(triang5))),
            *(Uncreate(triang6[i]) for i in range(0, len(triang6))),
            Uncreate(vectorNew)
        )
        self.wait(1)

        self.stop_ambient_camera_rotation()


    # Scene 15
    def Scene15DrawQuadTreeText(self):
        text = Text('Quad-Tree', color=GREEN_C).scale(1.5)
        self.play(Write(text, run_time=1.5))
        self.wait(2)
        self.play(Unwrite(text, run_time=1))
        self.wait(1)

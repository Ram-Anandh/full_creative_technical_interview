"""All the constants to be place here"""


class HomePageConstants:
    page_title = 'HTML Canvas Studio - Free Online Tool'
    rectangle = "rectangle"
    line = 'line'
    eraser = 'eraser'


class JavaScriptConstants:
    @staticmethod
    def draw_line(co_ordinates):
        """

        :param co_ordinates: tuples form (starting pt x-axis,starting pt y-axis,
        ending pt x-axis,ending pt y-axis)
        :return: string
        """
        return 'var canvas, context, canvaso, contexto;' \
               'canvaso = document.getElementById("imageView");' \
               'context = canvaso.getContext("2d");context.lineWidth = 5;' \
               'context.strokeStyle = "#000000";context.beginPath();context.moveTo({}, {});' \
               'context.lineTo({}, {});context.stroke();context.closePath();'.format(
            co_ordinates[0], co_ordinates[1], co_ordinates[2], co_ordinates[3])

    @staticmethod
    def draw_rectangle(co_ordinates):
        """

        :param co_ordinates: tuples (top, bottom, left, right)
        :return: string
        """

        return 'var canvas, context, canvaso, contexto;' \
               'canvaso = document.getElementById("imageView");' \
               'context = canvaso.getContext("2d");context.lineWidth = 5;' \
               'context.strokeStyle = "#000000";context.strokeRect({}, {}, {}, {});'.format(
            co_ordinates[0], co_ordinates[1], co_ordinates[2], co_ordinates[3])

    @staticmethod
    def eraser(co_ordinates):
        return 'var canvas, context, canvaso, contexto;' \
               'canvaso = document.getElementById("imageView");' \
               'context = canvaso.getContext("2d");' \
               'context.lineWidth = 5;context.strokeStyle = "#FFFFFF";context.beginPath();' \
               'context.moveTo({}, {}); context.lineTo({}, {});context.stroke();'.format(
            co_ordinates[0], co_ordinates[1], co_ordinates[2], co_ordinates[3]
        )

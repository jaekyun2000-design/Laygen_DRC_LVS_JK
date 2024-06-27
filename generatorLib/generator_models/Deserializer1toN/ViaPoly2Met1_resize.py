
import ViaPoly2Met1


class _ViaPoly2Met1_resize(ViaPoly2Met1._ViaPoly2Met1):
    _ParametersForDesignCalculation = dict(_ViaPoly2Met1NumberOfCOX=1,
                                           _ViaPoly2Met1NumberOfCOY=2,
                                           Met1XWidth=66, Met1YWidth=200,
                                           POXWidth=40, POYWidth=200)

    def _CalculateDesignParameter(self, _ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                                  Met1XWidth=66, Met1YWidth=200,
                                  POXWidth=50, POYWidth=200,
                                  ):
        """ Poly-Metal1 Contact with resize

            Calculate ViaPoly2Met1 and resize PolyLayer and/or Metal1Layer.
            NumberOfCOX,Y must be input.
            Other XYWidth can be optionally input (Number or None).
        Note:
            This method does not follow the DRC.

        """


        self._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=_ViaPoly2Met1NumberOfCOX,
                                                   _ViaPoly2Met1NumberOfCOY=_ViaPoly2Met1NumberOfCOY)

        if Met1XWidth != None:
            self._DesignParameter['_Met1Layer']['_XWidth'] = Met1XWidth
        if Met1YWidth != None:
            self._DesignParameter['_Met1Layer']['_YWidth'] = Met1YWidth
        if POXWidth != None:
            self._DesignParameter['_POLayer']['_XWidth'] = POXWidth
        if POYWidth != None:
            self._DesignParameter['_POLayer']['_YWidth'] = POYWidth
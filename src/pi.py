import math


class Pi:

    @staticmethod
    def calcular_pi(cantidad_decimales):
        current_number = 1
        end = (10 ** (cantidad_decimales + 1))
        result = 0
        result_pi = None
        while True:
            #            result_old = result
            result = result + (1 / (current_number ** 2))
            # print("resultado Operacion [" + str(result_old) + " + (1 / (" + str(current_number) + " ** 2))]  : " +
            # str( result))

            if current_number == end:
                result_pi_str = str(math.sqrt((6 * result)))
                pi_int = result_pi_str.split('.')[0]
                pi_decimal = result_pi_str.split('.')[1]
                pi_value_str = pi_int + '.' + pi_decimal[0:cantidad_decimales]
                print("resultado de pi : " + pi_value_str)
                break
            current_number = current_number + 1
        return float(pi_value_str)

    #def __get_value_history_pi_for_decimal(self):



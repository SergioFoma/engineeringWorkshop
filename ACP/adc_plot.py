import matplotlib.pyplot as plt

def plot_voltage_as_time( time, voltage, max_voltage ):
    plt.figure( figsize = (10, 6 ) )

    plt.plot( time, voltage, label = 'U(t)' )

    plt.title('Грфик  U(t) ')
    plt.xlabel('Время, с')
    plt.ylabel( 'Нарпяжение, В')

    plt.xlim( 0, max(time) if time else 1 )
    plt.ylim(0, max_voltage )

    plt.grid( True )

    plt.show()

def plot_sampling_period_hist( time ):
    sampling_periods = []
    for i in range( len(time) - 1 ):
        period = time[i+1] - time[i]
        sampling_periods.append( period )

    plt.figure( figsize =  (10, 6 ) )

    plt.hist( sampling_periods )

    plt.title("Распределение периодов дискретизации")
    plt.xlabel("Период измерения, с")
    plt.ylabel( "Количество измерений")

    plt.xlim( 0, 0.06 )

    plt.grid(True )

    plt.show()
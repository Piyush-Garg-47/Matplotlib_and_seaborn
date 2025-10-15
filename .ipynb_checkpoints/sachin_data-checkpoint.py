import matplotlib.pyplot as plt
years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 
          2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

runs = [819, 365, 1508, 969, 1789, 704, 2234, 2011, 2541, 2416,
 1903, 1907, 2133, 1294, 1727, 953, 900, 2201, 2063, 1513, 3124]

plt.plot(years , runs)
plt.xlabel("year")
plt.ylabel("Runs Scored")
plt.title("Sachin Tendulkar's  Yearly Runs")
plt.show()
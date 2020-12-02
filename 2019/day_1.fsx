open System.IO

let inputFilename = "2019/day_1_input.txt"

let linesFromFile filename : seq<int> = 
    seq { use streamReader = File.OpenText filename
        while not streamReader.EndOfStream
            do yield int (streamReader.ReadLine())}

let fuelCounterUpper mass : int =
    int (floor (float mass / 3.0)) - 2
    
Seq.sumBy fuelCounterUpper (linesFromFile inputFilename)


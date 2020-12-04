open System.IO

let inputFilename = "C:/git-jmschietekat/advent-of-code/2020/day_1_input.txt"

let linesFromFile filename : seq<int> = 
    seq { use streamReader = File.OpenText filename
        while not streamReader.EndOfStream
            do yield int (streamReader.ReadLine())}

let multiply a b = a * b

let printProductOfTwoValuesThatSumTo2020 (input: seq<int>) : Unit =
    for (i_a,v_a) in (Seq.indexed input) do
        for (i_b,v_b) in (Seq.indexed input) do
            if i_a < i_b then
                if v_a + v_b = 2020 then 
                    printf "[%i]=%i + [%i]=%i = 2020, " i_a v_a i_b v_b
                    printfn "%i x %i = %i" v_a v_b (v_a * v_b)
            

let printProductOfThreeValuesThatSumTo2020 (input: seq<int>) : Unit = 
    for (i_a,v_a) in (Seq.indexed input) do
        for (i_b,v_b) in (Seq.indexed input) do
            for (i_c,v_c) in (Seq.indexed input) do
                if i_a < i_b && i_b < i_c && i_c > i_a then
                    if v_a + v_b + v_c = 2020 then 
                        printf "[%i]=%i + [%i]=%i + [%i]=%i = 2020, " i_a v_a i_b v_b i_c v_c
                        printfn "%i x %i x %i = %i" v_a v_b v_c (v_a * v_b * v_c)
                                

let printSeq seq = 
    seq |> Seq.iter (printf "%A ")
    printfn ""


linesFromFile inputFilename |> productOfTwoValuesThatSumTo2020
linesFromFile inputFilename |> productOfThreeValuesThatSumTo2020

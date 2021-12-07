open System.IO

let sampleInput = "2021/day_01_input_sample.txt";
let challangeInput = "2021/day_01_input.txt";

let part1 fileName = 
    fileName
    |> File.ReadAllLines 
    |> Seq.map int
    |> Seq.pairwise
    |> Seq.sumBy (fun (a , b) -> if a < b then 1 else 0)
    |> printfn "Part 1 answer: %i"

part1 sampleInput
part1 challangeInput 

let part2 fileName =
    fileName
    |> File.ReadAllLines
    |> Seq.map int
    |> Seq.windowed 3
    |> Seq.pairwise
    |> Seq.sumBy (fun (a, b) -> if (a |> Array.sum ) < (b |> Array.sum ) then 1 else 0)
    |> printfn "Part 2 answer: %i"

part2 sampleInput
part2 challangeInput

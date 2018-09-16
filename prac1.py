"""An example file to upload into Github repository."""


"""Two functions that both give the sum of a sequence between 'start' and
'end', taking the 'step'-th values to calculate the sum in the sequence."""

#This one takes longer due to its usage of the sum() method.
def sequence_sum(start, end, step):
    return sum(range(start, end+1 if step > 0 else end-1, step))

#Using a formula saves time.
def sequence_sum(start, end, step):
    if step > 0:
        n = len(range(start, end + 1, step))
    else:
        n = len(range(start, end - 1, step))
    sum = n * (2 * start + (n - 1) * step)//2
    return round(sum)

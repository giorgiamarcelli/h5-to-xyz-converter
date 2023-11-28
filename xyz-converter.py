#!/bin/python3


# Import modules
import h5py
import numpy as np
import argparse
from tqdm import tqdm 


def save_file(file_input, group, file_output): 
    # load data from the h5 file
    with h5py.File(file_input, 'r') as h5:
        position = np.array(h5['particles'][group]['position/value'])
    
    n_time_step = len(position)
    n_particles = len(position[0,:])
    
    with open(file_output, 'w') as file:
        for step in tqdm(range(n_time_step)):
            file.write(str(n_particles) + '\n')
            file.write(f"Time step series \n")
            for particle in range(n_particles):
                file.write(" ".join(map(str, position[step, particle]))+'\n')


def main():
    # parse input, output, group from command line
    parser = argparse.ArgumentParser(description="Convert h5 file inot xyz file")
    
    parser.add_argument('input', type=str, help='Path to the input h5 file')
    parser.add_argument('group', type=str, help='Group within the h5 file containing the dataset')
    parser.add_argument('output', type=str, help='Path to the xyz output file')
    args = parser.parse_args()

    # generate and save xyz file 
    save_file(args.input, args.group, args.output)

if __name__ == '__main__':
    main()

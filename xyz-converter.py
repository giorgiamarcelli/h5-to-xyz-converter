# Import modules
import h5py
import numpy as np
import argparse
from tqdm import tqdm 


def save_file(file_name, position): 
    
    n_time_step = len(position)
    n_particles = len(position[0,:])
    
    with open(file_name, 'w') as file:
        for step in tqdm(range(n_time_step)):
            file.write(str(n_particles) + '\n')
            file.write(f"Time step series \n")
            for particle in range(n_particles):
                file.write(" ".join(map(str, position[step, particle]))+'\n')


def main(input, output, group):
    # load data from the h5 file
    with h5py.File(input, 'r') as h5:
        position = np.array(h5['particles'][group]['position/value'])

    # generate and save xyz file 
    save_file(input, position)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert h5 file inot xyz file")
    parser.add_argument('input', type=str, help='Path to the xyz output file')
    parser.add_argument('output', type=str, help='Path to the input h5 file')
    parser.add_argument('group', type=str, help='Group within the h5 file containing the dataset')
    args = parser.parse_args()

    main(args.input, args.output, args.group)
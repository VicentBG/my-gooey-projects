'''
A simple Gooey example. One required field, one optional.
'''

from gooey import Gooey, GooeyParser


@Gooey()
def main():
    parser = GooeyParser(description='Process some integers.')

    parser.add_argument(
        'required_field',
        metavar='Some Field',
        help='Enter some text!')

    parser.add_argument(
        '-f', '--foo',
        metavar='Some Flag',
        action='store_true',
        help='I turn things on and off')

    args = parser.parse_args()
    if args.foo:
        print(f'Se ha almacenado la cadena: {args.required_field}')
    else:
        print('Hooray! Nada almacenado...')


if __name__ == '__main__':
    main()
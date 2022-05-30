from typing import Callable, List


def belex_c_func(
        name: str,
        return_type: str,
        attributes: List[str],
        body: str,
        param_types: List[str],
        param_names: List[str]):
    r"""Implement a decorator that takes arguments about literal
    C code, and wraps a Python function that takes arguments
    *args and **kwargs"""
    assert len(param_types) == len(param_names), fr'''Number of
        parameter types {len(param_types)} must match number of
        parameter names {len(param_names)}.'''
    # Etc., more assertions.
    def decorator(fn: Callable):
        def wrapper(*args, **kwargs):
            pass
        print(f'{return_type} __attribute__(', end='')
        print(', '.join(attributes), end='')
        print(')')
        print(f'{name} (')
        parms = list(zip(param_types, param_names))
        parmss = [' '.join(p) for p in parms]
        parmsss = ['        ' + ps for ps in parmss]
        print(',\n'.join(parmsss))
        print('{', end='')
        print(body)
        print('}')
        return wrapper
    return decorator


@belex_c_func(
    name='pbkdf2_hmac_sha1_loop_second',
    return_type='void',
    attributes=[r'(section("text_hot_utils_gvml_pbkdf2"))'],
    body=r'''
    for (int i = 1; i < iterations; i++) {
        pbkdf2_blk_sha1_folded(in_sha1_16vmrs_out_sha1_5vmrs, passwords_inner_sha1_5vmrs, in_sha1_16vmrs_out_sha1_5vmrs, msb_vmr, _9_tmp_vmrs);
        pbkdf2_blk_sha1_folded(in_sha1_16vmrs_out_sha1_5vmrs, passwords_outer_sha1_5vmrs, in_sha1_16vmrs_out_sha1_5vmrs, msb_vmr, _9_tmp_vmrs);
        xor_3vmrs(chunk_dk_3_5vmrs, in_sha1_16vmrs_out_sha1_5vmrs);
    }''',
    param_types=['int'] + 6 * ['enum gvml_vm_reg'],
    param_names=[
        'iterations',
        'passwords_inner_sha1_5vmrs',
        'passwords_outer_sha1_5vmrs',
        'in_sha1_16vmrs_out_sha1_5vmrs',
        'msb_vmr',
        '_9_tmp_vmrs',
        'chunk_dk_3_5vmrs',
    ])
def pbkdf2_hmac_sha1_loop_second():
    pass


if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

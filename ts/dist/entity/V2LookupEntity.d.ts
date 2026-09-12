import { FreeMusicEntityBase } from '../FreeMusicEntityBase';
import type { FreeMusicSDK } from '../FreeMusicSDK';
import type { Control } from '../types';
import type { V2Lookup, V2LookupLoadMatch } from '../FreeMusicTypes';
declare class V2LookupEntity extends FreeMusicEntityBase<V2Lookup> {
    constructor(client: FreeMusicSDK, entopts: any);
    make(this: V2LookupEntity): V2LookupEntity;
    load(this: any, reqmatch?: V2LookupLoadMatch, ctrl?: Control): Promise<V2LookupEntity>;
}
export { V2LookupEntity };

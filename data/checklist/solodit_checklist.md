Id:
SOL-AM-DA-1
Description:
Attackers can manipulate the accounting by donating tokens.
Remediation:
Implement internal accounting instead of relying on `balanceOf` natively.
References:
#1
Id:
SOL-AM-FrA-1
Description:
Get-or-create pattern functionality is prone to frontrunning attacks.
Remediation:
Ensure the frontrunning does not cause user loss or unexpected problems.
Id:
SOL-AM-FrA-2
Description:
Actions that require two separate transactions may be at risk of frontrunning, where an attacker can intervene between the two calls.
Remediation:
Ensure critical actions that are split across multiple transactions cannot be interfered with by attackers. This can involve checks or locks between the transactions.
References:
#1
Id:
SOL-AM-FrA-3
Description:
Attackers may cause legitimate transactions to fail by front-running with transactions of negligible amounts.
Remediation:
Implement checks to prevent transactions with non-material amounts from affecting the contract's state or execution flow.
References:
#1
Id:
SOL-AM-FrA-4
Description:
Without a commit-reveal scheme, actions such as votes or bids are exposed in the mempool before they are mined, allowing adversaries to see and potentially act on this information. The commit-reveal pattern maintains confidentiality until all commitments are made.
Remediation:
Implement a commit-reveal scheme where users first commit a hash of their intended action and then reveal the actual action after the commitment phase is over. This protects against front-running and provides a fairer process.
Id:
SOL-AM-GA-1
Description:
Malicious actors can prevent normal user transactions by making a slight change on the on-chain states. More problematic on L2 chains where tx fee is low.
Remediation:
Ensure normal user actions especially important actions like withdrawal/repayment are not disturbed by other actors.
References:
#1
Id:
SOL-AM-MA-1
Description:
`block.timestamp` can be manipulated by miners to a small extent, so relying on it for precise timing might be risky.
Remediation:
Use `block.timestamp` only where a slight inaccuracy is acceptable, such as for longer intervals.
Id:
SOL-AM-PMA-1
Description:
Price, or rates between assets more generally, can be manipulated if it is derived from the ratio of balance. Flash loan and donation are the well-known attack vectors used to manipulate the prices.
Remediation:
Use the Chainlink oracles for the asset prices and implement internal accounting instead of relying on `balanceOf`.
References:
#1
#2
#3
Id:
SOL-AM-ReentrancyAttack-1
Description:
Read-only reentrancy. The read-only reentrancy is a reentrancy scenario where a view function is reentered, which in most cases is unguarded as it does not modify the contract's state. However, if the state is inconsistent, wrong values could be reported. Other protocols relying on a return value can be tricked into reading the wrong state to perform unwanted actions.
Remediation:
Extend the reentrancy guard to the view functions as well.
References:
#1
#2
#3
Id:
SOL-AM-ReentrancyAttack-2
Description:
Untrusted external contract calls could callback leading to unexpected results such as multiple withdrawals or out-of-order events.
Remediation:
Use check-effects-interactions pattern or reentrancy guards.
References:
#1
#2
#3
Id:
SOL-AM-ReplayAttack-1
Description:
Failed transactions can be susceptible to replay attacks if not properly protected.
Remediation:
Implement nonce-based or other mechanisms to ensure that each transaction can only be executed once, preventing replay attacks.
References:
#1
Id:
SOL-AM-ReplayAttack-2
Description:
Signatures valid on one chain may be replayed on another, leading to potential security breaches.
Remediation:
Use chain-specific parameters or domain separators to ensure signatures are only valid on the intended chain.
References:
#1
Id:
SOL-AM-RP-1
Description:
Some protocols grant an admin with a privilege of pulling assets directly from the protocol. In general, if there is an actor that can affect the user funds directly it must be reported.
Remediation:
Allow access to only the relevant parts of protocol funds, e.g. by tracking fees internally. Forcing a timelock on the admin actions can be another mitigation.
References:
#1
Id:
SOL-AM-SandwichAttack-1
Description:
An attacker can monitor the mempool and puts two transactions before and after the user's transaction. For example, when an attacker spots a large trade, executes their own trade first to manipulate the price, and then profits by closing their position after the user's trade is executed.
Remediation:
Allow users to specify the minimum output amount and revert the transaction if it is not satisfied.
References:
#1
#2
Id:
SOL-AM-SybilAttack-1
Description:
It is very easy to trigger actions using a lot of alternative addresses on blockchain. Any quorum mechanism or utilization based rewarding system can be vulnerable to sybil attacks.
Remediation:
Do not rely on the number of users in quorum design.
References:
#1
#2
#3
Id:
SOL-Basics-AC-1
Description:
This is a general check item. Having a clear understanding of all relevant actors and interactions in the protocol is critical for security.
Remediation:
List down all the actors and interactions and draw a diagram.
Id:
SOL-Basics-AC-2
Description:
Access controls determine who can use certain functions of a contract. If these are missing or improperly implemented, it can expose the contract to unauthorized changes or withdrawals.
Remediation:
Implement and rigorously test access controls like `onlyOwner` or role-based permissions to ensure only authorized users can access certain functions.
Id:
SOL-Basics-AC-3
Description:
Whitelisting allows only a specific set of addresses to interact with the contract, offering an additional layer of security against malicious actors.
Remediation:
Establish a whitelisting mechanism and ensure that only trusted addresses can execute sensitive or restricted operations.
Id:
SOL-Basics-AC-4
Description:
Transfer of critical privileges must be done in two-step process. A two-step transfer process, usually involving a request followed by a confirmation, adds an extra layer of security against unintentional or malicious owner changes.
Remediation:
Implement a two-step transfer mechanism that requires the new actor to accept the transfer, ensuring better security and intentional ownership changes.
Id:
SOL-Basics-AC-5
Description:
The protocol needs to work consistently and reasonably even during the transfer of privileges.
Remediation:
Double check how the protocol works during the transfer of privileges.
Id:
SOL-Basics-AC-6
Description:
If you do not override a parent contract's function explicitly, the parent's one will be exposed with its visibility and probably a wrong accessibiliy.
Remediation:
Make sure you check the accessibility to the parent's external/public functions.
Id:
SOL-Basics-AC-7
Description:
Use of `tx.origin` for authorization may be abused by a malicious contract forwarding calls from the legitimate user. Use `msg.sender` instead. `require( tx.origin == msg.sender)` is a useful check to ensure that the `msg.sender` is an EOA(externally owned account).
Remediation:
Make sure you know the difference of `tx.origin` and `msg.sender` and use properly.
References:
#1
Id:
SOL-Basics-AL-1
Description:
Sometimes the first and last cycles have a different logic from others and there can be problems.
Remediation:
Ensure the logic is correct for the first and the last cycles.
Id:
SOL-Basics-AL-4
Description:
`delete` does not rearrange the array but just resets the element.
Remediation:
Copy the last element to the index of the element to be removed and decrease the length of an array.
Id:
SOL-Basics-AL-5
Description:
If an array is supposed to be updated (removal in the middle), the indexes will change.
Remediation:
Do not use an index of an array that is supposed to be updated as a parameter of a function.
Id:
SOL-Basics-AL-6
Description:
Direct calculation against a sum may yield different results than the sum of individual calculations, leading to precision issues.
Remediation:
Ensure that summation logic is thoroughly tested and verified, especially when dealing with financial calculations to maintain accuracy.
References:
#1
Id:
SOL-Basics-AL-7
Description:
In most cases, an array (especially an input array by users) is supposed to be unique.
Remediation:
Add a validation to check the array is unique.
Id:
SOL-Basics-AL-8
Description:
The first and the last iteration in loops can sometimes have edge cases that differ from other iterations, possibly leading to vulnerabilities.
Remediation:
Always test the initial and the last iteration separately and ensure consistent behavior throughout all iterations.
Id:
SOL-Basics-AL-9
Description:
Due to the block gas limit, there is a clear limitation in the amount of operation that can be handled in a transaction.
Remediation:
Ensure the number of iterations is properly bounded.
Id:
SOL-Basics-AL-10
Description:
Loops that contain external calls or are dependent on user-controlled input can be exploited to halt the contract's functions. (e.g. sending ETH to multiple users)
Remediation:
Ensure a failure of a single iteration does not revert the whole operation.
Id:
SOL-Basics-AL-11
Description:
`msg.value` is consistent for the whole transaction. If it is used in the for loop, it is likely there is a mistake in accounting.
Remediation:
Avoid using `msg.value` inside loops. Refer to multi-call vulnerability.
Id:
SOL-Basics-AL-12
Description:
If there is a mechanism to transfer funds out based on some kind of shares, it is likely that there is a problem of 'dust' funds not handled correctly.
Remediation:
Make sure the last transfer handles all residual.
Id:
SOL-Basics-AL-13
Description:
Sometimes developers overlook the edge cases that can happened due to the break or continue in the middle of the loop.
Remediation:
Make sure the break or continue inside a loop does not lead to unexpected behaviors.
Id:
SOL-Basics-BR-1
Description:
Contracts created with the CREATE opcode will be eliminated if a block reorg happens.
Remediation:
Use CREATE2 instead of CREATE.
References:
#1
#2
#3
#4
#5
Id:
SOL-Basics-Event-1
Description:
Emitting events properly is important especially if the change is critical.
Remediation:
Ensure to emit events in all important functions.
Id:
SOL-Basics-Function-1
Description:
Inputs to functions should be validated to prevent unexpected behavior.
Remediation:
Ensure thorough validation. E.g. min/max for numeric values, start/end for dates, ownership of positions.
References:
#1
#2
#3
Id:
SOL-Basics-Function-2
Description:
Outputs of functions should be validated to prevent unexpected behavior.
Remediation:
Ensure the outputs are valid.
Id:
SOL-Basics-Function-3
Description:
Front-running can allow attackers to prioritize their transactions over others.
Remediation:
Make sure there is no unexpected risk even if attackers front-run.
References:
#1
#2
#3
Id:
SOL-Basics-Function-4
Description:
Misleading or outdated comments can result in misunderstood function behaviors.
Remediation:
Keep comments updated and ensure they accurately describe the function logic.
References:
#1
#2
Id:
SOL-Basics-Function-5
Description:
Edge input values can lead to unexpected behavior.
Remediation:
Make sure the function works as expected for the edge values.
References:
#1
#2
Id:
SOL-Basics-Function-6
Description:
Implementing a function that accepts arbitrary user input and makes low-level calls based on this data introduces a significant security risk. Low-level calls in Solidity, such as call(), are powerful and can lead to unintended contract behavior if not used cautiously. With the ability for users to supply arbitrary data, they can potentially trigger unexpected paths in the contract logic, exploit reentrancy vulnerabilities, or even interact with other contracts in a malicious manner.
Remediation:
Restrict the usage of low-level calls, especially when combined with arbitrary user input. Ensure that any data used in these calls is thoroughly validated and sanitized.
Id:
SOL-Basics-Function-7
Description:
Ensure the visibility modifier is appropriate for the function's use, preventing unnecessary exposure.
Remediation:
Limit function visibility to the strictest level possible (`private` or `internal`).
Id:
SOL-Basics-Function-8
Description:
There are several edge cases regarding the caller checking mechanism, both for EOA and contracts.
Remediation:
Ensure the correct access control is implemented according to the protocol's context. (read all the references)
References:
#1
#2
Id:
SOL-Basics-Function-9
Description:
Ensure that functions modifying contract state or accessing sensitive operations are access-controlled.
Remediation:
Implement access control mechanisms like `onlyOwner` or custom modifiers.
References:
#1
#2
#3
Id:
SOL-Basics-Inheritance-1
Description:
External/Public functions of all parent contracts will be exposed with the same visibility as long as they are not overridden.
Remediation:
Make sure to expose only relevant functions from parent contracts.
Id:
SOL-Basics-Inheritance-2
Description:
Parent contracts often assume the inheriting contracts to implement public functions to utilize the parent's functionality. Sometimes developers miss implementing them and it makes the inheritance useless.
Remediation:
Make sure to expose relevant functions from parent contracts.
References:
#1
#2
Id:
SOL-Basics-Inheritance-3
Description:
Interfaces are used by other protocols to interact with the protocol. Missing implementation will lead to unexpected cases.
Remediation:
Make sure to implement all functions specified in the interface.
Id:
SOL-Basics-Inheritance-4
Description:
Inheriting contracts in the wrong order can lead to unexpected behavior, e.g. storage allocation.
Remediation:
Verify the inheritance chain is ordered from 'most base-like' to 'most derived' to prevent issues like incorrect variable initialization.
Id:
SOL-Basics-Initialization-1
Description:
Overlooking explicit initialization of state variables can lead to critical issues.
Remediation:
Make sure to initialize all state variables correctly.
References:
#1
Id:
SOL-Basics-Initialization-2
Description:
If the contract is supposed to be inherited by other contracts, `onlyInitializing` modifier MUST be used instead of `initializer`.
Remediation:
Make sure to use the correct modifier for the initializer function.
References:
#1
Id:
SOL-Basics-Initialization-3
Description:
Initializer function can be front-run right after the deployment. The impact is critical if the initializer sets the access controls.
Remediation:
Use the factory pattern to allow only the factory to call the initializer or ensure it is not front-runnable in the deploy script.
References:
#1
Id:
SOL-Basics-Map-1
Description:
If a variable of nested structure is deleted, only the top-level fields are reset by default values (zero) and the nested level fields are not reset.
Remediation:
Always ensure that inner fields are deleted before the outer fields of the structure.
Id:
SOL-Basics-Math-1
Description:
Ensure that the logic behind any mathematical operation is correctly implemented.
Remediation:
Verify calculations against established mathematical rules in the document or the comments.
Id:
SOL-Basics-Math-2
Description:
Loss of precision can lead to significant errors over time or frequent calculations.
Remediation:
Use appropriate data types and ensure rounding methods are correctly applied.
Id:
SOL-Basics-Math-3
Description:
Operations with certain expressions might lead to unintended data type conversions.
Remediation:
Always be explicit with data types and avoid relying on implicit type conversions.
Id:
SOL-Basics-Math-4
Description:
Multiplying before division is generally better to keep the precision.
Remediation:
To avoid loss of precision, always multiply first and then divide.
Id:
SOL-Basics-Math-5
Description:
Rounding direction often matters when the accounting relies on user's shares.
Remediation:
Use the proper rounding direction in favor of the protocol
Id:
SOL-Basics-Math-6
Description:
Division by zero will revert the transaction.
Remediation:
Always check denominators before division.
Id:
SOL-Basics-Math-7
Description:
Variables can sometimes exceed their bounds, causing reverts.
Remediation:
Use checks to prevent variable underflows and overflows.
Id:
SOL-Basics-Math-8
Description:
Unsigned integers cannot hold negative values.
Remediation:
Always ensure that only non-negative values are assigned to unsigned integers.
Id:
SOL-Basics-Math-9
Description:
Arithmetics do not overflow inside the `unchecked{}` block.
Remediation:
Use `unchecked{}` only when it is strictly guaranteed that no overflow/underflow happens.
Id:
SOL-Basics-Math-10
Description:
Usage of incorrect inequality can cause unexpected behavior for the edge values.
Remediation:
Review the logic and ensure the appropriate comparison operators are used.
Id:
SOL-Basics-Math-11
Description:
Inline assembly can behave differently than high-level language constructs. (division by zero, overflow/underflow do not revert!)
Remediation:
Ensure mathematical operations in inline assembly are properly tested and verified.
Id:
SOL-Basics-Math-12
Description:
If the calculation includes numerous terms, you need to confirm all edge cases where each term has the possible min/max values.
Remediation:
Ensure the edge cases do not lead to unexpected outcome.
Id:
SOL-Basics-Payment-1
Description:
There are cases where a receiver contract can deny the transaction. For example, a malicious receiver can have a fallback to revert. If a caller tried to send funds using `transfer` or `send`, the whole transaction will revert. (Meanwhile, `call()` does not revert but returns a boolean)
Remediation:
Make sure that the receiver can not deny the payment or add a backup handler with a try-catch.
Id:
SOL-Basics-Payment-2
Description:
For ETH deposits, `msg.value` must be checked if it is not less than the amount specified.
Remediation:
Require `msg.value==amount`.
Id:
SOL-Basics-Payment-3
Description:
Certain actions like self-destruct, deterministic address feeding, and coinbase transactions can be used to force-feed contracts.
Remediation:
Ensure the contract behaves as expected when receiving unexpected funds.
References:
#1
Id:
SOL-Basics-Payment-4
Description:
Dust deposit/withdrawal often can lead to various vulnerabilities, e.g. rounding issue in accounting or Denial-Of-Service.
Remediation:
Add a threshold for the deposit/withdrawal amount.
Id:
SOL-Basics-Payment-5
Description:
The best practice in withdrawal process is to implement pull-based approach. Track the accounting and let users pull the payments instead of sending funds proactively.
Remediation:
Implement pull-based approach in withdrawals.
Id:
SOL-Basics-Payment-6
Description:
The transfer() and send() functions forward a fixed amount of 2300 gas. Historically, it has often been recommended to use these functions for value transfers to guard against reentrancy attacks. However, the gas cost of EVM instructions may change significantly during hard forks which may break already deployed contract systems that make fixed assumptions about gas costs. For example. EIP 1884 broke several existing smart contracts due to a cost increase of the SLOAD instruction.
Remediation:
Use `call()` to prevent potential gas issues.
References:
#1
#2
#3
Id:
SOL-Basics-Payment-7
Description:
If a `payable` function does not transfer all ETH passed in `msg.value` and the contract does not have a withdraw method, ETH will be locked in the contract
Remediation:
Make sure either no ETH remains in the contract at the end of `payable` functions or make sure there is a `withdraw` function.
References:
#1
#2
Id:
SOL-Basics-PU-1
Description:
Proxied contract can't have a constructor and it's common to move constructor logic to an external initializer function, usually called initialize
Remediation:
Use initializer functions for initialization of proxied contracts.
Id:
SOL-Basics-PU-2
Description:
Without the `initializer` modifier, there is a risk that the initialization function can be called multiple times.
Remediation:
Always use the `initializer` modifier for initialization functions in proxied contracts and ensure they're called once during deployment.
Id:
SOL-Basics-PU-3
Description:
Upgradable contracts must use the upgradable versions of parent initializer functions. (e.g. Pausable vs PausableUpgradable)
Remediation:
Use upgradable versions of parent initializer functions.
Id:
SOL-Basics-PU-4
Description:
Inadequate security on the `authorizeUpgrade()` function can allow unauthorized upgrades.
Remediation:
Ensure proper access controls and checks are in place for the `authorizeUpgrade()` function.
Id:
SOL-Basics-PU-5
Description:
An uninitialized contract can be taken over by an attacker. This applies to both a proxy and its implementation contract, which may impact the proxy.
Remediation:
To prevent the implementation contract from being used, invoke the `_disableInitializers` function in the constructor to automatically lock it when it is deployed.
References:
#1
Id:
SOL-Basics-PU-6
Description:
Using `selfdestruct` and `delegatecall` in implementation contracts can introduce vulnerabilities and unexpected behavior in a proxy setup.
Remediation:
Avoid using `selfdestruct` and `delegatecall` in implementation contracts to ensure contract stability and security.
Id:
SOL-Basics-PU-7
Description:
Immutable variables are stored in the bytecode, not in the proxy storage. So using immutable variable is not recommended in proxy setup. If used, make sure all immutables stay consistent across implementations during upgrades.
Remediation:
Avoid using immutable variables in upgradable contracts.
Id:
SOL-Basics-PU-8
Description:
Sometimes developers overlook and use an incorrect branch of OZ library, e.g. use Ownable instead of OwnableUpgradeable.
Remediation:
Make sure inherit the correct branch of OZ library according to the contract's upgradeability design.
References:
#1
Id:
SOL-Basics-PU-9
Description:
Storage collisions can occur when storage layouts between contract versions conflict, leading to data corruption and unpredictable behavior.
Remediation:
Maintain a consistent storage layout between upgrades, and when using inheritance, set storage gaps to avoid potential collisions.
Id:
SOL-Basics-PU-10
Description:
Changing the order or type of storage variables between upgrades can lead to storage collisions.
Remediation:
Maintain a consistent order and type for storage variables across contract versions to avoid storage collisions.
Id:
SOL-Basics-Type-1
Description:
Explicit type casting does not revert on overflow/underflow.
Remediation:
Avoid a forced type casting as much as possible and ensure values are in the range of type limit.
References:
#1
Id:
SOL-Basics-Type-2
Description:
The time units are of `uint8` type and this can lead to unintended overflow.
Remediation:
Double check the calculations including time units and ensure there is no overflow for reasonable values.
References:
#1
Id:
SOL-Basics-VI-EAI-1
Description:
`selfdestruct` will not be available after EIP-4758. This EIP will rename the SELFDESTRUCT opcode and replace its functionality.
Remediation:
Do not use `selfdestruct` to ensure the contract works in the future.
References:
#1
#2
#3
Id:
SOL-Basics-VI-OVI-1
Description:
`ERC2771Context._msgData()` reverts if `msg.data.length < 20`. The correct behavior is not specified in ERC-2771, but based on the specified behavior of `_msgSender` we assume the full `msg.data` should be returned in this case.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-2
Description:
GovernorCompatibilityBravo may trim proposal calldata. The proposal creation entrypoint (propose) in GovernorCompatibilityBravo allows the creation of proposals with a signatures array shorter than the calldatas array. This causes the additional elements of the latter to be ignored, and if the proposal succeeds the corresponding actions would eventually execute without any calldata. The ProposalCreated event correctly represents what will eventually execute, but the proposal parameters as queried through getActions appear to respect the original intended calldata.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-3
Description:
ECDSA signature malleability. The functions ECDSA.recover and ECDSA.tryRecover are vulnerable to a kind of signature malleability due to accepting EIP-2098 compact signatures in addition to the traditional 65 byte signature format. This is only an issue for the functions that take a single bytes argument, and not the functions that take r, v, s or r, vs as separate arguments. The potentially affected contracts are those that implement signature reuse or replay protection by marking the signature itself as used rather than the signed message or a nonce included in it. A user may take a signature that has already been submitted, submit it again in a different form, and bypass this protection.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-4
Description:
Extending this contract with a custom _beforeTokenTransfer function could allow a reentrancy attack to happen. More specifically, when burning tokens, _beforeTokenTransfer is invoked before the send hook is externally called on the sender while token balances are adjusted afterwards. At the moment of the call to the sender, which can result in reentrancy, state managed by _beforeTokenTransfer may not correspond to the actual token balances or total supply.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-5
Description:
When the `verifyMultiProof`, `verifyMultiProofCalldata`, `processMultiProof`, or `processMultiProofCalldata` functions are in use, it is possible to construct merkle trees that allow forging a valid multiproof for an arbitrary set of leaves.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-6
Description:
Governor proposal creation may be blocked by frontrunning. By frontrunning the creation of a proposal, an attacker can become the proposer and gain the ability to cancel it. The attacker can do this repeatedly to try to prevent a proposal from being proposed at all. This impacts the Governor contract in v4.9.0 only, and the GovernorCompatibilityBravo contract since v4.3.0.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-7
Description:
Transparency is broken in case of selector clash with non-decodable calldata. The TransparentUpgradeableProxy uses the ifAdmin modifier to achieve transparency. If a non-admin address calls the proxy the call should be frowarded transparently. This works well in most cases, but the forwarding of some functions can fail if there is a selector conflict and decoding issue.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-8
Description:
The ERC721Consecutive contract designed for minting NFTs in batches does not update balances when a batch has size 1 and consists of a single token. Subsequent transfers from the receiver of that token may overflow the balance as reported by balanceOf. The issue exclusively presents with batches of size 1.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-9
Description:
Denial of Service (DoS) in the `supportsERC165InterfaceUnchecked()` function in `ERC165Checker.sol` and `ERC165CheckerUpgradeable.sol`, which can consume excessive resources when processing a large amount of data via an EIP-165 supportsInterface query.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-10
Description:
Incorrect resource transfer between spheres via contracts using the cross-chain utilities for Arbitrum L2: `CrossChainEnabledArbitrumL2` or `LibArbitrumL2`. Calls from EOAs would be classified as cross-chain calls. The vulnerability will classify direct interactions of externally owned accounts (EOAs) as cross-chain calls, even though they are not started on L1.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-11
Description:
Checkpointing quorum was missing and past proposals that failed due to lack of quorum could pass later. It is necessary to avoid quorum changes making old, failed because of quorum, proposals suddenly successful.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-12
Description:
Since 0.8.0, abi.decode reverts if the bytes raw data overflow the target type. SignatureChecker.isValidSignatureNow is not expected to revert. However, an incorrect assumption about Solidity 0.8's abi.decode allows some cases to revert, given a target contract that doesn't implement EIP-1271 as expected. The contracts that may be affected are those that use SignatureChecker to check the validity of a signature and handle invalid signatures in a way other than reverting.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-13
Description:
Since 0.8.0, abi.decode reverts if the bytes raw data overflow the target type. ERC165Checker.supportsInterface is designed to always successfully return a boolean, and under no circumstance revert. However, an incorrect assumption about Solidity 0.8's abi.decode allows some cases to revert, given a target contract that doesn't implement EIP-165 as expected, specifically if it returns a value other than 0 or 1. The contracts that may be affected are those that use ERC165Checker to check for support for an interface and then handle the lack of support in a way other than reverting.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-14
Description:
GovernorCompatibilityBravo incorrect ABI encoding may lead to unexpected behavior
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-15
Description:
It is possible for `initializer()`-protected functions to be executed twice, if this happens in the same transaction. For this to happen, either one call has to be a subcall the other, or both call have to be subcalls of a common initializer()-protected function. This can particularly be dangerous is the initialization is not part of the proxy construction, and reentrancy is possible by executing an external call to an untrusted address.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-16
Description:
Possible inconsistency in the value returned by totalSupply DURING a mint. If you mint a token, the receiver is a smart contract, and the receiver implements onERC1155Receive, then this receiver is called with the balance already updated, but with the totalsupply not yet updated.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-17
Description:
Upgradeable contracts using UUPSUpgradeable may be vulnerable to an attack affecting uninitialized implementation contracts.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-OVI-18
Description:
A vulnerability in TimelockController allowed an actor with the executor role to take immediate control of the timelock, by resetting the delay to 0 and escalating privileges, thus gaining unrestricted access to assets held in the contract. Instances with the executor role set to 'open' allow anyone to use the executor role, thus leaving the timelock at risk of being taken over by an attacker.
Remediation:
Use the latest stable OpenZeppelin version
Id:
SOL-Basics-VI-SVI-1
Description:
Storage structs and arrays with types shorter than 32 bytes can cause data corruption if encoded directly from storage using the experimental ABIEncoderV2.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-2
Description:
If an empty string is used in a function call, the following function arguments will not be correctly passed to the function.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-3
Description:
In some situations, the optimizer replaces certain numbers in the code with routines that compute different numbers.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-4
Description:
If you use `keccak256(abi.encodePacked(a, b))` and both `a` and `b` are dynamic types, it is easy to craft collisions in the hash value by moving parts of `a` into `b` and vice-versa. More specifically, `abi.encodePacked(\'a\', \'bc\') == abi.encodePacked(\'ab\', \'c\').
Remediation:
Use `abi.encode` instead of `abi.encodePacked`.
References:
#1
#2
Id:
SOL-Basics-VI-SVI-5
Description:
Optimizer sequences containing FullInliner do not preserve the evaluation order of arguments of inlined function calls in code that is not in expression-split form.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-6
Description:
Calling functions that conditionally terminate the external EVM call using the assembly statements ``return(...)`` or ``stop()`` may result in incorrect removals of prior storage writes.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-7
Description:
ABI-encoding a tuple with a statically-sized calldata array in the last component would corrupt 32 leading bytes of its first dynamically encoded component.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-8
Description:
Copying ``bytes`` arrays from memory or calldata to storage may result in dirty storage values.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-9
Description:
The Yul optimizer may incorrectly remove memory writes from inline assembly blocks, that do not access solidity variables.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-10
Description:
ABI-reencoding of nested dynamic calldata arrays did not always perform proper size checks against the size of calldata and could read beyond `calldatasize()`.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-11
Description:
Literals used for a fixed length bytes parameter in ``abi.encodeCall`` were encoded incorrectly.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-12
Description:
User defined value types with underlying type shorter than 32 bytes used incorrect storage layout and wasted storage
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-13
Description:
Immutable variables of signed integer type shorter than 256 bits can lead to values with invalid higher order bits if inline assembly is used.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-14
Description:
If used on memory byte arrays, result of the function ``abi.decode`` can depend on the contents of memory outside of the actual byte array that is decoded.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-15
Description:
The bytecode optimizer incorrectly re-used previously evaluated Keccak-256 hashes. You are unlikely to be affected if you do not compute Keccak-256 hashes in inline assembly.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-16
Description:
Copying an empty byte array (or string) from memory or calldata to storage can result in data corruption if the target array's length is increased subsequently without storing new data.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-17
Description:
When assigning a dynamically-sized array with types of size at most 16 bytes in storage causing the assigned array to shrink, some parts of deleted slots were not zeroed out.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-18
Description:
Contract types used in events in libraries cause an incorrect event signature hash
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-19
Description:
Function calls to internal library functions with calldata parameters called via ``using for`` can result in invalid data being read.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-20
Description:
String literals containing double backslash characters passed directly to external or encoding function calls can lead to a different string being used when ABIEncoderV2 is enabled.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-21
Description:
Accessing array slices of arrays with dynamically encoded base types (e.g. multi-dimensional arrays) can result in invalid data being read.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-22
Description:
The creation code of a contract that does not define a constructor but has a base that does define a constructor did not revert for calls with non-zero value.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-23
Description:
The creation of very large memory arrays can result in overlapping memory regions and thus memory corruption.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-24
Description:
The Yul optimizer can remove essential assignments to variables declared inside for loops when Yul's continue or break statement is used. You are unlikely to be affected if you do not use inline assembly with for loops and continue and break statements.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-25
Description:
Private methods can be overridden by inheriting contracts.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-26
Description:
The Yul optimizer can remove essential assignments to variables declared inside for loops when Yul's continue or break statement is used. You are unlikely to be affected if you do not use inline assembly with for loops and continue and break statements.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-27
Description:
If both the experimental ABIEncoderV2 and the experimental Yul optimizer are activated, one component of the Yul optimizer may reuse data in memory that has been changed in the meantime.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-28
Description:
Reading from calldata structs that contain dynamically encoded, but statically-sized members can result in incorrect values.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-29
Description:
Assigning an array of signed integers to a storage array of different type can lead to data corruption in that array.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-30
Description:
Storage arrays containing structs or other statically-sized arrays are not read properly when directly encoded in external function calls or in abi.encode*.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-31
Description:
A contract's constructor that takes structs or arrays that contain dynamically-sized arrays reverts or decodes to invalid data.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-32
Description:
Calling uninitialized internal function pointers created in the constructor does not always revert and can cause unexpected behavior.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-33
Description:
Calling uninitialized internal function pointers created in the constructor does not always revert and can cause unexpected behavior.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-34
Description:
Contract types used in events in libraries cause an incorrect event signature hash
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-35
Description:
Storage structs and arrays with types shorter than 32 bytes can cause data corruption if encoded directly from storage using the experimental ABIEncoderV2.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-36
Description:
The optimizer incorrectly handles byte opcodes whose second argument is 31 or a constant expression that evaluates to 31. This can result in unexpected values.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-37
Description:
Double bitwise shifts by large constants whose sum overflows 256 bits can result in unexpected values.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-38
Description:
Using the ** operator with an exponent of type shorter than 256 bits can result in unexpected values.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-39
Description:
Using structs in events logged wrong data.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-40
Description:
Calling functions that return multi-dimensional fixed-size arrays can result in memory corruption.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-41
Description:
If a contract has both a new-style constructor (using the constructor keyword) and an old-style constructor (a function with the same name as the contract) at the same time, one of them will be ignored.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-42
Description:
It is possible to craft the name of a function such that it is executed instead of the fallback function in very specific circumstances.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-43
Description:
The low-level .delegatecall() does not return the execution outcome, but converts the value returned by the functioned called to a boolean instead.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-44
Description:
The ecrecover() builtin can return garbage for malformed input.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-45
Description:
Accessing the ``.selector`` member on complex expressions leaves the expression unevaluated in the legacy code generation.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-46
Description:
It was possible to change the data location of the parameters or return variables from ``calldata`` to ``memory`` and vice-versa while overriding internal and public functions. This caused invalid code to be generated when calling such a function internally through virtual function calls.
Remediation:
Use the latest Solidity version.
References:
#1
Id:
SOL-Basics-VI-SVI-47
Description:
The compiler does not flag an error when two or more free functions with the same name and parameter types are defined in a source unit or when an imported free function alias shadows another free function with a different name but identical parameter types.
Remediation:
Use the latest Solidity version.
Id:
SOL-Basics-VI-SVI-48
Description:
Tuple assignments with components that occupy several stack slots, i.e. nested tuples, pointers to external functions or references to dynamically sized calldata arrays, can result in invalid values.
Remediation:
Use the latest Solidity version.
Id:
SOL-CR-1
Description:
Users must be allowed to manage their existing positions in all protocol status. For example, users must be able to repay the debt even when the protocol is paused or the protocol should not accrue debts when it is paused.
Remediation:
Ensure user positions are protected in special/emergent protocol situations.
Id:
SOL-CR-2
Description:
Some functionalities must work even when the whole protocol is paused. For example, users must be able to withdraw (or repay) assets even while the protocol is paused.
Remediation:
Review the pause mechanism thoroughly to ensure that it only affects intended functions and can't be abused by a malicious operator.
Id:
SOL-CR-3
Description:
Some protocols are written to allow admin pull any amount of assets from the pool. This is a red flag and MUST be disallowed. The best practice is to track the protocol fee and only allow access to that amount.
Remediation:
Ensure the admin can not steal user funds. Track the protocol earning separately.
Id:
SOL-CR-4
Description:
Changes in the critical protocol properties MUST go through a cooling period to allow users react on the changes.
Remediation:
Implement a timelock for the critical property changes and emit proper events.
Id:
SOL-CR-5
Description:
Events are often used to monitor the protocol status. Without emission of events, users might be affected due to ignorance of the changes.
Remediation:
Emit proper events on critical configuration changes.
Id:
SOL-CR-6
Description:
Critical privileges MUST be transferred via a two-step process and the protocol MUST behave as expected before/during/after transfer.
Remediation:
Use two-step process for transferring critical privileges and ensure the protocol works properly before/during/after the transfer.
Id:
SOL-CR-7
Description:
The validation on the protocol configuration values is often overlooked assuming the admin is trusted. But it is always recommended clarifying the range of each configuration value and validate in setter functions. (e.g. protocol fee should be limited)
Remediation:
Ensure the protocol level properties are properly validated in the documented range.
Id:
SOL-Defi-AS-1
Description:
Using hardcoded slippage can lead to poor trades and freezing user funds during times of high volatility.
Remediation:
Allow users to specify the slippage parameter in the actual asset amount which was calculated off-chain.
References:
#1
Id:
SOL-Defi-AS-2
Description:
Without deadline protection, user transactions are vulnerable to sandwich attacks.
Remediation:
Allow a user specify the deadline of the swap.
References:
#1
Id:
SOL-Defi-AS-3
Description:
Protocols may face risks if reserves are not validated and can be lent out, affecting the system's solvency.
Remediation:
Ensure reserve validation logic is in place to safeguard the protocol's liquidity and overall health.
References:
#1
Id:
SOL-Defi-AS-4
Description:
Using forked code, especially from known projects like Uniswap, can introduce known vulnerabilities if not updated or audited properly.
Remediation:
Review the differences. Utilize tools such as contract-diff.xyz to compare and identify the origin of code snippets.
Id:
SOL-Defi-AS-5
Description:
Rounding issues in the formulas can lead to inaccuracies or imbalances in token swaps and liquidity provisions.
Remediation:
Review the mathematical operations in the AMM's formulas, ensuring they handle rounding appropriately without introducing vulnerabilities.
Id:
SOL-Defi-AS-6
Description:
Allowing arbitrary calls based on user input can expose the contract to various vulnerabilities.
Remediation:
Validate and sanitize user inputs. Avoid executing arbitrary calls based solely on input data.
Id:
SOL-Defi-AS-7
Description:
Without slippage protection, traders might experience unexpected losses due to large price deviations during a trade.
Remediation:
Incorporate a slippage parameter that users can set to limit their maximum acceptable slippage.
Id:
SOL-Defi-AS-8
Description:
If the AMM doesn't support tokens with varying decimals or types, it might lead to incorrect calculations and potential losses.
Remediation:
Ensure compatibility with tokens of varying decimal places and validate token types before processing them.
Id:
SOL-Defi-AS-9
Description:
Fee-on-transfer tokens can cause problems because the sending amount and the received amount do not match.
Remediation:
Ensure the fee-on-transfer tokens are handled correctly if they are supposed to be supported.
Id:
SOL-Defi-AS-10
Description:
Rebasing tokens can change the actual balance.
Remediation:
Ensure the rebasing tokens are handled correctly if they are supposed to be supported.
Id:
SOL-Defi-AS-11
Description:
Protocols integrating AMMs should determine the `minAmountOut` prior to swaps to avoid unfavorable rates. The source of the rates and potential for manipulation should also be considered.
Remediation:
Ensure that the protocol calculates `minAmountOut` before executing swaps. If external oracles are used, validate their trustworthiness and consider potential vulnerabilities like sandwich attacks.
References:
#1
Id:
SOL-Defi-AS-12
Description:
Callback functions can be manipulated if they don't validate the calling contract's address. This is especially crucial for functions like `swap()` that involve tokens or assets.
Remediation:
Implement checks in the callback functions to validate the address of the calling contract. Additionally, review the logic for any potential bypasses to this check.
Id:
SOL-Defi-AS-13
Description:
ON-chain slippage calculation can be manipulated.
Remediation:
Allow users to specify the slippage parameter in the actual asset amount which was calculated off-chain.
References:
#1
Id:
SOL-Defi-AS-14
Description:
Enforcing slippage parameters for intermediate swaps but not the final step can result in users receiving less tokens than their specified minimum
Remediation:
Enforce slippage parameter as the last step before transferring funds to users
References:
#1
Id:
SOL-Defi-FlashLoan-1
Description:
Allowing withdrawals within the same block as other interactions may enable attackers to exploit flashloan vulnerabilities.
Remediation:
Implement a delay or disable withdrawals within the same block where a deposit or loan action took place to mitigate such risks.
Id:
SOL-Defi-FlashLoan-2
Description:
ERC4626, the tokenized vault standard, could be susceptible to flashloan attacks if the underlying mechanisms do not adequately account for such threats.
Remediation:
Ensure that ERC4626-related operations have in-built protections against rapid, in-block actions that could be leveraged by flashloans.
References:
#1
Id:
SOL-Defi-General-1
Description:
Not all ERC20 tokens use 18 decimals. Overlooking this can lead to computation errors.
Remediation:
Always check and adjust for the decimal count of the ERC20 tokens being handled.
Id:
SOL-Defi-General-2
Description:
Some protocols or platforms may provide additional rewards for staked or deposited assets. If these rewards are not properly accounted for or managed, it could lead to discrepancies in the user's expected vs actual returns.
Remediation:
The protocol should have mechanisms in place to track all potential rewards for user deposited assets. Users should be provided with clear interfaces or methods to claim any unexpected rewards to ensure fairness and transparency.
Id:
SOL-Defi-General-3
Description:
Direct transfers of assets without using the protocol's logic can lead to various problems in accounting especially if the accounting relies on `balanceOf` (or `address.balance`).
Remediation:
Implement the internal accounting so that it is not be affected by direct transfers.
Id:
SOL-Defi-General-4
Description:
The first deposit can set certain parameters or conditions that subsequent deposits rely on.
Remediation:
Test and ensure that the first deposit initializes and sets all necessary parameters correctly.
Id:
SOL-Defi-General-5
Description:
The target tokens can be depegged.
Remediation:
Ensure the protocol behave as expected during the depeg.
Id:
SOL-Defi-General-6
Description:
Setting high allowances can make funds vulnerable to abuse; protocols sometimes set max to prevent this risk.
Remediation:
Consider implementing a revert on approval functions when an unnecessarily high allowance is set.
References:
#1
Id:
SOL-Defi-General-7
Description:
Leaving residual amounts can lead to discrepancies in accounting or locked funds.
Remediation:
Implement logic to handle minimal residual amounts in the pool.
Id:
SOL-Defi-General-8
Description:
Protocols often provide various benefits to the depositors based on the deposit amount. This can lead to flashloan-deposit-harvest-withdraw attack cycle.
Remediation:
Ensure the withdrawal is protected for some blocks after deposit.
Id:
SOL-Defi-General-9
Description:
Not all ERC20 tokens are compliant to the ERC20 standard and there are several weird ERC20 tokens (e.g. Fee-On-Transfer tokens, rebasing tokens, tokens with blacklisting).
Remediation:
Clarify what kind of tokens are supported and whitelist the ERC20 tokens that the protocol would accept.
References:
#1
Id:
SOL-Defi-Lending-1
Description:
Failure to liquidate positions during sharp price drops can result in substantial platform losses.
Remediation:
Ensure robustness during extreme market conditions.
Id:
SOL-Defi-Lending-2
Description:
If positions cannot be liquidated under these circumstances, it poses a risk to lenders who might not recover their funds.
Remediation:
Ensure a reliable mechanism for liquidating under-collateralized or defaulting loans to safeguard lenders.
Id:
SOL-Defi-Lending-3
Description:
Self-liquidation profit loopholes can lead to potential system abuse and unintended financial consequences.
Remediation:
Audit and test self-liquidation mechanisms to prevent any exploitative behaviors.
Id:
SOL-Defi-Lending-4
Description:
Unexpected pauses can place users at risk of unwarranted liquidations, despite their willingness to increase collateral.
Remediation:
Implement safeguards that protect users from liquidation during operational pauses or interruptions.
Id:
SOL-Defi-Lending-5
Description:
Pausing liquidations can increase the solvency risk and lead to unpredictable behaviors upon resumption.
Remediation:
Outline clear protocols for pausing and resuming liquidations, ensuring solvency is maintained.
Id:
SOL-Defi-Lending-6
Description:
Lenders must be prevented from griefing via front-running the liquidation.
Remediation:
Ensure it is not possible to prevent liquidators by any means.
Id:
SOL-Defi-Lending-7
Description:
Without proper incentives, small positions might be overlooked, leading to inefficiencies.
Remediation:
Ensure a balanced incentive structure that motivates liquidators to address positions of all sizes.
Id:
SOL-Defi-Lending-8
Description:
Omitting interest in LTV calculations can result in inaccurate credit assessments.
Remediation:
Include accrued interest in LTV calculations to maintain accurate and fair credit evaluations.
References:
#1
Id:
SOL-Defi-Lending-9
Description:
Protocols might need to ensure that liquidation and repaying mechanisms are either both active or inactive to maintain consistency.
Remediation:
Review protocol logic to allow or disallow liquidation and repaying functions collectively to avoid operational discrepancies.
References:
#1
Id:
SOL-Defi-Lending-10
Description:
Protocols that allow the same token to be lent and borrowed in a single transaction may be vulnerable to attacks that exploit rapid price inflation or flash loans to manipulate the system.
Remediation:
Protocols should implement constraints to prohibit the same token from being used in a lend and borrow action within the same block or transaction, reducing the risk of flash-loan attacks and other manipulative practices.
Id:
SOL-Defi-Lending-11
Description:
Discrepancies in liquidation returns can discourage liquidators and impact system stability.
Remediation:
Ensure a clear and consistent calculation mechanism for liquidation rewards.
Id:
SOL-Defi-Lending-12
Description:
Certain scenarios or conditions might prevent a user from repaying their loan, causing them to be perpetually in debt. This can be due to factors such as excessive collateralization, high fees, fluctuating token values, or other unforeseen events.
Remediation:
Review the lending protocol's logic to ensure there are no conditions that could trap a user in perpetual debt. Implement safeguards to notify or protect users from taking actions that may lead to irrecoverable financial situations.
Id:
SOL-Defi-LSD-1
Description:
A malicious Ethereum validator can betray a liquid staking protocol by front-running to first call `DepositContract::deposit` sending 1 ETH and passing their own withdrawal credentials; after the protocol's subsequent call succeeds the withdrawal credentials are not overwritten since only the "initial deposit" sets the withdrawals credentials while the second deposit is treated as a "top-up deposit". The malicious validator now controls 33 ether with 32 ether belonging to the protocol's users and has set their own withdrawal credentials instead of the protocol's withdrawal credentials.
Remediation:
The function which calls `DepositContract::deposit` should take as input `DepositContract.get_deposit_root` then check that the input deposit root matches the current one. This works as the current deposit root changes with every deposit.
Id:
SOL-Defi-LSD-2
Description:
Liquid staking protocols typically have their own liquid ERC20 token that accrues value against ETH as the protocol receives staking rewards; in the normal course of operations the exchange rate should continually be increasing as the protocol accrues rewards such that the protocol's ERC20 token can be exchanged for increasing amounts of ETH. If the protocol allows instant withdrawals, an attacker can perform a risk-free sandwich attack to drain ETH from the protocol by 1) front-running the exchange rate txn to deposit a large amount of ETH, 2) back-running to withdraw at the increased rate.
Remediation:
Don't allow instant withdrawals but use a withdrawal queue and run the repricing transaction through flashbots.
Id:
SOL-Defi-LSD-3
Description:
Re-entrancy vulnerabilties can often exist in the reward or withdrawal code of LSD protocols.
Remediation:
Always follow the Checks-Effects-Interactions pattern; sending ETH or minting NFTs via `_safeMint` should always happen after storage updates.
Id:
SOL-Defi-LSD-4
Description:
If an arbitrary exchange rate can be set when processing queued withdrawals this creates a subtle rug-pull vector of user withdrawals.
Remediation:
When withdrawals are processed the current exchange rate should be retrieved in the same way as when withdrawals are created.
Id:
SOL-Defi-LSD-5
Description:
LSD protocols often implement pausing of different functionality. Auditors should check if there are any gaps where for example one function is missing a pause check that other related functions contain.
Remediation:
All related functions should contain the same related pause checks.
Id:
SOL-Defi-LSD-6
Description:
To reduce the gas cost of reading from storage, protocols may use multiple inter-related data structures to store complex information like operator and validator information. Auditors should examine whether functions which update these inter-related data structures can be used to corrupt them by over-writing records which contain indexes into to another storage location.
Remediation:
Protocols can use invariant fuzz testing with invariants which validate that relationships between inter-related data structures can't be broken by functions which update them.
Id:
SOL-Defi-LSD-7
Description:
LSD protocols may need to iterate over the entire set of operators or validators which can become exorbitantly expensive or lead to out of gas if the operator or validator set becomes large. In permissionless systems where anyone can create operators or validators this creates a denial of service attack vector.
Remediation:
Refactor to avoid needing to iterate over the entire operator/validator set. Alternatively only use a small and trusted set of operators/validators.
Id:
SOL-Defi-LSD-8
Description:
LSD protocols may use an external Proof of Reserves Oracle to fetch off-chain data for their current ETH reserves. If the protocol doesn't check how long ago the data was last updated it can process stale data as if it were fresh.
Remediation:
Check the time data was last updated against the Oracle's heartbeat and revert if the data is too old.
Id:
SOL-Defi-LSD-9
Description:
Mathematical calculations have to be performed in LSD protocol deposit, withdrawal and reward functions. Auditors should check for precision loss issues such as division before multiplication, rounding down to zero etc.
Remediation:
Don't perform division before multiplication, be aware of rounding down to zero, rounding direction, unsafe casting etc.
Id:
SOL-Defi-Oracle-1
Description:
Usage of deprecated Chainlink functions like latestAnswer() might return stale or incorrect data, affecting the integrity of smart contracts.
Remediation:
Replace deprecated functions with the current recommended methods to ensure accurate data retrieval from oracles.
References:
#1
Id:
SOL-Defi-Oracle-2
Description:
Price feed might return zero and this must be handled as invalid.
Remediation:
Ensure the returned price is not zero.
Id:
SOL-Defi-Oracle-3
Description:
Price feeds might not be supported in the future. To ensure accurate price usage, it's vital to regularly check the last update timestamp against a predefined delay.
Remediation:
Implement a mechanism to check the heartbeat of the price feed and compare it against a predefined maximum delay (`MAX_DELAY`). Adjust the `MAX_DELAY` variable based on the observed heartbeat.
Id:
SOL-Defi-Oracle-4
Description:
The rollup sequencer can become offline, which can lead to potential vulnerabilities due to stale price.
Remediation:
Utilize the sequencer uptime feed to confirm the sequencers are up.
References:
#1
Id:
SOL-Defi-Oracle-5
Description:
An inadequately set TWAP (Time-Weighted Average Price) period could be exploited to manipulate prices.
Remediation:
Adjust the TWAP period to a duration that mitigates the risk of manipulation while providing timely price updates.
References:
#1
Id:
SOL-Defi-Oracle-6
Description:
In multi-chain deployments, it's crucial to ensure the desired price feed pair is available and consistent across all chains.
Remediation:
Review the supported price feed pairs on all chains and ensure they are consistent.
Id:
SOL-Defi-Oracle-7
Description:
A price feed heartbeat that's too slow might not be suitable for some use cases.
Remediation:
Assess the requirements of the use case and ensure the price feed heartbeat aligns with them.
Id:
SOL-Defi-Oracle-8
Description:
Different price feeds might have varying decimal precisions, which can lead to inaccuracies.
Remediation:
Ensure that the contract handles potential variations in decimal precision across different price feeds.
Id:
SOL-Defi-Oracle-9
Description:
Hard-coded price feed addresses can be problematic, especially if they become deprecated or if they're not accurate in the first place.
Remediation:
Review and verify the hardcoded price feed addresses. Consider mechanisms to update the address if required in the future.
Id:
SOL-Defi-Oracle-10
Description:
Oracle price updates can be front-run and cause various problems.
Remediation:
Ensure the protocol is not affected in the case where oracle price updates are front-run.
References:
#1
Id:
SOL-Defi-Oracle-11
Description:
Unanticipated oracle reverts can lead to Denial-Of-Service.
Remediation:
Implement try/catch blocks around oracle calls and have alternative strategies ready.
Id:
SOL-Defi-Oracle-12
Description:
Using an ETH price feed for stETH or a BTC price feed for WBTC can introduce risks associated with the underlying assets deviating from their pegs.
Remediation:
Ensure that the price feeds accurately represent the underlying assets to address potential depeg risks.
Id:
SOL-Defi-Oracle-13
Description:
Reliance on AMM spot prices as oracles can be manipulated via flashloan.
Remediation:
Choose reliable and tamper-resistant oracle sources. Avoid using spot prices from AMMs directly without additional checks.
Id:
SOL-Defi-Oracle-14
Description:
During flash crashes, oracles might return inaccurate prices.
Remediation:
Implement checks to ensure that the price returned by the oracle lies within an expected range to guard against potential flash crash vulnerabilities.
Id:
SOL-Defi-Staking-1
Description:
If users can amplify time locks for others by stacking tokens, it may lead to unintended lock durations and potentially be exploited.
Remediation:
Implement strict checks and controls to prevent users from influencing the time locks of other users through token stacking.
Id:
SOL-Defi-Staking-2
Description:
Manipulation in the timing of reward distribution can adversely affect users and the protocol's intended incentives.
Remediation:
Implement time controls and constraints on reward distributions to maintain the protocol's intended behavior.
Id:
SOL-Defi-Staking-3
Description:
The staking protocol often has a function to update the rewards (e.g. `updateRewards`) and sometimes it is used as a modifier. This update function MUST be called before all relevant operations.
Remediation:
Ensure the update reward function is called properly in all places where the reward is relevant.
Id:
SOL-EC-1
Description:
Reentrant calls to different functions can unpredictably alter contract states. Note that view functions should be checked as well to prevent the Readonly Reentrancy.
Remediation:
Ensure the contract state is maintained reasonably during the external interactions.
References:
#1
#2
Id:
SOL-EC-2
Description:
Mismanagement of `msg.value` across multiple calls can lead to vulnerabilities.
Remediation:
Do not use ETH in multicall.
References:
#1
Id:
SOL-EC-3
Description:
A delegatecall is a low-level function call that delegates the execution of a function in another contract while maintaining the original contract's context. It can lead to critical vulnerabilities if the destination address is not secure or can be altered by an unauthorized party.
Remediation:
Use delegatecall only with trusted contracts, and ensure that the address to be delegated to is not changeable by unauthorized users. Implement strong access controls and audit the code for potential security issues before deployment.
Id:
SOL-EC-4
Description:
Unnecessary external calls can introduce vulnerabilities.
Remediation:
Evaluate and eliminate non-essential external contract calls.
Id:
SOL-EC-5
Description:
Calling untrusted addresses can lead to malicious actions.
Remediation:
Ensure that only whitelisted or trusted contract addresses are called.
References:
#1
#2
Id:
SOL-EC-6
Description:
Specifying fixed gas amounts can lead to out-of-gas vulnerabilities.
Remediation:
Use dynamic gas estimation or ensure sufficient gas is available before the call.
References:
#1
#2
Id:
SOL-EC-7
Description:
Calls that consume all available gas can halt subsequent actions.
Remediation:
Ensure enough gas is reserved for post-call tasks or use dynamic gas estimation.
References:
#1
#2
Id:
SOL-EC-8
Description:
Large data passed to untrusted addresses may be exploited for griefing.
Remediation:
Limit data passed or employ inline assembly to manage data transfer.
References:
#1
Id:
SOL-EC-9
Description:
External calls returning vast data can deplete available gas.
Remediation:
Limit or verify data size returned from external sources.
Id:
SOL-EC-10
Description:
Non-library delegate calls can alter the state of the calling contract.
Remediation:
Thoroughly review and verify such delegate calls so that the delegate calls do not change the caller's state unexpectedly.
Id:
SOL-EC-11
Description:
Delegate calls grant the called contract the context of the caller, risking state alterations.
Remediation:
Restrict delegate calls to only trusted, reviewed, and audited contracts.
References:
#1
Id:
SOL-EC-12
Description:
Calling non-existent addresses can lead to unintended behaviors. Low level calls (call, delegate call and static call) return success if the called contract doesn't exist (not deployed or destructed)
Remediation:
Verify the existence of an address before making a call.
References:
#1
#2
#3
#4
#5
#6
Id:
SOL-EC-13
Description:
The check-effect-interaction pattern prevents reentrancy attacks.
Remediation:
Adhere to the CEI pattern and use `reentrancyGuard` judiciously.
References:
#1
#2
#3
Id:
SOL-EC-14
Description:
On interacting with external contracts, the caller becomes a new `msg.sender` instead of the original caller.
Remediation:
Ensure the validation is in place to check the actor is handled correctly.
References:
#1
#2
Id:
SOL-HMT-1
Description:
When using a merkle tree, the new proof is calculated at a certain time and there exists a period of time between when the proof is generated and the proof is published.
Remediation:
Ensure that front-running the merkle proof setting does not affect the protocol.
Id:
SOL-HMT-2
Description:
Validation of `msg.sender` is critical in the use of Merkle tree.
Remediation:
Ensure that the `msg.sender` is actually the same address included in the leave.
Id:
SOL-HMT-3
Description:
Passing the zero hash can lead to unintended behaviors or vulnerabilities if not properly handled.
Remediation:
Implement checks to handle zero hash values appropriately and prevent potential misuse.
Id:
SOL-HMT-4
Description:
Duplicate proofs within a Merkle tree can lead to double-spending or other vulnerabilities.
Remediation:
Ensure the Merkle tree construction and verification process detects and prevents the use of duplicate proofs.
Id:
SOL-HMT-5
Description:
Not including claimable addresses when hashing leaves can let an attacker to claim.
Remediation:
Ensure that the Merkle tree construction includes the hashing of claimable addresses within the leaves.
Id:
SOL-Heuristics-1
Description:
Inconsistent implementations of the same logic can introduce errors or vulnerabilities.
Remediation:
Standardize the logic and make it as a separate function.
Id:
SOL-Heuristics-2
Description:
If a variable of nested structure is deleted, only the top-level fields are reset by default values (zero) and the nested level fields are not reset.
Remediation:
Always ensure that inner fields are deleted before the outer fields of the structure.
Id:
SOL-Heuristics-3
Description:
Overlooking the possibility of a sender and a recipient (source and destination) being the same in smart contracts can lead to unintended problems.
Remediation:
Ensure the protocol behaves as expected when `src==dst`.
Id:
SOL-Heuristics-4
Description:
The order of modifiers can influence the behavior of a function. Generally, NonReentrant must come first than other modifiers.
Remediation:
Reorder modifiers so that NonReentrant is placed before other modifiers.
Id:
SOL-Heuristics-5
Description:
A `try/catch` block without adequate gas can fail, leading to unexpected behaviors.
Remediation:
Ensure sufficient gas is supplied when using the `try/catch` block.
References:
#1
Id:
SOL-Heuristics-6
Description:
Incomplete or incorrect implementation of EIP recommendations can lead to vulnerabilities.
Remediation:
Read the recommendations and security concerns and ensure all are implemented as per the official recommendations.
Id:
SOL-Heuristics-7
Description:
Off-by-one errors are not rare. Is `<=` correct in this context or should `<` be used? Should a variable be set to the length of a list or the length - 1? Should an iteration start at 1 or 0?
Remediation:
Review all usages of comparison operators for correctness.
Id:
SOL-Heuristics-8
Description:
Logical operators like `==`, `!=`, `&&`, `||`, `!` can be overlooked especially when the test coverage is not good.
Remediation:
Review all usages of logical operators for correctness.
Id:
SOL-Heuristics-9
Description:
Supplying unexpected addresses can lead to unintended behaviors, especially if the address points to another contract inside the same protocol.
Remediation:
Implement checks to validate receiver addresses and ensure the protocol behaves as expected.
Id:
SOL-Heuristics-10
Description:
While minor rounding errors can be inevitable in certain operations, they can pose significant issues if they can be magnified. Amplification can occur when a function is invoked multiple times strategically or under specific conditions.
Remediation:
Conduct thorough tests to identify and understand potential rounding errors. Ensure that they cannot be amplified to a level that would be detrimental to the system or its users. In cases where significant rounding errors are detected, the implementation should be revised to minimize or eliminate them.
References:
#1
Id:
SOL-Heuristics-11
Description:
Checking a variable against its default value might be used to detect initialization. If such defaults can also be valid state, it could lead to vulnerabilities.
Remediation:
Avoid solely relying on default values to determine initialization status.
Id:
SOL-Heuristics-12
Description:
Functions that should be unique per parameters set might be callable multiple times, leading to potential issues.
Remediation:
Ensure functions have measures to prevent repeated calls with identical or similar parameters, especially when these calls can produce adverse effects.
Id:
SOL-Heuristics-13
Description:
While working with a `memory` copy for optimization, developers might overlook updating the global state.
Remediation:
Always ensure the global state mirrors changes made in `memory`. Consider tools or extensions that can highlight discrepancies.
Id:
SOL-Heuristics-14
Description:
Contracts might have special logic for ETH, like wrapping to WETH. Assuming exclusivity between handling ETH and WETH without checks can introduce errors.
Remediation:
Clearly differentiate the logic between ETH and WETH handling, ensuring no overlap or mutual exclusivity assumptions without validation.
Id:
SOL-Heuristics-15
Description:
Data on the blockchain, including that marked 'private' in smart contracts, is visible to anyone who knows how to query the blockchain's state or analyze its transaction history. Private variables are not exempt from public inspection.
Remediation:
Sensitive data should either be kept off-chain or encrypted before being stored on-chain. It's important to manage encryption keys securely and ensure that on-chain data does not expose private information even when encrypted, if the encryption method is weak or the keys are mishandled.
Id:
SOL-Heuristics-16
Description:
In many projects, there should be some symmetries for different functions. For instance, a `withdraw` function should (usually) undo all the state changes of a `deposit` function and a `delete` function should undo all the state changes of the corresponding `add` function. Asymmetries in these function pairs (e.g., forgetting to unset a field or to subtract from a value) can often lead to undesired behavior. Sometimes one side of a 'pair' is missing, like missing removing from a whitelist while there is a function to add to a whitelist.
Remediation:
Review paired functions for symmetry and ensure they counteract each other's state changes appropriately.
References:
#1
Id:
SOL-Heuristics-17
Description:
Associative properties of certain financial operations suggest that performing the operation multiple times with smaller amounts should yield an equivalent outcome as performing it once with the aggregate amount. Variations might be indicative of potential issues such as rounding errors, unintended fee accumulations, or other inconsistencies.
Remediation:
Implement tests to validate consistency. Where discrepancies exist, ensure they are intentional, minimal, and well-documented. If discrepancies are unintended, reevaluate the implementation to ensure precision and correctness.
Id:
SOL-Integrations-AC-1
Description:
The absence of the `underlying()` function in the cETH token contract can cause integration issues.
Remediation:
Double check the protocol works as expected when integrating cETH token.
Id:
SOL-Integrations-AC-2
Description:
A high utilization rate can potentially mean that there aren't enough assets in the pool to allow users to withdraw their collateral.
Remediation:
Ensure that there are mechanisms to handle user withdrawal when the utilization rate is high.
Id:
SOL-Integrations-AC-3
Description:
If the AAVE protocol is paused, the protocol can not interact with it.
Remediation:
Ensure the protocol behaves as expected when the AAVE protocol is paused.
Id:
SOL-Integrations-AC-4
Description:
Pools can be deprecated.
Remediation:
Ensure the protocol behaves as expected when the Pools are paused.
Id:
SOL-Integrations-AC-5
Description:
Lending and borrowing assets within the same eMode category might have rules or limitations.
Remediation:
Ensure the protocol behaves as expected when interacting with assets in the same eMode category.
Id:
SOL-Integrations-AC-6
Description:
Flash loans can influence the pool index (a maximum of 180 flashloans can be performed within a block).
Remediation:
Implement mechanisms to manage the effects of flash loans on the pool index.
Id:
SOL-Integrations-AC-7
Description:
Misimplementation of reward claims can lead to users not receiving their correct rewards.
Remediation:
Ensure a proper and tested implementation of AAVE/COMP reward claims.
Id:
SOL-Integrations-AC-8
Description:
Reaching the maximum debt on an isolated asset can result in denial-of-service or other limitations on user actions.
Remediation:
Ensure that the protocol works as expected when a user reaches the maximum debt.
Id:
SOL-Integrations-AC-9
Description:
Borrowing a siloed asset on Aave will prohibit users from borrowing other assets.
Remediation:
Make use of `getSiloedBorrowing(address asset)` to prevent unexpected problems.
References:
#1
Id:
SOL-Integrations-Balancer-1
Description:
Balancer vault does not charge any fees for flash loans at the moment. However, it is possible Balancer implements fees for flash loans in the future.
Remediation:
Ensure the protocol repays the fee together with the original debt on repayment in the `receiveFlashLoan` function.
References:
#1
Id:
SOL-Integrations-Balancer-2
Description:
The price will only be updated whenever a transaction (e.g. swap) within the Balancer pool is triggered. Due to the lack of updates, the price provided by Balancer Oracle will not reflect the true value of the assets.
Remediation:
Do not use the Balancer's oracle for any pricing.
References:
#1
Id:
SOL-Integrations-Balancer-3
Description:
Balancer's Boosted Pool uses Phantom BPT where all pool tokens are minted at the time of pool creation and are held by the pool itself. Therefore, virtualSupply should be used instead of totalSupply to determine the amount of BPT supply in circulation.
Remediation:
Ensure the protocol uses the correct function to get the total BPT supply in circulation.
References:
#1
Id:
SOL-Integrations-Balancer-4
Description:
Balancer vault does not charge any fees for flash loans at the moment. However, it is possible Balancer implements fees for flash loans in the future.
Remediation:
Balancer pools are susceptible to manipulation of their external queries, and all integrations must now take an extra step of precaution when consuming data. Via readonly reentrancy, an attacker can force token balances and BPT supply to be out of sync, creating very inaccurate BPT prices.
References:
#1
Id:
SOL-Integrations-Chainlink-VRF-1
Description:
If the parameters are not thoroughly verified when Chainlink VRF is called, the `fullfillRandomWord` function will not revert but return an incorrect value.
Remediation:
Ensure that all parameters passed to Chainlink VRF are verified to ensure the correct operation of `fullfillRandomWord`.
Id:
SOL-Integrations-Chainlink-VRF-2
Description:
Chainlink VRF can go into a pending state if there's insufficient LINK in the subscription. Once the subscription is refilled, the transaction can potentially be frontrun, introducing vulnerabilities.
Remediation:
Ensure the pending subscription does not affect the protocol's functionality.
Id:
SOL-Integrations-Chainlink-VRF-3
Description:
Not choosing a high enough request confirmation number can pose risks, especially in the context of chain re-orgs.
Remediation:
Evaluate the chain's vulnerability to re-orgs and adjust the request confirmation number accordingly.
References:
#1
Id:
SOL-Integrations-Chainlink-VRF-4
Description:
VRF calls can be frontrun and it's crucial to ensure that the user interactions are closed before the VRF call to prevent this.
Remediation:
Ensure the implementation closes the user interaction phase before initiating the VRF call.
Id:
SOL-Integrations-GS-1
Description:
Failing to execute the Guard's hooks (`checkTransaction()`, `checkAfterExecution()`) can bypass critical security checks implemented in those hooks.
Remediation:
Ensure that all modules correctly execute the Guard's hooks as intended.
Id:
SOL-Integrations-GS-2
Description:
If the nonce is not incremented in `execTransactionFromModule()`, it can cause issues when relying on it for signatures.
Remediation:
Ensure increase nonce inside the function `execTransactionFromModule()`.
Id:
SOL-Integrations-LayerZero-1
Description:
It's crucial that the `_debitFrom` function verifies whether the specified owner is the actual owner of the tokenId and if the sender has the correct permissions to transfer the token.
Remediation:
Ensure thorough checks and validations are performed in the `_debitFrom` function to maintain token security.
References:
#1
Id:
SOL-Integrations-LayerZero-2
Description:
Using blocking mechanism can potentially lead to a Denial-of-Service (DoS) attack.
Remediation:
Consider using non-blocking mechanism to prevent potential DoS attacks.
References:
#1
Id:
SOL-Integrations-LayerZero-3
Description:
Inaccurate gas estimation can result in cross-chain message failures.
Remediation:
Implement mechanisms to estimate gas accurately.
Id:
SOL-Integrations-LayerZero-4
Description:
When inheriting LzApp, direct calls to `lzEndpoint.send` can introduce vulnerabilities. Using `_lzSend` is the recommended approach.
Remediation:
Ensure that the `_lzSend` function is used instead of making direct calls to `lzEndpoint.send`.
Id:
SOL-Integrations-LayerZero-5
Description:
The User Application should include the `forceResumeReceive` function to handle unexpected scenarios and unblock the message queue when needed.
Remediation:
Implement the `ILayerZeroUserApplicationConfig` interface and ensure that the `forceResumeReceive` function is present and functional.
Id:
SOL-Integrations-LayerZero-6
Description:
Default configuration contracts are upgradeable by the LayerZero team.
Remediation:
Configure the applications uniquely and avoid using default settings.
Id:
SOL-Integrations-LayerZero-7
Description:
Choosing an inappropriate number of confirmations can introduce risks, especially considering past reorg events on the chain.
Remediation:
Evaluate the chain's history and potential vulnerabilities to determine the optimal number of confirmations.
Id:
SOL-Integrations-Uniswap-1
Description:
ON-chain slippage calculation can be manipulated.
Remediation:
Allow users to specify the slippage parameter in the actual asset amount which was calculated off-chain.
References:
#1
Id:
SOL-Integrations-Uniswap-2
Description:
In case of failed or partially filled orders, the protocol must issue refunds to the users.
Remediation:
Implement a refund mechanism to handle failed or partially filled swaps.
Id:
SOL-Integrations-Uniswap-3
Description:
The order of `token0` and `token1` in AMM pools may vary depending on the chain, which can lead to inconsistencies.
Remediation:
Always verify the order of tokens when interacting with different chains to avoid potential issues.
Id:
SOL-Integrations-Uniswap-4
Description:
Missing verification on the interacting pools can introduce risks.
Remediation:
Ensure pools are whitelisted or verify the pool's factory address before any interactions.
Id:
SOL-Integrations-Uniswap-5
Description:
Relying on pool reserves can be risky, as they can be manipulated, especially using a flashloan.
Remediation:
Implement alternative methods or checks without relying solely on pool reserves.
Id:
SOL-Integrations-Uniswap-6
Description:
Directly using `pool.swap()` can bypass certain security mechanisms.
Remediation:
Always use the Router contract to handle swaps, providing an added layer of security and standardization.
Id:
SOL-Integrations-Uniswap-7
Description:
Uniswap's TickMath and FullMath libraries require careful usage of `unchecked` due to solidity version specifics.
Remediation:
Review and test the use of `unchecked` in contracts utilizing Uniswap's math libraries to ensure safety and correctness.
References:
#1
Id:
SOL-Integrations-Uniswap-8
Description:
Enforcing slippage parameters for intermediate swaps but not the final step can result in users receiving less tokens than their specified minimum
Remediation:
Enforce slippage parameter as the last step before transferring funds to users
References:
#1
Id:
SOL-Integrations-Uniswap-9
Description:
`pool.slot0` can be easily manipulated via flash loans to sandwich attack users.
Remediation:
Use UniswapV3 TWAP or Chainlink Price Oracle.
References:
#1
#2
#3
Id:
SOL-Integrations-Uniswap-10
Description:
In UniswapV3 liquidity can be spread across multiple fee tiers. If a function which initiates a uni v3 swap hard-codes the fee tier parameter, this can have several negative effects.
Remediation:
Functions allowing users to perform uni v3 swaps should allow users to pass in the fee tier parameter.
References:
#1
Id:
SOL-LL-1
Description:
In low-level, data size is not checked by default and it can affect the unintended memory locations.
Remediation:
Validate that inputs do not exceed the size of it's expected type and either revert or clean the unused bits depending on your use case before using that value.
References:
#1
Id:
SOL-LL-2
Description:
It is expected to revert if there is no matching function signature in the contract. Overlooking this can let the execution continue into other parts of the unintended bytecode.
Remediation:
Ensure that the code reverts after comparing all supported function signatures, fallback etc and not matching any.
References:
#1
Id:
SOL-LL-3
Description:
Calling an address without code is always successful.
Remediation:
Ensure that addresses being called, static-called or delegate-called have code deployed.
References:
#1
Id:
SOL-LL-4
Description:
When calling precompiled code, the call is still successful on error or ”failure”. A failed precompile call simply has a return data size of 0.
Remediation:
Check the return data size not the success of the call to determine if it failed.
References:
#1
Id:
SOL-LL-5
Description:
At the evm level and in yul/inline assembly, when dividing or modulo'ing by 0, It does not revert with Panic(18) as solidity would do, its result 0. If this behavior is not desired it should be checked. Basically, x / 0 = 0 and x % 0 = 0.
Remediation:
Check if the denominator is zero before division.
References:
#1
Id:
SOL-McCc-1
Description:
Block time can vary across different chains, leading to potential timing discrepancies.
Remediation:
Avoid hardcoding time values based on block numbers.
Id:
SOL-McCc-2
Description:
Understanding the differences between chains is vital for ensuring compatibility and preventing unexpected behaviors.
Remediation:
Regularly check for chain differences and update the protocol accordingly.
References:
#1
#2
Id:
SOL-McCc-3
Description:
Incompatibility can arise when the protocol uses EVM operations not supported on certain chains.
Remediation:
Review and ensure compatibility for chains like Arbitrum and Optimism.
References:
#1
#2
Id:
SOL-McCc-4
Description:
Different chains might interpret these values differently, leading to unexpected behaviors.
Remediation:
Test and verify the behavior on all targeted chains.
References:
#1
Id:
SOL-McCc-5
Description:
Some attacks become viable with low gas costs or when a large number of transactions can be processed.
Remediation:
Evaluate and mitigate potential attack vectors associated with gas fees.
References:
#1
Id:
SOL-McCc-6
Description:
Decimals in ERC20 tokens can differ across chains.
Remediation:
Ensure consistent ERC20 decimals or implement chain-specific adjustments.
References:
#1
Id:
SOL-McCc-7
Description:
Contracts may have different upgradability properties depending on the chain, like USDT being upgradable on Polygon but not on Ethereum.
Remediation:
Verify and document upgradability characteristics for each chain.
Id:
SOL-McCc-8
Description:
Cross-chain messaging requires robust security checks to ensure the correct permissions and intended functionality.
Remediation:
Double check the access control over cross-chain messaging components.
Id:
SOL-McCc-9
Description:
Allowing messages from an unsupported chain can lead to unpredictable results.
Remediation:
Implement a whitelist to prevent messages from unsupported chains.
Id:
SOL-McCc-10
Description:
zkSync Era might have specific requirements or differences when compared to standard Ethereum deployments.
Remediation:
Review and ensure compatibility before deploying contracts to zkSync Era.
References:
#1
Id:
SOL-McCc-11
Description:
Inconsistent block production can lead to unexpected application behaviors.
Remediation:
Develop with the assumption that block production may not always be consistent.
Id:
SOL-McCc-12
Description:
`PUSH0` might not be supported on all chains, leading to potential incompatibility issues.
Remediation:
Ensure if `PUSH0` is supported in the target chain.
References:
#1
Id:
SOL-Signature-1
Description:
Lacking protection mechanisms like `nonce` and `block.chainid` can make signatures vulnerable to replay attacks. Also, EIP-712 provides a standard for creating typed and structured data to be signed, ensuring better security and user experience.
Remediation:
Implement a `nonce` system and incorporate `block.chainid` in your signature scheme. Ensure adherence to EIP-712 for all signatures.
Id:
SOL-Signature-2
Description:
Signature malleability can be exploited by attackers to produce valid signatures without the private key. Using outdated versions of libraries can introduce known vulnerabilities.
Remediation:
Avoid using `ecrecover()` for signature verification. Instead, utilize the OpenZeppelin's latest version of ECDSA to ensure signatures are safe from malleability issues.
Id:
SOL-Signature-3
Description:
Mismatched public keys can indicate an incorrect or malicious signer, potentially leading to unauthorized actions.
Remediation:
Implement rigorous checks to ensure the public key derived from a signature matches the expected signer's public key.
Id:
SOL-Signature-4
Description:
If signatures aren't properly checked, malicious actors might exploit them, leading to unauthorized transactions or actions.
Remediation:
Ensure strict verification mechanisms are in place to confirm that signatures originate from the expected entities.
Id:
SOL-Signature-5
Description:
Signatures with expiration dates that aren't checked can be reused maliciously after they should no longer be valid.
Remediation:
Always check the expiration date of signatures and ensure they're not accepted past their valid period.
Id:
SOL-Timelock-1
Description:
Immediate changes in the protocol can affect the users.
Remediation:
Implement timelocks for important changes, allowing users adequate time to respond to proposed alterations.
Id:
SOL-Token-FE-1
Description:
Not all ERC20 tokens are compliant to the EIP20 standard. Some do not return boolean flag, some do not revert on failure.
Remediation:
Use OpenZeppelin's SafeERC20 where the safeTransfer and safeTransferFrom functions handle the return value check as well as non-standard-compliant tokens.
Id:
SOL-Token-FE-2
Description:
Race condition for approvals can cause an unexpected loss of funds to the signer.
Remediation:
Use OpenZeppelin's safeIncreaseAllowance and safeDecreaseAllowance functions.
References:
#1
Id:
SOL-Token-FE-3
Description:
Different decimals in ERC20 tokens can cause incorrect calculations or interpretations.
Remediation:
Always check and handle the decimals of ERC20 tokens to prevent potential issues.
Id:
SOL-Token-FE-4
Description:
Tokens that have address checks can lead to various problems.
Remediation:
Ensure the token's own blacklisting mechanism does not affect the protocol's functionality.
Id:
SOL-Token-FE-5
Description:
Some tokens have multiple addresses and this can introduce vulnerabilities.
Remediation:
Do not rely on the token address in the accounting.
Id:
SOL-Token-FE-6
Description:
Some tokens charge fee on transfer and the receiver gets less amount than specified.
Remediation:
If the protocol intends to support this kind of token, ensure the accounting logic is correct.
Id:
SOL-Token-FE-7
Description:
ERC777 tokens have hooks that execute code before and after transfers, which might lead to reentrancy.
Remediation:
Be cautious when integrating with ERC777 and be aware of the hook implications.
Id:
SOL-Token-FE-8
Description:
Solmate `ERC20.safeTransferLib` do not check the contract existence and this opens up a possibility for a honeypot attack.
Remediation:
Use OpenZeppelin's SafeERC20.
References:
#1
Id:
SOL-Token-FE-9
Description:
Flash mints can drastically increase token supply temporarily, leading to potential abuse.
Remediation:
Implement strict controls and checks around any flash mint functionality.
Id:
SOL-Token-FE-10
Description:
Some tokens revert on transfer of zero amount and can cause issues in certain integrations and operations.
Remediation:
Transfer only when the amount is positive.
Id:
SOL-Token-FE-11
Description:
Missing `DOMAIN_SEPARATOR()` can lead to vulnerabilities in the ERC2612 permit functionality.
Remediation:
Ensure complete and correct implementation of ERC2612, including the `DOMAIN_SEPARATOR()` function.
Id:
SOL-Token-FE-12
Description:
Certain addresses might be blocked or restricted to receive tokens (e.g. LUSD).
Remediation:
Ensure the receiver blacklisting does not affect the protocol's functionality.
Id:
SOL-Token-FE-13
Description:
Some ERC20 tokens do not work when changing the allowance from an existing non-zero allowance value. For example Tether (USDT)'s approve() function will revert if the current approval is not zero, to protect against front-running changes of approvals.
Remediation:
Set the allowance to zero before increasing the allowance and use safeApprove/safeIncreaseAllowance.
References:
#1
Id:
SOL-Token-FE-14
Description:
Some tokens don't support approve `type(uint256).max` amount and revert.
Remediation:
Avoid approval of `type(uint256).max`.
References:
#1
Id:
SOL-Token-FE-15
Description:
Some ERC20 tokens can be paused by the contract owner.
Remediation:
Ensure the protocol is not affected when the token is paused.
Id:
SOL-Token-FE-16
Description:
Allowance should not be decreased in a transferFrom() call if the sender is the same as the caller, to prevent incorrect balance and allowance tracking.
Remediation:
Ensure that the smart contract logic maintains correct allowance levels when transferFrom() involves the token owner themselves.
References:
#1
Id:
SOL-Token-NfE1-1
Description:
According to the ERC721 standard, a wallet/broker/auction application MUST implement the wallet interface if it will accept safe transfers. Use safe version of mint and transfer functions to prevent NFT being lost. (the similar applies to ERC1155)
Remediation:
Use OpenZeppelin's safe mint/transfer functions for ERC721/1155.
Id:
SOL-Token-NfE1-2
Description:
By standard, the token receiver contracts implement onERC721Received and onERC1155Received and this can potentially be a source of reentrancy attacks if not correctly handled.
Remediation:
Double check the potential reentrancy attack.
Id:
SOL-Token-NfE1-3
Description:
The `safeTransferFrom` functions in OpenZeppelin's ERC721 and ERC1155 can expose the contract to reentrancy attacks due to external calls to user addresses.
Remediation:
Use the checks-effects-interactions pattern and implement reentrancy guards to prevent potential reentrancy attacks when making external calls.
Id:
SOL-Token-NfE1-4
Description:
Most of the time the `from` parameter of `transferFrom()` should be `msg.sender`. Otherwise an attacker can take advantage of other user's approvals and steal.
Remediation:
Ensure that the contract verifies the `msg.sender` is actually the owner.
Id:
SOL-Token-NfE1-5
Description:
Contracts must properly implement the supportsInterface function to ensure they comply with ERC721/1155 standards and interoperate with other contracts correctly.
Remediation:
Implement the supportsInterface function to return true for ERC721 and ERC1155 token types, ensuring accurate reporting of supported features.
References:
#1
Id:
SOL-Token-NfE1-6
Description:
To facilitate broader compatibility and usage in various applications, contracts may need to support both ERC721 and ERC1155 token standards.
Remediation:
Use the supportsInterface method to check for and support interfaces of both ERC1155 and ERC721 within the same contract.
References:
#1
Id:
SOL-Token-NfE1-7
Description:
For many NFT collections, a kind of privilege is provided in various ways, e.g. airdrop. The NFT owner must be able to claim the benefits while they lock in protocols.
Remediation:
Ensure the NFT holders can claim all benefits.
References:
#1
Id:
SOL-Token-NfE1-8
Description:
CryptoPunks collections that do not support the `transferFrom()` function can present risks. The `offerPunkForSaleToAddress()` function in particular can be susceptible to front-running attacks, which can compromise the ownership and security of the token.
Remediation:
Ensure validation is done properly to prevent malicious actors claiming the ownership.
References:
#1
#2